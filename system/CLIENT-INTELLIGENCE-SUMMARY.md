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

| # | Client | GM | Status | Risk Level | CPL Target | Current CPL (Mar 13-19) | ESP | Deep Enrichment | Claude Chat Project |
|---|--------|----|--------|------------|------------|-------------|-----|:-:|:-:|
| 1 | 1636 Forum | Mariely Galindo | Active | MEDIUM | $2.00 | $3.01 | beehiiv | Yes | Yes |
| 2 | Big Desk Energy | Mariely | Active | LOW-MEDIUM | $3.00 | $2.30 | beehiiv | Yes | Yes |
| 3 | Contrarian Thinking | Luiz Pekelman | Active (90-day trial) | MEDIUM | $5-6 | $4.96 | beehiiv | Yes | Yes |
| 4 | Creator Spotlight | Kinte Otieno | Active | MEDIUM | MAR >4 (quality) | $2.19 | beehiiv | Yes | Yes |
| 5 | Daily Drop | Mariely | Creative Only | LOW-MEDIUM | $3-$4 | $4.16 (TFM) / $4.10 (BAU) | N/A (client-managed) | Yes | Yes |
| 6 | Experiential Hospitality | Mariely | Active | LOW-MEDIUM | $5.00 | $5.20 | GoHighLevel | Yes | Yes |
| 7 | Franklin's Forum | Mariely Galindo | Active | MEDIUM | $3.00-$3.50 | $4.03 | beehiiv | Yes | Yes |
| 8 | Houck (Founding Journey) | Luiz Pekelman | Active | MODERATE-LOW | $5-$15 | $1.80 | beehiiv | Yes | Yes |
| 9 | How to AI | Lays Paiva | Active | LOW-MEDIUM | $1.50-$2.50 | $2.28 | Substack | Yes | Yes |
| 10 | Insight Links | Lays | Active | MEDIUM-LOW | Qualified CPL < $20 | $16.24 blended qual | Mailchimp | Yes | Yes |
| 11 | Jay Shetty | Lays Paiva | Active | LOW-MEDIUM | $3.00 | $0.93 gross | beehiiv | Yes | Yes |
| 12 | Just Women's Sports | Lays Paiva (covering) | Active | MEDIUM | $1.50 | $2.32 | beehiiv | Yes | Yes |
| 13 | MarketBeat | Luiz Pekelman | Active | LOW | $10-14 | $7.51 | Custom (in-house) | Yes | Yes |
| 14 | MDhair | Kinte | Active | MEDIUM | $80 CAC | $130 CAC (testing) | N/A (DTC) | Yes | Yes |
| 15 | Open Source CEO | Aubree Clark | Active | LOW-MEDIUM | $3.50 | ~$3.50+ (trending down) | beehiiv | Yes | Yes |
| 16 | Points Path | Mariely | Active | LOW | $1.50-$2.00 | $1.78 | Kit | Yes | Yes |
| 17 | Quartz | Mariely | Active | MEDIUM | $2.50 | $3.27 | Delivra | Yes | Yes |
| 18 | RNT Fitness | Kinte Otieno | Active | MEDIUM | Unconfirmed | GBP 1.00 | beehiiv | Yes | Yes |
| 19 | Status (News) | Mariely | At Risk | HIGH | $1-$2 raw / ICP-Verified | $68.42/qualified (15 qualified/$1,026) | beehiiv | Yes | Yes |
| 20 | Stocks & Income | Luiz Pekelman | Active | MEDIUM | $2.00 | $3.70 (-15% WoW) | beehiiv | Yes | Yes |
| 21 | Stocks.News | Luiz Pekelman | Active | LOW-MEDIUM | Cost Per Trial < $60 | $57.38 per trial | N/A (app-based) | Yes | Yes |
| 22 | Student Loan Planner | Aubree Clark | Active | MEDIUM-HIGH | $15-20 | $18.82 (+60% since Jan) | Kit (ConvertKit) | Yes | Yes |
| 23 | The Points Guy | Jay Warner | Active | MODERATE | $3.50-$4.50 | ~$2.80 | N/A (Red Ventures) | Yes | Yes |
| 24 | Vendry (Case Studied) | Aubree Clark | Active | MEDIUM | $2-6 CAD | DR paused (LP rebuild) / $19.38 (NL) | beehiiv | Yes | Yes |
| 25 | Workweek | Lays Paiva | Active | LOW | $6-$9.50 Sub CAC | IHIH $6.08 / TMM $6.09 / FTT $5.78 / Hosp $6.30 / GTM $3.60 | Sailthru | Yes | Yes |

### Summary Counts
- **25 total clients** (24 Active + 1 At Risk)
- **25 clients with deep-enrichment.md** files (all clients now have deep enrichment)
- **25 clients with Claude Chat project instructions** (all clients now have claude-chat-project.md)
- **6 clients built from scratch on March 21:** 1636 Forum, Franklin's Forum, Just Women's Sports, Vendry, Student Loan Planner, MDhair
- **All 25 client files** have YAML frontmatter for Obsidian Bases
- **QA logs V1-V5** exist documenting data integrity checks across the enrichment process
- **CPLs updated March 21** from weekly Slack reports (Mar 13-19 period)

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

## Key Flags Across The Portfolio (Updated Mar 21 from live Slack data)

### HIGH Risk
- **Status (News)** — $68.42/qualified (15 qualified from $1,026 spend, Mar 13-19). 1P completion rate improved to 76.5%. March 26 meeting is prove-it-or-lose-it. Notion playbooks ALL empty.
- **Student Loan Planner** — $18.82 CPL, up 60% since Jan ($11.79 → $18.82). CVR collapsed 16.87% → 11.64%. CRITICAL: Refi landing page copy mismatch blocking scale. Jeffrey Trull must fix.

### MEDIUM Risk
- **1636 Forum** — CPL $3.01 vs $2.00 target. Testing phase. Waiting on Allison for creative approval.
- **Franklin's Forum** — CPL $4.03 vs $3.00-$3.50 target. Contract ambiguity (Gigi asking about "trial" end date — no end date per Sindy).
- **Contrarian Thinking** — CPL $4.96 within $5-6 range. 90-day trial, ~55 days remain (May 16 deadline). 8 new creatives sent to Codie for approval.
- **Creator Spotlight** — Quality-focused (MAR >4), not CPL-driven. GM transition to Kinte complete. Q2 goals 12+ days overdue from Francis. Budget overspend ($3,741 vs $2K/wk target).
- **MDhair** — DTC client, $130 CAC vs $80 target. March sprint at 53% as of 3/18. Kinte committed to completing by Friday. Dual feedback issue (Yasin vs Pooja).
- **Quartz** — CPL $3.27 (improved from $3.55) vs $2.50 target. Bake-off. Delivra infrastructure flagged (80.5% of TFM subs never sent email).
- **RNT Fitness** — KPIs still unconfirmed. GBP 1.00 CPL (confirmed via beehiiv, 311 subs). Female messaging dominating; male angles need work.
- **Stocks & Income** — CPL $3.70 vs $2.00 target (-15% WoW, trending down). Reporting quality flagged by Nathan (misspelled client name, missing CVR/CTR/CPM). 0/3 Friday reports on time.
- **Vendry** — DR funnel paused (LP rebuild). Newsletter CPL up to $19.38 (from $13.38). Migration to casestudied.com needs event verification. "Case Studied" is newsletter name.
- **Just Women's Sports** — CPL $2.32 (up from $1.17), now ABOVE $1.50 target. CPMs +17% WoW. Lays covering as GM. Needs attention.
- **How to AI** — CPL $2.28 within target, but landing page CVR crashed (45% → 24%, recovering at 29%). UGC fatigue burned $40K+. Substack confirmation step inflating CPL.

### Stable / Low Risk
- **Workweek** — All 5 newsletters green simultaneously (first time ever). GTM improved to $3.60. FTTB (6th newsletter) launching. IHIH under pressure (1% above $6.00 target).
- **Houck** — CPL $1.80, well under $5-$15 range. Spend scaled 9x to $225/day. 5 new DCTs approved Mar 20. Thank-you pages expected Mar 22-23.
- **Jay Shetty** — CPL $0.93 gross. Sparkloop reconciliation Mar 28 will inform scaling decisions.
- **The Points Guy** — CPL ~$2.80 vs $3.50-$4.50 target. New spend caps $3-4K/month per concept. Hub LP test blocked on Louisa pixel verification.
- **Points Path** — CPL $1.78 within $1.50-$2.00 range (+14% WoW though). Email retargeting of 19K subs + influencer partnership in pipeline.
- **MarketBeat** — CPL $7.51 (improved from $8.86), best week ever Mar 14-20. Leads +79% WoW. Momentum phase.
- **Big Desk Energy** — CPL $2.30 vs $3.00 target. Under budget. Stable.
- **Experiential Hospitality** — CPSA $5.20 vs $5.00 target. 2,137 webinar registrations Mar 19. GHL integration in progress.
- **Insight Links** — $16.24 blended qualified CPL, all 3 NLs under $20 for first time. Bake-off with Growletter — TFM has quality edge.
- **Stocks.News** — $57.38/trial vs $60 target. Spend up 82% WoW. GrowJoy competitive pressure.

### Process Flags (Cross-Account)
- **Friday report timeliness** — Multiple accounts at 0% on-time (Franklin's Forum, Insight Links, Stocks & Income, TPG, MDhair). Sindy has flagged this as a priority.
- **N8N report automation** — Template issues detected (Quartz/Stocks.News sheets showing placeholder IDs). Verify spreadsheet links.
- **Stock Earnings** — New #thefeed-stockearnings channel (Hiral Ghelani, Adarsh). SoW sent. Not yet in 25-client roster — monitor for onboarding.

---

*Updated March 21, 2026 by Claude Code. Full enrichment + live Slack cross-reference across all 25 clients.*
