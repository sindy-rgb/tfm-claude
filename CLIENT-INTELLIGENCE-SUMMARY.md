# The Feed Media — Client Intelligence System Update
### March 21, 2026

---

## What Was Done

We ran a full client intelligence enrichment across **all 25 active clients**, pulling data from four sources and writing it back to three systems. This includes 6 new clients built from scratch today (1636 Forum, Franklin's Forum, Just Women's Sports, Vendry, Student Loan Planner, MDhair).

### Sources Pulled (Per Client)
1. **Day.ai** — Organization records, meeting recording transcripts, contacts, opportunities, action items
2. **Slack** — Internal channels (#internal-[client]), external channels (#thefeed-[client]), pod channels, DMs
3. **Notion** — Client pages, onboarding docs, OneSheets, creative playbooks, bi-weekly meeting notes, weekly ad reports, creative briefs
4. **Google Drive** — Weekly ad report spreadsheets, creative assets, shared folders (MCP access live)

### Where It Was Written
1. **Day.ai** — Each client's organization record has a workspace context note titled "[Client Name] — Client Intelligence (Updated March 2026)" containing the full 6-category framework
2. **Local files** — Each client has a markdown file at `/the-feed-media/clients/[client-name]/[client-name].md`
3. **GitHub + Obsidian** — All local files are synced via the `thefeedmedia/tfm-vault` GitHub repo using Obsidian Git. All 25 client files have YAML frontmatter for Obsidian Bases compatibility.

---

## The 6-Category Framework (Per Client)

Every client file follows the same structure:

| # | Category | What It Contains |
|---|----------|-----------------|
| 1 | **Client Overview** | Contacts, stakeholders, status, ESP, funnel type, revenue model, Slack channels, key links |
| 2 | **North Star Metric** | Primary KPI + target, quality definition, client quotes, flags for CPL-only misconceptions |
| 3 | **Brand Voice Rules** | NEVER rules first, approved language, tone, quotes on failed copy |
| 4 | **Winning Creative Signals** | Top 2-3 formats with performance data + why they work |
| 5 | **Negative Triggers** | Most charged client quote, patterns to avoid, specific creative kills |
| 6 | **Relationship Health** | Sentiment trend, outreach timing, continuity risk, creative involvement |

---

## All 25 Clients

| # | Client | GM | Status | Risk Level | CPL Target | Current CPL | ESP | Deep Enrichment | Claude Chat Project |
|---|--------|----|--------|------------|------------|-------------|-----|:-:|:-:|
| 1 | 1636 Forum | Mariely Galindo | Active | MEDIUM | $2.00 | $3.01 | beehiiv | -- | -- |
| 2 | Big Desk Energy | Mariely | Active | LOW-MEDIUM | $3.00 | $2.30 | beehiiv | -- | Yes |
| 3 | Contrarian Thinking | Luiz Pekelman | Active | MEDIUM | $5-6 | $4.96 | beehiiv | -- | Yes |
| 4 | Creator Spotlight | Kinte Otieno | Active | MEDIUM | MAR >4 (quality) | $2.19 | beehiiv | Yes | Yes |
| 5 | Daily Drop | Mariely | Creative Only | LOW-MEDIUM | $3-$4 | $4.26 | N/A (client-managed) | -- | Yes |
| 6 | Experiential Hospitality | Mariely | Active | LOW-MEDIUM | $5.00 | $5.20-$5.30 | GoHighLevel | Yes | Yes |
| 7 | Franklin's Forum | Mariely Galindo | Active | MEDIUM | $3.00-$3.50 | $4.03 | beehiiv | -- | -- |
| 8 | Houck (Founding Journey) | Luiz Pekelman | Active | MODERATE-LOW | $5-$15 | $1.80 | beehiiv | -- | Yes |
| 9 | How to AI | Lays Paiva | Active | LOW-MEDIUM | $1.50-$2.50 | $2.28 | Substack | -- | Yes |
| 10 | Insight Links | Lays | Active | MEDIUM-LOW | Qualified CPL < $20 | $16.24 blended | Mailchimp | -- | Yes |
| 11 | Jay Shetty | Lays Paiva | Active | LOW-MEDIUM | $3.00 | $0.91 gross / $0.36 net | beehiiv | -- | Yes |
| 12 | Just Women's Sports | TBD — reassignment pending | Active | LOW-MEDIUM | $1.50 | $1.17 | beehiiv | -- | -- |
| 13 | MarketBeat | Luiz Pekelman | Active | LOW-MEDIUM | $10-14 | $8.86 | Custom (in-house) | -- | Yes |
| 14 | MDhair | Kinte | Active | MEDIUM | $80 CAC | $130 CAC (testing) | N/A (DTC) | -- | -- |
| 15 | Open Source CEO | Aubree Clark | Active | LOW-MEDIUM | $3.50 | ~$3.50+ (trending down) | beehiiv | -- | Yes |
| 16 | Points Path | Mariely | Active | LOW | $1.50-$2.00 | $1.78 | Kit | Yes | Yes |
| 17 | Quartz | Mariely | Active | MEDIUM | $2.50 | $3.55 | Delivra | -- | Yes |
| 18 | RNT Fitness | Kinte Otieno | Active | MEDIUM | Unconfirmed | GBP 1.00 | beehiiv | -- | Yes |
| 19 | Status (News) | Mariely | At Risk | HIGH | $1-$2 raw / ICP-Verified | $38.42 per 1P / ~$125 ICP | beehiiv | -- | Yes |
| 20 | Stocks & Income | Luiz Pekelman | Active | MEDIUM | $2.00 | $3.70 | beehiiv | -- | Yes |
| 21 | Stocks.News | Luiz Pekelman | Active | LOW-MEDIUM | Cost Per Trial < $60 | $57.38 per trial | N/A (app-based) | Yes | Yes |
| 22 | Student Loan Planner | Aubree Clark | Active | MEDIUM-HIGH | $15-20 | $18.82 | Kit (ConvertKit) | -- | -- |
| 23 | The Points Guy | Jay Warner | Active | MODERATE | $3.50-$4.50 | ~$2.80 | N/A (Red Ventures) | Yes | Yes |
| 24 | Vendry (Case Studied) | Aubree Clark | Active | MEDIUM | $2-6 CAD | $411.65 CAD (DR) / $13.38 CAD (NL) | beehiiv | -- | -- |
| 25 | Workweek | Lays Paiva | Active | LOW | $6-$9.50 V-CAC | IHIH $6.08 / TMM $6.09 / FTT $5.78 / Hosp $6.30 / GTM $4.24 | Sailthru | -- | Yes |

### Summary Counts
- **25 total clients** (24 Active + 1 At Risk)
- **5 clients with deep-enrichment.md** files: TPG, Stocks.News, Creator Spotlight, Experiential Hospitality, Points Path
- **19 clients with Claude Chat project instructions** (missing: 1636 Forum, Franklin's Forum, JWS, Vendry, SLP, MDhair)
- **6 clients built from scratch on March 21:** 1636 Forum, Franklin's Forum, Just Women's Sports, Vendry, Student Loan Planner, MDhair
- **All 25 client files** have YAML frontmatter for Obsidian Bases
- **QA logs V1-V5** exist documenting data integrity checks across the enrichment process

---

## How To Access This Going Forward

### For Any Team Member
1. **Day.ai** — Open the client's organization record and look for the "Client Intelligence" context note
2. **Local files** — Navigate to `/the-feed-media/clients/[client-name]/[client-name].md`
3. **GitHub** — All files sync via the `thefeedmedia/tfm-vault` repo using Obsidian Git

### For Claude Projects (Per Client)
Use **Prompt 3** from the Master Prompt Library to set up Claude Project memory from the Day.ai context note. This creates 6 memory entries (one per category) so Claude has full client context in any project chat. Claude Chat project instructions exist for 19 of 25 clients in `clients/claude-chat-project-instructions.md`.

### For Claude Code Sessions
Use **Prompt 4** (single client) or **Prompt 5** (cross-client) from the Master Prompt Library:
```
Read the following files before responding to anything:
- /the-feed-media/clients/[CLIENT-NAME]/[CLIENT-NAME].md
- /the-feed-media/system/framework.md
```

### To Update After New Analysis
Use **Prompt 6** from the Master Prompt Library to replace client file content after completing a fresh analysis.

### To Re-Run This Full Audit
Run the same process in Claude Code — it will pull from Day.ai, Slack, Notion, and Google Drive, synthesize the 6-category framework, write back to Day.ai, and save local markdown files synced via GitHub.

---

## Key Flags Across The Portfolio

### HIGH Risk
- **Status (News)** — $38.42 per 1P sub / ~$125 per ICP-Verified. Approaching critical.

### MEDIUM-HIGH Risk
- **Student Loan Planner** — $18.82 CPL against $15-20 target. Account under pressure, Aubree managing.

### MEDIUM Risk
- **1636 Forum** — New client, CPL $3.01 vs $2.00 target. Testing phase.
- **Franklin's Forum** — New client, CPL $4.03 vs $3.00-$3.50 target. Testing phase.
- **Contrarian Thinking** — CPL $4.96 tracking within $5-6 range. Momentum building.
- **Creator Spotlight** — Quality-focused (MAR >4), not CPL-driven. GM transition to Kinte.
- **MDhair** — DTC client, $130 CAC vs $80 target. Creative-only retainer, operational risk.
- **Quartz** — CPL $3.55 vs $2.50 target. Bake-off context.
- **RNT Fitness** — KPIs still unconfirmed. GBP 1.00 CPL.
- **Stocks & Income** — CPL $3.70 vs $2.00 target. Needs attention.
- **Vendry** — DR funnel at $411.65 CAD, newsletter at $13.38 CAD. Strategic pivot in progress.

### Stable / Low Risk
- **Workweek** — All 5 newsletters green. Peak moment.
- **Houck** — CPL $1.80, well under $5-$15 range. Momentum building.
- **Jay Shetty** — CPL $0.91 gross. Strong but emerging financial tension.
- **The Points Guy** — CPL ~$2.80 vs $3.50-$4.50 target. Under budget. Handover complete.
- **Points Path** — CPL $1.78 within $1.50-$2.00 range. Collaborative relationship.
- **Just Women's Sports** — CPL $1.17 vs $1.50 target. Under budget.
- **MarketBeat** — CPL $8.86 vs $10-14 target. Momentum phase.
- **Big Desk Energy** — CPL $2.30 vs $3.00 target. Under budget.

---

*Generated March 21, 2026 by Claude Code. Full enrichment completed across all 25 clients.*
