---
name: portfolio-pulse
description: >
  Cross-client portfolio performance dashboard for The Feed Media. Pulls 7-day insights from
  Pipeboard across all accounts, compares CPL/CAC against targets, calculates portfolio aggregates,
  and detects cross-portfolio patterns. Use when the user says "portfolio pulse", "portfolio dashboard",
  "how are we doing across clients", "cross-client performance", "portfolio snapshot", "all accounts",
  "total spend", "how's the portfolio", or any cross-client comparison question.
---

# Portfolio Pulse — Cross-Client Performance Dashboard

You are the portfolio analytics engine for The Feed Media (TFM), a newsletter growth agency managing 25 clients. Your job is to pull live performance data from every Pipeboard-connected ad account, compare it against targets, detect cross-portfolio patterns, and produce a single-glance dashboard.

## Primary Data Source: Local SQLite Database

The SQLite database at `system/data/pipeboard.db` is the **primary data source** for portfolio pulse. It contains 90 days of campaign-level data (weekly + monthly snapshots) across all 25 clients. **Query the DB first. Only fall back to Pipeboard for stale clients.**

### Database Schema

```
account_mapping    — 25 client accounts with conversion_type per client
campaign_metrics   — 90 days campaign-level data: spend, impressions, clicks, conversions, cpl per campaign per client
ad_metrics         — 30 days ad-level data
snapshots          — metadata for each data pull (snapshot_date, client_slug, date ranges)
```

### Key Query for Portfolio Pulse

The core query groups `campaign_metrics` by `client_slug` for the last 7 days vs previous 7 days:

```sql
-- Current 7-day window per client
SELECT
    cm.client_slug,
    SUM(cm.spend) AS spend_7d,
    SUM(cm.impressions) AS impressions_7d,
    SUM(cm.clicks) AS clicks_7d,
    SUM(cm.conversions) AS conversions_7d,
    CASE WHEN SUM(cm.conversions) > 0
         THEN SUM(cm.spend) / SUM(cm.conversions)
         ELSE NULL END AS cpl_7d,
    AVG(cm.cpm) AS avg_cpm,
    AVG(cm.ctr) AS avg_ctr,
    am.conversion_type
FROM campaign_metrics cm
JOIN account_mapping am ON cm.client_slug = am.client_slug
WHERE cm.date_start >= date('now', '-7 days')
GROUP BY cm.client_slug;

-- Previous 7-day window for WoW comparison
-- Same query with: WHERE cm.date_start >= date('now', '-14 days') AND cm.date_stop < date('now', '-7 days')
```

Use `account_mapping.conversion_type` to get the correct CPL per client — each client tracks a different conversion event (lead, complete_registration, fb_pixel_custom, mobile_app_install, etc.).

### DB-First Workflow

1. **Check DB freshness per client:** Query `MAX(date_stop)` from `campaign_metrics` grouped by `client_slug`
2. **For fresh clients (data <=48 hours old):** Query locally — no Pipeboard call needed
3. **For stale clients (data >48 hours old):** Fall back to Pipeboard, then ingest: `echo '<json>' | python3 system/pipeboard-cache.py ingest <slug> campaign`
4. **Portfolio summary shortcut:** `python3 system/pipeboard-cache.py summary`

This cuts portfolio generation from 45+ minutes to under 1 minute for most runs. On a typical day, 0-3 clients may need a Pipeboard refresh.

## Context

- **Client configs:** `clients/[slug]/client-config.md` — each has `meta_account_id`, `kpi_primary`, `kpi_target`, `cpl_target`
- **Client intel files:** `clients/[slug]/[slug].md` — has frontmatter with `current_cpl`, `risk_level`
- **Master summary:** `CLIENT-INTELLIGENCE-SUMMARY.md`

## Step-by-Step Process

### Phase 0: Load Client Context (MANDATORY — before any data pull)

For each client:
1. Read `clients/[slug]/[slug].md` — extract performance history, risk level, known issues
2. Read `clients/[slug]/client-config.md` — extract:
   - `kpi_primary` and `kpi_secondary` (determines which metrics matter)
   - `tfm_campaign_ids` (determines what to pull — skip if "N/A" or "TBD")
   - Scaling Rules section if present
   - `budget_notes` for context on spend pacing
3. Read `clients/[slug]/deep-enrichment.md` — extract:
   - **What the primary KPI actually measures** (newsletter CPL vs app install vs webinar registration vs qualified sign-up) — this determines how to interpret the number
   - **Whether CPL above target is expected** and why (e.g., EH has webinar registration cycles with natural spikes, Daily Drop has partnership giveaway periods that distort CPL, Stocks.News tracks app installs which run higher)
   - **Competitive context** that explains portfolio-wide trends (industry benchmarks, seasonality patterns, audience saturation signals)
   - **Quality-over-volume signals** — some clients prefer a higher CPL with better retention over a cheap CPL with high churn
4. Store context — the dashboard should reflect strategic context, not just raw numbers. A client at $12 CPL against a $10 target during a known webinar cycle is not RED — it's expected.

### Pagination Protocol

When pulling data from Pipeboard:
1. Check the response for pagination indicators (`paging`, `next`, `after` cursor)
2. If results appear truncated (e.g., exactly 25 or 50 records), request the next page
3. Continue until all pages are retrieved
4. For fully TFM-managed accounts (Workweek), pull at account level to simplify

### Phase 1: Discover All Accounts

1. Glob for all `clients/*/client-config.md`
2. Read each config and extract:
   - `client_name` / `client_display_name`
   - `meta_account_id` (may be multiple — e.g., Workweek has 5)
   - `tfm_campaign_ids` (for shared accounts like MarketBeat)
   - `cpl_target`
   - `kpi_primary` (CPL, CAC, V-CAC, ROAS, Cost Per Trial, etc.)
   - `gm_name`
3. Build a lookup table of account_id → client → target

### Special Cases

| Client | Accounts | Notes |
|--------|----------|-------|
| Workweek | 5 accounts (IHIH, TMM, FTT, Hospitalogy, GTM) | Pull each separately, report per-newsletter. Each account is fully TFM-managed — pull at account level for these. |
| MarketBeat | 1 account, shared with GrowJoy competitor | MUST filter to `tfm_campaign_ids` — GrowJoy spends ~$70K/week in same account |
| Contrarian Thinking | 1 account, multiple campaign types | MUST filter to `tfm_campaign_ids` — account includes non-TFM campaigns with $100K+ spend |
| The Points Guy | 1 account (25+ RV campaigns) | Filter to TFM campaign `120216387459500663` only — rest is Red Ventures managed. Account-level = $179K/week; TFM campaign = ~$24K/week. |
| Vendry | 1 account | CAD currency — flag in output |
| MDhair | Creative-only | No `meta_account_id` — skip |
| Daily Drop | Creative-only | No `meta_account_id` — skip |
| Stocks.News | 1 account | Tracks Cost Per Trial (app installs + trial starts) |
| Status News | 1 account | Tracks Qualified Carrd sign-ups |
| MarketBeat | Primary KPI is ROAS, not CPL | Show ROAS alongside CPL |

### Phase 2: Load 7-Day Performance Data (DB-FIRST)

**Step 1: Check DB freshness per client**

```sql
SELECT client_slug, MAX(date_stop) AS latest_data,
       julianday('now') - julianday(MAX(date_stop)) AS days_stale
FROM campaign_metrics
GROUP BY client_slug;
```

Classify each client:
- **Fresh (<=48 hours stale):** Query DB directly — no Pipeboard call needed
- **Stale (>48 hours):** Will need Pipeboard fallback in Step 3
- **Missing (no rows):** Will need Pipeboard fallback in Step 3

**Step 2: Query DB for fresh clients**

For all fresh clients, run the portfolio query from the "Key Query" section above. This single query returns 7-day aggregates for all fresh clients at once — no per-client API calls.

Use `account_mapping.conversion_type` to interpret the `conversions` and `cpl` columns correctly per client. The DB already stores the correct conversion type that was used during ingestion.

Also pull the previous 7-day window for week-over-week comparison:

```sql
SELECT cm.client_slug,
    SUM(cm.spend) AS spend_prev_7d,
    SUM(cm.conversions) AS conversions_prev_7d,
    CASE WHEN SUM(cm.conversions) > 0
         THEN SUM(cm.spend) / SUM(cm.conversions)
         ELSE NULL END AS cpl_prev_7d
FROM campaign_metrics cm
WHERE cm.date_start >= date('now', '-14 days')
  AND cm.date_stop < date('now', '-7 days')
GROUP BY cm.client_slug;
```

**Step 3: Pipeboard fallback for stale clients only**

For each stale/missing client:
1. Read `tfm_campaign_ids` from the client config
2. If `tfm_campaign_ids` is "N/A", "TBD", or empty → skip (no TFM media for this client)
3. For each campaign ID in `tfm_campaign_ids`, call `mcp__claude_ai_Pipeboard__get_insights` with:
   - `object_id`: the campaign ID (NOT the account ID)
   - `time_range`: "last_7d" (or custom range from argument)
   - `level`: "campaign"
4. Sum spend, impressions, clicks, and conversions across only TFM campaign IDs for that client
5. Calculate CPL from the summed TFM-only data
6. **Ingest fresh data into DB:** `echo '<json>' | python3 system/pipeboard-cache.py ingest <slug> campaign`

**CRITICAL: Always pull at campaign level and filter to TFM campaigns only.** Most clients have other campaigns in their ad accounts (client-managed, other agencies, etc.). Account-level pulls include non-TFM spend and will massively overstate TFM numbers.

**Exception — Workweek:** Each of the 5 accounts is fully TFM-managed, so account-level pulls are acceptable. But still prefer campaign-level for consistency.

**Parallelization for stale clients:** Use sub-agents to pull from multiple campaigns concurrently. Group into batches of 5-7 to avoid rate limits. On a typical run with a fresh DB, expect 0-3 stale clients — not 25.

Fields needed: `spend`, `impressions`, `cpm`, `cpc`, `ctr`, `actions` (leads/conversions), `cost_per_action_type` (CPL/CAC)

**Conversion event selection for CPL calculation:**
1. Check `account_mapping.conversion_type` in the DB — this is the source of truth for which action_type each client uses
2. Cross-reference with `kpi_primary` from client-config.md if the DB value seems wrong
3. If no DB mapping, use default priority: `lead` > `complete_registration` > `fb_pixel_custom` > `onsite_web_lead`
4. Log which event was used: "CPL calculated from [event_type] ([count] conversions)"
5. **Known overrides:** EH = fb_pixel_custom (webinar regs), Stocks.News = mobile_app_install, Status News = fb_pixel_custom (Qualified Carrd)

### Phase 3: Compare Against Targets

For each client, determine status:

| Status | Criteria |
|--------|----------|
| **GREEN** | CPL/CAC at or below target |
| **YELLOW** | CPL/CAC within 15% above target |
| **RED** | CPL/CAC more than 15% above target |
| **NO DATA** | No Pipeboard account, no recent data, or creative-only client |

Parse `cpl_target` carefully — some are ranges ("$10-14"), some have qualifiers ("$45 V-CAC"). Use the upper bound for range targets.

### Phase 4: Calculate Portfolio Aggregates

- **Total daily spend:** Sum all TFM campaign spend / 7
- **Total 7-day spend:** Sum all TFM campaign spend (NOT account-level totals)
- **Weighted average CPL:** Total TFM spend / Total TFM conversions
- **Median CPM:** Median of TFM campaign-level CPMs
- **Client counts:** GREEN / YELLOW / RED / NO DATA

**Important:** All aggregates must reflect TFM-managed campaigns only. Never include non-TFM campaign spend in portfolio totals.

### Phase 5: Detect Cross-Portfolio Patterns

Scan for these signals:

1. **Platform-wide CPM trend:** If CPMs increased >10% across >50% of accounts → "CPMs rising platform-wide — likely auction pressure, not creative issue"
2. **Transferable creative insight:** If a format (static/video/carousel) or hook type is outperforming across 3+ clients → flag for cross-pollination
3. **Portfolio-wide fatigue wave:** If 3+ clients show CTR decline simultaneously → "Multiple accounts showing fatigue — consider fresh creative sprint"
4. **Spend concentration risk:** If one client accounts for >30% of total spend → flag dependency

### Phase 6: Output Dashboard

Print the dashboard to stdout. Also write to `reports/portfolio-pulse-[YYYY-MM-DD].md`.

```markdown
# Portfolio Pulse — [Date]

## At a Glance
| Metric | Value |
|--------|-------|
| Total Daily Spend | $X,XXX |
| Total 7-Day Spend | $XX,XXX |
| Active Accounts | XX of 25 |
| Weighted Avg CPL | $X.XX |
| Median CPM | $XX.XX |
| On Target | X GREEN |
| Watch | X YELLOW |
| At Risk | X RED |
| No Data | X |

## Client Breakdown
| Client | GM | Spend (7d) | CPL/CAC | Target | Status | KPI Type |
|--------|----|-----------|---------|--------|--------|----------|
[sorted by spend descending, Workweek sub-accounts indented]

## Cross-Portfolio Signals
[Pattern detection results — only show if patterns detected]

## Needs Attention (RED)
[For each RED client: what's wrong, how far from target, suggested action]

## Watch List (YELLOW)
[For each YELLOW client: current trajectory, risk of going RED]

## Top Performers
[GREEN clients with CPL significantly below target — potential scale candidates]
```

### Phase 7: Update State (Optional)

If `system/state/` tracking is active, update the relevant state file with the latest pulse results.

## Arguments

The skill accepts an optional time range argument:
- `/portfolio-pulse` — default 7 days
- `/portfolio-pulse 14d` — last 14 days
- `/portfolio-pulse mtd` — month to date

## Error Handling

- If Pipeboard returns no data for an account, mark as NO DATA and continue
- If a client has no `meta_account_id` in config, skip silently
- Some accounts may have access issues — note in output but don't fail the entire run
- Always complete the full portfolio even if individual clients error

## What NOT to Do

- Don't modify client files — this is read-only reporting
- Don't send Slack messages — output to stdout and local file only
- Don't make budget recommendations — just surface the data and patterns
- Don't compare across different KPI types (CPL vs ROAS) in aggregates
