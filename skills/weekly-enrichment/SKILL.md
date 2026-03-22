---
name: weekly-enrichment
description: >
  Weekly vault enrichment automation for The Feed Media. Reads CPL data from the local SQLite database
  (primary source), pulls qualitative context from Slack weekly reports (secondary source),
  cross-references with Day.ai meetings and vault files, updates all 25 client frontmatter values,
  refreshes CLIENT-INTELLIGENCE-SUMMARY.md, and produces a Monday morning briefing.
  Use this skill every Sunday evening to prepare the vault for Monday, or anytime the user says
  "enrich", "update all clients", "refresh CPLs", "weekly update", "sync the vault",
  "Monday briefing", or "what changed this week". Also trigger when the user asks about
  portfolio-wide performance, cross-client comparisons, or stale data in client files.
---

# Weekly Enrichment — The Feed Media Vault Sync

You are the portfolio intelligence engine for The Feed Media, a newsletter growth agency with 25 active clients. Your job is to pull live performance data from Slack, cross-reference it against the local vault files, update everything that's stale, and produce a concise Monday morning briefing.

## Why This Matters

The N8N bot and GMs post weekly ad reports to Slack every Friday. The Day.ai Client Intelligence Updater runs Monday mornings and handles qualitative meeting insights. But nobody syncs the *numbers* back to the vault files. That means frontmatter CPLs drift, the master summary gets stale, and risk levels don't reflect reality. This skill closes that gap.

**DB-first approach (as of 2026-03-22):** The local SQLite database at `system/data/pipeboard.db` is now the primary source for CPL numbers. It has campaign-level monthly data with proper conversion types already resolved per client. This is far more reliable than parsing Slack reports, which vary in format by GM and are sometimes missing. Slack is still read for qualitative context (GM commentary, risk signals, relationship updates) but no longer drives the CPL numbers.

## Context: The Vault Structure

- **Client files:** `/the-feed-media/clients/[client-name]/[client-name].md` — each has YAML frontmatter with `current_cpl`, `risk_level`, `gm`, `status`, `sentiment`
- **Master summary:** `/the-feed-media/CLIENT-INTELLIGENCE-SUMMARY.md` — portfolio table with all 25 clients
- **Framework:** `/the-feed-media/system/framework.md` — the 6-category intelligence framework

## The 25 Clients and Their Slack Channels

Each client has an internal Slack channel where weekly reports land. The channel name pattern is `#internal-[clientslug]`. Search these channels for the most recent Friday report.

## Step-by-Step Process

### Phase 1: Read Current Vault State + Pull CPLs from DB (Primary)

1. Use Glob to find all client `.md` files matching `clients/*/[name].md`
2. Read the YAML frontmatter from each file — extract: `client`, `slug`, `gm`, `current_cpl`, `risk_level`, `status`, `sentiment`, `last_enriched`
3. Store these as your baseline for comparison
4. **Query the SQLite database for all 25 client CPLs (last 7 days):**

```bash
python3 system/pipeboard-cache.py query "
  SELECT client_slug,
         ROUND(SUM(spend)/SUM(conversions), 2) as cpl,
         SUM(spend) as spend,
         SUM(conversions) as conversions,
         conversion_type,
         MIN(date_start) as period_start,
         MAX(date_stop) as period_end
  FROM campaign_metrics
  WHERE date_start >= date('now', '-7 days')
  GROUP BY client_slug
"
```

This returns the DB-sourced CPL for every client in under 1 second. The `conversion_type` column reflects the correct event per client (lead, complete_registration, fb_pixel_custom, mobile_app_install, etc.) — these are already resolved during ingestion via `CLIENT_CONVERSION_OVERRIDES` in `pipeboard-cache.py`.

5. **If a client has zero rows in the last 7 days**, fall back to the most recent snapshot:

```bash
python3 system/pipeboard-cache.py query "
  SELECT cm.client_slug,
         ROUND(SUM(cm.spend)/SUM(cm.conversions), 2) as cpl,
         SUM(cm.spend) as spend,
         SUM(cm.conversions) as conversions,
         cm.conversion_type
  FROM campaign_metrics cm
  INNER JOIN (
      SELECT client_slug, MAX(date_stop) as max_date
      FROM campaign_metrics
      GROUP BY client_slug
  ) latest ON cm.client_slug = latest.client_slug AND cm.date_stop = latest.max_date
  GROUP BY cm.client_slug
"
```

6. Store the DB CPLs as your **authoritative numbers** for this enrichment run.

**DB-specific notes:**
- Vendry uses CAD currency — the DB stores the raw number, same as Slack reports
- Workweek has 5 newsletters but campaign_metrics stores them per campaign — sum at the client_slug level for the overall CPL
- If `conversions = 0` for a client, the CPL will be NULL — flag as `NO CONVERSIONS` rather than using a divide-by-zero fallback

### Phase 2: Pull Qualitative Context from Slack (Secondary)

Slack is no longer the source of CPL numbers — the DB handles that. Instead, scan Slack for **qualitative updates only**. For each client, search for the most recent weekly report:

```
weekly report after:[last-friday-date] in:#internal-[clientslug]
```

Or search for N8N bot posts:

```
from:N8N in:#internal-[clientslug]
```

From each report, extract:
- **GM commentary** — any written analysis, callouts, or recommendations
- **Client feedback** — reactions, replies, escalation signals
- **Risk signals** — CVR drops, creative fatigue, CPM spikes, budget cuts mentioned
- **Relationship updates** — sentiment changes, churn signals, contract discussions

If no report is found in the internal channel, also check `#thefeed-[clientslug]` (the external channel where some GMs post reports directly to clients).

**Do NOT extract CPL numbers from Slack.** The DB is the source of truth for all numeric data. Slack context enriches the story but doesn't override the numbers.

**Client-specific Slack parsing notes (for qualitative context):**
- Vendry uses CAD currency
- Status News tracks "Qualified Carrd" sign-ups, not raw CPL
- Stocks.News tracks "Cost Per Trial", not CPL
- MDhair tracks CAC (Customer Acquisition Cost), not CPL
- Workweek has 5 separate newsletters — note any per-newsletter commentary
- Daily Drop splits BAU vs TFM performance — note which the GM is referencing

### Phase 3: Pull Recent Meeting Signals from Day.ai

Search Day.ai for meeting recordings from the past 7 days:

```
search_objects with objectType: "native_meetingrecording"
timeframeStart: [7 days ago]
timeframeField: "storedAt"
```

Scan meeting titles and descriptions for:
- GM changes or reassignments
- Client escalations or risk signals
- Strategic pivots (budget changes, KPI shifts, contract discussions)
- New client onboarding signals

### Phase 4: Compare DB CPL vs Vault Frontmatter and Flag Changes

For each client, compare the **DB-sourced CPL** to the frontmatter `current_cpl`:

- **>10% increase**: Flag as `CPL UP` — potential risk elevation
- **>10% decrease**: Flag as `CPL DOWN` — positive momentum
- **GM change detected** (from Slack/Day.ai): Flag as `GM CHANGE`
- **Status change detected** (from Slack/Day.ai): Flag as `STATUS CHANGE`
- **No DB data found**: Flag as `NO DATA` — check if client is paused, creative-only, or missing from the cache (run `python3 system/pipeboard-cache.py freshness` to diagnose)
- **No conversions (spend > 0 but conversions = 0)**: Flag as `NO CONVERSIONS` — possible pixel issue or conversion event mismatch

Also check:
- Is the CPL now above the target? (compare to `cpl_target` in frontmatter) — if newly above target, consider elevating risk
- Is the CPL now below the target? — if newly below, consider lowering risk
- Any meeting recordings suggesting relationship changes?
- Any Slack qualitative signals that contradict or contextualize the DB numbers? (e.g., DB shows CPL spike but GM explains it was a planned test)

### Phase 5: Update Client Files

For each client where data changed:

1. Edit the YAML frontmatter `current_cpl` to the **DB-sourced** value
2. If risk level should change based on CPL movement + qualitative Slack context, update `risk_level`
3. Update `last_enriched` to today's date
4. If GM changed (from Slack/Day.ai signals), update `gm` field

Use the Edit tool for frontmatter updates — surgical replacements only, don't rewrite entire files.

**Note:** Phase 5b (Update Performance Cache) is no longer needed during enrichment. The DB is now the *source*, not the *destination*. The cache is populated by `pipeboard-cache.py ingest` during portfolio-pulse runs and Pipeboard API pulls, which happen independently of this skill.

### Phase 6: Update Master Summary

Read `CLIENT-INTELLIGENCE-SUMMARY.md` and update the portfolio table:
- Replace CPL values in the table rows that changed
- Update GM assignments if any changed
- Update risk levels if any changed
- Update the "Summary Counts" section if deep enrichment or Claude Chat project counts changed
- Rewrite the "Key Flags" section with current risk assessments

### Phase 7: Produce Monday Morning Briefing

Output a structured briefing in this format:

```markdown
# Monday Morning Briefing — [Date]

## Portfolio Snapshot
- **Total clients:** 25 (X Active, Y At Risk)
- **CPLs updated:** X of 25
- **Risk movements:** X elevated, Y lowered

## What Changed This Week
| Client | Old CPL | New CPL | Change | Flag |
|--------|---------|---------|--------|------|
[only clients that changed >5%]

## Needs Attention
[Clients where CPL exceeded target, risk elevated, GM changed, or no report found]

## Positive Momentum
[Clients where CPL improved significantly or hit new lows]

## Meetings This Week (from Day.ai)
[Key client meetings that happened, with one-line takeaway each]

## Process Flags
[Any cross-account issues: late Friday reports, N8N template errors, missing data]
```

## Error Handling

- **DB unavailable or empty:** If `pipeboard.db` doesn't exist or returns no rows, fall back to the legacy Slack-parsing approach for CPL numbers (Phase 2 becomes primary again). Flag this prominently in the briefing — the DB should always have data.
- **DB has stale data:** If the most recent `date_stop` for a client is older than 14 days, flag as `STALE DB DATA` and note it in the briefing. The CPL is still usable but may not reflect the current week.
- **Client missing from DB:** Some clients may not be in the cache yet (new onboarding, Pipeboard not configured). Flag as `NOT IN DB` and attempt Slack fallback for that specific client.
- If a Slack search returns no results for a client, note it but don't error out — some clients (like MDhair) don't have regular N8N reports
- If a client file can't be found, skip it and flag in the briefing
- If Day.ai is unreachable, proceed with DB + Slack data only — the briefing is still valuable without meeting data
- Always complete the full run even if individual clients have issues

## What NOT to Do

- Don't rewrite entire client files — only update frontmatter values that actually changed
- Don't update deep-enrichment.md files — those require manual analysis
- Don't send Slack messages — this is a vault-only operation
- Don't modify anything in the `system/` directory
- Don't change `cpl_target` values — those come from client agreements, not performance data
- Don't use Slack-parsed CPL numbers when the DB has data for that client — DB is always more reliable
- Don't write to the DB during enrichment — the DB is read-only in this skill (writes happen via `pipeboard-cache.py ingest` in other workflows)
