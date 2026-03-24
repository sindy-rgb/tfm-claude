# Obsidian + Claude Code Superbrain: Research for The Feed Media

> **Date:** 2026-03-19
> **Purpose:** Turn Obsidian into an AI-powered agency superbrain for 19 newsletter growth clients
> **Stack:** Obsidian + Claude Code + MCP + n8n + Day.ai + NotebookLM

---

## 1. Obsidian Plugins for AI Workflows — Install NOW

### Tier 1: Install Today (Core AI Layer)

#### Smart Connections (FREE)
- **What it does:** Semantic search across your entire vault using AI embeddings. Shows related notes in a sidebar based on meaning, not just keywords.
- **Why it matters for 19 clients:** When you open a client note, Smart Connections surfaces related strategy docs, past campaign results, and meeting notes from OTHER clients with similar challenges — automatically.
- **Setup:** Install from Community Plugins > enable > it starts indexing immediately with a local model. No API key needed for basic use.
- **Pro tip:** v4 works out of the box. The built-in local model creates embeddings without external tools or API keys.
- **Link:** [github.com/brianpetro/obsidian-smart-connections](https://github.com/brianpetro/obsidian-smart-connections)

#### Copilot for Obsidian (FREE)
- **What it does:** AI chat interface inside Obsidian. Ask questions about your vault, generate content, summarize notes.
- **Why it matters:** Ask "What growth tactics worked for clients in the fitness niche?" and it searches across all 19 client folders to synthesize an answer.
- **Setup:** Install from Community Plugins > configure with your Anthropic API key (Claude), OpenAI key, or use local models via Ollama.
- **Supports:** Claude, GPT-4, Gemini, local models via Ollama/LM Studio.
- **Link:** [obsidiancopilot.com](https://www.obsidiancopilot.com/en)

#### Claudian (Claude Code in Obsidian)
- **What it does:** Embeds Claude Code as a sidebar chat inside Obsidian with full agentic capabilities — file read/write, bash commands, vision, MCP servers, and multi-step workflows.
- **Why it matters:** Run Claude Code directly in your vault without switching to a terminal. Use slash commands, @-mention files, and get inline editing with word-level diff preview.
- **Setup:** Install via BRAT plugin (Community Plugins), or clone from [github.com/YishenTu/claudian](https://github.com/YishenTu/claudian).
- **Key feature:** Type `/` for custom slash commands, `#` for custom system prompt instructions.

### Tier 2: Install This Week (Structure & Automation)

#### Dataview
- **What it does:** Query your vault like a database. Create dynamic tables, lists, and dashboards from frontmatter metadata.
- **Why it matters for agency:** Build a single "Client Dashboard" note that auto-generates a table of all 19 clients with their current status, next deliverable date, subscriber count, and last meeting date — all pulled from frontmatter in each client file.
- **Example query:**
  ```dataview
  TABLE status, subscribers, next-deliverable, last-meeting
  FROM "clients"
  SORT next-deliverable ASC
  ```
- **Link:** [obsidian.md/plugins?search=dataview](https://obsidian.md/plugins?search=dataview)

#### Templater
- **What it does:** Advanced templating with JavaScript execution. Auto-populate notes with dates, prompts, folder-specific templates.
- **Why it matters:** Create a "New Client Onboarding" template that auto-generates the folder structure, strategy doc skeleton, meeting notes folder, and KPI tracker for each new client.
- **Example:** Template that prompts for client name, niche, current subscriber count, and auto-creates linked notes.
- **Link:** [github.com/SilentVoid13/Templater](https://github.com/SilentVoid13/Templater)

#### Tasks
- **What it does:** Track tasks across your entire vault with due dates, priorities, and filters.
- **Why it matters:** One view showing all deliverables across 19 clients, sorted by due date.

### Tier 3: Install When Ready (Advanced)

#### Obsidian Post Webhook
- **What it does:** Sends note content (including YAML frontmatter) to any webhook endpoint.
- **Why it matters:** Bridge between Obsidian and n8n — trigger automations when you update a client note.

#### Agent Client
- **What it does:** Brings Claude Code, Codex, and Gemini CLI inside Obsidian as embedded terminals.
- **Why it matters:** Run any AI agent directly in your vault without context-switching.

---

## 2. NotebookLM by Google — The Audio Companion

### What It Is
NotebookLM is Google's AI research tool that ingests documents and lets you query them. Its killer feature is **Audio Overviews** — AI-generated podcast-style briefings from your documents.

### Key Features (2026)

| Feature | What It Does | Agency Use Case |
|---------|-------------|-----------------|
| **Audio Overview (Deep Dive)** | Two AI hosts discuss your docs in a 20-min podcast | Weekly client portfolio review while commuting |
| **Audio Overview (Brief)** | 5-minute executive summary | Quick catch-up before a client call |
| **Lecture Mode (NEW 2026)** | 30-min single-narrator deep explanation | Training new team members on a client's history |
| **Interactive Mode** | Join the AI podcast live, ask questions | Prep for strategy sessions — interrupt to drill into specifics |
| **Critique/Debate Modes** | AI hosts argue different perspectives | Stress-test a campaign strategy before presenting to client |

### Where NotebookLM Complements Claude (Not Overlaps)

| Task | Use Claude | Use NotebookLM |
|------|-----------|----------------|
| Writing newsletter drafts | YES | No |
| Searching vault for patterns | YES (via MCP) | No |
| Audio briefing on client portfolio | No | YES |
| Summarizing 50-page strategy doc | Either works | YES (audio format) |
| Building automations | YES | No |
| Preparing for a client call on-the-go | No | YES (generate 5-min brief, listen in car) |
| Cross-referencing meeting transcripts | YES | YES (upload transcripts, ask questions) |

### Practical Workflow for The Feed Media
1. **Weekly:** Export the week's meeting transcripts + campaign results as PDFs
2. **Upload** to a NotebookLM notebook called "Week of [date]"
3. **Generate** a 5-min Audio Brief for each client or a 20-min portfolio overview
4. **Listen** during commute or gym — arrive at Monday meetings already briefed
5. **Deep dives:** Upload all docs for a specific client before a strategy session, use Interactive Mode to prep

### Limitations
- NotebookLM does NOT connect to Obsidian natively (you export/upload manually or via Google Drive)
- 50 source limit per notebook (enough for one client's key docs, not all 19 at once)
- No API for automation yet — it is a manual upload workflow
- Audio generation takes about 45 seconds for a 20-minute overview

---

## 3. MCP Servers for Obsidian — Connect Claude Code Directly to Your Vault

### What MCP Is
Model Context Protocol (MCP) is an open standard that lets AI tools (like Claude Code) read, search, and write to external data sources. Think of it as giving Claude a direct line into your Obsidian vault.

### Best MCP Options for Your Setup

#### Option A: obsidian-claude-code-mcp (RECOMMENDED)
- **By:** Ian Sinnott
- **What it does:** Obsidian plugin that runs an MCP server. Claude Code auto-discovers and connects via WebSocket.
- **Why best for you:** Zero config on the Claude Code side — it just finds your vault.
- **Setup steps:**
  1. Install the plugin in Obsidian (via BRAT or manual install)
  2. Enable the plugin — it starts an MCP server on port 22360
  3. Open Claude Code in your vault directory
  4. Claude Code auto-discovers the WebSocket connection
  5. Test: Ask Claude "What files are in my Obsidian vault?"
- **For Claude Desktop:** Add to config:
  ```json
  {
    "mcpServers": {
      "obsidian": {
        "command": "npx",
        "args": ["mcp-remote", "http://localhost:22360/sse"],
        "env": {}
      }
    }
  }
  ```
- **Multiple vaults:** Each vault needs a unique port (configure in plugin settings)
- **Link:** [github.com/iansinnott/obsidian-claude-code-mcp](https://github.com/iansinnott/obsidian-claude-code-mcp)

#### Option B: MCP-Vault (@bitbonsai/mcpvault)
- **What it does:** Universal AI bridge for Obsidian vaults, works with any MCP-compatible client.
- **v0.9.0 (March 2026):** Renamed to @bitbonsai/mcpvault on npm.
- **Link:** [mcp-obsidian.org](https://mcp-obsidian.org/)

#### Option C: mcp-obsidian (by MarkusPfundstein)
- **What it does:** Connects via Obsidian's REST API community plugin.
- **Best for:** If you want to keep the MCP server separate from Obsidian.
- **Link:** [github.com/MarkusPfundstein/mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian)

#### Option D: obsidian-notes-rag (MCP + RAG combined)
- **What it does:** Local vector store for semantic search over your vault, exposed via MCP.
- **Best for:** When you want Claude to do semantic search, not just file/folder browsing.
- **Link:** [github.com/proofgeist/obsidian-notes-rag](https://github.com/proofgeist/obsidian-notes-rag)

### What Claude Code Can Do Once Connected via MCP
- **Read** any note in your vault (client briefs, meeting notes, strategy docs)
- **Search** across all 19 client folders for patterns, insights, past decisions
- **Create** new notes (meeting summaries, content drafts, reports)
- **Edit** existing notes (update KPIs, add action items)
- **Navigate** your vault's structure and understand the graph

### Agency-Specific Power Moves
- "Search across all client meeting notes for anyone who mentioned churn problems"
- "Create a weekly report for Client X based on their last 4 meeting notes"
- "What growth tactics have we used for e-commerce clients? Compile from all relevant files"
- "Update the KPI dashboard for all clients with this week's numbers" (pass it a spreadsheet)

---

## 4. RAG Setups — Intelligent Search Across 19 Client Files

### Why You Need RAG
With 19 clients, your vault will have hundreds (eventually thousands) of notes. Standard search finds keywords. RAG (Retrieval-Augmented Generation) finds **meaning** — "which clients had subscriber plateaus in Q1" even if no note literally says "plateau."

### Option A: Smart Connections (Simplest — Already Covered)
- Built-in local embeddings, no setup needed.
- Good for: Personal use, quick semantic search.
- Limitation: Lives inside Obsidian only — Claude Code cannot directly query it.

### Option B: obsidian-notes-rag + MCP (RECOMMENDED for Agency Scale)
- **Stack:** OpenAI/Ollama embeddings + sqlite-vec (replaced ChromaDB in v1.0.0) + MCP server
- **Why:** Claude Code can query your vault semantically via MCP. Ask Claude a question, it searches embeddings, pulls relevant chunks, and synthesizes an answer.
- **Setup:**
  1. Clone [github.com/proofgeist/obsidian-notes-rag](https://github.com/proofgeist/obsidian-notes-rag)
  2. Configure vault path to your Obsidian vault
  3. Choose embedding model:
     - **OpenAI** `text-embedding-3-small` (fast, cheap, best quality)
     - **Local** via Ollama with `nomic-embed-text` (free, private, slightly lower quality)
  4. Run the indexer — it chunks your markdown files and creates embeddings
  5. Add the MCP server to your Claude Code config
  6. Query: "What patterns do we see across clients in the health niche?"

### Option C: Full Custom RAG Pipeline (Advanced)
- **Stack:** LangChain + ChromaDB/sqlite-vec + Ollama + Python
- **When to use:** If you want to include non-Obsidian data (PDFs, spreadsheets, Slack exports)
- **Architecture:**
  ```
  Obsidian Vault (markdown) ─┐
  Meeting Transcripts (PDF)  ─┤
  Slack Exports (JSON)       ─┼─> LangChain Loader ─> Chunking ─> Embeddings ─> ChromaDB
  Meta Ads Reports (CSV)     ─┤
  Email Threads (EML)        ─┘
                                                                        │
                                                            Claude queries via API
  ```
- **Key libraries:** `pip install chromadb sentence-transformers langchain langchain-community langchain-text-splitters langchain-ollama`
- **Performance benchmarks (2026):**
  - Semantic chunking: 0.79-0.82 faithfulness scores
  - Hybrid retrieval (BM25 + vector): Best for mixed keyword/semantic queries
  - Agentic RAG: 35-50% better on complex multi-hop queries

### Recommendation for Today
Start with **Option B** (obsidian-notes-rag + MCP). It gives Claude Code semantic search over your vault with minimal setup. Graduate to Option C when you need to include Slack, email, and ad platform data.

---

## 5. n8n Automations — Auto-Feed Data into Obsidian

### Overview
n8n is a self-hosted (or cloud) workflow automation platform. Think Zapier but with 400+ integrations, code nodes, and AI agent capabilities. It is the glue connecting Day.ai, Slack, Meta Ads, and Obsidian.

### Getting Data INTO Obsidian via n8n

#### Automation 1: Meeting Transcripts to Obsidian
```
Trigger: Day.ai meeting ends (webhook or scheduled check)
  → n8n HTTP Request: Pull transcript from Day.ai API
  → n8n AI Node: Summarize with Claude (key decisions, action items, sentiment)
  → n8n Code Node: Format as markdown with YAML frontmatter
  → n8n Google Drive / Local File: Write .md to Obsidian vault sync folder
```
**Frontmatter example:**
```yaml
---
type: meeting-notes
client: "{{client_name}}"
date: "{{meeting_date}}"
attendees: ["Jay", "{{client_contact}}"]
action-items: 3
sentiment: positive
tags: [meeting, client/{{client_slug}}]
---
```

#### Automation 2: Slack Channel Summaries
```
Trigger: Daily at 6 PM (Cron node)
  → n8n Slack Node: Pull messages from #client-updates channel (last 24h)
  → n8n AI Node: Summarize key updates per client
  → n8n Code Node: Format as daily digest markdown
  → Write to: vault/daily-digests/{{date}}.md
```

#### Automation 3: Meta Ads Weekly Reports
```
Trigger: Every Monday 8 AM
  → n8n HTTP Request: Pull Meta Ads data for each of 19 ad accounts
  → n8n Code Node: Calculate WoW changes, flag anomalies
  → n8n AI Node: Generate narrative summary per client
  → Write to: vault/clients/{{client}}/ads/weekly-{{date}}.md
  → Bonus: n8n Slack Node: Post summary to #ads-performance
```

#### Automation 4: iOS Meeting Notes (Voice Memos)
```
Trigger: n8n Webhook receives audio from iPhone shortcut
  → n8n AI Node: Transcribe with Whisper (or Apple on-device transcription)
  → n8n AI Node: Summarize and extract action items
  → Write to: vault/meetings/{{date}}-mobile-note.md
```

### Day.ai Integration Strategy
Day.ai does not have a native n8n node, but you can connect via:
1. **Day.ai MCP Server** — Claude can already read Day.ai data via the Day.ai MCP tools available in your setup (you have these: `mcp__claude_ai_Day_AI__search_objects`, `mcp__claude_ai_Day_AI__get_meeting_recording_context`, etc.)
2. **n8n HTTP Request Node** — Use Day.ai's API with your credentials to pull meeting data on a schedule
3. **Webhook approach** — If Day.ai supports webhooks for meeting completion events, trigger n8n workflows automatically

### Key n8n Patterns for Obsidian

| Pattern | How It Works |
|---------|-------------|
| **Google Drive Sync** | n8n writes .md files to a Google Drive folder synced with Obsidian (simplest) |
| **Local File System** | n8n writes directly to vault folder if self-hosted on same machine |
| **Post Webhook Plugin** | Obsidian plugin that receives webhooks — n8n sends data TO Obsidian |
| **Git Commit** | n8n writes files and commits to a git repo that syncs your vault |

---

## 6. Proposed Architecture — The Full Data Flow

### System Diagram

```
                    ┌─────────────────────────────────────┐
                    │         DATA SOURCES                 │
                    │                                       │
                    │  Day.ai (meetings, CRM, transcripts) │
                    │  Slack (client channels, updates)     │
                    │  Meta Ads (campaign performance)      │
                    │  Email (client comms)                 │
                    │  Voice Memos (mobile meeting notes)   │
                    └──────────────┬────────────────────────┘
                                   │
                          ┌────────▼────────┐
                          │     n8n         │
                          │  (automation    │
                          │   hub)          │
                          └────────┬────────┘
                                   │
                    Formats as markdown with frontmatter
                                   │
                          ┌────────▼────────┐
                          │  OBSIDIAN VAULT │
                          │                 │
                          │  /clients/      │  ← 19 client folders
                          │  /meetings/     │  ← auto-generated from Day.ai
                          │  /daily-digest/ │  ← auto-generated from Slack
                          │  /ads-reports/  │  ← auto-generated from Meta
                          │  /templates/    │  ← Templater templates
                          │  /dashboards/   │  ← Dataview queries
                          │  CLAUDE.md      │  ← Claude's memory file
                          └────────┬────────┘
                                   │
                    ┌──────────────┼──────────────┐
                    │              │              │
              ┌─────▼─────┐ ┌─────▼─────┐ ┌─────▼──────┐
              │ Smart      │ │ MCP       │ │ NotebookLM │
              │ Connections│ │ Server    │ │ (manual    │
              │ (in-vault  │ │ (Claude   │ │  upload)   │
              │  semantic  │ │  Code     │ │            │
              │  search)   │ │  access)  │ │ Audio      │
              └────────────┘ └─────┬─────┘ │ Briefings  │
                                   │       └────────────┘
                          ┌────────▼────────┐
                          │  CLAUDE CODE    │
                          │                 │
                          │  Read vault     │
                          │  Search notes   │
                          │  Write content  │
                          │  Run analysis   │
                          │  Draft emails   │
                          │  Generate recs  │
                          └─────────────────┘
```

### What to Automate vs. Keep Manual

| Process | Automate | Manual | Why |
|---------|----------|--------|-----|
| Meeting transcript → vault | YES (n8n) | | Predictable, repeatable |
| Transcript → summary + action items | YES (n8n + Claude) | | AI handles this well |
| Slack daily digest | YES (n8n) | | Daily cadence, no judgment needed |
| Meta Ads weekly reports | YES (n8n) | | Data pull + formatting |
| Client strategy decisions | | YES | Needs human judgment |
| Content calendar updates | SEMI (Claude drafts) | Review + approve | AI suggests, human decides |
| Onboarding new client | SEMI (Templater) | Customize strategy | Template creates structure, you fill strategy |
| NotebookLM audio briefings | | YES (upload docs weekly) | No API yet |
| Cross-client pattern analysis | YES (Claude + RAG) | Interpret results | AI finds patterns, you decide action |
| KPI dashboard updates | YES (n8n pulls data) | | Numbers flow automatically |

### Vault Folder Structure

```
the vault/
├── the-feed-media/
│   ├── clients/
│   │   ├── client-001-[name]/
│   │   │   ├── _overview.md          (frontmatter: status, niche, KPIs)
│   │   │   ├── strategy.md
│   │   │   ├── meetings/
│   │   │   │   └── 2026-03-19.md     (auto-generated)
│   │   │   ├── ads-reports/
│   │   │   │   └── week-2026-03-17.md (auto-generated)
│   │   │   ├── content/
│   │   │   └── notes/
│   │   ├── client-002-[name]/
│   │   │   └── ...
│   │   └── ... (19 total)
│   ├── dashboards/
│   │   ├── all-clients.md            (Dataview: master table)
│   │   ├── deliverables.md           (Tasks: what's due)
│   │   └── weekly-review.md          (Dataview: this week's metrics)
│   ├── daily-digests/
│   │   └── 2026-03-19.md             (auto from Slack)
│   ├── playbooks/
│   │   ├── growth-tactics.md
│   │   ├── onboarding-checklist.md
│   │   └── client-offboarding.md
│   ├── templates/
│   │   ├── new-client.md
│   │   ├── meeting-notes.md
│   │   ├── weekly-ads-report.md
│   │   └── strategy-doc.md
│   ├── research/
│   │   └── obsidian-superbrain-research.md  (this file)
│   └── CLAUDE.md                      (Claude's memory / vault conventions)
```

### The CLAUDE.md File (Critical)

This file lives at the vault root and is loaded into every Claude Code session. It tells Claude:

```markdown
# CLAUDE.md — The Feed Media Vault

## Vault Structure
- 19 clients in /clients/, each with overview, strategy, meetings, ads-reports
- Frontmatter conventions: type, client, date, status, tags
- Dataview dashboards in /dashboards/

## Conventions
- Client slugs: lowercase-hyphenated (e.g., client-fitness-brand)
- Meeting notes: YYYY-MM-DD.md in client/meetings/
- Status values: active, onboarding, paused, churned
- All dates: YYYY-MM-DD format

## Current Priorities
- [Update weekly with top priorities]

## What I Should Know
- Jay runs The Feed Media, a newsletter growth agency with 19 clients
- Primary services: newsletter growth, audience development, Meta Ads
- Key tools: Day.ai (CRM/meetings), Slack, Meta Ads Manager
- Deliverable cadence: [define per client]
```

---

## 7. Five Quick Wins for Today (30 Minutes Total)

### Quick Win 1: Install Smart Connections + Copilot (5 min)
1. Open Obsidian > Settings > Community Plugins > Browse
2. Search "Smart Connections" > Install > Enable
3. Search "Copilot" > Install > Enable
4. In Copilot settings, add your Anthropic API key
5. **Immediate value:** Open any client note, see related notes in the Smart Connections sidebar. Ask Copilot questions about your vault.

### Quick Win 2: Create CLAUDE.md at Vault Root (5 min)
1. Create a new note called `CLAUDE.md` in your vault root
2. Write your vault structure, naming conventions, and current priorities (use the template in Section 6)
3. **Immediate value:** Every Claude Code session now understands your vault. Run `claude` in your vault directory and it automatically reads CLAUDE.md.

### Quick Win 3: Install the Obsidian Claude Code MCP Plugin (10 min)
1. Install BRAT plugin (Community Plugins > Browse > "BRAT")
2. In BRAT settings, add repo: `iansinnott/obsidian-claude-code-mcp`
3. Enable the plugin — MCP server starts on port 22360
4. Open terminal in your vault directory, run `claude`
5. Test: "What notes do I have about [client name]?"
6. **Immediate value:** Claude Code can now read, search, and write to your vault directly.

### Quick Win 4: Create Client Frontmatter Template with Templater (5 min)
1. Install Templater (Community Plugins)
2. Create `/templates/new-client.md`:
```markdown
---
type: client
client: "<% tp.system.prompt("Client name") %>"
niche: "<% tp.system.prompt("Niche") %>"
status: onboarding
subscribers: <% tp.system.prompt("Current subscribers") %>
start-date: <% tp.date.now("YYYY-MM-DD") %>
tags: [client]
---

# <% tp.system.prompt("Client name") %>

## Overview
-

## Strategy
-

## KPIs
| Metric | Baseline | Target | Current |
|--------|----------|--------|---------|
| Subscribers | | | |
| Open Rate | | | |
| Growth Rate | | | |

## Meeting Notes
```dataview
LIST FROM "clients/<% tp.system.prompt("Client slug") %>/meetings"
SORT file.name DESC
```
```
3. Set Templater to use `/templates/` as the template folder
4. **Immediate value:** Onboard new clients with consistent structure. Dataview auto-lists their meeting notes.

### Quick Win 5: Set Up a NotebookLM Notebook for Your Top 3 Clients (5 min)
1. Go to [notebooklm.google.com](https://notebooklm.google.com)
2. Create a notebook for your highest-priority client
3. Upload their strategy doc, last 3 meeting transcripts, and latest ads report
4. Click "Audio Overview" > choose "Brief" (5 min)
5. **Immediate value:** Listen to an AI-generated briefing about this client's situation on your next drive. Use Interactive Mode to ask follow-up questions.

---

## Appendix: Tool Comparison Matrix

| Capability | Smart Connections | Copilot | Claude Code + MCP | NotebookLM | n8n |
|-----------|-------------------|---------|-------------------|------------|-----|
| Semantic search | YES (in-vault) | YES (in-vault) | YES (via RAG MCP) | YES (per notebook) | No |
| Write to vault | No | No | YES | No | YES |
| Audio output | No | No | No | YES | No |
| Automation | No | No | YES (scripting) | No | YES |
| Multi-client analysis | Limited | YES | YES (best) | No (50 source limit) | No |
| Works offline | YES (local model) | With Ollama | No | No | Self-hosted yes |
| Cost | Free | Free + API costs | Claude subscription | Free tier available | Free self-hosted |

## Appendix: Key Links

- [Smart Connections](https://smartconnections.app)
- [Copilot for Obsidian](https://www.obsidiancopilot.com/en)
- [Claudian Plugin](https://github.com/YishenTu/claudian)
- [Obsidian Claude Code MCP](https://github.com/iansinnott/obsidian-claude-code-mcp)
- [MCP-Vault](https://mcp-obsidian.org/)
- [obsidian-notes-rag](https://github.com/proofgeist/obsidian-notes-rag)
- [Templater](https://github.com/SilentVoid13/Templater)
- [Dataview](https://obsidian.md/plugins?search=dataview)
- [n8n](https://n8n.io/)
- [NotebookLM](https://notebooklm.google.com)
- [n8n + Obsidian Post Webhook](https://community.n8n.io/t/connect-obsidian-and-n8n-with-the-post-webhook-plugin/63821)
- [COG Second Brain (Claude-Obsidian-GitHub)](https://github.com/huytieu/COG-second-brain)
- [Building a Retrieval API for Obsidian](https://laurentcazanove.com/blog/obsidian-rag-api)
