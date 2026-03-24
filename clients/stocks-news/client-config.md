# Stocks.News — Client Config
<!-- Last updated: March 21, 2026 -->
<!-- Skills reference: /system/skills.md -->

---

## Identity

| Field | Value |
|-------|-------|
| `client_name` | stocks-news |
| `client_display_name` | Stocks.News |
| `client_intel_path` | clients/stocks-news/stocks-news.md |

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
| Primary | Margaret Powell — CMO / Primary Contact — margaret@stocks.news |
| Secondary | Raf — Founder/CEO — raf@stocks.news |
| Technical | Joe / Joseph Lombas — CTO — joe@stocks.news |

---

## Meta Ads

| Field | Value |
|-------|-------|
| `meta_account_id` | act_966430194860576 |
| `campaign_ids` | 120242193401400071 (Active — TFM Start Trial), 120241993404490071 (Active — TFM App Installs), 120241992974490071 (Active — TFM App Trials), 120240942718220071 (Active — TFM Lead Gen Broad), 120241950381480071 (Active — Growjoy Start Trial), 120241774694610071 (Paused — Growjoy App Installs) |
| `tfm_campaign_ids` | 120242193401400071 (The Feed Media - Start Trial), 120242023971680071 (The Feed Media - App Installs Broad — Paused), 120241993404490071 (The Feed Media - App Installs), 120241992974490071 (The Feed Media - App Trials), 120240942718220071 (TFM - Lead Generation - Broad) |
| `competitor_name` | GrowJoy |
| `competitor_campaign_ids` | 120241950381480071 (Growjoy - Start Trial), 120241774694610071 (Growjoy - App Installs), 120241291024630071 (Growjoy - Leads Campaign) |
| `ad_account_type` | shared (TFM + GrowJoy) |

---

## KPIs & Targets

| Field | Value |
|-------|-------|
| `kpi_primary` | Cost Per Trial Start |
| `kpi_target` | < $60 (stretch ~$38) |
| `cpl_target` | Cost Per Install < $10 (current: $6.50) |
| `kpi_secondary` | Cost Per Install |
| `kpi_secondary_target` | < $10 |
| `quality_definition` | User who starts a trial ($9.99/mo or $97/year app subscription). Day traders, NOT long-term investors. |

---

## Budget

| Field | Value |
|-------|-------|
| `monthly_budget` | Scaling — currently ~$24K/mo ($800/day), approved to scale to $3,000/day (~$90K/mo) |
| `budget_pacing_target` | Scaling from $800/day → $3,000/day (~20% increase every 2-3 days) |
| `budget_notes` | Margaret approved scale to $3,000/day (March 10). Past $35K/mo triggers commercial impact — Nathan needs 1:1 with Margaret on fee increase. Budget trajectory: $400/day → $800/day → $1,000/day → $3,000/day. Competing agency GrowJoy runs simultaneously; budgets move based on performance. |

---

## ESP

| Field | Value |
|-------|-------|
| `esp` | Custom app (stocks.news / app.stocks.news) |
| `esp_api_access` | false |
| `esp_dashboard_url` | N/A |
| `esp_metrics` | installs, trial_starts, install_cvr, trial_cvr |

---

## Partner Dashboard

| Field | Value |
|-------|-------|
| `partner_dashboard_url` | TBD |
| `partner_dashboard_metrics` | N/A |
| `partner_data_source` | AppsFlyer attribution (gap exists — in progress). Down-funnel subscription data not yet available. |

---

## Reporting

| Field | Value |
|-------|-------|
| `report_format` | Cost Per Trial Start, Cost Per Install, Install CVR, Trial CVR, spend, top creatives. Compare vs GrowJoy performance. |
| `report_destination` | Slack #thefeed-stocksnews |
| `report_cadence` | Bi-weekly (every other Tuesday starting March 17) |
| `report_owner` | Luiz Pekelman |

---

## Communication Channels

| Field | Value |
|-------|-------|
| `slack_internal` | #internal-stocksnews (C0A2ZMQTCFR) |
| `slack_external` | #thefeed-stocksnews (C0A3XANP1DF) |
| `day_ai_search_term` | Stocks.News |
| `notion_page_url` | TBD |

---

## Creative

| Field | Value |
|-------|-------|
| `dct_naming_prefix` | DCT_ |
| `next_dct_number` | TBD |
| `brand_voice_tone` | Feature-specific, compliance-careful. Use "might" instead of definitive claims. Competitive framing allowed (scanner competitors charge $100-160/mo; Stocks.News is $9.99/mo). Text-over-video outperforms all other formats. |
| `never_rules` | NEVER imply stock recommendations or picks — SEC compliance | NEVER claim risk ratio evaluations — app does not make risk/reward assessments | NEVER call the scanner "AI Scanner" — it presents real-time data, not AI analysis | NEVER claim alerts are SMS if they require the app | NEVER say "free" unless true for all features | NEVER misrepresent politician trade tracking — trades reported within 30 days | Use "might" instead of definitive claims |
| `approved_language` | "Stocks Dot News" (spoken) or "Stocks.News" (written), feature-specific descriptions, "Breaking news alerts delivered through the app" |
| `audience_segments` | Day traders (primary) | Active stock market participants | NOT long-term investors |
| `landing_page_urls` | thefinaltally.com, stocks.news/signup/ |

---

## UTM / Tracking

| Field | Value |
|-------|-------|
| `utm_format` | standard (utm_source=facebookads&utm_medium={{adset.name}}&utm_campaign={{ad.name}}) |
| `tracking_notes` | AppsFlyer attribution gap (medium risk). Down-funnel subscription data not yet available. Creative compliance rejections common on first pass — playbook now updated. |

---

## Relationship Context

| Field | Value |
|-------|-------|
| `relationship_health` | POSITIVE and IMPROVING. Margaret openly pleased. TFM winning vs GrowJoy ($38 vs $42 CPT). Budget scaling approved. |
| `sync_cadence` | Bi-weekly (every other Tuesday starting March 17) |
| `biggest_risk` | AppsFlyer attribution gap. Confirm budget increase is ongoing vs temporary. Creative compliance rejections on first pass. Nathan needs 1:1 with Margaret on fee increase past $35K/mo. |
