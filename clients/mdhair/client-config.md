# MDhair — Client Config
<!-- Last updated: March 21, 2026 -->
<!-- Skills reference: /system/skills.md -->

---

## Identity

| Field | Value |
|-------|-------|
| `client_name` | mdhair |
| `client_display_name` | MDhair |
| `client_intel_path` | clients/mdhair/mdhair.md |

---

## Team

| Field | Value |
|-------|-------|
| `gm_name` | Kinte |
| `media_buyer_name` | N/A (Creative Only — MDhair handles media buying) |

---

## Client Contacts

| `contacts` | |
|------------|---|
| Primary | Yasin Mahmood — Head of Growth Marketing — yasin@mdacne.com |
| Secondary | Pooja Kandappa — Head of Creative — pooja@mdacne.com |
| Executive | Oded Harth — CEO — oded@mdacne.com |

---

## Meta Ads

| Field | Value |
|-------|-------|
| `meta_account_id` | N/A (TFM does not have direct ad account access — relying on manual exports from client) |
| `campaign_ids` | N/A (client-managed) |
| `tfm_campaign_ids` | N/A (creative-only engagement) |
| `competitor_name` | Nutrafol (price comparison allowed) |
| `competitor_campaign_ids` | N/A |
| `ad_account_type` | N/A (client-managed) |

---

## KPIs & Targets

| Field | Value |
|-------|-------|
| `kpi_primary` | Customer Acquisition Cost (CAC) |
| `kpi_target` | ~$80 |
| `cpl_target` | N/A — CAC is the metric, not CPL |
| `kpi_secondary` | Conversion Rate (quiz to subscription) |
| `kpi_secondary_target` | TBD |
| `quality_definition` | Customers who complete the quiz, receive a personalized regimen, and subscribe monthly. Source of truth is Mixpanel (not Meta). Testing threshold: 5-6x CAC spend per concept before performance decisions. |

---

## Budget

| Field | Value |
|-------|-------|
| `monthly_budget` | ~$5,000/month (TFM fee for 8 concepts/month) |
| `budget_pacing_target` | N/A (client manages media spend — ~$84K/week total account in March 2026) |
| `budget_notes` | Creative-only engagement. 8 concepts/month. $100-200 per UGC creator (up to $300 for established talent). 3-month rolling contract. TFM does NOT control media spend. |

---

## ESP

| Field | Value |
|-------|-------|
| `esp` | N/A (DTC — not a newsletter client) |
| `esp_api_access` | N/A |
| `esp_dashboard_url` | N/A |
| `esp_metrics` | N/A |

---

## Partner Dashboard

| Field | Value |
|-------|-------|
| `partner_dashboard_url` | N/A |
| `partner_dashboard_metrics` | N/A |
| `partner_data_source` | Mixpanel (first-touch attribution). Manual exports from client. Pipeboard/Zapier automation for Meta data explored but unresolved. |

---

## Reporting

| Field | Value |
|-------|-------|
| `report_format` | CAC per concept, conversion rate, spend per creative. Weekly ad reports (Monday delivery, covering Fri-Thu). |
| `report_destination` | Slack #thefeed-mdhair |
| `report_cadence` | weekly (Monday) + bi-weekly (client syncs) |
| `report_owner` | Kinte |

---

## Communication Channels

| Field | Value |
|-------|-------|
| `slack_internal` | #internal-mdhair |
| `slack_external` | #thefeed-mdhair |
| `slack_pod` | #cs-tpg-mdhair (shared pod with TPG) |
| `day_ai_search_term` | MDhair |
| `notion_page_url` | TBD |

---

## Creative

| Field | Value |
|-------|-------|
| `dct_naming_prefix` | DCT_ |
| `next_dct_number` | 129 |
| `brand_voice_tone` | Scientific but accessible. Emotional validation (especially shedding, postpartum, confidence). Dermatologist-formulated, AI-personalized. Key stats: 88.9% reported improvement, 37.3% shedding reduction at 12 weeks, 100+ active ingredients. |
| `never_rules` | NEVER position Minoxidil as negative — MDhair offers it to some customers. Can position as better than Finasteride and hair transplants | NEVER misspell brand name — it is "MDhair" (no space, capital M and D) | NEVER use a CTA other than "Take the quiz" | NEVER omit "up to 60% off" offer in relevant creative | NEVER skip AI-generated content disclaimer | NEVER reference money-back guarantees without T&Cs | NEVER use generic branded statics — client exhausted these internally | NEVER use fake or unverifiable claims |
| `approved_language` | dermatologist-formulated, AI-personalized, Hair Growth Kit, personalized treatment plan, take the quiz, up to 60% off, sulfate-free paraben-free vegan |
| `audience_segments` | Women experiencing hair loss (shedding, postpartum, thinning) | Men experiencing hair loss (DHT, thinning) | Key split: women gravitate toward serums, men toward shampoo |
| `landing_page_urls` | mdhair.co |

---

## UTM / Tracking

| Field | Value |
|-------|-------|
| `utm_format` | N/A (client-managed media buying) |
| `tracking_notes` | Source of truth is Mixpanel, not Meta. TFM does not have direct Meta ad account access. Brand compliance is strict — fonts, colors, logos must be exact. UGC scripts must be approved BEFORE production. |

---

## Relationship Context

| Field | Value |
|-------|-------|
| `relationship_health` | Positive with Operational Risk |
| `sync_cadence` | Bi-weekly |
| `biggest_risk` | Kinte took over from Humza (March 2026) — Humza was the relationship originator (Yasin is his brother). No direct ad account access limits reporting speed. Current CAC at $130 (elevated due to testing phase). March sprint at 53% target completion. AI morph ads generate negative comments — format sensitivity. |
