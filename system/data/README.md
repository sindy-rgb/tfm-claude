# Pipeboard SQLite Database

**Location:** `system/data/pipeboard.db`
**Last audited:** 2026-03-22
**Current size:** 1.7 MB

## What This Is

Local SQLite cache of Meta Ads performance data pulled from the Pipeboard MCP integration. Stores campaign-level and ad-level metrics for all 25 TFM clients, with weekly and monthly granularity going back to late December 2025.

Used by Claude Code skills (weekly enrichment, creative QA, reporting) to answer performance questions without hitting the Pipeboard API every time.

## Database Schema

### Tables

| Table | Purpose | Rows (as of audit) |
|-------|---------|-------------------|
| `account_mapping` | Maps Meta ad account IDs to client slugs. Source of truth for account-to-client relationships. | 25 |
| `snapshots` | Tracks when data was pulled (snapshot metadata). | 3,134 |
| `campaign_metrics` | Weekly/monthly campaign performance data (spend, impressions, clicks, conversions, CPL). | 1,739 |
| `ad_metrics` | Individual ad-level performance data. Same fields as campaign_metrics but per-ad. | 1,669 |

### Views

| View | Purpose | Example Query |
|------|---------|---------------|
| `v_latest_weekly` | Latest week's aggregated data per client with CPL, CPC, CTR. | `SELECT * FROM v_latest_weekly ORDER BY spend DESC` |
| `v_wow_comparison` | This week vs last week per client with absolute and percentage deltas. | `SELECT client_slug, tw_cpl, lw_cpl, cpl_pct_change FROM v_wow_comparison` |
| `v_client_summary` | All-time summary per client. Uses only weekly rows to avoid double-counting from monthly compacts. | `SELECT client_slug, total_spend, avg_cpl FROM v_client_summary` |
| `v_stale_clients` | Clients whose latest data is older than 48 hours, plus clients with no data at all. | `SELECT * FROM v_stale_clients` |

### Indexes

- `idx_campaign_metrics_slug` — (client_slug, date_start) for client lookups
- `idx_campaign_metrics_campaign` — (campaign_id, date_start) for campaign drilldowns
- `idx_campaign_metrics_weekly` — (client_slug, date_start, date_stop) for view performance
- `idx_campaign_metrics_snapshot` — (snapshot_id) for FK joins
- `idx_ad_metrics_slug` — (client_slug, date_start)
- `idx_ad_metrics_ad` — (ad_id, date_start)
- `idx_ad_metrics_snapshot` — (snapshot_id)
- `idx_snapshots_slug` — (client_slug, snapshot_date)

## Data Audit Summary (2026-03-22)

### Coverage

- **24 of 25 clients** have campaign data in the DB
- **Vendry** has an account mapping but zero data rows (needs a Pipeboard pull)
- **Open Source CEO** has only 2 rows (one monthly compact, one weekly) — needs a full backfill
- **5 clients from the active list are not in account_mapping at all:**
  - `jay-shetty` — not mapped
  - `1636-forum` — not mapped
  - `student-loan-planner` — not mapped
  - `mdhair` — not mapped
  - `workweek` (parent slug) — not mapped, but the 5 Workweek sub-brands ARE mapped individually (`workweek-ftt`, `workweek-gtm`, `workweek-hospitalogy`, `workweek-ihih`, `workweek-tmm`)

### Data Freshness

- **23 clients** have data through 2026-03-22 (today) — current
- **Open Source CEO** latest data is 2026-03-21 (1 day stale)
- **Vendry** has no data at all

### Conversion Data Quality

- **1,141 of 1,739 rows (65.6%)** have conversions > 0
- **598 rows have zero conversions** — this is expected for two reasons:
  1. **The Points Guy** accounts for the majority (392 of its 442 rows have 0 conversions). TPG has many campaigns where the weekly breakdown doesn't return conversion actions — likely a conversion type mismatch at the weekly level
  2. **Just Women's Sports** has a similar pattern (118 of 138 rows have 0 conversions)
  3. Several clients have occasional weeks with 0 (typically low-spend or newly launched campaigns)
- **20 of 24 clients** with data have 70%+ conversion coverage
- The monthly compact rows DO capture conversions correctly for TPG, confirming the issue is with weekly granularity + action breakdowns

### Duplicates (Fixed)

- **30 duplicate rows in ad_metrics** for workweek-ihih were found and removed during this audit
- No duplicates exist in campaign_metrics
- Root cause: likely a double-pull during the initial data load

## The Weekly Compact vs Non-Compact Problem

### The Issue

Pipeboard's `get_insights` returns data differently based on the `time_increment` parameter:

- **Weekly (`time_increment=7`):** Returns spend, impressions, clicks correctly, but conversion actions may return 0 for some clients. This happens when the action type specified in `action_breakdowns` doesn't perfectly match Meta's internal attribution window at weekly granularity.
- **Monthly compact (full date range):** Returns correct totals including conversions, because Meta aggregates conversions properly at longer time horizons.

### Affected Clients

| Client | Weekly Conversion Rate | Notes |
|--------|----------------------|-------|
| the-points-guy | 11.3% of weekly rows have conversions | Huge gap — only monthly compacts are reliable for conversion counts |
| just-womens-sports | 14.5% | Similar issue |
| open-source-ceo | 0% of weekly rows | Only 1 weekly row, shows 0 conversions |
| rnt-fitness | 70.3% | Some weeks missing |
| quartz | 76.9% | A few weeks missing |

### Recommended Handling

1. **For CPL calculations in views**: The views already handle this by using `CASE WHEN conversions > 0 THEN ... ELSE NULL` to avoid showing misleading $0 CPLs
2. **For weekly enrichment skill**: Use weekly data for spend/impressions trends, but pull monthly compacts for accurate conversion/CPL numbers for affected clients
3. **For the v_client_summary view**: Already filters to weekly-only rows to avoid double-counting, but shows NULL CPL when conversions are unreliable
4. **Long-term fix**: When refreshing data, always pull both weekly AND a monthly compact, then use the monthly compact's conversion numbers to back-fill the weekly rows proportionally

## Size and Growth Rate

- **Current size:** 1.7 MB for ~13 weeks of data across 24 clients
- **Estimated growth:** ~130 KB/week (assuming all 25 clients, weekly + monthly pulls)
- **Projected annual size:** ~8-9 MB — very manageable, no need for archiving or pruning for years
- **With daily granularity added:** Would grow ~7x faster (~900 KB/week, ~50 MB/year) — still fine

## Recommended Refresh Schedule

| Frequency | What | Why |
|-----------|------|-----|
| **Daily (preferred)** | Last 3 days of data for all clients | Catches attribution window updates (Meta updates conversions for 1-3 days after the click) |
| **Weekly (minimum)** | Last 7 days for all clients | Sufficient for weekly reporting cadence |
| **On-demand** | Full date range for specific client | When a client asks about historical performance or after fixing a conversion type |

The refresh should always be an **upsert** (delete existing rows for the date range, then insert fresh data) to handle Meta's attribution window corrections.

## Ideas for Additional Data

### High Value (Should Do)

1. **Ad creative names in ad_metrics** — Already stored. Consider adding `adset_id` and `adset_name` columns for the DCT 4-3-2-2 analysis pattern.
2. **Daily granularity** — Add `time_increment=1` pulls for the last 7 days. Useful for spotting spend spikes, pacing issues, and day-of-week patterns. Store in the same `campaign_metrics` and `ad_metrics` tables (the date_start/date_stop range identifies the granularity).
3. **Adset-level table** — New `adset_metrics` table would enable DCT analysis (which ad sets are winners, which should be killed). Same schema as campaign_metrics but with adset_id/adset_name.

### Medium Value (Nice to Have)

4. **Landing page CVR data** — Could be pulled from Beehiiv subscriber API or Google Analytics and stored in a separate `landing_page_metrics` table.
5. **Historical conversion type mapping** — Track when a client's conversion type changes (e.g., from `lead` to `offsite_conversion.fb_pixel_custom`).
6. **Budget data** — Campaign daily/lifetime budgets to calculate delivery pacing.

### Lower Priority

7. **Audience data** — Custom audience sizes, interest targeting details per adset.
8. **Frequency distribution** — 1-day, 7-day frequency breakdowns for creative fatigue detection.

## How n8n Could Write Directly to the DB

### Current Architecture
```
Pipeboard API → Claude Code session → SQLite DB (local file)
```

### Proposed Architecture (n8n-native)
```
n8n workflow (scheduled) → Pipeboard HTTP nodes → SQLite node → pipeboard.db
```

### Implementation Options

**Option A: n8n writes to SQLite directly (Recommended)**
- n8n has a native SQLite node that can execute INSERT/UPDATE/DELETE
- The DB file path needs to be accessible from the n8n Docker container
- Mount the vault's data directory as a Docker volume: `-v "/path/to/vault/system/data:/data"`
- n8n workflow steps:
  1. Schedule trigger (daily at 6am ET)
  2. Loop through account_mapping entries (HTTP request to read the SQLite, or hardcode the list)
  3. For each client: call Pipeboard API with the account_id and conversion_type from account_mapping
  4. Transform response → SQLite INSERT with conflict resolution
  5. Send Slack notification on completion or failure

**Option B: n8n writes to Google Sheets + Claude syncs to SQLite**
- Keep the existing Google Sheets flow
- Add a Claude Code skill that reads Sheets → writes to SQLite on a schedule
- More complex, but doesn't require Docker volume mounting

**Option C: n8n calls a local API endpoint**
- Build a tiny FastAPI/Flask endpoint that accepts JSON and writes to SQLite
- n8n calls it via HTTP Request node
- Most flexible but requires running another service

### Recommendation

Option A is simplest if the n8n instance can access the file. Since n8n is hosted on Elestio and the DB is local to Jay's machine, the practical approach is:

1. **Short-term**: Use `refresh.sh` (see below) triggered by cron on Jay's machine, or manually by Claude Code
2. **Medium-term**: Move the DB to a shared location (e.g., a small Supabase/Turso instance) that both n8n and Claude Code can access
3. **Long-term**: n8n workflow writes directly to a hosted DB, Claude Code reads from it

## Refresh Script

See `system/data/refresh.sh` for a shell script that refreshes the last 7 days of data for all clients. It uses the Pipeboard bulk_get_insights API pattern and can be called by cron or n8n.
