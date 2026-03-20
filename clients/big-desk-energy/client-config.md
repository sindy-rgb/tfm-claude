# Big Desk Energy — Client Config
<!-- Last updated: March 15, 2026 -->
<!-- Skills reference: /system/skills.md -->

---

## Identity

| Field | Value |
|-------|-------|
| `client_name` | big-desk-energy |
| `client_display_name` | Big Desk Energy |
| `client_intel_path` | /Users/jay/Documents/the-feed-media/clients/big-desk-energy/big-desk-energy.md |

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
| Primary | Tyler Denk — Founder — tyler@bigdeskenergy.com |
| Secondary | N/A |

---

## Meta Ads

| Field | Value |
|-------|-------|
| `meta_account_id` | act_1402347147137781 |
| `campaign_ids` | 120209659764470257 (Active — DCT Campaign CPR), 120236433611840257 (Paused — DCT Campaign No Cap), 120224596077790257 (Paused — BG_BDE Newsletter ABO), 120221609685180257 (Paused — BG_BDE SeedDeck ABO), 120220790330410257 (Paused — BG_BDE Newsletter), 120220789528760257 (Paused — BG_BDE SeedDeck) |
| `tfm_campaign_ids` | 120209659764470257 (The Feed - DCT Campaign CPR), 120236433611840257 (The Feed - DCT Campaign No Cap), 120219966944520257 (The Feed - DCT Campaign 04/11), 120218640282360257 (The Feed - DCT Campaign BidCap), 120210326422460257 (The Feed - DCT Campaign no lead magnets), 120209553752630257 (The Feed - DCT Campaign) |
| `competitor_name` | Boletin (BG — previous, TFM won: $2.29 vs Boletin $2.83) |
| `competitor_campaign_ids` | 120224596077790257 (BG_BDE_Newsletter_TestingABO), 120221609685180257 (BG_BDE_SeedDeck_TestingABO), 120220790330410257 (BG_BDE_Newsletter), 120220789528760257 (BG_BDE_SeedDeck) |
| `ad_account_type` | shared (TFM + BG/Boletin historical) |

---

## KPIs & Targets

| Field | Value |
|-------|-------|
| `kpi_primary` | CPL |
| `kpi_target` | sub-$3.00 (stretch: sub-$2.00 — recently achieved at $2.03) |
| `cpl_target` | sub-$3.00 (stretch sub-$2.00) |
| `kpi_secondary` | Open Rate |
| `kpi_secondary_target` | >30% minimum, >35% preferred for scaling |
| `quality_definition` | Subscribers who open at >30%. Tyler will deprioritize low-CPL ads if OR drops below 20-25%. Quality > volume. |

---

## Budget

| Field | Value |
|-------|-------|
| `monthly_budget` | ~$10K/mo (~$2,300-2,500/week), scaling |
| `budget_pacing_target` | ~$330-360/day |
| `budget_notes` | Nearly doubled since January ($1,500/wk to $2,500/wk) with CPL improving. Tyler is open to scaling further if quality holds. |

---

## ESP

| Field | Value |
|-------|-------|
| `esp` | beehiiv |
| `esp_api_access` | TBD |
| `esp_dashboard_url` | N/A |
| `esp_metrics` | open_rate, click_rate, click_score |

---

## Partner Dashboard

| Field | Value |
|-------|-------|
| `partner_dashboard_url` | N/A |
| `partner_dashboard_metrics` | N/A |
| `partner_data_source` | beehiiv dashboard. 1Password for credentials. |

---

## Reporting

| Field | Value |
|-------|-------|
| `report_format` | Weekly report via Google Sheets (automated via n8n bot + manual Click Score by Noreen). Includes CPL, sign-ups, spend, CTR, CVR, Click Score, open rate. |
| `report_destination` | Slack #internal-bigdeskenergy (n8n automated) |
| `report_cadence` | Weekly |
| `report_owner` | Mariely |

---

## Communication Channels

| Field | Value |
|-------|-------|
| `slack_internal` | #internal-bigdeskenergy (C07Q8KK2ED6) |
| `slack_external` | #growth-for-tyler (on timemediaco.slack.com workspace) |
| `day_ai_search_term` | Big Desk Energy |
| `notion_page_url` | TBD |

---

## Creative

| Field | Value |
|-------|-------|
| `dct_naming_prefix` | DCT |
| `next_dct_number` | 235 |
| `brand_voice_tone` | Casual, direct, founder-to-founder. Startup insights, building in public, company culture. Tyler's personal brand is central. "Gatekept" information hooks work well. Freedom > growth messaging resonates — many readers want lifestyle freedom, not unicorn outcomes. |
| `never_rules` | Never run low-OR ads — Tyler kills sub-20% OR ads regardless of CPL | Never let lead quality decline without immediate ad set adjustments | Never let report quality slip during GM handover |
| `approved_language` | gatekept, building in public, startup culture, founder-led, seed deck, side project, going full-time |
| `audience_segments` | Founders and startup operators | Aspiring entrepreneurs wanting to quit 9-5 | Early-stage launchers | Growth-stage operators scaling to $1M |
| `landing_page_urls` | class.thefeedmedia.com/workshop-for-big-desk-energy/ |

---

## UTM / Tracking

| Field | Value |
|-------|-------|
| `utm_format` | standard (utm_source=facebookads&utm_medium={{adset.name}}&utm_campaign={{ad.name}}) |
| `tracking_notes` | CAPI integration incomplete — Meta pixel owned by beehiiv, not BDE's business manager. Token generation needs Tyler's team. |

---

## Relationship Context

| Field | Value |
|-------|-------|
| `relationship_health` | Positive — Tyler engaged, responsive, spend scaling = confidence signal |
| `sync_cadence` | TBD |
| `biggest_risk` | Humza to Mariely GM handover (Humza leaves April 2026). Quality gaps showing in reports and beehiiv access. 0/4 March concepts sent to client. Friday reports missing (0/2 on-time). CAPI integration incomplete. |
