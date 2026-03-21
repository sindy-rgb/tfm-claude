# MarketBeat — Client Config
<!-- Last updated: March 21, 2026 -->
<!-- Skills reference: /system/skills.md -->

---

## Identity

| Field | Value |
|-------|-------|
| `client_name` | marketbeat |
| `client_display_name` | MarketBeat |
| `client_intel_path` | /Users/jay/Documents/the-feed-media/clients/marketbeat/marketbeat.md |

---

## Team

| Field | Value |
|-------|-------|
| `gm_name` | Luiz Pekelman |
| `media_buyer_name` | Rabii Elhaouat |

---

## Client Contacts

| `contacts` | |
|------------|---|
| Primary | Matt Paulson — Founder — matt@marketbeat.com |
| Secondary | Maureen Ohm — Stakeholder — maureen@marketbeat.com |

---

## Meta Ads

| Field | Value |
|-------|-------|
| `meta_account_id` | act_1129788478833121 |
| `campaign_ids` | 120234644644600565 |
| `tfm_campaign_ids` | 120234644644600565 |
| `competitor_name` | GrowJoy |
| `competitor_campaign_ids` | 120226438970390565, 120242548982060565 |
| `ad_account_type` | partner |

---

## KPIs & Targets

| Field | Value |
|-------|-------|
| `kpi_primary` | ROAS |
| `kpi_target` | 45% (match GrowJoy → unlock 2x budget) |
| `cpl_target` | $10-14 (current: $7.51, well under target) |
| `kpi_secondary` | SMS Opt-ins |
| `kpi_secondary_target` | Close gap with GrowJoy (currently 6.2x behind in March) |
| `quality_definition` | Revenue-generating subscriber — measured by Rev/User and confirmed sales on partner dashboard |

---

## Budget

| Field | Value |
|-------|-------|
| `monthly_budget` | $60,000 |
| `budget_pacing_target` | $2,000/day |
| `budget_notes` | Matt approved $2K/day on Feb 20, 2026 ("you can go to $2K/day and that will also be the budget for March"). Currently pacing ~$1,911/day in March. GrowJoy spends ~$10K/day. |

---

## ESP

| Field | Value |
|-------|-------|
| `esp` | Custom (MarketBeat internal — not accessible to TFM) |
| `esp_api_access` | false |
| `esp_dashboard_url` | N/A |
| `esp_metrics` | N/A — subscriber data tracked via partner dashboard only |

---

## Partner Dashboard

| Field | Value |
|-------|-------|
| `partner_dashboard_url` | https://americanconsumernews.net/scripts/partners/TheFeedExport.aspx |
| `partner_dashboard_metrics` | Leads (Revenue Leads), Estimated Revenue, Confirmed Sales, Rev/User, SMS Opt-ins |
| `partner_data_source` | n8n daily ROAS report (posted to #internal-marketbeat) + manual dashboard pull (month selector available) |

---

## Reporting

| Field | Value |
|-------|-------|
| `report_format` | Rabii's format: ROAS-first, concise, conversational tone to Matt. Opens with MTD ROAS vs GrowJoy gap. Top ROAS ads with spend→revenue. Next steps on creative pipeline. No internal metrics (CPM, CPC, LP CVR). See #thefeed-marketbeat history for examples. |
| `report_destination` | Slack #thefeed-marketbeat (client-facing, posted directly to Matt) + Notion (Friday report archive) |
| `report_cadence` | weekly (Friday) + bi-weekly (client calls with Matt/Maureen) |
| `report_owner` | Rabii Elhaouat (took over from Luiz per Sindy's Jan 23 decision — MarketBeat is sensitive client, Rabii owns client-facing reports) |

---

## Communication Channels

| Field | Value |
|-------|-------|
| `slack_internal` | #internal-marketbeat (C09EDCNGFD0) |
| `slack_external` | #thefeed-marketbeat |
| `day_ai_search_term` | MarketBeat |
| `notion_page_url` | [MarketBeat Client OS page in Notion] |

---

## Creative

| Field | Value |
|-------|-------|
| `dct_naming_prefix` | DCT_ |
| `next_dct_number` | 200 |
| `brand_voice_tone` | Authority-driven, data-backed, actionable. "Smart money" positioning. Two ICPs with different hooks. |
| `never_rules` | Never use "MarketBeat" in ad creative (ads run under Early Bird Publishing) | Never make specific stock price predictions | Never use FOMO on specific stocks | Never conflate free newsletter with premium subscription | NEVER use nuclear/energy B-roll or imagery — Matt personally killed DCT_149 on Mar 6 ("That's the ad that got our old account banned"). Nuclear B-roll is an account ban risk. The nuclear stocks LP can still be used but creative must avoid nuclear imagery/footage. |
| `approved_language` | Smart money, edge, free report, $29.97 report yours free today, download free report now |
| `audience_segments` | Frank (60-70, conservative, near retirement, protecting wealth, dividend-focused) | Brian (35-45, aggressive investor, growth stocks, AI/tech, "what Wall Street insiders are watching") |
| `landing_page_urls` | earlybirdpublishing.com/users/PDFoffer.aspx?offer=newyear (primary — Top 10 Stocks), earlybirdpublishing.com/users/PDFoffer.aspx?offer=spacestocks (Space Stocks — DCT_199), marketbeat.com/newsletter/pdfoffer.aspx?offer=10BestAIStocks (AI Stocks), marketbeat.com/newsletter/pdfoffer.aspx?offer=nuclearstocks (Nuclear — DCT_149), marketbeat.com/newsletter/PDFOffer.aspx?offer=highyield (High-Yield Dividend — NEW Mar 10) |

---

## UTM / Tracking

| Field | Value |
|-------|-------|
| `utm_format` | RegistrationCode=meta-thefeedmedia-dctXXX (NOT standard UTMs) |
| `tracking_notes` | Original MarketBeat ad account was banned. All ads run under Early Bird Publishing domain. RegistrationCode is the attribution key — each DCT gets a unique code. Partner dashboard (TheFeedExport) breaks down performance by RegistrationCode. |

---

## Relationship Context

| Field | Value |
|-------|-------|
| `relationship_health` | Positive — Momentum Phase |
| `sync_cadence` | Bi-weekly (client calls with Matt/Maureen) + daily internal (n8n ROAS reports) |
| `biggest_risk` | ROAS gap vs GrowJoy is the existential risk. Matt allocates budget mathematically — no relationship cushion. Match GrowJoy = 2x budget. Fail = lose the account. |

---

## Current Performance Snapshot (March 11, 2026)

<!-- Updated by /friday or /competitive runs. Not a config variable — a quick reference. -->

| Metric | TFM | GrowJoy | Gap |
|--------|-----|---------|-----|
| ROAS (Mar 1-10) | 41.8% | 46.6% | -4.8 pts |
| CPL | $11.55 | $11.64 | TFM cheaper |
| Rev/User | $4.82 | $5.42 | -$0.60 |
| SMS Opt-ins | 284 | 1,928 | GJ 6.8x |
| Confirmed Sales | 7 | 51 | — |

### ROAS Gap Trend
| Month | Gap |
|-------|-----|
| January | -14 pts |
| February | -5.1 pts |
| March (1-10) | -4.8 pts |

### Top DCTs (March — by Rev/User from partner dashboard)
| DCT | Rev/User | Pixel CPL | Confirmed Sales |
|-----|----------|-----------|-----------------|
| DCT_140 (10 Stocks) | $7.84 | $11.89 | 2 |
| DCT_137 (Politics Proof) | $6.27 | $10.87 | 1 |
| DCT_134 (Results Speak) | $5.44 | $10.92 | 0 |
| DCT_151 (Last One) | $4.98 | $11.67 | 0 |
| DCT_131 (Sector Rotation) | $4.93 | $7.71 | 1 |
| DCT_132 (Near Retiree) | $4.59 | $7.72 | 4 |
| DCT_130 (2 Waves) | $4.23 | $6.51 | 0 |
| DCT_149 (Nuclear Boom) | $4.07 | $7.04 | 0 | **KILLED by Matt Mar 6 — account ban risk** |
