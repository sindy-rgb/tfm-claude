# The Feed Media -- Client Intelligence Vault

The Feed Media (TFM) is a newsletter growth agency running paid media (primarily Meta Ads) for 25 newsletter and DTC clients. This Obsidian vault is the team's single source of truth for client intelligence, SOPs, creative strategy, and team operations. Every team member should treat this as their primary reference for client context and workflows.

**GitHub Repo:** `thefeedmedia/tfm-vault` (synced via Obsidian Git)

---

## Team

| Name | Role |
|------|------|
| **Nathan May** | Agency Principal |
| **Sindy** | Head of Operations |
| **Jay Warner** | Director of Growth |
| **Rabii Elhaouat** | Media Buyer |
| **Luiz Pekelman** | Growth Manager |
| **Kinte Otieno** | Growth Manager |
| **Lays Paiva** | Growth Manager |
| **Mariely Galindo** | Growth Manager |
| **Aubree Clark** | Growth Manager |
| **Noreen** | Reporting & Data |
| **Melvin** | Team Member |
| **Marc** | Team Member |

---

## Clients (25)

| Client | GM | Status |
|--------|----|--------|
| 1636 Forum | Mariely | Active |
| Big Desk Energy | Mariely | Active |
| Contrarian Thinking | Luiz | Active (90-day trial) |
| Creator Spotlight | Kinte | Active |
| Daily Drop | Mariely | Creative Only |
| Experiential Hospitality | Mariely | Active |
| Franklin's Forum | Mariely | Active |
| Houck | Luiz | Active |
| How to AI | Lays | Active |
| Insight Links | Lays | Active |
| Jay Shetty | Lays | Active |
| Just Women's Sports | TBD | Active |
| MarketBeat | Luiz | Active |
| MDhair | Kinte | Active (Creative Only) |
| Open Source CEO | Aubree | Active |
| Points Path | Mariely | Active |
| Quartz | Mariely | Active (Bake-off) |
| RNT Fitness | Kinte | Active |
| Status (News) | Mariely | At Risk |
| Stocks & Income | Luiz | Active |
| Stocks.News | Luiz | Active |
| Student Loan Planner | Aubree | Active |
| The Points Guy | Jay | Active |
| Vendry | Aubree | Active |
| Workweek | Lays | Active |

---

## Vault Structure

```
the-feed-media/
├── clients/              # One folder per client, each with a [client].md intelligence file
│                         # Files follow the 6-category framework with YAML frontmatter
├── dashboards/           # Dataview dashboards (portfolio overview, risk tracker, GM workload)
├── templates/            # Templater templates for new clients, bi-weekly reports, creative briefs
├── research/             # Shared workspace research, media buying knowledge, industry analysis
├── system/               # Framework definitions, portfolio status, workflow SOPs
├── team/                 # Team onboarding docs, role definitions, training materials
├── memory/               # Session logs, media buying SOPs, external knowledge, project memory
├── prompts/              # Reusable prompts for analysis, Notion parsing, memory setup
├── copilot/              # Claude Code project instructions and configuration
├── scripts/              # Export/sync utilities
├── CLAUDE.md             # Claude Code project instructions (auto-loaded every session)
├── CLIENT-INTELLIGENCE-SUMMARY.md  # Master summary of all 25 clients
└── README.md             # This file
```

---

## How It Works

### Source of Truth Flow

1. **Day.ai** stores CRM data, meeting recordings, and org context notes for each client
2. **Monday automated skill** updates Day.ai org contexts every Monday at 9 AM EST
3. **Client intelligence files** in `clients/` are the local mirrors -- read instantly by Claude Code at session start with zero API calls
4. **Claude Code sessions** read from `clients/` directly for full intelligence in context

### Client Intelligence Framework

Every client file (`clients/[client-name]/[client-name].md`) follows six categories:

1. **Client Overview** -- Contacts, stakeholders, status, ESP, channels
2. **North Star Metric** -- Primary KPI + target, quality definition
3. **Brand Voice Rules** -- NEVER rules first, approved language, failed copy quotes
4. **Winning Creative Signals** -- Top formats with performance data
5. **Negative Triggers** -- Charged client quotes, patterns to avoid
6. **Relationship Health** -- Sentiment, risk level, continuity concerns

### Frontmatter System

Every client file has YAML frontmatter at the top with structured fields:

```yaml
---
client: Client Name
slug: client-name
status: Active
gm: GM Name
media_buyer: Rabii
esp: beehiiv
cpl_target: "$X.XX"
current_cpl: "$X.XX"
risk_level: LOW
sentiment: Positive
last_enriched: 2026-03-21
---
```

These fields power the **Dataview dashboards** in `dashboards/` -- live tables that show portfolio health, GM workload, risk levels, and CPL performance at a glance.

### Templater Templates

The `templates/` folder contains Templater templates for creating new client files, bi-weekly report shells, creative brief frameworks, and other repeatable documents. When creating a new client, use the client template to ensure the 6-category structure and frontmatter are applied automatically.

---

## MCP Integrations

Claude Code connects to external tools via MCP (Model Context Protocol):

| Tool | What It Does |
|------|-------------|
| **Day.ai** | CRM, meeting recordings, workspace context, org notes |
| **Notion** | Client pages, SOPs, creative concepts, bi-weekly reports, training docs |
| **Slack** | Internal and external client channels, DMs, message search |
| **Meta Ads (Pipeboard)** | Ad account management, campaign data, creative performance |
| **Gmail** | Email drafts, search, client communication |
| **Google Calendar** | Meeting scheduling, free time lookup, event management |
| **Google Drive** | File search, document reading |
| **Google Sheets** | Weekly ad report spreadsheets, data reads and updates |

---

## Onboarding (New Team Members)

If you are new to TFM (this section is written for Lays and future team members):

### 1. Clone the Repo

```bash
git clone https://github.com/thefeedmedia/tfm-vault.git
```

Or if you already have the folder, make sure it is up to date:

```bash
cd tfm-vault && git pull
```

### 2. Open in Obsidian

1. Download and install [Obsidian](https://obsidian.md) if you do not have it
2. Open Obsidian and select **Open folder as vault**
3. Point it at the `the-feed-media` folder you cloned

### 3. Install Obsidian Git Plugin

1. Go to **Settings > Community Plugins > Browse**
2. Search for **Obsidian Git** and install it
3. Enable the plugin
4. In Obsidian Git settings, configure:
   - **Auto pull interval:** 5 minutes (keeps your vault synced with the team)
   - **Auto push after commit:** On (your changes sync back to GitHub)
   - **Commit message format:** `vault sync: {{date}}`

### 4. Install Recommended Plugins

These plugins make the vault fully functional:

- **Dataview** -- Powers the live dashboards in `dashboards/`. Without this, dashboard pages will show raw code instead of tables.
- **Templater** -- Powers the templates in `templates/`. Use these when creating new client files or reports.
- **Obsidian Git** -- Keeps your local vault synced with the GitHub repo.

### 5. Orient Yourself

- Read `CLAUDE.md` to understand how Claude Code sessions work with this vault
- Read `system/portfolio-status.md` for a snapshot of all 25 clients and their current state
- Read `CLIENT-INTELLIGENCE-SUMMARY.md` for a condensed overview of every client
- Browse `clients/` and open your assigned client files to get familiar with the intelligence format
- Check `memory/media-buying-sop.md` for the DCT 4-3-2-2 method, CBO vs ABO strategy, and Meta benchmarks

### 6. Daily Workflow

- Obsidian Git auto-syncs in the background. You should see changes from other team members appear automatically.
- If you update a client file after a call or analysis, the change will push to GitHub on the next auto-commit cycle.
- After Monday skill runs, check Day.ai for updates and re-export any changed client context to local files.

---

## Last Updated
March 21, 2026
