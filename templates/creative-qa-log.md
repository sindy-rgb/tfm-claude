---
type: qa-log
client: "<% tp.system.prompt("Client name") %>"
date: <% tp.date.now("YYYY-MM-DD") %>
reviewer: "<% tp.system.prompt("Your name") %>"
tags: [qa, creative]
---

# <% tp.system.prompt("Client name") %> — Creative QA Log

**Date:** <% tp.date.now("YYYY-MM-DD") %>
**Reviewer:** <% tp.system.prompt("Your name") %>

## Issues Found

| # | DCT | Issue Type | Severity | Description | Status |
|---|-----|-----------|----------|-------------|--------|
| 1 | | | | | Open |
| 2 | | | | | Open |
| 3 | | | | | Open |

### Issue Types
- `NEVER_RULE` — Violates client NEVER rules
- `COPY_DRIFT` — Script differs between Drive/Notion/live ad
- `MISSING_SCRIPT` — No script document in Google Drive
- `PLACEHOLDER` — Unfinished or placeholder copy
- `FACTUAL_ERROR` — Wrong subscriber count, stat, or claim
- `MISSING_CTA` — No clear call-to-action
- `DESIGN_QA` — Visual/formatting issues (typos, spacing, brand compliance)
- `TARGETING` — Audience mismatch or exclusion list issue

### Severity Levels
- `CRITICAL` — Must fix before launch / pull live ad immediately
- `WARNING` — Should fix soon, impacts performance or brand safety
- `INFO` — Minor issue, fix when convenient

## NEVER Rules Checked
- [ ] Reviewed all active NEVER rules from client intelligence file
- [ ] Cross-referenced live ad copy against approved scripts
- [ ] Verified factual claims (subscriber counts, stats, percentages)
- [ ] Checked UTM parameters are correct
- [ ] Confirmed exclusion audiences are up to date

## Wins / Good Catches
| DCT | What's Working | Notes |
|-----|---------------|-------|
| | | |

## Action Items
- [ ]
- [ ]
