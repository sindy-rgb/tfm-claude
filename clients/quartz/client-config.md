# Quartz — Client Config
<!-- Last updated: March 15, 2026 -->
<!-- Skills reference: /system/skills.md -->

---

## Identity

| Field | Value |
|-------|-------|
| `client_name` | quartz |
| `client_display_name` | Quartz |
| `client_intel_path` | clients/quartz/quartz.md |

---

## Team

| Field | Value |
|-------|-------|
| `gm_name` | Mariely |
| `media_buyer_name` | Rabii Elhaouat |

---

## Client Contacts

| `contacts` | |
|------------|---|
| Primary | Armando Roggio — Decision-maker — TBD |
| Secondary | Simon — Creative Approval / LP Builds — TBD |

---

## Meta Ads

| Field | Value |
|-------|-------|
| `meta_account_id` | act_757128750591828 |
| `campaign_ids` | 120240219255170549 (Active — GL Website Sign Ups CBO), 120239976753120549 (Active — TFM Subscribe Broad), 120239544702600549 (Active — BG_Quartz_Signups), 120235786427000549 (Active — GL Lead Form Signups CBO) |
| `tfm_campaign_ids` | 120239976753120549 (The Feed Media - Subscribe - Broad) |
| `competitor_name` | Boletin (BG), Grow Letter (GL) |
| `competitor_campaign_ids` | 120239544702600549 (BG_Quartz_Signups), 120240219255170549 (GL Website Sign Ups CBO), 120235786427000549 (GL Lead Form Signups CBO), 120232125285050549 (NEW_GL_LeadCampaign), 120231717844250549 (GL_LeadCampaign_WRONG EVENT), 120230343087490549 (GL_LeadCampaign) |
| `ad_account_type` | shared (3-agency bake-off: TFM + BG + GL) |

---

## KPIs & Targets

| Field | Value |
|-------|-------|
| `kpi_primary` | CPL |
| `kpi_target` | <= $2.50 |
| `cpl_target` | <= $2.50 (current: $3.27 — 31% above target, improving) |
| `kpi_secondary` | Subscriber Quality |
| `kpi_secondary_target` | Open rate >50%, Click rate >5% within first 15 days |
| `quality_definition` | Subscribers who open (>50%) and click (>5%) within first 15 days. Competition rules for how CPL vs quality are weighted remain ambiguous — Armando has not clarified. |

---

## Budget

| Field | Value |
|-------|-------|
| `monthly_budget` | $7,000 media + $3,600 agency fee |
| `budget_pacing_target` | ~$233/day |
| `budget_notes` | Bake-off budget (Feb 1 - Mar 31, 2026). Each of 3 agencies gets the same budget. Post-test (April): One agency selected for quarterly engagement ($10,700/quarter). |

---

## ESP

| Field | Value |
|-------|-------|
| `esp` | Delivra |
| `esp_api_access` | false |
| `esp_dashboard_url` | N/A |
| `esp_metrics` | open_rate, click_rate |

---

## Partner Dashboard

| Field | Value |
|-------|-------|
| `partner_dashboard_url` | N/A |
| `partner_dashboard_metrics` | N/A |
| `partner_data_source` | Armando shared manual quality tracking sheet. Quartz measures open rate and click rate within first 15 days of subscription. |

---

## Reporting

| Field | Value |
|-------|-------|
| `report_format` | CPL, CTR, CVR, subscriber quality metrics. Must include comparison to competitor agencies (BG and GL) where available. |
| `report_destination` | Slack #thefeed-quartz |
| `report_cadence` | Weekly (Friday) + bi-weekly client calls |
| `report_owner` | Mariely |

---

## Communication Channels

| Field | Value |
|-------|-------|
| `slack_internal` | #internal-quartz (C0A4Y7GG230) |
| `slack_external` | #thefeed-quartz (C09P4UM9VMW) |
| `day_ai_search_term` | Quartz |
| `notion_page_url` | TBD |

---

## Creative

| Field | Value |
|-------|-------|
| `dct_naming_prefix` | DCT_ |
| `next_dct_number` | 112 |
| `brand_voice_tone` | Calm, confident, interpretive — slightly skeptical but not cynical. Conversational but intellectually sharp. Assumes the reader is smart, busy, and capable of nuance. "You don't need to panic — you need context." |
| `never_rules` | Never use emojis in final creative | Never use alarmist or fear-driven language — "Never alarmist, even when stakes are high" | Never use partisan framing | Never use flashy animations or stock newsroom montages | Never write full paragraphs in video ads — text appears in blocks | Never reuse B-roll across hook variations | Never position like 1440 (facts only), Morning Brew (casual), or Bloomberg (dense) |
| `approved_language` | interpretation, context, nuance, insight without terminal brain, credibility, depth |
| `audience_segments` | Strategic Decision-Makers | Aspiring Leaders | Policy Thinkers | Finance professionals | CEOs and founders |
| `landing_page_urls` | quartz.qz.com/join-the-quartz-daily-brief/ |

---

## UTM / Tracking

| Field | Value |
|-------|-------|
| `utm_format` | standard (utm_source=facebookads&utm_medium={{adset.name}}&utm_campaign={{ad.name}}) |
| `tracking_notes` | Landing pages built on Leadpages. Reporting discrepancy flagged — needs fixing before Thursday sync. |

---

## Relationship Context

| Field | Value |
|-------|-------|
| `relationship_health` | Cautious — Under Competitive Pressure (3rd place in bake-off on CPL and quality) |
| `sync_cadence` | Bi-weekly |
| `biggest_risk` | 3-agency bake-off (Feb 1 - Mar 31). TFM CPL improved to $3.27 (was $3.63) but still above BG and GL. 10 days remain. CRITICAL: 92.6% of TFM subscribers never received a Delivra broadcast — quality comparison is meaningless until this is fixed. The 58 TFM subs who DO receive email show 84.8% open rates (best of all agencies). Armando committed to audit but has gone silent since Mar 18. |
