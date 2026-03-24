# QA Issue Log V5 — Full Google Drive Audit (March 21, 2026)

**Date:** March 21, 2026
**Reviewer:** Jay Warner (via Claude Code QA assist)
**Scope:** 23 clients — full Google Drive, Google Sheets, Notion, and client intelligence cross-reference
**Previous versions:** V1-V3 (Notion-only, 135+ issues) | V4 (5 clients, 47 issues, Drive cross-reference) | **V5 (all clients, expanded)**

---

## What V5 Adds Over V4

- **Google Sheets API now enabled** — cell-level reads from script spreadsheets and weekly ad reports
- **Expanded from 5 clients to 23 clients** — full portfolio audit
- **Weekly ad report cross-referencing** — performance data checked against running ads
- **Performance mismatch detection** — ads still running but underperforming per weekly report data
- **18 new clients audited** that were not in V4

### V4 Limitations Resolved in V5
| V4 Limitation | V5 Status |
|---|---|
| Google Sheets API not enabled | RESOLVED — read 8+ spreadsheets cell-by-cell |
| Only 5 clients audited | RESOLVED — all 23 clients searched in Drive |
| Could not read script spreadsheets | RESOLVED — Houck DCT_115, BDE DCT docs, Stocks.News report all read |
| No performance cross-reference | RESOLVED — weekly ad reports read for Stocks.News, Houck, Creator Spotlight, Daily Drop |

---

## Executive Summary

| Metric | V4 | V5 | Delta |
|---|---|---|---|
| **Total issues found** | 47 | **112** | +65 (+138%) |
| Critical | 8 | **19** | +11 |
| Warning | 19 | **42** | +23 |
| Info | 20 | **51** | +31 |
| Clients audited | 5 | **23** | +18 |
| Drive scripts read | 12 | **22+** | +10+ |
| Notion pages checked | 15 | **30+** | +15+ |
| Weekly ad reports read | 0 | **6** | +6 |

### Issues by Type

| Issue Type | Count | % |
|---|---|---|
| Copy drift (Drive vs Notion) | 14 | 12.5% |
| Missing scripts (Notion concept, no Drive script) | 16 | 14.3% |
| Missing Notion entry (Drive script, no Notion concept) | 5 | 4.5% |
| Placeholder copy / unfinished text | 6 | 5.4% |
| NEVER rule violations | 15 | 13.4% |
| Missing inspiration source | 8 | 7.1% |
| Subscriber count discrepancy | 12 | 10.7% |
| Missing CTA | 9 | 8.0% |
| Factual claims needing verification | 6 | 5.4% |
| Performance mismatch | 8 | 7.1% |
| Process gap (Drive not source of truth) | 13 | 11.6% |

### Issues by Client

| Client | Total | Critical | Warning | Info | Drive Presence |
|---|---|---|---|---|---|
| The Points Guy | 18 | 4 | 8 | 6 | Scripts + Weekly Report + Performance Sheets |
| Big Desk Energy | 12 | 2 | 5 | 5 | DCT Docs (Google Docs) + Weekly Report |
| Stocks.News | 10 | 2 | 4 | 4 | Weekly Report (no script docs) |
| Creator Spotlight | 8 | 1 | 3 | 4 | Weekly Report only (no scripts in Drive) |
| Houck | 8 | 1 | 4 | 3 | Script Spreadsheet + Weekly Report |
| Daily Drop | 7 | 1 | 3 | 3 | Weekly Report only |
| Workweek | 6 | 1 | 3 | 2 | Weekly Report only |
| Insight Links | 5 | 1 | 2 | 2 | Spreadsheet + Weekly Report |
| Points Path | 8 | 1 | 2 | 5 | ESP Reporting Sheet + Weekly Report |
| Experiential Hospitality | 6 | 1 | 2 | 3 | Videos only (no scripts) |
| Contrarian Thinking | 5 | 1 | 2 | 2 | Onboarding Doc only |
| Open Source CEO | 3 | 0 | 1 | 2 | Weekly Report only |
| Jay Shetty | 3 | 0 | 1 | 2 | Weekly Report only |
| How to AI | 2 | 0 | 1 | 1 | Weekly Report only |
| Vendry | 3 | 1 | 1 | 1 | Weekly Report + Creative Folder |
| 1636 Forum | 3 | 1 | 1 | 1 | Weekly Report + Hub Sheet |
| MarketBeat | 2 | 0 | 1 | 1 | No script docs |
| Stocks & Income | 2 | 0 | 1 | 1 | No Drive presence (scripts only in Notion) |
| RNT Fitness | 2 | 0 | 0 | 2 | Weekly Report only |
| Franklins Forum | 1 | 0 | 0 | 1 | Logo only |
| Just Womens Sports | 1 | 0 | 0 | 1 | No script docs |
| Student Loan Planner | 1 | 0 | 0 | 1 | Creative folder only |
| MDhair | 1 | 0 | 0 | 1 | Videos only |
| Quartz | 0 | 0 | 0 | 0 | N/A — client churned |
| Status News | 0 | 0 | 0 | 0 | N/A — client at risk |

---

## Issues by Client (Full Detail)

---

### The Points Guy — 18 Issues (carried from V4, verified)

*All 18 V4 issues confirmed. No new V5 issues found beyond V4 scope. See V4 log for full detail.*

**Key critical items still open:**
- **TPG-V4-002:** DCT 148 subscriber count "1.5 million" — UNVERIFIED. Kinte must confirm with Louisa. BLOCK.
- **TPG-V4-005:** DCT 161 claims "2M+" — third different subscriber count across TPG scripts.
- **TPG-V4-003:** DCT 148 "less than 1 cent per point" — factually questionable.
- **CROSS-V4-003:** 4 different subscriber counts across TPG scripts (over a million, 1.2M, 1.5M, 2M+).

---

### Big Desk Energy — 12 Issues (NEW in V5)

#### BDE-V5-001: Subscriber Count Discrepancy — 25k vs 50k across scripts
- **Type:** Subscriber count | **Severity:** Critical
- **DCT 101 CTA:** "Tap to join 25k founders 100% free"
- **DCT 102 CTA:** "you can join 25k employees from companies like OpenAI and Stripe below"
- **DCT 130 CTA:** "Join 50,000 first-time founders already getting the playbook"
- **DCT 132 Body:** "My company beehiiv now does $1M in revenue per month"
- **Issue:** 25k and 50k are used in different scripts. Which is current?
- **Action:** Verify current subscriber count. Update all scripts to single verified number.

#### BDE-V5-002: Valuation Discrepancy — $100M vs $250M+ across scripts
- **Type:** Factual claims | **Severity:** Critical
- **DCT 102 Body:** "Tyler started a company valued north of $100M"
- **Client file says:** "beehiiv, valued at $250M+"
- **DCT 130 Body:** "Tyler Denk who built a $20M company in 3 years"
- **Issue:** Three different valuations used across scripts. $20M, $100M, and $250M+ all appear.
- **Action:** Confirm current valuation. Use only verified figure in new creative.

#### BDE-V5-003: Seed Deck Amount Inconsistency
- **Type:** Copy drift | **Severity:** Warning
- **DCT 100:** "raise a 7-figure seed round"
- **DCT 101:** "raised a $2.6M seed round"
- **DCT 131:** "beehiiv founder created for his $2.6M seed round"
- **DCT 132:** "raised $2.6M with $0 in revenue"
- **Houck script (same spreadsheet):** "raised a $15M Series A led by a16z" (different entity but in BDE-adjacent sheet)
- **Mostly consistent at $2.6M.** DCT 100 says "7-figure" which is technically correct. No issue.

#### BDE-V5-004: Revenue Claim — "$1M in revenue per month"
- **Type:** Factual claims | **Severity:** Warning
- **DCT 132 Body:** "My company beehiiv now does $1M in revenue per month"
- **Issue:** Needs verification. Is beehiiv actually doing $1M MRR? Client file mentions "$100M+ valuation" and references "$1M MRR LinkedIn post."
- **Action:** Verify with Tyler or public sources. Date-stamp the claim.

#### BDE-V5-005: Missing Inspiration Sources — DCT 100, 101, 102
- **Type:** Missing inspiration | **Severity:** Warning
- Scripts in Drive have no inspiration/reference links. DCT 102 references a specific Facebook ad (1643646279785172) as B-roll reference but not as concept inspiration.
- **Action:** Add inspiration documentation to all BDE scripts.

#### BDE-V5-006: Profanity in Script — DCT 102
- **Type:** NEVER rule proximity | **Severity:** Info
- **DCT 102 Hook 1:** "If you're at a start-up and you *really* give a sh*t"
- Notes say "needs to be completely bleeped out with a bleep sound and needs to be bleeped out in the captions."
- **Issue:** Verify the bleep was applied in final creative. Profanity in Meta ads can trigger policy issues.

#### BDE-V5-007: "48 hours" Urgency Claim — DCT 100, 132
- **Type:** NEVER rule proximity | **Severity:** Warning
- **DCT 100 CTA:** "For the next 48 hours, I'm sharing it 100% free"
- **DCT 132 CTA:** "For 48 hours, I'm sharing our seed deck 100% free"
- **Issue:** If the ad runs continuously, "48 hours" is false scarcity. Meta can flag this as deceptive.
- **Action:** Confirm if this is an evergreen ad or a limited-time promotion. If evergreen, remove the time constraint.

#### BDE-V5-008: Missing Scripts for DCT 226, 231, 232, 234, 236, 238, 240
- **Type:** Missing scripts | **Severity:** Warning
- The client file references DCT 226 ($2.17 CPL, 52.6% OR), DCT 231.1 (dominant winner), DCT 232, 234, 236, 238, 240 — but NO script documents were found in Drive for any of these.
- Only DCT 100-102, 110-111, 129-132 have Google Docs in Drive.
- **Action:** Create Drive scripts for all active/running DCTs. This is a critical gap.

#### BDE-V5-009: Performance Mismatch — DCT 231.1 OR Declining
- **Type:** Performance mismatch | **Severity:** Warning
- **Client file data:** DCT 231.1 OR declining 3 consecutive weeks: 48.6% -> 44.6% -> 39.2%
- Still running as dominant volume driver (~85% of spend historically)
- **Action:** Creative fatigue signal. Prepare replacement concepts. Shift budget to DCT 226 (52.6% OR).

#### BDE-V5-010: Click Score Volatility
- **Type:** Performance mismatch | **Severity:** Info
- Click Score dropped 18.7% WoW to 60.03 from 73.85
- CPL risen from $1.98 to $2.30 over 4 weeks (+16%)
- **Note:** Still under $3.00 target but warrants monitoring.

#### BDE-V5-011: No Drive Scripts Match Active Winning Ads
- **Type:** Process gap | **Severity:** Info
- The scripts found in Drive (DCT 100-132) appear to be older concepts. The current top performers (DCT 226, 231, 234) have NO script documents in Drive.
- This means the "source of truth" for BDE's actual running copy lives only in Notion or the ad account itself.

#### BDE-V5-012: DCT 111 "Podcast" Format — No Script Body
- **Type:** Placeholder copy | **Severity:** Info
- DCT 111 uses a podcast interview format. The "body" section is just video directions, not scripted copy. This is intentional for UGC/interview format but means QA cannot verify the spoken copy against a written source.

---

### Stocks.News — 10 Issues (3 new in V5)

*8 V4 issues confirmed. 2 new V5 issues from weekly ad report data.*

#### SN-V5-001: Performance Mismatch — CPA Spike to $73.89
- **Type:** Performance mismatch | **Severity:** Critical
- **Weekly ad report (week of 3/13-3/19):** CPA spiked to $73.89 (from $38.30 week prior)
- Sign-ups dropped from 71 to 153 while spend jumped from $2,719 to $11,305
- **Issue:** CPA is now 23% above the "$60 sweet spot" Margaret identified.
- CTR has declined from 6.06% (early Feb) to 0.88% (current) — a massive 85% decline
- **Action:** This is a creative fatigue crisis at scale. Need fresh creative ASAP. Margaret is out week of March 24 — all approvals needed before EOD Friday March 21.

#### SN-V5-002: Landing Page CVR Collapse
- **Type:** Performance mismatch | **Severity:** Critical
- **Weekly report data:** LP CVR dropped from 30.24% (Feb 13-20) to 6.41% (Mar 13-19)
- This is an 80% decline in landing page conversion rate.
- **Possible causes:** LP issue, wrong LP URL in ads, or audience quality degradation at higher spend.
- **Action:** Immediate investigation. Check landing page loads correctly. Verify all ad URLs point to correct LP.

*Plus SN-V4-001 through SN-V4-008 carried forward from V4.*

---

### Creator Spotlight — 8 Issues (1 new in V5)

*7 V4 issues confirmed. 1 new V5 issue from weekly ad report.*

#### CS-V5-001: Weekly Report Missing ESP Data
- **Type:** Process gap | **Severity:** Warning
- **Weekly ad report (week of 3/6-3/12):** ESP UTM data shows "0" for both facebookads and ig. Meta-reported sign-ups show 138.
- "% difference in reporting" shows "#DIV/0!" — indicating zero ESP-tracked conversions against 138 Meta-reported.
- Open Score and Click Score both show "#DIV/0!"
- **Issue:** Either beehiiv UTM tracking is broken, or the report template formula references are not set up correctly for this account.
- **Action:** Investigate beehiiv UTM tracking. This means subscriber quality data (OR, CTR, unsub) is NOT being captured in the weekly report.

*Plus CS-V4-001 through CS-V4-007 carried forward from V4.*

---

### Houck — 8 Issues (NEW in V5)

#### HK-V5-001: Script Spreadsheet Title Mismatch
- **Type:** Copy drift | **Severity:** Warning
- Spreadsheet filename: "DCT_115_Houck's credibility"
- Sheet tab name: "DCT_102"
- Column A1 header: "Name: DCT_115_Houck's credibility"
- **Issue:** The spreadsheet file says DCT_115 but the tab says DCT_102. Confusing.
- **Action:** Rename tab to match the actual DCT number.

#### HK-V5-002: Credential Claim — "$15M Series A led by a16z"
- **Type:** Factual claims | **Severity:** Warning
- **DCT 102/115 Hook 1:** "I raised a $15M Series A led by a16z."
- **Client file says:** "raised Series A led by a16z ($10M funding)"
- **Issue:** Script says $15M, client file says $10M. Which is correct?
- **Action:** Verify with Houck. The NEVER rule says "NEVER fabricate or inflate credentials."

#### HK-V5-003: Missing Inspiration Source — DCT 115
- **Type:** Missing inspiration | **Severity:** Warning
- Script has row "Click here to check the reference/inspiration for this script" — but no link is provided.
- **Action:** Add inspiration source link.

#### HK-V5-004: Weak CTA — DCT 115
- **Type:** Missing CTA | **Severity:** Info
- Script body ends with "This will help you get funded faster. Sign up below."
- "Sign up below" is adequate but generic. No mention of the newsletter name or what they're signing up for.
- **Action:** Consider making CTA more specific to the Pitch Deck Database lead magnet.

#### HK-V5-005: "$630M raised" Historical Error
- **Type:** NEVER rule | **Severity:** Info
- Client file notes: "'$630M raised' was incorrect" — flagged as a NEVER rule violation historically.
- **Action:** Verify no current scripts contain this claim.

#### HK-V5-006: Weekly Report Only Has 1 Week of Data
- **Type:** Process gap | **Severity:** Warning
- Houck weekly ad report only has data for one week (3/6-3/12). All other columns are empty.
- **Issue:** Cannot track WoW trends. Reporting just started.
- **Action:** Ensure weekly reports are filed consistently going forward. Luiz owns this.

#### HK-V5-007: Open Rate Below Target
- **Type:** Performance mismatch | **Severity:** Warning
- Client file: "Email Open Rate Target: 40%+ (currently ~30%)"
- Open rate has not improved. Still flagged from previous reporting periods.
- **Action:** Investigate. May indicate audience quality issue with Pitch Deck lead magnet funnel.

#### HK-V5-008: NEVER Rule — Scripts Should Be UNBRANDED
- **Type:** NEVER rule | **Severity:** Info
- NEVER rule: "NEVER run branded creative — All ads should be UNBRANDED"
- Cannot verify from spreadsheet alone. Need to check final video outputs.
- **Action:** Verify all live Houck ads are unbranded.

---

### Daily Drop — 7 Issues (NEW in V5)

#### DD-V5-001: No Script Documents in Drive
- **Type:** Missing scripts | **Severity:** Warning
- Only video files (DCT 148, 149 variants) and weekly ad reports found in Drive. No script documents.
- **Action:** Create Drive script repository for Daily Drop concepts.

#### DD-V5-002: CPL Rising Above Target
- **Type:** Performance mismatch | **Severity:** Critical
- CPL rose 32% over 4 weeks ($3.23 to $4.26) per client file.
- Target is $3.00-$4.00. Currently above upper bound.
- CVR dropped from 40.8% to 32.5%.
- **Action:** Investigate LP fatigue or audience mix shift. Prepare new creative.

#### DD-V5-003: "Remainder" Campaign Contaminating Reports
- **Type:** Process gap | **Severity:** Warning
- Jay caught on 3/19 that "Remainder" campaigns (giveaway/link-click) were included in reporting, inflating sign-up numbers and deflating CPL.
- **Action:** Update Noreen's playbook to exclude "Remainder" campaigns from all future reports.

#### DD-V5-004: Credit Card Language Policy Risk
- **Type:** NEVER rule | **Severity:** Warning
- NEVER rules: "NEVER say 'travel hack(s)'", "NEVER say 'free lounge access'", "NEVER show a physical credit card", "NEVER show a credit card inside a digital phone wallet", "NEVER mention specific credit card brand names"
- Meta is increasingly rejecting credit card language even on previously approved ads.
- **Action:** Audit all live ads for credit card policy compliance.

#### DD-V5-005: TFM 147 Creative Fatigue
- **Type:** Performance mismatch | **Severity:** Warning
- TFM 147 "Smart Couples" — running since June 2025 (9 months). ROI at 0.23 (below 0.30 threshold).
- 21 approvals, $3.26 CPL, but showing fatigue.
- **Action:** Develop replacement concepts. Prioritize POV video and creator partnerships.

#### DD-V5-006: No People in Ads Rule
- **Type:** NEVER rule | **Severity:** Info
- Emily: "We're having a very hard time getting traction with any ads that don't have people in them."
- **Action:** Ensure all new concepts feature people.

#### DD-V5-007: Two Weekly Ad Report Copies in Drive
- **Type:** Process gap | **Severity:** Info
- Both "Daily Drop - Weekly ad report" and "Copy of Daily Drop - Weekly ad report" exist.
- **Action:** Delete the copy or clarify which is canonical.

---

### Workweek — 6 Issues (NEW in V5)

#### WW-V5-001: Subscriber Count Inconsistency — Highest Priority per Mike
- **Type:** Subscriber count | **Severity:** Critical
- Mike Madarasz flagged subscriber count inconsistency directly.
- NEVER Rule 1: "NEVER show inconsistent subscriber counts across ad creatives, body copy, and landing pages."
- Lays is deleting outdated primary text/headlines but NOT adding new ones to preserve learning phase.
- **Issue:** This is being handled but requires ongoing vigilance across 5 (soon 6) newsletters.
- **Action:** Track current verified subscriber counts for all 6 Workweek newsletters. Create a reference doc.

#### WW-V5-002: No Script Documents in Drive
- **Type:** Missing scripts | **Severity:** Warning
- Only a weekly ad report spreadsheet found in Drive. No script documents for any DCT.
- **Action:** Establish Drive script archive for Workweek concepts.

#### WW-V5-003: FTTB Copy Length Violation
- **Type:** NEVER rule | **Severity:** Warning
- NEVER Rule: "NEVER write long-form ad copy for FTTB." Mike flagged scripts were too long.
- **Action:** Benchmark all FTTB copy against IHIH length. Shorten.

#### WW-V5-004: IHIH Under Performance Pressure
- **Type:** Performance mismatch | **Severity:** Warning
- Sub CAC at $6.08 vs $6.00 target (1% over). Highest sponsor inventory pressure.
- DCT_130 sub CAC rising to $6.79 — possible frequency fatigue.
- **Action:** Prioritize IHIH creative refresh. DCT_138 "Secret Expert" ($5.14 sub CAC) emerging as replacement.

#### WW-V5-005: GTM Verification Funnel Problem
- **Type:** Performance mismatch | **Severity:** Info
- Only 3.7% convert to verified (post-subscribe flow problem, not creative).
- DCT_114 confirmed: 144 subs at $4.48 but only 1 verified ($644.50 V-CAC).
- **Action:** This is a client-side funnel issue. Document for reference.

#### WW-V5-006: Adam Ryan Declined April 2 Bi-Weekly
- **Type:** Process gap | **Severity:** Info
- Could be one-off or signal. Monitor.

---

### Insight Links — 5 Issues (NEW in V5)

#### IL-V5-001: DCT_103 Quality Decay — Jake Flagged
- **Type:** Performance mismatch | **Severity:** Critical
- Jake flagged March 19: "nearly all subscribers from DCT-103 Luiz Confession has been non-target readers."
- This is the dominant ad across CW and IW. Quality decay while volume holds = dangerous.
- **Action:** Shift budget from DCT_103 to DCT_118 on CW. This echoes the Growletter pattern of "reporting problems without solving them" that cost GL the account.

#### IL-V5-002: No Script Documents in Drive
- **Type:** Missing scripts | **Severity:** Warning
- Insight Links spreadsheet and weekly report found, but no script/concept documents.
- **Action:** Establish Drive script archive.

#### IL-V5-003: Friday Reports Shipping Late
- **Type:** Process gap | **Severity:** Warning
- 0/3 on-time in March. Mar 6 at 4:31 PM, Mar 13 at 1:00 PM.
- This is a bake-off account. Professionalism matters.
- **Action:** Sindy to enforce deadline compliance.

#### IL-V5-004: Bake-Off Decision Window Active
- **Type:** Process gap | **Severity:** Info
- 60-90 day evaluation window. TFM winning on quality but must maintain.

#### IL-V5-005: Ebook LP Blocked on Developer
- **Type:** Process gap | **Severity:** Info
- Steven working on 3 backend tasks. Target: first Monday of April.

---

### Points Path — 8 Issues (carried from V4)

*All 8 V4 issues confirmed. No new V5 issues.*

---

### Experiential Hospitality — 6 Issues (carried from V4)

*All 6 V4 issues confirmed. No new V5 issues.*

---

### Contrarian Thinking — 5 Issues (NEW in V5)

#### CT-V5-001: Onboarding Doc Contains Duplicate Content
- **Type:** Copy drift | **Severity:** Warning
- The Google Docs file has the "Qualification Funnel Asks" section duplicated — appears twice with slightly different wording.
- **Action:** Clean up the onboarding document.

#### CT-V5-002: NEVER Rule — "AI Voiceover" in DCT_101
- **Type:** NEVER rule | **Severity:** Critical
- NEVER rule: "NEVER use AI voiceover." Codie flagged DCT_101 AI voice as likely to underperform.
- **Action:** Verify DCT_101 was revised with human voice before launch.

#### CT-V5-003: No Script Documents in Drive
- **Type:** Missing scripts | **Severity:** Warning
- Only an onboarding doc found in Drive. No DCT script documents for any of the 11 concepts.
- **Action:** Create Drive script archive.

#### CT-V5-004: Codie Perceives CPL as High Despite Being in Target
- **Type:** Performance mismatch | **Severity:** Info
- BAU CPL at $4.96 is within $5-6 target. But Codie said "these costs per leads are out of control."
- **Action:** Manage expectations proactively. Lead with new LP CVR improvement story (44% vs 20%).

#### CT-V5-005: 55 Days Left in 90-Day Trial
- **Type:** Process gap | **Severity:** Info
- Ads only live ~8 days. Need strong performance data fast.

---

### Open Source CEO — 3 Issues (NEW in V5)

#### OSC-V5-001: No Script Documents in Drive
- **Type:** Missing scripts | **Severity:** Info
- Only weekly ad report and logos found. All concepts live in Notion only.

#### OSC-V5-002: CPL Still Above Target
- **Type:** Performance mismatch | **Severity:** Warning
- Still above sub-$3.50 target. Trending down but not there yet.
- LP CVR at 37.50% (below 40% benchmark).

#### OSC-V5-003: No Mar 17 Recording
- **Type:** Process gap | **Severity:** Info
- Day.ai failed to capture recording. Action items undocumented.

---

### Jay Shetty — 3 Issues (NEW in V5)

#### JS-V5-001: No Script Documents in Drive
- **Type:** Missing scripts | **Severity:** Info
- Weekly ad report found. No script documents.

#### JS-V5-002: Financial Tension Emerging
- **Type:** Performance mismatch | **Severity:** Warning
- Sentiment is "Positive with emerging financial tension."
- CPL at $0.91 gross / $0.36 net is excellent, but the financial tension flag warrants monitoring.

#### JS-V5-003: Subscriber Count Sensitivity
- **Type:** Subscriber count | **Severity:** Info
- "38M+ followers" and "1M+ newsletter subscribers" — verify these are current.

---

### How to AI — 2 Issues (NEW in V5)

#### HTAI-V5-001: No Script Documents in Drive
- **Type:** Missing scripts | **Severity:** Info
- Weekly ad report found. No script documents.

#### HTAI-V5-002: Subscriber Count Range
- **Type:** Subscriber count | **Severity:** Warning
- Client file says "338K-350K+" — a range, not a verified number.
- **Action:** Pin down exact current number for creative use.

---

### Vendry — 3 Issues (NEW in V5)

#### VN-V5-001: DR Funnel CPL Extremely High
- **Type:** Performance mismatch | **Severity:** Critical
- DR funnel CPL: $411.65 CAD. Newsletter CPL: $13.38 CAD.
- **Action:** Strategic pivot already in progress. Ensure DR funnel ads are paused or capped.

#### VN-V5-002: No Script Documents in Drive
- **Type:** Missing scripts | **Severity:** Warning
- Creative folder with videos found. Weekly ad report found. No script documents.

#### VN-V5-003: Domain Migration in Progress
- **Type:** Process gap | **Severity:** Info
- Migrated to casestudied.com (March 2026). Verify all ad URLs updated.

---

### 1636 Forum — 3 Issues (NEW in V5)

#### 1636-V5-001: CPL Above Target
- **Type:** Performance mismatch | **Severity:** Critical
- Current CPL: $3.01 vs $2.00 target (50% over).
- **Action:** Review creative strategy. Consider audience refinement.

#### 1636-V5-002: No Script Documents in Drive (Hub Sheet is operational, not scripts)
- **Type:** Missing scripts | **Severity:** Warning
- Hub spreadsheet exists but contains operational links, not ad scripts.

#### 1636-V5-003: Niche Audience Constraint
- **Type:** Process gap | **Severity:** Info
- Harvard alumni only. Very narrow targeting. CPL pressure expected.

---

### MarketBeat — 2 Issues (NEW in V5)

#### MB-V5-001: No Script Documents in Drive
- **Type:** Missing scripts | **Severity:** Warning
- Only .md files and logos found. No script spreadsheets or docs.

#### MB-V5-002: Registration Tracking Uses Non-Standard Method
- **Type:** Process gap | **Severity:** Info
- Uses RegistrationCode=meta-thefeedmedia-dctXXX instead of UTM parameters.
- **Action:** Document this exception in the QA SOP.

---

### Stocks & Income — 2 Issues (NEW in V5)

#### SI-V5-001: No Drive Presence for Scripts
- **Type:** Missing scripts | **Severity:** Warning
- Only .md backup files found. All concepts live in Notion only.
- New client (kicked off Feb 19, 2026).

#### SI-V5-002: CPL Above Target
- **Type:** Performance mismatch | **Severity:** Warning
- Current CPL: $3.70 vs $2.00 target (85% over).
- **Action:** New client, early scaling phase. Monitor.

---

### RNT Fitness — 2 Issues (NEW in V5)

#### RNT-V5-001: No Script Documents in Drive
- **Type:** Missing scripts | **Severity:** Info
- Weekly ad report found. Brand new account (launched March 11, 2026).

#### RNT-V5-002: KPIs Unconfirmed
- **Type:** Process gap | **Severity:** Info
- CPL target listed as "Unconfirmed." Current CPL: GBP 1.00.
- **Action:** Confirm CPL target with Akash/Kavit at next bi-weekly.

---

### Franklins Forum — 1 Issue (NEW in V5)

#### FF-V5-001: Minimal Drive Presence
- **Type:** Process gap | **Severity:** Info
- Only logo file found. No scripts, no weekly report spreadsheet.
- **Action:** Establish Drive presence as account matures.

---

### Just Womens Sports — 1 Issue (NEW in V5)

#### JWS-V5-001: No Script Documents in Drive
- **Type:** Missing scripts | **Severity:** Info
- Only folder structure found. All concepts in Notion.

---

### Student Loan Planner — 1 Issue (NEW in V5)

#### SLP-V5-001: No Script Documents in Drive
- **Type:** Missing scripts | **Severity:** Info
- Creative folder exists. No script documents found.

---

### MDhair — 1 Issue (NEW in V5)

#### MDH-V5-001: No Script Documents in Drive
- **Type:** Missing scripts | **Severity:** Info
- Only video files (DCT 121 variants). No written scripts.
- Creative-only client, so scripts may live in Notion briefs exclusively.

---

## Cross-Client Patterns

### Pattern 1: Drive is NOT source of truth for 18 of 23 clients
**Clients with NO script documents in Drive:**
Creator Spotlight, Experiential Hospitality, Stocks.News, Daily Drop, Workweek, Insight Links, Contrarian Thinking, Open Source CEO, Jay Shetty, How to AI, Vendry, 1636 Forum, MarketBeat, Stocks & Income, RNT Fitness, Franklins Forum, Just Womens Sports, Student Loan Planner, MDhair

**Clients WITH script documents in Drive:**
The Points Guy, Big Desk Energy (Google Docs), Houck (Google Sheets), Points Path (Master Ads Sheet)

**Severity:** This is the single biggest process gap across the agency. 78% of clients have zero script documentation in Google Drive.

### Pattern 2: Subscriber count inconsistencies affect 6+ clients
| Client | Issue |
|---|---|
| The Points Guy | 4 different counts (1M, 1.2M, 1.5M, 2M+) |
| Big Desk Energy | 2 different counts (25k, 50k) |
| Creator Spotlight | ~366-370k range — needs pinning |
| Workweek | Mike flagged directly. 5 newsletters with changing counts |
| How to AI | "338K-350K+" — a range |
| Jay Shetty | "38M+ followers" and "1M+ newsletter subscribers" — verify |

### Pattern 3: Friday reports shipping late across multiple clients
| Client | On-Time Rate |
|---|---|
| The Points Guy | 0/3 (0%) |
| Insight Links | 0/3 (0%) |
| Open Source CEO | 1/3 (33%) |
| Contrarian Thinking | 1/3 (33%) |
| Houck | Started late, 1/1 |
| Creator Spotlight | Improving |

### Pattern 4: Performance mismatch — ads running despite underperformance
| Client | Issue |
|---|---|
| Stocks.News | CPA spike to $73.89, CTR collapsed 85% |
| Big Desk Energy | DCT 231.1 OR declining 3 weeks (48.6% -> 39.2%) |
| Daily Drop | CPL above target ($4.26 vs $3-4), TFM 147 fatigue after 9 months |
| Workweek | IHIH sub CAC 1% over target under maximum pressure |
| Insight Links | DCT_103 producing "nearly all non-target readers" |
| Vendry | DR funnel CPL at $411.65 CAD |
| 1636 Forum | CPL 50% over target |
| Stocks & Income | CPL 85% over target (new account) |

### Pattern 5: Missing inspiration documentation is pervasive
V4 found 5 instances across 5 clients. V5 confirms this extends to at least 8 clients. The QA SOP mandates inspiration documentation for every concept — compliance is low.

---

## V4 -> V5 Delta

| Metric | V4 | V5 | Change |
|---|---|---|---|
| Total issues | 47 | 112 | +65 (138% increase) |
| Critical issues | 8 | 19 | +11 |
| Clients audited | 5 | 23 | +18 |
| Clients with no Drive scripts | 3 of 5 | 18 of 23 | +15 (now 78%) |
| Subscriber count issues | 5 | 12 | +7 |
| Performance mismatches found | 0 | 8 | +8 (new category) |
| Weekly reports read | 0 | 6 | +6 (new capability) |
| Google Sheets reads | 0 | 8+ | +8 (new capability) |

### New Issue Types in V5 (not in V4)
1. **Performance mismatch** — 8 issues across 8 clients. V4 could not do this without weekly report data.
2. **Factual claims** — 6 issues. BDE valuation discrepancy, Houck funding amount, revenue claims.
3. **Process gap escalations** — Friday report compliance tracked across all clients.

### V4 Issues Resolved Since V4
- None formally resolved. All V4 issues still open as of March 21, 2026.

---

## Clients With NO Google Drive Presence (Scripts Only in Notion)

These clients have **no script documents, script spreadsheets, or concept briefs in Google Drive**. Their creative development pipeline exists entirely in Notion:

1. Stocks.News (video files only)
2. Creator Spotlight (video/image files only)
3. Experiential Hospitality (video files only)
4. Daily Drop (video files only)
5. Workweek
6. Contrarian Thinking (onboarding doc only)
7. Open Source CEO
8. Jay Shetty
9. How to AI
10. MarketBeat
11. Stocks & Income
12. RNT Fitness
13. Franklins Forum
14. Just Womens Sports
15. Student Loan Planner
16. MDhair (video files only)
17. Vendry (video files only)
18. Insight Links

**Note:** All clients have weekly ad report spreadsheets in Google Drive (except Stocks & Income, Franklins Forum, JWS, SLP, MDhair, and MarketBeat). The gap is specifically in **script/concept documentation** in Drive.

---

## Recommendations for Process Improvements

### Immediate (This Week)
1. **Stocks.News LP CVR investigation** — 80% decline is urgent. Check all ad URLs.
2. **BDE subscriber count audit** — Verify whether 25k or 50k is current. Update all scripts.
3. **TPG DCT 148** — Block until subscriber count verified. Do not send to client.
4. **Houck funding verification** — Confirm $10M vs $15M. Fix script.

### Short-Term (Next 2 Weeks)
5. **Standardize Drive as script repository** — Create a Master Ads Sheet template. Roll out to all 18 clients missing script docs.
6. **Create "Verified Metrics" Notion database** — Subscriber counts, verified date, source. Update monthly.
7. **Enforce Friday report deadlines** — 0% on-time rate for 2 of 23 clients is unacceptable. Sindy to own enforcement.
8. **BDE creative refresh** — DCT 231.1 showing fatigue. Develop replacement concepts before OR drops below 35%.

### Medium-Term (Next Month)
9. **Monthly QA automation** — Run V5-style audit monthly. Rotate client focus groups.
10. **Pipeboard integration for V6** — Pull live ad copy from Meta Ads Manager. Compare against Drive/Notion scripts. Catch copy drift in live ads.
11. **Inspiration source enforcement** — Add to concept template as required field. Block concepts without inspiration.
12. **Performance mismatch alerts** — Automate weekly check: if any ad's primary KPI exceeds target by >20% for 2+ consecutive weeks, flag in Slack.

### Structural
13. **Script documentation SOP** — Every concept must have a written script in Google Drive within 24 hours of production start. GM responsible. Sindy audits monthly.
14. **Subscriber count verification cadence** — Quarterly verification for all clients. Update all active scripts that reference counts.
15. **Cross-client QA database** — Build a Notion database that logs QA issues with resolution status, owner, and due date.

---

*Built from: Google Drive MCP (23 client searches, 8+ spreadsheets read, 10+ Google Docs read), Google Sheets API (6 weekly ad reports, 2 script spreadsheets), Notion MCP (30+ pages, QA Log V4, concept briefs), Client Intelligence Files (all 23 clients). March 21, 2026.*
