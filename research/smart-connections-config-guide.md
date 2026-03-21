# Smart Connections & Copilot Plus Configuration Guide for TFM

> **Date:** 2026-03-21
> **Vault:** the-feed-media (144 markdown files, 25 clients)
> **Installed versions:** Smart Connections v4.1.8, Copilot v3.2.5 (Plus license active)

---

## Important Clarification: Two Separate Plugins

You have **two** AI plugins that serve different purposes:

| Plugin | Purpose | Developer |
|--------|---------|-----------|
| **Smart Connections** | Semantic similarity sidebar + Smart Chat | Brian Petro |
| **Copilot** (Plus license) | AI chat with vault RAG, agents, memory | Logan Yang |

They use **separate** embedding indexes and **separate** settings. Both are worth keeping — they complement each other. Configure both.

---

## Part 1: Smart Connections Configuration

### Current State (What Needs Changing)

Your current `smart_env.json` shows:
- Embedding model: `TaylorAI/bge-micro-v2` (local, very small, lowest quality)
- Folder exclusions: **none** (indexing everything including templates, copilot conversations)
- File exclusions: only "Untitled"
- Chat model: Ollama (no model specified — likely broken)
- Results limit: 20 (fine)
- Block embedding: enabled with 200 char minimum (fine)

### Step-by-Step: Smart Connections Settings

Open Obsidian > Settings > Smart Connections (or Smart Environment if it shows as a separate entry).

#### 1A. Embedding Model — UPGRADE

**Current:** `TaylorAI/bge-micro-v2` (local transformers, ~25M params, lowest tier)
**Recommendation:** Stay local but upgrade, OR use an API model.

**Option A — Best quality, requires no API key (recommended):**
Keep the local `transformers` adapter but check if Smart Connections v4 offers a larger local model in the dropdown. The `bge-micro-v2` is the smallest option. If `bge-small-en-v1.5` or `bge-base-en-v1.5` are available, choose `bge-base-en-v1.5`. It's 6x larger but still runs locally in seconds on your Mac.

**Option B — Best quality overall:**
Since you already have Copilot Plus with API access, and your vault is small (144 files), you could use an API-based model. In Smart Environment settings, switch the embedding platform from `transformers` to one of:
- `OpenAI text-embedding-3-small` — excellent quality, very cheap (~$0.02 for your entire vault)
- `OpenAI text-embedding-3-large` — highest quality, still cheap (~$0.13 for your entire vault)

However, this requires an OpenAI API key set in Smart Environment. Given that your Copilot plugin already handles the heavy RAG work with `copilot-plus-small` embeddings, **keeping Smart Connections on a local model is fine.** The sidebar similarity feature doesn't need perfect embeddings — directional similarity is enough.

**Verdict:** If a `bge-base` or `bge-small` option appears in the model dropdown, pick it. Otherwise, the current `bge-micro-v2` is acceptable for sidebar connections. Don't overthink this — Copilot Plus handles the serious retrieval.

#### 1B. Folder Exclusions — ADD THESE

In Smart Connections settings, find **Folder Exclusions** and add:

```
templates, copilot, copilot/copilot-conversations, copilot/copilot-custom-prompts, scripts, dashboards
```

**Why each one:**
- `templates` — Template files contain placeholder variables, not real content. They pollute similarity results.
- `copilot` — Contains AI conversation logs and custom prompts. These are noise for Smart Connections similarity matching.
- `scripts` — If this contains automation code, it's not useful for semantic connections.
- `dashboards` — Dataview-heavy files with queries rather than content; they produce false positive connections.

**What to KEEP indexed:**
- `clients/` — The core. All 25 client intelligence files + deep enrichments + Claude Chat projects. This is the gold.
- `memory/` — Media buying SOPs, session logs, project memory. Valuable for cross-referencing.
- `system/` — Framework, creative frameworks, onboarding prompts. Useful for connecting client strategy back to methodology.
- `research/` — Research docs surface when relevant. Keep them.
- `team/` — Team profiles. Useful when Smart Connections links a client to the GM who manages them.
- `prompts/` — Master prompt library. Useful for finding relevant prompts while working on a client.

#### 1C. File Exclusions

Add to file exclusions:
```
Untitled, CLIENT-INTELLIGENCE-SUMMARY
```

The summary file is a condensed rollup. Including it causes every client file to match the summary instead of matching *each other* — which defeats the purpose.

#### 1D. Excluded Headings

Leave blank (current setting). Your client intelligence files use a consistent 6-category framework, and heading-level blocks are useful for Smart Connections to surface specific sections.

#### 1E. Chat Model — FIX OR DISABLE

Your Smart Chat is configured for Ollama with no model specified. Either:

**Option A (recommended):** Don't use Smart Chat at all. Use Copilot Plus for chat instead — it's better configured and you're paying for it.

**Option B:** If you want Smart Chat working, switch the chat model platform in Smart Environment from `ollama` to `open_router` (which is already set as your `chat_completion_platform`), then select a model. But this duplicates what Copilot already does.

#### 1F. Connections Display Settings

Your current settings are good:
- `results_limit: 20` — Fine. Could reduce to 10-15 if the sidebar feels cluttered.
- `exclude_frontmatter_blocks: true` — Correct. Frontmatter metadata creates false matches.
- `render_markdown: true` — Good for readability.
- `show_full_path: false` — Fine, saves space. Change to `true` if you want to see which client folder a result comes from at a glance.

**Consider changing:** Set `show_full_path` to `true`. When browsing connections for a client, seeing `clients/workweek/workweek.md` is more useful than just `workweek`.

#### 1G. Lookup Settings

Your lookup (semantic search) shows blocks by default with 20 results. This is good. Blocks are more useful than whole-note matches for your use case since client files are 200-340 lines each.

---

## Part 2: Copilot Plus Configuration

### Current State

Your Copilot Plus is well-configured already. Key current settings:
- Chat model: `copilot-plus-flash` (built-in, no API key needed)
- Embedding model: `copilot-plus-small` (built-in)
- Temperature: 0.1 (conservative, factual — correct for agency work)
- Max tokens: 6,000
- Context turns: 15
- Max source chunks: 30
- QA exclusions: `copilot` (correct — excludes its own conversation logs)
- Auto-save chat: on
- Autonomous agent: enabled with 4 max iterations
- Reasoning effort: low
- Lexical boosts: enabled

### Step-by-Step: Copilot Settings Changes

Open Obsidian > Settings > Copilot.

#### 2A. Embedding Model — UPGRADE TO LARGE

**Current:** `copilot-plus-small`
**Recommendation:** Switch to `copilot-plus-large` (1024 dimensions, Jina-based)

Since you have Plus, you get `copilot-plus-large` included. The large model produces significantly better retrieval for domain-specific content like ad performance data, creative frameworks, and client-specific terminology. Your vault is small enough that re-indexing will take under a minute.

**How:** In Copilot settings, find the embedding model dropdown and switch from `copilot-plus-small` to `copilot-plus-large`.

After switching, trigger a re-index: the setting `indexVaultToVectorStore` is set to "ON MODE SWITCH" — you may need to toggle it or restart Obsidian for re-indexing.

#### 2B. QA Exclusions — EXPAND

**Current:** `copilot`
**Recommendation:** Add more folders to exclude from Copilot's RAG retrieval:

In the `qaExclusions` field, change to:
```
copilot, templates, dashboards, scripts
```

Same logic as Smart Connections: templates and dashboards are noise for retrieval.

#### 2C. Temperature — Keep at 0.1

0.1 is correct for agency work. You want factual retrieval, not creative responses. The client intelligence files contain specific numbers (CPL targets, subscriber counts, never-say rules) that need to be returned accurately.

#### 2D. Max Source Chunks — Consider Increasing

**Current:** 30
**Recommendation:** Increase to 40-50.

With 25 clients, when asking cross-client questions ("What creative angles work for B2B newsletters?"), 30 chunks may not surface enough variety across clients. 50 chunks gives better coverage without meaningfully slowing responses.

#### 2E. Reasoning Effort — Increase to Medium

**Current:** `low`
**Recommendation:** Switch to `medium`.

For an agency vault with complex cross-client analysis, "low" may produce superficial answers. Medium gives better synthesis without being slow.

#### 2F. Context Turns — Keep at 15

15 is generous and fine. Allows multi-turn conversations about a client without losing thread context.

#### 2G. System Prompt — ADD A TFM-SPECIFIC ONE

**Current:** Empty (`userSystemPrompt: ""`)

This is the biggest missed optimization. Create a system prompt. In Copilot settings, find the system prompt field and add:

```
You are an AI assistant for The Feed Media (TFM), a newsletter growth agency managing 25 clients. When answering questions:

1. Always reference specific client data from the vault when available
2. When asked about creative strategy, check client intelligence files for NEVER rules before suggesting approaches
3. Use DCT (Dynamic Creative Testing) 4-3-2-2 methodology as the default framework
4. CPL benchmarks vary by client — always specify which client's benchmark you're referencing
5. When comparing clients, organize by vertical (B2B, fitness, finance, travel/points, news)
6. Landing page CVR benchmark is 40%+ for newsletters
7. For media buying questions, reference the media-buying-sop in the memory folder

Key verticals in the portfolio:
- Finance/investing: MarketBeat, Stocks & Income, Stocks News, Contrarian Thinking
- Points/travel: The Points Guy, Points Path
- B2B/professional: WorkWeek, Insight Links, Vendry, Big Desk Energy, Open Source CEO
- Lifestyle/wellness: Jay Shetty, RNT Fitness, How to AI, MDhair
- News/media: Quartz, Status News, Daily Drop
- Creator economy: Creator Spotlight, Houck
- Niche: 1636 Forum, Franklin's Forum, Just Women's Sports, Student Loan Planner, Experiential Hospitality
```

**Alternative (file-based):** Your Copilot has `userSystemPromptsFolder` set to `copilot/system-prompts`. Create a file there instead:

Create `copilot/system-prompts/TFM Agency Assistant.md` with the prompt above, then set it as the default system prompt in Copilot settings.

#### 2H. Autonomous Agent Tools

Your current enabled tools are good:
- `localSearch`, `readNote`, `webSearch`, `youtubeTranscription`, `writeFile`, `editFile`, `updateMemory`, `pomodoro`

Consider increasing `autonomousAgentMaxIterations` from 4 to 6 for complex cross-client queries that need to read multiple files.

---

## Part 3: Practical Usage for TFM

### High-Value Smart Connections Use Cases

**When editing a client file,** glance at the Smart Connections sidebar. It will show:
- Other clients with similar verticals/challenges
- Research docs relevant to the client's niche
- Creative framework sections that apply

**Best demonstration queries for Smart Lookup:**
1. "B2B newsletter creative angles that reduced CPL" — Should surface Insight Links, WorkWeek, Vendry winning patterns
2. "Static ad formats that outperform video" — Surfaces cross-client creative signals
3. "Client onboarding risks and red flags" — Surfaces negative triggers across clients
4. "Points and travel subscriber acquisition" — Links TPG and Points Path patterns
5. "Finance newsletter compliance language" — Surfaces MarketBeat, Stocks & Income NEVER rules

### High-Value Copilot Plus Use Cases

**Cross-client pattern discovery:**
- "Which clients have the lowest CPL and what do their winning creatives have in common?"
- "Compare the NEVER rules across all finance clients"
- "What creative formats work for clients with CPL targets under $3?"
- "Summarize all relationship health risks across the portfolio"

**Pre-meeting prep:**
- "Give me a briefing for the WorkWeek bi-weekly call" (will pull from client file + recent session logs)
- "What changed for MarketBeat since the last call?"

**Creative QA support:**
- "Does this ad copy violate any NEVER rules for [client]?" (paste copy into chat)
- "What headlines have worked for similar newsletters?"

### Plugin Integration

**With Dataview:** Smart Connections and Dataview don't directly integrate, but they complement each other. Use Dataview for structured queries (tables of client status, KPIs) and Smart Connections/Copilot for semantic queries (finding patterns, similar strategies).

**With Templater:** When creating new client files from the `new-client` template, the new file will automatically get indexed by both Smart Connections and Copilot within minutes, immediately becoming part of the semantic search corpus.

---

## Part 4: Performance Optimization

### Vault Size: Not a Concern

144 files is trivially small for both plugins. Performance issues typically start at 5,000+ files. You will experience:
- Initial indexing: 30-60 seconds (local model) or 5-10 seconds (API model)
- Re-indexing after edits: near-instant (both plugins use incremental updates)
- Sidebar connection load time: under 1 second
- Copilot RAG retrieval: 2-5 seconds depending on model

### Embedding Storage

- **Smart Connections:** Stores embeddings in `.smart-env/multi/` as `.ajson` files. Already in `.gitignore`. Good — these are local-only and regenerate automatically.
- **Copilot:** Stores its vector index internally. The `enableIndexSync` setting is `true`, which keeps the index fresh.

### Re-indexing Strategy

- **Smart Connections:** Re-indexes automatically when files change. No manual intervention needed. If connections seem stale after a big batch of edits, use the "Force re-index" button in Smart Environment settings.
- **Copilot:** Set to "ON MODE SWITCH" for `indexVaultToVectorStore`. This means it re-indexes when you switch between modes. For a vault this small, you could change this to "ON STARTUP" to ensure fresh indexes every session. Find this in Copilot settings.

### Mobile Considerations

Copilot has `disableIndexOnMobile: true` (correct). Smart Connections supports mobile but indexing on mobile drains battery. If you use Obsidian on mobile, the existing indexes from desktop will work — just avoid triggering re-indexes on mobile.

---

## Part 5: Quick-Reference Settings Checklist

### Smart Connections (Smart Environment settings)

| Setting | Current | Change To |
|---------|---------|-----------|
| Embedding model | `bge-micro-v2` | `bge-base-en-v1.5` if available, or keep current |
| Folder exclusions | (empty) | `templates, copilot, scripts, dashboards` |
| File exclusions | `Untitled` | `Untitled, CLIENT-INTELLIGENCE-SUMMARY` |
| Show full path | `false` | `true` |
| Chat model | Ollama (broken) | Disable Smart Chat or switch to open_router |
| Results limit | 20 | Keep (or reduce to 12-15) |

### Copilot Plus

| Setting | Current | Change To |
|---------|---------|-----------|
| Embedding model | `copilot-plus-small` | `copilot-plus-large` |
| QA exclusions | `copilot` | `copilot, templates, dashboards, scripts` |
| Max source chunks | 30 | 50 |
| Reasoning effort | `low` | `medium` |
| System prompt | (empty) | Add TFM agency prompt (see 2G above) |
| Agent max iterations | 4 | 6 |
| Index vault | ON MODE SWITCH | ON STARTUP |
| Temperature | 0.1 | Keep |
| Context turns | 15 | Keep |

---

## Part 6: After Configuration

After making these changes:

1. **Restart Obsidian** to trigger re-indexing with new exclusions
2. **Test Smart Connections** by opening any client file and checking the sidebar — excluded folders should not appear
3. **Test Copilot** by asking: "What are the top 3 creative formats across our B2B clients?"
4. **Verify exclusions** by asking Copilot about template content — it should not retrieve template files
5. **Create the system prompt file** at `copilot/system-prompts/TFM Agency Assistant.md` and set it as default
