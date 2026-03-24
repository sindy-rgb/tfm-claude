# {Client Name} — Client Config

> **NOTE (March 2026):** Core client metadata (status, GM, media buyer, ESP, CPL target, risk level, sentiment) has migrated to **YAML frontmatter** in each client's intelligence file (`clients/[slug]/[slug].md`). This config template remains relevant for **extended variables** needed by `/skills` commands (Meta account IDs, campaign IDs, budget details, creative naming, UTM formats) that do not fit in frontmatter. For new clients, populate the frontmatter first, then fill in this config for skill-command variables as needed.

<!-- This config file provides all variables referenced by /skills commands. -->
<!-- Fill in every field. Use "N/A" for fields that don't apply to this client. -->
<!-- Fields marked [REQUIRED] must be populated for core commands to work. -->
<!-- Fields marked [OPTIONAL] enable additional sections when populated. -->

---

## Identity

<!-- How this client is referenced across all systems -->
| Field | Value |
|-------|-------|
| `client_name` [REQUIRED] | <!-- Slug used in file paths, Slack channels, etc. e.g., "marketbeat" --> |
| `client_display_name` [REQUIRED] | <!-- Human-readable name for reports and messages. e.g., "MarketBeat" --> |
| `client_intel_path` [REQUIRED] | <!-- Absolute path to client intelligence .md file --> |

---

## Team

<!-- TFM team members assigned to this client -->
| Field | Value |
|-------|-------|
| `gm_name` [REQUIRED] | <!-- Growth Manager assigned. e.g., "Luiz Pekelman" --> |
| `media_buyer_name` [REQUIRED] | <!-- Media Buyer assigned. e.g., "Rabii Elhaouat" --> |

---

## Client Contacts

<!-- Key stakeholders on the client side. Used by /bi-weekly and /prep commands. -->
<!-- Format: Name — Role — Email -->
| `contacts` [REQUIRED] | |
|------------------------|---|
| Primary | <!-- e.g., "Matt Paulson — Founder — matt@marketbeat.com" --> |
| Secondary | <!-- e.g., "Maureen Ohm — Stakeholder — maureen@marketbeat.com" --> |
| Additional | <!-- Add more rows as needed, or "N/A" --> |

---

## Meta Ads

<!-- Pipeboard MCP connection details for pulling ad performance data -->
| Field | Value |
|-------|-------|
| `meta_account_id` [REQUIRED] | <!-- Ad account ID. e.g., "act_1129788478833121" --> |
| `campaign_ids` [REQUIRED] | <!-- Comma-separated campaign IDs managed by TFM. e.g., "120215130153550417" --> |
| `tfm_campaign_ids` [REQUIRED] | <!-- Same as campaign_ids — used in /competitive to distinguish from competitor --> |
| `competitor_name` [OPTIONAL] | <!-- Name of competing agency in same account. e.g., "GrowJoy" --> |
| `competitor_campaign_ids` [OPTIONAL] | <!-- Competitor's campaign IDs in same account. e.g., "120214387815550417, 120216169907550417" --> |
| `ad_account_type` | <!-- "partner" (client owns account, TFM has access) or "owned" (TFM owns account) --> |

---

## KPIs & Targets

<!-- Performance targets used by /friday, /status, /prep, /sindy-brief -->
| Field | Value |
|-------|-------|
| `kpi_primary` [REQUIRED] | <!-- The north star metric name. e.g., "ROAS" or "CPL" or "Subscriber Growth" --> |
| `kpi_target` [REQUIRED] | <!-- Target value for the primary KPI. e.g., "45%" or "$5.00" or "5,000/month" --> |
| `cpl_target` [REQUIRED] | <!-- Target cost per lead. e.g., "$14.00" --> |
| `kpi_secondary` [OPTIONAL] | <!-- Secondary metric name. e.g., "SMS Opt-ins" --> |
| `kpi_secondary_target` [OPTIONAL] | <!-- Target for secondary KPI. e.g., "500/week" --> |
| `quality_definition` | <!-- What makes a good lead for this client. e.g., "Opens 3+ emails in first 14 days" --> |

---

## Quality Data Join

<!-- MANDATORY for skills that rank ads or report CPL. If kpi_primary is anything other than -->
<!-- raw "CPL", this section MUST be filled in. Skills (/friday, /fatigue-scan, /portfolio-pulse) -->
<!-- will REFUSE to output ad rankings without this data or will flag reports as "Raw CPL only". -->
<!-- This section tells skills WHERE to get quality data and HOW to join it to Meta spend data. -->

| Field | Value |
|-------|-------|
| `quality_metric` [REQUIRED if kpi_primary ≠ CPL] | <!-- The client's primary quality KPI. e.g., "Qualified CPL", "V-CAC", "ROAS", "MAR >4", "Cost Per Trial", "CAC". Use "N/A" if raw CPL is the real KPI. --> |
| `quality_data_source` [REQUIRED if kpi_primary ≠ CPL] | <!-- Where quality data lives. e.g., "Sailthru verification rates via n8n", "beehiiv engagement (MAR >4)", "n8n daily ROAS report to Slack", "GHL pipeline data", "partner cohort dashboard" --> |
| `quality_join_key` [REQUIRED if kpi_primary ≠ CPL] | <!-- How to join Meta ad data to quality data. e.g., "utm_campaign maps to DCT name in ad_name", "RegistrationCode param maps to DCT number", "ad_name contains DCT number that matches ROAS report rows" --> |
| `raw_cpl_acceptable` [REQUIRED] | <!-- "true" if raw CPL alone is sufficient for this client (no quality overlay needed). "false" if quality join is mandatory before any ad ranking or CPL reporting. --> |
| `quality_data_freshness` [OPTIONAL] | <!-- How often quality data updates. e.g., "daily via n8n", "weekly partner report", "6-week cohort lag". Skills use this to know if quality data might be stale. --> |
| `quality_fallback_note` [OPTIONAL] | <!-- What to say when quality data is unavailable. e.g., "Use vault ROAS data from last bi-weekly report", "Escalate to Luiz — ROAS data is critical for this client" --> |

---

## Budget

<!-- Monthly budget and pacing targets -->
| Field | Value |
|-------|-------|
| `monthly_budget` [REQUIRED] | <!-- Total monthly ad spend. e.g., "$30,000" --> |
| `budget_pacing_target` [REQUIRED] | <!-- Daily spend target for pacing. e.g., "$1,000/day" --> |
| `budget_notes` [OPTIONAL] | <!-- Any context on budget flexibility. e.g., "Will double to $60K if ROAS matches GrowJoy" --> |

---

## ESP (Email Service Provider)

<!-- Used by /friday for subscriber and engagement data -->
| Field | Value |
|-------|-------|
| `esp` [REQUIRED] | <!-- ESP platform name. e.g., "beehiiv", "Mailchimp", "ActiveCampaign", "Custom" --> |
| `esp_api_access` | <!-- "true" if we can pull data programmatically, "false" if manual only --> |
| `esp_dashboard_url` [OPTIONAL] | <!-- Direct link to ESP dashboard for this client --> |
| `esp_metrics` [OPTIONAL] | <!-- Which ESP metrics to include in reports. e.g., "open_rate, click_rate, new_subs, total_subs" --> |

---

## Partner Dashboard

<!-- Some clients have their own reporting dashboards with downstream metrics (revenue, ROAS, SMS) -->
| Field | Value |
|-------|-------|
| `partner_dashboard_url` [OPTIONAL] | <!-- URL to client's internal dashboard. e.g., "N/A" or a URL --> |
| `partner_dashboard_metrics` [OPTIONAL] | <!-- Metrics available on dashboard. e.g., "Revenue, Rev/User, Confirmed Sales, SMS Opt-ins, Co-Reg Leads" --> |
| `partner_data_source` [OPTIONAL] | <!-- How we get this data. e.g., "n8n daily ROAS report", "Slack bot", "manual pull" --> |

---

## Reporting

<!-- Report format and delivery preferences -->
| Field | Value |
|-------|-------|
| `report_format` [REQUIRED] | <!-- "default" for standard TFM format, or describe custom format --> |
| `report_destination` [REQUIRED] | <!-- Where Friday reports go. e.g., "Notion" or "Slack #thefeed-marketbeat" --> |
| `report_cadence` | <!-- "weekly" (Friday reports) + "bi-weekly" (client calls) is default --> |

---

## Communication Channels

<!-- Slack channels and Day.ai identifiers -->
| Field | Value |
|-------|-------|
| `slack_internal` [REQUIRED] | <!-- Internal TFM channel. e.g., "#internal-marketbeat" --> |
| `slack_external` [OPTIONAL] | <!-- Shared channel with client. e.g., "#thefeed-marketbeat" --> |
| `day_ai_search_term` [REQUIRED] | <!-- How to find this client in Day.ai. e.g., "MarketBeat" or "Matt Paulson" --> |
| `notion_page_url` [OPTIONAL] | <!-- Notion client OS page URL --> |

---

## Creative

<!-- Naming conventions and creative context for /creative-brief -->
| Field | Value |
|-------|-------|
| `dct_naming_prefix` [REQUIRED] | <!-- DCT naming prefix. e.g., "DCT_" --> |
| `next_dct_number` [REQUIRED] | <!-- Next available DCT number. e.g., "152" (update after each /creative-brief) --> |
| `brand_voice_tone` | <!-- Tone aspiration from intel file. e.g., "Authority-driven, data-backed, actionable" --> |
| `never_rules` | <!-- Pipe-separated NEVER rules. e.g., "Never use MarketBeat in ad creative | Never make stock predictions | Never use FOMO on specific stocks" --> |
| `approved_language` [OPTIONAL] | <!-- Key approved phrases/terms. e.g., "Smart money, edge, free report" --> |
| `audience_segments` [OPTIONAL] | <!-- ICP names. e.g., "Frank (60-70, conservative investor) | Brian (35-45, growth investor)" --> |
| `landing_page_urls` [REQUIRED] | <!-- Active landing pages, comma-separated --> |

---

## UTM / Tracking

<!-- Attribution setup for this client -->
| Field | Value |
|-------|-------|
| `utm_format` | <!-- Standard TFM UTMs or custom. e.g., "standard" or "RegistrationCode=meta-thefeedmedia-dctXXX" --> |
| `tracking_notes` [OPTIONAL] | <!-- Any tracking quirks. e.g., "Uses RegistrationCode instead of UTMs" --> |

---

## Relationship Context

<!-- Pulled from intel file, cached here for quick reference -->
| Field | Value |
|-------|-------|
| `relationship_health` | <!-- "Improving", "Stable", "At Risk", "Prove-It Phase" --> |
| `sync_cadence` | <!-- "Bi-weekly", "Weekly", "Monthly" --> |
| `biggest_risk` [OPTIONAL] | <!-- One-line summary of the biggest continuity risk --> |

---
---

# EXAMPLE: MarketBeat (Filled In)

Below is a completed config for reference. Delete this section when creating a new client config.

---

## Identity

| Field | Value |
|-------|-------|
| `client_name` | marketbeat |
| `client_display_name` | MarketBeat |
| `client_intel_path` | /Users/jay/Documents/the-feed-media/clients/marketbeat/marketbeat.md |

## Team

| Field | Value |
|-------|-------|
| `gm_name` | Luiz Pekelman |
| `media_buyer_name` | Rabii Elhaouat |

## Client Contacts

| `contacts` | |
|------------|---|
| Primary | Matt Paulson — Founder — matt@marketbeat.com |
| Secondary | Maureen Ohm — Stakeholder — maureen@marketbeat.com |

## Meta Ads

| Field | Value |
|-------|-------|
| `meta_account_id` | act_1129788478833121 |
| `campaign_ids` | 120234644644600565 |
| `tfm_campaign_ids` | 120234644644600565 |
| `competitor_name` | GrowJoy |
| `competitor_campaign_ids` | 120226438970390565, 120242548982060565 |
| `ad_account_type` | partner |

## KPIs & Targets

| Field | Value |
|-------|-------|
| `kpi_primary` | ROAS |
| `kpi_target` | 45% (match GrowJoy) |
| `cpl_target` | $14.00 (ideal under $10) |
| `kpi_secondary` | SMS Opt-ins |
| `kpi_secondary_target` | Close gap with GrowJoy (currently 7x behind) |
| `quality_definition` | Revenue-generating subscriber — measured by Rev/User and confirmed sales |

## Quality Data Join

| Field | Value |
|-------|-------|
| `quality_metric` | ROAS |
| `quality_data_source` | n8n daily ROAS report (posted to #internal-marketbeat) + Matt's partner dashboard |
| `quality_join_key` | RegistrationCode param maps to DCT number in ROAS report rows |
| `raw_cpl_acceptable` | false |
| `quality_data_freshness` | Daily via n8n automated report |
| `quality_fallback_note` | Use vault ROAS data from last bi-weekly report. Escalate to Luiz if >1 week stale. |

## Budget

| Field | Value |
|-------|-------|
| `monthly_budget` | $30,000 |
| `budget_pacing_target` | $1,000/day |
| `budget_notes` | Matt will double to $60K/month if TFM matches GrowJoy ROAS |

## ESP

| Field | Value |
|-------|-------|
| `esp` | Custom (MarketBeat internal) |
| `esp_api_access` | false |
| `esp_dashboard_url` | N/A |
| `esp_metrics` | N/A — subscriber data tracked via partner dashboard |

## Partner Dashboard

| Field | Value |
|-------|-------|
| `partner_dashboard_url` | Delivered via n8n daily ROAS report to Slack |
| `partner_dashboard_metrics` | Revenue, Rev/User, Confirmed Sales, SMS Opt-ins, Co-Reg Leads, Revenue Leads |
| `partner_data_source` | n8n daily ROAS report (posted to #internal-marketbeat) |

## Reporting

| Field | Value |
|-------|-------|
| `report_format` | default + include ROAS comparison vs GrowJoy |
| `report_destination` | Notion |
| `report_cadence` | weekly (Friday) + bi-weekly (client calls) |

## Communication Channels

| Field | Value |
|-------|-------|
| `slack_internal` | #internal-marketbeat |
| `slack_external` | #thefeed-marketbeat |
| `day_ai_search_term` | MarketBeat |
| `notion_page_url` | [MarketBeat Client OS page] |

## Creative

| Field | Value |
|-------|-------|
| `dct_naming_prefix` | DCT_ |
| `next_dct_number` | 152 |
| `brand_voice_tone` | Authority-driven, data-backed, actionable. "Smart money" positioning. |
| `never_rules` | Never use "MarketBeat" in ad creative | Never make specific stock price predictions | Never use FOMO on specific stocks | Never conflate free newsletter with premium subscription |
| `approved_language` | Smart money, edge, free report, $29.97 report yours free today |
| `audience_segments` | Frank (60-70, conservative, near retirement, protecting wealth) | Brian (35-45, aggressive investor, growth stocks) |
| `landing_page_urls` | earlybirdpublishing.com/users/PDFoffer.aspx?offer=spacestocks&RegistrationCode=meta-thefeedmedia-dct199, earlybirdpublishing.com/users/PDFoffer.aspx?offer=top5, earlybirdpublishing.com/users/PDFoffer.aspx?offer=newyear |

## UTM / Tracking

| Field | Value |
|-------|-------|
| `utm_format` | RegistrationCode=meta-thefeedmedia-dctXXX |
| `tracking_notes` | Uses RegistrationCode parameter instead of standard UTMs. Original MarketBeat ad account was banned; ads run under Early Bird Publishing. |

## Relationship Context

| Field | Value |
|-------|-------|
| `relationship_health` | Neutral — Prove-It Phase |
| `sync_cadence` | Bi-weekly |
| `biggest_risk` | ROAS gap vs GrowJoy is the existential risk. Budget allocation is purely mathematical — no relationship cushion. |
