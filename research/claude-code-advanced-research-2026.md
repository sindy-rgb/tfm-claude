# Claude Code Advanced Features & Power-User Research — TFM 2026

**Generated:** 2026-03-22
**Purpose:** Identify practical, implementable upgrades for The Feed Media's Claude Code setup
**Current state:** 7 skills built, 3 hooks active, 12 MCP servers connected, SQLite performance DB, Obsidian vault

---

## Table of Contents
1. [Hooks System — Expand Beyond Current Setup](#1-hooks-system)
2. [Modular Rules — Replace CLAUDE.md Bloat](#2-modular-rules)
3. [Agent Teams & Sub-Agents](#3-agent-teams--sub-agents)
4. [Scheduled Tasks & /loop](#4-scheduled-tasks--loop)
5. [Context Window & Effort Optimization](#5-context-window--effort-optimization)
6. [MCP Server Ecosystem Expansion](#6-mcp-server-ecosystem)
7. [n8n + Claude Code Deep Integration](#7-n8n--claude-code-deep-integration)
8. [Playwright / Browser Automation](#8-playwright-browser-automation)
9. [Skills Ecosystem — Community & Marketing-Specific](#9-skills-ecosystem)
10. [Memory System Optimization](#10-memory-system-optimization)
11. [Headless / SDK / Programmatic Usage](#11-headless--sdk--programmatic-usage)
12. [Emerging: Channels, Voice, Cowork](#12-emerging-features)

---

## 1. Hooks System — Expand Beyond Current Setup {#1-hooks-system}

### What TFM Has Now
- `PreToolUse` on Slack send: creative-qa-gate.sh, slack-audit-trail.sh
- `PostToolUse` on Edit/Write: validate-frontmatter.sh

### What's Available (12+ Hook Events)
Claude Code now supports hooks on these lifecycle events:
- **PreToolUse** — before any tool runs (you have this)
- **PostToolUse** — after a tool succeeds (you have this)
- **Stop** — when Claude finishes a response
- **Notification** — when Claude sends an alert
- **UserPromptSubmit** — when user submits a prompt
- **SessionStart** — when a new session begins
- **PreCompact** — before context compaction (critical for preserving state)

Hooks support three handler types:
1. **Command** — shell scripts (you use this)
2. **Prompt** — single-turn Claude evaluation (new to TFM)
3. **Agent** — spawns a sub-agent with tool access for deep verification (new to TFM)

Hooks also support `async: true` for background execution without blocking.

### Recommendations

#### R1.1: PreCompact Hook — Preserve Work State Before Compaction
**Priority: P0**
**Why it matters:** When context hits the limit and auto-compacts, details about in-progress work get lost. A PreCompact hook can save the current state to a file before compaction occurs, so the post-compaction session picks up where it left off.

**Implementation:**
```json
{
  "hooks": {
    "PreCompact": [{
      "matcher": "auto|manual",
      "hooks": [{
        "type": "command",
        "command": ".claude/hooks/save-session-state.sh"
      }]
    }]
  }
}
```
The script writes a timestamped summary to `system/state/` with current task, pending items, and key decisions. This directly supports TFM's existing GSD state management pattern.

**Leverages:** system/state/ directory, existing session-log.md pattern

#### R1.2: SessionStart Hook — Auto-Load Relevant Context
**Priority: P1**
**Why it matters:** CLAUDE.md instructions say "before answering any client-specific question, read the relevant client file(s)." A SessionStart hook can automate this by detecting the most recently modified client files or reading a "current focus" state file.

**Implementation:** SessionStart command hook that reads `system/state/current-focus.md` and pipes the active client slug(s) into the session context.

**Leverages:** Client intelligence files, system/state/

#### R1.3: Stop Hook — Auto-Update Session Log
**Priority: P1**
**Why it matters:** CLAUDE.md requires updating `memory/session-log.md` at the end of every session. A Stop hook can automate this instead of relying on Claude remembering to do it.

**Implementation:** Stop hook with an `agent` type handler that summarizes what was accomplished and appends to session-log.md.

**Leverages:** memory/session-log.md

#### R1.4: Upgrade creative-qa to Agent-Type Hook
**Priority: P2**
**Why it matters:** The current creative-qa-gate.sh is a command hook. An agent-type hook would let Claude actually read the client's NEVER rules, check subscriber counts against Beehiiv, and do intelligent QA rather than pattern-matching.

**Implementation:** Change hook type from "command" to "agent" with a system prompt that references the client intelligence framework. The agent hook can use Read, Grep, and Glob tools for deep verification.

**Leverages:** Client intelligence files, Beehiiv MCP

---

## 2. Modular Rules — Replace CLAUDE.md Bloat {#2-modular-rules}

### What TFM Has Now
- One large CLAUDE.md at project root (loaded every session)
- No `.claude/rules/` directory

### What's Available
The `.claude/rules/` directory lets you split instructions into focused markdown files. Key feature: **conditional loading with path-based frontmatter** — rules only load when Claude is working on matching files.

### Recommendations

#### R2.1: Split CLAUDE.md Into Modular Rules
**Priority: P0**
**Why it matters:** TFM's CLAUDE.md is already substantial. Every token in CLAUDE.md loads every session, even when irrelevant. With 25 clients and growing, this will keep expanding. Modular rules save context tokens and keep instructions focused.

**Implementation structure:**
```
.claude/rules/
  always-on.md              # Core identity, team, conventions (no paths: field)
  client-work.md            # paths: ["clients/**/*.md"] — Client framework, NEVER rules pattern
  media-buying.md           # paths: ["clients/**", "skills/friday/**", "skills/fatigue-scan/**"]
  creative-qa.md            # paths: ["skills/creative-qa/**", ".claude/hooks/creative-qa*"]
  reporting.md              # paths: ["skills/friday/**", "skills/portfolio-pulse/**"]
  n8n-workflows.md          # paths: ["research/n8n*", "system/data/**"]
  slack-communication.md    # Loaded when Slack MCP tools are called — guidelines for drafting
  memory-updates.md         # paths: ["memory/**"] — How to update memory files properly
```

Rules with `paths:` frontmatter only load when Claude touches matching files. Rules without `paths:` load every session (like current CLAUDE.md behavior, but smaller).

**Token savings:** Estimated 30-40% reduction in baseline context consumption per session.

**Leverages:** Existing CLAUDE.md content (just reorganized), skills directory structure

---

## 3. Agent Teams & Sub-Agents {#3-agent-teams--sub-agents}

### What TFM Has Now
- Skills that run sequentially in the main session
- No explicit sub-agent patterns

### What's Available
**Sub-agents:** Separate Claude instances with their own context, system prompt, tool permissions, and optionally different models. Up to 5 concurrent sub-agents. Great for isolating heavy work from the main session.

**Agent Teams:** Multiple independent Claude sessions that coordinate via message passing, self-assign tasks, and challenge each other's findings. Cuts wall-clock time 3-5x on parallelizable work but costs more tokens.

### Recommendations

#### R3.1: Sub-Agent Pattern for /friday Reports
**Priority: P0**
**Why it matters:** The /friday skill currently processes 25 clients sequentially. With sub-agents, it could process 5 clients at a time, each sub-agent pulling metrics from the DB and generating the report for its batch. The main agent orchestrates and compiles.

**Implementation:** Modify `/friday` SKILL.md to instruct Claude to spawn sub-agents per client batch. Each sub-agent reads the SQLite DB, generates the report markdown, and writes to a temp file. Main agent collects and posts to Slack.

**Leverages:** pipeboard.db, /friday skill, Slack MCP

#### R3.2: Agent Teams for Monthly Client Reviews
**Priority: P2**
**Why it matters:** Monthly reviews require synthesizing data from multiple sources (Meta performance, ESP data, creative analysis, meeting notes). Agent Teams could parallelize: one agent pulls Meta data, one reads Day.ai meeting notes, one analyzes creative trends, one generates the narrative. They coordinate to produce a unified review.

**Leverages:** Pipeboard MCP, Day.ai MCP, Google Drive MCP, client intelligence files

---

## 4. Scheduled Tasks & /loop {#4-scheduled-tasks--loop}

### What TFM Has Now
- n8n for scheduled automation (server-side)
- Manual skill invocation in Claude Code sessions

### What's Available
**Desktop Scheduled Tasks:** Run locally on macOS. Each fires a fresh Claude Code session at the chosen frequency (hourly, daily, weekly, weekdays). Has access to all MCP tools, skills, and plugins. Available on Pro, Max, Team, and Enterprise plans.

**/loop command:** Session-scoped recurring prompts. Example: `/loop 5m check if the deployment finished`. Tasks expire after 3 days, max 50 per session.

**Important limitation:** Desktop scheduled tasks only run when the computer is awake and Claude Desktop is open. For production reliability, n8n remains the better backbone for critical automations.

### Recommendations

#### R4.1: Desktop Scheduled Task — Morning Portfolio Pulse
**Priority: P1**
**Why it matters:** Nathan or Jay could get an automated morning briefing every weekday at 8am. The task runs `/portfolio-pulse`, checks for CPL anomalies across all 25 accounts, and posts a summary to `#internal-operations`.

**Implementation:** Set up as a Desktop scheduled task on the team lead's machine. Falls back to n8n if machine is off.

**Leverages:** /portfolio-pulse skill, pipeboard.db, Slack MCP

#### R4.2: /loop for Real-Time Campaign Monitoring on Launch Days
**Priority: P1**
**Why it matters:** On launch days (new campaigns, new clients), GMs need to watch CPL and spend closely. Instead of manually checking, `/loop 30m check [client] campaign performance and alert if CPL > $X` monitors automatically during the session.

**Implementation:** Document as an SOP for GMs. No build required — just teach the pattern.

**Leverages:** Pipeboard MCP, existing session

#### R4.3: Weekly /loop for Fatigue Scan
**Priority: P2**
**Why it matters:** The `/fatigue-scan` skill should run weekly. A Desktop scheduled task on Monday morning catches weekend fatigue signals before the work week starts.

**Leverages:** /fatigue-scan skill, pipeboard.db

---

## 5. Context Window & Effort Optimization {#5-context-window--effort-optimization}

### What TFM Has Now
- Opus 4.6 with 1M context window (Max plan)
- Default effort level (medium)

### What's Available
**1M context window:** Opus 4.6 now supports 1M tokens by default. This means the entire TFM vault's client files, memory files, and framework docs can fit in context simultaneously.

**/effort command:** Set reasoning depth per session or per turn.
- `low` — fast, cheap, simple tasks
- `medium` — default, good for daily work
- `high` — complex debugging, multi-file analysis, architecture
- `max` — deepest reasoning, no token constraint

**"ultrathink" keyword:** Per-turn override that bumps effort to high for just the next response. Good for "think harder about this specific thing" moments.

### Recommendations

#### R5.1: Teach Team /effort Patterns
**Priority: P0**
**Why it matters:** Most TFM work (pulling reports, updating files, drafting Slack messages) is fine at medium. But strategic analysis (monthly reviews, creative strategy, client health assessment) benefits from high/max. Teaching the team when to use each level saves money on routine tasks and gets better output on important ones.

**Suggested patterns for TFM:**
- `/effort low` — file lookups, simple data pulls, formatting
- `/effort medium` (default) — daily operations, report generation, Slack drafts
- `/effort high` — client strategy analysis, creative QA, debugging skills
- `ultrathink` keyword — one-off deep analysis prompts ("ultrathink: analyze this client's 90-day CPL trend and recommend next steps")

**Implementation:** Add to team SOP / training doc. No code changes.

#### R5.2: PreCompact Strategy for Long Sessions
**Priority: P1**
**Why it matters:** Even with 1M tokens, complex multi-client sessions can hit limits. The PreCompact hook (R1.1) combined with strategic `/compact` usage keeps sessions productive longer.

**Pattern:** Before starting a second major task in the same session, manually run `/compact [summary of what we accomplished]` to free context while preserving key decisions.

---

## 6. MCP Server Ecosystem Expansion {#6-mcp-server-ecosystem}

### What TFM Has Now
12 MCP servers: Slack, Notion, Google Drive, Gmail, Calendar, Pipeboard/Meta Ads, Day.ai, n8n, Beehiiv, Playwright, plus WebSearch and WebFetch built-in.

### What's Available
The MCP ecosystem now has 1,200+ servers. The official registry is at registry.modelcontextprotocol.io.

### Recommendations

#### R6.1: SQLite MCP Server for Direct DB Access
**Priority: P0**
**Why it matters:** TFM already has `pipeboard.db` with 6 tables and 4 views. Currently, skills access it via Bash `sqlite3` commands. A dedicated SQLite MCP server would let Claude run SQL queries natively as a tool, with proper schema discovery, query validation, and result formatting. This is cleaner and safer than raw shell commands.

**Implementation:** Install the official SQLite MCP server (`mcp-server-sqlite` on PyPI or Docker Hub). Configure it to point at `system/data/pipeboard.db`. Add to `.claude/settings.json` permissions.

**Leverages:** Existing pipeboard.db, all DB-first skills (/friday, /fatigue-scan, /portfolio-pulse)

#### R6.2: GitHub MCP Server
**Priority: P1**
**Why it matters:** TFM has a private repo at `thefeedmedia/tfm-vault`. A GitHub MCP server would let Claude directly create issues (for tracking skill bugs or feature requests), manage PRs, and interact with the repo without Bash git commands.

**Implementation:** Add the official GitHub MCP server. Authenticate with a PAT scoped to the tfm-vault repo.

**Leverages:** Existing GitHub repo, Obsidian Git sync

#### R6.3: Build a Custom TFM MCP Server
**Priority: P2**
**Why it matters:** TFM has agency-specific operations that no generic MCP server covers: looking up client slugs, cross-referencing account_mapping, reading client intelligence files by slug, calculating WoW comparisons. A custom MCP server wrapping these operations would make every skill and session faster.

**Implementation:** Use the TypeScript SDK (`@modelcontextprotocol/typescript-sdk`). Define tools like:
- `get_client(slug)` — returns client overview, current CPL, GM, Slack channels
- `get_performance(slug, days)` — queries pipeboard.db, returns formatted metrics
- `get_all_clients_summary()` — portfolio-level snapshot
- `check_stale_data()` — identifies clients with stale metrics

This replaces scattered Bash/SQLite commands with clean, typed tool calls.

**Leverages:** pipeboard.db, client intelligence files, account_mapping table

#### R6.4: Zapier MCP Server (If Needed)
**Priority: P3**
**Why it matters:** If TFM uses any SaaS tools not covered by existing MCP servers, Zapier's MCP server exposes thousands of app integrations. Evaluate only if a gap is identified.

---

## 7. n8n + Claude Code Deep Integration {#7-n8n--claude-code-deep-integration}

### What TFM Has Now
- n8n self-hosted on Elestio (unlimited executions)
- n8n-mcp connected for building/deploying workflows
- EH workflow, Friday report workflow in progress

### What's Available
The n8n-MCP bridge now provides access to 1,239 automation nodes (809 core + 430 community). Claude Code can build, validate, and deploy n8n workflows directly. The n8n-skills project by czlonkowski teaches Claude Code to build production-ready n8n workflows.

Key pattern: **n8n as webhook backbone, Claude Code as intelligence layer.** n8n handles scheduling, API calls, and routing. Claude Code handles analysis, decision-making, and content generation.

### Recommendations

#### R7.1: Install n8n-skills for Better Workflow Building
**Priority: P1**
**Why it matters:** The `czlonkowski/n8n-skills` repo teaches Claude Code how to build flawless n8n workflows using the n8n-mcp server. Installing these skills would make building new automations significantly more reliable (reported 40% -> near-100% success rate).

**Implementation:** Clone the skills from the repo into TFM's `.claude/skills/` or install as a plugin. These complement the existing n8n-mcp server.

**Leverages:** Existing n8n-mcp server, Elestio hosting

#### R7.2: n8n Webhook -> Claude Code Headless Pipeline
**Priority: P1**
**Why it matters:** Currently, n8n workflows and Claude Code sessions are separate. The pattern: n8n receives a trigger (webhook, schedule, Slack event) -> calls Claude Code in headless mode via SDK -> Claude does the analysis -> n8n routes the output (Slack, Notion, email).

**Use cases:**
- Slack message in #thefeed-[client] mentions "CPL" or "performance" -> n8n triggers Claude Code to pull metrics and draft a response
- New subscriber milestone in Beehiiv -> Claude Code generates a congratulations message and strategy note
- Daily data refresh from Pipeboard -> Claude Code identifies anomalies and alerts

**Implementation:** Use `claude -p "prompt" --output-format json` in n8n's Execute Command node, or use the TypeScript SDK in an n8n Code node.

**Leverages:** n8n Elestio hosting, Claude Code SDK, all MCP servers

#### R7.3: n8n Self-Healer Workflow
**Priority: P2**
**Why it matters:** Already on the roadmap. n8n monitors its own workflow executions. When a workflow fails, it triggers Claude Code to read the error, diagnose the issue, and either fix it or alert the team with a diagnosis.

**Implementation:** n8n Error Trigger node -> Code node calling Claude Code SDK -> conditional fix or Slack alert.

**Leverages:** n8n-mcp, Slack MCP

---

## 8. Playwright / Browser Automation {#8-playwright-browser-automation}

### What TFM Has Now
- Playwright MCP server connected
- Not actively used in any skill

### What's Available
The Playwright MCP server (by Microsoft) lets Claude control a real browser: navigate, click, fill forms, take screenshots, read accessibility trees, and execute JavaScript. It works through structured accessibility snapshots rather than pixel coordinates, making it deterministic and reliable.

### Recommendations

#### R8.1: /lp-monitor Skill — Landing Page CVR Monitoring
**Priority: P0**
**Why it matters:** Already on the roadmap as P2, but this should be P0. Silent landing page CVR drops are one of TFM's biggest risks. A broken landing page can waste thousands in ad spend before anyone notices. Playwright can visit each client's landing page, verify it loads, check for form presence, and screenshot the result.

**Implementation:**
1. Maintain a list of client landing page URLs in `system/data/landing-pages.json`
2. Skill uses Playwright to navigate to each URL, check for form/CTA presence, measure load time
3. Screenshots saved to a date-stamped folder for visual diff
4. Alert via Slack if: page returns error, form is missing, load time > 5s, visual diff from baseline exceeds threshold

**Leverages:** Playwright MCP, Slack MCP, existing client infrastructure

#### R8.2: UTM Verification Automation
**Priority: P1**
**Why it matters:** TFM uses specific UTM formats for Meta Ads. Playwright can click through actual ads (or simulated URLs with UTM parameters), land on the page, and verify UTMs are preserved through to the form submission / ESP attribution.

**Implementation:** Build as part of /lp-monitor or as a standalone check. Playwright navigates to URL with UTM params, submits test form, verifies via Beehiiv API that the subscriber was created with correct UTM attribution.

**Leverages:** Playwright MCP, Beehiiv MCP

#### R8.3: Competitor Landing Page Monitoring
**Priority: P2**
**Why it matters:** Already on the roadmap as P3 `/competitor-watch`. Playwright screenshots competitor newsletter landing pages weekly, and Claude analyzes changes in messaging, offers, social proof, and conversion tactics.

**Implementation:**
1. Maintain competitor URL list per client in client intelligence files
2. Weekly scheduled task screenshots each URL
3. Claude compares to previous screenshots (visual analysis) and accessibility tree (structural analysis)
4. Reports on messaging shifts, new offers, A/B test signals

**Leverages:** Playwright MCP, client intelligence files

---

## 9. Skills Ecosystem — Community & Marketing-Specific {#9-skills-ecosystem}

### What TFM Has Now
7 custom skills: /friday, /creative-qa, /fatigue-scan, /vault-integrity, /action-tracker, /portfolio-pulse, /weekly-enrichment

### What's Available
The open-source skills ecosystem has exploded:
- **claude-ads** (AgriciDaniel) — 186 checks across Meta, Google, YouTube, LinkedIn, TikTok, Microsoft Ads. Weighted scoring, parallel agents, industry templates.
- **marketingskills** (coreyhaines31) — CRO, copywriting, SEO, analytics, and growth engineering skills.
- **claude-skills** (alirezarezvani) — 192+ skills across engineering, marketing, product, compliance.
- **awesome-claude-code-toolkit** (rohitg00) — 135 agents, 35+ skills, 150+ plugins, 19 hooks.

### Recommendations

#### R9.1: Adapt claude-ads for TFM's Meta Audit Workflow
**Priority: P1**
**Why it matters:** The claude-ads skill has 186 audit checks with Meta-specific benchmarks and scoring. TFM could adapt the Meta portion for periodic account audits — catching structural issues, budget inefficiencies, and targeting problems automatically.

**Implementation:** Fork relevant portions of claude-ads into TFM's skills directory. Customize benchmarks using TFM's own performance data from pipeboard.db. Wire to Pipeboard MCP for live data instead of manual exports.

**Leverages:** Pipeboard MCP, pipeboard.db, existing /portfolio-pulse data

#### R9.2: Install Marketing Copywriting Skills
**Priority: P1**
**Why it matters:** The marketingskills repo has dedicated copywriting skills with frameworks for ad copy generation. Combined with TFM's client NEVER rules and brand voice data, this creates a powerful copy generation pipeline that respects client constraints.

**Implementation:** Install relevant copywriting/ad-copy skills. Create a wrapper skill that loads the client's brand voice rules before invoking the copy skill.

**Leverages:** Client intelligence files (Category 3: Brand Voice Rules), Google Drive creative scripts

#### R9.3: /onboard-client Skill
**Priority: P2**
**Why it matters:** Already on the roadmap. New client setup involves creating files, Slack channels, Notion pages, account_mapping entries, and more. A skill that scaffolds all of this from a brief intake form would save hours.

**Implementation:**
1. Prompt for: client name, slug, contacts, ad account ID, ESP, landing page URL, target CPL
2. Create client directory and intelligence file from template
3. Add to account_mapping in pipeboard.db
4. Create Notion page structure
5. Draft Slack channel creation requests
6. Add to landing-pages.json for monitoring

**Leverages:** All MCP servers, pipeboard.db, client intelligence framework

---

## 10. Memory System Optimization {#10-memory-system-optimization}

### What TFM Has Now
- CLAUDE.md at project root (substantial)
- memory/MEMORY.md with index of feedback, reference, and project files
- Individual memory files for feedback and reference
- Auto-memory enabled

### What's Available
**Memory hierarchy (loaded in order):**
1. `~/.claude/CLAUDE.md` — Global personal preferences
2. Project CLAUDE.md — Project-level instructions
3. `.claude/rules/*.md` — Modular rules (conditional or always-on)
4. `memory/MEMORY.md` — Auto-memory (200-line limit in system prompt)

**Auto-memory** lets Claude write its own notes based on corrections and patterns. Limited to 200 lines in the system prompt.

### Recommendations

#### R10.1: Trim MEMORY.md — Migrate Structural Info to Rules
**Priority: P0**
**Why it matters:** MEMORY.md has a 200-line system prompt limit. Currently it contains both structural information (which belongs in rules) and learned corrections (which belongs in auto-memory). Keeping MEMORY.md focused on learned patterns and corrections maximizes its value.

**Implementation:**
- Move project structure information to `.claude/rules/always-on.md`
- Move media buying conventions to `.claude/rules/media-buying.md`
- Keep MEMORY.md for: feedback patterns, tool-specific corrections, discovered quirks

**Leverages:** Existing MEMORY.md content

#### R10.2: Feedback-to-Rules Pipeline
**Priority: P1**
**Why it matters:** TFM has excellent feedback memory files (e.g., `feedback_no_fabricated_stats.md`, `feedback_verify_subscriber_counts_in_copy.md`). These should be encoded as rules that load conditionally when relevant, not just stored in memory.

**Implementation:** For each critical feedback file, create a corresponding rule in `.claude/rules/` with appropriate `paths:` frontmatter. Example: `feedback_no_fabricated_stats.md` becomes a rule that loads when working on creative/copy files.

This follows the existing TFM principle: "Encode lessons into skills/systems, not just memory."

**Leverages:** Existing feedback files, .claude/rules/ system

---

## 11. Headless / SDK / Programmatic Usage {#11-headless--sdk--programmatic-usage}

### What TFM Has Now
- Interactive Claude Code sessions
- n8n for server-side automation

### What's Available
**Headless mode:** `claude -p "prompt" --output-format json` runs Claude Code non-interactively with full tool access. Output can be JSON-streamed for real-time processing.

**Claude Code SDK:** Available as TypeScript and Python packages. Full programmatic control — create sessions, send messages, handle tool calls, manage context.

**Claude Code Analytics API:** Track usage, session metrics, and tool invocation patterns across your organization.

### Recommendations

#### R11.1: Headless Claude Code in n8n Workflows
**Priority: P1**
**Why it matters:** This is the bridge between n8n's scheduling/routing and Claude Code's intelligence. Any n8n workflow can call Claude Code headlessly, getting AI analysis without manual intervention.

**Pattern:**
```
n8n Schedule Trigger -> Fetch Data -> Claude Code Headless (analyze) -> Route Output -> Slack/Notion/Drive
```

**Use cases:**
- Morning anomaly detection across all 25 accounts
- Auto-draft client responses when performance questions appear in Slack
- Weekly competitive intelligence reports

**Leverages:** n8n Elestio hosting, Claude Code SDK

#### R11.2: Analytics API for Team Usage Tracking
**Priority: P2**
**Why it matters:** With 10 team members potentially using Claude Code, the Analytics API lets Jay/Nathan track which skills are used most, which sessions consume the most tokens, and where the team gets the most value. This informs where to invest in further automation.

**Leverages:** Existing Claude Code usage

---

## 12. Emerging Features {#12-emerging-features}

### Claude Code Channels (March 2026)
**What it is:** Hook up Claude Code to Discord or Telegram. Message Claude Code from your phone, instruct it to run tasks.

**TFM relevance:** Nathan or Jay could message Claude from their phone: "Run fatigue scan for houck" and get results back in Telegram/Discord. Not critical, but useful for on-the-go monitoring.

**Priority: P3**

### Voice Mode (March 2026)
**What it is:** Push-to-talk voice interaction with Claude Code. Hold spacebar, speak, release to send.

**TFM relevance:** Useful for dictating client notes or quick queries during/after client calls. "Update the jay-shetty client file: sentiment is positive, they liked the new carousel format, CPL target moving to $2.50."

**Priority: P2**

### Claude Cowork (Desktop App)
**What it is:** "Claude Code for the rest of your work" — same autonomous power without command line. Supports scheduled tasks with full MCP access.

**TFM relevance:** For non-technical team members (Sindy, GMs) who don't use the CLI. They could run skills, check reports, and get briefings through the desktop app. Scheduled tasks in Cowork could replace some n8n workflows for tasks that only need to run on a single machine.

**Priority: P1** (for team adoption)

---

## Implementation Roadmap

### This Week (P0)
| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 1 | Create `.claude/rules/` directory, split CLAUDE.md into modular rules (R2.1) | 2 hours | 30-40% context savings, cleaner sessions |
| 2 | Add PreCompact hook to preserve session state (R1.1) | 30 min | Never lose work-in-progress during compaction |
| 3 | Install SQLite MCP server for pipeboard.db (R6.1) | 30 min | Cleaner DB access for all DB-first skills |
| 4 | Trim MEMORY.md, migrate structural info to rules (R10.1) | 1 hour | Better auto-memory capacity |
| 5 | Document /effort patterns for team (R5.1) | 30 min | Immediate cost savings + quality improvement |

### This Month (P1)
| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 6 | Build /lp-monitor skill with Playwright (R8.1) | 4 hours | Catch silent LP failures before they waste spend |
| 7 | Add SessionStart hook for auto-context loading (R1.2) | 1 hour | Faster session starts, less manual context setup |
| 8 | Add Stop hook for auto session logging (R1.3) | 1 hour | Consistent session logs without manual effort |
| 9 | Install n8n-skills for workflow building (R7.1) | 1 hour | Near-100% success rate building n8n workflows |
| 10 | Build n8n -> Claude Code headless pipeline (R7.2) | 4 hours | Server-side AI analysis on schedule |
| 11 | Sub-agent pattern for /friday reports (R3.1) | 2 hours | 3-5x faster report generation |
| 12 | Desktop scheduled task for morning portfolio pulse (R4.1) | 30 min | Automated daily briefing |
| 13 | Adapt claude-ads audit for TFM (R9.1) | 4 hours | 186-check audit across all accounts |
| 14 | Install marketing copywriting skills (R9.2) | 2 hours | Better ad copy generation with guardrails |
| 15 | Feedback-to-rules pipeline (R10.2) | 2 hours | Hard-learned lessons become enforced rules |
| 16 | UTM verification with Playwright (R8.2) | 2 hours | Catch broken attribution |
| 17 | Evaluate Cowork for non-technical team (R12-Cowork) | 2 hours | Broader team AI adoption |

### This Quarter (P2)
| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 18 | Build custom TFM MCP server (R6.3) | 8 hours | Clean, typed tool calls for all TFM operations |
| 19 | Agent Teams for monthly client reviews (R3.2) | 4 hours | Parallelized deep analysis |
| 20 | n8n self-healer workflow (R7.3) | 4 hours | Self-healing automation infrastructure |
| 21 | /onboard-client skill (R9.3) | 4 hours | Hours saved per new client |
| 22 | Competitor landing page monitoring (R8.3) | 4 hours | Automated competitive intelligence |
| 23 | Upgrade creative-qa to agent-type hook (R1.4) | 2 hours | Intelligent QA instead of pattern matching |
| 24 | Voice mode for client call notes (R12-Voice) | 1 hour | Faster note-taking |
| 25 | Analytics API for team usage (R11.2) | 2 hours | Data-driven tool investment |
| 26 | GitHub MCP server (R6.2) | 30 min | Cleaner repo management |

---

## Sources

### Claude Code Features & Architecture
- [Claude Code Hooks Guide — Official Docs](https://code.claude.com/docs/en/hooks-guide)
- [Claude Code Hooks Reference: All 12 Events (Pixelmojo)](https://www.pixelmojo.io/blogs/claude-code-hooks-production-quality-ci-cd-patterns)
- [Claude Code Extensions Explained: Skills, MCP, Hooks, Subagents (Medium)](https://muneebsa.medium.com/claude-code-extensions-explained-skills-mcp-hooks-subagents-agent-teams-plugins-9294907e84ff)
- [Understanding Claude Code's Full Stack (alexop.dev)](https://alexop.dev/posts/understanding-claude-code-full-stack/)
- [Claude Code Customization: CLAUDE.md, Skills, Subagents (alexop.dev)](https://alexop.dev/posts/claude-code-customization-guide-claudemd-skills-subagents/)
- [Extend Claude with Skills — Official Docs](https://code.claude.com/docs/en/skills)
- [Claude Code March 2026 Updates (Pillitteri)](https://pasqualepillitteri.it/en/news/381/claude-code-march-2026-updates)
- [Claude Code 2.1.0 (VentureBeat)](https://venturebeat.com/orchestration/claude-code-2-1-0-arrives-with-smoother-workflows-and-smarter-agents)
- [Enabling Claude Code to Work Autonomously (Anthropic)](https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously)
- [Claude Code Changelog — Official](https://code.claude.com/docs/en/changelog)

### Agent Teams & Sub-Agents
- [Orchestrate Teams of Claude Code Sessions — Official Docs](https://code.claude.com/docs/en/agent-teams)
- [Claude Code Agent Teams Complete Guide (claudefa.st)](https://claudefa.st/blog/guide/agents/agent-teams)
- [Building a C Compiler with Parallel Claudes (Anthropic Engineering)](https://www.anthropic.com/engineering/building-c-compiler)
- [Claude Code Agent Teams Advanced Workflows (OpenAIToolsHub)](https://www.openaitoolshub.org/en/blog/claude-code-agent-teams-advanced)

### Context, Memory & Effort
- [Claude Code 1M Context Window (claudefa.st)](https://claudefa.st/blog/guide/mechanics/1m-context-ga)
- [Claude Code Context Management (claudefa.st)](https://claudefa.st/blog/guide/mechanics/context-management)
- [How Claude Remembers Your Project — Official Docs](https://code.claude.com/docs/en/memory)
- [Claude Code Rules Directory (claudefa.st)](https://claudefa.st/blog/guide/mechanics/rules-directory)
- [Auto-Memory MEMORY.md (Medium)](https://medium.com/@joe.njenga/anthropic-just-added-auto-memory-to-claude-code-memory-md-i-tested-it-0ab8422754d2)
- [Claude Code Effort Levels (kentgigger.com)](https://kentgigger.com/posts/claude-code-effort-parameter)
- [PreCompact Hook Explained (yuanchang.org)](https://yuanchang.org/en/posts/claude-code-auto-memory-and-hooks/)

### MCP Ecosystem
- [Official MCP Registry](https://registry.modelcontextprotocol.io/)
- [Awesome MCP Servers (1200+)](https://mcp-awesome.com/)
- [MCP Servers Directory (593+)](https://aiagentslist.com/mcp-servers)
- [MCP TypeScript SDK (GitHub)](https://github.com/modelcontextprotocol/typescript-sdk)
- [Build an MCP Server — Official Guide](https://modelcontextprotocol.io/docs/develop/build-server)
- [SQLite MCP Server (PyPI)](https://pypi.org/project/mcp-server-sqlite/)

### n8n Integration
- [Claude Code + n8n: Self-Building Agents (ability.ai)](https://www.ability.ai/blog/claude-code-n8n-workflows)
- [n8n-MCP Server (GitHub)](https://github.com/czlonkowski/n8n-mcp)
- [n8n-Skills for Claude Code (GitHub)](https://github.com/czlonkowski/n8n-skills)
- [Build AI Agents with n8n + Claude API (n8nlab.io)](https://n8nlab.io/blog/build-ai-agents-n8n-claude-api)

### Marketing & Agency Applications
- [Claude Code for Paid Ads (Metaflow)](https://metaflow.life/blog/claude-code-for-paid-ads)
- [Claude Code Agent Teams for Marketing (Marketing Agent Blog)](https://marketingagent.blog/2026/02/13/claude-code-agent-teams-for-marketing-a-primer/)
- [Claude Code Marketing Agency Workflow (RSL/A)](https://rsla.io/blog/claude-code-marketing-agency-workflow)
- [Claude Ads — 186 Audit Checks (GitHub)](https://github.com/AgriciDaniel/claude-ads)
- [Marketing Skills for Claude Code (GitHub)](https://github.com/coreyhaines31/marketingskills)
- [5 Ways Claude Code Changes Agencies (AdventurePPC)](https://www.adventureppc.com/blog/5-ways-claude-code-is-changing-how-digital-agencies-work-in-2026)

### Scheduled Tasks & Automation
- [Run Prompts on a Schedule — Official Docs](https://code.claude.com/docs/en/scheduled-tasks)
- [Claude Code Scheduled Tasks Setup (claudefa.st)](https://claudefa.st/blog/guide/development/scheduled-tasks)
- [Claude Code SDK & Headless Mode — Official Docs](https://code.claude.com/docs/en/headless)
- [Schedule Recurring Tasks in Cowork (Claude Help Center)](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-cowork)

### Playwright & Browser Automation
- [Playwright MCP Server (GitHub/Microsoft)](https://github.com/microsoft/playwright-mcp)
- [Playwright MCP Servers for AI Testing (Bug0)](https://bug0.com/blog/playwright-mcp-servers-ai-testing)
- [Competitor Website Scraping with Claude Code (AdventurePPC)](https://www.adventureppc.com/blog/how-to-use-claude-code-to-scrape-and-analyze-competitor-websites-ethically)

### Skills & Plugins Ecosystem
- [Awesome Claude Code (GitHub)](https://github.com/hesreallyhim/awesome-claude-code)
- [Awesome Claude Code Toolkit — 135 Agents, 35+ Skills (GitHub)](https://github.com/rohitg00/awesome-claude-code-toolkit)
- [Awesome Claude Skills (awesome-skills.com)](https://awesome-skills.com/)
- [Awesome Claude Plugins (GitHub/Composio)](https://github.com/ComposioHQ/awesome-claude-plugins)
