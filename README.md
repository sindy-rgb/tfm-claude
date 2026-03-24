# TFM Operations Vault

The Feed Media (TFM) shared operations vault. This is the team's single source of truth for client intelligence, SOPs, creative strategy, and workflows.

**Managed by:** Sindy (Head of Operations)
**Repo:** `sindy-rgb/tfm-claude`

---

## Team

| Name | Role | Clients |
|------|------|---------|
| Nathan May | Agency Principal | — |
| Sindy | Head of Operations | All |
| Rabii Elhaouat | Media Buyer | All |
| Luiz Pekelman | Growth Manager | MarketBeat, Quartz, Stocks & Income, Houck |
| Kinte Otieno | Growth Manager | Creator Spotlight, RNT Fitness, MDhair |
| Lays Paiva | Growth Manager | WorkWeek, Jay Shetty, How to AI, Insight Links |
| Mariely Galindo | Growth Manager | 1636 Forum, Franklin's Forum, Points Path, EH, Daily Drop, Status News, Big Desk Energy |
| Aubree Clark | Growth Manager | Vendry, Student Loan Planner, Open Source CEO |
| Jay Warner | Director | The Points Guy |
| Noreen | Reporting Analyst | Friday reports |
| Melvin | Video Editor | — |
| Marc | Static Designer | — |

---

## Vault Structure

```
tfm-claude/
├── clients/          # 25 client folders — intelligence files, configs, enrichment data
├── SOPs/             # Team playbooks, frameworks, prompts, meeting schedules
├── skills/           # 7 automated skills for Claude Code
├── templates/        # Reusable templates (new client, meeting notes, reports)
├── dashboards/       # Dataview dashboards (portfolio, creative pipeline, weekly review)
├── reports/          # Active reports and audits
├── system/           # Framework definitions, SQLite data, state tracking
├── Archive/          # Old files kept for reference
├── CLAUDE.md         # Claude Code instructions (auto-loaded every session)
├── CLIENT-INTELLIGENCE-SUMMARY.md  # Master summary of all 25 clients
└── README.md         # This file
```

---

## Client Files

Every client has a folder in `clients/` with these files:

| File | What it is |
|------|-----------|
| `[client].md` | Main intelligence file — contacts, KPIs, voice rules, creative signals, risks |
| `client-config.md` | Machine-readable config — ad account IDs, Slack channels, budgets |
| `deep-enrichment.md` | Auto-generated audit — cross-references Drive, Notion, and Meta data |

Client intelligence files follow 6 categories:
1. **Client Overview** — Contacts, status, ESP, channels
2. **North Star Metric** — Primary KPI + target
3. **Brand Voice Rules** — NEVER rules, approved language
4. **Winning Creative Signals** — Top formats with data
5. **Negative Triggers** — Things to avoid
6. **Relationship Health** — Sentiment, risk level

---

## Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/sindy-rgb/tfm-claude.git ~/Documents/tfm-claude
```

### 2. Open in Obsidian

1. Download [Obsidian](https://obsidian.md) if you don't have it
2. Open Obsidian → **Open folder as vault**
3. Select the `tfm-claude` folder you just cloned

### 3. Install Required Plugins

Go to **Settings > Community Plugins > Browse** and install:

| Plugin | Why |
|--------|-----|
| **Obsidian Git** | Syncs your changes with the team via GitHub |
| **Dataview** | Powers the live dashboards in `dashboards/` |
| **Templater** | Powers the templates in `templates/` |

### 4. Configure Obsidian Git

In **Settings > Obsidian Git**:
- **Auto pull interval:** 5 minutes
- **Auto push after commit:** On
- **Commit message format:** `vault sync: {{date}}`

### 5. Orient Yourself

- Read your assigned client files in `clients/`
- Check `CLIENT-INTELLIGENCE-SUMMARY.md` for a quick overview of all 25 clients
- Browse `SOPs/` for team playbooks and frameworks
- Check `dashboards/` for portfolio views

---

## Daily Workflow

1. Obsidian Git auto-syncs in the background — you'll see team changes appear
2. When you update a client file after a call or analysis, it pushes to GitHub automatically
3. Check `SOPs/` for any process questions before asking
4. Use your client's intelligence file as context when working with Claude

---

## Last Updated
March 24, 2026
