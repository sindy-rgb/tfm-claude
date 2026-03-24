# TFM Claude Code Environment -- Complete Inventory Audit

**Audit date:** 2026-03-22
**Environment:** macOS Darwin 25.3.0, zsh shell

---

## 1. CLAUDE CODE SETUP

### Project Configuration File
- **Path:** `/Users/jay/Documents/the vault/the-feed-media/CLAUDE.md`
- **Status:** Comprehensive, 128 lines. Defines identity, 25 active clients, team roster (10+ members), external tools, skills, conventions, and state management.

### Settings Files (3 tiers)

**User-level:** `/Users/jay/.claude/settings.json`
- Plugin enabled: `skill-creator@claude-plugins-official`
- Default mode: `auto`
- Extensive allow-list: all core tools (Read, Write, Edit, Glob, Grep, WebSearch, WebFetch), Bash commands (git, ls, find, npm, node, python3, jq, curl, gh, brew, etc.), and full permissions for 10 MCP server namespaces (Slack, Notion, Day.ai, Pipeboard, Pipeboard_Meta_Ads, Google Calendar, Gmail, Hex, Coupler_io, gdrive)
- Deny-list: `rm -rf:*` and `rm -r /:*` only

**Project-level:** `/Users/jay/Documents/the vault/the-feed-media/.claude/settings.json`
- Hooks configured (see section 6)
- More restrictive allow-list than user-level: no wildcard MCP permissions, explicit per-tool grants
- Permissions cover: all core tools, targeted Bash commands, and specific MCP tools for gdrive, Notion (search/fetch/create/update), Slack (search/read/draft only -- no auto-send), Day.ai (search/read/workspace), Pipeboard_Meta_Ads (read-only), Google Calendar (list events), Gmail (search/read/thread)

**Local override:** `/Users/jay/Documents/the vault/the-feed-media/.claude/settings.local.json`
- Large file (~19K tokens) with broad wildcard permissions (`Bash(*)`, `mcp__claude_ai_Pipeboard__*`, `mcp__claude_ai_Slack__*`, etc.)
- Contains session-specific permission grants (accumulated from past approvals)
- Also includes `mcp__n8n-mcp__*`, `mcp__beehiiv__*`, `mcp__playwright__*` -- these are NOT in the project-level settings.json

**Gap:** The project-level settings.json does not include permissions for n8n-mcp, beehiiv, or playwright MCP servers. Only the local override file grants those. If the local override is cleared, those integrations break.

### Plugin
- **skill-creator** (claude-plugins-official) -- installed 2026-03-18, last updated 2026-03-21

---

## 2. MCP SERVERS AVAILABLE (12 confirmed)

Based on the deferred tools list and settings files:

| MCP Server | Namespace | Available Tools | Notes |
|---|---|---|---|
| **Slack** | `mcp__claude_ai_Slack__` | 12 tools (read channel/thread/profile, search, send message/draft, create/read/update canvas, schedule) | Drafts auto-allowed; sends gated by creative-qa hook |
| **Notion** | `mcp__claude_ai_Notion__` | 13 tools (search, fetch, create/update pages, create DB/view, get comments/users/teams, duplicate, move) | Full CRUD |
| **Day.ai** | `mcp__claude_ai_Day_AI__` | 15 tools (search, CRM schema, meeting recordings, workspace context, person/org/relationship CRUD, pages, skills, lists) | Read + write |
| **Pipeboard (Meta Ads)** | `mcp__claude_ai_Pipeboard__` | 40+ tools (get campaigns/adsets/ads/insights/creatives, create/update/duplicate campaigns/adsets/ads, upload images/videos, bulk operations, lead gen forms, catalogs, audience sizing) | Full Meta Ads management |
| **Google Drive** | `mcp__gdrive__` | 4 tools (search, read file, sheets read, sheets update cell) | Read + write cells |
| **Google Calendar** | `mcp__claude_ai_Google_Calendar__` | 9 tools (list events/calendars, get event, find meeting times, find free time, create/update/delete event, respond) | Full CRUD |
| **Gmail** | `mcp__claude_ai_Gmail__` | 7 tools (search, read message/thread, get profile, list labels/drafts, create draft) | Read + draft |
| **n8n** | `mcp__n8n-mcp__` | 5 tools (get node, get template, search nodes/templates, tools documentation, validate node/workflow) | Workflow design + validation |
| **Beehiiv** | `mcp__beehiiv__` | 1 tool (get-subscribers) | Subscriber data only |
| **Playwright** | `mcp__playwright__` | 20+ tools (navigate, click, fill form, screenshot, evaluate JS, file upload, drag, hover, etc.) | Full browser automation |
| **Hex** | `mcp__claude_ai_Hex__` | 4 tools (create/continue/get thread, search projects) | Listed in user settings but not in CLAUDE.md |
| **Coupler.io** | `mcp__claude_ai_Coupler_io__` | 4 tools (get data/dataflow/schema, list dataflows) | Listed in user settings but not in CLAUDE.md |

**Undocumented integrations:** Hex and Coupler.io are permitted in user-level settings but not mentioned anywhere in the CLAUDE.md or vault documentation.

---

## 3. n8n WORKFLOWS

- **Instance URL:** `https://n8n-zwzfv-u62151.vm.elestio.app/`
- **Hosting:** Elestio (unlimited executions, no overage charges)
- **MCP access:** n8n-mcp server provides workflow design, validation, and template tools

### Known Workflows/Designs

| Workflow | Status | Location |
|---|---|---|
| Friday report automation | Design doc only | `research/n8n-friday-report-automation.md` |
| n8n Self-Healer | Design doc + JSON ready | `research/n8n-self-healer-workflow.md` |
| YouTube transcript pipeline | Design doc + JSON | `research/n8n-youtube-transcript-pipeline.md` + `.json` |
| EH consolidated reporting | Planned | Referenced in session log |
| Insight Links quality dashboard | Broken | Mailchimp API key expired ~Mar 10 |

**Blockers:** The Self-Healer needs Anthropic API credential, Slack OAuth2, and n8n API key configured. The Friday automation needs correct Meta API tokens and spreadsheet IDs.

### n8n Skills Repo
- **Path:** `/Users/jay/.claude/n8n-skills-repo/` (7 skill directories, 35 files)
- Installed from `czlonkowski/n8n-skills`

---

## 4. LOCAL DATABASE

- **Path:** `/Users/jay/Documents/the vault/the-feed-media/system/data/pipeboard.db`
- **Size:** ~1.7 MB
- **Documentation:** `/Users/jay/Documents/the vault/the-feed-media/system/data/README.md` (thorough, 188 lines)

### Tables

| Table | Rows | Purpose |
|---|---|---|
| `account_mapping` | 25 | Client slug to Meta account ID + conversion type |
| `campaign_metrics` | 1,739 | Weekly/monthly campaign data (90-day window) |
| `ad_metrics` | 1,669 | Ad-level data (30-day window) |
| `snapshots` | 3,134 | Ingestion metadata |

### Views (4)

| View | Purpose |
|---|---|
| `v_latest_weekly` | Latest week's aggregated data per client |
| `v_wow_comparison` | Week-over-week comparison per client |
| `v_client_summary` | All-time summary per client |
| `v_stale_clients` | Clients with stale or missing data |

### Indexes: 7 indexes covering the main query patterns (client_slug, campaign_id, date_start, snapshot_id)

### Data Freshness (as of 2026-03-22)
- **campaign_metrics:** 23 of 24 clients have data through 2026-03-22 (today). Open Source CEO latest is 2026-03-21.
- **ad_metrics:** 23 clients have data through 2026-03-21 (1 day stale). Open Source CEO missing from ad_metrics.
- **Missing from DB entirely:** Vendry has an account mapping but zero data rows. Jay Shetty, 1636 Forum, Student Loan Planner, MDhair have no account mapping at all.

### Conversion Type Mapping (per account_mapping)
The DB stores per-client conversion types: lead (default for 12 clients), `offsite_conversion.fb_pixel_custom` (6 clients: big-desk-energy, creator-spotlight, EH, points-path, rnt-fitness, status-news), `complete_registration` (how-to-ai), `mobile_app_install` (stocks-news), custom events for franklins-forum and open-source-ceo.

### Known Issues
- TPG has 392/442 weekly rows with 0 conversions (weekly granularity vs Meta attribution windows)
- JWS similar pattern (118/138 rows with 0 conversions)
- Monthly compact rows capture conversions correctly, so the issue is weekly-level only

### Refresh Script
- **Path:** `/Users/jay/Documents/the vault/the-feed-media/system/data/refresh.sh`
- Generates a Claude Code prompt that uses Pipeboard MCP to pull data and write to SQLite
- Auto-execution is disabled by default (commented out)
- Supports `--client`, `--days`, `--dry-run` flags
- Has a log directory at `system/data/logs/`

---

## 5. SKILLS INVENTORY (7 skills)

All skills live in `/Users/jay/Documents/the vault/the-feed-media/skills/`.

| Skill | File | Lines | Status | Trigger Phrases |
|---|---|---|---|---|
| `/friday` | `skills/friday/SKILL.md` | ~589 | Built (V3) | "friday report", "weekly report", "draft reports" |
| `/weekly-enrichment` | `skills/weekly-enrichment/SKILL.md` | ~222 | Built | "enrich", "refresh CPLs", "weekly update", "Monday briefing" |
| `/creative-qa` | `skills/creative-qa/SKILL.md` | ~175 | Built | "creative QA", "check this copy", "review creative" |
| `/fatigue-scan` | `skills/fatigue-scan/SKILL.md` | ~333 | Built | "fatigue scan", "ad fatigue", "kill list" |
| `/vault-integrity` | `skills/vault-integrity/SKILL.md` | ~195 | Built | "vault integrity", "validate vault", "frontmatter check" |
| `/action-tracker` | `skills/action-tracker/SKILL.md` | ~216 | Built | "action tracker", "meeting actions", "what's overdue" |
| `/portfolio-pulse` | `skills/portfolio-pulse/SKILL.md` | ~284 | Built + Tested | "portfolio pulse", "portfolio dashboard", "total spend" |

### Not Yet Built (from roadmap)

| Skill | Priority | Status |
|---|---|---|
| `/friday-autopilot` (n8n workflow) | P0 | Design doc exists, blocked on API tokens |
| `/lp-monitor` | P2 | Not started (Playwright + CVR monitoring) |
| n8n Self-Healer | P2 | JSON + design doc ready, needs credential setup |
| `/competitor-watch` | P3 | Not started (Meta Ad Library scraping) |
| `/onboard-client` | P3 | Not started |

**Note:** Skills were migrated from `~/.claude/skills/` to the vault's `skills/` directory on 2026-03-22. The user-level skills directory at `~/.claude/skills/` now contains **zero** SKILL.md files (the glob returned empty), confirming the migration is complete.

---

## 6. HOOKS & AUTOMATION

### Claude Code Hooks (3 active)

**PreToolUse hooks (on Slack sends):**

1. **creative-qa-gate.sh** -- Blocks outgoing Slack messages that violate client NEVER rules. Keyword-matching against MarketBeat naming, nuclear imagery, stock predictions, subscriber count inconsistencies. Exits with code 2 to block, 0 to pass.
   - Known limitation: Channel ID resolution fails (passes through silently when Slack sends channel IDs instead of names)
   - Slug normalization covers all 25 client variations

2. **slack-audit-trail.sh** -- Logs all Slack sends/drafts to `.claude/hooks/slack-audit-log.jsonl`. Audit-only (never blocks). Captures timestamp, tool name, channel, thread_ts, and message preview (first 200 chars).
   - Current log: 1 entry (2026-03-22)
   - No log rotation mechanism

**PostToolUse hook (on file edits):**

3. **validate-frontmatter.sh** -- Validates YAML frontmatter on client intel files after Edit/Write. Checks 10 required fields (client, slug, gm, status, current_cpl, cpl_target, risk_level, sentiment, last_enriched, north_star_metric). Warns but never blocks (exit 0).
   - Also validates slug matches directory name, status enum, risk_level enum, CPL format, date format

**Stop hook:**

4. **check-deliverable-qa.sh** -- Runs on session stop. Checks if 3+ files were modified for any single client in the last 2 hours. If so, reminds to run `/deliverable-qa`.

### Cron Jobs
- None configured (`crontab -l` returns empty)

### GitHub Actions (2 workflows)

| Workflow | Trigger | What It Does |
|---|---|---|
| `lint.yml` | PR touching `*.md` | Markdown lint on clients/, system/, research/ |
| `validate-clients.yml` | PR touching `clients/**/*.md` | Checks frontmatter for required fields (client, status, gm) and config file presence |

### PR Template
- `.github/PULL_REQUEST_TEMPLATE.md` exists with a checklist (frontmatter, no sensitive data, naming conventions, NEVER rules, Dataview queries)

---

## 7. MEMORY SYSTEM

### In-Vault Memory
- **Path:** `/Users/jay/Documents/the vault/the-feed-media/memory/`
- **Files:** 4 total
  - `MEMORY.md` -- Index file (in vault but also linked from project memory)
  - `session-log.md` -- Session activity log (latest entry: 2026-03-22)
  - `external-ai-tooling-knowledge.md` -- External knowledge captures
  - `claude-memory-index.md` -- Memory index

### Project Memory (Claude Code auto-memory)
- **Path:** `/Users/jay/.claude/projects/-Users-jay-Documents-the-vault-the-feed-media/memory/`
- **Files:** 18 total, categorized as:
  - **Feedback (12):** Mailchimp access, fatigue scan context, Pipeboard filtering, report types, qualified over raw, qualification is TFM only, build guardrails not memory, no fabricated stats, verify subscriber counts, verify publish frequency, ICP title match over qualified field, Jake's manual quality scoring, Jake's 4-tier scoring system
  - **Reference (2):** n8n credentials, Google Sheets OAuth config
  - **Project (2):** Unified performance DB initiative, vault next steps
  - **Index (1):** MEMORY.md
  - **Uncategorized (1):** feedback_jake_4tier_scoring_system.md (not in MEMORY.md index)

**Gap:** 3 memory files are not listed in the MEMORY.md index: `feedback_icp_title_match_over_qualified_field.md`, `feedback_jake_manual_quality_scoring.md`, `feedback_jake_4tier_scoring_system.md`. These were likely added after the index was last updated.

---

## 8. GIT/GITHUB SETUP

- **Repo:** `https://github.com/thefeedmedia/tfm-vault.git` (private)
- **Branch:** `main`
- **Status:** Clean (no uncommitted changes)
- **Latest commit:** `29bfc8c` -- "vault backup: 2026-03-22 19:47:02"
- **Sync method:** Obsidian Git plugin (automated vault backups)
- **CI/CD:** 2 GitHub Actions workflows (markdown lint + client file validation, on PRs only)
- **No branch protection rules visible** from local config

---

## 9. SYSTEM STATE

- **Path:** `/Users/jay/Documents/the vault/the-feed-media/system/state/`
- **Convention doc:** `README.md` (well-defined GSD pattern)

### Active State Files

1. **skills-build.md** (last updated 2026-03-21)
   - Tracks 10-skill roadmap: 8 of 10 built, plus 3 additional recommendations (all done)
   - 3 skills not started: `/friday-autopilot` (n8n), `/lp-monitor`, `/competitor-watch`, `/onboard-client`
   - Blockers: Meta API tokens, n8n credentials, Pipeboard access for Vendry/Jay Shetty/JWS

2. **skills-qa-plan.md** (created 2026-03-21, status: APPLIED)
   - Comprehensive QA review of all 6 skills, 3 hooks, and pipeboard-cache.py
   - 4 P0 issues (all applied), 6 P1 issues (most applied), 8 P2 issues (partially addressed)
   - Documents all known bugs, fixes applied, and remaining improvements

---

## 10. TEMPLATES

**Path:** `/Users/jay/Documents/the vault/the-feed-media/templates/`

| Template | Purpose |
|---|---|
| `meeting-notes.md` | Meeting notes structure |
| `friday-report.md` | Friday report format |
| `new-client.md` | New client intel file template |
| `bi-weekly-prep.md` | Bi-weekly client call prep |
| `creative-qa-log.md` | Creative QA log format |
| `client-onboarding.md` | Client onboarding checklist |

Also in `/Users/jay/Documents/the vault/the-feed-media/system/`:
- `client-template.md` -- Client file template
- `client-config-template.md` -- Client config template
- `presentation-template.html` -- HTML presentation template

---

## 11. RESEARCH LIBRARY

**Path:** `/Users/jay/Documents/the vault/the-feed-media/research/`
**Files:** 26 documents covering:
- n8n workflow designs (friday automation, self-healer, youtube transcript pipeline)
- Meta ads playbooks (creative frameworks 2026, ad copywriting, media buying 2026)
- QA logs (v4 and v5)
- Friday report database research (3 batches)
- Skills automation roadmap
- Competitor ad copy swipe file
- Claude Code power user guide
- Various platform research (TikTok API, Obsidian Superbrain, shared workspace)

---

## 12. CLIENT COVERAGE

- **25 client directories** in `clients/` (matches the CLAUDE.md list)
- **25 account mappings** in the SQLite DB
- **5 clients not in account_mapping:** jay-shetty, 1636-forum, student-loan-planner, mdhair, workweek (parent -- but 5 sub-brands ARE mapped)
- **1 client with mapping but no data:** Vendry

---

## SUMMARY: WHAT'S WORKING

1. **7 Claude Code skills** -- all built, documented, and migrated to vault
2. **3 hooks** -- creative QA gate, Slack audit trail, frontmatter validator all active
3. **Local SQLite database** -- 25 accounts mapped, 1,739 campaign rows, 1,669 ad rows, 4 views, 7 indexes. Data current as of today for 23/24 clients.
4. **12 MCP servers connected** -- covering Slack, Notion, Day.ai, Pipeboard, Google Drive/Calendar/Gmail, n8n, Beehiiv, Playwright, plus Hex and Coupler.io
5. **GitHub integration** -- private repo with CI/CD (lint + client validation)
6. **State management** -- GSD pattern with 2 active state files
7. **Memory system** -- 18 project memory files + 4 in-vault memory files
8. **DB refresh tooling** -- `refresh.sh` script ready, though auto-execution disabled

## SUMMARY: GAPS AND ISSUES

1. **Permission inconsistency** -- n8n-mcp, beehiiv, and playwright are only permitted in settings.local.json (session accumulation), not in project-level settings.json. A fresh session without the local override would lose access to these.
2. **Undocumented MCP servers** -- Hex and Coupler.io are in user-level settings but not mentioned in CLAUDE.md.
3. **3 memory files missing from index** -- `feedback_icp_title_match_over_qualified_field.md`, `feedback_jake_manual_quality_scoring.md`, `feedback_jake_4tier_scoring_system.md`
4. **No cron automation** -- The refresh.sh script exists but no cron job is set up. DB refreshes are manual.
5. **n8n workflows not deployed** -- Self-healer and Friday automation are design docs only, blocked on credentials.
6. **Vendry has no data** -- Account mapping exists but zero rows in either metrics table.
7. **TPG/JWS weekly conversion gap** -- 88-89% of weekly rows show 0 conversions; only monthly compacts work for these clients.
8. **Creative QA hook channel ID resolution** -- When Slack sends channel IDs instead of readable names, the hook silently passes through.
9. **No log rotation** on the Slack audit trail JSONL file.
10. **3 roadmap skills not started** -- `/lp-monitor` (P2), `/competitor-watch` (P3), `/onboard-client` (P3)
11. **Insight Links quality dashboard broken** -- Mailchimp API key expired ~Mar 10; n8n workflow needs new key.
12. **EH GHL integration incomplete** -- PIT token obtained but returning 403; needs scope configuration in GHL admin panel.
13. **Duplicate skills at user level** -- The vault migration moved skills to `skills/`, but the original 7 n8n platform skills remain at `~/.claude/n8n-skills-repo/`. The `~/.claude/skills/` directory itself is now empty, which is correct.
