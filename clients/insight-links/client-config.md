# Insight Links — Client Config
<!-- Last updated: March 11, 2026 -->
<!-- Skills reference: /system/skills.md -->

---

## Identity

| Field | Value |
|-------|-------|
| `client_name` | insight-links |
| `client_display_name` | Insight Links |
| `client_intel_path` | clients/insight-links/insight-links.md |

---

## Team

| Field | Value |
|-------|-------|
| `gm_name` | Lays Paiva |
| `media_buyer_name` | Rabii Elhaouat |

---

## Client Contacts

| `contacts` | |
|------------|---|
| Primary | Jake Fishman — CEO — jfishman@insight-links.com |
| Secondary | Jason Barry — Partner & Editor (DHW) — jbarry@insight-links.com |

---

## Meta Ads

| Field | Value |
|-------|-------|
| `meta_account_id` | act_507049163040180 |
| `campaign_ids` | 120237192634290138, 120237192451030138, 120237192398350138 |
| `tfm_campaign_ids` | 120237192634290138, 120237192451030138, 120237192398350138 |
| `competitor_name` | Growletter |
| `competitor_campaign_ids` | 120204938994780138, 120204938908950138, 120204938700260138 |
| `ad_account_type` | partner |

### Campaign Name Reference
<!-- For report generation — maps campaign IDs to newsletter names -->
| Campaign ID | Newsletter |
|---|---|
| 120237192634290138 | TFM - IMAGING WIRE - LEAD |
| 120237192451030138 | TFM - CARDIAC WIRE - LEAD |
| 120237192398350138 | TFM - DIGITALHEALTH - LEAD |
| 120204938994780138 | GL - CW Newsletter - Re-Launch |
| 120204938908950138 | GL - DHW Newsletter - Re-Launch |
| 120204938700260138 | GL - TIW Newsletter - Re-Launch |

---

## KPIs & Targets

| Field | Value |
|-------|-------|
| `kpi_primary` | Qualified CPL |
| `kpi_target` | < $20 per qualified lead |
| `cpl_target` | < $5.00 raw CPL (varies by newsletter — DHW ~$3.34, CW ~$1.94, IW ~$3.17) |
| `kpi_secondary` | Qualification Rate |
| `kpi_secondary_target` | > 20% across all three newsletters |
| `quality_definition` | Submits first-party data (name, role, company) via post-subscribe form AND holds a relevant professional role in the newsletter's target specialty. Non-qualified: retired, disabled, patients, students, non-industry roles. |

---

## Budget

| Field | Value |
|-------|-------|
| `monthly_budget` | ~$8,000 (~$2,000/week) |
| `budget_pacing_target` | ~$260/day total (~$80-100/day per newsletter) |
| `budget_notes` | Split across 3 newsletters. Jake is open to increasing if qualified CPL stays under $20. |

---

## ESP

| Field | Value |
|-------|-------|
| `esp` | Mailchimp |
| `esp_api_access` | false (n8n workflow planned but not yet operational) |
| `esp_dashboard_url` | N/A — manual export from Mailchimp |
| `esp_metrics` | open_rate, click_rate, new_subs, qualified_leads, qualification_rate |

---

## Partner Dashboard

| Field | Value |
|-------|-------|
| `partner_dashboard_url` | N/A |
| `partner_dashboard_metrics` | N/A |
| `partner_data_source` | Mailchimp manual export — qualified lead counts analyzed in Mailchimp + Excel by Jake. n8n automation for Mailchimp data ingestion is planned but NOT yet operational. |

---

## Reporting

| Field | Value |
|-------|-------|
| `report_format` | Per-newsletter breakdown (DHW, CW, IW). Each newsletter gets: Spend (WoW%), Website Leads (WoW%), CPL (WoW%), Unique Outbound CTR (WoW%), CVR (WoW%), CPM (WoW%), Qualified Leads (WoW%). Then: Top Performing Creatives per newsletter (leads, CPL, CTR, qualified count + fb.me preview links). Then: Insights (4-5 bullets). Then: Next Steps (3-4 action items). MUST include qualified lead data — raw CPL alone is unacceptable for this client. See #thefeed-insightlinks history for exact format. |
| `report_destination` | Slack #thefeed-insightlinks (client-facing) |
| `report_cadence` | weekly (Friday) + bi-weekly (client calls, Tuesdays 10am EST, odd weeks) |
| `report_owner` | Lays |

---

## Communication Channels

| Field | Value |
|-------|-------|
| `slack_internal` | #internal-insightlinks (C0A42KZ2LQJ) |
| `slack_external` | #thefeed-insightlinks (C0A3Z3J0NQ6) |
| `day_ai_search_term` | Insight Links |
| `notion_page_url` | https://www.notion.so/readthefeed/Insight-Links-2cbf4a126e06804cba20e55029523003 |

---

## Creative

| Field | Value |
|-------|-------|
| `dct_naming_prefix` | DCT_ |
| `next_dct_number` | 123 |
| `brand_voice_tone` | Professional but accessible. Time-saving framing ("stay current," "filter the noise"). Authority positioning ("curated," "what actually matters"). Peer-to-peer confession style. Text-heavy ads outperform visual creative for this B2B healthcare audience. |
| `never_rules` | Never use overly casual or consumer-grade language — audience is MDs, PhDs, executives | Never make clinical claims or promise patient outcomes | Never use clickbait-style hooks that resemble spam or hospital blast emails | Never use AI-generated sounding copy — Jake wants natural human voice | Never target or speak to patients, retired professionals, or students | Never report raw CPL without qualified CPL — Jake does not trust raw CPL alone | Never let Imaging Wire stagnate without visible action — IW = 65% of revenue, stale IW is what killed Growletter's relationship |
| `approved_language` | stay current, filter the noise, caught up fast, smarter while saving time, curated, context for smarter decisions, what actually matters, easy and accessible |
| `audience_segments` | Cardiologists & cardiac specialists (CW) | Radiologists & imaging professionals (IW) | Digital health executives & health tech leaders (DHW) |
| `landing_page_urls` | cardiacwire.com/subscribe-feed, theimagingwire.com/subscribe-feed, digitalhealthwire.com/subscribe-feed |

---

## UTM / Tracking

| Field | Value |
|-------|-------|
| `utm_format` | standard (utm_source=facebookads&utm_medium={{adset.name}}&utm_campaign={{ad.name}}) |
| `tracking_notes` | Qualified lead tracking depends on Mailchimp post-subscribe form data + manual Excel analysis by Jake. n8n Mailchimp workflow is planned to automate this but not yet live. Currently qualified lead counts come from Jake's manual reports shared in Slack or bi-weekly calls. |

---

## Relationship Context

| Field | Value |
|-------|-------|
| `relationship_health` | Positive and Improving — but Prove-It Phase (bake-off vs Growletter) |
| `sync_cadence` | Bi-weekly (Tuesdays 10am EST, odd weeks) |
| `biggest_risk` | This is a bake-off account. TFM runs alongside Growletter. Jake evaluates at 60-90 days (~March-April 2026). Imaging Wire is make-or-break — if TFM proves qualified CPL advantage on IW, account is locked in. Reporting without qualified lead data would signal we don't understand his business. |

---

## n8n Automation Status

| Field | Value |
|-------|-------|
| `n8n_status` | IN PROGRESS — Claude Chat is finishing the n8n node setup |
| `n8n_planned_workflow` | Mailchimp → n8n → Google Spreadsheet (incremental updates) → auto-pull into reports |
| `n8n_data_destination` | Google Spreadsheet (updates incrementally as new data comes in) |
| `n8n_blocker` | Node setup actively being completed. Once live, /friday and /bi-weekly should pull qualified lead data from the spreadsheet automatically instead of relying on Jake's manual exports. |
| `n8n_priority` | HIGH — this is the last piece needed to make /friday fully self-sufficient. |
