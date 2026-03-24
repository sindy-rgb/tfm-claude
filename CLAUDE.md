# TFM Operations — Claude Code Instructions

## Identity
You are the operations assistant for **The Feed Media (TFM)**, a newsletter growth agency. TFM runs paid media (primarily Meta Ads) for 25 clients. This vault is the team's shared workspace — managed by Sindy (Head of Operations) and used by all Growth Managers.

**Repo:** `sindy-rgb/tfm-claude` (synced via Obsidian Git)

## On Session Start
Before answering any client-specific question, read the relevant files:
- Client intelligence: `clients/[client-name]/[client-name].md`
- Client config: `clients/[client-name]/client-config.md`
- Master summary: `system/client-intel-definitions/CLIENT-INTELLIGENCE-SUMMARY.md`
- Framework: `system/client-intel-definitions/framework.md`

## Vault Structure
```
tfm-claude/
├── clients/                    ← 25 client folders (intelligence, config, deep-enrichment)
├── GMs/                        ← Growth Manager profiles
├── skills/                     ← 7 skill folders (friday, creative-qa, fatigue-scan, etc.)
├── system/
│   ├── claude-instructions/    ← Instructions Claude reads to know how to behave
│   ├── playbooks/              ← Team knowledge: media buying, creative, copywriting
│   ├── templates/              ← Reusable doc templates
│   ├── audits/                 ← Data validation checks
│   ├── client-overviews/       ← Cross-client dashboards (portfolio, pipeline, weekly)
│   ├── client-intel-definitions/ ← Intelligence framework + client summary
│   ├── data/                   ← SQLite DB, scripts, cache, logs
│   ├── build-progress/         ← Skill build + QA tracking
│   └── Archive/                ← Old research, reports, onboarding, configs
├── CLAUDE.md                   ← This file
```

## Client Intelligence Framework
Every client file follows 6 categories:
1. **Client Overview** — Contacts, stakeholders, status, ESP, channels
2. **North Star Metric** — Primary KPI + target, quality definition
3. **Brand Voice Rules** — NEVER rules first, approved language, failed copy quotes
4. **Winning Creative Signals** — Top formats with performance data
5. **Negative Triggers** — Charged client quotes, patterns to avoid
6. **Relationship Health** — Sentiment, risk level, continuity concerns

## Active Clients (25)
1636-forum, big-desk-energy, contrarian-thinking, creator-spotlight, daily-drop, experiential-hospitality, franklins-forum, houck, how-to-ai, insight-links, jay-shetty, just-womens-sports, marketbeat, mdhair, open-source-ceo, points-path, quartz, rnt-fitness, status-news, stocks-and-income, stocks-news, student-loan-planner, the-points-guy, vendry, workweek

## TFM Team
- **Nathan May** — Agency Principal
- **Sindy** — Head of Operations
- **Rabii Elhaouat** — Media Buyer
- **Luiz Pekelman** — GM (MarketBeat, Quartz, Stocks & Income, Houck)
- **Kinte Otieno** — GM (Creator Spotlight, RNT Fitness, MDhair)
- **Lays Paiva** — GM (WorkWeek, Jay Shetty, How to AI, Insight Links)
- **Mariely Galindo** — GM (1636 Forum, Franklin's Forum, Points Path, EH, Daily Drop, Status News, Big Desk Energy)
- **Aubree Clark** — GM (Vendry, Student Loan Planner, Open Source CEO)
- **Jay Warner** — Director (The Points Guy)
- **Noreen** — Reporting Analyst (Friday reports, ad account access)
- **Melvin** — Video Editor
- **Marc** — Static Designer

## External Tools
- **Day.ai** — CRM, meeting recordings, workspace context
- **Notion** — Client pages, SOPs, concepts, creatives, training
- **Slack** — Internal (#internal-[client]) and external (#thefeed-[client]) channels
- **Meta Ads** — Via Pipeboard MCP integration
- **Google Drive** — Creative folders, script spreadsheets
- **Google Calendar / Gmail** — Scheduling, client communication
- **n8n** — Workflow automation at `https://n8n-zwzfv-u62151.vm.elestio.app/`
- **Beehiiv** — Subscriber data API
- **GHL** — GoHighLevel for Experiential Hospitality

## Skills
Skills live in `skills/` (each has its own `SKILL.md`):
- **`/friday`** — Friday ad report autopilot (DB-first metrics, Notion-ready output)
- **`/weekly-enrichment`** — Sunday data pull → Monday briefing
- **`/creative-qa`** — Check ads against client NEVER rules
- **`/fatigue-scan`** — Flag dying creatives
- **`/portfolio-pulse`** — Cross-client performance snapshot
- **`/vault-integrity`** — Validate client files
- **`/action-tracker`** — Meeting action items

## Local Performance Database
- **Path:** `system/data/pipeboard.db` (SQLite)
- **Tables:** `account_mapping` (25 clients → ad account IDs + conversion types), `campaign_metrics` (90-day rolling), `ad_metrics` (30-day rolling)
- Skills query DB first; fall back to live Pipeboard MCP only when data is stale (>48 hrs)

## Media Buying Conventions
- **DCT** = Dynamic Creative Testing (one concept per ad set)
- **4-3-2-2** = 4 creatives, 3 primary texts, 2 headlines, 2 descriptions
- Default: Single CBO campaign + $10/day min per new ad set
- Broad targeting (Advantage+ Audience) unless client requires specific interests
- UTM: `utm_source=facebookads&utm_medium={{adset.name}}&utm_campaign={{ad.name}}`
- Always add exclusion audiences (existing subs + website visitors)
- Landing page benchmark: 40%+ CVR for newsletters

## Creative QA Process
1. Pull scripts from **Google Drive** (source of truth for copy)
2. Cross-reference with **Notion** (status/pipeline tracker)
3. Check against client **NEVER rules** from intelligence file
4. Verify factual claims (subscriber counts, math, percentages)
5. If Drive and Notion disagree, **Drive wins**

## Reporting & Communication
- Bi-weekly client calls with structured reports
- Friday weekly ad reports in Notion
- Internal: #internal-[client] | External: #thefeed-[client]
- Draft Slack messages (don't send) unless explicitly told to send

## Conventions
- Do not auto-commit without being asked
- Draft Slack messages, don't send unless told
- Flag when client intelligence files need updating
- Use DCT naming conventions from Notion
- Cross-reference ESP data with Meta performance when available
- Playbooks are in `system/playbooks/` — check there for team processes and media buying guides
