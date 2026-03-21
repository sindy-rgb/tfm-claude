# Skills & Automations Build
**Last updated:** 2026-03-21
**Owner:** Jay / Claude Code
**Roadmap:** `research/skills-automation-roadmap.md`

## Current Status
8 of 10 roadmap skills built. All 3 additional recommendations done. First live test of `/portfolio-pulse` completed — pulled data from 19 accounts across all Pipeboard-connected clients.

## Work Items

### Roadmap Skills (10)

| # | Skill | Priority | Status | Notes |
|---|-------|----------|--------|-------|
| 1 | `/friday-autopilot` | P0 | not started | 13-node n8n workflow design doc at `research/n8n-friday-report-automation.md`. Blocker: Meta API tokens + spreadsheet ID placeholders. |
| 2 | `/creative-qa` | P0 | **done** | SKILL.md + PreToolUse hook (`creative-qa-gate.sh`). Keyword NEVER-rule gate + full AI-powered QA skill. |
| 3 | `/fatigue-scan` | P1 | **done** | SKILL.md at `~/.claude/skills/fatigue-scan/SKILL.md`. 14-day ad-level scan with kill/scale/iterate recs. |
| 4 | `/vault-integrity` | P1 | **done** | SKILL.md + PostToolUse hook (`validate-frontmatter.sh`). Schema validation, staleness, Slack cross-ref. |
| 5 | `/action-tracker` | P1 | **done** | SKILL.md at `~/.claude/skills/action-tracker/SKILL.md`. Day.ai extraction, overdue tracking, pre-call briefings. |
| 6 | `/lp-monitor` | P2 | not started | n8n daily + Playwright screenshots + CVR check. |
| 7 | `/portfolio-pulse` | P2 | **done + tested** | SKILL.md + first live run on 2026-03-21. Report at `reports/portfolio-pulse-2026-03-21.md`. |
| 8 | n8n Self-Healer | P2 | **done** | 12-node workflow JSON + design doc at `research/n8n-self-healer-workflow.md`. Ready for import into n8n. Needs credential setup (Anthropic API, Slack, n8n API key). |
| 9 | `/competitor-watch` | P3 | not started | Playwright + Meta Ad Library scraping. |
| 10 | `/onboard-client` | P3 | not started | End-to-end new client setup automation. |

### Additional Recommendations (3)

| # | Item | Status | Notes |
|---|------|--------|-------|
| 1 | Install `czlonkowski/n8n-skills` | **done** | 7 skill directories (35 files) installed. Repo at `~/.claude/n8n-skills-repo/`. |
| 2 | Add Claude Code hooks | **done** | 3 hooks: Slack audit trail (PreToolUse), creative-qa gate (PreToolUse), frontmatter validator (PostToolUse). |
| 3 | GSD context management pattern | **done** | `system/state/` dir, README, initial state file, CLAUDE.md updated. |

## Blockers
- `/friday-autopilot`: Need correct Meta API tokens and Google Sheets IDs
- n8n Self-Healer: Ready for import but needs Anthropic API credential, Slack OAuth2, and n8n API key configured in n8n instance
- Vendry, Jay Shetty, JWS: No Pipeboard access — need account permissions granted

## Decisions Made
- 2026-03-21: Adopted GSD-style context management (state files + sub-agents)
- 2026-03-21: Creative QA hook runs BEFORE audit trail hook on Slack sends (gate first, log second)
- 2026-03-21: Portfolio pulse uses `lead` or `complete_registration` or `fb_pixel_custom` as CPL event depending on client
- 2026-03-21: TPG ($179K/week) excluded from TFM-managed spend calculations (RV account, TFM is creative/strategy only)
- 2026-03-21: Status News $29 CPL flagged as likely tracking/pixel issue, not real performance

## Next Steps
1. Build `/friday-autopilot` n8n workflow (P0 — last P0 item)
2. Import n8n Self-Healer workflow and configure credentials
3. Build `/lp-monitor` (P2 — Playwright + CVR monitoring)
4. Build `/competitor-watch` (P3 — Meta Ad Library scraping)
5. Build `/onboard-client` (P3 — new client setup automation)
6. Investigate Status News pixel/tracking issue
7. Get Pipeboard access for Vendry, Jay Shetty, JWS
8. **Unified Performance DB** — ad-level Pipeboard backfill (Tier 2) as fatigue scans run organically; ESP integration as clients connect (Beehiiv first, then Sailthru/custom). Goal: join Meta ad performance with ESP engagement per UTM source.
9. Add ESP tables to `system/pipeboard-cache.py` (subscriber engagement by UTM source, open rates, click rates)

## Relevant Files
- `research/skills-automation-roadmap.md` — Full roadmap with specs
- `research/n8n-friday-report-automation.md` — Friday autopilot design doc
- `research/n8n-self-healer-workflow.md` — Self-healer workflow JSON + setup guide
- `reports/portfolio-pulse-2026-03-21.md` — First portfolio pulse report
- `~/.claude/skills/` — All installed skills (12 total)
- `.claude/hooks/` — All hooks (3 scripts)
- `.claude/settings.json` — Hook configuration + permissions
- `system/state/README.md` — State file conventions
