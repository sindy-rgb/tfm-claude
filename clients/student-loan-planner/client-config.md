# Student Loan Planner — Client Config
<!-- Last updated: March 21, 2026 -->
<!-- Skills reference: /system/skills.md -->

---

## Identity

| Field | Value |
|-------|-------|
| `client_name` | student-loan-planner |
| `client_display_name` | Student Loan Planner (SLP) |
| `client_intel_path` | /Users/jay/Documents/the-feed-media/clients/student-loan-planner/student-loan-planner.md |

---

## Team

| Field | Value |
|-------|-------|
| `gm_name` | Aubree Clark |
| `media_buyer_name` | Rabii Elhaouat |

---

## Client Contacts

| `contacts` | |
|------------|---|
| Primary | Travis Hornsby — Founder/CEO — travis@studentloanplanner.com |
| Secondary | John Lee — Analytics — john@studentloanplanner.com |
| Secondary | Jeffrey Trull — Zapier/Kit/LP/Creative Approvals — jeffreytrull1@gmail.com |

---

## Meta Ads

| Field | Value |
|-------|-------|
| `meta_account_id` | Not in Pipeboard DB (account under client's Business Manager with partner access) |
| `campaign_ids` | Multiple ICP-specific CBO campaigns (Physicians, Dentists, Veterinarians, Lawyers, Nursing, Chiropractors, PAs, Optometrists, Pharmacists, PTs, Psychologists) |
| `tfm_campaign_ids` | TBD |
| `competitor_name` | N/A |
| `competitor_campaign_ids` | N/A |
| `ad_account_type` | Partner access (client-owned Business Manager) |

---

## KPIs & Targets

| Field | Value |
|-------|-------|
| `kpi_primary` | Cost Per Lead (CPL) — per ICP segment |
| `kpi_target` | Physicians/Dentists: < $20 | Veterinarians: < $15 | Lawyers/Nursing/Chiro/PAs: < $15 |
| `cpl_target` | $15-20 blended (current: $18.82) |
| `kpi_secondary` | CVR (Landing Page) |
| `kpi_secondary_target` | > 15% (current: 11.64% — critical bottleneck) |
| `quality_definition` | High-income professionals with six-figure student loan debt. Subscriber value tiers: Physicians/Dentists $50-100/sub, Veterinarians $30-50/sub, Lawyers/Pharmacists/Chiro/PAs $20-40/sub. |

---

## Budget

| Field | Value |
|-------|-------|
| `monthly_budget` | ~$18,000 (down from ~$34K in Jan) |
| `budget_pacing_target` | ~$610/day (March 2026) |
| `budget_notes` | Spend declining MoM: Jan $34K -> Feb $27K -> Mar ~$18K projected. Budget allocated per ICP with Physicians/Dentists at $200/day each, smaller ICPs at $40-50/day. Private student loan campaign planned mid-March with $10-30/day per ICP. |

---

## ESP

| Field | Value |
|-------|-------|
| `esp` | Kit (ConvertKit) |
| `esp_api_access` | TBD |
| `esp_dashboard_url` | N/A |
| `esp_metrics` | subscriber_count, segment_performance |

---

## Partner Dashboard

| Field | Value |
|-------|-------|
| `partner_dashboard_url` | N/A |
| `partner_dashboard_metrics` | N/A |
| `partner_data_source` | Google Analytics + custom conversion events per ICP. Travis maintains paid leads list manually tracking backend conversion values. |

---

## Reporting

| Field | Value |
|-------|-------|
| `report_format` | Per-ICP breakdown: CPL, leads, spend, CTR, CVR. Must include profession-specific performance. Weekly in Google Sheets + Slack. |
| `report_destination` | Slack #thefeed-slp + Google Sheets |
| `report_cadence` | weekly (Friday) + bi-weekly (client calls, Mondays) |
| `report_owner` | Aubree Clark |

---

## Communication Channels

| Field | Value |
|-------|-------|
| `slack_internal` | #internal-slp |
| `slack_external` | #thefeed-slp |
| `day_ai_search_term` | Student Loan Planner |
| `notion_page_url` | https://www.notion.so/25df4a126e0680858dd4dfdaca8c16cb |

---

## Creative

| Field | Value |
|-------|-------|
| `dct_naming_prefix` | DCT |
| `next_dct_number` | 129 |
| `brand_voice_tone` | Conversational, profession-specific. Pain -> Relief -> Empowerment arc. Positions SLP as the trusted expert simplifying chaos. Creates clarity during chaos — not by increasing fear. |
| `never_rules` | NEVER overpromise guaranteed loan forgiveness — regulated financial space | NEVER use financial fearmongering or overtly negative tone | NEVER reference political opinions or partisan positions on student loan policy | NEVER use generic "debt help" language — always profession-specific | NEVER position SLP as a lender or servicer — they are educational/consulting | NEVER conflate SLP with government programs |
| `approved_language` | free weekly newsletter, trusted by professionals with six-figure student loan debt, student loan strategies in 5 minutes, shows you exactly what to do next, made for high-debt high-income professionals |
| `audience_segments` | Physicians (Tier 1) | Dentists (Tier 1) | Veterinarians (Tier 2) | Lawyers/Pharmacists/Optometrists/Chiropractors/PAs/Psychologists (Tier 3) |
| `landing_page_urls` | Custom profession-specific ConvertKit pages (11 ICPs) |

---

## UTM / Tracking

| Field | Value |
|-------|-------|
| `utm_format` | standard (utm_source=facebookads&utm_medium={{adset.name}}&utm_campaign={{ad.name}}) |
| `tracking_notes` | Each ICP has its own CBO campaign with unique custom conversion event, landing page, and UTMs. Tracking/attribution gap is a known issue — GA event values and refinance click tracking too weak to show true value. Travis has flagged this repeatedly. |

---

## Relationship Context

| Field | Value |
|-------|-------|
| `relationship_health` | Cautiously Optimistic, Under Pressure |
| `sync_cadence` | Bi-weekly (Mondays) |
| `biggest_risk` | CPL deteriorating MoM (Jan $11.79 -> Feb $15.39 -> Mar $18.82). CVR dropping (11.64% from ~17% in Feb). Spend declining. Tracking/attribution gap prevents demonstrating true subscriber value. Private student loan campaign infrastructure not fully ready. Sensitive financial category adds regulatory complexity. |
