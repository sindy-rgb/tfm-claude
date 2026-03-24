# Claude Code for TFM — Full Setup & Usage Guide

## Why Are We Doing This?

You already know Claude from the web (claude.ai). You use it to draft reports, review copy, brainstorm creatives. But every time you start a conversation, you have to explain who the client is, what their NEVER rules are, what their CPL target is, what happened last week.

**Claude Code changes that.**

Claude Code is Claude in your terminal. When you run it inside the TFM vault, Claude instantly has access to:
- Every client's intelligence file (contacts, KPIs, voice rules, creative signals, risks)
- Every client's config (ad account IDs, Slack channels, budgets, UTM format)
- All SOPs and playbooks (media buying, creative frameworks, copywriting guides)
- Your GM profile (how you like reports, what you prioritize, your working style)
- All 7 automation skills (/friday, /creative-qa, /fatigue-scan, etc.)

**No more copy-pasting. No more re-explaining. Claude already knows everything.**

### What can you actually do with it?

| What you do today manually | What Claude Code does |
|---------------------------|----------------------|
| Spend 30-45 min writing Friday reports | `/friday` generates it in 2 minutes from live data |
| Manually check ad copy against client rules | `/creative-qa` checks every NEVER rule automatically |
| Guess when creatives are dying | `/fatigue-scan` flags dying ads before CPL spikes |
| Forget what happened in last client call | Ask Claude — it reads the client file with full history |
| Re-explain client context every Claude session | Claude reads it automatically from the vault |
| Lose context when switching between clients | All 25 clients are always in context |

### What gets saved?

Every insight you share with Claude gets saved back to the vault. When you tell Claude "this client hates that tone" or "this creative approach worked" — that knowledge lives in the vault permanently. Next time anyone works on that client, Claude already knows. We stop losing context.

---

## STEP 1 — Create a GitHub Account

GitHub is where the vault lives. It's like Google Drive but for code and text files. Everyone on the team has access to the same vault, and changes sync automatically.

1. Go to **https://github.com/join**
2. Sign up with your TFM email
3. Choose the free plan
4. **Send Sindy your GitHub username** — she needs to add you as a collaborator
5. Wait for an email invitation from GitHub — **accept it**

Do NOT continue until Sindy confirms you've been added.

---

## STEP 2 — Install Git

Git is the tool that syncs files between your computer and GitHub. You need it installed before anything else.

### Mac

1. Open **Terminal** (press `Cmd + Space`, type "Terminal", press Enter)
2. Type this and press Enter:
   ```
   git --version
   ```
3. If you see a version number (like `git version 2.39.0`) — Git is already installed, skip to Step 3
4. If a popup appears asking to install developer tools — click **Install** and wait (takes 5-10 minutes)
5. After it finishes, type `git --version` again to confirm

### Windows

1. Go to **https://git-scm.com/download/win**
2. Download and run the installer
3. Use all default settings — just click **Next** through everything
4. When it finishes, **restart your computer**
5. Open **PowerShell** (search "PowerShell" in Start menu)
6. Type `git --version` and press Enter to confirm it worked

---

## STEP 3 — Install Node.js

Claude Code needs Node.js to run. This is a one-time install.

### Mac

1. Go to **https://nodejs.org**
2. Download the **LTS version** (the green button on the left)
3. Open the downloaded file and follow the installer
4. Open Terminal and verify:
   ```
   node --version
   ```
   You should see something like `v20.11.0`

### Windows

1. Go to **https://nodejs.org**
2. Download the **LTS version** (the green button on the left)
3. Run the installer — use all default settings
4. **Restart your computer**
5. Open PowerShell and verify:
   ```
   node --version
   ```

---

## STEP 4 — Install Claude Code

### Mac (Terminal)

```
npm install -g @anthropic-ai/claude-code
```

### Windows (PowerShell)

```
npm install -g @anthropic-ai/claude-code
```

If you get a permissions error on Mac, try:
```
sudo npm install -g @anthropic-ai/claude-code
```
(It will ask for your computer password — type it and press Enter. You won't see the characters as you type, that's normal.)

---

## STEP 5 — Clone the Vault

This downloads the entire TFM vault to your computer. You only do this once.

### Mac (Terminal)

```
git clone https://github.com/sindy-rgb/tfm-claude.git ~/Documents/tfm-claude
```

### Windows (PowerShell)

```
git clone https://github.com/sindy-rgb/tfm-claude.git $HOME\Documents\tfm-claude
```

When prompted:
- **Username:** your GitHub username
- **Password:** paste the Personal Access Token Sindy gave you (not your GitHub password)

---

## STEP 6 — Open Claude Code (Every Time)

This is what you do every time you want to use Claude Code. Always start from the vault folder.

### Mac

1. Open Terminal
2. Type:
   ```
   cd ~/Documents/tfm-claude
   ```
3. Type:
   ```
   claude
   ```
4. First time only: it will ask you to log in with your Anthropic account. Follow the link it gives you.
5. You're in. Start talking to Claude.

### Windows

1. Open PowerShell
2. Type:
   ```
   cd $HOME\Documents\tfm-claude
   ```
3. Type:
   ```
   claude
   ```
4. First time only: log in with your Anthropic account.
5. You're in.

### CRITICAL: Always start from tfm-claude

**You MUST be inside the `tfm-claude` folder when you run Claude.** If you run `claude` from any other folder, Claude won't have access to the vault and none of the skills or client files will work.

If you're not sure you're in the right folder, type:
```
pwd
```
It should show something like `/Users/yourname/Documents/tfm-claude` (Mac) or `C:\Users\yourname\Documents\tfm-claude` (Windows).

If it shows anything else, run `cd ~/Documents/tfm-claude` (Mac) or `cd $HOME\Documents\tfm-claude` (Windows) first.

---

## Understanding the Vault — What's Inside

When you open the vault, here's what every folder and file is for:

### Folders

| Folder | What's inside | Do you use it? |
|--------|--------------|----------------|
| **clients/** | 25 client folders. Each has an intelligence file, config, and enrichment data. This is your main reference. | YES — read and update your client files |
| **GMs/** | One profile per GM. Your preferences, working style, what Claude learns about you. | YES — Claude reads this to personalize how it works with you |
| **SOPs/** | 19 team playbooks — media buying, creative frameworks, copywriting guides, meeting schedules, prompt library | YES — reference these, suggest updates |
| **skills/** | 7 automated skills (see below). Each has a SKILL.md explaining how it works. | YES — run these with slash commands |
| **templates/** | 6 reusable templates — new client, meeting notes, friday report, creative QA log, bi-weekly prep, client onboarding | YES — use these when creating new docs |
| **dashboards/** | 3 Dataview dashboards — portfolio overview, creative pipeline, weekly review | View only (works in Obsidian) |
| **reports/** | 3 active reports — enrichment audit, data audit, onboarding reference | Reference only |
| **system/** | Framework definitions, SQLite database, state tracking, config templates | DO NOT TOUCH — this powers the skills |
| **Archive/** | Old files kept for reference — Jay's research, stale reports, root files, dev configs | Reference only if needed |

### Client Files (inside each clients/[client-name]/ folder)

| File | What it is |
|------|-----------|
| **[client-name].md** | Main intelligence file — contacts, KPIs, NEVER rules, creative signals, relationship health. This is the most important file. |
| **client-config.md** | Machine-readable config — ad account IDs, Slack channels, budgets, UTM format. Skills read from this. |
| **deep-enrichment.md** | Auto-generated audit — cross-references Google Drive, Notion, and Meta Ads data. Shows gaps. |
| Extra files (some clients) | Concept briefs, creative frameworks, analysis docs — varies by client |

### Root Files

| File | What it is |
|------|-----------|
| **CLAUDE.md** | Instructions Claude reads every session. Defines how Claude behaves in this vault. |
| **CLIENT-INTELLIGENCE-SUMMARY.md** | One-page summary of all 25 clients — quick reference. |
| **README.md** | Team onboarding doc (you're reading the detailed version now). |

---

## Skills — What You Can Run

Type these commands inside Claude Code:

| Command | What it does | When to use |
|---------|-------------|-------------|
| `/friday` | Generates your Friday ad report from live Meta data, formatted for Notion | Every Friday |
| `/creative-qa` | Checks a concept against the client's NEVER rules, voice guidelines, and brand restrictions | Before sending any creative to a client |
| `/fatigue-scan` | Analyzes your ads and flags which ones are dying (rising CPL, falling CTR) | Weekly or when performance dips |
| `/portfolio-pulse` | Cross-client performance snapshot — see all your accounts at a glance | Monday morning or before pod meetings |
| `/weekly-enrichment` | Pulls latest CPL data from Slack and updates client files | Sunday (usually Sindy runs this) |
| `/vault-integrity` | Validates that all client files are complete and correctly formatted | When you think something might be missing |
| `/action-tracker` | Pulls action items from meetings and tracks them | After client calls |

You can also just ask Claude anything:
- "What are the NEVER rules for Jay Shetty?"
- "What's Houck's CPL target?"
- "Draft ad copy for WorkWeek based on their winning signals"
- "Summarize the last month's performance for all my clients"

---

## How Your Work Gets Saved

### The branch workflow

You cannot push changes directly to the main vault. This protects everyone's work. Instead:

1. **You work on a branch** — think of it as your own copy
2. **You make changes** — update client files, add notes, create docs
3. **You submit a Pull Request (PR)** — this sends your changes to Sindy for review
4. **Sindy approves** — your changes merge into the main vault
5. **Everyone gets your updates** — the whole team benefits

### How to do this in practice

Claude Code handles most of this for you. Just tell Claude:
- "Create a branch for my updates"
- "Save my changes and submit a PR"
- Claude will walk you through it step by step

Or manually:

**Create your branch (once per work session):**
```
git checkout -b your-name/update-description
```
Example: `git checkout -b lays/jay-shetty-march-update`

**After making changes, save and submit:**
```
git add -A
git commit -m "Updated Jay Shetty intelligence file after client call"
git push origin your-name/update-description
```

Then go to GitHub and create a Pull Request, or ask Claude to do it for you.

---

## Naming Conventions

### When you create new files

Follow this format: `your-name_description.md`

Examples:
- `lays_workweek-concept-brief-april.md`
- `mariely_eh-landing-page-analysis.md`
- `kinte_creator-spotlight-q2-strategy.md`

### When you create new folders

Same pattern: `your-name_folder-description/`

### Why?

So everyone can see who created what at a glance. Sindy reviews all PRs and this makes it much faster.

### Files you DON'T rename

- Existing client files ([client].md, client-config.md, deep-enrichment.md) — keep the original names
- Anything in system/, skills/, templates/, dashboards/ — don't rename these
- CLAUDE.md, README.md, CLIENT-INTELLIGENCE-SUMMARY.md — don't rename

---

## What You Can and Cannot Do

### You CAN:
- Update your client intelligence files (add notes from calls, update NEVER rules, change CPL targets)
- Create new files in your client folders (concept briefs, analysis docs, strategy notes)
- Update your GM profile in GMs/
- Run any skill (/friday, /creative-qa, etc.)
- Ask Claude anything about any client
- Suggest changes to SOPs (submit a PR)

### You CANNOT:
- Push directly to main (branch protection blocks this)
- Modify system/, CLAUDE.md, or the vault structure
- Delete other people's files
- Rename existing client folders

If you try to do something you can't, Claude will tell you and guide you to the right approach.

---

## Troubleshooting

### "Claude doesn't know my client"
You're probably not in the vault folder. Run `pwd` to check, then `cd ~/Documents/tfm-claude` if needed.

### "Permission denied when pushing"
You need to be on a branch, not main. Run `git checkout -b your-name/your-update` first.

### "Git asks for username/password"
Use your GitHub username and the Personal Access Token (not your GitHub password).

### "npm command not found"
Node.js isn't installed. Go back to Step 3.

### "claude command not found"
Claude Code isn't installed. Go back to Step 4.

### Still stuck?
Message Sindy on Slack. She'll help you out.

---

## Quick Reference Card

```
# Every time you start:
cd ~/Documents/tfm-claude    # (Mac)
cd $HOME\Documents\tfm-claude  # (Windows)
claude

# Run skills:
/friday
/creative-qa
/fatigue-scan
/portfolio-pulse

# Save your work:
# Just tell Claude: "save my changes and submit a PR"

# Exit:
exit
```
