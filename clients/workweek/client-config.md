# Workweek — Client Config
<!-- Last updated: March 15, 2026 -->
<!-- Skills reference: /system/skills.md -->

---

## Identity

| Field | Value |
|-------|-------|
| `client_name` | workweek |
| `client_display_name` | Workweek |
| `client_intel_path` | /Users/jay/Documents/the-feed-media/clients/workweek/workweek.md |

---

## Team

| Field | Value |
|-------|-------|
| `gm_name` | Lays |
| `media_buyer_name` | Rabii Elhaouat |

---

## Client Contacts

| `contacts` | |
|------------|---|
| Primary | Mike Madarasz — Budget Owner / Creative Approver — mike@workweek.com |
| Secondary | Adam Ryan — Head of Sales — adam@workweek.com |
| Newsletter | Hebba Youssef — IHIH Creator — ihateithere@workweek.com |

---

## Meta Ads

| Field | Value |
|-------|-------|
| `meta_account_id` | 5 separate accounts: IHIH=act_3186358998360632, TMM=act_579954186820640, FTT=act_1079516909306359, Hospitalogy=act_718612189266939, GTM=act_4673797136057796 |
| `campaign_ids` | **IHIH:** 120238290253090498 (Active — TFM LEADS 01/01/26), 120208519540300498 (Active — IHIH_PR_Newsletter) | **TMM:** 120241087157250671 (Active — TFM LEADS 01/01/26) | **FTT:** 120238837962440504 (Active — TFM LEADS 01/01/26) | **Hospitalogy:** 120238302528030086 (Active — TFM LEADS 03/01/26) | **GTM:** 120240688746600606 (Active — TFM LEADS 03/01/26) |
| `tfm_campaign_ids` | **IHIH:** 120238290253090498, 120208519540300498 | **TMM:** 120241087157250671 | **FTT:** 120238837962440504 | **Hospitalogy:** 120238302528030086 | **GTM:** 120240688746600606 |
| `competitor_name` | N/A |
| `competitor_campaign_ids` | N/A |
| `ad_account_type` | TFM-managed (5 separate accounts, one per newsletter) |

---

## KPIs & Targets

| Field | Value |
|-------|-------|
| `kpi_primary` | Verified Subscriber CAC (V-CAC) |
| `kpi_target` | Per newsletter: IHIH $45, TMM $40, FTT $55, Hospitalogy $40, GTM $170 |
| `cpl_target` | Raw CPL does NOT count — only verified (membership-approved) subscribers matter |
| `kpi_secondary` | Verification Rate |
| `kpi_secondary_target` | N/A — varies by newsletter |
| `quality_definition` | Subscriber who passes Workweek's membership verification process. Raw CPL is meaningless for this client. |

---

## Budget

| Field | Value |
|-------|-------|
| `monthly_budget` | ~$92,500 total across 5 newsletters (IHIH $30K, TMM $30K, FTT $15K, Hospitalogy $10K, GTM $7.5K) |
| `budget_pacing_target` | ~$3,080/day total across all 5 accounts |
| `budget_notes` | Mike frequently shifts budgets based on internal sales pipeline and profitability — NOT performance dissatisfaction. Expansion signal: Fintech Takes Banking at $10-15K/mo. |

---

## ESP

| Field | Value |
|-------|-------|
| `esp` | Sailthru |
| `esp_api_access` | TBD |
| `esp_dashboard_url` | TBD |
| `esp_metrics` | verified_subscribers, v-cac, verification_rate |

---

## Partner Dashboard

| Field | Value |
|-------|-------|
| `partner_dashboard_url` | TBD |
| `partner_dashboard_metrics` | V-CAC, verified volume, quality score |
| `partner_data_source` | Workweek internal dashboard — quality cap at 0.85 can mask improvements. Use internal V-CAC as source of truth. |

---

## Reporting

| Field | Value |
|-------|-------|
| `report_format` | Per-newsletter breakdown with V-CAC (vs target), verified volume, spend, top creatives. Must include V-CAC — raw CPL reporting is unacceptable for this client. |
| `report_destination` | Slack #thefeed-workweekgrowth |
| `report_cadence` | weekly (Friday) + bi-weekly (client calls) |
| `report_owner` | Lays |

---

## Communication Channels

| Field | Value |
|-------|-------|
| `slack_internal` | #internal-workweek (C09UD5BV2BF) |
| `slack_external` | #thefeed-workweekgrowth (C09SZN1HB41) |
| `day_ai_search_term` | Workweek |
| `notion_page_url` | TBD |

---

## Creative

| Field | Value |
|-------|-------|
| `dct_naming_prefix` | DCT_ |
| `next_dct_number` | TBD |
| `brand_voice_tone` | Varies by newsletter — IHIH: vulnerability-first empathy; FTT: authority gatekeeping; TMM: anti-guru tactical utility; Hospitalogy: unfair advantage/life hack; GTM: in-the-trenches operator pain |
| `never_rules` | NEVER show inconsistent subscriber counts across ad creatives, body copy, and landing pages | NEVER use polished/corporate brand video aesthetic |
| `approved_language` | Per newsletter voice archetype — see brand voice section in intel file |
| `audience_segments` | HR / People Ops professionals (IHIH) | Marketing professionals (TMM) | VP/Director-level financial services (FTT) | Healthcare operations executives (Hospitalogy) | DTC / Ecom founders (GTM) |
| `landing_page_urls` | TBD — custom WordPress sites per newsletter |

---

## UTM / Tracking

| Field | Value |
|-------|-------|
| `utm_format` | standard (utm_source=facebookads&utm_medium={{adset.name}}&utm_campaign={{ad.name}}) |
| `tracking_notes` | Broad audiences outperform segmented across all 5 accounts — Mike approved full migration to broad targeting. |

---

## Relationship Context

| Field | Value |
|-------|-------|
| `relationship_health` | STRONG — Peak Moment. All 5 accounts GREEN simultaneously (first time ever, March 2026). CEO very happy. |
| `sync_cadence` | Bi-weekly |
| `biggest_risk` | LOW. Budget shifts are internal (sales pipeline), not performance-driven. Subscriber count inconsistency across creatives is the highest-priority fix. GTM verification funnel has 3.7% convert rate — post-subscribe flow problem, not creative. |
