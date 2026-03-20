# The Feed Media — Client Intelligence System Update
### March 8, 2026

---

## What Was Done

We ran a full client intelligence audit across **all 15 active clients**, pulling data from three sources and writing it back to two systems:

### Sources Pulled (Per Client)
1. **Day.ai** — Organization records, meeting recording transcripts, contacts, opportunities, action items
2. **Slack** — Internal channels (#internal-[client]), external channels (#thefeed-[client]), pod channels, DMs
3. **Notion** — Client pages, onboarding docs, OneSheets, creative playbooks, bi-weekly meeting notes, weekly ad reports, creative briefs

### Where It Was Written
1. **Day.ai** — Each client's organization record now has a workspace context note titled "[Client Name] — Client Intelligence (Updated March 2026)" containing the full 6-category framework
2. **Local files** — Each client has a markdown file at `/the-feed-media/clients/[client-name].md`

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

## Clients Updated

| # | Client | Day.ai Written | Local File | Risk Level |
|---|--------|---------------|------------|------------|
| 1 | Creator Spotlight (beehiiv) | Partial (Slack/Day.ai blocked) | creator-spotlight.md | MEDIUM — Natalie handover |
| 2 | Workweek | Yes | workweek.md | LOW — All 5 accounts green |
| 3 | Insight Links | Yes | insight-links.md | MEDIUM — Bake-off with Growletter |
| 4 | Status (News) | Yes | status-news.md | HIGH — 1 paid conversion in 6 months |
| 5 | Stocks.News | Yes | stocks-news.md | LOW — Metrics improving, budget scaling |
| 6 | The Points Guy | Partial (write blocked) | the-points-guy.md | MEDIUM-HIGH — Contract renewal + CS handover |
| 7 | Houck | Yes | houck.md | MODERATE — 4-month onboarding delay |
| 8 | RNT Fitness | Yes | rnt-fitness.md | LOW — Honeymoon phase, KPIs unconfirmed |
| 9 | Daily Drop | Yes | daily-drop.md | LOW — Creative-only, stable |
| 10 | Open Source CEO | Partial (write blocked) | open-source-ceo.md | LOW — CPL above target but stable |
| 11 | Jay Shetty | Partial (Slack/Day.ai blocked) | jay-shetty.md | LOW-MEDIUM — Strong performance |
| 12 | How to AI | Partial (write blocked) | how-to-ai.md | LOW-MEDIUM — CPL above target |
| 13 | Points Path | Partial (write blocked) | points-path.md | LOW-MEDIUM — Install conversion gap |
| 14 | Experiential Hospitality | Partial (write blocked) | experiential-hospitality.md | MODERATE — ROAS declining |
| 15 | Quartz | Yes | quartz.md | HIGH — Bake-off, 23 days left, CPL gap |

---

## How To Access This Going Forward

### For Any Team Member
1. **Day.ai** — Open the client's organization record → look for the "Client Intelligence" context note
2. **Local files** — Navigate to `/the-feed-media/clients/[client-name].md`

### For Claude Projects (Per Client)
Use **Prompt 3** from the Master Prompt Library to set up Claude Project memory from the Day.ai context note. This creates 6 memory entries (one per category) so Claude has full client context in any project chat.

### For Claude Code Sessions
Use **Prompt 4** (single client) or **Prompt 5** (cross-client) from the Master Prompt Library:
```
Read the following files before responding to anything:
- /the-feed-media/clients/[CLIENT-NAME].md
- /the-feed-media/system/framework.md
```

### To Update After New Analysis
Use **Prompt 6** from the Master Prompt Library to replace client file content after completing a fresh analysis.

### To Re-Run This Full Audit
Run the same process in Claude Code — it will pull from Day.ai, Slack, and Notion, synthesize the 6-category framework, write back to Day.ai, and save local markdown files.

---

## Key Flags Across The Portfolio

### Immediate Attention Required
- **Status (News)** — March 19 meeting is prove-it-or-lose-it. 1 paid conversion in 6 months.
- **Quartz** — 23 days left in bake-off. CPL 56% above target. 5 March concepts unsent.
- **Creator Spotlight** — Natalie handover from Francis. Brand standards briefing needed ASAP.
- **The Points Guy** — Contract renewal window open. Francis → Natalie handover.

### Friday Reports Missing (March 6)
- Insight Links, Open Source CEO, Houck, RNT Fitness, Quartz, Status

### Sprint Delivery Gaps (March)
- Multiple accounts have concepts stuck in initial stage with 0% on-time delivery

---

*Generated March 8, 2026 by Claude Code using the Master Prompt Library automated workflow.*
