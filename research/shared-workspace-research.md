# Shared Workspace Research: Getting the Vault to the Team

**Date:** 2026-03-20
**Author:** Jay Warner (with Claude Code)
**Status:** Research complete, ready for decision

---

## TL;DR Recommendation

**Use GitHub (free private repo) + GitHub Desktop + Obsidian as the editor.** This gives you version history, access control, conflict handling, and a non-intimidating editing experience for Lays and eventually the whole team. Total cost: $0 for up to 10 people on a single private repo. Obsidian is free for commercial use. GitHub Desktop is free. The vault files stay local on each person's machine, so Claude Code works exactly as it does today.

---

## Table of Contents

1. [The Problem](#the-problem)
2. [Requirements Matrix](#requirements-matrix)
3. [Git Hosting Platforms Compared](#git-hosting-platforms-compared)
4. [Git GUI Clients Compared](#git-gui-clients-compared)
5. [Non-Git Sync Alternatives Compared](#non-git-sync-alternatives-compared)
6. [Full Comparison Table](#full-comparison-table)
7. [How Other Teams Share AI Configurations](#how-other-teams-share-ai-configurations)
8. [The Recommended Stack](#the-recommended-stack)
9. [Exact Setup Steps](#exact-setup-steps)
10. [Handling Conflicts (Jay + Lays Edit Same File)](#handling-conflicts)
11. [What to Demo for Nathan and Sindy](#what-to-demo-for-nathan-and-sindy)
12. [Long-Term Architecture](#long-term-architecture)
13. [How This Complements Notion](#how-this-complements-notion)
14. [Sources](#sources)

---

## The Problem

The vault is 97 files of markdown, CSVs, PNGs, JS scripts, and one PDF. It powers Claude Code for Jay's daily work across 19 clients. The value is proven. Now it needs to be shared with Lays (senior GM), and eventually up to 10 people, without:

- Requiring anyone to learn command-line Git
- Losing version history or overwriting each other's work
- Exposing Jay's private management files (team/, memory/)
- Breaking Claude Code's local filesystem requirement
- Costing real money before the concept is proven

---

## Requirements Matrix

| Requirement | Weight | Notes |
|---|---|---|
| Files exist locally on each machine | **Must have** | Claude Code reads from filesystem |
| Non-technical setup/usage | **Must have** | GMs are marketers, not engineers |
| Conflict resolution | **Must have** | Jay and Lays will edit same client files |
| Version history / rollback | **Must have** | Need to undo bad edits |
| Access control (hide folders) | **Should have** | team/ and memory/ must stay private |
| Free or near-free | **Should have** | Unfunded experiment |
| Mobile access | **Nice to have** | For reference on the go |
| Binary file handling | **Nice to have** | PNGs, PDFs, CSVs in the vault |

---

## Git Hosting Platforms Compared

### 1. GitHub (Recommended)

- **Free tier:** Unlimited private repos, unlimited collaborators, 500 MB Packages storage
- **Paid tier:** Team plan at $4/user/month adds branch protection, required reviewers, code owners
- **Why it fits:** Most widely known platform. GitHub Desktop is purpose-built for it. Free tier is sufficient for what Jay needs right now. The `gh` CLI is already integrated into Claude Code workflows.
- **Access control:** On free tier, all collaborators see all files in the repo. Jay's private files are already gitignored, so they never enter the repo at all. If Jay later needs per-folder permissions, GitHub Team ($4/user/month) adds CODEOWNERS for review gating, though true folder-level read restrictions require GitHub Enterprise.
- **Binary files:** Handles PNGs, PDFs, CSVs fine. Large files (>100 MB) need Git LFS, but the vault's binaries are small.

### 2. GitLab

- **Free tier:** Up to 5 users per top-level group, unlimited private repos, built-in CI/CD
- **Paid tier:** Premium at $29/user/month (steep jump)
- **Why it's second choice:** More features than needed, higher learning curve, expensive upgrade path. The 5-user limit on free tier is fine initially but restrictive if the full team joins.
- **Access control:** Better than GitHub on free tier — supports granular permissions at the group/project level.
- **Downside:** No equivalent to GitHub Desktop's simplicity. GitLab's own web IDE is decent but doesn't solve the local-files-for-Claude-Code requirement.

### 3. Bitbucket

- **Free tier:** Up to 5 users, unlimited private repos
- **Paid tier:** Standard at $3.30/user/month (cheapest paid option)
- **Why it's third:** Atlassian ecosystem integration is irrelevant since TFM doesn't use Jira/Confluence. Sourcetree (Atlassian's Git GUI) is free but clunkier than GitHub Desktop. Community and documentation are thinner.
- **Access control:** Branch permissions on free tier, similar to GitLab.

### 4. Other Options

- **Azure DevOps:** Free for up to 5 users, but overkill and Microsoft-ecosystem-heavy.
- **Gitea/Forgejo (self-hosted):** Free, but requires server setup and maintenance. Not appropriate for a non-technical team.

**Verdict:** GitHub. The free tier covers everything Jay needs. The ecosystem (GitHub Desktop, `gh` CLI, Claude Code integration) is unmatched.

---

## Git GUI Clients Compared

### 1. GitHub Desktop (Recommended)

- **Setup complexity:** 1/5 (easiest)
- **Cost:** Free
- **Platform:** Mac + Windows
- **Conflict resolution:** Shows merge conflicts inline with visual markers. Not the most sophisticated, but clear enough for markdown files.
- **Why it fits:** Built specifically for GitHub. Sign in with your GitHub account, clone, and go. The UI reduces Git to three concepts: pull (get latest), commit (save changes), push (share changes). This is the minimum viable Git experience for a marketer.
- **Limitations:** No Linux support. Limited advanced Git features. But that's a feature, not a bug, for this use case.

### 2. GitKraken

- **Setup complexity:** 2/5
- **Cost:** Free for public repos only. Pro at $4.95/user/month for private repos.
- **Platform:** Mac, Windows, Linux
- **Conflict resolution:** Built-in merge conflict editor with side-by-side view. Best-in-class.
- **Why it's second:** The visual commit graph is beautiful and helps users understand what's happening. But the free tier doesn't support private repos, so this would cost ~$5/user/month on top of the free GitHub repo. For an unfunded experiment, that's a hard sell.

### 3. Sourcetree (Atlassian)

- **Setup complexity:** 2/5
- **Cost:** Free
- **Platform:** Mac + Windows
- **Conflict resolution:** Relies on external diff tools. Less intuitive than GitKraken.
- **Why it's third:** Free and functional, but the UI feels dated compared to GitHub Desktop. Requires an Atlassian account. Better paired with Bitbucket, which Jay isn't using.

### 4. VS Code with Git Extensions

- **Setup complexity:** 3/5
- **Cost:** Free
- **Platform:** Mac, Windows, Linux
- **Conflict resolution:** Excellent inline merge conflict resolution.
- **Why it's not recommended:** VS Code is a code editor. Asking a growth marketer to install and navigate a code editor to edit markdown files is unnecessary friction. The Git integration is good, but it's buried inside a tool that will feel foreign.

### 5. Tower

- **Setup complexity:** 2/5
- **Cost:** $69-99/year per user
- **Platform:** Mac + Windows
- **Conflict resolution:** Excellent, with visual diff tools.
- **Why it's not recommended:** Paid, and the UX is designed for developers. Overkill for markdown file syncing.

### 6. Fork

- **Setup complexity:** 2/5
- **Cost:** $49.99 one-time (evaluation period is free)
- **Platform:** Mac + Windows
- **Conflict resolution:** Good built-in merge tool.
- **Why it's notable:** Fast, clean, reasonably priced. But still developer-oriented.

**Verdict:** GitHub Desktop. Lowest friction, free, purpose-built for GitHub repos. The whole team can be onboarded in a 10-minute screen share.

---

## Non-Git Sync Alternatives Compared

### 1. Obsidian Sync

- **Setup complexity:** 1/5
- **Cost:** $4/month (Standard) or $8/month (Plus) per user. Shared vaults only on Plus.
- **Conflict resolution:** Automatic merge for non-conflicting changes. For true conflicts, creates a "conflicted copy" file. No line-level merge.
- **Version history:** 1 month (Standard) or 12 months (Plus)
- **Max collaborators:** 20 per shared vault
- **Claude Code compatible:** Yes, files are local.
- **Access control:** No per-folder restrictions. Everyone in the vault sees everything.
- **Why it's tempting:** Seamless sync, no Git concepts at all. The editing experience in Obsidian is excellent for markdown.
- **Why it falls short:** At $8/user/month for Plus (needed for shared vaults with 12-month history), cost for 10 people is $80/month or $960/year. Conflict handling is crude (duplicate files, not line-level merges). No access control means Jay can't hide management files within the shared vault — he'd need to maintain a separate personal vault.

### 2. Syncthing (P2P)

- **Setup complexity:** 4/5
- **Cost:** Free (open source)
- **Conflict resolution:** Last-write-wins by default. Creates `.sync-conflict` files for simultaneous edits. No merge capability.
- **Version history:** Optional file versioning (simple, staggered, or external)
- **Claude Code compatible:** Yes, files are local.
- **Access control:** Per-folder sharing is possible (share different folders with different people).
- **Why it's not recommended:** Both devices must be online simultaneously to sync. No central server means if Jay's laptop is closed, Lays can't pull updates. Technical to set up. Conflict resolution is primitive.

### 3. Resilio Sync

- **Setup complexity:** 3/5
- **Cost:** Free for personal use. Business at ~$6/user/month.
- **Conflict resolution:** Similar to Syncthing — conflict files, not merges.
- **Version history:** Basic, via archive folder.
- **Claude Code compatible:** Yes, files are local.
- **Access control:** Per-folder sharing with read-only or read-write permissions.
- **Why it's notable:** Faster than Syncthing for large files. Per-folder permissions are genuinely useful (Jay could share clients/ but not team/). But the conflict resolution is still last-write-wins, which doesn't work when two people edit the same client file.

### 4. iCloud / Google Drive / Dropbox

- **Setup complexity:** 1/5
- **Cost:** Varies. Google Drive 2 TB at $10/month. Dropbox Business at $15/user/month.
- **Conflict resolution:** Creates "conflicted copy" files. No merge.
- **Version history:** 30 days (Google Drive), 180 days (Dropbox Business)
- **Claude Code compatible:** Partially. Files sync locally, but sync latency can cause Claude Code to read stale files. Lock files and sync metadata can cause issues.
- **Access control:** Folder-level sharing permissions.
- **Why it's not recommended:** Cloud sync tools are designed for documents, not for structured knowledge bases that are programmatically read. The "conflicted copy" approach is a mess for a 97-file vault. No line-level merge means every conflict requires manual resolution. Sync latency means Claude Code might read a file mid-sync and get garbage.

### 5. Obsidian + Git Plugin (Hybrid)

- **Setup complexity:** 2/5 (once configured)
- **Cost:** Free (Obsidian is free for commercial use, Git plugin is free, GitHub is free)
- **Conflict resolution:** Full Git merge. The plugin auto-pulls on startup and auto-pushes on interval.
- **Version history:** Full Git history, unlimited.
- **Claude Code compatible:** Yes, files are local.
- **Access control:** Same as Git (gitignore for private files).
- **Why this is the real answer:** Obsidian becomes the editing layer. The Git plugin handles sync in the background. Users never see Git commands. They open Obsidian, edit files, and the plugin auto-commits and pushes. When they reopen Obsidian, it auto-pulls. Conflicts are rare with a small team, and when they happen, Obsidian shows a diff. This is Git under the hood with a markdown editor on top.

**Verdict:** Obsidian + Git plugin as the editing/sync layer, backed by GitHub. This combines the best editing experience with real version control.

---

## Full Comparison Table

| Option | Setup (1-5) | Conflict Handling | Cost (10 users) | Claude Code Works | Version History | Access Control | Mobile |
|---|---|---|---|---|---|---|---|
| **GitHub + GitHub Desktop** | 2 | Line-level merge | Free | Yes (local files) | Unlimited | Gitignore only (free) | GitHub mobile app (view only) |
| **GitHub + Obsidian Git** | 2 | Line-level merge (auto) | Free | Yes (local files) | Unlimited | Gitignore only (free) | Obsidian mobile (no Git) |
| GitLab + GitKraken | 3 | Line-level merge | $50/mo (GitKraken) | Yes | Unlimited | Per-folder (free tier) | GitLab mobile (view) |
| Bitbucket + Sourcetree | 2 | External diff tools | Free | Yes | Unlimited | Branch permissions | Bitbucket mobile (view) |
| Obsidian Sync | 1 | Conflicted copies | $80/mo | Yes | 12 months (Plus) | None | Obsidian mobile (full sync) |
| Syncthing | 4 | Last-write-wins | Free | Yes | Basic | Per-folder | No |
| Resilio Sync | 3 | Last-write-wins | ~$60/mo | Yes | Basic | Per-folder, R/W | Mobile app |
| Google Drive | 1 | Conflicted copies | ~$10/mo | Risky (sync lag) | 30 days | Folder-level | Full mobile |
| Dropbox | 1 | Conflicted copies | $150/mo | Risky (sync lag) | 180 days | Folder-level | Full mobile |

---

## How Other Teams Share AI Configurations

### Emerging patterns in 2026

1. **CLAUDE.md in Git is the standard.** Teams check their `CLAUDE.md` into the repo and treat it like code — PRs for changes, regular pruning, collective ownership. One team at Anthropic described contributing "multiple times a week" to a shared CLAUDE.md, adding rules whenever Claude makes a mistake.

2. **Personal overrides via CLAUDE.local.md.** Claude Code auto-adds `CLAUDE.local.md` to `.gitignore`. This is where individuals put their personal preferences ("explain everything before changing" or "respond in Spanish") without affecting the team.

3. **The `.claude/rules/` directory for domain-specific standards.** Teams create separate rule files for different domains (API conventions, testing rules, component patterns) and commit them to Git. These are scoped to specific paths so they only activate in relevant directories.

4. **Shared prompt libraries via Git repos.** More technical teams use Git repositories as prompt libraries. The `.github/prompts/` folder pattern (from VS Code) and `.prompt` files in Claude Code are both emerging as standards for reusable, version-controlled prompts.

5. **No dominant "AI workspace platform" yet.** Tools like TeamAI and AICamp offer shared AI workspaces with prompt libraries, but they're SaaS platforms that don't integrate with local tooling like Claude Code. The Git-based approach remains the most flexible and is what Anthropic themselves recommend.

6. **Teams with centralized knowledge bases report 3.2x productivity gains** over those relying on individual documentation. Shared prompt libraries specifically show 40% productivity improvement and 60% faster onboarding.

### What this means for TFM

The vault is ahead of the curve. Most teams are still figuring out that they need shared AI configurations. Jay has already built the knowledge base, the prompt library, the client intelligence framework, and the CLAUDE.md that ties it together. The only missing piece is distribution.

---

## The Recommended Stack

### Primary: GitHub + Obsidian + Obsidian Git Plugin

| Layer | Tool | Role |
|---|---|---|
| **Hosting** | GitHub (free private repo) | Central source of truth, version history, access control |
| **Editor** | Obsidian (free) | Markdown editing, vault navigation, link/search |
| **Sync** | Obsidian Git plugin (free) | Auto-pull on open, auto-push on interval, background sync |
| **Backup GUI** | GitHub Desktop (free) | For when Obsidian Git has issues, or for initial clone |
| **AI tool** | Claude Code | Reads from local filesystem, same as today |

### Why this stack

- **Zero ongoing cost** for up to unlimited collaborators
- **Obsidian is the best markdown editor** and the vault is already markdown-first
- **Git plugin hides Git entirely** — users just edit files and the plugin syncs
- **GitHub Desktop is the safety net** — if the plugin acts up, open GitHub Desktop and click "Pull" or "Push"
- **CLAUDE.md stays in Git** — shared team intelligence, version-controlled
- **CLAUDE.local.md stays personal** — per-person preferences, auto-gitignored
- **team/ and memory/ stay gitignored** — Jay's private files never touch the repo

---

## Exact Setup Steps

### Phase 1: Jay Sets Up the Repo (30 minutes)

```
Step 1: Create GitHub repo
- Go to github.com, create new private repository "tfm-vault"
- Do NOT initialize with README (you already have files)

Step 2: Push existing vault to GitHub
- Open Terminal in /Users/jay/Documents/the vault/the-feed-media
- Run:
    git remote add origin git@github.com:jay-warner/tfm-vault.git
    git branch -M main
    git push -u origin main

Step 3: Verify .gitignore
- Confirm team/, memory/, .claude/ are gitignored
- Confirm no credentials or personal files are tracked
- Check with: git status (should show nothing unexpected)

Step 4: Install Obsidian Git plugin
- Open the vault in Obsidian
- Go to Settings > Community Plugins > Browse
- Search "Obsidian Git" (by Vinzent03)
- Install and enable
- Configure:
    - Auto pull on startup: ON
    - Auto push interval: 5 minutes
    - Pull on startup: ON
    - Disable notifications: OFF (keep them visible at first)
    - Commit message format: "{{hostname}}: {{date}}"

Step 5: Test the round-trip
- Edit a file in Obsidian
- Wait for auto-push (or trigger manually via command palette > "Obsidian Git: Push")
- Verify the change appears on github.com
```

### Phase 2: Onboard Lays (20 minutes, screen share)

```
Step 1: Create Lays' GitHub account
- Go to github.com/join
- Use her work email

Step 2: Invite Lays to the repo
- Jay goes to github.com/jay-warner/tfm-vault/settings/access
- Click "Add people" > enter Lays' GitHub username
- Set permission to "Write" (can push, but can't change repo settings)

Step 3: Install GitHub Desktop on Lays' Mac
- Download from desktop.github.com
- Sign in with her GitHub account
- Clone the repo: File > Clone Repository > select tfm-vault
- Choose a local folder (e.g., ~/Documents/tfm-vault)

Step 4: Install Obsidian on Lays' Mac
- Download from obsidian.md
- Open as vault: select the cloned folder
- Install Obsidian Git plugin (same settings as Jay's)

Step 5: Create Lays' personal config
- Create ~/.claude/CLAUDE.md for Lays' personal Claude Code preferences
- Create CLAUDE.local.md in the vault root for her personal overrides

Step 6: Walk through the workflow
- Open Obsidian, notice "Pulled X changes" notification on startup
- Edit a client file, save
- Wait for auto-push or manually push
- Jay verifies the change appears on his side
```

### Phase 3: Daily Workflow (what Lays actually does)

```
1. Open Obsidian (plugin auto-pulls latest changes)
2. Navigate to clients/[client-name]/
3. Edit the file
4. Save (Cmd+S)
5. Plugin auto-commits and pushes within 5 minutes
6. If notification says "merge conflict":
   - Open the file, look for <<<< ==== >>>> markers
   - Keep the right content, delete the markers
   - Save again (plugin will auto-commit the resolution)
```

That's it. No terminal. No Git commands. No branching or PRs.

---

## Handling Conflicts

### The scenario: Jay and Lays both edit the-points-guy.md

**How often will this actually happen?**
Rarely. The vault is 97 files across 19 clients. For two people to edit the same file at the same time, they'd need to be working on the same client simultaneously and both save within a 5-minute auto-push window. Markdown files with structured sections further reduce the chance of touching the same lines.

**When it does happen, here's what Git does:**

1. **Non-overlapping edits:** Git auto-merges silently. Jay edits the "Brand Voice" section while Lays edits "Winning Creative Signals" — both changes merge automatically with zero intervention.

2. **Overlapping edits:** Git flags a merge conflict. The file shows:
   ```
   <<<<<<< HEAD
   Jay's version of the line
   =======
   Lays' version of the line
   >>>>>>> origin/main
   ```
   The person who pulls second sees this, picks the right version, deletes the markers, and saves. Done.

**Best practices to minimize conflicts:**

- **Establish ownership conventions.** "Lays owns creator-spotlight.md, Jay reviews but doesn't edit directly." Use the `client-config.md` files to note the primary owner.
- **Pull before you start editing.** Open Obsidian first (auto-pull fires), then start working.
- **Push frequently.** The 5-minute auto-push interval keeps changes flowing.
- **Use Notion for real-time collaboration.** If Jay and Lays need to simultaneously draft something, do it in Notion. The vault is for settled knowledge, not live brainstorming.

---

## What to Demo for Nathan and Sindy

### The 15-Minute Pitch

**Slide 1: The problem (2 min)**
"Every GM is reinventing the wheel. When a new GM takes over a client, there's no structured handoff of what works in creative, what the client hates, what the benchmarks are. This knowledge lives in Jay's head or scattered across Notion pages, Slack threads, and Loom recordings."

**Slide 2: What the vault is (3 min)**
Show Obsidian open with the vault. Click through:
- A client intelligence file (show the 6-category structure)
- The master prompt library
- A Claude Chat project instruction file
- The creative frameworks document

Say: "This is a knowledge base that makes AI 10x more useful. Instead of Claude giving generic answers, it gives answers informed by our actual client data, our actual SOPs, and our actual creative history."

**Slide 3: Live demo (5 min)**
1. Open Claude Code in the vault
2. Ask: "Draft 3 ad concepts for [client] based on their winning creative signals"
3. Show Claude referencing the client intelligence file, applying the DCT 4-3-2-2 framework, and avoiding the client's negative triggers
4. Compare to asking the same question in vanilla Claude (generic, uninformed output)

**Slide 4: How sharing works (3 min)**
"Lays has been using this for [X weeks]. Here's what changed."
- Show a before/after of a task Lays did with and without the vault
- Show the version history on GitHub (every change tracked, rollback available)
- Show that Lays' workflow is just: open Obsidian, edit, save

**Slide 5: The ask (2 min)**
"This costs nothing. The tools are free. I need permission to roll this out to [next 2-3 GMs] and 30 minutes of their time for onboarding. If it works, we standardize it across the team."

### Key metrics to track during the pilot with Lays

- Time to draft first ad concept (vault vs. no vault)
- Number of client-specific details Claude catches (brand voice rules, negative triggers)
- GM confidence score ("How confident are you in this output? 1-5")
- Time saved on client handoffs
- Number of times Lays contributes back to the vault (adds a new winning signal, updates benchmarks)

---

## Long-Term Architecture

### If this works with 2-3 people

```
tfm-vault (GitHub private repo)
|
|-- CLAUDE.md                    # Shared team instructions for Claude Code
|-- CLIENT-INTELLIGENCE-SUMMARY.md
|-- clients/
|   |-- [client-name]/
|   |   |-- [client-name].md    # Intelligence file (structured)
|   |   |-- client-config.md    # Config + ownership metadata
|   |   |-- claude-chat-project.md
|   |   |-- (other client assets)
|-- prompts/
|   |-- master-prompt-library.md
|-- system/
|   |-- framework.md
|   |-- tfm-creative-frameworks.md
|   |-- skills.md
|   |-- onboarding-prompts.md
|-- research/
|-- .claude/
|   |-- rules/                   # Domain-specific AI rules (committed)
|   |   |-- media-buying.md
|   |   |-- creative-review.md
|   |   |-- client-comms.md
|-- scripts/
```

### If this scales to the full team (10 people)

1. **Upgrade to GitHub Team ($4/user/month = $40/month).** Adds CODEOWNERS so Jay can require his review before changes to critical files (CLAUDE.md, framework.md).

2. **Add branch protection on main.** GMs work on main for day-to-day edits (auto-commit via Obsidian Git). But changes to system/ and prompts/ require a PR reviewed by Jay. This prevents someone from accidentally breaking the AI instructions.

3. **Use `.claude/rules/` for scoped instructions.** Instead of one monolithic CLAUDE.md, break domain rules into separate files that apply only to relevant directories.

4. **Establish a "vault gardening" cadence.** Monthly review where Jay prunes outdated content, merges duplicates, and updates benchmarks. The vault compounds in value only if it's maintained.

5. **Consider a read-only "published" branch for clients.** If TFM ever wants to share curated intelligence files with clients (e.g., "here's our creative framework for your brand"), a separate branch with limited content could serve that purpose.

### What the workflow looks like at scale

```
GM opens Obsidian
  -> Plugin auto-pulls latest from GitHub
  -> GM edits client file after a call
  -> GM saves, plugin auto-pushes
  -> Jay sees the change in his Obsidian (auto-pull)
  -> Jay reviews, maybe adds context from his perspective
  -> Claude Code on any team member's machine reads the latest local files
  -> AI output is informed by the entire team's collective knowledge
```

---

## How This Complements Notion

The vault does NOT replace Notion. They serve different purposes:

| | The Vault (Git/Obsidian) | Notion |
|---|---|---|
| **Purpose** | AI-readable knowledge base | Team collaboration & project management |
| **Content type** | Structured intelligence files, prompts, frameworks | Meeting notes, task boards, creative briefs, client dashboards |
| **Who reads it** | Claude Code / Claude Chat | Humans (and occasionally AI via MCP) |
| **Edit frequency** | Weekly (when insights change) | Daily (tasks, notes, updates) |
| **Format** | Markdown (optimized for LLM consumption) | Rich text, databases, embeds |
| **Collaboration model** | Async (edit, push, pull) | Real-time (simultaneous editing) |

**The relationship:** Notion is where work happens in real time. The vault is where proven knowledge gets distilled and structured for AI consumption. Think of it as: Notion is the kitchen, the vault is the recipe book.

**Workflow example:**
1. Lays has a client call, takes notes in Notion
2. Call reveals a new "negative trigger" (client hates a certain phrase)
3. Lays opens Obsidian, adds it to `clients/[client]/[client].md` under Negative Triggers
4. Next time anyone uses Claude Code for that client, the AI knows to avoid that phrase

---

## Sources

- [GitHub Pricing Plans](https://github.com/pricing)
- [GitHub Desktop Getting Started](https://docs.github.com/en/desktop/overview/getting-started-with-github-desktop)
- [GitKraken Review 2026](https://thesoftwarescout.com/gitkraken-review-2026-the-best-git-gui-client-for-most-developers/)
- [Best Git GUI Clients 2026](https://thesoftwarescout.com/best-git-clients-2026-top-gui-tools-for-version-control/)
- [Obsidian Sync Standard Plan](https://obsidian.md/blog/standard-plan/)
- [Obsidian Shared Vault Documentation](https://help.obsidian.md/Collaborate+on+a+shared+vault)
- [Obsidian Git Plugin (GitHub)](https://github.com/Vinzent03/obsidian-git)
- [Leveraging Obsidian with GitHub for Collaborative Documentation](https://luegm.dev/posts/obsidiangit/)
- [Claude Code Best Practices](https://code.claude.com/docs/en/best-practices)
- [Claude Code on a Team: What's Shared, What's Private](https://medium.com/@binu_thayamkery/claude-code-on-a-team-whats-shared-what-s-private-and-how-not-to-step-on-each-other-11ebcea8d01c)
- [Claude Code Team Best Practices: CLAUDE.md, Hooks & Actions](https://smartscope.blog/en/generative-ai/claude/claude-code-creator-team-workflow-best-practices/)
- [Syncthing vs Resilio Sync Comparison](https://noted.lol/syncthing-or-resilio-sync/)
- [GitLab Pricing](https://about.gitlab.com/pricing/)
- [Bitbucket vs GitHub Comparison](https://www.upguard.com/blog/bitbucket-vs-github)
- [GitHub vs GitLab vs Bitbucket Feature Comparison](https://tryhoverify.com/blog/github-vs-gitlab-vs-bitbucket-feature-comparison/)
- [Why Teams Need Shared Prompt Libraries](https://aicamp.so/blog/why-team-needs-shared-prompt-libraries/)
- [Tower Git Client Pricing](https://www.git-tower.com/pricing)
