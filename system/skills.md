# The Feed Media — Skills Library (Slash Commands)

Master skills definitions for Claude Chat client projects. Each command uses variables from the client's config file (`client-config.md`). Commands are generic — they work across all 19 clients when the config is populated.

---

## `/friday` — Weekly Friday Ad Report

**Description:** Generate the weekly Friday ad performance report for posting to the client-facing Slack channel.

**Required Config Variables:**
- `{client_name}`, `{meta_account_id}`, `{campaign_ids}`
- `{esp}`, `{esp_api_access}` (if available)
- `{partner_dashboard_url}`, `{partner_dashboard_metrics}` (if applicable)
- `{kpi_primary}`, `{kpi_target}`, `{cpl_target}`
- `{report_format}`, `{report_destination}`, `{report_owner}`
- `{slack_internal}`, `{slack_external}`, `{notion_page_url}`
- `{competitor_name}`, `{competitor_campaign_ids}` (if applicable)
- `{never_rules}` (to avoid recommending killed creative or banned angles)
- `{monthly_budget}`, `{budget_pacing_target}`

**Execution Steps:**

1. **Read the client's `{slack_external}` channel** (last 3-4 Friday reports) to learn the established report format, tone, and structure for this specific client. The report MUST match the format the client is used to receiving. Do NOT use a generic template — mirror the actual format from recent posts.

2. **Read `{slack_internal}`** (last 7-10 days) for:
   - Recent creative decisions (paused, launched, killed ads and WHY)
   - Client requests or feedback that affect messaging
   - Any context that should be referenced in the report (e.g., new LPs, budget changes, compliance issues)
   - Active threads about creative pipeline or next steps

3. **Read the client intelligence file** (`{client_intel_path}`) and `{never_rules}` to ensure:
   - No killed or banned creatives are recommended for scaling
   - Budget figures are current
   - Relationship context informs tone (e.g., prove-it phase = data-heavy, strong relationship = more casual)

4. **Pull Meta Ads data** for the trailing 7 days using Pipeboard MCP:
   - Account: `{meta_account_id}`
   - TFM Campaigns: `{campaign_ids}`
   - Competitor Campaigns: `{competitor_campaign_ids}` (if applicable)
   - Metrics: spend, leads, CPL, CTR, CPC, CPM, impressions, LP views
   - Breakdowns: by ad set and by ad (top performers)

5. **Pull n8n ROAS reports from `{slack_internal}`** (if available):
   - These are the source of truth for revenue metrics (ROAS, Rev/User, confirmed sales, SMS opt-ins)
   - Use the most recent MTD report as the basis, NOT Pipeboard pixel data alone
   - For clients with competitor comparison (e.g., MarketBeat vs GrowJoy), pull both reports

6. **Pull ESP / partner dashboard data** (if `{esp_api_access}` = true or `{partner_dashboard_url}` exists):
   - Metrics defined in `{partner_dashboard_metrics}`

7. **Draft the report matching `{report_format}`:**

   If `{report_format}` specifies a custom format, follow it exactly. Otherwise use:

   **Default format (internal, for clients without established external format):**
   ```
   # {client_name} — Weekly Ad Report
   **Week of:** [Monday] – [Friday]
   **Prepared by:** The Feed Media

   ## Performance Summary
   | Metric | This Week | Last Week | WoW Change |
   |--------|-----------|-----------|------------|
   | Spend | $ | $ | % |
   | Leads | | | % |
   | CPL | $ | $ | % |
   | CTR | % | % | pts |
   | CPC | $ | $ | % |
   | CPM | $ | $ | % |

   ## vs. Target
   - KPI ({kpi_primary}): [actual] vs. {kpi_target} — [ON TRACK / AT RISK / OFF TRACK]
   - CPL: [actual] vs. {cpl_target} — [status]

   ## Creative Highlights
   **Top 3 by CPL:**
   1. [Ad name] — $X.XX CPL, X leads, X% CTR
   2. [Ad name] — $X.XX CPL, X leads, X% CTR
   3. [Ad name] — $X.XX CPL, X leads, X% CTR

   ## What We Changed This Week
   - [Paused/launched/scaled actions taken]

   ## What We're Testing Next Week
   - [Upcoming creative, targeting, or budget changes]
   ```

   **IMPORTANT:** For clients where `{report_owner}` is specified, the draft should be written in that person's voice and style, ready for them to review and post. Do NOT generate a report that looks like it came from a different person than who posts it.

8. **Compliance check before output:**
   - Verify NO recommended creatives or angles appear in `{never_rules}`
   - Verify budget figures match `{monthly_budget}` / `{budget_pacing_target}`
   - Verify no killed ads are recommended for reactivation or scaling
   - Verify tone matches client relationship health (from intelligence file)

9. **Output:** Draft ready for `{report_owner}` to review and post to `{report_destination}`.

**Memory Storage:** After running, save this week's top-line numbers (spend, leads, CPL, ROAS, Rev/User if available) to memory for next week's comparison. Note any creatives paused or launched, and any client feedback received.

---

## `/bi-weekly` — Pre-Call Notion Document Builder

**Description:** Build the Notion document the GM screen-shares during the bi-weekly client call. This is a PRESENTATION DOC prepared BEFORE the meeting — not a post-call recap. The GM drives the screen, narrates each section, and pauses for client questions.

**Required Config Variables:**
- `{client_name}`, `{client_display_name}`
- `{meta_account_id}`, `{campaign_ids}`
- `{kpi_primary}`, `{kpi_target}`, `{cpl_target}`
- `{slack_internal}`, `{slack_external}`
- `{notion_page_url}` (client hub — bi-weekly docs live here)
- `{gm_name}` (Growth Manager assigned)
- `{esp}`, `{esp_api_access}` (if available)
- `{never_rules}`

**Execution Steps:**

1. **Read the 2 most recent bi-weekly Notion docs for this client** to match the exact format, section order, level of detail, and visual structure. The doc MUST look like what came before. Do NOT invent a new format.

2. **Read `{slack_internal}` and `{slack_external}`** (since last bi-weekly call) for:
   - Creative decisions (launched, paused, killed, scaled)
   - Client feedback or requests
   - Performance discussions
   - Any open action items from the last call — check if they were completed
   - Anything the client raised that should be on the agenda

3. **Pull Meta Ads data** for the trailing 14 days (bi-weekly period) using Pipeboard:
   - Account: `{meta_account_id}`, Campaigns: `{campaign_ids}`
   - Metrics: spend, leads, CPL, CTR, CVR, CPM, qualified leads (if trackable)
   - Breakdowns: by ad set and by ad (top performers)

4. **Pull ESP / qualification data** (if `{esp_api_access}` = true or n8n spreadsheet is operational):
   - Qualified lead counts, qualification rate, qualified CPL per segment/newsletter
   - If not available, note "Qualified data pending" and use most recent available numbers with the date

5. **Build the Notion document in this structure:**

   **Section 1: Agenda**
   - 2-4 bullet points of what will be discussed
   - Identify from Slack activity, performance changes, and open action items since last call

   **Section 2: What We Know** (toggle section)
   - **Bold headline summary** — 1-2 lines capturing the key takeaway for the period
   - **Cost KPIs (14 days)** — Per segment/newsletter (if applicable) or account-level:
     Spend, Leads, CPL, CTR, CVR, Qualified Leads
   - **Insights** — 3-5 analytical bullets interpreting the data (not just "what" but "why" and "so what")
   - **Qualification Data** — Per segment qualified count + qualified CPL + qualification rate + period-over-period comparison
   - **Roadblocks / Concerns** — Flag issues needing discussion (optional — omit if none)
   - **Next steps** — Forward-looking action items pre-populated before the call

   **Section 3: Winning Angles**
   - Top 3 performing angles/formats with names
   - For each: specific DCT(s) with creative preview links + Performance metrics (CTR, CVR, CPL, Qualified Leads if available)
   - Present in 3-column layout matching previous docs

   **Section 4: Observations on Formats**
   - Callout box with 3-5 bullets on creative format learnings
   - What's working and why, fatigue signals, cross-segment patterns

   **Section 5: New Creatives Breakdown** (if new creatives launched since last call)
   - New DCTs with early performance signals
   - Creative previews + metrics

   **Section 6: Winning Hooks**
   - Table: Hook | Type | Notes
   - Top hooks from the last 14 days by CPL

   **Section 7: To Explore**
   - Link to Concept Database and Designer Briefs inline views

   **Section 8: Meeting Notes**
   - Leave EMPTY — filled during/after the call

6. **Compliance check before output:**
   - Verify no killed/banned creatives appear in Winning Angles or recommendations
   - Verify qualified lead data is included (if available) — most clients care about quality, not just CPL
   - Verify the doc structure matches previous bi-weekly docs for this client

**How the GM uses this doc on the call:**
- Screen-shares and narrates — the client watches, not reads along
- Spends most time on creative performance (Section 3) and qualification/down-funnel data (Section 2.4)
- Nathan's framing: "The less interesting part is ad account metrics. The interesting part is what creative is working and why, plus down-funnel qualified leads."
- After structured sections, GM opens the floor for client questions — the best client ideas often come here
- The doc should be built to present well on screen

**Memory Storage:** After the call, save action items, decisions, and any intelligence updates. Note what sections got the most client engagement for future doc optimization.

---

## `/recap` — Post-Call Meeting Recap

**Description:** Process a client meeting recording from Day.ai, extract action items and decisions, and draft follow-up messages for the client-facing Slack channel, internal Slack channel, and the Meeting Notes section of the bi-weekly Notion doc.

**Required Config Variables:**
- `{client_name}`, `{client_display_name}`
- `{day_ai_search_term}` (how the client appears in Day.ai)
- `{contacts}` (key stakeholders with names and roles)
- `{kpi_primary}`, `{kpi_target}`
- `{slack_internal}`, `{slack_external}`
- `{client_intel_path}` (path to client intelligence .md file)
- `{gm_name}` (Growth Manager assigned)

**Execution Steps:**

1. **Find the meeting recording:**
   - Search Day.ai for the most recent meeting with `{day_ai_search_term}`
   - If multiple recent meetings, pick the one closest to today
   - Read the full transcript

2. **Extract structured notes:**
   - **Action items** — with owner (TFM team member or client contact), deadline if mentioned
   - **Key decisions** — anything agreed upon that changes strategy, budget, creative direction, or KPIs
   - **Client sentiment** — tone, energy, concerns raised, satisfaction signals
   - **New KPI targets** — any adjustments to `{kpi_primary}`, CPL targets, budget
   - **Strategy shifts** — new angles, audience segments, LP changes, ESP changes
   - **Creative feedback** — specific ads praised, killed, or requested

3. **Draft client-facing recap for `{slack_external}`:**
   Match the GM's established recap format. Read the last 2-3 recaps in `{slack_external}` to match tone and structure. Default format:
   ```
   Meeting Recap — TFM <> {client_display_name} | [Date]

   Next steps / Action items
   - @[client contact] to [action] by [deadline]
   - @[gm] to [action] by [deadline]
   - @[other owner] to [action] by [deadline]

   Key takeaways
   - [3-5 bullet points of what was discussed and decided]

   Decisions made
   - [Specific decisions that change strategy, budget, targeting, or creative direction]
   ```

4. **Draft internal recap for `{slack_internal}`:**
   ```
   📋 **{client_display_name} Bi-Weekly Recap — [Date]**

   **Attendees:** [names]
   **Sentiment:** [Positive / Neutral / Concerned / At Risk]

   **Decisions:**
   - [bullet points]

   **Action Items:**
   - [Owner]: [action] — due [date]

   **Intel Updates Needed:**
   - [Any flags for client intelligence file changes]

   **Next Call:** [date]
   ```

5. **Update the Meeting Notes section** of the most recent bi-weekly Notion doc with action items, decisions, and key takeaways from the call.

6. **Check for intelligence updates:**
   - Compare extracted info against the 6-category framework in `{client_intel_path}`
   - Flag changes to: contacts, KPIs, brand voice rules, creative signals, negative triggers, relationship health
   - Show the diff before writing: "PROPOSED UPDATE: [category] — [old] → [new]"
   - Only write updates after confirmation

**Output:** Three drafts:
1. Client-facing recap for `{slack_external}` (ready for GM to review and post)
2. Internal recap for `{slack_internal}`
3. Meeting Notes update for the bi-weekly Notion doc

**Memory Storage:** Save action items with owners and deadlines. Note sentiment trend. Flag any intelligence file updates that were or need to be made.

---

## `/status` — Quick Client Health Check

**Description:** Generate a 3-5 line health check formatted for a DM to Nathan. Answer first, data second.

**Required Config Variables:**
- `{client_name}`, `{client_display_name}`
- `{meta_account_id}`, `{campaign_ids}`
- `{kpi_primary}`, `{kpi_target}`, `{cpl_target}`
- `{monthly_budget}`, `{budget_pacing_target}`
- `{client_intel_path}`
- `{relationship_health}` (from intel file)

**Execution Steps:**

1. **Pull latest 7 days of Meta Ads performance:**
   - Account: `{meta_account_id}`, Campaigns: `{campaign_ids}`
   - Key metrics: spend, leads, CPL, CTR

2. **Compare to targets:**
   - CPL vs. `{cpl_target}` — calculate % over/under
   - Spend vs. `{budget_pacing_target}` — on pace for monthly budget?
   - `{kpi_primary}` vs. `{kpi_target}` if measurable

3. **Check intelligence file for risks:**
   - Read `{client_intel_path}`
   - Pull relationship health, negative triggers, continuity risks
   - Check for stale creative (no new ads launched in 10+ days)
   - Check for missing reports (Friday report not posted this week)

4. **Surface risks:**
   - Spend pacing off by >10%
   - CPL above target by >15%
   - No new creative in 10+ days
   - Missing Friday report
   - Relationship health flagged as "At Risk"
   - Any open action items overdue

5. **Output in Nathan's format (answer first, data second):**
   ```
   **{client_display_name}:** [ON TRACK / WATCH / AT RISK]
   [One sentence summary — the answer]
   CPL: $X.XX ({cpl_target} target) | Spend: $X.XK of {monthly_budget} | CTR: X.X%
   [Risk flag if any, or "No flags."]
   ```

**Memory Storage:** None — this is a read-only status check.

---

## `/creative-brief` — Generate Creative Brief

**Description:** Generate a structured creative brief using the client's winning signals, brand voice, and top-performing ad data.

**Required Config Variables:**
- `{client_name}`, `{client_display_name}`
- `{meta_account_id}`, `{campaign_ids}`
- `{client_intel_path}`
- `{brand_voice_tone}`, `{never_rules}`, `{approved_language}`
- `{audience_segments}` (ICPs from intel file)
- `{landing_page_urls}` (active LPs)
- `{dct_naming_prefix}` (e.g., "DCT_" for naming new concepts)
- `{next_dct_number}` (next available DCT number)

**Execution Steps:**

1. **Pull winning creative signals from `{client_intel_path}`:**
   - Top formats with performance data
   - Mechanisms that drive results (why they work)
   - Client-validated angles

2. **Pull top 3 performing ads from Meta:**
   - Sort by CPL (lowest) from the last 30 days
   - For each: ad name, primary text, headline, description, format (image/video/carousel), CPL, CTR, leads
   - Identify patterns: hooks, emotional triggers, CTAs, formats

3. **Generate the creative brief:**
   ```
   # Creative Brief — {client_display_name}
   **Date:** [today]
   **DCT Name:** {dct_naming_prefix}{next_dct_number}_[Concept Name]

   ## Angle / Hook
   [1-2 sentences describing the core angle and why it should work, referencing winning signals]

   ## Target Audience
   [Which ICP segment from {audience_segments} this targets and why]

   ## Primary Text Variants (3)
   1. [Variant — different hook, same angle]
   2. [Variant — different hook, same angle]
   3. [Variant — different hook, same angle]

   ## Headline Variants (2)
   1. [Headline]
   2. [Headline]

   ## Description Variants (2)
   1. [Description]
   2. [Description]

   ## CTA Recommendation
   [Recommended CTA button + rationale]

   ## Format Recommendation
   [Static image / Video / Carousel — with rationale based on winning signals]

   ## Landing Page
   [Which LP from {landing_page_urls} to use and why]

   ## Compliance Check
   - [ ] Does NOT violate any NEVER rules: {never_rules}
   - [ ] Matches brand voice tone: {brand_voice_tone}
   - [ ] No unapproved claims or language
   ```

4. **Flag violations:**
   - If any generated copy would violate a NEVER rule, flag it immediately with the specific rule
   - If the angle conflicts with negative triggers from the intel file, flag it

**Memory Storage:** Save the DCT number used and concept name. Note that `{next_dct_number}` should be incremented for next brief.

---

## `/prep {meeting_type}` — Meeting Prep

**Description:** Prepare for a meeting with Nathan (1:1), a client call, or an internal team sync.

**Required Config Variables:**
- `{client_name}`, `{client_display_name}`
- `{meta_account_id}`, `{campaign_ids}`
- `{kpi_primary}`, `{kpi_target}`, `{cpl_target}`
- `{monthly_budget}`
- `{contacts}` (for client prep)
- `{day_ai_search_term}`
- `{gm_name}`, `{media_buyer_name}`
- `{client_intel_path}`
- `{slack_internal}`

**Meeting Types:**

### `/prep nathan` — 1:1 with Nathan

1. Pull last 7 days Meta performance
2. Search Day.ai for last meeting with Nathan about this client — extract outstanding action items
3. Search `{slack_internal}` for last 7 days — any escalations or flags
4. Format as exception-based update:
   ```
   **{client_display_name} Update for Nathan**

   **Bottom line:** [One sentence — is this client on track or not, and why]

   **What's off track (if anything):**
   - [Issue] — [Plan to fix] — [Timeline]

   **What's working:**
   - [Brief wins — only if Nathan would care]

   **Open items from last meeting:**
   - [ ] [Action item] — [Status: Done / In Progress / Blocked]

   **Decision needed (if any):**
   - [Question for Nathan with recommended answer]
   ```

### `/prep client` — Client Call

1. Pull last 14 days Meta performance (to cover full bi-weekly period)
2. Search Day.ai for last client meeting — extract outstanding action items
3. Pull ESP data if available
4. Read `{client_intel_path}` for relationship health and recent concerns
5. Format with "tell them how to feel about the information":
   ```
   **{client_display_name} Call Prep — [Date]**

   **Performance Summary (Last 2 Weeks):**
   | Metric | Period | vs. Target | Narrative |
   |--------|--------|------------|-----------|
   | CPL | $X.XX | {cpl_target} | [Good/Concerning — why] |
   | Spend | $X.XK | {monthly_budget} pace | [On track / Ahead / Behind] |
   | Leads | X,XXX | — | [Context] |

   **Talking Points:**
   1. [Lead with the best news — frame the narrative]
   2. [Address any concerns proactively — don't wait for them to ask]
   3. [Creative update — what's new, what's coming]
   4. [Ask for what you need from them]

   **Outstanding Action Items:**
   - [From last call — status update for each]

   **Landmines to Avoid:**
   - [Anything from negative triggers or recent sentiment that could derail the call]

   **Tell Them How to Feel:**
   - [One sentence framing: "Overall, we're in a strong position because..." or "We have a clear plan to address X..."]
   ```

### `/prep internal` — Team Sync

1. Pull current week Meta performance
2. Search Day.ai for recent meetings — any open action items
3. Search `{slack_internal}` for open threads and blockers
4. Format:
   ```
   **{client_display_name} — Internal Sync Prep**

   **This Week's Numbers:** Spend $X.XK | X leads | $X.XX CPL
   **vs. Target:** [On track / Off track]

   **Open Action Items:**
   - [{gm_name}]: [action] — [status]
   - [{media_buyer_name}]: [action] — [status]
   - [Jay]: [action] — [status]

   **Creative Pipeline:**
   - In concept: [X]
   - In review: [X]
   - Ready to launch: [X]
   - Live: [X]

   **Blockers:**
   - [Any blockers or dependencies]

   **This Week's Priority:**
   - [Single most important thing to move forward]
   ```

**Memory Storage:** Save any decisions made during the meeting. Update action item status.

---

## `/competitive` — Competitive Analysis

**Description:** Side-by-side comparison against a competitor running in the same Meta ad account (e.g., GrowJoy in MarketBeat).

**Required Config Variables:**
- `{client_name}`, `{client_display_name}`
- `{meta_account_id}`
- `{tfm_campaign_ids}` (TFM campaigns only)
- `{competitor_name}`, `{competitor_campaign_ids}`
- `{partner_dashboard_url}`, `{partner_dashboard_metrics}` (for downstream metrics)

**Execution Steps:**

1. **Pull TFM campaign data** from Meta (last 7 days):
   - Campaigns: `{tfm_campaign_ids}`
   - Metrics: spend, leads, CPL, CTR, CPC, CPM, LP views, LP CVR
   - Ad-level breakdown: top 5 by spend

2. **Pull competitor campaign data** from Meta (last 7 days):
   - Campaigns: `{competitor_campaign_ids}`
   - Same metrics
   - Ad set-level breakdown: top 5 by spend

3. **Pull partner dashboard data** (if available):
   - Revenue, Rev/User, confirmed sales, SMS opt-ins, co-reg leads
   - Split by TFM vs. competitor

4. **Build comparison table:**
   ```
   # {client_display_name} — TFM vs. {competitor_name} Comparison
   **Period:** [Date range]

   ## Top-Line Comparison
   | Metric | TFM | {competitor_name} | Gap | TFM Advantage? |
   |--------|-----|-------------------|-----|----------------|
   | Spend | $ | $ | | |
   | Leads | | | | |
   | CPL | $ | $ | | |
   | CTR | % | % | | |
   | CPC | $ | $ | | |
   | CPM | $ | $ | | |
   | LP CVR | % | % | | |

   ## Downstream Metrics (from partner dashboard)
   | Metric | TFM | {competitor_name} | Gap |
   |--------|-----|-------------------|-----|
   | Revenue | $ | $ | |
   | ROAS | % | % | |
   | Rev/User | $ | $ | |
   | SMS Opt-ins | | | |

   ## Structural Differences
   - **Creative strategy:** [What they're doing vs. what we're doing]
   - **Budget allocation:** [How they concentrate vs. spread budget]
   - **LP strategy:** [LP themes, rotation cadence]
   - **Targeting:** [Any differences in audience, placements]
   - **Creative velocity:** [How often they launch new ads vs. us]

   ## Where TFM Wins
   1. [Metric/strategy advantage + data]

   ## Where {competitor_name} Wins
   1. [Metric/strategy advantage + data]

   ## Recommended Actions
   1. [Specific, actionable step to close the gap]
   2. [Step 2]
   3. [Step 3]
   ```

**Memory Storage:** Save comparison snapshot for WoW trending. Note any structural changes observed.

---

## `/update-intel` — Refresh Client Intelligence File

**Description:** Scan recent Day.ai recordings and Slack messages to find new information that updates the 6-category intelligence framework.

**Required Config Variables:**
- `{client_name}`, `{client_display_name}`
- `{day_ai_search_term}`
- `{slack_internal}`, `{slack_external}`
- `{client_intel_path}`

**Execution Steps:**

1. **Search Day.ai** for the last 7 days:
   - Find all meeting recordings mentioning `{day_ai_search_term}`
   - Read transcripts for: KPI changes, contact changes, brand voice feedback, creative feedback, sentiment signals, strategy shifts

2. **Search Slack** for the last 7 days:
   - `{slack_internal}` — internal discussions, escalations, creative reviews
   - `{slack_external}` — client messages, requests, feedback
   - Look for: copy approvals/rejections, performance reactions, new contacts, deadline changes

3. **Map findings to the 6-category framework:**
   - **Client Overview:** New contacts, role changes, ESP changes, channel changes
   - **North Star Metric:** KPI adjustments, new targets, quality definition changes
   - **Brand Voice Rules:** New NEVER rules, approved language, copy feedback
   - **Winning Creative Signals:** New validated winners, format discoveries
   - **Negative Triggers:** New kills, complaints, quality flags
   - **Relationship Health:** Sentiment shift, risk changes, continuity concerns

4. **Show diff before writing:**
   ```
   ## Proposed Intelligence Updates — {client_display_name}

   ### Category X: [NAME]
   **CURRENT:** [existing text]
   **PROPOSED:** [new text]
   **SOURCE:** [Day.ai recording from [date] / Slack message from [user] on [date]]

   [Repeat for each change]

   ### No Changes Detected:
   - [List categories with no updates]
   ```

5. **Write updates** only after confirmation (or draft if running unattended).

**Memory Storage:** Log what was updated, what was unchanged, and the sources used. Note the date so this doesn't re-scan the same period.

---

## `/sindy-brief` — Generate Sindy Ops Update

**Description:** Generate an operations update for Sindy (Head of Operations) covering client status, report accuracy, creative pipeline, and blockers.

**Required Config Variables:**
- `{client_name}`, `{client_display_name}`
- `{meta_account_id}`, `{campaign_ids}`
- `{kpi_primary}`, `{kpi_target}`, `{cpl_target}`
- `{gm_name}`, `{media_buyer_name}`
- `{slack_internal}`
- `{client_intel_path}`
- `{report_destination}`

**Execution Steps:**

1. **Determine client status:**
   - Pull last 7 days Meta performance
   - Compare CPL to `{cpl_target}`, spend to budget pace
   - Classify: ON TRACK (CPL within 10% of target) / AT RISK (10-25% over) / CRITICAL (25%+ over or spend stalled)

2. **Check reporting accuracy:**
   - Was Friday report posted this week to `{report_destination}`?
   - Was bi-weekly report completed after last client call?
   - Any gaps in reporting cadence?

3. **Creative pipeline status:**
   - Search Slack `{slack_internal}` for creative discussions
   - Search Notion for creative concepts in pipeline
   - Categorize: In Concept / In Review / Ready to Launch / Live
   - Count active ads vs. paused ads in Meta

4. **Surface blockers and action items:**
   - Open action items from last client meeting (Day.ai)
   - Open threads in `{slack_internal}` without resolution
   - Any dependencies on client (approvals, assets, access)

5. **Format in Sindy's preferred style:**
   ```
   **{client_display_name} — OPS UPDATE**

   **STATUS:** [ON TRACK / AT RISK / CRITICAL]
   CPL: $X.XX (target: {cpl_target}) | Spend: $X.XK/{monthly_budget}

   **REPORTING:**
   - Friday report: [POSTED / MISSING] — [date]
   - Bi-weekly recap: [POSTED / MISSING] — [date]

   **CREATIVE PIPELINE:**
   - Live: X ads
   - Ready to launch: X
   - In review: X
   - In concept: X

   **OWNERS & ACTION ITEMS:**
   - @{gm_name}: [action] — due [date]
   - @{media_buyer_name}: [action] — due [date]
   - @client: [action] — due [date]

   **BLOCKERS:**
   - [Blocker] — waiting on [who] — [days waiting]

   **NEXT MILESTONE:**
   - [What happens next and when]
   ```

**Memory Storage:** Log the status classification and any blockers for tracking resolution over time.

---

## `/concept` — Concept Ideation Engine (Parker-Style)

**Description:** Research what's winning, analyze brand context and competitors, and generate new ad concept ideas with copy, visual direction, and iterations. This is TFM's internal version of Parker — built for GMs to run when they need fresh concepts for a sprint.

**Required Config Variables:**
- `{client_name}`, `{client_display_name}`
- `{meta_account_id}`, `{campaign_ids}`
- `{client_intel_path}`
- `{brand_voice_tone}`, `{never_rules}`, `{approved_language}`
- `{audience_segments}` (ICPs from intel file)
- `{landing_page_urls}` (active LPs)
- `{dct_naming_prefix}`, `{next_dct_number}`
- `{notion_page_url}` (client hub — concept database lives here)
- `{slack_internal}` (for recent creative decisions)

**Optional Config Variables:**
- `{foreplay_board_id}` — Foreplay swipe file board for this client (if they have one)
- `{competitor_domains}` — Domains to search in Foreplay Discovery for competitor creative

**Execution Steps:**

### Phase 1: Learn (What's working and what the brand needs)

1. **Read the client intelligence file** (`{client_intel_path}`):
   - Winning Creative Signals — top formats, mechanisms, validated angles
   - Brand Voice Rules — NEVER rules, approved language, tone
   - Negative Triggers — killed creative, client complaints, charged quotes
   - North Star Metric — what "success" means for this client (CPL? ROAS? Qualified leads? MAR?)
   - Audience Segments — ICPs with specific hooks for each

2. **Pull top 10 performing ads (L30D)** from Pipeboard:
   - Account: `{meta_account_id}`, Campaigns: `{campaign_ids}`
   - Sort by: primary KPI (CPL for CPL clients, ROAS for ROAS clients)
   - For each ad: name, primary text, headline, description, format, CPL, CTR, spend, leads
   - Identify patterns across top performers:
     - Hook structures (confession, question, statistic, story, UGC)
     - Emotional triggers (fear, curiosity, aspiration, belonging, status)
     - CTA styles (direct, soft, curiosity-gap)
     - Formats (text-heavy, image, video, UGC, carousel)

3. **Pull bottom 5 performing ads (L30D)** from Pipeboard:
   - Same metrics — identify what's NOT working
   - Anti-patterns: what angles, hooks, formats to avoid

4. **Read `{slack_internal}` (last 14 days)** for:
   - Recent creative decisions — what was launched, paused, killed and WHY
   - Client feedback on specific ads — quotes from the client
   - Creative direction from GM or Jay
   - Sprint status — what concepts are in pipeline, in review, ready to launch

5. **Read the Notion concept database** (`{notion_page_url}`):
   - What concepts have already been created (avoid duplicates)
   - What angles have been tested and their results
   - Any upcoming briefs or requests

6. **[If Foreplay configured] Research competitor creative:**
   - Search Foreplay Discovery API for `{competitor_domains}` — last 30 days
   - Pull top 10 competitor ads by engagement
   - OR read from `{foreplay_board_id}` saved swipe file
   - Identify angles/hooks/formats competitors are using that we haven't tested

7. **[If no Foreplay] Use web research:**
   - Search for the client's newsletter niche + "best ad creative" or "top performing ads"
   - Search Meta Ad Library (manual — provide the URL for the GM to reference)
   - Note: this is less precise than Foreplay but still valuable for angle discovery

### Phase 2: Ideate (Generate new concepts)

8. **Generate 5 new concept ideas**, each with:

   ```
   ## Concept [X]: [Concept Name]
   **DCT Name:** {dct_naming_prefix}[number]_[ConceptName]
   **Angle:** [1-2 sentences — what this concept is about and why it should work]
   **Target ICP:** [Which segment from {audience_segments}]
   **Format:** [Static image / Video / UGC script / Carousel / Text-heavy]
   **Inspiration:** [What winning ad or pattern inspired this — cite specific DCT or competitor reference]

   ### Primary Text (3 variations)
   **V1 — [Hook type: Confession / Question / Statistic / Story]**
   [Full primary text — ready to paste into Ads Manager]

   **V2 — [Different hook type]**
   [Full primary text]

   **V3 — [Different hook type]**
   [Full primary text]

   ### Headlines (2)
   1. [Headline]
   2. [Headline]

   ### Descriptions (2)
   1. [Description]
   2. [Description]

   ### Visual Direction
   - **Format:** [Image / Video / Carousel]
   - **Style:** [Photo, illustration, text overlay, UGC, Apple Notes, screenshot, meme]
   - **Key visual elements:** [What should be in the image/thumbnail]
   - **Text overlay (if applicable):** [Exact text for the creative]
   - **Reference:** [Link to similar winning creative or describe the visual feel]
   - **Designer notes:** [Specific guidance for the designer — colors, layout, fonts, mood]

   ### Landing Page
   [Which LP from {landing_page_urls} to use and why]

   ### Why This Should Work
   [2-3 sentences connecting this concept to winning patterns, audience psychology, and client brand voice]
   ```

9. **Diversify the concept mix.** The 5 concepts MUST include:
   - At least 2 different hook types (confession, question, statistic, story, UGC)
   - At least 2 different formats (text-heavy, image, video, UGC)
   - At least 2 different ICPs (if the client has multiple audience segments)
   - At least 1 iteration/variation on a current top performer (same angle, new hook)
   - At least 1 net-new angle that hasn't been tested

### Phase 3: Iterate (Build on winners)

10. **Generate 3 iterations on top performers:**

   ```
   ## Iteration: [Original DCT Name] → [New Variation]
   **Original:** [Brief description of the winning ad + its metrics]
   **What we're changing:** [Hook / Angle / Format / CTA / Visual]
   **Why:** [What signal suggests this iteration could improve on the original]

   ### New Primary Text (2 variations)
   [Full text — ready to paste]

   ### New Headline
   [Headline]

   ### Visual Adjustment
   [What changes in the visual vs. the original]
   ```

### Phase 4: Validate & Output

11. **Compliance check — run every concept against:**
   - `{never_rules}` — flag ANY violation with the specific rule
   - `{brand_voice_tone}` — verify tone matches
   - `{approved_language}` — verify key phrases are used where appropriate
   - Dead angles — concepts that overlap with recently killed or underperforming ads
   - Duplicate check — concepts that are too similar to existing ones in the concept database

12. **Generate a hooks bank:**

   ```
   ## Hooks Bank (10 new hooks)
   | # | Hook | Type | Target ICP | Notes |
   |---|------|------|------------|-------|
   | 1 | [Hook text] | Confession | [ICP] | [Why this should work] |
   | 2 | [Hook text] | Question | [ICP] | |
   | ... | | | | |
   ```

13. **Output summary:**

   ```
   ## /concept Summary — {client_display_name}
   **Date:** [today]
   **Based on:** L30D top performers, {X} competitor references, brand intelligence

   **What's winning now:**
   - [Pattern 1 — with data]
   - [Pattern 2 — with data]
   - [Pattern 3 — with data]

   **What's NOT working:**
   - [Anti-pattern 1]
   - [Anti-pattern 2]

   **New Concepts Generated:** 5
   **Iterations on Winners:** 3
   **New Hooks:** 10

   **Recommended launch priority:**
   1. [Concept X] — [reason: highest confidence based on winning patterns]
   2. [Concept Y] — [reason]
   3. [Concept Z] — [reason]
   ```

**Memory Storage:** Save the winning patterns identified, concepts generated, and hooks bank. Track which concepts from previous runs got launched and their performance to improve future ideation.

---

## Usage Notes

### Running Commands
- Invoke any command by typing the slash command (e.g., `/friday`)
- Commands will prompt for confirmation before writing to external systems (Notion, Slack, client files)
- All Slack messages are drafted, not sent, unless explicitly told to send

### Variable Resolution
- All `{variables}` are resolved from the client's `client-config.md` file
- If a required variable is missing, the command will flag it and skip that section rather than fail entirely
- Optional sections (ESP data, partner dashboard) are skipped gracefully when not configured

### Memory Continuity
- Commands that store to memory enable WoW comparisons and trend tracking
- The `/friday` command depends on previous `/friday` data for WoW calculations
- The `/update-intel` command tracks scan dates to avoid re-processing

### Cross-Command Workflows
Common sequences:
1. **Friday flow:** `/friday` → post to Notion → post summary to `{slack_internal}`
2. **Client call flow:** `/bi-weekly` (build pre-call Notion doc) → `/prep client` (talking points) → [attend call] → `/recap` (post-call follow-ups) → `/update-intel`
3. **Nathan 1:1 flow:** `/status` for each client → `/prep nathan` for flagged clients
4. **Weekly ops:** `/sindy-brief` for all clients → compile into single ops report
5. **Sprint creative flow:** `/concept` (generate ideas) → GM reviews + selects → `/creative-brief` (build specific brief for selected concept) → designer executes → launch
6. **Concept ideation flow:** `/concept` → review hooks bank → select top 3-5 concepts → iterate on winners → add to Notion concept database → assign to designer
