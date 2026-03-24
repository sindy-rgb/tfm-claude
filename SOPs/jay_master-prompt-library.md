# The Feed Media — Master Prompt Library

---

## PROMPT 1: FULL CLIENT ANALYSIS
*Use in a fresh claude.ai chat, one client at a time*

```
Analyze all Day AI meeting recordings, the relevant Slack channels, and the Notion database for [CLIENT NAME].

**Sources to pull:**
1. Day AI — all meeting recordings tagged to this client
2. Slack — internal channel (#internal-[client]) AND external channel (#[client-channel])
3. Notion — search for "[CLIENT NAME]" to find: (a) the main client page, (b) Kick-off Call Template, (c) Onboarding Document, (d) Creative Playbook, (e) Client OS if present

**Notion parsing sequence:**
- Step 1: Find client page in the Clients database
- Step 2: Extract from properties: contact, GM, ESP, funnel type, Slack channels, "how client makes money," KPI focus
- Step 3: Fetch Onboarding/Kickoff doc — extract audience segments (with verbatim client quotes), dream outcomes, problems, personas, funnel structure, KPI definition
- Step 4: Fetch Creative Playbook — extract DO list, DON'T list, emotional drivers
- Step 5: Scan Concepts database for angle patterns and any comments
- Step 6: Note all blank/incomplete fields as intelligence gaps

**Synthesize into the 6-category Client Intelligence framework:**
1. CLIENT OVERVIEW — contacts, stakeholders, status, links
2. NORTH STAR METRIC — primary KPI + target, quality definition, client quote; flag CPL-only clients
3. BRAND VOICE RULES — NEVER rules first, approved language, one quote on failed copy
4. WINNING CREATIVE SIGNALS — top 2-3 formats with performance + client reaction
5. NEGATIVE TRIGGERS — most charged client quote first, then patterns, specific kills
6. RELATIONSHIP HEALTH — sentiment trend, outreach timing, continuity risk, creative involvement

Then write the full context to their Day AI org record titled "[CLIENT NAME] — Client Intelligence (Updated [Month Year])".

Finally, output the complete formatted intelligence as markdown so I can save it locally.
```

---

## PROMPT 2: NOTION-ONLY PARSE
*Use when you need just the Notion layer without re-running full analysis*

```
Parse the Notion database for [CLIENT NAME] and extract all client-specific intelligence.

Step 1 — Find client page: Search Notion for "[CLIENT NAME]" to find the main client record under the Clients database. Fetch the full page.

Step 2 — Extract from properties: contact name(s), GM assigned, ESP, ad account type, funnel type, kickoff date, Slack channels (internal + external), "explain how client makes money," "KPI focus," Win vs Lost creative links.

Step 3 — Fetch Onboarding/Kickoff doc: Find "Kick-off Call Template" or "Onboarding Document" or "Client OS" for this client. Extract: audience segments (all, with verbatim client quotes), dream outcomes, problems, objections, failed solutions, benefits, personas, funnel structure, primary KPI, content pillars.

Step 4 — Fetch Creative Playbook: Find "Client-Specific Playbooks" section. Extract: DO list, DON'T list, emotional drivers, language the audience connects with.

Step 5 — Scan Concepts database: Patterns in brainstormed angles, any hooks with comments. Note any with feedback suggesting edits or approvals.

Step 6 — Flag gaps: List any section that was blank (KPI focus, client playbook, bi-weekly notes, etc.)

Output only client-specific content — no Notion boilerplate, no template instructions, no empty fields.
Format as markdown sections matching the 6-category framework.
```

---

## PROMPT 3: CLAUDE PROJECT MEMORY SETUP
*Run once per client in their dedicated Claude Project*

```
You are setting up this Claude Project with client intelligence. Do the following in order:

1. Use the Day AI search_objects tool to find the organization record for the client this project is about. Search native_organization by name matching the project name.

2. Once you have the org record, search for any native_context attached to that org where the title contains "Client Intelligence."

3. Read the full content of that context note.

4. Using only what's in that context, create exactly 6 memory entries using memory_user_edits with the add command — one for each category below. Each entry has a 500-character limit, so prioritize ruthlessly using these rules:

   - CLIENT OVERVIEW: contact name + email, key internal stakeholders, active status, link to Day AI analysis page
   - NORTH STAR METRIC: primary KPI + target number, how they define quality, one direct quote if it fits
   - BRAND VOICE RULES: lead with the hardest NEVER rules first, then approved language, then one client quote on copy that failed
   - WINNING CREATIVE SIGNALS: top 2-3 proven formats with what makes them work — skip specific DCT numbers if space is tight
   - NEGATIVE TRIGGERS: lead with the most emotionally charged client quote about what failed, then the patterns to avoid
   - RELATIONSHIP HEALTH: sentiment trend, optimal outreach timing, biggest continuity risk, creative involvement preference

5. Confirm all 6 entries were added and show me a summary of what was stored.

If no Client Intelligence context exists yet for this client in Day AI, tell me — the analysis must run first before memory can be set up.
```

---

## PROMPT 4: CLAUDE CODE SESSION STARTUP (SINGLE CLIENT)
*Paste at start of Claude Code session for focused client work*

```
Read the following files before responding to anything:
- /the-feed-media/clients/[CLIENT-NAME].md
- /the-feed-media/system/framework.md

You are a performance creative strategist for The Feed Media. You have full client intelligence loaded. Do not fetch any external data — work entirely from the local files unless I explicitly ask you to.

The client is [CLIENT NAME]. What would you like to work on?
```

---

## PROMPT 5: CLAUDE CODE SESSION STARTUP (CROSS-CLIENT)
*For pattern analysis, competitive intelligence, or portfolio-level work*

```
Read all files in /the-feed-media/clients/ and /the-feed-media/system/framework.md.

You are a performance creative strategist for The Feed Media with full portfolio intelligence loaded. Do not fetch any external data.

[Your task here]
```

---

## PROMPT 6: LOCAL FILE UPDATE AFTER NEW ANALYSIS
*Paste into Claude Code after completing a new analysis in claude.ai*

```
I've completed a new client intelligence analysis for [CLIENT NAME]. The updated content is below.

Please:
1. Open /the-feed-media/clients/[client-name].md
2. Replace the full content with the updated intelligence below
3. Update the "Last Updated" header to [current month/year]
4. Confirm the file is saved

[PASTE UPDATED INTELLIGENCE HERE]
```

---

## CLIENT ANALYSIS PROMPTS (All 14 Active Clients)

### CREATOR SPOTLIGHT (beehiiv)
```
Analyze all Day AI meeting recordings, Slack channels, and Notion database for Creator Spotlight (beehiiv). Pull Day AI + #internal-creatorspotlight + #[external channel] + Notion. Also search Notion for any pages related to this client including onboarding docs, ICP definitions, brand voice guidelines, or strategy documents. Synthesize into the 6-category Client Intelligence framework. Write to Day AI org record titled "Creator Spotlight — Client Intelligence (Updated March 2026)". Output full markdown for local file.
```

### WORKWEEK
```
Analyze all Day AI meeting recordings, Slack channels, and Notion database for Workweek. Pull Day AI + #internal-workweek + #thefeed-workweekgrowth + Notion. Also search Notion for any pages related to this client. Synthesize into the 6-category Client Intelligence framework. Write to Day AI org record titled "Workweek — Client Intelligence (Updated March 2026)". Output full markdown for local file.
```

### INSIGHT LINKS
```
Analyze all Day AI meeting recordings, Slack channels, and Notion database for Insight Links. Pull Day AI + relevant Slack channels + Notion. Also search Notion for any pages related to this client including the Brand Voice - InsightLinks page. Synthesize into the 6-category Client Intelligence framework. Write to Day AI org record titled "Insight Links — Client Intelligence (Updated March 2026)". Output full markdown for local file.
```

### STATUS (NEWS)
```
Analyze all Day AI meeting recordings, Slack channels, and Notion database for Status (News). Pull Day AI + relevant Slack channels + Notion. Also search Notion for any pages related to this client. Synthesize into the 6-category Client Intelligence framework. Write to Day AI org record titled "Status — Client Intelligence (Updated March 2026)". Output full markdown for local file.
```

### STOCKS.NEWS
```
Analyze all Day AI meeting recordings, Slack channels, and Notion database for Stocks.News. Pull Day AI + relevant Slack channels + Notion. Also search Notion for any pages related to this client. Synthesize into the 6-category Client Intelligence framework. Write to Day AI org record titled "Stocks.News — Client Intelligence (Updated March 2026)". Output full markdown for local file.
```

### THE POINTS GUY
```
Analyze all Day AI meeting recordings, Slack channels, and Notion database for The Points Guy. Pull Day AI + relevant Slack channels + Notion. Also search Notion for any pages related to this client. Synthesize into the 6-category Client Intelligence framework. Write to Day AI org record titled "The Points Guy — Client Intelligence (Updated March 2026)". Output full markdown for local file.
```

### HOUCK
```
Analyze all Day AI meeting recordings, Slack channels, and Notion database for Houck (Founding Journey). Pull Day AI + relevant Slack channels + Notion (including the Kick-off Call Template Houck page at https://www.notion.so/2aef4a126e068099b975e8926c231e48 and the Houck client page at https://www.notion.so/29af4a126e06803f8092cc7b57410bcc). Also search Notion for any pages related to this client. Synthesize into the 6-category Client Intelligence framework. Write to Day AI org record titled "Houck — Client Intelligence (Updated March 2026)". Output full markdown for local file.
```

### RNT FITNESS
```
Analyze all Day AI meeting recordings, Slack channels, and Notion database for RNT Fitness. Pull Day AI + #internal-rntfitness + #thefeed-rntfitness + Notion (including the RNT Fitness client page at https://www.notion.so/2fbf4a126e06807d9f9fd1083c25c55a). Also search Notion for any pages related to this client. Synthesize into the 6-category Client Intelligence framework. Write to Day AI org record titled "RNT Fitness — Client Intelligence (Updated March 2026)". Output full markdown for local file.
```

### DAILY DROP
```
Analyze all Day AI meeting recordings, Slack channels, and Notion database for Daily Drop. Pull Day AI + relevant Slack channels + Notion. Also search Notion for any pages related to this client. Synthesize into the 6-category Client Intelligence framework. Write to Day AI org record titled "Daily Drop — Client Intelligence (Updated March 2026)". Output full markdown for local file.
```

### OPEN SOURCE CEO
```
Analyze all Day AI meeting recordings, Slack channels, and Notion database for Open Source CEO. Pull Day AI + relevant Slack channels + Notion. Also search Notion for any pages related to this client. Synthesize into the 6-category Client Intelligence framework. Write to Day AI org record titled "Open Source CEO — Client Intelligence (Updated March 2026)". Output full markdown for local file.
```

### JAY SHETTY
```
Analyze all Day AI meeting recordings, Slack channels, and Notion database for Jay Shetty. Pull Day AI + relevant Slack channels + Notion. Also search Notion for any pages related to this client. Synthesize into the 6-category Client Intelligence framework. Write to Day AI org record titled "Jay Shetty — Client Intelligence (Updated March 2026)". Output full markdown for local file.
```

### HOW TO AI
```
Analyze all Day AI meeting recordings, Slack channels, and Notion database for How to AI. Pull Day AI + relevant Slack channels + Notion. Also search Notion for any pages related to this client. Synthesize into the 6-category Client Intelligence framework. Write to Day AI org record titled "How to AI — Client Intelligence (Updated March 2026)". Output full markdown for local file.
```

### POINTS PATH
```
Analyze all Day AI meeting recordings, Slack channels, and Notion database for Points Path. Pull Day AI + relevant Slack channels + Notion. Also search Notion for any pages related to this client. Synthesize into the 6-category Client Intelligence framework. Write to Day AI org record titled "Points Path — Client Intelligence (Updated March 2026)". Output full markdown for local file.
```

### EXPERIENTIAL HOSPITALITY
```
Analyze all Day AI meeting recordings, Slack channels, and Notion database for Experiential Hospitality (EH). Pull Day AI + #eh-ads-nr-thefeed + #internal-experientialhospitality + Notion (Experiential Hospitality page: https://www.notion.so/261f4a126e06808c8af9f5b0c4890c05). Contacts: Isaac French, Weston Hudspeth. Also search Notion for any pages related to this client. Synthesize into the 6-category Client Intelligence framework. Write to Day AI org record titled "Experiential Hospitality — Client Intelligence (Updated March 2026)". Output full markdown for local file.
```

### QUARTZ
```
Analyze all Day AI meeting recordings, Slack channels, and Notion database for Quartz. Pull Day AI + relevant Slack channels + Notion. Also search Notion for any pages related to this client. Synthesize into the 6-category Client Intelligence framework. Write to Day AI org record titled "Quartz — Client Intelligence (Updated March 2026)". Output full markdown for local file.
```

### HOUCK (ALTERNATE SHORT VERSION)
See full version above.
