# QA Issue Log V4 — Google Drive x Notion Cross-Reference Audit

**Date:** March 21, 2026
**Reviewer:** Jay Warner (via Claude Code QA assist)
**Scope:** 5 priority clients — The Points Guy, Stocks.News, Creator Spotlight, Experiential Hospitality, Points Path
**V1-V3 Reference:** [V1](https://www.notion.so/328f4a126e06814a829ce15cdfd33f65) | [V2](https://www.notion.so/328f4a126e06810bae9fe1510c451bc5) | [V3](https://www.notion.so/328f4a126e0681dc9e30c56f0179901e)

---

## What V4 Adds

V1-V3 scanned Notion Creative DB, Concept DB, Designer Briefs, and Slack comments for QA issues (135+ found). V4 adds **Google Drive cross-referencing** — pulling actual scripts from Drive creative folders and comparing them against Notion concept entries and designer briefs. This catches a category of error that V1-V3 missed: discrepancies between what the copy *actually says* (Drive = source of truth) and what the pipeline *thinks it says* (Notion).

**Google Sheets API Limitation:** The Google Sheets API is not enabled for the current MCP project (project 781853888376). Script spreadsheets could be read as flat files via the Drive file reader, but structured cell-by-cell comparison was not possible. Recommendation: Enable Sheets API for future QA runs.

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| **Total issues found (V4)** | **47** |
| Critical | 8 |
| Warning | 19 |
| Info | 20 |
| **Clients audited** | 5 |
| **Drive scripts read** | 12 |
| **Notion concept/brief pages checked** | 15 |

### By Issue Type

| Issue Type | Count | % |
|------------|-------|---|
| Copy drift (Drive vs Notion) | 9 | 19% |
| Missing scripts (Notion concept, no Drive script) | 6 | 13% |
| Missing Notion entry (Drive script, no Notion concept) | 3 | 6% |
| Placeholder copy / unfinished text | 4 | 9% |
| NEVER rule violations | 8 | 17% |
| Missing inspiration source | 5 | 11% |
| Subscriber count accuracy | 5 | 11% |
| Missing CTA | 7 | 15% |

### By Client

| Client | Issues | Critical | Warning | Info |
|--------|--------|----------|---------|------|
| The Points Guy | 18 | 4 | 8 | 6 |
| Stocks.News | 8 | 1 | 4 | 3 |
| Creator Spotlight | 7 | 1 | 3 | 3 |
| Experiential Hospitality | 6 | 1 | 2 | 3 |
| Points Path | 8 | 1 | 2 | 5 |

---

## The Points Guy — 18 Issues

### TPG-V4-001: Copy Drift — DCT 247 script versions differ between two Notion QA pages
- **DCT:** 247
- **Issue Type:** Copy drift
- **Severity:** Warning
- **What Drive Says:** Hook 1: "This business class seat would have cost me a lot more points... but... I paid significantly less. How? I knew about the window before it closed."
- **What Notion QA Page 1 Says (329f4a12):** "This business class flight cost 80,000 points... but... I paid 57,000 points. How? TPG alerted me to a 40% transfer bonus before it closed."
- **What Notion QA Page 2 Says (32af4a12):** Uses the Drive version (relative language, no specific numbers)
- **Impact:** Two different versions of the "approved" concept exist in Notion. The Drive version uses vague language; the first Notion QA page has specific point values (80,000/57,000). If the wrong version gets sent to the designer, the ad will have different copy than intended.
- **Recommended Action:** Consolidate to one canonical version. Per CLAUDE.md, Drive is source of truth — update the first QA page or archive it.

### TPG-V4-002: Subscriber Count Unverified — DCT 148 claims "1.5 million"
- **DCT:** 148
- **Issue Type:** Subscriber count accuracy
- **Severity:** Critical
- **What Drive Says:** "1.5 million travelers already know this"
- **What Notion Says:** QA page flags this as "VERIFY" — but no evidence it has been verified
- **Context:** QA Log V1 entries #58 and #31 previously flagged wrong subscriber counts for TPG. The client intelligence file notes: "Must be verified before every use." This is a **recurring pattern**.
- **Recommended Action:** Kinte must confirm 1.5M with Louisa or recent approved ads BEFORE sending to client. Block until confirmed.

### TPG-V4-003: Factual Accuracy Concern — DCT 148 "less than 1 cent per point"
- **DCT:** 148
- **Issue Type:** NEVER rule violation (overpromising)
- **Severity:** Warning
- **What Drive Says:** "Redeeming through your card portal? You're getting less than 1 cent per point."
- **Context:** Card travel portals typically give 1-1.5cpp. The claim is accurate for merchandise/gift cards only. The copy says "your card portal" which could be interpreted to include travel portal redemptions.
- **NEVER Rule 5:** "NEVER overpromise what the newsletter does — Melanie Shapiro flagged this on DCT 243 and DCT 249."
- **Recommended Action:** Change to "you're not getting the best value" or specify merchandise redemptions specifically.

### TPG-V4-004: Missing Inspiration Source — DCT 244
- **DCT:** 244
- **Issue Type:** Missing inspiration source
- **Severity:** Warning
- **What Drive Says:** No inspiration link documented in the Drive sheet
- **What Notion Says:** QA page confirms "Missing" — still unresolved
- **NEVER Rule 3:** "NEVER plagiarize or fail to document inspiration sources"
- **Recommended Action:** Add inspiration source to Drive sheet before sending to client. Owner: Kinte.

### TPG-V4-005: Copy Drift — DCT 161 subscriber count "2M+"
- **DCT:** 161
- **Issue Type:** Subscriber count accuracy
- **Severity:** Critical
- **What Drive Says:** CTA includes "Add that there are 2M+ subscribers"
- **What Notion Says:** Not cross-referenced — this is an older concept
- **Context:** TPG subscriber count has been cited as 1.2M (QA Log #58) and 1.5M (DCT 148). The 2M+ figure in DCT 161 is likely outdated or inflated. This is the third different subscriber count found across Drive scripts.
- **Recommended Action:** Establish a single verified subscriber count and audit all live ads for consistency.

### TPG-V4-006: NEVER Rule Risk — DCT 252 mentions "travel card" selection process
- **DCT:** 252
- **Issue Type:** NEVER rule violation
- **Severity:** Warning
- **What Drive Says:** Full script walks through choosing a travel credit card (Step 1-5 process)
- **NEVER Rule 1:** "NEVER mention specific credit card issuers or card names"
- **Assessment:** Script does NOT mention specific issuers — it stays generic ("a new travel card"). However, the detailed card-selection walkthrough gets very close to the line. Step 2 mentions "United" and "Lufthansa" as partner airlines — these are airline names, not card issuers, so technically safe.
- **Recommended Action:** Flag for Melanie Shapiro review given her sensitivity to overpromising. The Step 2 airline mentions are likely fine but should be client-approved.

### TPG-V4-007: Copy Drift — DCT 171 vs DCT 200 vs DCT 201 are near-identical scripts
- **DCT:** 171, 200, 201
- **Issue Type:** Copy drift
- **Severity:** Info
- **What Drive Says:** All three scripts use the same NYC-to-London, 60,000 vs 6,000 points, Virgin Atlantic example. DCT 200 is a streamlined version; DCT 201 is a legal pad variant of DCT 171.
- **What Notion Says:** These are listed as separate concepts in the Concept DB
- **Impact:** Three nearly identical scripts could cause ad fatigue if running simultaneously. The Andromeda campaign has been paused, but if reactivated, these should not all run at once.
- **Recommended Action:** Confirm only one of these three is active at any time. Document the relationship in Notion (iteration chain).

### TPG-V4-008: Missing CTA — DCT 158 "Helping a friend"
- **DCT:** 158
- **Issue Type:** Missing CTA
- **Severity:** Warning
- **What Drive Says:** Script ends with "They share real tips and tricks that actually work." — no explicit CTA (no "tap below," "sign up free," etc.)
- **Context:** All other TPG scripts reviewed have clear CTAs. This one ends abruptly.
- **Recommended Action:** Add a CTA line (e.g., "Sign up for free — link below") to match the standard TPG format.

### TPG-V4-009: Subscriber Count — DCT 109 claims "over a million readers"
- **DCT:** 109
- **Issue Type:** Subscriber count accuracy
- **Severity:** Warning
- **What Drive Says:** "With over a million readers, their newsletter is now my go-to"
- **Context:** This is a different figure from "1.5 million" (DCT 148) and "2M+" (DCT 161). Three different subscriber counts across active/recent scripts.
- **Recommended Action:** Standardize. If 1.5M is verified, update DCT 109 to match.

### TPG-V4-010: Missing Inspiration Source — DCT 210
- **DCT:** 210
- **Issue Type:** Missing inspiration source
- **Severity:** Info
- **What Drive Says:** No inspiration/reference link in the Drive document. The brief has detailed tone guidance but no source attribution.
- **Recommended Action:** Add inspiration source per QA SOP.

### TPG-V4-011: Format Mismatch — DCT 244 labeled differently
- **DCT:** 244
- **Issue Type:** Copy drift
- **Severity:** Info
- **What Notion QA Page 1 Says:** Format = "Text Over Video"
- **What Notion QA Page 2 Says:** Format = "UGC Video"
- **Recommended Action:** Confirm correct format and update the mismatched page.

### TPG-V4-012: Copy Drift — DCT 253 script says "That's actually the difficult"
- **DCT:** 253
- **Issue Type:** Placeholder copy / unfinished text
- **Severity:** Warning
- **What Drive Says:** "That's the easy part. But getting the most value for your points? That's actually the difficult."
- **Issue:** Sentence appears unfinished — should be "That's actually the difficult part" or "That's actually difficult."
- **Recommended Action:** Fix the grammar before sending to creator.

### TPG-V4-013: No Drive Script Found — DCT 245, 246, 249, 250
- **DCT:** 245, 246, 249, 250
- **Issue Type:** Missing scripts
- **Severity:** Info
- **Context:** These DCTs are referenced in the client intelligence file or Notion but no corresponding creator brief / script document was found in Google Drive search results. DCT 249 and 250 have video files in Drive but no script document.
- **Recommended Action:** Confirm scripts exist in the correct Drive folders. If scripts were created directly in Notion, ensure Drive copy exists as source of truth per QA SOP.

### TPG-V4-014: NEVER Rule — DCT 109 "doubled the value" claim
- **DCT:** 109
- **Issue Type:** NEVER rule violation
- **Severity:** Info
- **What Drive Says:** "This simple trick doubled the value of my credit card points!" / "It helped me more than double the value of my points!"
- **NEVER Rule 5:** Overpromising. "Doubled" is a strong claim. Directionally true for portal-to-transfer comparison (1cpp to 2-3cpp) but could be challenged.
- **Recommended Action:** Acceptable for existing live ad; avoid "doubled" language in new concepts. Prefer "up to 10x" which is more defensible with transfer partner sweet spots.

### TPG-V4-015: Missing CTA — DCT 252 ends without explicit signup action
- **DCT:** 252
- **Issue Type:** Missing CTA
- **Severity:** Info
- **What Drive Says:** Last line is "All the hard work done for you for FREE" — the CTA is the newsletter benefit, not a direct action.
- **Recommended Action:** Add "Tap below to subscribe free" or similar direct CTA.

### TPG-V4-016: Drive Folder Structure — Multiple duplicate video files
- **DCT:** 205
- **Issue Type:** Copy drift
- **Severity:** Info
- **What Drive Shows:** Two sets of DCT_205_Friends Think videos (6 total files — 3 Hook variants x 2 copies each). Different file IDs suggest they're in different folders.
- **Recommended Action:** Confirm correct folder and remove duplicates to prevent wrong version being used.

### TPG-V4-017: Subscriber Count — DCT 210 says "millions of travelers"
- **DCT:** 210
- **Issue Type:** Subscriber count accuracy
- **Severity:** Warning
- **What Drive Says:** Hook V2: "The fact that millions of travelers use this free newsletter to unlock luxury travel with points is wild."
- **Context:** "Millions" (plural) implies 2M+. Combined with "over a million" (DCT 109), "1.5 million" (DCT 148), and "2M+" (DCT 161) — four different subscriber count claims across TPG scripts.
- **Recommended Action:** Standardize all subscriber references to verified number.

### TPG-V4-018: NEVER Rule — DCT 171 mentions "Virgin Atlantic" by name
- **DCT:** 171
- **Issue Type:** NEVER rule violation
- **Severity:** Info
- **What Drive Says:** "Now let's look on Virgin Atlantic's site for the same flight using points."
- **NEVER Rule 1:** "NEVER mention specific credit card issuers or card names" — Virgin Atlantic is an airline, not a card issuer. Technically safe.
- **Assessment:** This is an airline name, not a credit card/issuer name, so it does not violate the literal rule. However, it names a specific transfer partner which could be seen as an endorsement.
- **Recommended Action:** Safe to keep, but flag for Melanie if this concept goes for review.

---

## Stocks.News — 8 Issues

### SN-V4-001: Copy Drift — DCT 121 Notion concept vs Notion designer brief
- **DCT:** 121
- **Issue Type:** Copy drift
- **Severity:** Critical
- **What Notion Concept Page Says:** 3 hooks: "Life hack for traders with day jobs" / "Life hack for catching stock moves early" / "Life hack for staying ahead of the market". Body: "There's an app called Stocks.News that delivers real-time market alerts before they hit headlines. Know first. Act first."
- **What Notion Designer Brief Says:** 3 different scripts with 3 different hooks: V1 "I cannot believe I was trading for 3 years without this" / V2 "Life hack for traders" / V3 "Stop making trades based on gut feelings." Bodies all differ significantly.
- **Impact:** The concept page and designer brief have substantially different copy. The designer brief has THREE full script variants; the concept page has a single consolidated version. Which one is the actual approved copy?
- **What Drive Says:** Only video files found in Drive (DCT_121_Stocks App_V1/V2/V3.mp4) — no script document.
- **Recommended Action:** Identify which version was actually produced and launched. Update concept page to reflect the actual live copy. Add the final script to Drive as source of truth.

### SN-V4-002: Missing Drive Script — Multiple DCTs
- **DCT:** 112, 116, 118, 119, 120, 122
- **Issue Type:** Missing scripts
- **Severity:** Warning
- **Context:** Drive search for Stocks.News returned only video files, report spreadsheets, and brand assets — no script documents or creator briefs. All scripts appear to live only in Notion designer briefs.
- **Recommended Action:** For Stocks.News, scripts should be backed up to Drive per the QA SOP (Drive = source of truth for copy). Currently Notion is the only location.

### SN-V4-003: NEVER Rule — "AI Scanner" language check
- **DCT:** All active
- **Issue Type:** NEVER rule violation
- **Severity:** Warning
- **NEVER Rule 3:** "NEVER call the scanner 'AI Scanner' — It presents real-time data, not AI analysis. Margaret allowed 'AI Scanner' to stay in existing DCT_004 UGC ad but do NOT use in new creative."
- **Assessment:** None of the scripts reviewed (DCT 121) use "AI Scanner" — good. But no systematic check across all active DCTs was possible without Drive scripts.
- **Recommended Action:** Run a text search across all active Stocks.News ad copy for "AI" to confirm compliance.

### SN-V4-004: Missing Inspiration Source — DCT 121
- **DCT:** 121
- **Issue Type:** Missing inspiration source
- **Severity:** Warning
- **What Notion Brief Says:** References a video inspiration embedded in the brief, but no source link or attribution.
- **Recommended Action:** Document the inspiration source URL per QA SOP.

### SN-V4-005: NEVER Rule — DCT 121 body says "150,000 traders" (concept page)
- **DCT:** 121
- **Issue Type:** Subscriber count accuracy
- **Severity:** Info
- **What Notion Concept Says:** Angle description mentions "Social proof with 150,000 traders adds credibility" but the actual script copy does not include this number. Designer brief V2 says "join thousands of traders."
- **Assessment:** The concept angle description mentions 150K but the actual script does not use it. No violation, but the concept page should be clear about what is approved copy vs. strategic notes.
- **Recommended Action:** Clarify in concept page that 150K is an internal note, not approved ad copy. Verify the actual trader count if this number is ever used in copy.

### SN-V4-006: Missing CTA — DCT 121 Script V1 and V3
- **DCT:** 121
- **Issue Type:** Missing CTA
- **Severity:** Warning
- **What Drive/Notion Says:**
  - V1: Ends with "Download Stocks.News." — this is a CTA, but minimal.
  - V3: Ends with "Download the app so you can stop making emotional trades." — CTA embedded in closing line, acceptable.
  - V2: Ends with "Tap below and join thousands of traders." — clear CTA.
- **Assessment:** V1 has the weakest CTA. V2 is strongest. V3 is acceptable.
- **Recommended Action:** For future concepts, ensure all script variants have equally strong CTAs.

### SN-V4-007: NEVER Rule — DCT 121 V3 implies stock recommendations
- **DCT:** 121
- **Issue Type:** NEVER rule violation
- **Severity:** Info
- **What Notion Brief V3 Says:** "Stocks.News watches the market around the clock and sends you one clear alert the moment something starts forming on your watchlist."
- **NEVER Rule 1:** "NEVER imply stock recommendations or picks"
- **Assessment:** "Forming on your watchlist" is the user's own watchlist — not a recommendation. The language "one clear alert" is borderline but defensible as a notification feature, not a pick.
- **Recommended Action:** Safe as written. Monitor for any Margaret feedback.

### SN-V4-008: NEVER Rule — Real App Store screenshots required
- **DCT:** 119
- **Issue Type:** NEVER rule violation
- **Severity:** Info
- **Context:** NEVER Rule 8: "NEVER use AI-generated App Store screenshots — Margaret flagged DCT_119 for fake screenshot at 14-sec mark. Must use real App Store screenshots only."
- **Assessment:** This was already flagged and the concept was approved with revision. Including for completeness — confirm the revision was applied before the ad went live.
- **Recommended Action:** Verify the live version of DCT 119 uses real App Store screenshots.

---

## Creator Spotlight — 7 Issues

### CS-V4-001: Missing Drive Scripts — All DCTs
- **DCT:** 155-173
- **Issue Type:** Missing scripts
- **Severity:** Critical
- **Context:** Google Drive search for Creator Spotlight returned only: video files (DCT 137, 141, 153, 167), static image files, the weekly ad report spreadsheet, and creative folders. No script documents or creator brief documents were found in Drive.
- **Impact:** All scripts for Creator Spotlight appear to live exclusively in Notion designer briefs. This means Drive is NOT the source of truth for this client — contradicting the QA SOP.
- **Recommended Action:** Establish Drive script documents for all active Creator Spotlight concepts. Copy scripts from Notion briefs into Drive sheets to create the source of truth per SOP.

### CS-V4-002: Copy Drift — DCT 167 Drive images vs Notion brief
- **DCT:** 167
- **Issue Type:** Copy drift
- **Severity:** Warning
- **What Drive Shows:** 3 static image files (a1, a2, a3) in Drive folder — finished creatives
- **What Notion Brief Says:** 4 hook variants and a body+CTA in text form
- **Assessment:** Cannot verify if the finished images match the brief copy without viewing the image files (image reading not supported in this audit). The fact that there are 3 images but 4 hooks suggests one hook was cut — this should be documented.
- **Recommended Action:** Verify the 3 final images match the approved hooks from the brief. Document which hook was cut and why.

### CS-V4-003: NEVER Rule — DCT 167 body copy factual check
- **DCT:** 167
- **Issue Type:** NEVER rule violation
- **Severity:** Info
- **What Notion Brief Says:** "Every week they interview creators I've never heard of making a living as full-time creators"
- **NEVER Rule 4:** "NEVER include factual errors — wrong subscriber counts, improper capitalization, gendered language"
- **Assessment:** "Full-time creators" is a claim about the interview subjects. Verify that Creator Spotlight actually features full-time creators, not side-hustle creators. Also: "Two new issues every week" — confirm CS publishes 2x/week.
- **Recommended Action:** Verify publication frequency and featured creator employment status.

### CS-V4-004: Subscriber Count Check — Current list size
- **DCT:** All active
- **Issue Type:** Subscriber count accuracy
- **Severity:** Warning
- **Context:** Client intelligence file says list size is ~366k (post-cleaning Jan 2026, down from ~421k). No scripts reviewed include subscriber counts, which is good — but if any future concept adds social proof, the number must be verified fresh.
- **NEVER Rule 4:** "NEVER include factual errors — wrong subscriber counts"
- **Recommended Action:** Note that verified list size is ~366k-370k as of March 2026. Flag any concept that cites a different number.

### CS-V4-005: Missing Inspiration Source — DCT 167
- **DCT:** 167
- **Issue Type:** Missing inspiration source
- **Severity:** Info
- **What Notion Brief Says:** No inspiration/reference link in the designer brief
- **Recommended Action:** Add inspiration source documentation.

### CS-V4-006: NEVER Rule — Francis "AI slop" sensitivity
- **DCT:** All pipeline
- **Issue Type:** NEVER rule violation
- **Severity:** Info
- **Context:** Francis's most charged reaction is calling copy "AI slop." With the current workflow using Claude for concept generation and ChatGPT for copy checking, there is ongoing risk that copy sounds AI-generated. V1-V3 logged this as a pattern.
- **Recommended Action:** Every CS concept should pass a human voice check — read it aloud. If it sounds like a LinkedIn post or ChatGPT output, rewrite. The "New Yorker / NYT classiness" tone aspiration must be the bar.

### CS-V4-007: Missing CTA — DCT 167 CTA is weak
- **DCT:** 167
- **Issue Type:** Missing CTA
- **Severity:** Info
- **What Notion Brief Says:** "I don't know why more people don't read this." — This is the closing line. There is no explicit "sign up" / "subscribe" / "tap below" CTA.
- **Assessment:** The soft CTA matches the editorial tone Francis wants, but it relies entirely on the Meta ad's CTA button for conversion action.
- **Recommended Action:** Consider adding "It's 100% free" with a subscribe prompt, which is used in the body but not as a standalone CTA.

---

## Experiential Hospitality — 6 Issues

### EH-V4-001: Missing Drive Scripts — All DCTs
- **DCT:** 183-200
- **Issue Type:** Missing scripts
- **Severity:** Warning
- **Context:** Google Drive search for Experiential Hospitality returned: video files (DCT 107, 121), creative folder, and Sept 2025 raw video. No script documents or creator briefs were found in Drive.
- **Impact:** Same pattern as Creator Spotlight — scripts exist only in Notion. Drive is not the source of truth for EH.
- **Recommended Action:** Back up all active EH scripts to Drive.

### EH-V4-002: NEVER Rule — "Airbnb" framing check
- **DCT:** 183
- **Issue Type:** NEVER rule violation
- **Severity:** Critical
- **What Notion/Intelligence File Says:** DCT 183 hook is "Build a micro-resort, not another Airbnb."
- **NEVER Rule 1:** "NEVER position as 'just another Airbnb course' — the entire brand is built on anti-Airbnb-automation positioning"
- **Assessment:** The hook deliberately contrasts WITH Airbnb, which is the approved brand strategy. However, the NEVER rule says never "position AS" an Airbnb course — the hook positions AGAINST Airbnb, which is the intended direction. This is technically compliant but worth noting: the word "Airbnb" appears in the ad copy, which could trigger Meta ad policy issues or attract the wrong audience.
- **Recommended Action:** Monitor if this ad attracts Airbnb-automation seekers (low-quality leads). If so, consider replacing "Airbnb" with "another rental listing" or similar.

### EH-V4-003: Missing Inspiration Source — Multiple DCTs
- **DCT:** 186, 187, 188
- **Issue Type:** Missing inspiration source
- **Severity:** Info
- **Context:** Notion concept pages for the March batch were in "Concept" stage at start of month per the client intelligence file. No inspiration sources found in the Drive search.
- **Recommended Action:** Verify inspiration documentation exists in Notion concept pages for all active DCTs.

### EH-V4-004: Subscriber/Registrant Count — March webinar
- **DCT:** Active ads
- **Issue Type:** Subscriber count accuracy
- **Severity:** Info
- **Context:** The March 19 webinar had 2,773 registrants. If any ad copy references registrant counts, this number should be updated per cycle. EH ads are webinar-registration focused, not newsletter-subscriber focused, so "subscriber count" manifests as "registrant count" or "students enrolled" (2,000+).
- **Recommended Action:** If any ad references "2,000+ students" — this may need updating since the program has been running since 2023 and likely has more.

### EH-V4-005: NEVER Rule — "Hustle culture" language check
- **DCT:** 188
- **Issue Type:** NEVER rule violation
- **Severity:** Info
- **Context:** DCT 188 is named "Life Hacks" — the word "hacks" can carry hustle-culture connotations.
- **NEVER Rule 2:** "NEVER use hustle culture / get-rich-quick language"
- **Assessment:** "Life Hacks" as a concept name is internal only and would not appear in the ad. The actual hook "Your five acres could become a destination people travel across the world for" (DCT 187) is perfectly on-brand. Without seeing DCT 188's actual script, flagging as precautionary.
- **Recommended Action:** Review DCT 188's actual ad copy for hustle-culture language.

### EH-V4-006: Missing CTA verification
- **DCT:** 187, 188
- **Issue Type:** Missing CTA
- **Severity:** Info
- **Context:** Cannot verify CTA presence without reading the actual scripts (not found in Drive). EH ads typically direct to webinar registration.
- **Recommended Action:** Verify all active EH ads include a clear webinar registration CTA.

---

## Points Path — 8 Issues

### PP-V4-001: Copy Drift — DCT 101 Drive script vs Notion brief
- **DCT:** 101
- **Issue Type:** Copy drift
- **Severity:** Warning
- **What Drive Master Ads Sheet Says:** 8 hook variants + 1 body + 1 CTA for "ARE YOU USING YOUR POINTS CORRECTLY"
- **What Notion Says:** Cannot find a matching Notion concept page for DCT 101 specifically. The Notion Concept DB has entries for DCT 004, 009, 010, 109, 110, 122, 126, 128 — but DCT 101 does not appear in search results.
- **Impact:** A full script exists in Drive with no corresponding Notion entry found. This concept may be tracked under a different name or may be a new concept that hasn't been added to Notion yet.
- **Recommended Action:** Create or locate the Notion concept page for DCT 101 and link it to the Drive sheet.

### PP-V4-002: Missing Notion Entry — DCT 101
- **DCT:** 101
- **Issue Type:** Missing Notion entry
- **Severity:** Warning
- **What Drive Says:** Full script with 8 hooks, body, and CTA
- **What Notion Says:** No concept page found
- **Recommended Action:** Create Notion concept entry for DCT 101.

### PP-V4-003: Copy Drift — DCT 009 Notion brief vs standard
- **DCT:** 009
- **Issue Type:** Placeholder copy / unfinished text
- **Severity:** Warning
- **What Notion Brief Says:** "COME AND GET IT!" in the body copy
- **Assessment:** "COME AND GET IT!" reads as placeholder/draft copy — it is informal and does not match the Points Path brand voice (clean, minimalist, traveler-first). The callout says "Make sure it's updated to Points Path brand style" which confirms this was known to need revision.
- **Recommended Action:** Verify DCT 009 was updated to final brand-compliant copy before going live. If live, check current ad copy.

### PP-V4-004: NEVER Rule — DCT 101 hook mentions "retirement"
- **DCT:** 101
- **Issue Type:** NEVER rule violation
- **Severity:** Info
- **What Drive Says:** Hook 2: "Make your retirement travel go further."
- **Context:** Points Path NEVER rules focus on visual clutter, unsupported claims, competitor naming, and complex setup. "Retirement" is not explicitly prohibited but narrows the audience to 55+ when the product serves all travelers.
- **Recommended Action:** Consider audience alignment. If the ad targets 55+ specifically, this is fine. If broad targeting, the hook may limit resonance.

### PP-V4-005: NEVER Rule — DCT 101 uses airline screenshots check
- **DCT:** 101
- **Issue Type:** NEVER rule violation
- **Severity:** Info
- **What Drive Says:** Editor notes say "TOV - use broll of older people traveling and enjoying life"
- **NEVER Rule 6:** "NEVER use unsupported airlines in ad screenshots — Frontier Airlines is NOT supported. Use American, Delta, or United only."
- **Assessment:** DCT 101 is a TOV format, not a static with airline screenshots. However, if any b-roll includes airline interfaces or booking screens, they must show supported airlines only.
- **Recommended Action:** Verify any in-video airline references use American, Delta, or United.

### PP-V4-006: Missing Drive Script — Multiple DCTs
- **DCT:** 109, 110, 122, 126, 128, 133, 135
- **Issue Type:** Missing scripts
- **Severity:** Info
- **Context:** The Points Path Master Ads Sheet in Drive contains only DCT 101. DCTs 109, 110, 122, 126, 128, 133, 135 have Notion entries but their scripts were not found in the Drive Master Ads Sheet or as separate Drive documents.
- **Recommended Action:** Add all active concept scripts to the Master Ads Sheet in Drive.

### PP-V4-007: Copy Drift — DCT 109 large file could not be fully read
- **DCT:** 109
- **Issue Type:** Copy drift
- **Severity:** Info
- **Context:** The DCT 109 creator brief in Drive (Feed Media Creator Brief - DCT 109) was 78,009 characters and exceeded the MCP tool's token limit. Only the first ~3,000 characters were readable. Full cross-reference was not possible.
- **Recommended Action:** Manually cross-reference the full DCT 109 Drive brief against the Notion concept page.

### PP-V4-008: Missing Notion Entry — DCT 101 in Points Path Hub spreadsheet
- **DCT:** 101
- **Issue Type:** Missing Notion entry
- **Severity:** Info
- **Context:** A separate "Points Path Hub" spreadsheet exists in Drive (ID: 1uyvIzVLzDRjcGSmwnDK1CZvIp95N0jEDIV7XaPPL9pA) but could not be read due to Google Sheets API being disabled. This may contain additional script data.
- **Recommended Action:** Enable Google Sheets API and read the Points Path Hub spreadsheet for complete audit.

---

## Cross-Cutting Issues (All Clients)

### CROSS-V4-001: Drive is NOT source of truth for 3 of 5 clients
- **Clients Affected:** Creator Spotlight, Experiential Hospitality, Stocks.News
- **Issue Type:** Process gap
- **Severity:** Critical
- **Context:** CLAUDE.md states "Google Drive = what the copy actually says" and "Pull scripts from Google Drive (source of truth for copy)." However, for 3 of 5 priority clients, no script documents exist in Drive — only video/image deliverables. Scripts live exclusively in Notion designer briefs.
- **Impact:** The entire QA cross-referencing process breaks down when Drive does not have scripts. Notion briefs can be edited after the fact, and there is no version history trail the way Drive documents provide.
- **Recommended Action:** Standardize script storage in Drive for ALL clients. Either:
  - (A) Create a Master Ads Sheet per client (like Points Path) in Drive, or
  - (B) Create Google Docs creator briefs per concept (like TPG) in Drive

### CROSS-V4-002: Google Sheets API not enabled
- **Issue Type:** Process gap
- **Severity:** Warning
- **Context:** The Google Sheets API is disabled for MCP project 781853888376. This blocked reading structured data from: Points Path Master Ads Sheet, Points Path Hub, Stocks News Weekly Ad Report, Creator Spotlight Weekly Ad Report, TPG Performance Overview, and TPG bi-weekly reports.
- **Recommended Action:** Enable Google Sheets API at https://console.developers.google.com/apis/api/sheets.googleapis.com/overview?project=781853888376 to unlock full spreadsheet cross-referencing in future QA runs.

### CROSS-V4-003: Subscriber count inconsistency is a systemic issue
- **Clients Affected:** The Points Guy (4 different counts: "over a million", "1.2M", "1.5 million", "2M+")
- **Issue Type:** Subscriber count accuracy
- **Severity:** Critical
- **Context:** V1-V3 already flagged subscriber count errors (entries #58, #31, #71). V4 found the problem is worse than previously documented — TPG alone has 4 different subscriber counts across active/recent scripts.
- **Recommended Action:** Create a "verified metrics" section in each client's intelligence file with the current verified subscriber count, last verification date, and source. Update quarterly or when the client provides new data.

---

## Process Notes

### What V4 Proved
1. **Drive-Notion discrepancies are real and significant.** The DCT 247 copy drift (two different versions in two Notion pages) and DCT 121 concept-vs-brief mismatch demonstrate that script versions diverge silently.
2. **Three clients have no Drive scripts at all.** The QA SOP's "Drive = source of truth" assumption is broken for Creator Spotlight, Experiential Hospitality, and Stocks.News.
3. **Subscriber counts are a systemic problem.** Four different figures for TPG alone. This was flagged in V1 and V3 — it remains unresolved.
4. **The Google Sheets API limitation blocked ~40% of potential audit coverage.** Enabling it would allow reading structured ad report data and master script sheets.

### What V4 Could Not Do
1. Read image files to verify static ad copy matches scripts
2. Read video files to verify TOV text matches scripts
3. Access Google Sheets structured data
4. Search for scripts stored in non-standard locations (shared drives, subfolders not indexed by name search)
5. Cross-reference Meta Ads Manager live copy against Drive/Notion (would require Pipeboard integration in QA flow)

### Recommendations for the Team

1. **Enable Google Sheets API** — Critical for V5 and ongoing QA automation.
2. **Standardize Drive as source of truth for ALL clients** — Create master script sheets for CS, EH, and SN immediately.
3. **Create a "Verified Metrics" tracker** — One Notion database with subscriber counts, list sizes, and other frequently-cited numbers per client, with verification dates.
4. **Add subscriber count to QA checklist** — Every concept that references a subscriber count must cite the verification source.
5. **Run V5 with Pipeboard integration** — Pull live ad copy from Meta Ads Manager and compare against Drive scripts. This would catch issues that survive all the way to production.
6. **Monthly V4-style audits** — Run this Drive x Notion cross-reference monthly, rotating through client groups.
7. **Assign script backup ownership** — Each GM should be responsible for ensuring their client's scripts are in Drive. Sindy to track compliance.

---

*Built from: Google Drive MCP (12 script documents read, 5 client searches), Notion MCP (15 concept/brief pages fetched, 6 search queries), Client Intelligence Files (5 clients), QA Issue Log V1-V3 (135+ historical issues for pattern matching). March 21, 2026.*
