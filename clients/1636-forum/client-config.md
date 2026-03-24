# 1636 Forum — Client Config
<!-- Last updated: March 21, 2026 -->
<!-- Skills reference: /system/skills.md -->

---

## Identity

| Field | Value |
|-------|-------|
| `client_name` | 1636-forum |
| `client_display_name` | 1636 Forum |
| `client_intel_path` | clients/1636-forum/1636-forum.md |

---

## Team

| Field | Value |
|-------|-------|
| `gm_name` | Mariely Galindo |
| `media_buyer_name` | Rabii Elhaouat |

---

## Client Contacts

| `contacts` | |
|------------|---|
| Primary | Allison Wu — Operations/Data Lead — awu@1636forum.com |
| Secondary | Ali Warshay — Ad Reviewer/Analytics — awarshay@1636forum.com |
| Secondary | Gabrielle (Gigi) Solomon — Creative Direction (Franklin's Forum) — gsolomon@1636forum.com |

---

## Meta Ads

| Field | Value |
|-------|-------|
| `meta_account_id` | Not in Pipeboard DB (deep-enrichment references act_2257251771354778, but this may be a new/migrated account) |
| `campaign_ids` | TBD |
| `tfm_campaign_ids` | TBD |
| `competitor_name` | N/A |
| `competitor_campaign_ids` | N/A |
| `ad_account_type` | TFM-managed |

---

## KPIs & Targets

| Field | Value |
|-------|-------|
| `kpi_primary` | Cost Per Lead (CPL) |
| `kpi_target` | < $2.00 (current overall: $2.34; recent 7-day: $3.01) |
| `cpl_target` | < $2.00 |
| `kpi_secondary` | Email Open Rate |
| `kpi_secondary_target` | > 40% per ad |
| `quality_definition` | Harvard-affiliated subscribers (alumni, faculty, parents). Effective qualified CPL is ~$7. Email open rate 40%+. Non-alumni are deprioritized for quality purposes. |

---

## Budget

| Field | Value |
|-------|-------|
| `monthly_budget` | ~$6,000 ($1,380-1,400/week) |
| `budget_pacing_target` | ~$200/day |
| `budget_notes` | Pricing: $6K/month base + 50% for Franklin's Forum. No end-date contract — retention-focused. |

---

## ESP

| Field | Value |
|-------|-------|
| `esp` | beehiiv |
| `esp_api_access` | TBD |
| `esp_dashboard_url` | TBD |
| `esp_metrics` | open_rate, click_rate, unsubscribe_rate, alumni_vs_nonalumni_segmentation |

---

## Partner Dashboard

| Field | Value |
|-------|-------|
| `partner_dashboard_url` | N/A |
| `partner_dashboard_metrics` | N/A |
| `partner_data_source` | beehiiv subscriber survey (alumni / friend / parent segmentation) |

---

## Reporting

| Field | Value |
|-------|-------|
| `report_format` | CPL, sign-ups, CTR, CVR, open rate, per-DCT creative performance. Must include alumni quality signals (open rate per ad, alumni segmentation data). |
| `report_destination` | Slack #thefeed-1636forum + Google Sheets weekly report |
| `report_cadence` | weekly (Friday) + bi-weekly (client calls, Tuesdays) |
| `report_owner` | Mariely Galindo |

---

## Communication Channels

| Field | Value |
|-------|-------|
| `slack_internal` | #internal-1636forum (C09ASEF84FP) |
| `slack_external` | #thefeed-1636forum (C09BJBYS4FJ) |
| `day_ai_search_term` | 1636 Forum |
| `notion_page_url` | https://www.notion.so/25cf4a126e0680d69605ffee55f8761a |

---

## Creative

| Field | Value |
|-------|-------|
| `dct_naming_prefix` | DCT_ |
| `next_dct_number` | 124 |
| `brand_voice_tone` | Calm, grounded, intellectual — not alarmist or performative. Community-oriented but not exclusive-feeling. Concern-driven without being outrage-driven. |
| `never_rules` | NEVER use "honest news" — newsletter is analysis and community, not news | NEVER position as political or agenda-driven — principled neutrality | NEVER target faculty directly — positioning is "for alumni" | NEVER use founder's face/likeness in ads — Allison explicitly banned this | NEVER frame as a "news roundup" — focus on alumni concerns and institutional change | NEVER copy text from briefs without exact capitalization |
| `approved_language` | sharp independent analysis, no spin, no partisan noise, Harvard Explained Clearly, 5 minutes weekly always free, join for free, get the briefing |
| `audience_segments` | Harvard alumni 30-70 (primary — high-achieving professionals) | Friends/parents of alumni (secondary — deprioritized for quality) |
| `landing_page_urls` | news.1636forum.com/subscribe |

---

## UTM / Tracking

| Field | Value |
|-------|-------|
| `utm_format` | standard (utm_source=facebookads&utm_medium={{adset.name}}&utm_campaign={{ad.name}}) |
| `tracking_notes` | Text-over-video is dominant winning format. DCT_104 is fatiguing — CPL trending up from $2.15 to $3.01. Alumni quality tracked via beehiiv subscriber survey segmentation. |

---

## Relationship Context

| Field | Value |
|-------|-------|
| `relationship_health` | Cautiously Positive |
| `sync_cadence` | Bi-weekly (Tuesdays, rescheduled frequently) |
| `biggest_risk` | CPL trending above $2.00 target as DCT_104 fatigues. Effective qualified (Harvard-affiliated) CPL is ~$7. Sister publication Franklin's Forum adds complexity. Creative pipeline needs fresh concepts to replace fatiguing anchor ads. |
