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

## Local Performance Cache

A SQLite database at `system/data/pipeboard.db` caches all Pipeboard pulls. **Always use this workflow:**

1. **Check cache freshness:** `python3 system/pipeboard-cache.py freshness`
2. **If a client's data is <24 hours old**, use cached data instead of re-pulling
3. **After any Pipeboard pull**, ingest into cache: `echo '<json>' | python3 system/pipeboard-cache.py ingest <slug> campaign`
4. **For portfolio summary from cache:** `python3 system/pipeboard-cache.py summary`

This avoids redundant API calls and builds historical data for trend detection.

## Context

- **Client configs:** `/the-feed-media/clients/[slug]/client-config.md` — each has `meta_account_id`, `kpi_primary`, `kpi_target`, `cpl_target`
- **Client intel files:** `/the-feed-media/clients/[slug]/[slug].md` — has frontmatter with `current_cpl`, `risk_level`
- **Master summary:** `/the-feed-media/CLIENT-INTELLIGENCE-SUMMARY.md`

## Step-by-Step Process

### Phase 0: Load Client Context (MANDATORY — before any Pipeboard pull)

For each client:
1. Read `clients/[slug]/[slug].md` — extract performance history, risk level, known issues
2. Read `clients/[slug]/client-config.md` — extract:
   - `kpi_primary` and `kpi_secondary` (determines which metrics matter)
   - `tfm_campaign_ids` (determines what to pull — skip if "N/A" or "TBD")
   - Scaling Rules section if present
   - `budget_notes` for context on spend pacing
3. Store context — the dashboard should reflect strategic context, not just raw numbers

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

### Phase 2: Pull 7-Day Insights (CAMPAIGN LEVEL ONLY)

**CRITICAL: Always pull at campaign level and filter to TFM campaigns only.** Most clients have other campaigns in their ad accounts (client-managed, other agencies, etc.). Account-level pulls include non-TFM spend and will massively overstate TFM numbers.

For each client:
1. Read `tfm_campaign_ids` from the client config
2. If `tfm_campaign_ids` is "N/A", "TBD", or empty → skip (no TFM media for this client)
3. For each campaign ID in `tfm_campaign_ids`, call `mcp__claude_ai_Pipeboard__get_insights` with:
   - `object_id`: the campaign ID (NOT the account ID)
   - `time_range`: "last_7d" (or custom range from argument)
   - `level`: "campaign"
4. Sum spend, impressions, clicks, and conversions across only TFM campaign IDs for that client
5. Calculate CPL from the summed TFM-only data

**Exception — Workweek:** Each of the 5 accounts is fully TFM-managed, so account-level pulls are acceptable. But still prefer campaign-level for consistency.

**Parallelization:** Use sub-agents to pull from multiple campaigns concurrently. Group into batches of 5-7 to avoid rate limits.

Fields needed: `spend`, `impressions`, `cpm`, `cpc`, `ctr`, `actions` (leads/conversions), `cost_per_action_type` (CPL/CAC)

**Conversion event selection for CPL calculation:**
1. Check `kpi_primary` from client-config.md for which metric this client cares about
2. Check `CLIENT_CONVERSION_OVERRIDES` in `system/pipeboard-cache.py` for the correct action_type per client
3. If no override, use default priority: `lead` > `complete_registration` > `fb_pixel_custom` > `onsite_web_lead`
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

Print the dashboard to stdout. Also write to `/the-feed-media/reports/portfolio-pulse-[YYYY-MM-DD].md`.

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
