# The Feed Media — Client Intelligence System

## Architecture Overview

```
the-feed-media/
├── clients/              # One .md file per client — pre-rendered 6-category intelligence
├── prompts/              # Reusable prompts for analysis, Notion parsing, memory setup
├── system/               # Framework definitions, brand rules, workflow SOPs
└── scripts/              # Export/sync utilities
```

## How This Works

**Source of truth:** Day AI org context records (updated every Monday by the automated skill)  
**Local files:** Fast-access mirrors — no tool calls required at session start  
**Claude Code sessions:** Read from `/clients/` directly — full intelligence in context instantly  

## Workflow

1. **Analysis chat** (claude.ai) → pulls Day AI + Slack + Notion → writes to Day AI context
2. **Export step** → copy Day AI context into `/clients/[client].md`
3. **Work session** (Claude Code) → reads local `.md` files, zero fetch overhead
4. **Monday skill** updates Day AI → re-export to local files

## File Naming

All client files use kebab-case: `creator-spotlight.md`, `rnt-fitness.md`, `how-to-ai.md`

## Session Startup (Claude Code)

For single-client work:
```
Read /the-feed-media/clients/houck.md and /the-feed-media/system/framework.md before proceeding.
```

For cross-client work:
```
Read all files in /the-feed-media/clients/ and summarize the winning creative patterns across accounts.
```

## Last Updated
March 2026
