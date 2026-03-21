# The Feed Media — Claude Code Project Instructions

## Identity
You are assisting **Jay Warner, Director of Growth at The Feed Media**, a newsletter growth agency. TFM runs paid media (primarily Meta Ads) for 25 clients, managing creative strategy, media buying, and performance reporting.

## On Session Start
Before answering any client-specific question, read the relevant client file(s):
- Client intelligence files: `clients/[client-name]/[client-name].md`
- Master summary: `CLIENT-INTELLIGENCE-SUMMARY.md`
- Framework reference: `system/framework.md`

## Key Knowledge Files (Auto-Memory)
These are stored in project memory and persist across sessions:
- `memory/media-buying-sop.md` — Full media buying SOPs, DCT 4-3-2-2 method, CBO vs ABO strategy, Meta benchmarks, Nathan's training videos, client-specific campaign variations, Notion page links
- `memory/MEMORY.md` — Project structure, key people, external systems, pending items

## Client Intelligence Framework
Every client file follows the 6-category structure:
1. **Client Overview** — Contacts, stakeholders, status, ESP, channels
2. **North Star Metric** — Primary KPI + target, quality definition
3. **Brand Voice Rules** — NEVER rules first, approved language, failed copy quotes
4. **Winning Creative Signals** — Top formats with performance data
5. **Negative Triggers** — Charged client quotes, patterns to avoid
6. **Relationship Health** — Sentiment, risk level, continuity concerns

## Active Clients (25)
creator-spotlight, workweek, insight-links, status-news, stocks-news, the-points-guy, houck, rnt-fitness, daily-drop, open-source-ceo, jay-shetty, how-to-ai, points-path, experiential-hospitality, quartz, big-desk-energy, stocks-and-income, contrarian-thinking, marketbeat, 1636-forum, franklins-forum, just-womens-sports, vendry, student-loan-planner, mdhair

## TFM Team
- **Nathan May** — Agency Principal
- **Sindy** — Head of Operations
- **Rabii Elhaouat** — Media Buyer
- **Luiz Pekelman** — GM (MarketBeat, Quartz, Stocks & Income)
- **Natalie Rose** — GM (JWS, TPG)
- **Kinte Otieno** — GM (Creator Spotlight, RNT Fitness, TPG support)
- **Lays Paiva** — GM (WorkWeek, Jay Shetty, How to AI)
- **Mariely Galindo** — GM (1636 Forum, Franklin's Forum, Points Path, EH, Daily Drop, Status News)
- **Aubree Clark** — GM (Vendry, Student Loan Planner)
- **Noreen** — Reporting Analyst (Friday reports, ad account access)
- **Melvin** — Video Editor
- **Marc** — Static Designer

## External Tools & Access
- **Day.ai** — CRM, meeting recordings, workspace context notes (MCP access)
- **Notion** — Client pages, SOPs, concepts, creatives, training (MCP access)
- **Slack** — Internal/external client channels, DMs (MCP access)
- **Meta Ads** — Via Pipeboard MCP integration
- **Google Drive** — Creative folders, script spreadsheets, ad reports (MCP access via gdrive)
- **Google Calendar** — MCP access
- **Gmail** — MCP access
- **n8n** — Self-hosted workflow automation at `https://n8n-zwzfv-u62151.vm.elestio.app/`
- **GitHub** — Private repo at `thefeedmedia/tfm-vault` (synced via Obsidian Git)

## Creative QA Process
When QA'ing ad concepts:
1. **Pull scripts from Google Drive** (source of truth for copy)
2. **Cross-reference with Notion** (status/pipeline tracker)
3. **Check against client NEVER rules** from intelligence file
4. **Verify factual claims** (subscriber counts, math, percentages)
5. **Flag discrepancies** between Drive scripts and Notion entries
- Google Drive = what the copy actually says
- Notion = what the status/pipeline says
- If they disagree, Drive wins and Notion needs updating

## Media Buying Conventions
- **DCT** = Dynamic Creative Testing (one concept per ad set)
- **4-3-2-2** = 4 creatives, 3 primary texts, 2 headlines, 2 descriptions
- Default structure: Single CBO campaign + $10/day min per new ad set
- Broad targeting (Advantage+ Audience) unless client requires specific interests
- UTM format: `utm_source=facebookads&utm_medium={{adset.name}}&utm_campaign={{ad.name}}`
- Always add exclusion audiences (existing subs + website visitors)
- Landing page benchmark: 40%+ CVR for newsletters
- CPL benchmarks vary by client — check client file for specific targets

## Reporting & Communication
- Bi-weekly client calls with structured reports
- Friday weekly ad reports in Notion
- Internal Slack channels for each client (#internal-[client])
- External shared channels (#thefeed-[client])
- When drafting client-facing messages, follow the "being proactive and communicating well" framework

## Working With External Knowledge
When Jay shares URLs (YouTube, Reddit, articles, courses, Looms):
1. Fetch and read the content
2. Extract relevant media buying / newsletter growth insights
3. Save to `memory/external-media-buying-knowledge.md`
4. Reference in future sessions automatically

## Session Logging
At the end of every session (or when significant work is completed), update `memory/session-log.md` with:
- What was done and why
- Key decisions made
- What's pending
This log serves two purposes:
1. **Sindy briefings** — When Jay asks, generate a clean summary of recent work for Sindy
2. **Team SOPs** — Extract repeatable processes into team-facing documentation for Claude Chat usage

## Conventions
- Do not auto-commit without being asked
- Draft Slack messages (don't send) unless explicitly told to send
- Flag when client intelligence files need updating after new analysis
- Use DCT naming conventions from Notion when referencing ad concepts
- Always cross-reference ESP data (open rates, engagement) with Meta performance when available
