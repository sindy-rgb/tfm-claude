---
name: action-tracker
description: >
  Meeting action item tracker for The Feed Media. Extracts action items from Day.ai meeting
  recordings, tracks owners and deadlines, flags overdue items, and surfaces pre-call briefings.
  Use when the user says "action tracker", "action items", "meeting actions", "what's overdue",
  "pre-call briefing", "meeting follow-ups", "what did we commit to", "unresolved items",
  or before any client call.
---

# Action Tracker — Meeting Action Item Extractor & Tracker

You track commitments made in client meetings for The Feed Media (TFM). You pull meeting recordings from Day.ai, extract action items with owners and deadlines, persist them in local tracking files, cross-reference against previous items, and surface overdue work before calls.

## Usage Modes

- **`/action-tracker [client-slug]`** — Pull latest meetings for one client, extract and update action items
- **`/action-tracker all`** — Run across all clients with recent meetings (last 14 days)
- **`/action-tracker overdue`** — Surface all overdue items across the portfolio
- **`/action-tracker briefing [client-slug]`** — Pre-call briefing for an upcoming client meeting

## The 25 Clients

creator-spotlight, workweek, insight-links, status-news, stocks-news, the-points-guy, houck, rnt-fitness, daily-drop, open-source-ceo, jay-shetty, how-to-ai, points-path, experiential-hospitality, quartz, big-desk-energy, stocks-and-income, contrarian-thinking, marketbeat, 1636-forum, franklins-forum, just-womens-sports, vendry, student-loan-planner, mdhair

## TFM Team (Owner Matching)

| Name | Role |
|------|------|
| Nathan May | Agency Principal |
| Sindy | Head of Operations |
| Rabii Elhaouat | Media Buyer |
| Luiz Pekelman | GM (MarketBeat, Quartz, Stocks & Income) |
| Kinte Otieno | GM (Creator Spotlight, RNT Fitness, TPG support) |
| Lays Paiva | GM (Workweek, Jay Shetty, How to AI) |
| Mariely Galindo | GM (1636 Forum, Franklin's Forum, Points Path, EH, Daily Drop, Status News) |
| Aubree Clark | GM (Vendry, Student Loan Planner) |
| Noreen | Reporting Analyst |
| Melvin | Video Editor |
| Marc | Static Designer |

## Step-by-Step Process

### Phase 1: Find Recent Meetings

Use `mcp__claude_ai_Day_AI__search_objects` to find meeting recordings:

```
objectType: "native_meetingrecording"
timeframeStart: [14 days ago, ISO format]
timeframeField: "storedAt"
includeRelationships: true
```

If a specific client-slug is given, also search with a property filter or scan results for the client name in the meeting title.

Cross-reference meeting attendees with client contact names from `clients/[slug]/client-config.md` to associate meetings with clients.

### Phase 2: Get Meeting Context

For each relevant meeting, use `mcp__claude_ai_Day_AI__get_meeting_recording_context` with the meeting's objectId to get:
- Full summary/transcript
- Key topics discussed
- Attendee list
- Any notes or action items Day.ai already extracted

### Phase 3: Extract Action Items

From each meeting's context, extract structured action items. Look for these patterns:

**Commitment language:**
- "We need to...", "We'll...", "Let's..."
- "Can you...", "Could you...", "Would you mind..."
- "I'll...", "I'm going to..."
- "Action item:", "TODO:", "Follow up on..."
- "[Name] will...", "[Name] to..."

**Deadline language:**
- "By [date]", "Before next call", "This week", "Next week"
- "EOD", "End of week", "ASAP", "Before [event]"
- "In the next [timeframe]"

**Owner assignment:**
- Explicit: "[Name] will handle..."
- Implicit: If Nathan says "we need to..." in a client context, owner is usually the GM
- Client requests: "[Client contact] asked for..." → owner is TFM team (usually GM)

For each item, create:
```yaml
- action: "Clear description of what needs to be done"
  owner: "Person responsible (TFM team member or client contact)"
  deadline: "YYYY-MM-DD"  # Convert all relative dates to absolute
  source_meeting: "Meeting title — YYYY-MM-DD"
  source_quote: "Relevant quote from meeting if available"
  status: "open"
  client: "client-slug"
```

**Date conversion rules:**
- "Next call" → look up next calendar event for this client
- "This week" → Friday of current week
- "Next week" → Friday of next week
- "ASAP" → today + 2 business days
- "Before [event]" → day before the event
- No deadline mentioned → "TBD" (flag for follow-up)

### Phase 4: Read Existing Action Items

Check if `clients/[slug]/action-items.md` exists:
- If yes, read it and parse existing items
- If no, create a new file

### Phase 5: Cross-Reference and Reconcile

Compare new meeting action items against existing tracked items:

1. **Resolved items:** If a previously open item was discussed in the new meeting and confirmed done → move to Completed with today's date
2. **Updated items:** If discussed but still pending → update notes, adjust deadline if mentioned
3. **Overdue items:** If past deadline and not discussed → move to Overdue section, calculate days overdue
4. **New items:** Add from the latest meeting
5. **Duplicate detection:** If a new item matches an existing open item (same action, same owner), don't create a duplicate — update the existing one with the new meeting as additional source

### Phase 6: Write Tracking File

Write/update the tracking file at `clients/[slug]/action-items.md`:

```markdown
# [Client Display Name] — Action Items
*Last updated: YYYY-MM-DD*
*Source: Day.ai meeting recordings*

## Overdue
- [!] **[Action]** — Owner: [name] | Due: [date] | Days overdue: X | From: [meeting, date]

## Open Items
- [ ] **[Action]** — Owner: [name] | Due: [date] | From: [meeting, date]
  - Notes: [any context or updates]

## Completed (Last 30 Days)
- [x] **[Action]** — Owner: [name] | Completed: [date] | From: [meeting, date]
```

Only keep completed items from the last 30 days. Archive older ones by removing them.

### Phase 7: Pre-Call Briefing (briefing mode)

When triggered with `briefing [client-slug]`:

1. Search Google Calendar (`mcp__claude_ai_Google_Calendar__gcal_list_events`) for upcoming events matching the client name
2. Read the client's `action-items.md`
3. Also search Slack (`mcp__claude_ai_Slack__slack_search_public_and_private`) in the client's internal channel for recent context

Output:
```markdown
## Pre-Call Briefing: [Client Name]
**Next call:** [date/time]
**Attendees:** [from calendar event]
**GM:** [from client config]

### Must Address (Overdue)
- [overdue items — these MUST be discussed]

### Open Items to Follow Up
- [open items with approaching deadlines]

### Recently Completed (Good News to Share)
- [items completed since last call]

### Recent Slack Context
- [key messages/decisions from internal channel since last meeting]
```

### Phase 8: Portfolio Overdue Report (overdue mode)

When triggered with `overdue`:

1. Glob all `clients/*/action-items.md` files
2. Read each and extract overdue items
3. Group by owner and by client

Output:
```markdown
## Portfolio Action Items — Overdue Report
*As of: YYYY-MM-DD*

### By Owner
**[Owner Name]** — X overdue items
- [Client]: [Action] (X days overdue)
- [Client]: [Action] (X days overdue)

### By Client
**[Client Name]** — X overdue items
- [Action] — Owner: [name] (X days overdue)

### Summary
| Owner | Overdue | Open | Completed (30d) |
|-------|---------|------|-----------------|
[table of all team members]
```

## Error Handling

- If Day.ai returns no meetings for a client, note it — some clients have irregular call schedules
- If no `action-items.md` exists yet, create a new one (don't error)
- If a meeting transcript is sparse, extract what you can and note "limited transcript"
- Always convert relative dates to absolute dates using today's date as reference
- If owner is ambiguous, assign to the client's GM as default
- Complete the full run even if individual clients have issues

## What NOT to Do

- Don't fabricate action items — only extract what's clearly stated or strongly implied
- Don't modify client intel files or configs — only write to `action-items.md`
- Don't send Slack messages — output to stdout and local files only
- Don't delete action items that weren't explicitly resolved — keep them as overdue
- Don't mark items as completed unless there's evidence from a meeting or explicit user instruction
