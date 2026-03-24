# Skills QA & Improvement Plan
**Created:** 2026-03-21
**Author:** Claude Code (post-build review)
**Status:** APPLIED — all P0, P1, and most P2 fixes applied on 2026-03-21

---

## Executive Summary

After reviewing all 6 SKILL.md files, 3 hooks, the pipeboard-cache.py, and the feedback memories from today's testing, there are **4 P0 issues** (broken/produce wrong output), **6 P1 issues** (misleading/incomplete), and **8 P2 issues** (nice-to-have improvements). The two biggest cross-cutting problems are:

1. **No skill has a "Phase 0: Load Context" step** — they jump straight to data pulling without reading client intel files first. This caused the TPG ROAS miss and will repeat for every ROAS/V-CAC/Cost-Per-Trial client.
2. **No skill handles Pipeboard pagination** — the IHIH bug (only page 1 returned) will repeat for any client with >25 ads per campaign.

---

## Cross-Cutting Issues (affect multiple skills)

### CC-1: Missing "Phase 0: Load Context" — P0

**Affects:** `/fatigue-scan`, `/portfolio-pulse`
**Problem:** Both skills go straight to Pipeboard pulls without first reading `clients/[slug]/[slug].md` and `client-config.md` for strategic context. Jay had to manually point out that TPG's vault file already contained 6-week ROAS at 14%, per-DCT ROAS data, and ad mix shift analysis — the fatigue scan ignored all of it and said "ROAS data not available."
**Fix:** Add a Phase 0 to both skills:

```markdown
### Phase 0: Load Client Context (BEFORE any data pull)

For each client being scanned:
1. Read `clients/[slug]/[slug].md` — extract:
   - Performance history sections (ROAS data, trend notes, known issues)
   - Current strategic context (what's being tested, paused, restructured)
   - Risk level and relationship context
2. Read `clients/[slug]/client-config.md` — extract:
   - `kpi_primary` and `kpi_secondary` (determines which metrics matter)
   - `tfm_campaign_ids` (determines what to pull)
   - Scaling Rules section if present (determines recommendations)
   - `never_rules` (for creative context in recommendations)
3. Store this context and reference it throughout the analysis.
   - If ROAS data exists in vault files, include it in the report even if Pipeboard can't provide it.
   - If ads disappeared between windows (paused/killed), cross-reference with Slack/vault context to explain WHY.
```

### CC-2: No Pipeboard Pagination Handling — P0

**Affects:** `/fatigue-scan`, `/portfolio-pulse`
**Problem:** The IHIH fatigue scan returned only page 1 of ad-level results, missing the top 4 spending ads. The SKILL.md files don't mention pagination at all. Pipeboard's `get_insights` likely returns paginated results for campaigns with many ads.
**Fix:** Add to both skills:

```markdown
### Pagination Protocol

When pulling ad-level or campaign-level data from Pipeboard:
1. Check the response for pagination indicators (`paging`, `next`, `after` cursor, or similar)
2. If results appear truncated (e.g., exactly 25 records returned), explicitly request the next page
3. Continue until all pages are retrieved
4. Log total record count vs expected: "Retrieved X ads from Y campaigns"
5. If the API returns fewer ads than expected for a known active client, flag: "WARNING: May be missing ads — verify pagination"

For multi-campaign clients (Workweek 5 accounts, Stocks.News 5 campaigns), pull each campaign separately to avoid hitting single-request limits.
```

### CC-3: No Client-Specific Conversion Event Mapping — P0

**Affects:** `/portfolio-pulse`, `/fatigue-scan`, `pipeboard-cache.py`
**Problem:** The `pipeboard-cache.py` has a hardcoded priority list for conversion events: `onsite_web_lead` > `fb_pixel_lead` > `complete_registration` > `fb_pixel_custom` > `lead` > `mobile_app_install`. This caused:
- **Experiential Hospitality:** CPL showed $389 because it picked `onsite_web_lead` (27 conversions) instead of `fb_pixel_custom` (1,968 conversions) — the actual webinar registrations
- **Open Source CEO & RNT Fitness:** Use custom beehiiv events not in the priority list at all
- **Stocks.News:** Tracks app installs + trial starts, which need `mobile_app_install` prioritized, not deprioritized
**Fix:** Add a `preferred_conversion_event` field to each `client-config.md`, and modify `pipeboard-cache.py` to check it:

```python
# In pipeboard-cache.py, add client-specific override:
CLIENT_CONVERSION_OVERRIDES = {
    "experiential-hospitality": "offsite_conversion.fb_pixel_custom",  # webinar registrations
    "stocks-news": "mobile_app_install",  # app installs (primary), then trial starts
    "open-source-ceo": None,  # needs investigation — custom beehiiv event
    "rnt-fitness": None,  # needs investigation — custom beehiiv event
    "status-news": "offsite_conversion.fb_pixel_custom",  # Qualified Carrd sign-ups
}

# Before using priority list, check for client-specific override
if client_slug in CLIENT_CONVERSION_OVERRIDES and CLIENT_CONVERSION_OVERRIDES[client_slug]:
    # Use the override event type
```

Also add `preferred_conversion_event` to each client's `client-config.md` under KPIs & Targets, so the cache script and skills can read it.

### CC-4: Skills Don't Read Scaling Rules Section — P1

**Affects:** `/fatigue-scan`, `/portfolio-pulse`
**Problem:** TPG has a detailed "Scaling Rules" section in its config (ROAS validation required, no unvalidated spend >5%, top performer protection, kill criteria). The fatigue scan's Phase 3b mentions reading it, but only for ROAS-primary clients. Other clients may have scaling rules too (e.g., EH: "Do NOT scale beyond $15K per webinar").
**Fix:** In both skills, Phase 0 should always read the full client-config.md, not just the meta_account_id and tfm_campaign_ids fields. The "Scaling Rules" section and "budget_notes" field both contain guardrails that affect recommendations.

---

## Per-Skill Issues

### `/portfolio-pulse`

#### PP-1: No Phase 0 context loading — P0
See CC-1 above. The first live run pulled account-level data for CT ($120K) and TPG ($179K) because it didn't read tfm_campaign_ids first. This was fixed in the SKILL.md (Phase 2 now says "CAMPAIGN LEVEL ONLY"), but the fix relies on the skill actually reading config files first, which isn't structured as a distinct phase.

**Specific edit:** Insert Phase 0 (from CC-1) before the current Phase 1. Renumber all subsequent phases.

#### PP-2: No pagination handling — P0
See CC-2 above.

#### PP-3: Decisions log says TPG was "excluded" then was fixed — P1
The skills-build.md says "TPG ($179K/week) excluded from TFM-managed spend calculations (RV account, TFM is creative/strategy only)" but then the SKILL.md was updated to filter to TFM campaign IDs. The state file decision is now stale/contradictory.

**Specific edit:** Update `system/state/skills-build.md` decisions section: change "TPG excluded" to "TPG filtered to TFM campaign IDs only (120216387459500663, 120239047814670663) — account total is $179K/week but TFM manages ~$24K/week."

#### PP-4: Workweek exception says "account-level pulls are acceptable" — P2
Phase 2 says for Workweek "account-level pulls are acceptable" since all 5 accounts are TFM-managed. But it also says "still prefer campaign-level for consistency." The exception creates an opportunity for the skill to take the shortcut. Remove the exception — just pull campaign-level for all clients, no exceptions.

**Specific edit:** Remove the line "Each of the 5 accounts is fully TFM-managed, so account-level pulls are acceptable." Replace with: "Each of the 5 accounts is fully TFM-managed, but still pull at campaign level for consistency."

#### PP-5: No mention of conversion event selection — P1
The skill says to pull `actions` and `cost_per_action_type` but doesn't specify which action_type to use for CPL calculation. Different clients use different events (see CC-3). The skill should reference the client config's `kpi_primary` and preferred conversion event.

**Specific edit:** Add to Phase 2 after step 5:
```
6. Determine the correct conversion event for CPL calculation:
   - Read `kpi_primary` from client-config.md
   - If `preferred_conversion_event` is specified, use that action_type
   - If not specified, use the default priority: lead > complete_registration > fb_pixel_custom > onsite_web_lead
   - Log which event was used: "CPL calculated from [event_type] ([count] conversions)"
```

### `/fatigue-scan`

#### FS-1: No Phase 0 context loading — P0
See CC-1. Jay explicitly called this out: "not useful without the full context." The feedback memory (`feedback_fatigue_scan_context.md`) documents exactly what needs to happen but it hasn't been incorporated into the SKILL.md yet.

**Specific edit:** Insert the following as Phase 0 before Phase 1:

```markdown
### Phase 0: Load Client Context (MANDATORY — before any Pipeboard pull)

1. Read `clients/[slug]/[slug].md`:
   - Extract any ROAS data, performance history, trend notes
   - Note known issues (e.g., "Andromeda paused — ROAS degraded at scale")
   - Check for per-DCT performance data already in the vault
2. Read `clients/[slug]/client-config.md`:
   - Extract `kpi_primary` — determines whether CPL, ROAS, V-CAC, or Cost Per Trial is the fatigue signal
   - Extract `tfm_campaign_ids` — determines what to pull
   - Read full Scaling Rules section if present
   - Read `budget_notes` for scaling guardrails
3. If `kpi_secondary` mentions ROAS:
   - Search the intel file for ROAS data (6-week ROAS, per-DCT ROAS, ROAS trends)
   - Search Slack `#internal-[slug]` for recent ROAS reports/dashboard shares
   - Include vault ROAS data in the fatigue report even if Pipeboard can't provide it
4. Store all context — the fatigue report should LEAD with strategic context, then layer metrics on top.
```

#### FS-2: No pagination handling — P0
See CC-2. The IHIH bug was exactly this: campaign-level ad pull returned only page 1, missing the top 4 spending ads. Made the account look like it collapsed.

#### FS-3: Ads disappearing between windows not handled as a signal — P1
The feedback memory specifically notes: "Flag when ads disappear between windows (paused/killed) — this is a decision signal, not missing data." The current SKILL.md doesn't address this pattern at all.

**Specific edit:** Add to Phase 3 (Calculate Fatigue Signals):
```markdown
**Window-to-window disappearance check:**
- If an ad appeared in Window 1 (days 8-14) but NOT in Window 2 (days 1-7), it was likely paused or killed.
- Report these separately as "Paused Between Windows" with their Window 1 spend.
- If >50% of Window 1 ads disappeared, flag: "Major restructure detected — cross-reference with Slack/vault for context."
- Do NOT treat disappeared ads as "missing data" — they are operational decisions that affect the fatigue assessment.
```

#### FS-4: ROAS data source instructions are incomplete — P1
Phase 3b says "Search Slack `#internal-[slug]` for the most recent ROAS report/dashboard share" but doesn't mention checking the client's intel file first. Jay's complaint was that ROAS data was ALREADY IN THE VAULT and the skill ignored it.

**Specific edit:** In Phase 3b, reorder the "Where to find ROAS data" section:
```markdown
**Where to find ROAS data (check in this order):**
1. The client's intel file (`clients/[slug]/[slug].md`) — often has per-DCT ROAS data, trend analysis, and cohort dashboard summaries already documented
2. The client's config file — check `kpi_secondary_target` for ROAS thresholds
3. Slack `#internal-[slug]` — search for recent ROAS report/dashboard shares
4. If no ROAS data found anywhere, note "ROAS data not available — recommend requesting from [contact]"
```

#### FS-5: ROAS-primary client list is too narrow — P2
Phase 3b hardcodes "ROAS-primary clients (as of Mar 2026): The Points Guy, MarketBeat." But TPG's kpi_primary is actually CPL, with ROAS as kpi_secondary. And EH has ROAS as kpi_secondary too. The skill should dynamically read `kpi_secondary` from config rather than maintaining a hardcoded list.

**Specific edit:** Replace "ROAS-primary clients (as of Mar 2026): The Points Guy, MarketBeat" with:
```
Check `kpi_primary` and `kpi_secondary` in client-config.md. If either mentions ROAS, apply the ROAS analysis rules below. Do not maintain a hardcoded list — client KPIs change.
```

### `/creative-qa`

#### CQ-1: No issues found — skill is well-structured
The creative-qa SKILL.md has a solid Phase 1 that reads client intel files and configs before doing anything. This is the model that other skills should follow.

#### CQ-2: Hook description could be clearer about scope — P2
Jay asked "does it scan every message anyone sends?" The answer is no — it only gates Claude Code's own Slack sends. The SKILL.md's Hook Integration section says this correctly ("PreToolUse hook... runs before every Slack send/draft") but the hook script itself has no header comment explaining this scope.

**Specific edit:** Add to the top of `creative-qa-gate.sh` after the description:
```bash
# SCOPE: This hook only runs on Claude Code's own outgoing Slack messages.
# It does NOT monitor messages sent by team members or other bots.
# It triggers via Claude Code's PreToolUse hook system on slack_send_message and slack_send_message_draft.
```

### `/vault-integrity`

#### VI-1: Required fields list doesn't match hook — P1
The SKILL.md requires 10 frontmatter fields: `client`, `slug`, `gm`, `status`, `current_cpl`, `cpl_target`, `risk_level`, `sentiment`, `last_enriched`, `north_star_metric`.

The `validate-frontmatter.sh` hook only checks 7: `client`, `slug`, `gm`, `status`, `current_cpl`, `risk_level`, `last_enriched`.

Missing from hook: `cpl_target`, `sentiment`, `north_star_metric`.

**Specific edit for hook:** Add the missing fields to the loop on line 51:
```bash
for FIELD in client slug gm status current_cpl cpl_target risk_level sentiment last_enriched north_star_metric; do
```

#### VI-2: No validation of client-config.md `preferred_conversion_event` — P2
Once CC-3 is implemented (adding `preferred_conversion_event` to client configs), vault-integrity should validate it exists for all active clients with Pipeboard accounts.

**Specific edit:** Add to Phase 5 (Config File Validation):
```
- `preferred_conversion_event` is specified (if client has `meta_account_id`)
```

### `/action-tracker`

#### AT-1: No issues found for the core skill — P2 improvement only
The action-tracker is Day.ai-centric and doesn't touch Pipeboard, so the pagination and conversion event issues don't apply.

#### AT-2: Could cross-reference action items with vault context — P2
When extracting action items, the skill doesn't read the client intel file for context on whether commitments were already completed and documented in the vault. A "Check client file for evidence of completion" step would reduce false overdue flags.

**Specific edit:** Add to Phase 5 (Cross-Reference and Reconcile):
```
6. **Vault evidence check:** For items older than 7 days, search the client's intel file, Slack, and recent meeting recordings for evidence the item was completed but never formally closed. Mark as "Likely completed — verify" rather than "Overdue."
```

### `/weekly-enrichment`

#### WE-1: Doesn't use the SQLite cache — P1
The weekly-enrichment skill updates frontmatter CPLs from Slack data but doesn't ingest that data into the `pipeboard.db` cache. This means the cache only gets populated when portfolio-pulse or fatigue-scan runs, creating gaps.

**Specific edit:** Add after Phase 5 (Update Client Files):
```markdown
### Phase 5b: Update Performance Cache

After extracting CPL data from Slack, ingest it into the SQLite cache for historical tracking:
```bash
echo '{"data":[{"spend":"...","conversions":"...","cpl":"..."}]}' | python3 system/pipeboard-cache.py ingest <slug> campaign
```
This ensures the cache has weekly data points even between portfolio-pulse runs.
```

#### WE-2: No conversion event awareness — P2
When the skill pulls CPL from Slack, it doesn't note which conversion event type the CPL corresponds to. For Stocks.News (Cost Per Trial), Status News (Qualified Carrd), and others, the "CPL" in Slack may mean different things. The skill should log the metric type when updating frontmatter.

---

## Hook Issues

### creative-qa-gate.sh

#### H-CQ-1: Channel name extraction is fragile — P1
The hook extracts the client slug from channel names using `sed`, but Slack sends often use channel IDs (like `C0839CZFUUV`), not human-readable names. When a channel ID is passed, the grep for `thefeed-|internal-` won't match, and the hook silently passes through without checking anything.

**Specific edit:** Add a channel ID-to-slug lookup, or at minimum, add a comment acknowledging the limitation:
```bash
# LIMITATION: This hook only works when channel is passed as a readable name.
# When Slack MCP passes channel_id (e.g., C0839CZFUUV), slug extraction fails
# and the hook passes through without checking. To fix: maintain a channel_id-to-slug
# mapping file, or query Slack API for channel info.
```

Better fix: Create a lookup file at `.claude/hooks/channel-map.json`:
```json
{
  "C0839CZFUUV": "the-points-guy",
  "C08Q8MBH0U9": "experiential-hospitality",
  ...
}
```
And load it in the hook when the channel is an ID.

#### H-CQ-2: Slug normalization doesn't cover all variations — P2
The `case` statement handles `workweek*`, `marketbeat*`, `points-guy|pointsguy|tpg`, `womens-sports|jws`, `slp`. But several clients have non-obvious channel name patterns:
- `#internal-experientialhospitality` would need mapping to `experiential-hospitality`
- `#internal-stocksnews` would need mapping to `stocks-news`
- `#internal-rntfitness` would need mapping to `rnt-fitness`
- `#thefeed-opensourceceo` would need mapping to `open-source-ceo`
- `#internal-bigdeskenergy` would need mapping to `big-desk-energy`
- `#internal-jayshetty` would need mapping to `jay-shetty`
- `#internal-howtoai` would need mapping to `how-to-ai`

**Specific edit:** Extend the case statement:
```bash
case "$SLUG" in
  workweek*) SLUG="workweek" ;;
  marketbeat*) SLUG="marketbeat" ;;
  "points-guy"|"pointsguy"|"tpg"|"thepointsguy") SLUG="the-points-guy" ;;
  "womens-sports"|"jws"|"justwomenssports") SLUG="just-womens-sports" ;;
  "slp"|"studentloanplanner") SLUG="student-loan-planner" ;;
  "experientialhospitality"|"eh") SLUG="experiential-hospitality" ;;
  "stocksnews") SLUG="stocks-news" ;;
  "rntfitness") SLUG="rnt-fitness" ;;
  "opensourceceo"|"osc") SLUG="open-source-ceo" ;;
  "bigdeskenergy"|"bde") SLUG="big-desk-energy" ;;
  "jayshetty") SLUG="jay-shetty" ;;
  "howtoai") SLUG="how-to-ai" ;;
  "stocksandincome") SLUG="stocks-and-income" ;;
  "insightlinks") SLUG="insight-links" ;;
  "creatorspotlight") SLUG="creator-spotlight" ;;
  "contrarianthinking") SLUG="contrarian-thinking" ;;
  "1636forum") SLUG="1636-forum" ;;
  "franklinsforum") SLUG="franklins-forum" ;;
  "pointspath") SLUG="points-path" ;;
  "statusnews") SLUG="status-news" ;;
  "dailydrop") SLUG="daily-drop" ;;
esac
```

#### H-CQ-3: Growth suffix stripping may be too aggressive — P2
Line 29: `sed 's/growth$//'` strips "growth" from the end of channel names. This is presumably for channels like `#thefeed-marketbeat-growth`, but it would also incorrectly strip from a hypothetical channel ending in "growth" that's part of the client name.

### validate-frontmatter.sh

#### H-VF-1: Missing 3 required fields — P1
See VI-1 above. The hook checks `client slug gm status current_cpl risk_level last_enriched` but the SKILL.md also requires `cpl_target`, `sentiment`, `north_star_metric`.

#### H-VF-2: No validation for `gm` against valid team members — P2
The hook checks that `gm` is non-empty but doesn't validate it against the valid team member list (Nathan May, Sindy, Rabii Elhaouat, Luiz Pekelman, Kinte Otieno, Lays Paiva, Mariely Galindo, Aubree Clark, Noreen, Melvin, Marc). A typo in the GM field would pass the hook but fail vault-integrity.

### slack-audit-trail.sh

#### H-SA-1: Log file location is relative to hook script — P2
Line 6: `AUDIT_LOG="$(dirname "$0")/slack-audit-log.jsonl"` puts the log in `.claude/hooks/slack-audit-log.jsonl`. This works but means the audit log lives outside the vault and won't be tracked by Obsidian Git. Consider moving to `system/logs/slack-audit.jsonl`.

#### H-SA-2: No log rotation — P2
The audit log appends forever. Over months of use, this file will grow unbounded. Add a date-based log rotation or size check.

#### H-SA-3: Thread context not captured — P2
The hook logs `channel` and `message_preview` but not `thread_ts` (if replying to a thread). Thread context matters for understanding what conversation the message was part of.

**Specific edit:** Add thread_ts extraction:
```bash
THREAD=$(echo "$INPUT" | jq -r '.tool_input.thread_ts // "none"')
# In the echo line, add: \"thread_ts\":\"$THREAD\"
```

---

## pipeboard-cache.py Issues

### PC-1: Conversion event priority list is wrong for multiple clients — P0
See CC-3 above. The hardcoded priority list:
```python
conv_priorities = [
    "onsite_web_lead", "offsite_conversion.fb_pixel_lead",
    "complete_registration", "offsite_conversion.fb_pixel_complete_registration",
    "offsite_conversion.fb_pixel_custom", "lead",
    "mobile_app_install"
]
```

Problems:
1. `onsite_web_lead` is highest priority, but for EH it returns only 27 conversions vs 1,968 for `fb_pixel_custom` — the actual webinar registrations. This inflated EH's CPL to $389.
2. `mobile_app_install` is lowest priority, but for Stocks.News it's the primary KPI.
3. `offsite_conversion.fb_pixel_custom` is used by Status News, EH, and potentially others as their primary event, but it's ranked 5th.
4. Open Source CEO and RNT Fitness may use custom beehiiv events not in the list at all.

**Fix:** Accept a `client_slug` parameter and look up the preferred event. Fall back to the priority list only if no override exists. Also flip the default priority: `lead` and `complete_registration` should be higher than `onsite_web_lead` for newsletter clients.

### PC-2: No deduplication on ingest — P1
If the same data is ingested twice (e.g., running portfolio-pulse twice in one day), the cache creates duplicate snapshot records. The `ingest_response` function should check for existing snapshots with the same `client_slug`, `snapshot_date`, and `level` before inserting.

**Specific edit:** Add before the INSERT into snapshots:
```python
# Check for existing snapshot
existing = cursor.execute(
    "SELECT id FROM snapshots WHERE client_slug = ? AND snapshot_date = ? AND level = ?",
    (client_slug, snapshot_date, level)
).fetchone()
if existing:
    print(f"Snapshot already exists for {client_slug} on {snapshot_date} ({level}-level). Skipping.")
    conn.close()
    return
```

### PC-3: Summary query doesn't account for multi-campaign clients — P2
The `show_summary` function gets the latest snapshot per client, but a client with 5 campaigns (e.g., Stocks.News) might have 5 separate snapshots with different IDs. The query groups by `client_slug` and takes `MAX(snapshot_id)`, which would only capture the last campaign ingested.

**Fix:** Group by `(client_slug, snapshot_date)` and take all records from the latest date, not just the latest snapshot_id.

---

## Priority Summary

### P0 — Broken (produce wrong output)
1. **CC-1:** No Phase 0 context loading in fatigue-scan and portfolio-pulse
2. **CC-2:** No pagination handling in any Pipeboard-pulling skill
3. **CC-3:** Conversion event priority list wrong in pipeboard-cache.py (EH $389 CPL bug, Stocks.News deprioritized)
4. **PC-1:** Same as CC-3 — the cache script is the root cause

### P1 — Misleading (correct but incomplete)
1. **CC-4:** Skills don't read Scaling Rules section from client configs
2. **PP-5:** Portfolio pulse doesn't specify conversion event selection logic
3. **FS-3:** Ads disappearing between windows not handled as operational signal
4. **FS-4:** ROAS data source instructions don't check vault first
5. **VI-1 / H-VF-1:** Frontmatter hook missing 3 required fields vs SKILL.md
6. **WE-1:** Weekly enrichment doesn't populate SQLite cache
7. **H-CQ-1:** Creative QA hook can't resolve channel IDs to slugs
8. **PC-2:** Cache allows duplicate snapshot ingestion

### P2 — Nice-to-have
1. **PP-4:** Workweek exception allows account-level pulls
2. **FS-5:** ROAS-primary client list hardcoded instead of dynamic
3. **CQ-2:** Hook scope description could be clearer
4. **AT-2:** Action tracker could cross-reference vault for completion evidence
5. **WE-2:** Weekly enrichment doesn't track conversion event type
6. **H-CQ-2:** Slug normalization doesn't cover all 25 channel name variations
7. **H-CQ-3:** Growth suffix stripping may be too aggressive
8. **H-VF-2:** Hook doesn't validate GM against team member list
9. **H-SA-1:** Audit log location outside vault
10. **H-SA-2:** No log rotation
11. **H-SA-3:** Thread context not captured in audit log
12. **VI-2:** No validation of preferred_conversion_event once added
13. **PC-3:** Cache summary query wrong for multi-campaign clients
14. **PP-3:** State file has contradictory TPG decision

---

## Recommended Execution Order

1. **Fix pipeboard-cache.py conversion priorities** (PC-1/CC-3) — root cause of EH and Stocks.News bugs
2. **Add Phase 0 to fatigue-scan** (FS-1/CC-1) — Jay's explicit feedback, already documented in memory
3. **Add Phase 0 to portfolio-pulse** (PP-1/CC-1) — same pattern
4. **Add pagination handling to both skills** (CC-2) — prevents IHIH repeat
5. **Add missing fields to validate-frontmatter.sh** (H-VF-1/VI-1) — quick fix, high value
6. **Extend creative-qa-gate.sh slug normalization** (H-CQ-2) — prevents silent pass-through for most clients
7. **Add preferred_conversion_event to client configs** (CC-3 client-side) — enables per-client event mapping
8. **Everything else** — P2 items in any order

---

## Files That Need Editing (when approved)

| File | Issues |
|------|--------|
| `~/.claude/skills/fatigue-scan/SKILL.md` | FS-1, FS-2, FS-3, FS-4, FS-5 |
| `~/.claude/skills/portfolio-pulse/SKILL.md` | PP-1, PP-2, PP-4, PP-5 |
| `~/.claude/skills/vault-integrity/SKILL.md` | VI-2 |
| `~/.claude/skills/weekly-enrichment/SKILL.md` | WE-1, WE-2 |
| `system/pipeboard-cache.py` | PC-1, PC-2, PC-3 |
| `.claude/hooks/creative-qa-gate.sh` | H-CQ-1, H-CQ-2, H-CQ-3, CQ-2 |
| `.claude/hooks/validate-frontmatter.sh` | H-VF-1, H-VF-2 |
| `.claude/hooks/slack-audit-trail.sh` | H-SA-1, H-SA-2, H-SA-3 |
| `system/state/skills-build.md` | PP-3 |
| 25x `clients/*/client-config.md` | CC-3 (add `preferred_conversion_event` field) |
