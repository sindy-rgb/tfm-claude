# Claude Code for TFM — Full Setup & Usage Guide

## Why Claude Code? Why Now?

Most agencies use AI the same way — copy-paste into ChatGPT, re-explain the client every time, lose context between sessions. That's not us.

**TFM is building something different.** We're giving every Growth Manager an AI assistant that already knows every client — their KPIs, their NEVER rules, what creative worked last month, what tone makes them uncomfortable, what their CPL target is. Not because someone typed it in that morning, but because it lives in a shared knowledge vault that Claude reads automatically.

**What this means for the agency:**
- **Institutional memory that doesn't walk out the door.** When a GM learns something about a client — "they hate that tone," "this hook style crushed it" — it gets saved to the vault. Everyone benefits. No more tribal knowledge living in one person's head.
- **Consistent quality across 25 accounts.** Every GM has access to the same playbooks, the same creative frameworks, the same NEVER rules. Claude enforces them automatically.
- **Speed that compounds.** Friday reports that took 45 minutes take 2. Creative QA that required manual cross-referencing happens in seconds. That time adds up — across 6 GMs, across 25 clients, every single week.
- **We're not replacing anyone.** We're removing the tedious parts so GMs can focus on strategy, client relationships, and creative thinking — the stuff that actually grows accounts.

**This is what separates TFM from every other agency.** Our competitors are still copy-pasting into ChatGPT. We have an AI that knows our entire operation and gets smarter every week.

### What can you actually do with it?

| What you do today manually | What Claude Code does |
|---------------------------|----------------------|
| Spend 30-45 min writing Friday reports | `/friday` generates it in 2 minutes from live data |
| Manually check ad copy against client rules | `/creative-qa` checks every NEVER rule automatically |
| Guess when creatives are dying | `/fatigue-scan` flags dying ads before CPL spikes |
| Forget what happened in last client call | Ask Claude — it reads the client file with full history |
| Re-explain client context every Claude session | Claude reads it automatically from the vault |
| Lose context when switching between clients | All 25 clients are always in context |

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

## Saving Your Work

When you update a client file, add notes, or create a new doc — you need to save it back to the vault so the rest of the team gets your changes.

**The simple version:** Just tell Claude:
- "Save my changes"
- "Submit my updates"

Claude will handle the technical steps for you (creating a branch, committing, submitting for review).

**What happens behind the scenes:**
1. Your changes go to a separate copy (branch) so they don't affect anyone else's work
2. Sindy reviews your changes
3. Once approved, they merge into the main vault and everyone gets them

**That's it.** You don't need to learn git commands. If something goes wrong, ask Claude or message Sindy.

---

## Naming Conventions

### When you create new files

Follow this format: `your-name_description.md`

Examples:
- `lays_workweek-concept-brief-april.md`
- `mariely_eh-landing-page-analysis.md`
- `kinte_creator-spotlight-q2-strategy.md`

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

## Security & Privacy

### What Claude can and cannot see

- **Claude CAN see:** Everything in the tfm-claude vault — client files, SOPs, configs, your GM profile. That's the whole point.
- **Claude CANNOT see:** Your personal files, other apps on your computer, your browser, your passwords, your email. It only sees what's inside the vault folder.
- **Claude does NOT send data to other people.** Your conversation is between you and Claude. Other team members cannot see your conversations.

### What about client data?

- All data processed by Claude is covered by Anthropic's enterprise privacy policy — it is **not used to train AI models**
- Client ad account IDs, CPL numbers, and contact info live in the vault. Treat them the same way you treat any client data — don't share outside TFM
- If a client ever asks: "We use AI tools with enterprise-grade privacy to manage our internal operations. No client data is used for model training."

### Access control

- **Only TFM team members** have access to the vault (controlled via GitHub)
- **Sindy reviews all changes** before they go live — nothing gets into the main vault without approval
- **If you leave TFM**, your GitHub access gets revoked and you lose vault access immediately
- **Your Anthropic login** is personal to you — don't share it with anyone

### What to never put in the vault

- Client passwords or login credentials
- Credit card or payment information
- Personal health or financial data about contacts
- Anything a client has explicitly marked as confidential/NDA-protected that isn't already in our systems

---

## Troubleshooting

### "Claude doesn't know my client"
You're probably not in the vault folder. Run `pwd` to check, then `cd ~/Documents/tfm-claude` if needed.

### "Permission denied when pushing"
You need to be on a branch, not main. Just tell Claude "save my changes" and it will handle this for you.

### "Git asks for username/password"
Use your GitHub username and the Personal Access Token (not your GitHub password).

### "npm command not found"
Node.js isn't installed. Go back to Step 3.

### "claude command not found"
Claude Code isn't installed. Go back to Step 4.

### Still stuck?
Message Sindy on Slack. She'll help you out.
