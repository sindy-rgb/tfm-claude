# TFM Vault Audit Report
**Generated:** 2026-03-22
**Scope:** Deep enrichment audit, Pipeboard cross-reference, vault structure review, research index update

---

## 1. DEEP ENRICHMENT FILE AUDIT (25 Clients)

All 25 clients have deep-enrichment.md files. Every file was generated on 2026-03-21.

### Section Coverage Matrix

| Client | Google Drive | Notion Concepts | Notion Creatives | Meta Ads Perf | Day.ai/CRM | Website/LP | Competitor Research | Overall |
|--------|:-----------:|:---------------:|:----------------:|:-------------:|:----------:|:----------:|:-------------------:|:-------:|
| 1636 Forum | FULL | FULL | FULL | FULL | FULL (11 recs) | FULL | FULL | COMPLETE |
| Big Desk Energy | FULL | FULL | FULL | PARTIAL (insights inaccessible) | PARTIAL (no recs) | PARTIAL (JS-rendered) | FULL | NEAR-COMPLETE |
| Contrarian Thinking | FULL | FULL | FULL | PARTIAL (from intel) | FULL (4 recs) | FULL | FULL | COMPLETE |
| Creator Spotlight | FULL | FULL | FULL | N/A (no Pipeboard) | PARTIAL (no recs) | PARTIAL (JS-rendered) | FULL | NEAR-COMPLETE |
| Daily Drop | FULL | FULL | FULL | PARTIAL (from intel) | FULL (11 recs) | FULL | FULL | COMPLETE |
| Experiential Hospitality | FULL | FULL | FULL | N/A (from intel) | PARTIAL (no Day.ai recs) | FULL | FULL | COMPLETE |
| Franklin's Forum | THIN (1 sheet, 1 folder) | FULL | PARTIAL | PARTIAL | PARTIAL (no recs) | FULL | FULL | ADEQUATE |
| Houck | FULL | FULL | FULL | PARTIAL (from intel) | PARTIAL (2 recs) | PARTIAL (JS-rendered) | FULL | NEAR-COMPLETE |
| How to AI | FULL | FULL | FULL | PARTIAL (insights inaccessible) | PARTIAL (no recs) | FULL | FULL | NEAR-COMPLETE |
| Insight Links | FULL | FULL | FULL | PARTIAL (from intel) | FULL (6 recs) | FULL (3 LPs) | FULL | COMPLETE |
| Jay Shetty | FULL | FULL | FULL | N/A (not in Pipeboard) | PARTIAL (no recs) | FULL | FULL | NEAR-COMPLETE |
| Just Women's Sports | THIN (1 folder) | FULL | FULL | PARTIAL | PARTIAL (no recs) | FULL | FULL | ADEQUATE |
| MarketBeat | FULL | FULL | FULL | PARTIAL (from intel) | PARTIAL (2 recs) | PARTIAL (403 blocked) | FULL | NEAR-COMPLETE |
| MDhair | FULL | FULL | FULL | N/A (no direct access) | PARTIAL (no recs) | FULL | FULL | NEAR-COMPLETE |
| Open Source CEO | PARTIAL (no DCT scripts) | FULL | FULL | N/A (not in Pipeboard) | PARTIAL (no recs) | FULL | FULL | NEAR-COMPLETE |
| Points Path | FULL | FULL | FULL | N/A (from intel) | PARTIAL (no recs) | FULL | FULL (6 competitors) | COMPLETE |
| Quartz | THIN (1 sheet only) | FULL | FULL | PARTIAL (insights inaccessible) | PARTIAL (no recs) | FULL | FULL | ADEQUATE |
| RNT Fitness | PARTIAL (no DCT scripts) | FULL | FULL | PARTIAL (from intel) | FULL (3 recs) | FULL | FULL | NEAR-COMPLETE |
| Status News | FULL | FULL | FULL | PARTIAL (from intel) | FULL (13 recs -- most of any client) | FULL | FULL | COMPLETE |
| Stocks & Income | PARTIAL (no report sheet) | FULL | FULL | PARTIAL (from intel) | FULL (7 recs) | PARTIAL (CSS only) | FULL | NEAR-COMPLETE |
| Stocks.News | FULL | FULL | FULL (22 concepts) | FULL (weekly report data) | PARTIAL (no recs) | FULL (2 sites + App Store) | FULL (5 competitors) | COMPLETE |
| Student Loan Planner | PARTIAL (folders only) | FULL | FULL (11 ICP campaigns) | N/A (not in Pipeboard) | PARTIAL (no recs) | FULL | FULL | NEAR-COMPLETE |
| The Points Guy | FULL (94 files, 20+ DCTs) | FULL (100+ concepts) | FULL | PARTIAL (from intel) | N/A (no recs surfaced) | FULL (2 pages) | FULL (6 competitors) | COMPLETE |
| Vendry | FULL | FULL (43+ DCTs) | FULL | PARTIAL (not in Pipeboard) | PARTIAL (no recs) | FULL (2 sites) | FULL | NEAR-COMPLETE |
| Workweek | PARTIAL (no DCT scripts) | FULL (22+ DCTs) | FULL | PARTIAL (5 accounts identified) | FULL (4 recs) | PARTIAL (LP not resolved) | FULL | NEAR-COMPLETE |

### Summary Statistics
- **COMPLETE** (all 7 sections substantive): 8 clients
- **NEAR-COMPLETE** (minor gaps in 1-2 sections): 14 clients
- **ADEQUATE** (thin in 2+ sections): 3 clients (Franklin's Forum, Just Women's Sports, Quartz)

### Common Gaps Across All Files
1. **Pipeboard insights were inaccessible** during the March 21 enrichment for most clients -- performance data was pulled from client intel files and Slack instead. The Pipeboard DB (built March 22) now has campaign-level data for 24 accounts.
2. **Day.ai meeting recordings** were not found for 12 of 25 clients. This is likely a tagging issue (recordings not linked to org domains) rather than missing data.
3. **Landing pages rendered via JavaScript** (beehiiv, Substack) could not be fully analyzed via WebFetch for 4 clients. Visual audits via Playwright recommended.
4. **No files reference being "last updated" with a date after 2026-03-21** -- all are current as of that date.

### Stale Numbers to Flag
All deep-enrichment files use performance data from the week of March 13-19, 2026. The following numbers will need updating by the next enrichment cycle:
- All CPL figures (volatile week-over-week)
- Subscriber counts (growing constantly)
- Budget pacing figures
- Sprint status (concepts in "Concept stage" will have progressed)
- Contrarian Thinking trial days remaining (stated as "~55 days" on 3/21 -- now ~54)

---

## 2. PIPEBOARD DB vs. CLIENT-CONFIG CROSS-REFERENCE

### Clients IN Pipeboard DB (20 account mappings covering 25 client slugs)

| Client Slug | DB Account ID | Config Account ID | Match | Conversion Type (DB) |
|-------------|---------------|-------------------|:-----:|----------------------|
| big-desk-energy | act_1402347147137781 | act_1402347147137781 | OK | offsite_conversion.fb_pixel_custom |
| contrarian-thinking | act_1329828287615052 | act_1329828287615052 | OK | lead |
| creator-spotlight | act_727705002666774 | act_727705002666774 | OK | offsite_conversion.fb_pixel_custom |
| daily-drop | act_593626712597229 | N/A (creative-only) | OK | lead |
| experiential-hospitality | act_1644253359451312 | act_1644253359451312 | OK | offsite_conversion.fb_pixel_custom |
| franklins-forum | act_1870272053696920 | **FIXED: was TBD** | FIXED | offsite_conversion.custom.2133776527360217 |
| houck | act_601589271801820 | act_601589271801820 | OK | lead |
| how-to-ai | act_816391071105542 | act_816391071105542 | OK | complete_registration |
| insight-links | act_507049163040180 | act_507049163040180 | OK | lead |
| just-womens-sports | act_472919260251410 | **FIXED: had partner ID only** | FIXED | lead |
| marketbeat | act_1129788478833121 | act_1129788478833121 | OK | lead |
| open-source-ceo | act_2116667552418074 | act_2116667552418074 | OK | offsite_conversion.custom.889821167133951 |
| points-path | act_1308877270502995 | act_1308877270502995 | OK | offsite_conversion.fb_pixel_custom |
| quartz | act_757128750591828 | act_757128750591828 | OK | lead |
| rnt-fitness | act_537505457933105 | act_537505457933105 | OK | offsite_conversion.fb_pixel_custom |
| status-news | act_455914147435901 | act_455914147435901 | OK | offsite_conversion.fb_pixel_custom |
| stocks-and-income | act_24102682642704582 | act_24102682642704582 | OK | lead |
| stocks-news | act_966430194860576 | act_966430194860576 | OK | mobile_app_install |
| the-points-guy | act_2130099530351734 | act_2130099530351734 | OK | lead |
| vendry | act_1283376772272478 | act_1283376772272478 | OK | lead |
| workweek-ftt | act_1079516909306359 | act_1079516909306359 | OK | lead |
| workweek-gtm | act_4673797136057796 | act_4673797136057796 | OK | lead |
| workweek-hospitalogy | act_718612189266939 | act_718612189266939 | OK | lead |
| workweek-ihih | act_3186358998360632 | act_3186358998360632 | OK | lead |
| workweek-tmm | act_579954186820640 | act_579954186820640 | OK | lead |

### Clients NOT in Pipeboard DB (4 clients)
| Client | Reason | Config Status |
|--------|--------|---------------|
| 1636 Forum | Not in Pipeboard accessible accounts | Config notes act_2257251771354778 from deep-enrichment (may be new/migrated) |
| Jay Shetty | Account under Jay Shetty team's own Business Manager | Config correctly documents this |
| MDhair | Creative-only engagement -- no direct ad account access | Config correctly documents N/A |
| Student Loan Planner | Account under client's Business Manager | **FIXED: updated ad_account_type to "Partner access"** |

### Config Fixes Applied
1. **franklins-forum/client-config.md**: `meta_account_id` updated from "TBD" to `act_1870272053696920` (confirmed in Pipeboard DB)
2. **just-womens-sports/client-config.md**: `meta_account_id` updated to include actual account ID `act_472919260251410` alongside partner ID
3. **just-womens-sports/client-config.md**: `cpl_target` current value updated from $1.17 to $2.32 (stale data)
4. **student-loan-planner/client-config.md**: `meta_account_id` note updated; `ad_account_type` changed from "TFM-managed" to "Partner access (client-owned Business Manager)"

### Conversion Type Documentation Gap
The Pipeboard DB tracks conversion_type per account, but **no client-config.md files document conversion_type**. This is a structural gap. The conversion types vary significantly:
- **lead** (12 accounts): Standard Meta lead event
- **offsite_conversion.fb_pixel_custom** (6 accounts): Custom pixel event
- **offsite_conversion.custom.[ID]** (2 accounts): Named custom conversions (Franklin's Forum, Open Source CEO)
- **complete_registration** (1 account): How to AI
- **mobile_app_install** (1 account): Stocks.News

Recommendation: Add a `conversion_type` field to the client-config template and backfill for all clients.

---

## 3. CLIENT-INTELLIGENCE-SUMMARY.md UPDATES

### Corrections Applied
1. **Claude Chat Project column**: MDhair and Student Loan Planner both have claude-chat-project.md files (verified on disk). Updated from "--" to "Yes" in the table. Summary count updated from "23 clients" to "25 clients."

### CPL Values (Current as of Mar 13-19 -- No DB-based update needed)
The summary already reflects the Mar 13-19 CPL data. The Pipeboard DB has campaign_metrics and ad_metrics tables but these contain spend/impression/click data, not pre-computed CPL values. The CPLs in the summary were sourced from Slack weekly reports during the March 21 enrichment and remain the most accurate source.

---

## 4. VAULT STRUCTURE AUDIT

### File Inventory Per Client Directory

Every client directory contains these standard files:
- `[slug].md` -- Client intelligence file (6-category framework)
- `client-config.md` -- Machine-readable configuration
- `deep-enrichment.md` -- Deep research report
- `claude-chat-project.md` -- Claude Chat project instructions

**25/25 clients have all 4 standard files.** No missing standard files.

### Extra Files by Client
| Client | Extra Files | Assessment |
|--------|-------------|------------|
| daily-drop | `ROI by Campaign 3 11 26.xlsx` | Client data file -- appropriate |
| experiential-hospitality | 13 extra files (CSVs, JSON, HTML, n8n workflows) | Heavy but justified -- GHL integration, n8n backfill workflows, funnel data |
| marketbeat | `growjoy-competitive-analysis-march2026.md` | Competitive research -- appropriate |
| quartz | 12 extra files (Delivra scripts, screenshots, raw data folder) | Delivra API investigation artifacts. Consider archiving `.py` scripts to `scripts/` |
| status-news | 2 extra files (CSV export, client update email draft) | Operational data -- appropriate |
| stocks-and-income | `lead-magnet-strategy.md` | Strategy doc -- appropriate |
| the-points-guy | `Newsletter Paid Social 2026-03-17 13_08.pdf` | Client-shared report -- appropriate |

### Root-Level Files
| File | Assessment |
|------|------------|
| `2026-03-21.md` | Empty (0 bytes) -- Obsidian daily note placeholder. Orphan. |
| `2026-03-23.md` | Empty (0 bytes) -- Obsidian daily note placeholder. Orphan. |
| `Untitled.base` | Empty Obsidian Bases file. Orphan. |
| `Untitled.canvas` | Near-empty Obsidian Canvas file (2 bytes). Orphan. |
| `3-day-build-summary-2026-03-19-22.pdf` | Build summary PDF -- should be in `reports/` |
| `lays-obsidian-onboarding.pdf` | Team onboarding doc -- should be in `team/` |

### Orphan Files Identified
1. `/2026-03-21.md` -- Empty daily note, can be deleted
2. `/2026-03-23.md` -- Empty daily note, can be deleted
3. `/Untitled.base` -- Empty Bases file, can be deleted
4. `/Untitled.canvas` -- Empty Canvas file, can be deleted
5. `/3-day-build-summary-2026-03-19-22.pdf` -- Misplaced (should be in `reports/`)
6. `/lays-obsidian-onboarding.pdf` -- Misplaced (should be in `team/`)

### Quartz Delivra Files
The `/clients/quartz/` directory contains 12 Delivra-related files that were artifacts of the API investigation (March 17-18). These are:
- `delivra-analyze.py`, `delivra-export.py`, `delivra-focused-pull.py` -- Python scripts
- `delivra-n8n-all-in-one.js`, `delivra-n8n-code-debug.js`, `delivra-n8n-code.js`, `delivra-n8n-config.js`, `delivra-n8n-final.js`, `delivra-n8n-test.js` through `delivra-n8n-test4.js` -- n8n JavaScript nodes
- `delivra-raw/` -- Raw API response data
- `delivra-api-v2-plan.md`, `delivra-export-results.md`, `delivra-verification-report.md` -- Documentation
- `image (19).png`, `Screenshot 2026-03-17 at 2.55.41 PM.png` -- Screenshots

Recommendation: Keep `delivra-n8n-config.js` (active credentials), `delivra-verification-report.md` (reference), and the screenshots. Archive the rest to a `quartz/delivra-archive/` subdirectory.

### Directory Naming Consistency
All 25 client directories use the correct slug format matching CLAUDE.md's active clients list. No naming inconsistencies found.

---

## 5. RESEARCH DIRECTORY INDEX

### Files in `/research/` (23 files)

| File | Status | Notes |
|------|--------|-------|
| `skills-automation-roadmap.md` | **UPDATED** | Added build status for 7/10 skills now built (P0: both built, P1: all 3 built, P2: portfolio-pulse built) |
| `n8n-friday-report-automation.md` | Partially outdated | Describes 13-node workflow design; the `/friday` skill V3 (547 lines) was built on 2026-03-22 and supersedes this |
| `n8n-youtube-transcript-pipeline.md` | Current | 4-node n8n workflow spec -- not yet deployed |
| `n8n-youtube-transcript-workflow.json` | Current | Importable JSON for above -- ready to deploy |
| `n8n-self-healer-workflow.md` | Current | From Simon Scrapes research -- not yet built |
| `meta-ads-media-buying-2026.md` | Current | Reference material |
| `meta-creative-frameworks-2026.md` | Current | Reference material |
| `friday-report-database.md` | Current | Phase 1 DB schema documentation |
| `friday-report-database-batch2.md` | Current | Phase 2 expansion |
| `friday-report-database-batch3.md` | Current | Phase 3 expansion |
| `gm-friday-report-scorecard.md` | Current | GM performance tracking framework |
| `qa-log-v4.md` | Current | QA training reference |
| `qa-log-v5.md` | Current | Latest QA training reference |
| `claude-code-power-user-guide.md` | Current | Internal reference |
| `claude-extensions-connectors.md` | Current | MCP/extension research |
| `ad-transcript-automation-research.md` | Current | Research for ad transcript pipeline |
| `github-obsidian-improvements.md` | Current | Vault sync improvements |
| `obsidian-superbrain-research.md` | Current | Smart Connections research |
| `smart-connections-config-guide.md` | Current | Configuration reference |
| `shared-workspace-research.md` | Current | Team workspace research |
| `parker-ai-rebuild-competitive-research.md` | Current | Competitive intelligence |
| `presentation-best-practices.md` | Current | Reference material |
| `tiktok-api-trend-discovery-research.md` | Current | TikTok research |

### Research Files Assessment
- 22/23 files are current or reference material that remains valid
- 1 file updated: `skills-automation-roadmap.md` (added build status column)
- `n8n-friday-report-automation.md` is superseded by the built `/friday` V3 skill but retains value as design documentation

---

## 6. RECOMMENDATIONS

### Immediate (no changes made -- flagging for manual decision)

1. **Delete orphan files**: `2026-03-21.md`, `2026-03-23.md`, `Untitled.base`, `Untitled.canvas` -- all empty
2. **Move misplaced files**: `3-day-build-summary-2026-03-19-22.pdf` to `reports/`, `lays-obsidian-onboarding.pdf` to `team/`
3. **Archive Quartz Delivra scripts**: Move test scripts and raw data to `quartz/delivra-archive/`
4. **Add conversion_type to client-config template**: Important for `/friday` skill and Pipeboard automation

### Next Enrichment Cycle

5. **Tag Day.ai recordings to organizations**: 12 of 25 clients have no meeting recordings linked to their org domain in Day.ai
6. **Pull Pipeboard campaign-level data**: Now that the DB exists with 1,739 campaign rows, the next enrichment can use DB data instead of Slack reports
7. **Screenshot JS-rendered landing pages**: Use Playwright MCP for beehiiv/Substack pages that WebFetch cannot render
8. **Get 1636 Forum into Pipeboard**: The account act_2257251771354778 (referenced in deep-enrichment) should be verified and added to the account_mapping table
9. **Thin client deep-enrichments**: Franklin's Forum, Just Women's Sports, and Quartz have notably thinner Google Drive sections -- consolidate creative scripts into Drive for continuity

---

*Report generated 2026-03-22 by Claude Code. Cross-referenced: 25 deep-enrichment files, 25 client-config files, 25 client directories, Pipeboard DB (25 account mappings, 1,739 campaigns), CLIENT-INTELLIGENCE-SUMMARY.md, 23 research files, vault root structure.*
