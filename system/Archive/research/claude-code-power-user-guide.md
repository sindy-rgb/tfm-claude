# Claude Code Power User Guide (2026)

> Compiled for Jay Warner -- Newsletter Growth Agency workflows
> Last updated: March 2026
> Sources: Official Anthropic documentation (code.claude.com), GitHub (claude-code repo, 80.3k stars), community resources, YouTube practitioners
> Target audience: Intermediate-to-advanced Claude Code users running agency workflows

---

## Table of Contents

1. [Core Architecture & Mental Model](#core-architecture--mental-model)
2. [Installation & Setup](#installation--setup)
3. [CLAUDE.md Mastery](#claudemd-mastery)
4. [Memory System Deep Dive](#memory-system-deep-dive)
5. [Skills & Custom Commands](#skills--custom-commands)
6. [Hooks: Deterministic Automation](#hooks-deterministic-automation)
7. [MCP Servers: Tool Integration](#mcp-servers-tool-integration)
8. [Subagents & Delegation](#subagents--delegation)
9. [Agent Teams: Parallel Orchestration](#agent-teams-parallel-orchestration)
10. [CLI Power Moves](#cli-power-moves)
11. [Prompt Engineering for Claude Code](#prompt-engineering-for-claude-code)
12. [Context Management Mastery](#context-management-mastery)
13. [Settings & Configuration Deep Dive](#settings--configuration-deep-dive)
14. [Permissions & Security](#permissions--security)
15. [Extended Thinking & Model Configuration](#extended-thinking--model-configuration)
16. [Best Practices & Anti-Patterns](#best-practices--anti-patterns)
17. [Multi-Client Agency Setup](#multi-client-agency-setup)
18. [Claude Code + Obsidian Workflow](#claude-code--obsidian-workflow)
19. [Claude Code + n8n Automation](#claude-code--n8n-automation)
20. [Data Analysis Workflows](#data-analysis-workflows)
21. [CI/CD & GitHub Actions Integration](#cicd--github-actions-integration)
22. [Debugging Workflows](#debugging-workflows)
23. [Testing Workflows](#testing-workflows)
24. [Git & PR Workflows](#git--pr-workflows)
25. [Worktrees for Parallel Development](#worktrees-for-parallel-development)
26. [Plugins & The Plugin Ecosystem](#plugins--the-plugin-ecosystem)
27. [Remote Control & Cross-Device Workflows](#remote-control--cross-device-workflows)
28. [Essential Community Tools & Resources](#essential-community-tools--resources)
29. [Claude Code vs Cursor vs Windsurf](#claude-code-vs-cursor-vs-windsurf)
30. [Real-World Practitioner Tips (from YouTube)](#real-world-practitioner-tips-from-youtube)
31. [Complete Environment Variable Reference](#complete-environment-variable-reference)
32. [Complete Keyboard Shortcut Reference](#complete-keyboard-shortcut-reference)
33. [Complete Slash Command Reference](#complete-slash-command-reference)
34. [Troubleshooting](#troubleshooting)
35. [Quick Reference Card](#quick-reference-card)

---

## Core Architecture & Mental Model

Claude Code is an **agentic coding environment** -- not a chatbot. It reads your codebase, edits files, runs commands, and autonomously works through problems. The key constraint to understand:

**Context window management is everything.** Claude's context fills up fast with every file read, every command output, every message. Performance degrades as context fills. Track this with a custom status line and manage it aggressively.

### How the Agentic Loop Works

1. You send a prompt
2. Claude reads files, runs commands, makes changes
3. It verifies its own work (if you give it verification criteria)
4. It repeats until the task is done

The loop is self-correcting when given proper verification. Without verification criteria, Claude produces plausible-looking output that may not actually work. **Giving Claude a way to verify its work is the single highest-leverage thing you can do.**

### The Fundamental Constraint: Context Window

Most best practices reduce to one constraint: Claude's context window fills up fast, and performance degrades as it fills. The context window holds your entire conversation, every file Claude reads, every command output. A single debugging session can consume tens of thousands of tokens.

This matters because:
- LLM performance degrades as context fills
- Claude may start "forgetting" earlier instructions
- Response quality drops as noise increases
- You pay for every token consumed

**Track context usage continuously.** Install a custom status line via `/statusline` or use a community plugin (ccstatusline, claude-powerline, claudia-statusline).

### Available Surfaces

| Surface | Best For | Key Features |
|---------|----------|-------------|
| **Terminal CLI** | Full power, scripting, CI/CD | All features, pipe support, non-interactive mode |
| **VS Code Extension** | Inline diffs, @-mentions, plan review | Extensions view, Cmd+Shift+P "Claude Code" |
| **Desktop App** | Visual diff review, multiple sessions | Download from claude.ai, parallel sessions |
| **Web (claude.ai/code)** | Long-running tasks, no local setup | Isolated VMs, mobile-accessible |
| **JetBrains Plugin** | IntelliJ/PyCharm/WebStorm users | Interactive diff viewing, selection context |
| **Chrome Extension** | Live web app debugging and UI testing | Screenshot capture, element interaction |
| **Slack Integration** | Route bug reports from Slack to PRs | @Claude mentions in channels |
| **iOS App** | Start/monitor tasks on the go | Pairs with web sessions |
| **Remote Control** | Control from phone or another device | `claude --remote-control` |

### How Sessions Work

Sessions are persistent, local, and reversible:
- Every action creates a checkpoint you can rewind to
- Sessions survive terminal closure and can be resumed
- Each session is tied to a project directory
- Sessions from the same git repo appear in the session picker

### The Unix Philosophy

Claude Code is composable. It follows the Unix philosophy: pipe data in, get structured data out, chain with other tools. This is what makes it fundamentally different from IDE-based AI assistants.

```bash
# Pipe logs into Claude
tail -200 app.log | claude -p "Slack me if you see any anomalies"

# Chain with other tools
git diff main --name-only | claude -p "review these changed files for security issues"

# Structured output for scripts
claude -p "List all API endpoints" --output-format json | jq '.endpoints[]'
```

---

## Installation & Setup

### Install (macOS/Linux)

```bash
# Native install (recommended -- auto-updates in background)
curl -fsSL https://claude.ai/install.sh | bash

# Homebrew (manual updates required)
brew install --cask claude-code

# Check version
claude --version

# Update manually if needed
claude update
# Or for Homebrew:
brew upgrade claude-code
```

### Install (Windows)

```powershell
# PowerShell
irm https://claude.ai/install.ps1 | iex

# WinGet
winget install Anthropic.ClaudeCode

# CMD
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

**Windows requires Git for Windows.** Install it first if you don't have it.

### Install (VS Code / Cursor)

```
# Install via Extensions view (Cmd+Shift+X)
Search "Claude Code" by Anthropic

# Or install directly
vscode:extension/anthropic.claude-code
cursor:extension/anthropic.claude-code
```

After installing, open Command Palette (Cmd+Shift+P), type "Claude Code", select **Open in New Tab**.

### Requirements

- **Node.js 18+** (for npm-based installations)
- **Git** (recommended for worktrees, diffs, PRs)
- **Claude subscription** or **Anthropic Console** account (for API billing)

### First Run

```bash
cd your-project
claude
# Follow login prompts on first use

# Login options
claude auth login                    # Default (Claude.ai subscription)
claude auth login --console          # API usage billing (Anthropic Console)
claude auth login --email me@co.com  # Pre-fill email
claude auth login --sso              # Force SSO authentication

# Check auth status
claude auth status
claude auth status --text            # Human-readable output
```

### Essential First Steps

```bash
# 1. Generate a starter CLAUDE.md from your codebase
/init

# Or use the interactive multi-phase flow (recommended for new projects)
CLAUDE_CODE_NEW_INIT=true claude
/init
# This asks which artifacts to set up: CLAUDE.md files, skills, hooks
# Explores codebase with a subagent, asks follow-up questions
# Presents reviewable proposal before writing any files

# 2. Configure permissions to reduce prompting fatigue
/permissions
# Add: npm test, npm run lint, git commit, git push, gh pr create

# 3. Install a status line to monitor context usage
/statusline

# 4. Set your preferred model and effort level
/model
/effort
```

### Configure Permissions Early

Use `/permissions` to allowlist safe commands. This is critical for reducing permission fatigue during long sessions:

```json
// .claude/settings.json or ~/.claude/settings.json
{
  "permissions": {
    "allow": [
      "Bash(npm run lint)",
      "Bash(npm run test *)",
      "Bash(npm run dev)",
      "Bash(git status)",
      "Bash(git log *)",
      "Bash(git diff *)",
      "Bash(git commit *)",
      "Bash(git push *)",
      "Bash(git branch *)",
      "Bash(gh pr *)",
      "Bash(gh issue *)",
      "Read(~/.zshrc)"
    ],
    "deny": [
      "Bash(curl *)",
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)"
    ]
  }
}
```

### Permission Rule Syntax

| Pattern | Matches |
|---------|---------|
| `Bash(npm test)` | Exact command |
| `Bash(npm run *)` | Any npm run subcommand |
| `Bash(git *)` | All git commands |
| `Read(~/.zshrc)` | Specific file |
| `Read(./.env.*)` | Glob pattern |
| `Agent(Explore)` | Specific subagent |
| `Skill(deploy *)` | Skill with prefix match |

---

## CLAUDE.md Mastery

CLAUDE.md is the single most important file for Claude Code effectiveness. It's loaded into context every session as a user message (not system prompt). Here's how to make it exceptional.

### File Locations & Precedence (highest to lowest)

| Scope | Location | Purpose | Shared? |
|-------|----------|---------|---------|
| **Managed Policy** | macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md` | Org-wide standards (cannot be excluded) | Yes (IT deployed) |
| | Linux/WSL: `/etc/claude-code/CLAUDE.md` | | |
| | Windows: `C:\Program Files\ClaudeCode\CLAUDE.md` | | |
| **Project** | `./CLAUDE.md` or `./.claude/CLAUDE.md` | Team-shared instructions | Yes (git) |
| **User** | `~/.claude/CLAUDE.md` | Personal preferences | No |

**Loading behavior:**
- Files in the directory hierarchy above the working directory load at launch
- Files in subdirectories load on demand when Claude reads files in those directories
- In monorepos, use `claudeMdExcludes` in settings to skip irrelevant CLAUDE.md files

### Writing Effective Instructions

**Size**: Target under 200 lines per CLAUDE.md file. Longer files consume more context and reduce adherence. If growing large, split using imports or `.claude/rules/`.

**Structure**: Use markdown headers and bullets. Claude scans structure the same way readers do.

**Specificity**: Write instructions concrete enough to verify:
- "Use 2-space indentation" (not "Format code properly")
- "Run `npm test` before committing" (not "Test your changes")
- "API handlers live in `src/api/handlers/`" (not "Keep files organized")

**Emphasis for critical rules**: Add "IMPORTANT" or "YOU MUST" to boost adherence on rules that matter most.

**Consistency**: If two rules contradict each other, Claude picks one arbitrarily. Review periodically to remove conflicts.

**Pruning test**: For each line, ask: "Would removing this cause Claude to make mistakes?" If not, cut it. Bloated CLAUDE.md files cause Claude to ignore your actual instructions.

### Example CLAUDE.md for a Newsletter Growth Agency

```markdown
# The Feed Media - Claude Code Instructions

## Build & Test
- `npm run dev` to start local server
- `npm test` to run test suite
- `npm run lint` to check code quality
- Always run tests before committing

## Code Style
- Use ES modules (import/export), not CommonJS (require)
- Destructure imports when possible
- TypeScript strict mode -- no `any` types
- 2-space indentation, single quotes

## Git Workflow
- Branch naming: `feature/CLIENT-description` or `fix/CLIENT-description`
- Commit messages: conventional commits (feat:, fix:, chore:)
- Always create PRs, never push directly to main
- PR descriptions must include context and testing notes

## Project Architecture
- `/src/clients/` -- client-specific configurations
- `/src/templates/` -- email/newsletter templates
- `/src/analytics/` -- tracking and reporting modules
- `/src/automations/` -- n8n workflow definitions

## Client Work
- IMPORTANT: Never mix client data between projects
- Each client has isolated config in /src/clients/{client-name}/
- Check client-specific CLAUDE.md in subdirectories for overrides

## Preferences
- Prefer existing patterns in the codebase over introducing new ones
- When debugging, trace the full path before making changes
- Always explain architectural decisions in PR descriptions
```

### Import Syntax

Pull in additional context without bloating your main CLAUDE.md. Imports are expanded and loaded into context at launch alongside the CLAUDE.md that references them.

```markdown
See @README.md for project overview
See @package.json for available npm commands
Git workflow: @docs/git-instructions.md
Personal overrides: @~/.claude/my-project-instructions.md
```

**Key details:**
- Both relative and absolute paths allowed
- Relative paths resolve relative to the file containing the import
- Imported files can recursively import (max depth: 5 hops)
- First encounter of external imports triggers an approval dialog
- Imports survive `/compact` (they're re-read from disk)

### Organized Rules with `.claude/rules/`

For larger projects, split instructions into modular files. Rules without `paths` frontmatter load at launch. Path-scoped rules load when Claude works with matching files.

```
.claude/
  CLAUDE.md              # Main instructions (keep concise)
  rules/
    code-style.md        # Code formatting rules
    testing.md           # Testing conventions
    security.md          # Security requirements
    client-onboarding.md # Client setup procedures
    frontend/
      react-patterns.md  # React-specific rules
    backend/
      api-design.md      # API conventions
```

#### Path-Specific Rules

Scope rules to specific file types so they only load when relevant:

```markdown
---
paths:
  - "src/api/**/*.ts"
---

# API Development Rules
- All API endpoints must include input validation
- Use the standard error response format
- Include OpenAPI documentation comments
```

**Glob pattern reference:**

| Pattern | Matches |
|---------|---------|
| `**/*.ts` | All TypeScript files in any directory |
| `src/**/*` | All files under src/ |
| `*.md` | Markdown files in the project root |
| `src/components/*.tsx` | React components in a specific directory |
| `src/**/*.{ts,tsx}` | TypeScript and TSX files under src/ |

#### User-Level Rules

Personal rules in `~/.claude/rules/` apply to every project:

```
~/.claude/rules/
  preferences.md    # Your personal coding preferences
  workflows.md      # Your preferred workflows
```

User-level rules load before project rules, giving project rules higher priority.

### Symlink Shared Rules Across Projects

```bash
# Share agency-wide rules across all client projects
ln -s ~/agency-claude-rules .claude/rules/shared

# Share a single file
ln -s ~/company-standards/security.md .claude/rules/security.md
```

Symlinks are resolved and loaded normally. Circular symlinks are detected and handled gracefully.

### Exclude CLAUDE.md Files in Monorepos

```json
// .claude/settings.local.json
{
  "claudeMdExcludes": [
    "**/monorepo/CLAUDE.md",
    "/home/user/monorepo/other-team/.claude/rules/**"
  ]
}
```

Patterns match against absolute file paths using glob syntax. Managed policy CLAUDE.md files cannot be excluded.

### Loading CLAUDE.md from Additional Directories

```bash
# --add-dir gives Claude access but doesn't load CLAUDE.md by default
claude --add-dir ../shared-config

# To also load CLAUDE.md from additional directories:
CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1 claude --add-dir ../shared-config
```

---

## Memory System Deep Dive

Claude Code has two complementary memory systems. Both are loaded at the start of every conversation.

| | CLAUDE.md Files | Auto Memory |
|--|-----------------|-------------|
| **Who writes it** | You | Claude |
| **What it contains** | Instructions and rules | Learnings and patterns |
| **Scope** | Project, user, or org | Per working tree |
| **Loaded into** | Every session (full file) | Every session (first 200 lines of MEMORY.md) |
| **Survives /compact** | Yes (re-read from disk) | Yes (separate files) |
| **Use for** | Coding standards, workflows, architecture | Build commands, debugging insights, discovered preferences |

### 1. CLAUDE.md Files (You Write)

- Instructions, rules, and standards
- Loaded every session in full
- Shared via version control
- Treated as context, not enforced configuration
- More specific and concise = more consistent adherence

### 2. Auto Memory (Claude Writes)

Auto memory lets Claude accumulate knowledge across sessions without you writing anything. Claude saves notes for itself: build commands, debugging insights, architecture notes, code style preferences, workflow habits. Claude decides what's worth remembering based on whether the information would be useful in a future conversation.

**Requirements:** Claude Code v2.1.59 or later.

### Storage Location

Each project gets its own memory directory at `~/.claude/projects/<project>/memory/`. The `<project>` path derives from the git repository, so **all worktrees and subdirectories within the same repo share one auto memory directory**. Outside a git repo, the project root is used instead.

```
~/.claude/projects/<project>/memory/
  MEMORY.md              # Concise index, loaded every session (first 200 lines)
  debugging.md           # Detailed debugging patterns
  api-conventions.md     # API design decisions
  client-preferences.md  # Client-specific preferences
  ...                    # Any other topic files Claude creates
```

### How Auto Memory Works

1. First 200 lines of `MEMORY.md` are loaded at session start
2. Content beyond line 200 is NOT loaded at session start
3. Claude keeps `MEMORY.md` concise by moving detailed notes into separate topic files
4. Topic files are read on demand when Claude needs the information
5. Auto memory is machine-local; not shared across machines

### Managing Auto Memory

```bash
# View and edit memory files
/memory

# Toggle auto memory on/off
/memory  # Then use the auto memory toggle

# Or disable via settings
# In .claude/settings.json:
{
  "autoMemoryEnabled": false
}

# Or via environment variable
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1

# Custom memory directory (user or local settings only, not project settings)
{
  "autoMemoryDirectory": "~/my-custom-memory-dir"
}
```

### Pro Tips for Memory

- Tell Claude to "remember this" and it saves to auto memory
- Tell Claude to "add this to CLAUDE.md" for persistent instructions
- Run `/memory` to audit what Claude has stored
- CLAUDE.md fully survives `/compact` -- instructions given only in conversation do not
- After `/compact`, Claude re-reads CLAUDE.md from disk and re-injects it fresh
- If an instruction disappeared after compaction, it was conversation-only, not in CLAUDE.md
- Subagents can maintain their own persistent memory (see Subagents section)

---

## Skills & Custom Commands

Skills extend Claude's capabilities with reusable workflows. They load on demand (not every session), preserving context. Skills follow the [Agent Skills](https://agentskills.io) open standard.

**Note:** Custom commands (`.claude/commands/`) have been merged into skills. A file at `.claude/commands/deploy.md` and a skill at `.claude/skills/deploy/SKILL.md` both create `/deploy` and work the same way. Existing command files keep working, but skills are recommended.

### Creating a Skill

Every skill needs a directory with a `SKILL.md` entrypoint:

```bash
mkdir -p .claude/skills/newsletter-deploy
```

Create `.claude/skills/newsletter-deploy/SKILL.md`:

```yaml
---
name: newsletter-deploy
description: Deploy newsletter campaign for a client
disable-model-invocation: true
---

Deploy the newsletter campaign for $ARGUMENTS:

1. Verify all template variables are populated
2. Run `npm run validate:email -- --client $ARGUMENTS`
3. Check that tracking pixels are in place
4. Run preview in Litmus/Email on Acid
5. Deploy via the client's ESP API
6. Verify delivery and log results
```

Invoke with: `/newsletter-deploy acme-corp`

### Skill Locations

| Location | Path | Scope | Priority |
|----------|------|-------|----------|
| Enterprise | See managed settings | All users in org | Highest |
| Personal | `~/.claude/skills/<name>/SKILL.md` | All your projects | High |
| Project | `.claude/skills/<name>/SKILL.md` | This project only | Medium |
| Plugin | `<plugin>/skills/<name>/SKILL.md` | Where plugin enabled | Lowest |

When skills share the same name, higher-priority locations win. Plugin skills use `plugin-name:skill-name` namespace (no conflicts).

### Frontmatter Reference

| Field | Required | Description |
|-------|----------|-------------|
| `name` | No | Display name / slash command. Default: directory name. Lowercase, hyphens, max 64 chars |
| `description` | Recommended | What the skill does. Claude uses this for automatic invocation decisions |
| `argument-hint` | No | Hint for autocomplete, e.g., `[issue-number]` |
| `disable-model-invocation` | No | `true` = manual-only (for side effects like deploy). Default: false |
| `user-invocable` | No | `false` = hidden from `/` menu (background knowledge only). Default: true |
| `allowed-tools` | No | Tools Claude can use without permission when skill is active |
| `model` | No | Override model when skill is active |
| `context` | No | `fork` = run in isolated subagent context |
| `agent` | No | Which subagent to use when `context: fork` (e.g., `Explore`, `Plan`, custom) |
| `hooks` | No | Hooks scoped to this skill's lifecycle |

### Invocation Control

| Frontmatter | You can invoke | Claude can invoke | When loaded |
|-------------|---------------|-------------------|-------------|
| (default) | Yes | Yes | Description always in context |
| `disable-model-invocation: true` | Yes | No | Description NOT in context |
| `user-invocable: false` | No | Yes | Description always in context |

### String Substitutions

| Variable | Description |
|----------|-------------|
| `$ARGUMENTS` | All arguments passed when invoking |
| `$ARGUMENTS[N]` or `$N` | Specific argument by 0-based index |
| `${CLAUDE_SESSION_ID}` | Current session ID |
| `${CLAUDE_SKILL_DIR}` | Directory containing the SKILL.md |

**Example with indexed arguments:**
```yaml
---
name: migrate-component
description: Migrate a component from one framework to another
---

Migrate the $0 component from $1 to $2.
Preserve all existing behavior and tests.
```

Running `/migrate-component SearchBar React Vue` replaces `$0` with SearchBar, `$1` with React, `$2` with Vue.

### Bundled Skills (Built-In)

| Skill | Purpose |
|-------|---------|
| `/batch <instruction>` | Large-scale parallel changes. Researches codebase, decomposes into 5-30 units, spawns one background agent per unit in isolated worktrees. Each implements, tests, opens a PR. Requires git. |
| `/claude-api` | Load Claude API reference for your language (Python, TS, Java, Go, Ruby, C#, PHP, cURL). Auto-activates when importing `anthropic` or `@anthropic-ai/sdk` |
| `/debug [description]` | Troubleshoot current session by reading debug log |
| `/loop [interval] <prompt>` | Run a prompt repeatedly. E.g., `/loop 5m check if the deploy finished` |
| `/simplify [focus]` | Review recent changes for code reuse, quality, efficiency. Spawns 3 review agents in parallel, aggregates, applies fixes |

### Dynamic Context Injection

Use `!`command`` to run shell commands before skill content reaches Claude:

```yaml
---
name: pr-summary
description: Summarize changes in a pull request
context: fork
agent: Explore
allowed-tools: Bash(gh *)
---

## Pull request context
- PR diff: !`gh pr diff`
- PR comments: !`gh pr view --comments`
- Changed files: !`gh pr diff --name-only`

## Your task
Summarize this pull request...
```

When this skill runs:
1. Each `!`command`` executes immediately (before Claude sees anything)
2. Output replaces the placeholder
3. Claude receives fully-rendered prompt with actual data

### Running Skills in Subagents

Add `context: fork` to run in isolation. The skill content becomes the prompt driving the subagent:

```yaml
---
name: deep-research
description: Research a topic thoroughly
context: fork
agent: Explore
---

Research $ARGUMENTS thoroughly:
1. Find relevant files using Glob and Grep
2. Read and analyze the code
3. Summarize findings with specific file references
```

### Supporting Files

Skills can include multiple files in their directory:

```
my-skill/
  SKILL.md           # Main instructions (required, keep under 500 lines)
  template.md        # Template for Claude to fill in
  examples/
    sample.md        # Example output
  scripts/
    validate.sh      # Script Claude can execute
    visualize.py     # Python script for visual output
```

Reference them from SKILL.md:
```markdown
## Additional resources
- For complete API details, see [reference.md](reference.md)
- For usage examples, see [examples.md](examples.md)
```

### Visual Output from Skills

Skills can generate interactive HTML files that open in your browser:

```yaml
---
name: codebase-visualizer
description: Generate interactive collapsible tree visualization of your codebase
allowed-tools: Bash(python *)
---

Run the visualization script from your project root:
python ~/.claude/skills/codebase-visualizer/scripts/visualize.py .
```

This pattern works for dependency graphs, test coverage reports, API documentation, database schema visualizations, and more.

### Restricting Claude's Skill Access

```bash
# Via /permissions - deny all skills
Skill

# Allow specific skills only
Skill(commit)
Skill(review-pr *)

# Deny specific skills
Skill(deploy *)
```

### Skills vs Other Approaches

| Tool | Best For | Context Cost |
|------|----------|-------------|
| **Skills** | Reusable procedural knowledge, loaded on demand | Low (on-demand) |
| **CLAUDE.md** | Always-on context, coding standards | High (every session) |
| **Subagents** | Independent task execution in isolation | None (separate context) |
| **MCP** | External data/API integration | Varies |
| **Hooks** | Deterministic automation on every action | None (shell scripts) |

---

## Hooks: Deterministic Automation

Hooks are user-defined shell commands, HTTP endpoints, LLM prompts, or agents that execute automatically at specific lifecycle points. Unlike CLAUDE.md (advisory), hooks are **deterministic and guaranteed**.

**Claude can write hooks for you.** Try prompts like "Write a hook that runs eslint after every file edit" or "Write a hook that blocks writes to the migrations folder."

### Hook Types

| Type | Mechanism | When to Use |
|------|-----------|-------------|
| `command` | Execute shell scripts. Receive event JSON on stdin. | Most hooks. Format, validate, log, block. |
| `http` | Send POST request to URL. Supports headers and env var interpolation. | External services, webhooks, logging APIs. |
| `prompt` | Ask Claude for yes/no decisions. `$ARGUMENTS` placeholder for hook input. | Context-dependent approval/denial. |
| `agent` | Spawn subagent with tool access (Read, Grep, Glob). | Complex verification before action. |

### Hook Configuration Format

```json
{
  "type": "command",
  "command": ".claude/hooks/validate.sh",
  "timeout": 600,
  "async": false,
  "statusMessage": "Validating..."
}
```

```json
{
  "type": "http",
  "url": "http://localhost:8080/hooks/pre-tool-use",
  "headers": {
    "Authorization": "Bearer $MY_TOKEN"
  },
  "allowedEnvVars": ["MY_TOKEN"],
  "timeout": 30
}
```

```json
{
  "type": "prompt",
  "prompt": "Is this database operation safe? $ARGUMENTS",
  "model": "fast-model",
  "timeout": 30
}
```

```json
{
  "type": "agent",
  "prompt": "Verify that all tests pass before approving",
  "timeout": 60
}
```

### Configuration Locations

| Location | Scope | Shareable |
|----------|-------|-----------|
| `~/.claude/settings.json` | All projects | No |
| `.claude/settings.json` | Single project | Yes (git) |
| `.claude/settings.local.json` | Single project | No (gitignored) |
| Managed policy | Organization-wide | Yes |
| Plugin `hooks/hooks.json` | When plugin enabled | Yes |
| Skill/agent frontmatter | Component active | Yes |

### Complete Hook Events Reference

#### Session Events

| Event | When | Matchers | Can Block? |
|-------|------|----------|------------|
| `SessionStart` | Session begins/resumes | `startup`, `resume`, `clear`, `compact` | No (add context) |
| `SessionEnd` | Session terminates | `clear`, `resume`, `logout`, `prompt_input_exit`, etc. | No (cleanup only) |
| `InstructionsLoaded` | CLAUDE.md or rule loaded | `session_start`, `nested_traversal`, `path_glob_match`, `include`, `compact` | No (observability) |

#### User Input Events

| Event | When | Matchers | Can Block? |
|-------|------|----------|------------|
| `UserPromptSubmit` | Before Claude processes prompt | None (always fires) | Yes (`decision: "block"`) |

#### Tool Events

| Event | When | Matchers | Can Block? |
|-------|------|----------|------------|
| `PreToolUse` | Before tool execution | Tool name (`Bash`, `Edit`, `Write`, `Read`, etc.) | Yes (deny/allow/ask) |
| `PostToolUse` | After successful tool execution | Tool name | No (tool already ran) |
| `PostToolUseFailure` | After tool fails | Tool name | No (add context only) |
| `PermissionRequest` | Permission dialog shown | Tool name | Yes (allow/deny) |

#### Agent Events

| Event | When | Matchers | Can Block? |
|-------|------|----------|------------|
| `SubagentStart` | Subagent spawned | Agent type name | No (add context) |
| `SubagentStop` | Subagent finishes | Agent type name | Yes (prevent stopping) |
| `Stop` | Main Claude finishes responding | None (always fires) | Yes (`decision: "block"`) |
| `StopFailure` | Turn ends due to API error | Error type | No (logging only) |

#### Team Events

| Event | When | Matchers | Can Block? |
|-------|------|----------|------------|
| `TeammateIdle` | Agent team teammate about to idle | None | Yes (continue with feedback) |
| `TaskCompleted` | Task marked complete | None | Yes (reject completion) |

#### Configuration & Context Events

| Event | When | Matchers | Can Block? |
|-------|------|----------|------------|
| `ConfigChange` | Settings file changes during session | `user_settings`, `project_settings`, etc. | Yes (except policy) |
| `PreCompact` | Before compaction starts | `manual`, `auto` | No |
| `PostCompact` | After compaction completes | `manual`, `auto` | No |
| `Notification` | Notification sent | `permission_prompt`, `idle_prompt`, `auth_success`, `elicitation_dialog` | No |

#### Worktree Events

| Event | When | Can Block? |
|-------|------|------------|
| `WorktreeCreate` | `--worktree` or subagent with `isolation: "worktree"` | Yes |
| `WorktreeRemove` | Worktree being removed | No |

#### MCP Events

| Event | When | Can Block? |
|-------|------|------------|
| `Elicitation` | MCP server requests user input | Yes (accept/decline/cancel) |
| `ElicitationResult` | User responds to MCP elicitation | Yes (override response) |

### Exit Code Behavior

| Exit Code | Behavior |
|-----------|----------|
| **0** | Success. Parse stdout for JSON output |
| **2** | Blocking error. Stderr = error message. Effect depends on event type |
| **Other** | Non-blocking error. Stderr shown in verbose mode only |

### Common Input Fields (All Hooks Receive)

```json
{
  "session_id": "abc123",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/working/directory",
  "permission_mode": "default|plan|acceptEdits|dontAsk|bypassPermissions",
  "hook_event_name": "EventName",
  "agent_id": "optional-subagent-id",
  "agent_type": "optional-agent-name"
}
```

### Environment Variables Available in Hooks

```bash
$CLAUDE_PROJECT_DIR    # Project root
${CLAUDE_PLUGIN_ROOT}  # Plugin directory
${CLAUDE_PLUGIN_DATA}  # Plugin persistent data
$CLAUDE_ENV_FILE       # SessionStart only -- persist env vars
$CLAUDE_CODE_REMOTE    # "true" in web, unset locally
```

### Essential Hook: Desktop Notifications

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "osascript -e 'display notification \"Claude Code needs your attention\" with title \"Claude Code\"'"
          }
        ]
      }
    ]
  }
}
```

**Linux variant:**
```json
{
  "type": "command",
  "command": "notify-send 'Claude Code' 'Claude Code needs your attention'"
}
```

**Narrow the matcher:**
- `permission_prompt` -- Claude needs tool approval
- `idle_prompt` -- Claude done, waiting for next prompt
- `auth_success` -- Authentication completes
- `elicitation_dialog` -- Claude asking a question

### Essential Hook: Auto-Format After File Edits

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "npx prettier --write \"$(echo $TOOL_INPUT | jq -r '.file_path')\"",
            "async": true
          }
        ]
      }
    ]
  }
}
```

### Essential Hook: Block Dangerous Commands

```bash
#!/bin/bash
# .claude/hooks/block-destructive.sh
COMMAND=$(jq -r '.tool_input.command' < /dev/stdin)

if echo "$COMMAND" | grep -qE '(rm -rf|drop database|git push.*--force|:(){:|fork)'; then
  jq -n '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: "Destructive command blocked"
    }
  }'
  exit 0
fi
exit 0
```

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/block-destructive.sh"
          }
        ]
      }
    ]
  }
}
```

### Essential Hook: Auto-Approve Safe Commands

```bash
#!/bin/bash
# .claude/hooks/auto-approve.sh
COMMAND=$(jq -r '.tool_input.command')

if echo "$COMMAND" | grep -qE '^(npm test|npm run lint|git status|git log|git diff)'; then
  jq -n '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "allow",
      permissionDecisionReason: "Safe build/read command"
    }
  }'
else
  exit 0
fi
```

### Essential Hook: Audit Logging

```bash
#!/bin/bash
# .claude/hooks/audit-tools.sh
jq -r '.tool_name + ": " + (.tool_input.command // .tool_input.file_path // "")' \
  >> ~/.claude/tool-audit.log
exit 0
```

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/audit-tools.sh",
            "async": true
          }
        ]
      }
    ]
  }
}
```

### Essential Hook: Persist Session Environment (SessionStart)

```bash
#!/bin/bash
# Load NVM and set Node version for all Claude Code sessions
if [ -n "$CLAUDE_ENV_FILE" ]; then
  source ~/.nvm/nvm.sh
  nvm use 20
  export -p >> "$CLAUDE_ENV_FILE"
fi
exit 0
```

### Essential Hook: Force Tests on Stop

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/verify-tests.sh"
          }
        ]
      }
    ]
  }
}
```

```bash
#!/bin/bash
# .claude/hooks/verify-tests.sh
if ! npm test 2>&1; then
  echo '{"decision": "block", "reason": "Tests failing. Fix before stopping."}'
  exit 0
fi
exit 0
```

### MCP Tool Matching in Hooks

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__memory__.*",
        "hooks": [{ "type": "command", "command": "log-mcp.sh" }]
      },
      {
        "matcher": "mcp__.*__write.*",
        "hooks": [{ "type": "command", "command": "validate-write.sh" }]
      }
    ]
  }
}
```

### Viewing Configured Hooks

Type `/hooks` in Claude Code to open a read-only browser showing all hook events with counts, matcher details, handler configs, and source locations.

### Disabling Hooks

```json
{
  "disableAllHooks": true
}
```

Note: Cannot disable managed policy hooks at user/project level.

---

## MCP Servers: Tool Integration

MCP (Model Context Protocol) is an open standard for connecting AI tools to external data sources. With MCP, Claude Code can read design docs in Google Drive, update tickets in Jira, pull data from Slack, query databases, or use your own custom tooling.

### Adding MCP Servers

```bash
# Add via CLI
claude mcp add <server-name> -- <command> [args...]

# Add with transport type
claude mcp add <server-name> --transport http <url>
claude mcp add <server-name> --transport sse <url>
claude mcp add <server-name> --transport stdio -- <command> [args...]

# Add with environment variables
claude mcp add <server-name> --env API_KEY=your_key -- npx -y @some/mcp-server

# List configured servers
claude mcp list

# Remove a server
claude mcp remove <server-name>
```

### MCP Configuration File (.mcp.json)

Create `.mcp.json` in your project root for project-scoped servers:

```json
{
  "mcpServers": {
    "github": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-github"]
    },
    "slack": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-slack"]
    },
    "notion": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-notion"]
    },
    "playwright": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    }
  }
}
```

### Transport Types

| Type | Use Case | Format |
|------|----------|--------|
| `stdio` | Local process communication | `command` + `args` |
| `http` | Remote HTTP server (streamable) | `url` |
| `sse` | Server-sent events | `url` |
| `ws` | WebSocket | `url` |

### MCP Configuration Scopes

| Scope | Location | Purpose |
|-------|----------|---------|
| User | `~/.claude.json` | Personal MCP servers across all projects |
| Project | `.mcp.json` | Team-shared servers for this project |
| Local | `~/.claude.json` (per-project section) | Personal overrides for this project |
| Managed | `/Library/Application Support/ClaudeCode/managed-mcp.json` | Org-wide servers |
| CLI | `--mcp-config ./custom-mcp.json` | Session-specific |
| Strict | `--strict-mcp-config --mcp-config ./mcp.json` | Only these servers, ignore all others |

### Approving Project MCP Servers

When Claude encounters project `.mcp.json` servers, it asks for approval. To auto-approve:

```json
// .claude/settings.json or ~/.claude/settings.json
{
  "enableAllProjectMcpServers": true
}

// Or approve specific servers only
{
  "enabledMcpjsonServers": ["memory", "github"],
  "disabledMcpjsonServers": ["filesystem"]
}
```

### Best MCP Servers for a Newsletter Growth Agency

| Server | Purpose | Install Command |
|--------|---------|----------------|
| **GitHub** | PR management, issue tracking, code review | `claude mcp add github -- npx -y @anthropic-ai/mcp-github` |
| **Slack** | Team communication, client notifications | `claude mcp add slack -- npx -y @anthropic-ai/mcp-slack` |
| **Notion** | Client wikis, content calendars, project tracking | `claude mcp add notion -- npx -y @anthropic-ai/mcp-notion` |
| **Google Drive** | Shared docs, design assets, client briefs | `claude mcp add google-drive -- npx -y @anthropic-ai/mcp-google-drive` |
| **Google Calendar** | Meeting scheduling, deadline tracking | Available via MCP registry |
| **Gmail** | Email drafts, client communication | Available via MCP registry |
| **Playwright** | Browser automation, email preview testing | `claude mcp add playwright -- npx -y @playwright/mcp@latest` |
| **PostgreSQL** | Database queries for analytics | `claude mcp add postgres -- npx -y @anthropic-ai/mcp-postgres` |
| **Sentry** | Error monitoring and debugging | Available via MCP registry |
| **Linear/Jira** | Project management, sprint tracking | Available via MCP registry |
| **Figma** | Design handoff, template review | Available via MCP registry |

### Using MCP Resources in Prompts

```
Show me the data from @github:repos/owner/repo/issues
```

### Scope MCP to Subagents

Give specific subagents access to MCP servers without loading them into the main conversation:

```yaml
---
name: browser-tester
description: Tests features in a real browser using Playwright
mcpServers:
  # Inline definition: scoped to this subagent only
  - playwright:
      type: stdio
      command: npx
      args: ["-y", "@playwright/mcp@latest"]
  # Reference by name: reuses an already-configured server
  - github
---

Use the Playwright tools to navigate, screenshot, and interact with pages.
```

Inline definitions keep the MCP server out of the main conversation entirely, avoiding tool descriptions consuming context there.

### Managed MCP Configuration (Enterprise)

```json
// /Library/Application Support/ClaudeCode/managed-mcp.json (macOS)
{
  "mcpServers": {
    "company-tools": {
      "type": "http",
      "url": "https://mcp.company.com/tools"
    }
  }
}
```

```json
// managed-settings.json
{
  "allowManagedMcpServersOnly": true,
  "allowedMcpServers": [{ "serverName": "github" }],
  "deniedMcpServers": [{ "serverName": "filesystem" }]
}
```

---

## Subagents & Delegation

Subagents are specialized AI assistants that handle specific tasks. Each runs in its own context window with a custom system prompt, specific tool access, and independent permissions. This keeps your main conversation clean.

### Built-In Subagents

| Agent | Model | Tools | Purpose |
|-------|-------|-------|---------|
| **Explore** | Haiku (fast) | Read-only | Codebase search and analysis. Thoroughness: quick/medium/very thorough |
| **Plan** | Inherited | Read-only | Research for plan mode |
| **General-purpose** | Inherited | All | Complex multi-step tasks |
| **Bash** | Inherited | Terminal | Running commands in separate context |
| **statusline-setup** | Sonnet | - | When you run `/statusline` |
| **Claude Code Guide** | Haiku | - | When you ask about Claude Code features |

### Creating Custom Subagents

**Interactive method (recommended):**
```
/agents
# Select "Create new agent" -> Personal or Project
# Generate with Claude or write manually
```

**Manual method:**

Create `.claude/agents/newsletter-reviewer.md`:

```markdown
---
name: newsletter-reviewer
description: Reviews newsletter HTML for deliverability and rendering issues. Use proactively after email template changes.
tools: Read, Grep, Glob, Bash
model: sonnet
memory: project
---

You are a senior email developer specializing in newsletter deliverability.

When invoked:
1. Check HTML email against email client compatibility
2. Validate all links are absolute URLs
3. Check image alt text is present
4. Verify preheader text is set
5. Check for spam trigger words
6. Validate tracking pixels and UTM parameters
7. Test dark mode compatibility

Provide feedback organized by:
- Critical (blocks send)
- Warning (should fix)
- Suggestion (nice to have)
```

### Supported Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique identifier (lowercase, hyphens) |
| `description` | Yes | When Claude should delegate. Include "use proactively" for eager delegation |
| `tools` | No | Tools the subagent can use. Inherits all if omitted |
| `disallowedTools` | No | Tools to deny, removed from inherited list |
| `model` | No | `sonnet`, `opus`, `haiku`, full model ID, or `inherit` (default) |
| `permissionMode` | No | `default`, `acceptEdits`, `dontAsk`, `bypassPermissions`, `plan` |
| `maxTurns` | No | Maximum agentic turns before stopping |
| `skills` | No | Skills to preload into context at startup |
| `mcpServers` | No | MCP servers available to this subagent |
| `hooks` | No | Lifecycle hooks scoped to this subagent |
| `memory` | No | Persistent memory scope: `user`, `project`, or `local` |
| `background` | No | `true` = always run as background task |
| `effort` | No | Override effort level: `low`, `medium`, `high`, `max` |
| `isolation` | No | `worktree` = run in temporary git worktree |

### Subagent Scopes

| Location | Scope | Priority |
|----------|-------|----------|
| `--agents` CLI flag | Current session only | 1 (highest) |
| `.claude/agents/` | Current project | 2 |
| `~/.claude/agents/` | All your projects | 3 |
| Plugin's `agents/` | Where plugin enabled | 4 (lowest) |

### CLI-Defined Subagents

```bash
claude --agents '{
  "code-reviewer": {
    "description": "Expert code reviewer. Use proactively after code changes.",
    "prompt": "You are a senior code reviewer. Focus on code quality, security, and best practices.",
    "tools": ["Read", "Grep", "Glob", "Bash"],
    "model": "sonnet"
  },
  "debugger": {
    "description": "Debugging specialist for errors and test failures.",
    "prompt": "You are an expert debugger. Analyze errors, identify root causes, and provide fixes."
  }
}'
```

### Invoking Subagents

```
# Automatic delegation (Claude decides based on description)
review the newsletter template for rendering issues

# Natural language (name the subagent)
Use the newsletter-reviewer subagent to check the new template

# @-mention for guaranteed delegation
@"newsletter-reviewer (agent)" check the new campaign email

# Session-wide agent mode
claude --agent newsletter-reviewer

# Background execution
Use a subagent in the background to run the full test suite

# Ctrl+B to background a running task
```

### Foreground vs Background Subagents

| Mode | Behavior |
|------|----------|
| **Foreground** | Blocks main conversation. Permission prompts pass through to you |
| **Background** | Runs concurrently. Pre-approves needed permissions before launch. Auto-denies anything not pre-approved |

To disable all background tasks: `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1`

### Persistent Memory for Subagents

```yaml
---
name: code-reviewer
memory: user
---
```

| Scope | Location | Use when |
|-------|----------|----------|
| `user` | `~/.claude/agent-memory/<name>/` | Learnings across all projects |
| `project` | `.claude/agent-memory/<name>/` | Project-specific, shareable via git |
| `local` | `.claude/agent-memory-local/<name>/` | Project-specific, not in git |

**Tip:** Ask the subagent to consult its memory before starting work: "Review this PR, and check your memory for patterns you've seen before." Ask it to update memory after: "Save what you learned to your memory."

### Restricting Subagent Spawning

```yaml
---
name: coordinator
description: Coordinates work across specialized agents
tools: Agent(worker, researcher), Read, Bash
---
```

Only `worker` and `researcher` subagents can be spawned. To block specific agents while allowing others:
```json
{
  "permissions": {
    "deny": ["Agent(Explore)", "Agent(my-custom-agent)"]
  }
}
```

### Resuming Subagents

Each subagent invocation creates a new instance. To continue existing work:
```
Continue that code review and now analyze the authorization logic
```
Claude resumes the subagent with full context from previous conversation.

### Key Patterns

**Isolate high-volume operations (saves context):**
```
Use a subagent to run the test suite and report only failing tests
```

**Parallel research (independent investigations):**
```
Research the authentication, database, and API modules in parallel using separate subagents
```

**Chain subagents (sequential workflow):**
```
Use the code-reviewer subagent to find issues, then use the optimizer to fix them
```

**Worktree isolation (parallel file edits):**
```yaml
---
name: feature-builder
isolation: worktree
---
```

### When to Use Subagents vs Main Conversation

| Use Main Conversation | Use Subagents |
|----------------------|---------------|
| Frequent back-and-forth | Verbose output you don't need in main context |
| Multiple phases sharing context | Enforce specific tool/permission restrictions |
| Quick, targeted changes | Self-contained tasks returning summaries |
| Latency matters | Research without cluttering main context |

For quick questions: Use `/btw` instead (sees full context, no tool access, answer discarded).

---

## Agent Teams: Parallel Orchestration

Agent teams coordinate multiple Claude Code instances working together. One session is the lead; others are teammates with independent context windows. Unlike subagents, teammates can message each other directly.

**Requirements:** Claude Code v2.1.32+. Agent teams are experimental.

### Enable Agent Teams

```json
// ~/.claude/settings.json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

### Starting a Team

```
Create an agent team to audit all client newsletter configurations:
- One teammate checking deliverability settings
- One teammate reviewing analytics tracking
- One teammate validating template rendering
- One teammate checking compliance (CAN-SPAM, GDPR)

Have them share findings and flag any critical issues.
```

### Architecture

| Component | Role |
|-----------|------|
| **Team lead** | Main session. Creates team, spawns teammates, coordinates |
| **Teammates** | Separate Claude Code instances with independent context |
| **Task list** | Shared work items teammates claim and complete |
| **Mailbox** | Messaging system for inter-agent communication |

Team data stored at:
- Config: `~/.claude/teams/{team-name}/config.json`
- Tasks: `~/.claude/tasks/{team-name}/`

### Display Modes

| Mode | Description | Requirement |
|------|-------------|-------------|
| **In-process** (default) | All teammates in your terminal. `Shift+Down` to cycle | Any terminal |
| **Split panes** | Each teammate gets own pane. Click to interact | tmux or iTerm2 |
| **Auto** | Split panes if in tmux/iTerm2, else in-process | Default |

```json
{
  "teammateMode": "in-process"
}
```

Or per-session: `claude --teammate-mode in-process`

### Task Management

Tasks have three states: pending, in progress, completed. Tasks can depend on other tasks.
- **Lead assigns**: Tell the lead which task to give which teammate
- **Self-claim**: After finishing, a teammate picks up the next unassigned, unblocked task
- File locking prevents race conditions when multiple teammates claim simultaneously

### Competing Hypotheses Debugging

```
Users report the app exits after one message instead of staying connected.
Spawn 5 agent teammates to investigate different hypotheses. Have them talk
to each other to try to disprove each other's theories, like a scientific
debate. Update the findings doc with whatever consensus emerges.
```

### Requiring Plan Approval

```
Spawn an architect teammate to refactor the authentication module.
Require plan approval before they make any changes.
```

Teammate works in plan mode until lead approves. Rejected = revise + resubmit.

### Quality Gates with Hooks

```bash
#!/bin/bash
# TaskCompleted hook -- verify tests pass before marking done
if ! npm test 2>&1; then
  echo "Tests failing. Fix before completing task." >&2
  exit 2
fi
exit 0
```

### Best Practices for Teams

- Start with 3-5 teammates (coordination overhead increases with team size)
- 5-6 tasks per teammate keeps everyone productive
- Avoid having two teammates edit the same file
- Pre-approve common operations in `/permissions` before spawning
- Don't let teams run unattended too long
- Start with research/review tasks before parallel implementation
- Tell the lead to "wait for teammates to finish" if it starts doing work itself
- Always use the lead to clean up (`Clean up the team`)

### Agent Teams vs Subagents

| | Subagents | Agent Teams |
|--|-----------|-------------|
| **Context** | Own window; results return to caller | Own window; fully independent |
| **Communication** | Report back to main agent only | Teammates message each other |
| **Coordination** | Main agent manages all | Shared task list with self-coordination |
| **Best for** | Focused tasks where only result matters | Complex work requiring discussion |
| **Token cost** | Lower | Higher (each teammate = separate instance) |

### Known Limitations

- No session resumption with in-process teammates
- Task status can lag (teammates may not mark tasks complete)
- One team per session
- No nested teams (teammates cannot spawn teams)
- Lead is fixed for team lifetime
- Split panes not supported in VS Code terminal, Windows Terminal, or Ghostty

---

## CLI Power Moves

### Non-Interactive Mode (Scripting)

```bash
# One-off query
claude -p "Explain what this project does"

# Structured output
claude -p "List all API endpoints" --output-format json

# Streaming JSON (real-time)
claude -p "Analyze this log file" --output-format stream-json

# Pipe data through Claude
cat build-error.txt | claude -p 'explain the root cause' > output.txt

# Budget limit
claude -p --max-budget-usd 5.00 "large analysis task"

# Turn limit
claude -p --max-turns 10 "focused task"

# Plan mode (read-only analysis)
claude --permission-mode plan -p "Analyze the authentication system"

# Fallback model for overload
claude -p --fallback-model sonnet "query"

# Add to package.json scripts
"lint:claude": "claude -p 'look at changes vs main and report issues'"
```

### Session Management

```bash
# Continue most recent conversation
claude --continue    # or -c

# Resume by name
claude --resume auth-refactor

# Name a session at start
claude -n "client-x-redesign"

# Rename mid-session
/rename auth-refactor

# Resume from PR
claude --from-pr 123

# Fork a session (branch the conversation)
claude --resume abc123 --fork-session

# Start a web session
claude --remote "Fix the login bug"

# Teleport web session to local terminal
claude --teleport
```

### Complete CLI Flags Reference

| Flag | Description |
|------|-------------|
| `--add-dir` | Add additional working directories |
| `--agent` | Start session as specific agent |
| `--agents` | Define subagents dynamically via JSON |
| `--allowedTools` | Tools that execute without prompting |
| `--append-system-prompt` | Append to default system prompt |
| `--append-system-prompt-file` | Append system prompt from file |
| `--channels` | Enable named channel servers |
| `--chrome` | Enable Chrome browser integration |
| `--continue`, `-c` | Continue most recent conversation |
| `--dangerously-skip-permissions` | Skip permission prompts (use with caution) |
| `--debug` | Enable debug mode with category filtering |
| `--disable-slash-commands` | Disable all skills/commands |
| `--disallowedTools` | Remove tools from model context |
| `--effort` | Set effort level: `low`, `medium`, `high`, `max` |
| `--fallback-model` | Auto-fallback when default overloaded (print mode) |
| `--fork-session` | Create new session ID when resuming |
| `--from-pr` | Resume sessions linked to a GitHub PR |
| `--json-schema` | Get validated JSON output matching schema (print mode) |
| `--max-budget-usd` | Maximum dollar spend before stopping |
| `--max-turns` | Limit agentic turns (print mode) |
| `--mcp-config` | Load MCP servers from JSON file |
| `--model` | Set model: `sonnet`, `opus`, full ID |
| `--name`, `-n` | Set session display name |
| `--no-chrome` | Disable Chrome integration |
| `--output-format` | `text`, `json`, `stream-json` |
| `--permission-mode` | `default`, `plan`, `acceptEdits`, `dontAsk`, `bypassPermissions` |
| `--print`, `-p` | Non-interactive mode |
| `--remote` | Create new web session |
| `--remote-control`, `--rc` | Enable Remote Control for cross-device |
| `--resume`, `-r` | Resume session by ID or name |
| `--strict-mcp-config` | Only use specified MCP servers |
| `--system-prompt` | Replace entire system prompt |
| `--system-prompt-file` | Replace system prompt from file |
| `--teammate-mode` | Agent team display: `auto`, `in-process`, `tmux` |
| `--teleport` | Resume web session locally |
| `--tools` | Restrict available tools. `""` = none, `"default"` = all |
| `--verbose` | Enable verbose logging |
| `--version`, `-v` | Output version |
| `--worktree`, `-w` | Start in isolated git worktree |

### Fan Out Across Files

```bash
# Generate task list, then process in parallel
for file in $(cat files.txt); do
  claude -p "Migrate $file from React to Vue. Return OK or FAIL." \
    --allowedTools "Edit,Bash(git commit *)"
done
```

---

## Prompt Engineering for Claude Code

### The Interview Technique

For complex features, let Claude interview you first:

```
I want to build [brief description]. Interview me in detail using
the AskUserQuestion tool.

Ask about technical implementation, UI/UX, edge cases, concerns,
and tradeoffs. Don't ask obvious questions -- dig into the hard
parts I might not have considered.

Keep interviewing until we've covered everything, then write a
complete spec to SPEC.md.
```

Then start a fresh session to execute the spec. Clean context focused entirely on implementation.

### The Four-Phase Workflow

1. **Explore** (Plan Mode): Read files, understand the codebase
2. **Plan**: Create detailed implementation plan. Press `Ctrl+G` to edit in your text editor
3. **Implement** (Normal Mode): Code, test, verify
4. **Commit**: Descriptive message + PR

### Prompt Strategies

| Strategy | Before | After |
|----------|--------|-------|
| **Scope the task** | "add tests for foo.py" | "write a test for foo.py covering the edge case where the user is logged out. avoid mocks." |
| **Point to sources** | "why does ExecutionFactory have a weird api?" | "look through ExecutionFactory's git history and summarize how its api came to be" |
| **Reference patterns** | "add a calendar widget" | "look at how existing widgets work on the home page. HotDogWidget.php is a good example. follow the pattern for a new calendar widget." |
| **Describe symptoms** | "fix the login bug" | "users report login fails after session timeout. check src/auth/, especially token refresh. write a failing test, then fix it." |
| **Give verification** | "implement email validation" | "write a validateEmail function. test cases: user@example.com -> true, invalid -> false, user@.com -> false. run tests after implementing." |

### Rich Content in Prompts

- **Reference files with @** instead of describing locations
- **Paste images directly** (copy/paste, drag-drop, or path reference)
- **Give URLs** for documentation and API references
- **Pipe in data**: `cat error.log | claude`
- **Let Claude fetch**: Tell Claude to pull context itself with tools

### When to Be Vague

Vague prompts are useful when exploring:
- "what would you improve in this file?"
- "investigate this error"
- "explain this architecture"

Precision is for execution; vagueness is for discovery.

### Extended Thinking in Prompts

Include the word "ultrathink" anywhere in your prompt to set effort to high for that turn (Opus 4.6 and Sonnet 4.6). Useful for one-off deep reasoning without changing your effort setting permanently.

---

## Context Management Mastery

### The #1 Rule

**Context is your most precious resource.** Every file read, command output, and message consumes it. Performance degrades as it fills.

### Context Management Cheat Sheet

| Situation | Action |
|-----------|--------|
| Switching topics | `/clear` |
| Context getting full | `/compact Focus on X` |
| Need to research | Use subagent (preserves main context) |
| Quick question | `/btw` (doesn't enter history) |
| Part of conversation irrelevant | `Esc + Esc` or `/rewind`, select checkpoint, "Summarize from here" |
| Long session degrading | `/clear` + better initial prompt |
| Need to remember across /compact | Put it in CLAUDE.md (not just conversation) |

### Auto-Compaction

Claude Code automatically compacts when approaching context limits. Customize behavior:
- Add to CLAUDE.md: "When compacting, always preserve the full list of modified files and any test commands"
- Set `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=50` for earlier auto-compaction

### /compact With Focus

```
/compact Focus on the API changes we made to auth.ts
/compact Keep the list of modified files and test results
/compact Preserve the database migration plan
```

### Rewind / Checkpoints

Every action creates a checkpoint. Double-tap `Escape` or `/rewind` to open the menu:
- Restore conversation only
- Restore code only
- Restore both
- Summarize from a selected message

Checkpoints persist across sessions. Close your terminal and still rewind later.

**Note:** Checkpoints only track changes made by Claude, not external processes. Not a replacement for git.

### /btw for Side Questions

```
/btw what's the syntax for TypeScript generics again?
```

Answer appears in a dismissible overlay, never enters conversation history. Zero context cost.

### The 2-Correction Rule

If you've corrected Claude more than twice on the same issue, the context is cluttered with failed approaches. `/clear` and start fresh with a better prompt incorporating what you learned. A clean session with a better prompt almost always outperforms accumulated corrections.

---

## Settings & Configuration Deep Dive

### Settings Files & Precedence

1. **Managed** (highest) -- cannot be overridden
2. **Command line arguments** -- temporary session overrides
3. **Local** (`.claude/settings.local.json`) -- you, this project only
4. **Project** (`.claude/settings.json`) -- all collaborators
5. **User** (`~/.claude/settings.json`) -- you, all projects

### Complete Settings Reference

| Key | Description | Example |
|-----|-------------|---------|
| `permissions` | Allow/deny rules for tools | See Permissions section |
| `hooks` | Lifecycle hook definitions | See Hooks section |
| `env` | Environment variables for every session | `{"FOO": "bar"}` |
| `model` | Default model override | `"claude-sonnet-4-6"` |
| `availableModels` | Restrict model selection in `/model` | `["sonnet", "haiku"]` |
| `effortLevel` | Persistent effort level | `"medium"` |
| `agent` | Run main thread as named subagent | `"code-reviewer"` |
| `autoMemoryEnabled` | Toggle auto memory | `false` |
| `autoMemoryDirectory` | Custom memory storage path | `"~/my-memory"` |
| `cleanupPeriodDays` | Session retention (default: 30) | `20` |
| `statusLine` | Custom status line config | `{"type":"command","command":"~/.claude/statusline.sh"}` |
| `teammateMode` | Agent team display mode | `"in-process"` |
| `language` | Claude's response language | `"japanese"` |
| `outputStyle` | Adjust system prompt style | `"Explanatory"` |
| `alwaysThinkingEnabled` | Extended thinking default | `true` |
| `includeGitInstructions` | Include git workflow instructions | `false` |
| `disableAllHooks` | Disable all hooks | `true` |
| `enableAllProjectMcpServers` | Auto-approve project MCP servers | `true` |
| `enabledMcpjsonServers` | Specific approved MCP servers | `["memory", "github"]` |
| `claudeMdExcludes` | Skip specific CLAUDE.md files | `["**/other/CLAUDE.md"]` |
| `attribution` | Custom git commit attribution | `{"commit": "Generated with AI"}` |
| `spinnerVerbs` | Custom spinner action verbs | `{"mode":"append","verbs":["Pondering"]}` |
| `voiceEnabled` | Push-to-talk voice dictation | `true` |
| `autoUpdatesChannel` | Release channel: `"stable"` or `"latest"` | `"stable"` |
| `prefersReducedMotion` | Reduce UI animations | `true` |
| `plansDirectory` | Custom plan file storage | `"./plans"` |
| `forceLoginMethod` | Restrict login to `claudeai` or `console` | `"claudeai"` |
| `forceLoginOrgUUID` | Auto-select organization during login | UUID string |

### JSON Schema for Autocompletion

Add this to the top of your settings.json for autocomplete in VS Code/Cursor:

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": { ... }
}
```

---

## Permissions & Security

### Permission Modes

| Mode | Behavior | Shortcut |
|------|----------|----------|
| **Normal** (default) | Standard permission checking | Default |
| **Auto-Accept** | Auto-accept file edits | `Shift+Tab` once |
| **Plan** | Read-only exploration, no changes | `Shift+Tab` twice |
| **Don't Ask** | Auto-deny permission prompts (allowed tools still work) | Settings |
| **Bypass Permissions** | Skip prompts (use with extreme caution) | `--dangerously-skip-permissions` |

### Sandbox Mode

OS-level isolation that restricts filesystem and network access, allowing Claude to work more freely within boundaries:

```
/sandbox
```

### Permission Rule Syntax

```json
{
  "permissions": {
    "allow": [
      "Bash(npm run lint)",
      "Bash(npm run test *)",
      "Bash(git *)",
      "Read(~/.zshrc)",
      "Skill(commit)",
      "Skill(review-pr *)"
    ],
    "deny": [
      "Bash(curl *)",
      "Read(./.env)",
      "Read(./.env.*)",
      "Agent(Explore)"
    ],
    "defaultMode": "plan"
  }
}
```

---

## Extended Thinking & Model Configuration

### Extended Thinking

Enabled by default. Claude reasons through complex problems step-by-step before responding.

| Config Method | How | Details |
|--------------|-----|---------|
| **Effort level** | `/effort`, `/model`, or `CLAUDE_CODE_EFFORT_LEVEL` | Control thinking depth for Opus 4.6 and Sonnet 4.6 |
| **"ultrathink" keyword** | Include in any prompt | Sets effort to high for that turn |
| **Toggle shortcut** | `Option+T` (Mac) / `Alt+T` (Win/Linux) | Toggle on/off for current session |
| **Global default** | `/config` toggle | Saved as `alwaysThinkingEnabled` |
| **Token budget limit** | `MAX_THINKING_TOKENS` env var | On Opus/Sonnet 4.6, only `0` applies unless adaptive thinking disabled |

View thinking: Press `Ctrl+O` for verbose mode. Thinking appears as gray italic text.

### Effort Levels (Opus 4.6 / Sonnet 4.6)

| Level | Behavior |
|-------|----------|
| `low` | Minimal thinking. Fast responses. Good for simple tasks |
| `medium` | Balanced. Default for most work |
| `high` | Deep reasoning. Complex architecture, debugging, planning |
| `max` | Maximum thinking (Opus 4.6 only) |

```bash
# Set per-session
claude --effort high

# Set persistently
/effort high
# Saved to settings.json as effortLevel
```

### Model Selection

```bash
# Use specific model for session
claude --model claude-opus-4-6
claude --model sonnet
claude --model haiku

# Set default in settings
{
  "model": "claude-sonnet-4-6"
}

# Restrict available models
{
  "availableModels": ["sonnet", "haiku"]
}
```

---

## Best Practices & Anti-Patterns

### The #1 Leverage Point

**Give Claude a way to verify its work.** Include tests, screenshots, or expected outputs. This is the single highest-leverage thing you can do.

```
# Bad
"implement email validation"

# Good
"write a validateEmail function. test cases: user@example.com -> true,
invalid -> false, user@.com -> false. run the tests after implementing"
```

### The Top 10 Best Practices

1. **Give verification criteria.** Tests, screenshots, expected outputs. Always.
2. **Explore first, plan second, code third.** Use Plan Mode for research.
3. **Be specific in prompts.** Reference files, mention constraints, point to patterns.
4. **Use `/clear` between unrelated tasks.** Context pollution is the #1 killer.
5. **Use subagents for research.** Keep main context clean for implementation.
6. **Write a concise CLAUDE.md.** Under 200 lines. Prune ruthlessly.
7. **Configure permissions early.** Reduce fatigue. `/permissions` or settings.json.
8. **Use hooks for deterministic actions.** Format, lint, block, notify -- guaranteed.
9. **Install a status line.** Monitor context usage continuously.
10. **Name your sessions.** `/rename auth-refactor` for easy resumption later.

### Anti-Patterns to Avoid

| Anti-Pattern | Symptom | Fix |
|-------------|---------|-----|
| **Kitchen sink session** | Mixing unrelated tasks | `/clear` between tasks |
| **Correction spiral** | Fixing same error 3+ times | `/clear`, better initial prompt |
| **Over-specified CLAUDE.md** | 500+ lines nobody reads | Prune to <200 lines, use rules/ |
| **Trust-then-verify gap** | Shipping without testing | Always provide verification criteria |
| **Infinite exploration** | "investigate everything" | Scope narrowly, use subagents |
| **Context hoarding** | Never clearing, never compacting | `/clear` frequently, `/compact` when needed |
| **Permission fatigue** | Clicking through 50 approvals | `/permissions` allowlist upfront |
| **Ignoring degradation** | Quality drops but you keep going | `/clear` + fresh prompt |

### When to Skip Planning

Planning adds overhead. Skip it when:
- The scope is clear and the fix is small
- You're fixing a typo, adding a log line, renaming a variable
- You could describe the diff in one sentence

Plan when:
- Uncertain about the approach
- Change modifies multiple files
- Unfamiliar with the code being modified

---

## Multi-Client Agency Setup

### Project Structure

```
agency-root/
  .claude/
    CLAUDE.md              # Agency-wide standards
    rules/
      shared/              # Symlinked to ~/agency-claude-rules
      code-style.md
      git-workflow.md
    skills/
      client-onboard/      # Onboard new client
      campaign-deploy/     # Deploy newsletter campaign
      analytics-report/    # Generate client report
    agents/
      newsletter-reviewer.md
      analytics-agent.md
      client-auditor.md
  clients/
    acme-corp/
      .claude/
        CLAUDE.md          # Acme-specific instructions
        rules/
          acme-api.md      # Acme-specific API rules
      src/
    beta-inc/
      .claude/
        CLAUDE.md          # Beta-specific instructions
      src/
```

### Agency-Wide CLAUDE.md

```markdown
# Agency Standards

## Client Isolation
- IMPORTANT: Never reference or access another client's data
- Each client project is fully isolated
- Use client-specific env vars, never hardcode credentials

## Workflow
- All work done in feature branches
- PRs require at least one review
- Every deployment gets a changelog entry
- Client reporting on Monday mornings

## Tools
- ESPs: Mailchimp API, SendGrid API, Klaviyo API
- Analytics: Google Analytics 4, Plausible
- CMS: WordPress REST API, Ghost API
- Design: Figma API via MCP
```

### Per-Client CLAUDE.md

```markdown
# Acme Corp - Newsletter Project

## ESP: Mailchimp
- API key in ACME_MAILCHIMP_KEY env var
- List ID: abc123def
- Template folder: /templates/acme/

## Brand Guidelines
- Primary color: #2563EB
- Font: Inter for headings, system font for body
- Tone: Professional but approachable
- Never use exclamation marks in subject lines

## Sending Schedule
- Tuesday 9am EST (main newsletter)
- Thursday 2pm EST (product updates)
```

### User-Level CLAUDE.md (~/.claude/CLAUDE.md)

```markdown
# Jay's Personal Preferences

## Working Style
- Always explain reasoning before making changes
- Prefer functional programming patterns
- Use TypeScript over JavaScript when possible

## Tools
- Terminal: Warp
- Editor: VS Code
- Git GUI: GitKraken for complex merges

## Agency Shortcuts
- Client list: @~/agency/clients.md
- Standard templates: @~/agency/templates/
```

### Switching Between Clients

```bash
# Use worktrees for parallel client work
claude --worktree acme-newsletter
# (In another terminal)
claude --worktree beta-redesign

# Or use named sessions
claude -n "acme-weekly" --add-dir ../shared-templates
claude -n "beta-onboard" --add-dir ../shared-templates
```

---

## Claude Code + Obsidian Workflow

### Strategy: Obsidian as Knowledge Base, Claude Code as Executor

Since Claude Code can read files via `@` references and `--add-dir`, your Obsidian vault becomes a powerful knowledge base:

```bash
# Give Claude Code access to your Obsidian vault
claude --add-dir "/Users/jay/Documents/the vault"

# Also load CLAUDE.md from the vault
CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1 claude --add-dir "/Users/jay/Documents/the vault"
```

Or set it permanently in CLAUDE.md:

```markdown
# Knowledge Base
- Obsidian vault available at: /Users/jay/Documents/the vault
- Reference client briefs in the vault for context
- Check /the vault/templates/ for standard formats
```

### Obsidian MCP Integration

Use an Obsidian MCP server to let Claude search and read your notes:

```bash
claude mcp add obsidian -- npx -y @anthropic-ai/mcp-obsidian \
  --vault-path "/Users/jay/Documents/the vault"
```

### Workflow: Research to Execution

1. **Research phase**: Take notes in Obsidian as you discover things
2. **Brief Claude**: Reference your Obsidian notes with `@` when prompting
3. **Execute**: Claude implements based on your research
4. **Document**: Ask Claude to write findings back to your vault

### Practical Example

```
Read @"/Users/jay/Documents/the vault/clients/acme/brief.md" and
implement the newsletter redesign described there. Follow the brand
guidelines in @"/Users/jay/Documents/the vault/clients/acme/brand.md"
```

### Skill: Generate Obsidian Note from Code Analysis

```yaml
---
name: vault-note
description: Generate an Obsidian-formatted analysis note
disable-model-invocation: true
---

Analyze $ARGUMENTS and create an Obsidian-formatted markdown note.

Include:
- YAML frontmatter with tags, date, and category
- Summary section
- Key findings with wiki-links to related notes
- Code snippets where relevant
- Action items as Obsidian tasks (- [ ])

Write the note to: /Users/jay/Documents/the vault/notes/$0-analysis.md
```

---

## Claude Code + n8n Automation

### Strategy: Claude Code as n8n Workflow Builder and Debugger

Claude Code can read, write, and debug n8n workflow JSON files directly.

### Build n8n Automations

```
Read the n8n workflow at @automations/newsletter-signup.json
and add a step that sends a Slack notification when a new subscriber
signs up with a .edu email address.
```

### Debug n8n Errors

```bash
cat /tmp/n8n-error.log | claude -p "Explain this n8n workflow error and suggest a fix"
```

### Skill: Create n8n Workflow

```yaml
---
name: n8n-workflow
description: Create or modify n8n automation workflows
---

Create an n8n workflow for: $ARGUMENTS

Requirements:
1. Use n8n's native JSON workflow format
2. Include error handling nodes
3. Add webhook triggers where appropriate
4. Include Slack/email notifications for failures
5. Save to /automations/ directory
6. Include a README explaining the workflow

Reference existing workflows in @automations/ for patterns.
```

### Common n8n + Newsletter Automations

| Workflow | Trigger | Actions |
|----------|---------|---------|
| New subscriber welcome | Webhook from ESP | Add to CRM, send welcome sequence, notify Slack |
| Campaign performance | Scheduled (daily) | Pull ESP stats, generate report, post to Slack |
| Bounce handler | Webhook from ESP | Update subscriber status, alert if bounce rate >2% |
| Content pipeline | RSS/webhook | Curate content, draft newsletter, create review task |
| Client report | Scheduled (weekly) | Aggregate analytics, generate PDF, email to client |

### Non-Interactive n8n Debugging

```bash
claude -p "Validate the n8n workflow at automations/signup-flow.json. \
Check for missing credentials, broken connections, and logical errors. \
Output a JSON report." --output-format json > validation-report.json
```

---

## Data Analysis Workflows

### Subagent: Data Scientist

Create `.claude/agents/data-analyst.md`:

```markdown
---
name: data-analyst
description: Analyze newsletter and campaign data. Use proactively for data analysis tasks, metric queries, and performance reports.
tools: Bash, Read, Write
model: sonnet
memory: project
---

You are a data analyst specializing in email marketing and newsletter metrics.

When invoked:
1. Understand the analysis requirement
2. Query data sources (CSV, JSON, databases)
3. Use Python/pandas for analysis when appropriate
4. Generate clear visualizations when helpful
5. Present findings with actionable recommendations

Key metrics you track:
- Open rates, click rates, conversion rates
- Subscriber growth and churn
- Revenue per subscriber
- A/B test results
- Deliverability metrics (bounce, spam, unsubscribe rates)

Always provide:
- Executive summary (3 bullet points)
- Detailed findings with data
- Specific recommendations
- Comparison to industry benchmarks

Update your agent memory as you discover data patterns, metric baselines,
and analytical approaches that work well for this project.
```

### Analysis Commands

```bash
# Pipe CSV data for analysis
cat subscriber-data.csv | claude -p "Analyze subscriber growth trends. \
Identify the top 3 acquisition channels and churn patterns."

# Quick metric check
claude -p "Read @analytics/march-2026.json and tell me: \
1. Which campaigns had >25% open rate \
2. Any deliverability issues \
3. Top performing subject lines"
```

### Skill: Generate Client Report

```yaml
---
name: client-report
description: Generate a weekly client performance report
context: fork
agent: data-analyst
---

Generate a weekly performance report for client: $0

1. Read analytics data from @clients/$0/analytics/
2. Compare with previous week's data
3. Calculate key metrics: open rate, CTR, conversions, revenue
4. Identify trends and anomalies
5. Generate recommendations
6. Format as a professional report
7. Save to clients/$0/reports/week-of-$(date +%Y-%m-%d).md
```

---

## CI/CD & GitHub Actions Integration

### Claude Code in CI/CD Pipelines

```bash
# Automated code review in CI
claude -p "Review the changes in this PR for security issues, \
code quality, and test coverage. Output findings as JSON." \
  --output-format json > review.json

# Automated translations
claude -p "translate new strings into French and raise a PR for review"

# Lint with Claude
claude -p 'look at changes vs main and report issues related to typos. \
Report filename and line number on one line, description on the second. \
Do not return any other text.'
```

### GitHub Actions Integration

Claude Code can automate PR reviews and issue triage via GitHub Actions. See official docs at `code.claude.com/docs/en/github-actions`.

### GitLab CI/CD

Claude Code also supports GitLab CI/CD integration. See `code.claude.com/docs/en/gitlab-ci-cd`.

### Automated Code Review on Every PR

Set up `@Claude` code review on GitHub PRs. See `code.claude.com/docs/en/code-review`.

---

## Debugging Workflows

### The Standard Debugging Flow

```
# 1. Share the error
I'm seeing this error when I run npm test:
[paste error]

# 2. Let Claude trace the root cause
trace the full path from the error to the root cause

# 3. Get fix recommendations
suggest a few ways to fix this. explain tradeoffs.

# 4. Apply and verify
implement option 2. run the tests after to verify.
```

### Debugging Tips

- **Tell Claude the command to reproduce** so it can get a stack trace
- **Mention if intermittent** so Claude investigates timing/race conditions
- **Use subagents** for investigation to keep main context clean:
  ```
  Use subagents to investigate how our authentication system handles
  token refresh, and whether we have any existing OAuth utilities
  ```
- **Use the Chrome extension** for frontend debugging -- Claude can screenshot, inspect elements, and iterate
- **Use `/debug` skill** to troubleshoot Claude Code session issues itself

### Competing Hypotheses with Agent Teams

```
The newsletter open rates dropped 40% for client X.
Spawn 3 agent teammates to investigate:
- One checks ESP configuration and deliverability metrics
- One reviews recent template changes
- One examines sending time and audience segmentation changes
Have them debate and converge on the root cause.
```

---

## Testing Workflows

### Write Tests

```
find functions in NotificationsService.swift that are not covered by tests
add tests for the notification service covering edge conditions
run the new tests and fix any failures
```

### Test-Driven Development with Parallel Sessions

| Session A (Tests) | Session B (Implementation) |
|-------------------|---------------------------|
| Write failing tests for the auth module | |
| | Implement code to pass all tests |
| Review implementation for edge cases | |

### Fan-Out Testing

```bash
# Test each module independently
for module in auth payments notifications; do
  claude -p "Run tests for the $module module. Report PASS/FAIL with details." \
    --max-turns 5 --allowedTools "Bash(npm test *),Read"
done
```

---

## Git & PR Workflows

### Create Commits and PRs

```
# Automatic commit message
commit my changes with a descriptive message

# Create PR with context
create a pr for my changes. describe the security improvements.

# Resume from PR later
claude --from-pr 123
```

### Writer/Reviewer Pattern

| Session A (Writer) | Session B (Reviewer) |
|-------------------|---------------------|
| Implement the rate limiter for API endpoints | |
| | Review the rate limiter in @src/middleware/rateLimiter.ts for edge cases, race conditions, and consistency |
| Address review feedback | |

### PR-Based Session Linking

When you create a PR using `gh pr create`, the session is automatically linked. Resume with:
```bash
claude --from-pr 123
```

---

## Worktrees for Parallel Development

### The Problem

Multiple Claude sessions editing the same files = collisions. Git worktrees solve this by creating separate working directories with their own files and branch, sharing the same repository history.

### Using Worktrees

```bash
# Start Claude in a worktree
claude --worktree feature-auth
# Creates .claude/worktrees/feature-auth/ with branch worktree-feature-auth

# Another parallel session
claude --worktree bugfix-123

# Auto-generated name
claude --worktree
# Creates something like "bright-running-fox"

# Ask Claude to create one mid-session
"work in a worktree" or "start a worktree"
```

### Worktree Cleanup

- **No changes**: worktree and branch removed automatically on exit
- **Changes exist**: Claude prompts to keep or remove

### Subagent Worktrees

```yaml
---
name: feature-builder
isolation: worktree
---
```

Each subagent gets its own worktree, automatically cleaned up when done without changes.

### Manual Worktree Management

```bash
# Create with specific branch
git worktree add ../project-feature-a -b feature-a

# Check out existing branch
git worktree add ../project-bugfix bugfix-123

# List all worktrees
git worktree list

# Remove when done
git worktree remove ../project-feature-a
```

**Tip:** Add `.claude/worktrees/` to `.gitignore`.

---

## Plugins & The Plugin Ecosystem

Plugins bundle skills, hooks, subagents, and MCP servers into a single installable unit.

### Installing Plugins

```
/plugin
# Browse the marketplace
```

### Code Intelligence Plugins

Install a code intelligence plugin for your language to give Claude precise "go to definition" and "find references" navigation, plus automatic error detection after edits.

### Plugin Security

Plugin subagents do NOT support `hooks`, `mcpServers`, or `permissionMode` frontmatter fields (ignored for security). If you need them, copy the agent file to `.claude/agents/`.

### Local Plugin Development

```bash
claude --plugin-dir ./my-plugins
```

---

## Remote Control & Cross-Device Workflows

### Remote Control

Control your local Claude Code session from Claude.ai or the Claude iOS app:

```bash
# Start with Remote Control enabled
claude --remote-control "My Project"
# Or shorthand
claude --rc "My Project"

# Server mode (no local interactive session)
claude remote-control --name "My Project"
```

### Cross-Surface Workflows

| I want to... | Best option |
|--------------|-------------|
| Continue local session from phone | Remote Control |
| Push events from Telegram/Discord/webhooks | Channels |
| Start task locally, continue on mobile | Web or Claude iOS app |
| Transfer to Desktop app for visual diffs | `/desktop` |
| Pull web session into terminal | `/teleport` |

---

## Essential Community Tools & Resources

### Top GitHub Repositories

| Repository | Stars | Description |
|------------|-------|-------------|
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | 80.3k | Official repository with plugins directory |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 29.3k | Curated list of skills, hooks, commands, plugins |
| [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | 14.4k | 127+ specialized subagents across 10 categories |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | 9.3k | Curated list of Claude Skills and tools |
| [Mizoreww/awesome-claude-code-config](https://github.com/Mizoreww/awesome-claude-code-config) | 167 | Production-ready config with self-improvement loop |
| [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | 859 | 135 agents, 35 skills, 42 commands, 150+ plugins |

### Essential Tools to Install

| Tool | Purpose |
|------|---------|
| **Claude Squad** | Terminal app managing multiple agents in separate workspaces |
| **cc-sessions** | Opinionated productive Claude Code development |
| **claudekit** | CLI toolkit with auto-save checkpointing, 20+ subagents |
| **recall** | Full-text search of sessions with terminal resumption |
| **ccflare / better-ccflare** | Web UI usage dashboard with cost tracking |
| **Claude Code Usage Monitor** | Terminal-based real-time token tracking |
| **Dippy** | Auto-approve safe bash via AST parsing |
| **SuperClaude Framework** | Specialized commands and cognitive personas |

### Orchestrators for Complex Workflows

| Tool | Purpose |
|------|---------|
| **Claude Task Master** | Task management for AI-driven development |
| **Auto-Claude** | Multi-agent framework with kanban-style UI |
| **Claude Code Flow** | Code-first orchestration for recursive agent cycles |
| **Claude Swarm** | Launch sessions connected to agent swarms |

### Status Line Plugins

| Plugin | Description |
|--------|-------------|
| **ccstatusline** | Customizable model info, git branch, token display |
| **claude-powerline** | Vim-style with real-time usage tracking |
| **claudia-statusline** | Rust implementation with SQLite persistence |

---

## Claude Code vs Cursor vs Windsurf

### When to Use Each

| Criterion | Claude Code | Cursor | Windsurf |
|-----------|------------|--------|----------|
| **Paradigm** | Agentic (autonomous execution) | AI-assisted editing | AI-assisted editing |
| **Best for** | Complex multi-file tasks, automation, CI/CD | Quick inline edits, code completion | Code completion, chat-based editing |
| **Context** | Entire codebase + external tools via MCP | Open files + indexed codebase | Open files + indexed codebase |
| **Customization** | CLAUDE.md, skills, hooks, subagents, plugins | .cursorrules, custom commands | Rules, AI flows |
| **Automation** | Full CLI scripting, CI/CD, headless mode | Limited | Limited |
| **Multi-agent** | Native subagents + agent teams | No | No |
| **External tools** | MCP servers (Slack, Notion, GitHub, etc.) | Limited integrations | Limited integrations |
| **Terminal** | Native terminal-first | Integrated terminal | Integrated terminal |
| **Pricing** | Claude subscription or API usage | $20/mo Pro, $40/mo Business | $10/mo Pro, $50/mo Team |

### Why Claude Code Wins for Agency Work

1. **Multi-client isolation**: Worktrees + per-project CLAUDE.md + rules
2. **Automation**: Non-interactive mode for CI/CD, batch operations
3. **Tool integration**: MCP connects to all your agency tools (Slack, Notion, ESPs)
4. **Parallel work**: Agent teams for complex multi-faceted tasks
5. **Customization depth**: Skills, hooks, subagents are far more powerful than .cursorrules
6. **Scriptability**: Pipe data in/out, chain with other tools, fan out across files

### When to Use Cursor/Windsurf Instead

- Quick single-file edits where you want inline suggestions
- When you need real-time code completion as you type
- When working in a visual IDE is essential
- For junior developers who prefer guided code completion

### Combined Workflow

Many power users run Claude Code alongside their IDE:
- Use **Claude Code** for planning, architecture, multi-file changes, automation
- Use **Cursor** (with the Claude Code VS Code extension) for quick inline edits
- Use the **Claude Code Desktop app** for visual diff review

---

## Advanced Hook Recipes

This section provides battle-tested hook configurations that solve real workflow problems. Each recipe includes the settings.json configuration and any required shell scripts.

### Recipe: Enforce Branch Naming Conventions

Block commits to branches that don't follow your naming convention:

```bash
#!/bin/bash
# .claude/hooks/enforce-branch-naming.sh
COMMAND=$(jq -r '.tool_input.command' < /dev/stdin)

# Only check git commit commands
if echo "$COMMAND" | grep -q 'git commit'; then
  BRANCH=$(git branch --show-current 2>/dev/null)
  if [ -n "$BRANCH" ] && ! echo "$BRANCH" | grep -qE '^(feature|fix|chore|docs|refactor)/[A-Z]+-'; then
    echo "Branch name '$BRANCH' does not follow convention: type/CLIENT-description" >&2
    exit 2
  fi
fi
exit 0
```

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/enforce-branch-naming.sh"
          }
        ]
      }
    ]
  }
}
```

### Recipe: Inject Client Context on Session Start

Automatically load client-specific context when starting a session in a client directory:

```bash
#!/bin/bash
# .claude/hooks/load-client-context.sh
CWD=$(jq -r '.cwd' < /dev/stdin)

# Check if we're in a client directory
CLIENT_DIR=$(echo "$CWD" | grep -oP 'clients/\K[^/]+' 2>/dev/null)
if [ -n "$CLIENT_DIR" ] && [ -f "clients/$CLIENT_DIR/$CLIENT_DIR.md" ]; then
  echo "Working with client: $CLIENT_DIR. Client intelligence loaded from clients/$CLIENT_DIR/$CLIENT_DIR.md"
fi
exit 0
```

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/load-client-context.sh"
          }
        ]
      }
    ]
  }
}
```

### Recipe: Auto-Run Linter After Every Edit

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "FILE=$(jq -r '.tool_input.file_path' < /dev/stdin); if echo \"$FILE\" | grep -qE '\\.(ts|tsx|js|jsx)$'; then npx eslint --fix \"$FILE\" 2>/dev/null; fi",
            "async": true,
            "statusMessage": "Running ESLint..."
          }
        ]
      }
    ]
  }
}
```

### Recipe: Prevent Writes to Protected Directories

```bash
#!/bin/bash
# .claude/hooks/protect-dirs.sh
FILE_PATH=$(jq -r '.tool_input.file_path // empty' < /dev/stdin)

PROTECTED_DIRS="migrations|.github/workflows|infrastructure|terraform"

if echo "$FILE_PATH" | grep -qE "($PROTECTED_DIRS)/"; then
  jq -n '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: "Protected directory. Changes require manual review."
    }
  }'
  exit 0
fi
exit 0
```

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/protect-dirs.sh"
          }
        ]
      }
    ]
  }
}
```

### Recipe: Log All Tool Usage to a File (Full Audit Trail)

```bash
#!/bin/bash
# .claude/hooks/full-audit.sh
INPUT=$(cat)
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
SESSION_ID=$(echo "$INPUT" | jq -r '.session_id // "unknown"')
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name // "unknown"')
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // .tool_input.file_path // "N/A"')

echo "[$TIMESTAMP] session=$SESSION_ID tool=$TOOL_NAME action=$COMMAND" \
  >> ~/.claude/audit-log.txt
exit 0
```

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/full-audit.sh",
            "async": true
          }
        ]
      }
    ]
  }
}
```

### Recipe: Webhook Notification to Slack

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "idle_prompt",
        "hooks": [
          {
            "type": "http",
            "url": "https://hooks.slack.com/services/YOUR/WEBHOOK/URL",
            "headers": {
              "Content-Type": "application/json"
            },
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

### Recipe: Enforce Read-Only Database Queries

```bash
#!/bin/bash
# .claude/hooks/validate-readonly-query.sh
INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

if [ -z "$COMMAND" ]; then
  exit 0
fi

# Block write operations (case-insensitive)
if echo "$COMMAND" | grep -iE '\b(INSERT|UPDATE|DELETE|DROP|CREATE|ALTER|TRUNCATE|REPLACE|MERGE)\b' > /dev/null; then
  echo "Blocked: Write operations not allowed. Use SELECT queries only." >&2
  exit 2
fi

exit 0
```

### Recipe: Force Test Suite on Task Completion (Agent Teams)

```bash
#!/bin/bash
# .claude/hooks/task-completed-verify.sh
if ! npm test 2>&1; then
  echo "Tests failing. Fix before completing task." >&2
  exit 2
fi
exit 0
```

```json
{
  "hooks": {
    "TaskCompleted": [
      {
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/task-completed-verify.sh"
          }
        ]
      }
    ]
  }
}
```

### Recipe: Custom Permission Dialog via Prompt Hook

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "prompt",
            "prompt": "The following command is about to be executed. Is it safe and appropriate for the current task? If it could modify production data, cause data loss, or make irreversible changes, say no. Command details: $ARGUMENTS",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

---

## Advanced Skill Recipes

### Skill: Fix GitHub Issue End-to-End

```yaml
---
name: fix-issue
description: Fix a GitHub issue end-to-end
disable-model-invocation: true
---

Analyze and fix GitHub issue: $ARGUMENTS

1. Use `gh issue view $0` to get the issue details
2. Understand the problem described in the issue
3. Search the codebase for relevant files
4. Implement the necessary changes to fix the issue
5. Write and run tests to verify the fix
6. Ensure code passes linting and type checking
7. Create a descriptive commit message referencing the issue
8. Push and create a PR that closes the issue
```

Usage: `/fix-issue 1234`

### Skill: PR Review Checklist

```yaml
---
name: review-pr
description: Thorough PR review against team standards
context: fork
agent: Explore
---

## Pull request context
- PR diff: !`gh pr diff`
- PR comments: !`gh pr view --comments`
- Changed files: !`gh pr diff --name-only`
- PR description: !`gh pr view --json body --jq .body`

## Review checklist
For each changed file, check:

1. **Correctness**: Does the code do what the PR description says?
2. **Edge cases**: Are boundary conditions handled?
3. **Error handling**: Are errors caught and handled gracefully?
4. **Tests**: Are new behaviors tested? Are edge cases covered?
5. **Security**: Any SQL injection, XSS, secrets in code, or auth bypasses?
6. **Performance**: Any N+1 queries, unnecessary loops, or memory leaks?
7. **Code style**: Does it match existing patterns in the codebase?
8. **Documentation**: Are public APIs documented?

Provide feedback organized by severity:
- **Critical** (must fix before merge)
- **Warning** (should fix)
- **Suggestion** (nice to have)
- **Praise** (things done well)
```

### Skill: Generate API Documentation

```yaml
---
name: api-docs
description: Generate OpenAPI documentation for API endpoints
context: fork
---

Scan the codebase for API endpoints and generate OpenAPI 3.0 documentation.

1. Find all route definitions (Express, Fastify, or framework-specific)
2. For each endpoint, document:
   - HTTP method and path
   - Request parameters (path, query, body)
   - Response schema with status codes
   - Authentication requirements
   - Rate limiting if applicable
3. Generate a complete OpenAPI 3.0 YAML file
4. Save to docs/api-spec.yaml
5. Validate the generated spec
```

### Skill: Migration Planner

```yaml
---
name: migration-plan
description: Plan a technology migration with detailed steps
context: fork
agent: Explore
---

Create a detailed migration plan for: $ARGUMENTS

1. Analyze current usage of the technology being migrated
2. Identify all files and components affected
3. Assess dependencies and potential breaking changes
4. Create a phased migration plan with:
   - Phase 1: Setup and scaffolding
   - Phase 2: Core migration (highest-risk changes)
   - Phase 3: Peripheral migration (lower-risk changes)
   - Phase 4: Cleanup and removal of old code
5. For each phase, list:
   - Files to modify
   - Expected effort
   - Risks and mitigations
   - Verification steps
6. Save plan to MIGRATION-PLAN.md
```

### Skill: Client Onboarding

```yaml
---
name: client-onboard
description: Set up a new client project with all standard configurations
disable-model-invocation: true
---

Set up a new client project for: $0

1. Create directory structure:
   - clients/$0/
   - clients/$0/.claude/CLAUDE.md
   - clients/$0/src/
   - clients/$0/templates/
   - clients/$0/analytics/
   - clients/$0/reports/

2. Generate client CLAUDE.md with:
   - ESP configuration placeholders
   - Brand guidelines section
   - Sending schedule section
   - Contact information section

3. Create initial client intelligence file:
   - clients/$0/$0.md following the 6-category framework

4. Set up git branch: feature/$0-onboarding

5. Create initial n8n workflow templates for:
   - Subscriber welcome sequence
   - Campaign performance tracking
   - Weekly report generation

6. Add client to the master client list

7. Create PR with all onboarding changes
```

### Skill: Performance Audit

```yaml
---
name: perf-audit
description: Audit codebase for performance issues
context: fork
allowed-tools: Read, Grep, Glob, Bash
---

Perform a comprehensive performance audit of the codebase.

Check for:
1. **Database**: N+1 queries, missing indexes, unoptimized queries
2. **API**: Large payloads, missing pagination, slow endpoints
3. **Frontend**: Large bundle size, unnecessary re-renders, blocking resources
4. **Memory**: Memory leaks, large object retention, circular references
5. **Caching**: Missing cache layers, stale cache, cache invalidation issues
6. **Concurrency**: Race conditions, deadlocks, inefficient async patterns

For each finding, provide:
- Location (file + line)
- Current behavior
- Impact assessment (high/medium/low)
- Recommended fix with code example
- Estimated improvement

Save report to PERFORMANCE-AUDIT.md
```

### Skill: Security Scan

```yaml
---
name: security-scan
description: Scan codebase for security vulnerabilities
context: fork
agent: Explore
---

Perform a thorough security scan of the codebase.

Check for:
1. **Injection**: SQL injection, XSS, command injection, LDAP injection
2. **Authentication**: Weak password handling, missing auth checks, session issues
3. **Authorization**: Missing access controls, privilege escalation paths
4. **Data exposure**: Secrets in code, sensitive data in logs, PII leaks
5. **Dependencies**: Known vulnerabilities in dependencies (check package-lock.json)
6. **Configuration**: Insecure defaults, debug mode in production, CORS misconfiguration
7. **Cryptography**: Weak algorithms, hardcoded keys, insecure random

For each finding:
- Severity: Critical / High / Medium / Low / Informational
- Location: file + line number
- Description of the vulnerability
- Exploitation scenario
- Recommended fix with code example
- CWE reference number

Save report to SECURITY-AUDIT.md
```

---

## Advanced Subagent Configurations

### Subagent: Full-Stack Developer

```markdown
---
name: fullstack-dev
description: Full-stack development specialist. Use for features spanning frontend and backend.
tools: Read, Write, Edit, Bash, Grep, Glob
model: opus
memory: project
isolation: worktree
---

You are a senior full-stack developer. When implementing features:

1. Start by understanding the full request and existing architecture
2. Plan the changes across frontend and backend
3. Implement backend changes first (API, database, services)
4. Then implement frontend changes (components, state, styling)
5. Write tests for both layers
6. Run the full test suite
7. Commit with conventional commit messages

Architecture notes:
- Check your agent memory for project patterns before starting
- Follow existing code patterns -- never introduce new frameworks without approval
- Always handle errors at both API and UI layers
- Write integration tests, not just unit tests
```

### Subagent: Documentation Writer

```markdown
---
name: doc-writer
description: Technical documentation specialist. Use proactively when code changes affect APIs or user-facing features.
tools: Read, Write, Edit, Grep, Glob
model: sonnet
memory: project
---

You are a technical writer specializing in developer documentation.

When writing documentation:
1. Read the code to understand what it actually does (not just what comments say)
2. Write clear, concise documentation with practical examples
3. Include:
   - Overview and purpose
   - Installation/setup steps
   - API reference with parameters, return values, and examples
   - Common use cases
   - Troubleshooting section
4. Follow the existing documentation style in the project
5. Update the table of contents if one exists

Save any discovered patterns to your agent memory for consistency.
```

### Subagent: Database Analyst (Read-Only)

```markdown
---
name: db-analyst
description: Database analysis specialist. Execute read-only queries for reports and analysis.
tools: Bash
permissionMode: dontAsk
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: ".claude/hooks/validate-readonly-query.sh"
---

You are a database analyst with read-only access.

When analyzing data:
1. Identify relevant tables and their relationships
2. Write efficient SELECT queries with appropriate filters and indexes
3. Present results clearly with context and interpretation
4. Suggest data-driven recommendations

You cannot modify data. If asked to INSERT, UPDATE, DELETE, or modify schema,
explain that you only have read access and suggest who to contact.
```

### Subagent: Email Template Builder

```markdown
---
name: email-builder
description: HTML email template specialist. Use for building and debugging newsletter templates.
tools: Read, Write, Edit, Bash, Grep, Glob
model: sonnet
mcpServers:
  - playwright:
      type: stdio
      command: npx
      args: ["-y", "@playwright/mcp@latest"]
---

You are an expert HTML email developer. You specialize in building
newsletter templates that render correctly across all email clients.

When building templates:
1. Use table-based layouts for maximum compatibility
2. Inline all CSS styles (no external stylesheets)
3. Support dark mode with @media (prefers-color-scheme: dark)
4. Include alt text for all images
5. Set preheader text
6. Use web-safe fonts with fallbacks
7. Test at multiple widths (320px, 480px, 600px)

Problematic patterns to avoid:
- Flexbox/Grid (Outlook doesn't support them)
- Background images (spotty support)
- Interactive elements (most clients strip JavaScript)
- External fonts (Gmail strips @font-face)

Use Playwright to preview the rendered email in a browser and
take screenshots at different viewport widths.
```

---

## Real-World Practitioner Tips (from YouTube)

These tips are synthesized from the most-watched Claude Code tutorials and practitioner videos on YouTube in 2025-2026, including "Master 80% of Claude Code in 26 Minutes" (WCuwYLVE6j8), "The ONLY Claude Code Tutorial You'll Ever Need in 2026" (LlFgLsffbBs), "800+ hours of Learning Claude Code in 8 minutes" (Ffh9OeJ7yxw), "How Claude Code Hooks Save Me HOURS Daily" (Q4gsvJvRjCU), and "Building Claude Code with Boris Cherny" (julbw1JuAz0).

### Tip 1: Start Every Project with /init

Run `/init` immediately on any new project. Let Claude analyze the codebase and generate CLAUDE.md, then refine it. The AI-generated starting point catches things you'd forget to document.

### Tip 2: The "5-Minute Context Rule"

If you've been working on something for 5 minutes without clearing context, and you're about to switch topics, `/clear` first. Context pollution from the old topic actively hurts the new task.

### Tip 3: CLAUDE.md as a Living Document

Treat CLAUDE.md like a wiki, not a config file. Every time Claude does something wrong, add a rule. Every time Claude does something right that surprised you, document the pattern. Review monthly and prune.

### Tip 4: Use Subagents for Everything Long-Running

Any task that will produce a lot of output (test suites, code reviews, codebase exploration) should be delegated to a subagent. The main context stays clean and focused on your current task.

### Tip 5: The Two-Session Workflow

Run two Claude Code sessions simultaneously:
- Session 1: Implementation (making changes)
- Session 2: Review (reading and verifying changes from Session 1)

This catches mistakes that a single session misses because it's not biased toward code it just wrote.

### Tip 6: Hooks Are Your Best Friend

The most productive Claude Code users have 5-10 hooks configured:
- Notification on idle (so you know when to come back)
- Auto-format on file edit
- Lint check on file edit
- Block dangerous commands
- Audit logging
- Tests on stop

### Tip 7: Named Sessions for Everything

Never leave a session unnamed. Use `/rename` or `claude -n` every time. Future you will thank present you when trying to resume work.

### Tip 8: Use Claude Code for Non-Code Tasks

Claude Code is excellent for tasks beyond code:
- Writing and editing documentation
- Analyzing CSV data and generating reports
- Creating and debugging n8n/automation workflows
- Managing Obsidian vaults and knowledge bases
- Drafting client communications
- Generating and reviewing email campaigns

### Tip 9: The Obsidian + Claude Code Stack

Many practitioners use Obsidian as their knowledge base with Claude Code as the executor:
- Notes become context via `@` references
- Claude writes back analysis results to the vault
- YAML frontmatter in Obsidian notes feeds into Claude Code skills
- The vault becomes a persistent "second brain" for Claude

(Referenced from "Obsidian + AI: How to Do It The Right Way" - a1FDaoF8Jog, "How I Use Obsidian + Claude Code to Run My Life" - 6MBq1paspVU)

### Tip 10: Cost Management

- Use `--effort low` for simple tasks (saves tokens)
- Use subagents with `model: haiku` for exploration (cheapest)
- Set `--max-budget-usd` in CI/CD pipelines
- Monitor with ccflare or Usage Monitor
- Use `/compact` proactively before context gets expensive
- `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=50` for earlier compaction

### Tip 11: The Batch Skill for Large Migrations

For large-scale changes (migrating frameworks, updating APIs across many files), use the built-in `/batch` skill:

```
/batch migrate src/ from Solid to React
```

This researches the codebase, decomposes work into 5-30 independent units, presents a plan, then spawns one background agent per unit in isolated worktrees. Each implements, tests, and opens a PR.

### Tip 12: MCP Servers Are a Game-Changer

The practitioners who get the most value from Claude Code are those who connect it to their full tool stack via MCP: Slack, Notion, GitHub, databases, ESPs. Claude Code becomes a central hub that can read from and write to every tool you use.

(Referenced from "5 MCP Servers That Make Claude Code 10x More Powerful" - M5CsRj6zSCA, "Claude Code MCP: How to Add MCP Servers" - DfWHX7kszQI)

### Tip 13: Subagent Teams for Complex Debugging

When a bug is hard to pin down, spawn 3-5 subagents each investigating a different hypothesis. Have them share findings and disprove each other. The theory that survives is likely the root cause.

(Referenced from "Claude Code Subagents are Absolutely Insane" - sNI18nzwgn8, "Claude Code NEW Sub Agents in 7 Minutes" - DNGxMX7ym44)

### Tip 14: Hooks for CLI Tool Enforcement

Use PreToolUse hooks to force Claude to use specific CLI tools rather than CLAUDE.md instructions (which are advisory). For example, force `pnpm` instead of `npm`:

```bash
#!/bin/bash
COMMAND=$(jq -r '.tool_input.command' < /dev/stdin)
if echo "$COMMAND" | grep -q '^npm '; then
  jq -n '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: "Use pnpm instead of npm"
    }
  }'
  exit 0
fi
exit 0
```

(Referenced from "How to actually force Claude Code to use the right CLI" - 3CSi8QAoN-s)

### Tip 15: Executive Assistant Mode

Claude Code can function as an executive assistant when connected to Calendar, Gmail, and Slack via MCP:
- Draft responses to emails
- Schedule meetings based on availability
- Send Slack messages
- Generate weekly summaries

(Referenced from "Turn Claude Code Into Your Executive Assistant in 27 Mins" - mi4hcipESKQ)

---

## Complete Environment Variable Reference

### Core Environment Variables

| Variable | Description |
|----------|-------------|
| `CLAUDE_CODE_EFFORT_LEVEL` | Default effort: `low`, `medium`, `high` |
| `CLAUDE_CODE_DISABLE_AUTO_MEMORY` | Set to `1` to disable auto memory |
| `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` | Set to `1` to disable background tasks |
| `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD` | Set to `1` to load CLAUDE.md from `--add-dir` dirs |
| `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` | Override auto-compaction threshold (e.g., `50`) |
| `MAX_THINKING_TOKENS` | Limit thinking budget (e.g., `10000`) |
| `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING` | Set to `1` to revert Opus/Sonnet 4.6 to fixed thinking budget |
| `CLAUDE_CODE_NEW_INIT` | Set to `true` for interactive multi-phase `/init` |
| `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` | Set to `1` to enable agent teams |
| `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` | Override SessionEnd hooks timeout (default: 1500ms) |
| `CLAUDE_CODE_REMOTE` | Set to `"true"` in web sessions |
| `CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS` | Remove built-in git workflow instructions |
| `SLASH_COMMAND_TOOL_CHAR_BUDGET` | Override skill description budget |
| `ANTHROPIC_MODEL` | Override default model |

### Provider Environment Variables

| Variable | Description |
|----------|-------------|
| `ANTHROPIC_API_KEY` | API key for Anthropic |
| `ANTHROPIC_BASE_URL` | Custom API base URL |
| `CLAUDE_CODE_USE_BEDROCK` | Use Amazon Bedrock |
| `CLAUDE_CODE_USE_VERTEX` | Use Google Cloud Vertex AI |

### Environment Variables via Settings

Set environment variables in `settings.json` so they apply to every session:

```json
{
  "env": {
    "CLAUDE_CODE_EFFORT_LEVEL": "high",
    "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50",
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

---

## Complete Keyboard Shortcut Reference

| Shortcut | Action |
|----------|--------|
| `Esc` | Stop Claude mid-action |
| `Esc + Esc` | Open rewind menu |
| `Shift+Tab` | Cycle permission modes (Normal -> Auto-Accept -> Plan) |
| `Ctrl+G` | Open plan in text editor |
| `Ctrl+O` | Toggle verbose mode (see thinking) |
| `Ctrl+B` | Background current task |
| `Ctrl+T` | Toggle task list (agent teams) |
| `Option+T` / `Alt+T` | Toggle extended thinking |
| `Shift+Down` | Cycle through teammates (agent teams) |
| `Enter` | Send message / confirm |
| `Ctrl+C` | Cancel current input |

### Session Picker Shortcuts

| Shortcut | Action |
|----------|--------|
| `Up/Down` | Navigate between sessions |
| `Left/Right` | Expand/collapse grouped sessions |
| `Enter` | Select and resume |
| `P` | Preview session content |
| `R` | Rename session |
| `/` | Search/filter sessions |
| `A` | Toggle current dir / all projects |
| `B` | Filter to current git branch |
| `Esc` | Exit picker |

---

## Complete Slash Command Reference

### Built-In Commands

| Command | Purpose |
|---------|---------|
| `/init` | Generate/improve CLAUDE.md |
| `/memory` | View/edit memory files and toggle auto memory |
| `/clear` | Reset context window |
| `/compact [instructions]` | Compress context with optional focus |
| `/permissions` | Manage tool permissions |
| `/agents` | Manage subagents (view, create, edit, delete) |
| `/hooks` | View configured hooks |
| `/config` | Open settings interface |
| `/model` | Change model and effort level |
| `/effort [level]` | Set effort level |
| `/statusline` | Configure custom status line |
| `/context` | Check context usage and loaded files |
| `/btw <question>` | Quick side question (no context cost) |
| `/rename <name>` | Name current session |
| `/resume [name]` | Resume a previous session |
| `/rewind` | Restore previous checkpoint |
| `/branch` | Fork current session |
| `/desktop` | Transfer to Desktop app |
| `/teleport` | Pull web session into terminal |
| `/sandbox` | Enable OS-level sandboxing |
| `/bug` | Report a bug |
| `/plugin` | Browse plugin marketplace |
| `/fast` | Toggle fast mode |
| `/voice` | Toggle voice dictation |

### Bundled Skills (Slash Commands)

| Skill | Purpose |
|-------|---------|
| `/batch <instruction>` | Large-scale parallel changes across codebase |
| `/claude-api` | Load Claude API reference for your language |
| `/debug [description]` | Troubleshoot current session |
| `/loop [interval] <prompt>` | Run prompt repeatedly on interval |
| `/simplify [focus]` | Review recent changes for quality/efficiency |

---

## Troubleshooting

### Claude Isn't Following CLAUDE.md

1. Run `/memory` to verify files are loaded
2. Check location is correct (see loading rules)
3. Make instructions more specific
4. Look for conflicting instructions across files
5. Check file isn't too long (>200 lines = reduced adherence)
6. Use `--append-system-prompt` for critical rules that must be in system prompt

### Context Degradation

Signs: Claude "forgets" instructions, makes more mistakes, produces lower-quality output.

Fix:
1. `/clear` and start fresh
2. Write a better initial prompt incorporating what you learned
3. Use subagents for research to keep main context clean
4. Set `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=50` for earlier auto-compaction

### Instructions Lost After /compact

CLAUDE.md fully survives compaction (re-read from disk). If instruction disappeared, it was conversation-only. Add to CLAUDE.md to persist.

### CLAUDE.md Too Large

Move detailed content to:
- `@path` imports for reference files
- `.claude/rules/` for modular instructions
- Skills for on-demand knowledge

### MCP Server Connection Issues

```bash
# Check configured servers
claude mcp list

# Remove and re-add
claude mcp remove <name>
claude mcp add <name> -- <command> [args...]

# Debug mode
claude --debug "mcp"
```

### Hooks Not Running

1. Check `/hooks` to see if registered
2. Verify script is executable (`chmod +x`)
3. Test script manually: `echo '{}' | .claude/hooks/my-hook.sh`
4. Check `disableAllHooks` isn't set
5. Use `--debug "hooks"` for verbose logging

### Session Won't Resume

- Sessions are per-project directory
- Check `claude --resume` for the session picker
- Sessions within the same git repo appear in the picker
- Use `claude auth status` to verify authentication

---

## Quick Reference Card

### Most-Used Commands

```bash
claude                          # Start interactive session
claude -p "prompt"              # Non-interactive query
claude -c                       # Continue last session
claude --resume name            # Resume named session
claude --worktree feature       # Isolated worktree session
claude --agent my-agent         # Run as specific agent
claude --effort high            # High-effort session
claude --model opus             # Use Opus model
claude --add-dir ../shared      # Add directory access
claude -p --output-format json  # JSON output
```

### Most-Used Slash Commands

```
/init                # Generate/improve CLAUDE.md
/memory              # View/edit memory files
/clear               # Reset context
/compact             # Compress context
/permissions         # Manage tool permissions
/agents              # Manage subagents
/hooks               # View configured hooks
/batch <task>        # Parallel batch operations
/simplify            # Review recent changes
/debug               # Troubleshoot session
/btw <question>      # Quick side question (no context cost)
/rename <name>       # Name current session
/rewind              # Restore previous checkpoint
/effort              # Set effort level
/statusline          # Configure status line
```

### Context Management Cheat Sheet

| Situation | Action |
|-----------|--------|
| Switching topics | `/clear` |
| Context getting full | `/compact Focus on X` |
| Need to research | Use subagent |
| Quick question | `/btw` |
| Part of conversation irrelevant | `/rewind` + "Summarize from here" |
| Long session degrading | `/clear` + better initial prompt |
| Need to remember across /compact | Put it in CLAUDE.md |

### The 30-Second Setup Checklist

1. `curl -fsSL https://claude.ai/install.sh | bash`
2. `cd your-project && claude`
3. `/init` -- generate CLAUDE.md
4. `/permissions` -- allowlist safe commands
5. `/statusline` -- monitor context usage
6. Start working

---

## Resources & Further Reading

### Official Documentation
- Overview: https://code.claude.com/docs/en/overview
- Best Practices: https://code.claude.com/docs/en/best-practices
- Memory: https://code.claude.com/docs/en/memory
- Skills: https://code.claude.com/docs/en/skills
- Hooks: https://code.claude.com/docs/en/hooks
- MCP: https://code.claude.com/docs/en/mcp
- Subagents: https://code.claude.com/docs/en/sub-agents
- Agent Teams: https://code.claude.com/docs/en/agent-teams
- CLI Reference: https://code.claude.com/docs/en/cli-reference
- Common Workflows: https://code.claude.com/docs/en/common-workflows
- Settings: https://code.claude.com/docs/en/settings
- Permissions: https://code.claude.com/docs/en/permissions
- Plugins: https://code.claude.com/docs/en/plugins
- Remote Control: https://code.claude.com/docs/en/remote-control
- Chrome Extension: https://code.claude.com/docs/en/chrome
- GitHub Actions: https://code.claude.com/docs/en/github-actions
- Agent SDK: https://platform.claude.com/docs/en/agent-sdk/overview
- Full docs index: https://code.claude.com/docs/llms.txt

### Community Resources
- https://github.com/anthropics/claude-code (80.3k stars)
- https://github.com/hesreallyhim/awesome-claude-code (29.3k stars)
- https://github.com/VoltAgent/awesome-claude-code-subagents (14.4k stars)
- https://github.com/travisvn/awesome-claude-skills (9.3k stars)
- https://github.com/Mizoreww/awesome-claude-code-config
- https://github.com/rohitg00/awesome-claude-code-toolkit
- https://github.com/ccplugins/awesome-claude-code-plugins

### YouTube Channels & Videos Referenced
- "Master 80% of Claude Code in 26 Minutes" (WCuwYLVE6j8)
- "The ONLY Claude Code Tutorial You'll Ever Need in 2026" (LlFgLsffbBs)
- "800+ hours of Learning Claude Code in 8 minutes" (Ffh9OeJ7yxw)
- "My top 6 tips & ways of using Claude Code efficiently" (WwdIYp5fuxY)
- "How Claude Code Hooks Save Me HOURS Daily" (Q4gsvJvRjCU)
- "Claude Code hooks are Officially Awesome" (eFjqogpmNkQ)
- "I'm HOOKED on Claude Code Hooks: Advanced Agentic Coding" (J5B9UGTuNoM)
- "Claude Code MCP: How to Add MCP Servers (Complete Guide)" (DfWHX7kszQI)
- "5 MCP Servers That Make Claude Code 10x More Powerful" (M5CsRj6zSCA)
- "Claude Code Subagents are Absolutely Insane" (sNI18nzwgn8)
- "Claude Code NEW Sub Agents in 7 Minutes" (DNGxMX7ym44)
- "From Zero to Your First Agentic AI Workflow in 26 Minutes" (tDGiWn0flK8)
- "Building Claude Code with Boris Cherny" (julbw1JuAz0)
- "Mastering Claude Code in 30 minutes" (6eBSHbLKuN0)
- "Obsidian + AI: How to Do It The Right Way" (a1FDaoF8Jog)
- "How I Use Obsidian + Claude Code to Run My Life" (6MBq1paspVU)
- "Turn Claude Code Into Your Executive Assistant in 27 Mins" (mi4hcipESKQ)
- "Cursor vs Claude Code: Which is best?" (KW35wHNU7pY - Lex Fridman)
- "How to actually force Claude Code to use the right CLI" (3CSi8QAoN-s)
- "Claude Code is all you need in 2026" (0hdFJA-ho3c)

### Agent Skills Standard
- https://agentskills.io (open standard used by Claude Code)

---

*This guide synthesizes official Anthropic documentation (code.claude.com), the claude-code GitHub repository (80.3k stars), community resources (awesome-claude-code, awesome-claude-skills, awesome-claude-code-subagents), production configurations, and practitioner insights from YouTube. It will evolve as Claude Code continues to ship new features.*

*Note: YouTube transcript downloads were blocked during compilation. The practitioner tips section synthesizes insights from video titles, descriptions, and established community patterns. Future updates should download full transcripts for deeper extraction.*

---

## Day-in-the-Life: Agency Workflow with Claude Code

This section walks through a realistic day using Claude Code for newsletter growth agency work, showing how all the features connect.

### Morning: Check In and Prioritize

```bash
# Start the day by resuming yesterday's session
claude --resume "monday-planning"

# If starting fresh, name the session
claude -n "monday-mar-20"
```

```
Read @CLIENT-INTELLIGENCE-SUMMARY.md and @memory/session-log.md.
What are the top priorities for today across all clients?
```

### Mid-Morning: Client Campaign Work

```bash
# Switch to client-specific worktree
claude --worktree acme-campaign -n "acme-weekly-mar-20"
```

```
Read the client intelligence file at @clients/acme-corp/acme-corp.md.
We need to build the March 20 newsletter campaign.

1. Check the template at templates/acme/weekly.html for any needed updates
2. Review last week's performance data in analytics/acme/
3. Suggest subject line variations based on what's worked before
4. Validate the template for deliverability
```

**Use the newsletter-reviewer subagent for quality check:**
```
@"newsletter-reviewer (agent)" check templates/acme/weekly-mar-20.html
```

### Late Morning: Cross-Client Analytics

```bash
# Clear context before switching tasks
/clear
```

```
/client-report acme-corp
/client-report beta-inc
/client-report workweek
```

### Afternoon: Debugging a Deliverability Issue

```
One of our clients (daily-drop) is seeing a 40% drop in open rates.
Spawn an agent team to investigate:
- One teammate analyzing ESP deliverability metrics
- One teammate reviewing recent template changes
- One teammate checking sending reputation and authentication (SPF, DKIM, DMARC)
```

### Late Afternoon: Automation Work

```bash
/clear
claude -n "n8n-automation"
```

```
Read the n8n workflow at automations/daily-drop-bounce-handler.json.
The bounce rate threshold alert isn't triggering. Debug it and fix the
conditional logic. Test by simulating a 3% bounce rate.
```

### End of Day: Session Logging

```
Update memory/session-log.md with what we did today:
- Built and validated Acme March 20 campaign
- Generated weekly reports for 3 clients
- Investigated Daily Drop deliverability issue (root cause: authentication)
- Fixed n8n bounce handler automation

Flag for Sindy: Daily Drop needs SPF record updated by their dev team.
```

### Weekly: Batch Operations Across Clients

```
/batch update all client CLAUDE.md files to include the latest sending
schedule changes from @docs/q1-schedule-updates.md
```

### Monthly: Codebase Health Check

```
/simplify focus on code reuse across client modules
```

```
Use an agent team to audit all 19 client configurations:
- 4 teammates, each auditing ~5 clients
- Check for stale API keys, outdated templates, missing tracking pixels
- Report findings in a unified audit document
```

---

## Advanced MCP Patterns

### Chaining MCP Tools in a Single Prompt

```
Read the latest 5 messages from #internal-acme in Slack.
Check if any mention deliverability issues.
If so, look up the Acme campaign performance in Notion.
Draft a response in Slack with the data.
```

With Slack, Notion, and Gmail MCP servers connected, Claude orchestrates across all three tools in a single conversation.

### MCP for Meeting Prep

With Day.ai and Google Calendar MCP connected:

```
I have a meeting with Acme Corp in 30 minutes.
Pull the last meeting notes from Day.ai.
Check their latest campaign metrics.
Draft a meeting agenda based on open action items.
```

### MCP for Automated Reporting

```bash
# Non-interactive report generation
claude -p "Pull this week's campaign data from the Notion database, \
calculate week-over-week changes for all clients, and draft a \
summary Slack message for #agency-updates" --max-turns 20
```

### Custom MCP Server for Your ESP

If your ESP doesn't have an existing MCP server, you can build one:

```json
// .mcp.json
{
  "mcpServers": {
    "mailchimp": {
      "type": "stdio",
      "command": "node",
      "args": ["./tools/mailchimp-mcp-server.js"],
      "env": {
        "MAILCHIMP_API_KEY": "${MAILCHIMP_API_KEY}"
      }
    }
  }
}
```

---

## Advanced Obsidian Integration Patterns

### Bidirectional Obsidian Workflow

**Obsidian to Claude Code (knowledge in):**
```
Read @"/Users/jay/Documents/the vault/clients/acme/meeting-notes/2026-03-15.md"
and extract all action items. Create tasks for each one.
```

**Claude Code to Obsidian (knowledge out):**
```
Save the analysis we just did to an Obsidian note at
"/Users/jay/Documents/the vault/analysis/acme-q1-performance.md"

Use YAML frontmatter with:
  - tags: [acme, q1-2026, performance, newsletter]
  - date: 2026-03-20
  - status: complete
  - client: acme-corp

Include wiki-links to related notes like [[Acme Corp]] and [[Q1 2026 Goals]]
```

### Daily Notes Integration

```yaml
---
name: daily-note
description: Create or update today's daily note in Obsidian
disable-model-invocation: true
---

Read today's daily note at "/Users/jay/Documents/the vault/daily/$(date +%Y-%m-%d).md"

If it exists, append to the "Work Log" section.
If not, create it with this template:

---
date: $(date +%Y-%m-%d)
tags: [daily, work-log]
---

# $(date +"%A, %B %d, %Y")

## Tasks
- [ ]

## Work Log

## Notes

## End of Day Review

Then add the following to the Work Log section:
$ARGUMENTS
```

### Obsidian as a Prompt Library

Store complex prompts in Obsidian and reference them:

```
Run the prompt described in @"/Users/jay/Documents/the vault/prompts/client-audit.md"
for client acme-corp
```

### Knowledge Graph Updates

```
After analyzing the Acme Corp campaign data, update the relevant
Obsidian notes:

1. Update [[Acme Corp]] with latest metrics
2. Create a new note [[Acme Q1 2026 Campaign Analysis]]
3. Add backlinks from [[Newsletter Performance Tracking]]
4. Update the [[Client Dashboard]] MOC (Map of Content)
```

---

## Advanced n8n Integration Patterns

### Claude Code as n8n Node Designer

```
Design an n8n workflow that:
1. Triggers every Monday at 8am
2. Queries our PostgreSQL database for weekly subscriber metrics per client
3. For each client:
   a. Calculate week-over-week growth
   b. Flag any client with >5% churn
   c. Generate a summary block
4. Compile all summaries into a single Slack message
5. Post to #weekly-metrics
6. If any client is flagged, also DM the assigned GM

Output the complete n8n workflow JSON.
```

### Debugging n8n Executions

```bash
# Pipe n8n execution data into Claude for analysis
curl -s "https://n8n-instance.com/api/v1/executions?workflowId=123&limit=5" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" | \
  claude -p "Analyze these n8n execution results. Identify any failures, \
  explain root causes, and suggest fixes. Output as a structured report."
```

### n8n Webhook + Claude Code Automation

Set up an n8n webhook that triggers Claude Code for on-demand analysis:

```bash
# n8n webhook triggers this script
#!/bin/bash
# webhook-handler.sh
CLIENT=$1
METRIC=$2

claude -p "Analyze the $METRIC for client $CLIENT. \
Compare to last 4 weeks. If degrading, draft an alert message." \
  --output-format json --max-turns 5 > "/tmp/analysis-$CLIENT.json"
```

---

## Cost Optimization Strategies

### Token Usage by Activity

| Activity | Token Cost | Optimization |
|----------|-----------|-------------|
| Reading large files | High | Use subagents (separate context) |
| Running test suites | High | Use subagents; report only failures |
| Codebase exploration | High | Use Explore subagent (Haiku, fast) |
| Simple edits | Low | Direct prompts, no planning needed |
| Complex architecture | Medium-High | Plan Mode first, implement second |
| Batch operations | Very High | Fan out with `--max-turns` limits |

### Cost-Saving Patterns

1. **Use Haiku for exploration.** The built-in Explore subagent uses Haiku. Create custom subagents with `model: haiku` for any read-only investigation.

2. **Set budget limits in CI/CD.** Always use `--max-budget-usd` in automated pipelines:
   ```bash
   claude -p "review this PR" --max-budget-usd 2.00
   ```

3. **Early compaction.** Set `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=50` to compact at 50% capacity instead of 95%.

4. **Effort level management.** Use `--effort low` for simple tasks, `--effort high` only when needed:
   ```bash
   claude --effort low -p "rename this variable across the codebase"
   claude --effort high -p "design the authentication architecture"
   ```

5. **Use /btw for questions.** Zero context cost for quick lookups.

6. **Clear between tasks.** Don't let irrelevant context accumulate and pay for it with every response.

7. **Scope subagent tools.** Restrict tools to what's needed. Fewer tools = smaller prompt.

8. **Monitor with status line.** Install `/statusline` to see token usage in real time.

### Estimating Costs

- Track via ccflare (web dashboard) or Claude Code Usage Monitor (terminal)
- Use `--verbose` during development to see token counts
- Review session transcripts at `~/.claude/projects/{project}/{sessionId}/`

---

## Enterprise & Team Deployment

### Managed Settings for Organizations

Deploy organization-wide settings that cannot be overridden:

**macOS:** `/Library/Application Support/ClaudeCode/managed-settings.json`
**Linux/WSL:** `/etc/claude-code/managed-settings.json`
**Windows:** `C:\Program Files\ClaudeCode\managed-settings.json`

```json
{
  "permissions": {
    "deny": [
      "Bash(curl *)",
      "Bash(wget *)",
      "Read(.env*)",
      "Read(secrets/**)"
    ]
  },
  "forceLoginMethod": "claudeai",
  "forceLoginOrgUUID": "your-org-uuid",
  "allowManagedPermissionRulesOnly": true,
  "allowManagedMcpServersOnly": true,
  "allowedMcpServers": [
    { "serverName": "github" },
    { "serverName": "slack" }
  ],
  "deniedMcpServers": [
    { "serverName": "filesystem" }
  ],
  "companyAnnouncements": [
    "Welcome to TFM! Review our code guidelines at docs.thefeed.media",
    "All PRs require review before merge"
  ]
}
```

### Team Onboarding Checklist

1. Deploy managed settings and managed CLAUDE.md
2. Set up project-level `.claude/settings.json` with team permissions
3. Create shared skills in `.claude/skills/` and commit to git
4. Create shared subagents in `.claude/agents/` and commit to git
5. Configure `.mcp.json` with team MCP servers
6. Document team CLAUDE.md conventions in a wiki
7. Set up CI/CD integration with Claude Code for PR reviews

### Attribution Settings

Control how Claude Code attributes its contributions:

```json
{
  "attribution": {
    "commit": "Generated with Claude Code",
    "pr": ""
  }
}
```

Set `includeCoAuthoredBy: false` to remove the co-authored-by byline (deprecated in favor of `attribution`).

---

## Voice Dictation

Claude Code supports push-to-talk voice dictation for hands-free input:

```
/voice
```

Configure in settings:
```json
{
  "voiceEnabled": true,
  "language": "english"
}
```

Useful for:
- Describing bugs while looking at another screen
- Brainstorming architecture while away from keyboard
- Quick questions without typing

---

## Output Styles

Customize how Claude responds:

```json
{
  "outputStyle": "Explanatory"
}
```

Available styles affect the system prompt to adjust verbosity, formatting, and communication style.

---

## Frequently Asked Questions

### General

**Q: How much does Claude Code cost?**
A: Claude Code requires either a Claude Pro/Team/Enterprise subscription (claude.ai) or an Anthropic Console account (API billing). Subscription users get included usage; Console users pay per-token. Use `--max-budget-usd` in CI/CD to cap costs.

**Q: Does Claude Code send my code to Anthropic?**
A: Claude Code sends conversation context (including file contents it reads) to Anthropic's API for processing. Data usage policies are at code.claude.com/docs/en/data-usage. Anthropic does not use feedback for model training.

**Q: Can I use Claude Code with Amazon Bedrock or Google Vertex?**
A: Yes. Set `CLAUDE_CODE_USE_BEDROCK=1` or `CLAUDE_CODE_USE_VERTEX=1` with appropriate credentials. See official docs for provider-specific configuration.

**Q: What models can I use?**
A: Default depends on your subscription. You can switch with `--model sonnet`, `--model opus`, `--model haiku`, or a full model ID. Use `/model` to change mid-session.

### CLAUDE.md

**Q: How long should my CLAUDE.md be?**
A: Under 200 lines. Longer files reduce adherence because important rules get lost. Move detailed content to `.claude/rules/`, `@` imports, or skills.

**Q: Does CLAUDE.md survive /compact?**
A: Yes. CLAUDE.md is re-read from disk after compaction. Only conversation-only instructions are lost.

**Q: Can I have multiple CLAUDE.md files?**
A: Yes. Put them in parent directories, subdirectories, or use `.claude/rules/` for modular instructions. Subdirectory CLAUDE.md files load on demand when Claude reads files there.

**Q: Why isn't Claude following my CLAUDE.md?**
A: Run `/memory` to verify it's loaded. Check for conflicts between multiple CLAUDE.md files. Make instructions more specific. If the file is too long, Claude may deprioritize some rules.

### Hooks

**Q: Can hooks modify Claude's input or output?**
A: PreToolUse hooks can modify tool parameters via `updatedInput`. PostToolUse hooks can modify MCP tool output via `updatedMCPToolOutput`. Hooks can also inject `additionalContext` into Claude's awareness.

**Q: What happens if a hook script crashes?**
A: Non-zero exit codes (except 2) are treated as non-blocking errors. Stderr is shown in verbose mode. Claude continues execution. Only exit code 2 blocks the action.

**Q: Can I use hooks to auto-approve everything?**
A: Technically yes, via PreToolUse hooks that return `permissionDecision: "allow"`. But this is equivalent to `--dangerously-skip-permissions` and carries the same risks. Use specific patterns instead of blanket approvals.

### Subagents & Agent Teams

**Q: Can subagents spawn other subagents?**
A: No. Subagents cannot spawn other subagents. If you need nested delegation, chain subagents from the main conversation or use skills.

**Q: How many subagents can run in parallel?**
A: There's no hard limit, but each subagent consumes tokens independently. 3-5 is practical for most tasks. More than that and coordination overhead outweighs benefits.

**Q: When should I use agent teams vs subagents?**
A: Use subagents when workers just need to report back results. Use agent teams when workers need to communicate with each other, challenge findings, or coordinate on shared tasks.

**Q: Do agent teams cost more?**
A: Yes, significantly. Each teammate is a separate Claude instance with its own context window. Token usage scales linearly with team size.

### MCP

**Q: Can I build my own MCP server?**
A: Yes. MCP is an open standard. Build servers using the MCP SDK (available in Python, TypeScript, and other languages). See modelcontextprotocol.io for the specification.

**Q: Do MCP servers run locally or remotely?**
A: Both. `stdio` transport runs a local process. `http`, `sse`, and `ws` transports connect to remote servers.

**Q: Can I give different MCP servers to different subagents?**
A: Yes. Use the `mcpServers` field in subagent frontmatter to scope servers. Inline definitions keep MCP tools out of the main conversation entirely.

### Sessions & Context

**Q: How long do sessions persist?**
A: Sessions persist for 30 days by default (configurable via `cleanupPeriodDays`). They're stored locally and can be resumed anytime within that window.

**Q: What's the difference between /clear and /compact?**
A: `/clear` completely resets the context window (fresh start). `/compact` summarizes and compresses the existing context, preserving key information while freeing space.

**Q: Can I share a session with a teammate?**
A: Sessions are local to your machine. You can share the transcript files or use the Desktop app's session features, but there's no built-in multi-user session sharing.

### Worktrees

**Q: Do I need to install anything extra for worktrees?**
A: No. Git worktrees are a built-in Git feature. Claude Code's `--worktree` flag automates the creation and cleanup.

**Q: What happens to my worktree if Claude Code crashes?**
A: The worktree persists on disk at `<repo>/.claude/worktrees/<name>`. Clean up manually with `git worktree remove`.

**Q: Can I use worktrees with SVN or Mercurial?**
A: Yes. Configure `WorktreeCreate` and `WorktreeRemove` hooks to provide custom VCS logic. These replace the default git behavior when you use `--worktree`.

---

## Glossary

| Term | Definition |
|------|-----------|
| **Agentic loop** | The cycle where Claude reads, plans, acts, and verifies autonomously |
| **Auto memory** | Notes Claude writes for itself across sessions, stored in `~/.claude/projects/<project>/memory/` |
| **CLAUDE.md** | Markdown file with persistent instructions loaded every session |
| **Compaction** | Process of summarizing conversation to free context space |
| **Context window** | The total amount of text (conversation + files + outputs) Claude can hold at once |
| **DCT** | Dynamic Creative Testing -- one concept per ad set in Meta Ads |
| **Effort level** | Controls how deeply Claude thinks before responding (low/medium/high/max) |
| **Extended thinking** | Claude's internal reasoning process before producing a response |
| **Hook** | Shell command, HTTP call, prompt, or agent that runs at specific lifecycle points |
| **MCP** | Model Context Protocol -- open standard for connecting AI tools to external data |
| **Permission mode** | Controls how Claude handles approval for actions (normal/auto-accept/plan/bypass) |
| **Plan Mode** | Read-only mode where Claude analyzes without making changes |
| **Skill** | Reusable workflow or knowledge defined in SKILL.md, loaded on demand |
| **Subagent** | Specialized AI assistant running in its own context window |
| **Agent team** | Multiple Claude Code instances coordinating with shared tasks and messaging |
| **Worktree** | Isolated copy of a git repository for parallel work without file conflicts |
| **Plugin** | Bundle of skills, hooks, subagents, and MCP servers installable as a unit |
| **Status line** | Customizable display showing context usage, model info, and other metrics |
| **Checkpoint** | Snapshot of conversation and code state that can be restored |
| **ESP** | Email Service Provider (Mailchimp, SendGrid, Klaviyo, etc.) |
| **CPL** | Cost Per Lead -- key metric in newsletter growth |
| **CVR** | Conversion Rate -- percentage of landing page visitors who subscribe |

---

## Claude Code for Non-Developers

Claude Code is not just for software engineers. As a newsletter growth agency, many of the most powerful use cases involve non-code work. Here are patterns for using Claude Code outside traditional development.

### Content Analysis and Writing

```bash
# Analyze newsletter content for engagement patterns
cat newsletters/acme-q1/*.html | claude -p "Analyze these 12 newsletters. \
Which subject lines had the highest open rates? What content topics drove \
the most clicks? What writing patterns should we replicate?"

# Draft newsletter copy
claude -p "Write 5 subject line variations for Acme Corp's March newsletter \
about cloud computing trends. Their voice is professional but approachable. \
Never use exclamation marks. Previous best performer: \
'The 3 Cloud Trends Your CFO Needs to Know'"
```

### Competitive Research

```
Search the web for the top 10 newsletter growth agencies. For each:
1. What services do they offer?
2. What pricing models do they use?
3. What differentiates them?

Compile findings into a competitive analysis note at
"/Users/jay/Documents/the vault/research/competitive-analysis-mar-2026.md"
```

### Client Communication Drafts

```
Draft a proactive update email to the Acme Corp team about their
Q1 newsletter performance. Include:
- Key metrics (pull from @clients/acme-corp/analytics/q1-summary.json)
- Wins to celebrate
- Areas for improvement
- Recommended next steps for Q2

Tone: confident, data-driven, collaborative. Not salesy.
```

### Meeting Prep and Follow-Up

With Day.ai and Google Calendar MCP servers connected:

```
I have a call with the Workweek team in 20 minutes.
1. Pull the last meeting notes from Day.ai
2. Check their campaign performance from the last 2 weeks
3. List any open action items
4. Draft a 3-bullet agenda

After the meeting:
Update the session log with decisions made and new action items.
```

### Spreadsheet and Data Processing

```bash
# Process a CSV export
cat subscriber-export.csv | claude -p "Clean this subscriber data: \
remove duplicates by email, standardize date formats to YYYY-MM-DD, \
flag any rows with missing required fields. Output as clean CSV."

# Generate reports from raw data
cat campaign-results.json | claude -p "Generate a formatted markdown \
report with tables showing: campaign name, sends, opens, clicks, \
unsubscribes, and revenue. Calculate rates. Highlight top 3 and bottom 3."
```

### Process Documentation

```
I just finished onboarding a new client (ExampleCo). Document the
process I followed as a repeatable SOP. Include:
1. Initial setup steps
2. ESP integration checklist
3. Creative brief template
4. First campaign launch checklist
5. Reporting setup

Save to /docs/sops/client-onboarding.md in a format that Sindy
can follow independently.
```

---

## Performance Benchmarks and Expectations

### What Claude Code Does Well

| Task | Expected Quality | Notes |
|------|-----------------|-------|
| Reading and explaining code | Excellent | Understands most languages and frameworks |
| Writing tests | Very good | Follows existing patterns, catches edge cases |
| Bug fixing with error messages | Very good | Especially when given reproduction steps |
| Multi-file refactoring | Good to very good | Better with clear scope and patterns |
| PR creation and description | Very good | Generates meaningful descriptions |
| Code review | Good | Catches common issues, misses some domain-specific concerns |
| Architecture design | Good | Better as co-pilot than sole designer |
| CSS/UI implementation | Good | Better when given screenshots or design references |
| Database queries | Good | Validate against production data carefully |
| n8n/automation workflows | Good | JSON output may need manual validation |

### What Requires More Supervision

| Task | Watch For | Mitigation |
|------|-----------|-----------|
| Complex state management | Race conditions, stale state | Thorough test cases |
| Security-sensitive code | Auth bypasses, injection | Security-focused subagent review |
| Performance-critical paths | Inefficient algorithms | Performance benchmarks |
| Database migrations | Data loss, breaking changes | Always review before running |
| Client-facing communications | Tone mismatches, incorrect data | Human review before sending |
| Production deployments | Missing steps, wrong environments | Use hooks to enforce checklists |

### Context Window Capacity Guidelines

| Task Complexity | Context Usage | Recommended Approach |
|----------------|--------------|---------------------|
| Simple edit (1-2 files) | ~5% | Direct prompt |
| Feature (5-10 files) | ~20-40% | Plan + implement |
| Large refactor (20+ files) | 60-80% | Subagents for research, `/batch` for changes |
| Codebase audit | 80%+ | Agent team, each auditing a subset |
| Full-stack feature | 40-60% | Worktree isolation, phased approach |

---

## Changelog

| Date | Changes |
|------|---------|
| March 2026 | Major expansion: 4000+ lines. Added complete hook events reference, advanced hook recipes, advanced skill recipes, advanced subagent configurations, day-in-the-life workflow, cost optimization, enterprise deployment, FAQ, glossary. Sourced from official docs and 20+ YouTube practitioner videos. |
| March 2026 (initial) | Original 1400-line guide compiled from official docs and community resources |
