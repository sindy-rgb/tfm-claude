---
name: creative-qa
description: >
  Pre-send creative QA for The Feed Media. Checks ad copy, scripts, and Slack messages against
  client NEVER rules, brand voice guidelines, and factual accuracy before sharing with clients.
  Cross-references copy against Google Drive scripts and Notion pipeline. Use when the user says
  "creative QA", "QA this", "check this copy", "review creative", "check against NEVER rules",
  "brand voice check", "is this copy safe to send", "review before sending", or before sharing
  any creative in a client channel.
---

# Creative QA — Pre-Send Copy & Creative Review

You are the creative quality gate for The Feed Media (TFM). Before any ad copy, creative concept, or script is shared with a client, you check it against that client's NEVER rules, brand voice guidelines, and factual claims. You catch violations before they reach the client or go live in ads.

## Why This Matters

TFM has been burned by creative violations — MarketBeat's ad account was banned over nuclear B-roll, subscriber counts have been inconsistent across Workweek creatives, and specific stock price predictions could trigger financial compliance issues. One bad creative can lose a client or an ad account.

## Usage

- `/creative-qa [client-slug]` — Full QA check on the most recent creative/copy for a client
- `/creative-qa [client-slug] "[copy text]"` — QA a specific piece of copy
- Automatic: The PreToolUse hook at `.claude/hooks/creative-qa-gate.sh` does keyword-level checks before any Slack send. This skill does the deep AI-powered review.

## Hook Integration

A shell script hook runs before every Slack send/draft:
- **Hook:** `.claude/hooks/creative-qa-gate.sh`
- **Trigger:** PreToolUse on `slack_send_message` and `slack_send_message_draft`
- **What it does:** Keyword-matching against NEVER rules (e.g., "MarketBeat" in ad copy, nuclear imagery references, stock price predictions)
- **What it blocks:** Hard keyword violations only (exit 2 = blocked)
- **What it misses:** Subtle brand voice issues, factual accuracy, context-dependent violations

This skill catches everything the hook misses.

## Step-by-Step Process

### Phase 1: Identify the Client and Load Rules

1. Determine the client slug from the argument or from the Slack channel context
2. Read the client's intel file: `/the-feed-media/clients/[slug]/[slug].md`
3. Extract:
   - **NEVER Rules** (Section: "### NEVER Rules") — hard stops, absolute violations
   - **Brand Voice** — tone, approved language, audience segments
   - **Approved Language** — specific phrases and terminology that ARE allowed
   - **Negative Triggers** — things that upset this specific client
4. Read the client's config file: `/the-feed-media/clients/[slug]/client-config.md`
5. Extract:
   - `never_rules` from config (may have additional rules)
   - `brand_voice_tone`
   - `approved_language`
   - `landing_page_urls` (for URL verification)
   - `utm_format` (for UTM verification)

### Phase 2: Gather the Creative to QA

If copy is provided directly in the command, use that.

Otherwise, find the most recent creative:
1. **Google Drive** (source of truth for copy): Search `mcp__gdrive__gdrive_search` for recent scripts/docs matching the client name
2. **Notion** (pipeline tracker): Search `mcp__claude_ai_Notion__notion-search` for the client's concept pipeline
3. **Slack** (latest shared creative): Search `mcp__claude_ai_Slack__slack_search_public_and_private` in `#internal-[slug]` for recent creative/concept messages

If Google Drive and Notion disagree, Drive wins (it's the copy source of truth).

### Phase 3: NEVER Rules Check (Hard Stops)

For each NEVER rule, check whether the creative violates it:

| Check | Method |
|-------|--------|
| Banned words/phrases | Direct text matching |
| Brand name restrictions | Check if restricted brand names appear in ad copy context |
| Compliance violations | Check for price predictions, guaranteed returns, medical claims |
| Imagery restrictions | Check script directions for banned visual elements |
| Tone violations | Compare against brand voice guidelines |
| Subscriber count consistency | Verify all number claims match current data |

**If ANY NEVER rule is violated: report as BLOCKED with the specific rule and the violating text.**

### Phase 4: Brand Voice Check

Compare the creative against the client's brand voice guidelines:

1. **Tone match:** Does the copy match the defined tone? (e.g., Workweek IHIH = vulnerability-first empathy, not corporate)
2. **Audience alignment:** Is the copy speaking to the right ICP/audience segment?
3. **Approved language:** Are approved phrases and terminology being used correctly?
4. **Formatting:** Does the copy follow the client's preferred style?

Score: PASS / WARN (minor tone drift) / FAIL (wrong voice entirely)

### Phase 5: Factual Accuracy Check

1. **Subscriber/reader counts:** If the copy claims a number, verify against:
   - The client's intel file (latest known counts)
   - Recent Slack reports (if available)
   - The client's landing page (if accessible via Playwright)
2. **Mathematical claims:** Verify any percentages, multipliers, or calculations
3. **Date references:** Check that time-sensitive claims are still valid
4. **Landing page URLs:** Verify URLs in the copy match `landing_page_urls` from config
5. **UTM parameters:** If UTMs are included, verify they follow the client's `utm_format`

### Phase 6: Cross-Creative Consistency

If multiple creatives exist for this client (multiple DCTs, variations):
1. Check subscriber counts are consistent across all active creatives
2. Check brand claims are consistent
3. Check that different creatives target different audience segments (not cannibalizing)

### Phase 7: QA Report

```markdown
# Creative QA Report — [Client Name]
*Date: YYYY-MM-DD*
*Source: [Google Drive / Notion / Slack / Direct input]*

## Verdict: [APPROVED / BLOCKED / NEEDS REVISION]

## NEVER Rules Check
| Rule | Status | Details |
|------|--------|---------|
| [Rule 1] | PASS/FAIL | [Details if failed] |
| [Rule 2] | PASS/FAIL | [Details if failed] |

## Brand Voice Check
| Aspect | Status | Notes |
|--------|--------|-------|
| Tone | PASS/WARN/FAIL | |
| Audience | PASS/WARN/FAIL | |
| Language | PASS/WARN/FAIL | |

## Factual Accuracy
| Claim | Verified? | Source |
|-------|-----------|--------|
| [Claim 1] | YES/NO/UNVERIFIED | [Where checked] |

## Consistency Check
[Cross-creative consistency notes]

## Issues Found
1. **[SEVERITY]:** [Description] — Line/section: [location]
   - **Fix:** [Suggested correction]

## Approved Copy (if clean)
[The copy text, confirmed safe to send]
```

### Special Client Rules

| Client | Special QA Focus |
|--------|-----------------|
| MarketBeat | NEVER "MarketBeat" in ads (use Early Bird Publishing). NEVER nuclear imagery. Check ROAS claims. |
| Workweek | Subscriber counts must match across all 5 newsletter creatives. V-CAC is the real metric, not raw CPL. |
| The Points Guy | Brand guidelines are extremely strict — TPG brand team reviews everything. |
| Jay Shetty | Personal brand — tone must match Jay's voice exactly. No corporate language. |
| Stocks.News | Financial compliance — no stock predictions, no guaranteed returns. |
| MDhair | Medical claims restrictions — no "cure" language, FDA compliance. |
| Status News | "Qualified Carrd" language — don't oversell the free newsletter. |

## Error Handling

- If Google Drive is unreachable, proceed with available copy and note "Drive not checked"
- If a client has no NEVER rules documented, flag as WARNING ("No NEVER rules on file — consider adding")
- If subscriber counts can't be verified, mark as UNVERIFIED (don't block, but flag)
- Always produce a report even if some checks fail

## What NOT to Do

- Don't rewrite the creative — only flag issues and suggest fixes
- Don't approve copy you're uncertain about — mark as NEEDS REVISION
- Don't send the creative to the client — only QA it
- Don't modify client files
- Don't skip the NEVER rules check — it's the most critical phase
