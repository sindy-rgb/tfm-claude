---
name: fatigue-scan
description: >
  Creative fatigue detection for The Feed Media ad accounts. Pulls 14 days of ad-level performance
  from Pipeboard, compares week-over-week CTR and CPL trajectories, flags ads with declining
  performance, and outputs kill/scale/iterate recommendations. Use when the user says "fatigue scan",
  "creative fatigue", "ad fatigue", "which ads are tired", "what needs killing", "kill list",
  "ad performance decay", "CTR declining", or asks about ad creative health.
---

# Fatigue Scan — Creative Fatigue Detection

You detect creative fatigue across The Feed Media's (TFM) client ad accounts. You pull 14 days of ad-level data, compare week-over-week performance trajectories, and produce actionable kill/scale/iterate recommendations.

## Local Performance Database (Primary Data Source)

A SQLite database at `system/data/pipeboard.db` stores all ad performance data. **This is the primary data source — Pipeboard live pulls are the fallback.**

**Tables:**
- `ad_metrics` — 30 days of ad-level data: spend, impressions, clicks, cpc, cpm, ctr, conversions, cpl, frequency, reach per ad per client per day
- `account_mapping` — maps client slugs to Meta account IDs and conversion types
- `snapshots` — ingestion metadata with `created_at` timestamps for freshness checks

**Standard workflow:**

1. **Query the DB directly** for the client's 14-day ad data (see Phase 2, Step 0)
2. **If data is <48 hours old**, use it — skip Pipeboard entirely
3. **If data is stale or missing**, fall back to Pipeboard live pull, then **ingest into cache:**
   ```bash
   echo '<pipeboard_json>' | python3 system/pipeboard-cache.py ingest <client-slug> ad [YYYY-MM-DD]
   ```
4. **For historical trends**, query the DB directly:
   ```bash
   python3 system/pipeboard-cache.py trends <ad_id>
   python3 system/pipeboard-cache.py query "SELECT * FROM ad_metrics WHERE client_slug='the-points-guy' ORDER BY date_start"
   ```

Over time, the DB builds a full history. A fatigue scan run 4 weeks from now can compare against today's data without re-fetching it.

## Usage

- `/fatigue-scan [client-slug]` — Scan one client's ads
- `/fatigue-scan all` — Scan all clients with Pipeboard accounts
- `/fatigue-scan [client-slug] 21d` — Custom lookback window (default 14 days)

## Step-by-Step Process

### Phase 0: Load Client Context (MANDATORY — before any data pull)

For each client being scanned:
1. Read `clients/[slug]/[slug].md` — extract:
   - Performance history sections (ROAS data, trend notes, known issues)
   - Current strategic context (what's being tested, paused, restructured)
   - Risk level and relationship context
   - Per-DCT performance data already documented in the vault
2. Read `clients/[slug]/deep-enrichment.md` — extract:
   - **Funnel structure** — what conversion event defines "fatigue" for this client (newsletter signup vs webinar registration vs app install vs trial start). A CTR drop on a webinar funnel means something different than on a newsletter signup funnel.
   - **Competitive context** — seasonal patterns, market shifts, or platform changes that could explain performance dips (not everything is fatigue)
   - **DCT performance history** — what concepts have been tested before, what creative angles are proven, what's been retired. This prevents recommending iterations on angles that already failed.
   - **Google Drive creative audit** — current creative inventory and pipeline status
3. Read `clients/[slug]/client-config.md` — extract:
   - `kpi_primary` and `kpi_secondary` — determines whether CPL, ROAS, V-CAC, or Cost Per Trial is the fatigue signal
   - `tfm_campaign_ids` — determines what to pull
   - Full Scaling Rules section if present (e.g., TPG has ROAS validation thresholds, spend caps)
   - `budget_notes` for scaling guardrails
4. If `kpi_primary` or `kpi_secondary` mentions ROAS:
   - Search the intel file for ROAS data (6-week ROAS, per-DCT ROAS, ROAS trends)
   - Check `kpi_primary` and `kpi_secondary` in client-config.md. If either mentions ROAS, apply the ROAS analysis rules in Phase 3b. Do not maintain a hardcoded list — client KPIs change.
   - Include vault ROAS data in the fatigue report even if Pipeboard can't provide it
5. Store all context. **The fatigue report should LEAD with strategic context, then layer metrics on top.**

### Pagination Protocol

When pulling ad-level or campaign-level data from Pipeboard:
1. Check the response for pagination indicators (`paging`, `next`, `after` cursor)
2. If results appear truncated (e.g., exactly 25 or 50 records returned), explicitly request the next page using the `after` cursor
3. Continue until all pages are retrieved
4. Log total record count: "Retrieved X ads from Y campaigns"
5. If the API returns fewer ads than expected for a known active client, flag: "WARNING: May be missing ads — verify pagination"

For fully TFM-managed accounts (Workweek), pull at account level to avoid pagination issues across multiple campaign-level pulls.

### Phase 1: Identify Accounts

If a specific client-slug is given:
1. Read `clients/[slug]/client-config.md`
2. Extract `meta_account_id` and `tfm_campaign_ids`

If "all":
1. Glob for all `clients/*/client-config.md`
2. Extract every account with a `meta_account_id`
3. Skip clients without Pipeboard accounts silently

### Multi-Account Clients

| Client | Accounts | Handling |
|--------|----------|----------|
| Workweek | 5 accounts | Scan each separately: IHIH (act_3186358998360632), TMM (act_579954186820640), FTT (act_1079516909306359), Hospitalogy (act_718612189266939), GTM (act_4673797136057796) |
| MarketBeat | 1 shared account (act_1129788478833121) | Filter to `tfm_campaign_ids` only — exclude GrowJoy competitor campaigns |
| All others | 1 account each | Standard pull |

### Phase 2: Pull 14-Day Ad-Level Data

#### Step 0: Check Local DB First (before any Pipeboard call)

The SQLite database at `system/data/pipeboard.db` is the **primary data source**. Only fall back to live Pipeboard if the DB data is stale.

**Query for ad-level data:**
```sql
SELECT * FROM ad_metrics
WHERE client_slug = '[slug]'
  AND date_start >= date('now', '-14 days')
ORDER BY date_start, ad_id;
```

**Freshness check:**
```sql
SELECT MAX(created_at) as last_ingested
FROM snapshots
WHERE client_slug = '[slug]'
  AND level = 'ad';
```

**Decision logic:**
- If `last_ingested` is **<48 hours old** → use DB data. Skip the Pipeboard pull entirely for this client.
- If `last_ingested` is **>48 hours old** or no rows returned → fall back to Pipeboard live pull (Step 1 below), then ingest the results into the cache for next time.
- If DB returns data but covers **fewer than 10 of the last 14 days**, treat as incomplete and supplement with a Pipeboard pull for the missing date range.

**Account mapping (if needed):**
```sql
SELECT account_id, conversion_type
FROM account_mapping
WHERE client_slug = '[slug]';
```

The DB has all the fields the fatigue scan needs: `spend`, `impressions`, `clicks`, `cpc`, `cpm`, `ctr`, `conversions`, `cpl`, `frequency`, `reach`, `ad_name`, `ad_id`, `campaign_id`, `date_start`, `date_stop`.

When DB data is used, log: "Data source: local DB (last ingested: [timestamp])". When Pipeboard is used, log: "Data source: Pipeboard live pull (DB was stale: [timestamp])".

#### Step 1: Pipeboard Live Pull (fallback only)

**CRITICAL: Only pull ads from TFM-managed campaigns.** Use `tfm_campaign_ids` from client config — never pull at account level. Most clients have non-TFM campaigns running in their accounts.

For each TFM campaign ID, use `mcp__claude_ai_Pipeboard__get_insights`:

**Two-window approach:**
- **Window 1 (older):** Days 8-14 ago → baseline performance
- **Window 2 (recent):** Days 1-7 ago → current performance

Parameters:
- `object_id`: each TFM campaign ID (NOT account ID)
- Level: `ad`
- If `tfm_campaign_ids` is "N/A" or "TBD" → skip this client
- Fields needed: `ad_name`, `ad_id`, `impressions`, `clicks`, `ctr`, `spend`, `cost_per_action_type` (for CPL), `frequency`, `cpm`, `actions`

If the API doesn't support custom date ranges easily, pull `last_14d` and split the data by date in post-processing.

**Data quality filters:**
- Exclude ads with <1,000 impressions in either window (insufficient data)
- Exclude ads running <3 days (too new to evaluate — mark as WATCH)
- Exclude paused ads unless they were active in Window 1

### Phase 3: Calculate Fatigue Signals

For each ad, compare Window 1 vs Window 2:

| Signal | Calculation | Threshold | Severity |
|--------|------------|-----------|----------|
| CTR Decline | (W2_CTR - W1_CTR) / W1_CTR | >20% decline | HIGH |
| CPL Increase | (W2_CPL - W1_CPL) / W1_CPL | >15% increase | HIGH |
| High Frequency | W2 frequency value | >3.0 | MEDIUM |
| CPM Spike | (W2_CPM - W1_CPM) / W1_CPM | >25% increase | LOW |
| Impression Decline | (W2_impressions - W1_impressions) / W1_impressions | >40% decline | MEDIUM (delivery issue) |

**Window-to-window disappearance check:**
- If an ad appeared in Window 1 (days 8-14) but NOT in Window 2 (days 1-7), it was likely paused or killed.
- Report these separately as "Paused Between Windows" with their Window 1 spend.
- If >50% of Window 1 ads disappeared, flag: "Major restructure detected — cross-reference with Slack/vault for context."
- Do NOT treat disappeared ads as "missing data" — they are operational decisions that affect the fatigue assessment.

### Phase 3b: ROAS-Primary Client Analysis

**Some clients use ROAS (not CPL) as the primary success metric.** Check `kpi_primary` in client config. If it mentions ROAS, apply these additional rules:

**ROAS-primary clients (as of Mar 2026):** The Points Guy, MarketBeat

For these clients:
1. **Read the client config for scaling rules** — check for a "Scaling Rules" section with ROAS validation thresholds
2. **CPL alone is misleading** — an ad can have a great CPL but terrible ROAS (low subscriber quality). Meta optimizes for CPL, not revenue.
3. **Check spend share** — flag any ad consuming >5% of total campaign spend that hasn't had ROAS validated (launched <6 weeks ago)
4. **3-month ROAS trend** — if an ad has shown declining ROAS for 3+ consecutive reporting periods, recommend KILL regardless of CPL
5. **Top performer protection** — flag if proven ROAS ads (listed in config or intel file) are getting squeezed on spend share by newer unvalidated concepts

**Additional signals for ROAS clients:**

| Signal | Calculation | Threshold | Severity |
|--------|------------|-----------|----------|
| Unvalidated high spend | Ad <6 weeks old AND >5% of campaign spend | Automatic | HIGH |
| Top performer squeeze | Proven ROAS ad's spend share declined >30% WoW | Flag | MEDIUM |
| Spend share imbalance | Top 3 proven ROAS ads getting <40% of total spend | Flag | MEDIUM |

**Where to find ROAS data (check in this order):**
1. **The client's intel file** (`clients/[slug]/[slug].md`) — often has per-DCT ROAS data, trend analysis, and cohort dashboard summaries already documented. CHECK THIS FIRST.
2. **The client's config file** — check `kpi_secondary_target` for ROAS thresholds
3. **Slack** `#internal-[slug]` — search for recent ROAS report/dashboard shares
4. If no ROAS data found anywhere, note "ROAS data not available — recommend requesting from [contact]" and proceed with CPL-only analysis with a disclaimer

### Phase 4: Score and Classify

**Fatigue Score per ad:**

| Condition | Classification |
|-----------|---------------|
| 0 signals triggered | **HEALTHY** |
| 1 LOW or MEDIUM signal | **MONITOR** |
| 1 HIGH signal | **FATIGUED** |
| 2+ signals (any severity) | **FATIGUED** |
| CTR decline + CPL increase together | **CRITICAL** |
| Ad age <3 days | **WATCH** (insufficient data) |
| ROAS clients: unvalidated ad >5% spend share | **ROAS WATCH** (needs validation) |
| ROAS clients: 3+ months low ROAS | **KILL** (regardless of CPL) |

### Phase 5: Generate Recommendations

| Classification | Recommendation | Action |
|---------------|----------------|--------|
| HEALTHY + CPL below target | **SCALE** | Increase budget, duplicate to new ad sets |
| HEALTHY + CPL at target | **MAINTAIN** | Keep running, no changes needed |
| MONITOR | **MONITOR** | Check again in 3-4 days, no action yet |
| FATIGUED | **ITERATE** | Create variation with new hook/headline, keep original running at lower budget |
| CRITICAL | **KILL** | Pause immediately, reallocate budget to healthy ads |
| WATCH | **WATCH** | New ad, check next scan |
| ROAS WATCH | **CAP SPEND** | Cap at current level until ROAS validates (6 weeks from launch). Do not scale. |

**ROAS-client scaling rules (from client config):**
- Read the client's `Scaling Rules` section in their config for specific thresholds
- Default if no rules specified: new ads capped at 5% of campaign spend until 6-week ROAS validates
- Never scale an ad that has good CPL but unproven ROAS — CPL and quality are different things

### Phase 6: Output Report

```markdown
# Fatigue Scan — [Client Name] — [Date]
*Lookback: [X] days | Window 1: [date range] | Window 2: [date range]*

## Summary
| Status | Count | Action |
|--------|-------|--------|
| KILL | X | Pause immediately |
| ITERATE | X | Create variations |
| MONITOR | X | Watch closely |
| MAINTAIN | X | No action |
| SCALE | X | Increase budget |
| WATCH | X | Too new to evaluate |

## Immediate Action Required (KILL / CRITICAL)
| Ad Name | CTR Δ | CPL Δ | Freq | CPM Δ | Score |
|---------|-------|-------|------|-------|-------|
[ads to kill — sorted by severity]

**Recommended:** Pause these ads and reallocate $[daily spend] to healthy ads.

## Iterate Soon (FATIGUED)
| Ad Name | CTR Δ | CPL Δ | Freq | Primary Signal |
|---------|-------|-------|------|----------------|
[ads needing creative refresh]

**Recommended:** Create new variations preserving the winning elements. Change: [hook/headline/thumbnail/CTA].

## Healthy Ads
| Ad Name | CTR (W2) | CPL (W2) | Freq | Status | Spend (7d) |
|---------|----------|----------|------|--------|-----------|
[healthy ads sorted by spend]

## Watch (New Ads)
| Ad Name | Age | Impressions | Early CTR | Early CPL |
|---------|-----|-------------|-----------|-----------|
[new ads with insufficient data]

## Creative Pipeline Check
- Ads recommended to kill: X → Need X replacement concepts
- Ads recommended to iterate: X → Need X variations
- Total creative need: X new concepts/variations
```

### Phase 7: Portfolio Summary (all mode)

When running across all clients, produce a portfolio-level summary first:

```markdown
# Portfolio Fatigue Scan — [Date]

## Portfolio Summary
| Client | KILL | ITERATE | HEALTHY | WATCH | Urgency |
|--------|------|---------|---------|-------|---------|
[one row per client, sorted by urgency]

## Highest Priority
[Top 3 clients with most KILL/CRITICAL ads — brief action items]

## Cross-Portfolio Patterns
- [If same ad format fatiguing across clients → format burnout]
- [If fatigue concentrated in one GM's accounts → workload flag]
- [If fatigue wave across portfolio → seasonal/platform-level]
```

### Phase 8: Optional Slack Draft

If the scan finds KILL or CRITICAL ads, draft a Slack message to the client's internal channel (`slack_internal` from client-config.md) using `mcp__claude_ai_Slack__slack_send_message_draft`:

> :warning: Fatigue scan flagged X ads for [Client].
> **KILL:** [ad names] — CTR down [X]%, CPL up [Y]%
> **Action:** Recommend pausing and replacing. Pipeline needs X new concepts.
> cc @[GM name]

Only draft — never send automatically.

## Error Handling

- If Pipeboard returns no data for an account, skip and note "No data available"
- If an account has <3 active ads, still scan but note "Limited ad set — fatigue less meaningful"
- If CTR or CPL is 0 in either window, exclude that ad from percentage calculations
- If all ads are <3 days old, report "All ads too new for fatigue analysis — run again in [X] days"
- Complete the full scan even if individual accounts error

## What NOT to Do

- Don't pause or modify any ads — this is analysis only
- Don't compare ads across different clients (different niches = different benchmarks)
- Don't flag CPM increases as creative fatigue — CPM is platform-level, not creative-level
- Don't recommend specific creative concepts — just flag what needs replacing
- Don't modify client files — output to stdout only (plus optional Slack draft)
