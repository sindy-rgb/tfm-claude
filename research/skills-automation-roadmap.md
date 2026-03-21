# TFM Skills & Automations Roadmap
**Generated:** 2026-03-21
**Sources:** Chase H AI, Simon Scrapes, czlonkowski/n8n-skills, GSD framework, Claude Code hooks docs

---

## Priority Matrix

| Priority | Skill | Impact | Effort | What It Solves |
|----------|-------|--------|--------|----------------|
| **P0** | `/friday-autopilot` | Highest | Medium | Friday reports 0% on-time across multiple accounts |
| **P0** | `/creative-qa` hook | High | Medium | No QA gate before creative goes to client |
| **P1** | `/fatigue-scan` | High | Simple | Creative fatigue detection is manual |
| **P1** | `/vault-integrity` | High | Simple | Frontmatter drift degrades all other skills |
| **P1** | `/action-tracker` | High | Medium | Action items lost between meetings |
| **P2** | `/lp-monitor` | Medium | Medium | Silent landing page CVR drops |
| **P2** | `/portfolio-pulse` | Medium | Medium | No single-glance portfolio view |
| **P2** | n8n Self-Healer | Medium | Complex | Cascading automation failures |
| **P3** | `/competitor-watch` | Medium | Complex | No automated competitor monitoring |
| **P3** | `/onboard-client` | Low urgency | Medium | New client setup takes hours |

---

## P0: Build Immediately

### 1. `/friday-autopilot` — Automated Friday Report Generator
**Trigger:** Every Friday at 8am EST via n8n, or manual `/friday-autopilot [client-slug]`

Replaces the manual Friday report process. N8n pulls Meta Ads data via Pipeboard for all accounts, calculates WoW changes, generates the markdown report, and posts a draft to each `#internal-[clientslug]` Slack channel. GM reviews and forwards to external channel.

The 13-node workflow design doc already exists at `research/n8n-friday-report-automation.md`. The blocker is building it with correct Meta API tokens and fixing spreadsheet ID placeholders.

**MCP tools:** Pipeboard (get_insights, get_campaigns, get_ads), Slack (send_message_draft), Google Drive (gsheets_update_cell)

### 2. `/creative-qa` — Pre-Send Creative QA Hook
**Trigger:** Claude Code hook (PreToolUse on Slack send_message) + manual `/creative-qa [client-slug]`

Before any creative is shared in a client Slack channel, this hook intercepts the message, reads the client's NEVER rules, checks copy against brand voice rules, verifies factual claims (subscriber counts, math), and either approves or blocks with specific violations.

Zero tokens consumed — runs as a shell script hook:
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "mcp__claude_ai_Slack__slack_send_message",
      "hooks": [{
        "type": "command",
        "command": ".claude/hooks/creative-qa-gate.sh"
      }]
    }]
  }
}
```

**MCP tools:** None at hook level (zero-token). Manual skill uses Google Drive, Notion, local vault files.

---

## P1: Build This Sprint

### 3. `/fatigue-scan` — Creative Fatigue Detection
**Trigger:** Weekly via loop or manual `/fatigue-scan [client-slug]`

Pulls 14 days of ad-level performance from Pipeboard. Compares each ad's CTR and CPL trajectory (days 1-7 vs 8-14). Flags ads showing: CTR declining >20% WoW, CPL increasing >15% WoW, frequency >3.0. Outputs a kill/scale/iterate list per client.

**MCP tools:** Pipeboard (get_insights with level=ad), Slack (send_message_draft)
**Complexity:** Simple — read-only data pull with comparison logic.

### 4. `/vault-integrity` — Client File Frontmatter Validator
**Trigger:** Claude Code hook on PostToolUse for Edit/Write on `clients/**/*.md`, plus weekly scheduled run

After any edit to a client file, validates YAML frontmatter has all required fields and values are consistent. Weekly run cross-references every file's `current_cpl` against the most recent Slack report.

Hook configuration:
```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit|Write",
      "hooks": [{
        "type": "command",
        "command": ".claude/hooks/validate-frontmatter.sh"
      }]
    }]
  }
}
```

**MCP tools:** None at hook level. Weekly scan uses Slack search.
**Complexity:** Simple — pattern matching on YAML fields.

### 5. `/action-tracker` — Meeting Action Item Tracker
**Trigger:** Auto after Day.ai meeting tools used, plus manual `/action-tracker [client-slug]`

Extracts action items with owners and deadlines from meeting recordings, writes to `clients/[slug]/action-items.md`, cross-references against previous meeting's items to flag overdue. Before each call, surfaces unresolved items.

**MCP tools:** Day.ai (search_objects, get_meeting_recording_context), Slack (search), local files
**Complexity:** Medium — tracking state across meetings requires persistence layer.

---

## P2: Build Next

### 6. `/lp-monitor` — Landing Page CVR Watchdog
Daily n8n workflow checks each client's landing page (HTTP 200, load time, screenshot). Claude Code skill pulls Pipeboard CVR data, compares against 40%+ benchmark, flags drops. How to AI's CVR crash (45% → 24%) would have been caught immediately.

**MCP tools:** Pipeboard (get_insights), Playwright (navigate, screenshot), Slack

### 7. `/portfolio-pulse` — Cross-Client Portfolio Dashboard
Daily performance snapshot across all 20 Pipeboard accounts. Calculates total spend, average CPL, clients above/below target. Detects cross-portfolio patterns: CPMs rising everywhere = platform trend, format winning across clients = transferable insight.

**MCP tools:** Pipeboard (get_insights batch), Slack, local file edit

### 8. n8n Self-Healing Workflow Monitor
From Simon Scrapes: when any n8n workflow fails, Error Trigger captures details → Claude-powered AI Agent node diagnoses (expired token, wrong sheet ID, rate limit) → auto-fixes or posts diagnostic to `#tfm-ops`.

Install `czlonkowski/n8n-skills` package for Claude Code to build/debug n8n workflows.

**Built entirely in n8n** — Error Trigger node, AI Agent node with Claude, Slack node.

---

## P3: Build When Ready

### 9. `/competitor-watch` — Competitor Creative Monitor
Uses Playwright to check Meta Ad Library for competitor domains, screenshots new ads, summarizes creative patterns. For in-account competitors (MarketBeat vs GrowJoy), pulls directly from Pipeboard.

### 10. `/onboard-client` — New Client Automation Pipeline
End-to-end new client setup: creates vault directory, intelligence file, config, Claude Chat instructions, deep enrichment skeleton, searches Day.ai/Slack/Notion for existing data, drafts Slack channel creation message, updates summary.

---

## Additional Recommendations

1. **Install `czlonkowski/n8n-skills`** — 7 skill directories that teach Claude Code to build/debug n8n workflows directly
2. **Add Claude Code hooks now** — even before full `/creative-qa`, a simple PreToolUse hook on Slack sends creates an audit trail at zero cost
3. **Borrow GSD context management** — fresh sub-agents for large tasks, persistent state files for cross-session continuity (don't need the full framework, just the philosophy)
