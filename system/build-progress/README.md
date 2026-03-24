# State Files — GSD Context Management

State files persist context across Claude Code sessions so work doesn't get lost between conversations.

## How It Works

- Each major initiative gets its own state file in this directory (e.g., `skills-build.md`, `friday-autopilot-build.md`)
- State files use structured markdown with consistent sections
- Sub-agents should **read** the relevant state file at the start of work and **update** it when done

## State File Structure

Every state file should include these sections:

```
# [Initiative Name]
**Last updated:** YYYY-MM-DD
**Owner:** [who's driving this]

## Current Status
One-paragraph summary of where things stand.

## Work Items
| Item | Status | Notes |
|------|--------|-------|
| ...  | not started / in progress / blocked / done | ... |

## Blockers
- What's preventing progress, if anything

## Decisions Made
- Key decisions with dates so future sessions don't relitigate them

## Next Steps
- Ordered list of what to do next

## Relevant Files
- Paths to files this initiative touches
```

## Rules

1. **Read before writing.** Always check the state file before starting work on an initiative.
2. **Update on milestones.** Don't update on every minor change, but do update when you complete a meaningful step, hit a blocker, or make a decision.
3. **One file per initiative.** Don't combine unrelated work streams. If a task is a sub-task of a larger initiative, track it in the parent file.
4. **Use sub-agents for isolation.** Large tasks (building a full skill, refactoring many files) should run in sub-agents that read the state file, do the work, and write back results. This protects main session context.
