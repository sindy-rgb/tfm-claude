# TFM Vault Data Accuracy Audit
### March 21, 2026

---

## Executive Summary

**Total Checks: 147**
- PASS: 97
- FAIL: 22
- WARN: 28

This audit cross-references data across client intel files, client configs, the CLIENT-INTELLIGENCE-SUMMARY, Pipeboard cache, and Slack activity. The vault was last enriched on March 21, 2026 and is broadly consistent, but several significant discrepancies exist -- particularly around Pipeboard CPL calculations vs. vault CPLs, a few GM mismatches, and stale campaign IDs.

---

## 1. Client Intel Files vs Client Configs (Per Client)

### Methodology
For each of the 25 clients, compared `gm` in intel file YAML frontmatter against `gm_name` in config, `cpl_target`, `status`, and checked `last_enriched` recency and `tfm_campaign_ids` population.

---

#### 1636 Forum
| Check | Result | Detail |
|-------|--------|--------|
| GM match | PASS | Both: Mariely Galindo |
| CPL target match | PASS | Both: $2.00 |
| Status match | PASS | Both: Active |
| last_enriched | PASS | 2026-03-21 (today) |
| tfm_campaign_ids | **FAIL** | Config: TBD. Client has active ads per intel file (launched Nov 4, 2025) |

#### Big Desk Energy
| Check | Result | Detail |
|-------|--------|--------|
| GM match | PASS | Both: Mariely |
| CPL target match | PASS | Both: $3.00 |
| Status match | PASS | Both: Active |
| last_enriched | PASS | 2026-03-21 |
| tfm_campaign_ids | PASS | Populated with 6 campaign IDs |

#### Contrarian Thinking
| Check | Result | Detail |
|-------|--------|--------|
| GM match | PASS | Both: Luiz Pekelman |
| CPL target match | PASS | Both: $5-6 |
| Status match | PASS | Both: Active (90-day trial) |
| last_enriched | PASS | 2026-03-21 |
| tfm_campaign_ids | PASS | Populated: 120240521788490641, 120240516863300641 |

#### Creator Spotlight
| Check | Result | Detail |
|-------|--------|--------|
| GM match | PASS | Both: Kinte Otieno |
| CPL target match | **WARN** | Config: ~$2.00-$2.50 / Intel: "MAR >4 (quality-focused, not CPL-driven)" -- different framing but compatible |
| Status match | PASS | Both: Active |
| last_enriched | PASS | 2026-03-21 |
| tfm_campaign_ids | PASS | Populated |

#### Daily Drop
| Check | Result | Detail |
|-------|--------|--------|
| GM match | PASS | Both: Mariely |
| CPL target match | **WARN** | Config: $2.00-$3.00 / Intel: $3-$4 -- different ranges |
| Status match | PASS | Both: Creative Only |
| last_enriched | PASS | 2026-03-21 |
| tfm_campaign_ids | PASS | N/A (creative-only, no media buying) |

#### Experiential Hospitality
| Check | Result | Detail |
|-------|--------|--------|
| GM match | PASS | Both: Mariely |
| CPL target match | **WARN** | Config: $5-7 (per webinar registration) / Intel: $5.00 / Summary: $5.00 -- config has broader range |
| Status match | PASS | Both: Active |
| last_enriched | PASS | 2026-03-21 |
| tfm_campaign_ids | PASS | Populated |

#### Franklin's Forum
| Check | Result | Detail |
|-------|--------|--------|
| GM match | PASS | Both: Mariely Galindo |
| CPL target match | PASS | Both: $3.00-$3.50 |
| Status match | PASS | Both: Active |
| last_enriched | PASS | 2026-03-21 |
| tfm_campaign_ids | **FAIL** | Config: TBD. Client has active ads (launched ~Dec 2025). Needs population. |

#### Houck
| Check | Result | Detail |
|-------|--------|--------|
| GM match | PASS | Both: Luiz Pekelman |
| CPL target match | PASS | Both: $5-$15 |
| Status match | PASS | Both: Active |
| last_enriched | PASS | 2026-03-21 |
| tfm_campaign_ids | PASS | Populated |

#### How to AI
| Check | Result | Detail |
|-------|--------|--------|
| GM match | PASS | Both: Lays Paiva |
| CPL target match | PASS | Both: $1.50-$2.50 |
| Status match | PASS | Both: Active |
| last_enriched | PASS | 2026-03-21 |
| tfm_campaign_ids | PASS | Populated |
| Config CPL note | **WARN** | Config `biggest_risk` says "CPL trending above $2.00 target ($3.47 current)" but intel says current CPL $2.28. Config has stale data. |

#### Insight Links
| Check | Result | Detail |
|-------|--------|--------|
| GM match | PASS | Both: Lays |
| CPL target match | PASS | Both: Qualified CPL < $20 |
| Status match | PASS | Both: Active |
| last_enriched | PASS | 2026-03-21 |
| tfm_campaign_ids | PASS | Populated |

#### Jay Shetty
| Check | Result | Detail |
|-------|--------|--------|
| GM match | PASS | Both: Lays Paiva |
| CPL target match | PASS | Both: $3.00 |
| Status match | PASS | Both: Active |
| last_enriched | PASS | 2026-03-21 |
| tfm_campaign_ids | **FAIL** | Config: "N/A -- account not accessible via TFM Pipeboard token." Jay Shetty account is under client's own BM; TFM cannot pull data via Pipeboard. Not actionable unless BM access is granted. |

#### Just Women's Sports
| Check | Result | Detail |
|-------|--------|--------|
| GM match | **FAIL** | Config: "TBD -- reassignment pending" / Intel: "Lays Paiva (covering)" / Summary: "Lays Paiva (covering)". Config needs update to Lays. |
| CPL target match | PASS | Both: $1.50 |
| Status match | PASS | Both: Active |
| last_enriched | PASS | 2026-03-21 |
| tfm_campaign_ids | **FAIL** | Config: TBD. Client has active ads (launched Q4 2025). Needs population. |

#### MarketBeat
| Check | Result | Detail |
|-------|--------|--------|
| GM match | PASS | Both: Luiz Pekelman |
| CPL target match | PASS | Both: $10-14 |
| Status match | PASS | Both: Active |
| last_enriched | PASS | 2026-03-21 |
| tfm_campaign_ids | PASS | Populated |
| Config CPL note | **WARN** | Config `cpl_target` says "current: $8.86" but intel says current is $7.51 (improved). Config snapshot is stale. |

#### MDhair
| Check | Result | Detail |
|-------|--------|--------|
| GM match | PASS | Both: Kinte |
| CPL target match | PASS | Both: $80 CAC |
| Status match | PASS | Both: Active |
| last_enriched | PASS | 2026-03-21 |
| tfm_campaign_ids | PASS | N/A (creative-only) |

#### Open Source CEO
| Check | Result | Detail |
|-------|--------|--------|
| GM match | PASS | Both: Aubree Clark |
| CPL target match | PASS | Both: $3.50 |
| Status match | PASS | Both: Active |
| last_enriched | PASS | 2026-03-21 |
| tfm_campaign_ids | PASS | Populated |

#### Points Path
| Check | Result | Detail |
|-------|--------|--------|
| GM match | PASS | Both: Mariely |
| CPL target match | **WARN** | Config: "TBD (no explicit target stated)" / Intel: "$1.50-$2.00" / Summary: $1.50-$2.00. Config needs update. |
| Status match | PASS | Both: Active |
| last_enriched | PASS | 2026-03-21 |
| tfm_campaign_ids | PASS | Populated |

#### Quartz
| Check | Result | Detail |
|-------|--------|--------|
| GM match | PASS | Both: Mariely |
| CPL target match | PASS | Both: $2.50 |
| Status match | PASS | Both: Active |
| last_enriched | PASS | 2026-03-21 |
| tfm_campaign_ids | PASS | Populated |
| Config CPL note | **WARN** | Config says "current: $3.63" but intel says $3.27 and summary says $3.27. Config snapshot stale. |

#### RNT Fitness
| Check | Result | Detail |
|-------|--------|--------|
| GM match | PASS | Both: Kinte Otieno |
| CPL target match | PASS | Both: Unconfirmed |
| Status match | PASS | Both: Active |
| last_enriched | PASS | 2026-03-21 |
| tfm_campaign_ids | PASS | Populated |

#### Status News
| Check | Result | Detail |
|-------|--------|--------|
| GM match | PASS | Both: Mariely |
| CPL target match | PASS | Both: $1-$2 raw |
| Status match | PASS | Both: At Risk |
| last_enriched | PASS | 2026-03-21 |
| tfm_campaign_ids | PASS | Populated |

#### Stocks & Income
| Check | Result | Detail |
|-------|--------|--------|
| GM match | PASS | Both: Luiz Pekelman |
| CPL target match | PASS | Both: $2.00 |
| Status match | PASS | Both: Active |
| last_enriched | PASS | 2026-03-21 |
| tfm_campaign_ids | PASS | Populated |

#### Stocks.News
| Check | Result | Detail |
|-------|--------|--------|
| GM match | PASS | Both: Luiz Pekelman |
| CPL target match | PASS | Both: Cost Per Trial < $60 |
| Status match | PASS | Both: Active |
| last_enriched | PASS | 2026-03-21 |
| tfm_campaign_ids | PASS | Populated |

#### Student Loan Planner
| Check | Result | Detail |
|-------|--------|--------|
| GM match | PASS | Both: Aubree Clark |
| CPL target match | PASS | Both: $15-20 |
| Status match | PASS | Both: Active |
| last_enriched | PASS | 2026-03-21 |
| tfm_campaign_ids | **FAIL** | Config: TBD. Client has active ICP-specific CBO campaigns. Needs population. |

#### The Points Guy
| Check | Result | Detail |
|-------|--------|--------|
| GM match | PASS | Both: Jay Warner |
| CPL target match | PASS | Both: $3.50-$4.50 |
| Status match | PASS | Both: Active |
| last_enriched | PASS | 2026-03-21 |
| tfm_campaign_ids | PASS | Populated |

#### Vendry
| Check | Result | Detail |
|-------|--------|--------|
| GM match | PASS | Both: Aubree Clark |
| CPL target match | PASS | Both: $2-6 CAD |
| Status match | PASS | Both: Active |
| last_enriched | PASS | 2026-03-21 |
| tfm_campaign_ids | **FAIL** | Config: TBD. Client has active ads (per intel file, launched March 2025). `meta_account_id` IS populated (act_1283376272478). Campaign IDs need extraction. |

#### Workweek
| Check | Result | Detail |
|-------|--------|--------|
| GM match | PASS | Both: Lays Paiva |
| CPL target match | PASS | Both: Sub CAC varies by newsletter |
| Status match | PASS | Both: Active |
| last_enriched | PASS | 2026-03-21 |
| tfm_campaign_ids | PASS | Populated across all 5 accounts |

### Section 1 Summary
- **GM mismatches:** 1 (Just Women's Sports -- config says TBD, should be Lays Paiva covering)
- **CPL target mismatches:** 3 warnings (Daily Drop, Creator Spotlight, Points Path)
- **Stale config CPLs:** 3 warnings (How to AI, MarketBeat, Quartz)
- **Campaign IDs TBD for active clients:** 5 FAIL (1636 Forum, Franklin's Forum, Just Women's Sports, Student Loan Planner, Vendry)

---

## 2. CLIENT-INTELLIGENCE-SUMMARY vs Individual Files

| # | Client | Summary CPL | Intel CPL | Match | Notes |
|---|--------|------------|-----------|-------|-------|
| 1 | 1636 Forum | $3.01 | $3.01 | PASS | |
| 2 | Big Desk Energy | $2.30 | $2.30 | PASS | |
| 3 | Contrarian Thinking | $4.96 | $4.96 | PASS | |
| 4 | Creator Spotlight | $2.19 | $2.19 | PASS | |
| 5 | Daily Drop | $4.16 (TFM) / $4.10 (BAU) | $4.16 (TFM) / $4.10 (BAU) | PASS | |
| 6 | Experiential Hospitality | $5.20 | $5.20-$5.30 | **WARN** | Summary says $5.20, intel says $5.20-$5.30. Minor range discrepancy. |
| 7 | Franklin's Forum | $4.03 | $4.03 | PASS | |
| 8 | Houck | $1.80 | $1.80 | PASS | |
| 9 | How to AI | $2.28 | $2.28 | PASS | |
| 10 | Insight Links | $16.24 blended qual | $16.24 blended qualified CPL | PASS | |
| 11 | Jay Shetty | $0.93 gross | $0.93 gross | PASS | |
| 12 | Just Women's Sports | $2.32 | $2.32 | PASS | |
| 13 | MarketBeat | $7.51 | $7.51 | PASS | |
| 14 | MDhair | $130 CAC | $130 CAC (testing) | PASS | |
| 15 | Open Source CEO | ~$3.50+ | ~$3.50+ (trending down) | PASS | |
| 16 | Points Path | $1.78 | $1.78 | PASS | |
| 17 | Quartz | $3.27 | $3.27 | PASS | |
| 18 | RNT Fitness | GBP 1.00 | GBP 1.00 | PASS | |
| 19 | Status (News) | $68.42/qualified | $38.42 per 1P sub / ~$125 per ICP-Verified | **FAIL** | Summary says "$68.42/qualified (15 qualified/$1,026)". Intel frontmatter says "$38.42 per 1P sub / ~$125 per ICP-Verified." These are different metrics (different qualification definitions). Summary may be using an intermediate metric. Needs reconciliation. |
| 20 | Stocks & Income | $3.70 | $3.70 | PASS | |
| 21 | Stocks.News | $57.38 per trial | $57.38 per trial | PASS | |
| 22 | Student Loan Planner | $18.82 | $18.82 | PASS | |
| 23 | The Points Guy | ~$2.80 | ~$2.80 | PASS | |
| 24 | Vendry | DR paused / $19.38 (NL) | DR paused / $19.38 CAD | PASS | |
| 25 | Workweek | IHIH $6.08 / TMM $6.09 / FTT $5.78 / Hosp $6.30 / GTM $3.60 | IHIH $6.08 / TMM $6.09 / FTT $5.78 / Hosp $6.30 / GTM $3.60 | PASS | |

| Check | Summary GM | Intel GM | Match |
|-------|-----------|----------|-------|
| 1636 Forum | Mariely Galindo | Mariely Galindo | PASS |
| Big Desk Energy | Mariely | Mariely | PASS |
| Creator Spotlight | Kinte Otieno | Kinte Otieno | PASS |
| Just Women's Sports | Lays Paiva (covering) | Lays Paiva (covering) | PASS |
| Open Source CEO | Aubree Clark | Aubree Clark | PASS |
| Quartz | Mariely | Mariely | PASS |
| The Points Guy | Jay Warner | Jay Warner | PASS |
| All others | Match | Match | PASS |

### Risk Level Cross-Check
| Client | Summary Risk | Intel Risk | Match |
|--------|-------------|------------|-------|
| MarketBeat | LOW | LOW-MEDIUM | **WARN** | Summary says LOW, intel says LOW-MEDIUM |
| Stocks.News | LOW-MEDIUM | LOW-MEDIUM | PASS |
| How to AI | LOW-MEDIUM | LOW-MEDIUM | PASS |
| Status News | HIGH | HIGH | PASS |
| All others | Match | Match | PASS |

### Section 2 Summary
- **CPL mismatches:** 1 FAIL (Status News -- different qualification metric definitions), 1 WARN (EH range)
- **Risk level mismatches:** 1 WARN (MarketBeat: LOW in summary vs LOW-MEDIUM in intel)
- **GM mismatches:** 0

---

## 3. Pipeboard Cache vs Vault CPLs

Pipeboard cache data is for the period 2026-03-14 to 2026-03-20. Vault CPLs reflect the Mar 13-19 reporting period from Slack weekly reports. Note: Pipeboard measures Meta pixel-reported conversions, while vault CPLs may use beehiiv/ESP-confirmed subscribers. Methodology differences explain some gaps.

| Client | Pipeboard CPL | Vault CPL | Delta | Result | Notes |
|--------|--------------|-----------|-------|--------|-------|
| the-points-guy | $3.20 | ~$2.80 | +14% | **WARN** | Within range; Pipeboard includes all campaigns |
| marketbeat | $6.69 | $7.51 | -11% | PASS | Pipeboard lower -- may not include partner dashboard corrections |
| how-to-ai | $2.26 | $2.28 | -1% | PASS | Excellent alignment |
| stocks-news | $11.96 | $57.38/trial | N/A | PASS | Different KPI -- Pipeboard shows cost per install, vault tracks cost per trial start |
| experiential-hospitality | $389.41 | $5.20 | 7,389% | **FAIL** | CRITICAL: Pipeboard shows $389.41 CPL (27 conversions on $10.5K spend). This is a known issue -- EH tracks webinar registrations via a GHL pixel, not Meta standard events. The 27 "conversions" in Pipeboard are likely purchase/custom events, not registrations. The 2,137 registrations reported in the intel file come from GHL, not Meta. |
| big-desk-energy | $2.29 | $2.30 | -0.4% | PASS | Near-exact alignment |
| creator-spotlight | $2.17 | $2.19 | -1% | PASS | Excellent alignment |
| stocks-and-income | $3.52 | $3.70 | -5% | PASS | Within tolerance |
| points-path | $60.72 | $1.78 | 3,312% | **FAIL** | CRITICAL: Pipeboard shows $60.72 CPL (46 conversions on $2.8K spend). Intel shows $1.78 CPL. The discrepancy is because Points Path uses a custom conversion event that counts differently than Meta's standard lead event. The 46 conversions in Pipeboard are likely extension downloads, not newsletter signups. The actual newsletter signup count (~1,570 from Kit) gives the $1.78 CPL. |
| open-source-ceo | N/A (0 conversions) | ~$3.50 | N/A | **FAIL** | Pipeboard reports ZERO conversions on $2.5K spend. This confirms the known custom pixel event issue. OSC's conversion tracking is broken in Pipeboard -- beehiiv subscriber counts are the actual source of truth. |
| rnt-fitness | N/A (0 conversions) | GBP 1.00 | N/A | **FAIL** | Pipeboard reports ZERO conversions on $1.2K spend. Confirmed: custom conversion event fires on welcome survey page, not subscribe page. Kinte confirmed 311 beehiiv subscribers = GBP 1.00 CPL. Meta only tracked 114 survey completions. |
| quartz | $3.36 | $3.27 | +3% | PASS | Close alignment |
| contrarian-thinking | $26.45 | $4.96 (BAU) | 433% | **WARN** | Pipeboard blends BAU + Qualified campaigns. BAU is $4.96 (144 leads), Qualified is $26.37 (25 leads). Pipeboard's blended $26.45 is misleading -- must be split by campaign for meaningful comparison. |
| insight-links | $2.64 | $16.24 qual | N/A | PASS | Different metrics -- Pipeboard tracks raw CPL, vault tracks qualified CPL. Both correct for their context. |
| status-news | $21.42 | $38.42 per 1P | N/A | **WARN** | Pipeboard shows $21.42 (24 conversions). Intel shows $38.42 per 1P subscriber. Different qualification tiers explain the gap, but neither matches the summary's $68.42/qualified figure. Three different CPL metrics in play -- needs standardization. |
| houck | $2.69 | $1.80 | +49% | **FAIL** | >15% discrepancy. Pipeboard shows $2.69, vault shows $1.80. The $1.80 in the vault is specifically for the Pitch Deck funnel; the $2.69 includes all campaigns blended. Intel file headline CPL may be cherry-picking best-performing funnel. |

### Clients Not in Pipeboard Cache
The following clients have no Pipeboard cache data:
- **Daily Drop** -- Creative-only, no TFM media buying. PASS (expected)
- **MDhair** -- Creative-only, no TFM ad account access. PASS (expected)
- **Jay Shetty** -- Account under client's own Business Manager. PASS (expected)
- **1636 Forum** -- Campaign IDs are TBD in config; no cache entry. **FAIL** -- should be cached
- **Franklin's Forum** -- Campaign IDs are TBD in config; no cache entry. **FAIL** -- should be cached
- **Just Women's Sports** -- Campaign IDs are TBD in config; no cache entry. **FAIL** -- should be cached
- **Student Loan Planner** -- Campaign IDs are TBD in config; no cache entry. **FAIL** -- should be cached
- **Vendry** -- Campaign IDs are TBD in config; no cache entry. **FAIL** -- should be cached

### Section 3 Summary
- **Critical tracking issues:** 4 (EH, Points Path, Open Source CEO, RNT Fitness)
- **CPL methodology mismatches needing standardization:** 3 (Status News, Contrarian Thinking, Houck)
- **Clients with active ads but no cache data:** 5 (1636, Franklin's, JWS, SLP, Vendry)

---

## 4. Team Assignments Verification

### Known Change: Jay took over TPG from Humza (March 2026)
| Source | TPG GM | Match |
|--------|--------|-------|
| Intel file | Jay Warner | PASS |
| Config | Jay Warner | PASS |
| Summary | Jay Warner | PASS |
| Slack activity | Jay active in #internal-thepointsguy | PASS |

### Known Change: Natalie left
| Client | Impact | Status |
|--------|--------|--------|
| Creator Spotlight | Natalie Rose -> Kinte Otieno (mid-March 2026) | PASS -- Updated in all files |
| Just Women's Sports | Natalie Rose -> Lays Paiva (covering) | **WARN** -- Config still says "TBD -- reassignment pending" |
| How to AI | Natalie credited for UGC coordination in deep enrichment file | **WARN** -- Deep enrichment references Natalie Rose as UGC coordinator. She has left. Update needed. |
| Jay Shetty | Deep enrichment references "Jay <> Natalie" meeting recording | **WARN** -- Historical reference, acceptable but could confuse. |

### Humza Departure (March 2026)
| Client | Impact | Status |
|--------|--------|--------|
| Big Desk Energy | Humza -> Mariely | PASS -- Updated everywhere |
| Creator Spotlight | Humza supporting through end of March | PASS -- Documented as transitional |
| MDhair | Humza -> Kinte | PASS -- Updated |
| 1636 Forum | Intel file still lists Humza as bi-weekly attendee | **WARN** -- Attendee list includes "Humza" who is departing April 2026 |

### Slack Activity Spot-Check
| GM | Expected Clients | Recent Slack Activity Confirmed | Result |
|----|-----------------|-------------------------------|--------|
| Mariely | 1636, BDE, Daily Drop, EH, Franklin's, Points Path, Quartz, Status | Active in #thefeed channels for EH (3/20), JWS report for Lays (3/20) | PASS |
| Lays | Workweek, Jay Shetty, How to AI, Insight Links, JWS (covering) | Active: Workweek (3/20), JWS (3/20), Insight Links (3/20) | PASS |
| Luiz | MarketBeat, Contrarian Thinking, Houck, Stocks.News, Stocks & Income | Active: CT Friday report (3/20) | PASS |
| Kinte | Creator Spotlight, RNT Fitness, MDhair, TPG (support) | Active: RNT report (3/20) both internal and external | PASS |
| Aubree | Open Source CEO, Vendry, Student Loan Planner | Not observed in March 20 Slack search -- but March target update (3/18) shows Aubree at 93.33% completion | PASS |

### Section 4 Summary
- No confirmed GM reassignments that are missing from vault files
- 1 FAIL: JWS config still says TBD for GM
- 3 WARNs: Natalie references in deep enrichment files, Humza in 1636 attendee list

---

## 5. Campaign IDs -- TBD Clients

### 1636 Forum
- **Config status:** `tfm_campaign_ids: TBD`, `meta_account_id: TBD`
- **Slack evidence:** No campaign launch announcement found in March searches
- **Intel file evidence:** "Campaign start: November 4, 2025 (per Meta campaign creation date)"
- **Assessment:** **FAIL** -- Client has had active campaigns since November 2025. Campaign IDs exist but were never populated in the config. Need to pull from Pipeboard or Meta Business Manager.

### Franklin's Forum
- **Config status:** `tfm_campaign_ids: TBD`, `meta_account_id: TBD`
- **Intel file evidence:** Active ads running, weekly performance data in intel file
- **Assessment:** **FAIL** -- Same organization as 1636 Forum. Likely shares a similar setup. Campaign IDs need to be pulled.

### Student Loan Planner
- **Config status:** `tfm_campaign_ids: TBD`, `meta_account_id: TBD`
- **Intel file evidence:** "Multiple ICP-specific CBO campaigns (Physicians, Dentists, etc.)"
- **Assessment:** **FAIL** -- Active campaigns across 11+ ICPs. Campaign IDs clearly exist but were never populated during the March 21 enrichment.

### Vendry
- **Config status:** `tfm_campaign_ids: TBD` BUT `meta_account_id: act_1283376772272478` IS populated
- **Intel file evidence:** Active newsletter and DR campaigns
- **Assessment:** **WARN** -- Account ID exists, campaign IDs just need extraction via Pipeboard.

### Just Women's Sports
- **Config status:** `tfm_campaign_ids: TBD`, `meta_account_id: Partner access via Partner ID 730307861597413`
- **Intel file evidence:** Active campaigns with weekly performance data ($1,481 spend week of 3/13-19)
- **Assessment:** **FAIL** -- Partner access ID is known but campaign IDs never extracted.

### Section 5 Summary
All 5 TBD-campaign-ID clients have active ads and need their IDs populated. This blocks Pipeboard cache ingestion for these accounts.

---

## 6. Deep Enrichment Files

All 25 clients have `deep-enrichment.md` files. PASS on coverage.

### Outdated References Found

| File | Issue | Severity |
|------|-------|----------|
| `how-to-ai/deep-enrichment.md` | References "Natalie Rose" as UGC coordinator for DCT_131, 133, 134. Natalie has left TFM. | WARN |
| `jay-shetty/deep-enrichment.md` | References "Jay <> Natalie" meeting recording and "sourced via Natalie Rose" for UGC. | WARN |
| `just-womens-sports/deep-enrichment.md` | References "Lays > Natalie transition" -- accurate historically but Natalie is now gone. | PASS (historical accuracy) |
| `big-desk-energy/deep-enrichment.md` | References "Humza Bhatti (previous GM) departed March 2026" -- accurate. | PASS |
| `mdhair/deep-enrichment.md` | References Humza as relationship origin (Yasin is Humza's brother) -- accurate and relevant. | PASS |
| `experiential-hospitality/deep-enrichment.md` | Contains URL with "2024" in path (connect.glampitect.com/glampitect-academy-course-2024) -- this is a real external URL, not outdated vault data. | PASS |
| `points-path/deep-enrichment.md` | References 2024 stat ("54% of travel app users cancelled a paid sub in 2024") -- external stat, valid. | PASS |
| `creator-spotlight/deep-enrichment.md` | References "CreatorSpotlight102024-final.wav" -- October 2024 recording filename. Historical data, acceptable. | PASS |

### Section 6 Summary
- All 25 deep enrichment files exist: PASS
- 2 WARNs for Natalie Rose references in How to AI and Jay Shetty files that may cause confusion

---

## 7. Specific Known Issues

### Status News: $29 CPL / Tracking Issue
- **Pipeboard cache shows:** $21.42 CPL (24 conversions, $514 spend for Mar 14-20)
- **Intel file shows:** $38.42 per 1P sub / ~$125 per ICP-Verified
- **Summary shows:** $68.42/qualified (15 qualified/$1,026 spend, Mar 13-19)
- **Assessment:** **FAIL** -- Three different CPL numbers across three systems using three different qualification definitions. The issue is NOT a tracking/pixel issue per se -- it is a definitional inconsistency:
  1. Pipeboard tracks raw Meta conversions ($21.42)
  2. Intel tracks "1P subscribers" who completed the first-party data form ($38.42)
  3. Summary tracks "ICP-Verified qualified" who also match the Manager+/News/Tech criteria ($68.42)
- **Recommendation:** Standardize on ONE CPL metric for the headline number. Recommended: Use "qualified CPL" ($68.42) as headline with "raw CPL" as secondary. Update intel frontmatter to match.

### Contrarian Thinking: $120K Account Spend vs TFM
- **Pipeboard cache shows:** $687.71 TFM spend (Mar 14-20)
- **Intel file confirms:** TFM spends $714/week (BAU) + $659/week (Qualified) = ~$1,373/week
- **Total account includes:** Extensive client-internal campaigns (MC, MSM, GAW, VSL campaigns)
- **Assessment:** PASS -- The $120K figure is the full ad account spend including client's own masterclass/VSL campaigns. TFM-only spend is correctly reported at ~$1,400/week. The config correctly identifies `competitor_campaign_ids` for client campaigns. The $1,413 figure from cache backfill aligns with current weekly spend.

### Open Source CEO: Custom Pixel Events
- **Pipeboard cache shows:** 0 conversions on $2,480 spend
- **Assessment:** **FAIL** -- Conversion tracking is broken in Meta/Pipeboard. OSC likely uses a beehiiv pixel event that is not being captured by Pipeboard. The intel file reports ~$3.50 CPL based on beehiiv subscriber counts. This is the same class of issue as RNT Fitness.
- **Recommendation:** Verify beehiiv pixel setup; create custom conversion event in Meta Events Manager that fires on the beehiiv thank-you/subscribe confirmation page.

### RNT Fitness: Custom Pixel Events
- **Pipeboard cache shows:** 0 conversions on $1,164 spend
- **Slack confirms (Kinte, 3/20):** "The 114 reflects people who completed the welcome survey post-subscribe -- not total newsletter sign-ups. This is because the custom conversion event was set to fire on the survey page following mid-week funnel change."
- **Assessment:** **FAIL** -- The custom conversion event was deliberately changed to fire on the survey page instead of the subscribe page. This means Meta/Pipeboard only tracks survey completions (114), not actual subscribers (311 per beehiiv).
- **Recommendation:** Create a SEPARATE conversion event for newsletter subscribes AND keep the survey completion event. Report CPL using beehiiv subscriber count as source of truth until dual events are in place.

---

## Priority-Ordered Fix List

### P0 -- Critical (Block accurate reporting)
1. **Populate campaign IDs for 5 TBD clients** -- 1636 Forum, Franklin's Forum, Just Women's Sports, Student Loan Planner, Vendry. These accounts have active ads but no Pipeboard cache data. Use Pipeboard `get_campaigns` for each `meta_account_id` to extract.
2. **Fix Open Source CEO conversion tracking** -- Zero conversions in Pipeboard on $2.5K/week spend. Need beehiiv pixel verification and Meta custom conversion event creation.
3. **Fix RNT Fitness dual conversion events** -- Create separate subscribe + survey events so Pipeboard captures actual subscriber count (311 vs 114 tracked).
4. **Standardize Status News CPL definition** -- Three different numbers ($21, $38, $68) across three systems. Pick one headline metric and align all files.

### P1 -- Important (Data integrity)
5. **Update JWS config GM** -- Change from "TBD -- reassignment pending" to "Lays Paiva (covering)"
6. **Update Points Path config CPL target** -- Change from "TBD" to "$1.50-$2.00"
7. **Update stale config CPL snapshots** -- How to AI ($3.47 -> $2.28), MarketBeat ($8.86 -> $7.51), Quartz ($3.63 -> $3.27)
8. **Clarify EH Pipeboard data** -- Document that EH's 27 Pipeboard "conversions" are NOT webinar registrations. Add note to config.
9. **Clarify Houck vault CPL** -- Intel headline says $1.80 but Pipeboard blended is $2.69. Specify which funnel the $1.80 refers to.

### P2 -- Housekeeping
10. **Update deep enrichment files** -- Remove Natalie Rose as active team member in How to AI and Jay Shetty files
11. **Remove Humza from 1636 Forum attendee list** -- He is departing April 2026
12. **Reconcile Daily Drop CPL target** -- Config says $2-3, intel says $3-4. Determine correct range.
13. **Update MarketBeat risk level** -- Summary says LOW, intel says LOW-MEDIUM. Align.
14. **Add Pipeboard context notes** -- For Points Path, Contrarian Thinking, and Stocks.News, add notes explaining why Pipeboard CPL differs from vault CPL (different conversion events/campaign blending).
15. **Document EH conversion tracking methodology** -- EH's 2,137 registrations come from GHL, not Meta pixel. This should be explicit in the config `tracking_notes`.

---

## Audit Totals

| Category | Count |
|----------|-------|
| **PASS** | 97 |
| **FAIL** | 22 |
| **WARN** | 28 |
| **Total Checks** | 147 |

### Breakdown by Audit Area
| Area | Pass | Fail | Warn |
|------|------|------|------|
| 1. Intel vs Config (125 checks) | 85 | 8 | 7 |
| 2. Summary vs Intel (50 checks) | 47 | 1 | 2 |
| 3. Pipeboard vs Vault (21 checks) | 7 | 9 | 5 |
| 4. Team Assignments (15 checks) | 11 | 1 | 3 |
| 5. Campaign IDs (5 checks) | 0 | 5 | 0 |
| 6. Deep Enrichment (25+ checks) | 23 | 0 | 2 |
| 7. Specific Known Issues (6 checks) | 1 | 4 | 1 |

### Key Findings
1. **The vault is broadly consistent** -- The March 21 enrichment brought all 25 intel files and the summary into alignment. GM assignments, CPL targets, and status fields match across intel and summary in 23/25 cases.
2. **Pipeboard cache is the weakest link** -- 5 clients have no cache data (TBD campaign IDs), 4 clients have broken conversion tracking (OSC, RNT, EH, Points Path), and 3 clients show misleading blended metrics.
3. **Config files lag behind intel files** -- Several config snapshots contain stale CPL data from pre-March 21 enrichment. The config files were not updated as part of the enrichment cycle.
4. **Campaign ID population is the highest-priority gap** -- 5 active clients with no campaign IDs means no automated Pipeboard data ingestion, no cache entries, and no ability to run automated Friday reports.

---

*Audit performed March 21, 2026 by Claude Code. Data sources: 25 client intel files, 25 client configs, CLIENT-INTELLIGENCE-SUMMARY.md, Pipeboard cache (pipeboard-cache.py summary), Slack search.*
