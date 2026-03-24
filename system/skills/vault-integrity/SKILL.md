---
name: vault-integrity
description: >
  Client file frontmatter validator for The Feed Media vault. Checks all 25 client files for
  required YAML fields, validates consistency between intel files and master summary,
  detects staleness, and cross-references CPLs against Slack reports. Use when the user says
  "vault integrity", "validate vault", "check frontmatter", "vault health", "are client files
  up to date", "stale files", "frontmatter check", "data consistency", or after bulk edits.
---

# Vault Integrity — Client File Validator

You are the data integrity checker for The Feed Media's (TFM) vault. You validate that all 25 client files have correct frontmatter, consistent data across files, and fresh CPL values. You catch drift before it degrades other skills.

## Why This Matters

Every other skill (weekly-enrichment, portfolio-pulse, fatigue-scan) reads client frontmatter to make decisions. If a `current_cpl` is stale, a `risk_level` is wrong, or a `gm` assignment is outdated, those skills produce bad output. This skill is the foundation that keeps everything else accurate.

## Usage

- `/vault-integrity` — Full validation run across all 25 clients
- `/vault-integrity [client-slug]` — Validate one client's files
- `/vault-integrity --slack` — Include Slack CPL cross-reference (slower, requires MCP)

## Constants

### Vault Root
The vault root is the working directory (i.e., the root of this repository). All paths below are relative to it.

### The 25 Client Slugs
creator-spotlight, workweek, insight-links, status-news, stocks-news, the-points-guy, houck, rnt-fitness, daily-drop, open-source-ceo, jay-shetty, how-to-ai, points-path, experiential-hospitality, quartz, big-desk-energy, stocks-and-income, contrarian-thinking, marketbeat, 1636-forum, franklins-forum, just-womens-sports, vendry, student-loan-planner, mdhair

### Valid TFM Team Members
Nathan May, Sindy, Rabii Elhaouat, Luiz Pekelman, Kinte Otieno, Lays Paiva, Mariely Galindo, Aubree Clark, Noreen, Melvin, Marc

### Required Frontmatter Fields

| Field | Type | Required | Validation Rules |
|-------|------|----------|-----------------|
| `client` | string | YES | Non-empty, matches display name |
| `slug` | string | YES | Non-empty, matches directory name exactly |
| `gm` | string | YES | Must be a valid TFM team member from the list above |
| `status` | enum | YES | One of: `active`, `paused`, `onboarding`, `churned` |
| `current_cpl` | number or "N/A" | YES | Non-negative if number. "N/A" acceptable for ROAS-primary clients |
| `cpl_target` | string | YES | Non-empty |
| `risk_level` | enum | YES | One of: `low`, `medium`, `high` |
| `sentiment` | string | YES | Non-empty |
| `last_enriched` | date | YES | Format YYYY-MM-DD |
| `north_star_metric` | string | YES | Non-empty |

## Execution Steps

### Phase 1: File Structure Validation

For each of the 25 client slugs:

1. Check that the directory `clients/[slug]/` exists
2. Check that the main intel file `clients/[slug]/[slug].md` exists
3. Check that `clients/[slug]/client-config.md` exists
4. Check for orphan directories not in the known client list

Report:
- PASS: Both files exist
- FAIL: Missing intel file or config file
- WARN: Orphan directory found

### Phase 2: Frontmatter Schema Validation

Read each `[slug].md` file's YAML frontmatter (between `---` markers) and validate every field from the table above:

- Present and non-empty
- `slug` matches the directory name
- `gm` is one of the valid GM names listed above
- `status` is one of: active, paused, onboarding, churned
- `current_cpl` is a non-negative number or the string "N/A"
- `risk_level` is one of: low, medium, high
- `last_enriched` matches YYYY-MM-DD format

Record each issue as FAIL (missing required field) or WARN (invalid value).

### Phase 3: Summary Cross-Reference

1. Read `CLIENT-INTELLIGENCE-SUMMARY.md` at the vault root
2. For each of the 25 client slugs, check the client appears in the summary
3. For each entry in the summary, check a corresponding directory exists
4. Compare values between intel file frontmatter and summary table:
   - `current_cpl` — flag any mismatch
   - `risk_level` — flag any mismatch
   - `gm` — flag any mismatch
5. Check for duplicate entries in the summary

### Phase 4: Staleness Check

For each client, examine the `last_enriched` date:

| Age | Status | Level |
|-----|--------|-------|
| 0-7 days | FRESH | PASS |
| 8-14 days | OK | PASS |
| 15-21 days | STALE | WARN |
| 22-30 days | VERY STALE | WARN (elevated) |
| 30+ days | CRITICAL | FAIL |
| Missing/unparseable | UNKNOWN | FAIL |

### Phase 5: Config File Validation

For each `client-config.md`, check:
- `meta_account_id` is present (if client has active ads)
- `gm_name` matches the intel file's `gm` field
- `slack_internal` channel is specified
- `kpi_primary` is specified
- `cpl_target` is consistent with intel file's `cpl_target`

### Phase 6: Slack CPL Cross-Reference (optional, --slack flag)

This phase only runs when `--slack` is passed or Slack MCP tools are available and requested.

For each active client:
1. Search `#internal-[slug]` for the most recent message containing "weekly report" or "N8N"
2. Extract the CPL/CAC value from that Slack message
3. Compare to frontmatter `current_cpl`

| Discrepancy | Level |
|-------------|-------|
| Within 10% | PASS |
| 10-25% | WARN |
| >25% | FAIL |

Special parsing patterns:
- N8N reports: `*CPL:* $X.XX (+Y.YY% WoW)`
- Workweek: look for V-CAC per newsletter
- MarketBeat: look for ROAS, not CPL
- MDhair: look for CAC
- Status News: look for Qualified Carrd cost
- Stocks.News: look for Cost Per Trial

### Phase 7: Generate Integrity Report

Output in this format:

```markdown
# Vault Integrity Report — [YYYY-MM-DD]

## Summary
| Check | Pass | Fail | Warn |
|-------|------|------|------|
| File Structure | X | X | X |
| Frontmatter Schema | X | X | X |
| Summary Sync | X | X | - |
| Staleness | X | X | X |
| Config Consistency | X | X | X |
| Slack CPL Sync | X | X | X |
| **Total** | **X** | **X** | **X** |

## Failures (Must Fix)
### [Category]
- **[client-slug]**: [description of failure]
  - Current value: [what's there]
  - Expected: [what should be there]
  - Fix: [suggested action]

## Warnings
### [Category]
- **[client-slug]**: [description of warning]

## All Clear (X clients)
[List of clients passing all checks]

## Recommendations
1. [Prioritized list of fixes]
2. [Suggest running /weekly-enrichment if many CPLs are stale]
```

Replace X with actual counts. If a phase was skipped, note "Skipped" in that row.

## Hook Integration

This skill pairs with a PostToolUse hook at `.claude/hooks/validate-frontmatter.sh` that runs after every Edit/Write to `clients/**/*.md`. The hook does lightweight field-presence checks in real time. This skill does the full deep validation.

## Error Handling

- If a client file can't be parsed (malformed YAML), report as FAIL with "frontmatter parse error"
- If CLIENT-INTELLIGENCE-SUMMARY.md doesn't exist, skip Phase 3 and note
- If Slack MCP is unavailable, skip Phase 6 and note
- Always complete the full run — don't stop at first error
- Count and report totals even if individual checks fail

## What NOT to Do

- Don't fix issues automatically — only report them (the user or /weekly-enrichment fixes)
- Don't modify any files — this is read-only analysis
- Don't send Slack messages
- Don't change `cpl_target` values
- Don't create new client directories
