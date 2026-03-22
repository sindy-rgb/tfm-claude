---
name: weekly-enrichment
description: >
  Weekly vault enrichment automation for The Feed Media. Pulls live CPL data from Slack weekly reports,
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

## Context: The Vault Structure

- **Client files:** `/the-feed-media/clients/[client-name]/[client-name].md` — each has YAML frontmatter with `current_cpl`, `risk_level`, `gm`, `status`, `sentiment`
- **Master summary:** `/the-feed-media/CLIENT-INTELLIGENCE-SUMMARY.md` — portfolio table with all 25 clients
- **Framework:** `/the-feed-media/system/framework.md` — the 6-category intelligence framework

## The 25 Clients and Their Slack Channels

Each client has an internal Slack channel where weekly reports land. The channel name pattern is `#internal-[clientslug]`. Search these channels for the most recent Friday report.

## Step-by-Step Process

### Phase 1: Read Current Vault State

1. Use Glob to find all client `.md` files matching `clients/*/[name].md`
2. Read the YAML frontmatter from each file — extract: `client`, `slug`, `gm`, `current_cpl`, `risk_level`, `status`, `sentiment`, `last_enriched`
3. Store these as your baseline for comparison

### Phase 2: Pull Live Data from Slack

For each client, search Slack for the most recent weekly ad report. Use `slack_search_public_and_private` with queries like:

```
weekly report after:[last-friday-date] in:#internal-[clientslug]
```

Or search for N8N bot posts:

```
from:N8N in:#internal-[clientslug]
```

From each report, extract:
- **CPL** (or CAC, CPSA, Cost Per Trial — whatever metric this client uses)
- **Spend** (total and WoW change)
- **Sign-ups/Leads** (volume)
- **Any flags** the GM or bot highlighted (CVR drops, creative fatigue, CPM spikes)

If no report is found in the internal channel, also check `#thefeed-[clientslug]` (the external channel where some GMs post reports directly to clients).

**Important parsing patterns:**
- N8N reports use format: `*CPL:* $X.XX (+Y.YY% WoW)`
- GM reports vary but always include a CPL/CAC figure
- Vendry uses CAD currency
- Status News tracks "Qualified Carrd" sign-ups, not raw CPL
- Stocks.News tracks "Cost Per Trial", not CPL
- MDhair tracks CAC (Customer Acquisition Cost), not CPL
- Workweek has 5 separate newsletters — pull Sub CAC for each
- Daily Drop splits BAU vs TFM performance

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

### Phase 4: Compare and Flag Changes

For each client, compare the Slack CPL to the frontmatter `current_cpl`:

- **>10% increase**: Flag as `CPL UP` — potential risk elevation
- **>10% decrease**: Flag as `CPL DOWN` — positive momentum
- **GM change detected**: Flag as `GM CHANGE`
- **Status change detected**: Flag as `STATUS CHANGE`
- **No report found**: Flag as `NO DATA` — check if client is paused or creative-only

Also check:
- Is the CPL now above the target? (compare to `cpl_target` in frontmatter) — if newly above target, consider elevating risk
- Is the CPL now below the target? — if newly below, consider lowering risk
- Any meeting recordings suggesting relationship changes?

### Phase 5: Update Client Files

For each client where data changed:

1. Edit the YAML frontmatter `current_cpl` to the new value
2. If risk level should change based on CPL movement, update `risk_level`
3. Update `last_enriched` to today's date
4. If GM changed, update `gm` field

Use the Edit tool for frontmatter updates — surgical replacements only, don't rewrite entire files.

### Phase 5b: Update Performance Cache

After extracting CPL data from Slack, ingest it into the SQLite cache for historical tracking:
```bash
python3 system/pipeboard-cache.py ingest <slug> campaign
```
This ensures the cache has weekly data points even between portfolio-pulse runs. The cache at `system/data/pipeboard.db` is the shared historical record for the whole team.

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

- If a Slack search returns no results for a client, note it but don't error out — some clients (like MDhair) don't have regular N8N reports
- If a client file can't be found, skip it and flag in the briefing
- If Day.ai is unreachable, proceed with Slack data only — the briefing is still valuable without meeting data
- Always complete the full run even if individual clients have issues

## What NOT to Do

- Don't rewrite entire client files — only update frontmatter values that actually changed
- Don't update deep-enrichment.md files — those require manual analysis
- Don't send Slack messages — this is a vault-only operation
- Don't modify anything in the `system/` directory
- Don't change `cpl_target` values — those come from client agreements, not performance data
