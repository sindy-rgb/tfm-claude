# Claude Project Onboarding Flow

Use these prompts in order when you first get access to a client project. Each one tests a different part of the setup and teaches you how to use it.

---

## Prompt 1 — Verify Your Context

> **"Summarize everything you know about this client from your project instructions. Include: client name, primary contact, ESP, North Star metric and target, and current relationship health."**

**What this checks:** Confirms the context file loaded correctly and the core client data is accurate.
**What to QA:** Compare every detail against what you know. Flag anything outdated or wrong back to Jay.

---

## Prompt 2 — Brand Voice Guardrails

> **"What are the NEVER rules for this client's copy? Give me 3 example headlines that would VIOLATE these rules and explain why each one breaks a rule."**

**What this checks:** Tests that brand voice constraints are in the context and Claude actually follows them.
**What to QA:** Make sure the NEVER rules match reality. If Claude can't list any, the context file is missing Section 3.

---

## Prompt 3 — Creative Strategy Recall

> **"What are this client's top-performing ad formats and creative signals? If I needed to brief a designer on a new concept, what would you tell them based on past winners?"**

**What this checks:** Section 4 (Winning Creative Signals) is populated with real performance data.
**What to QA:** Confirm the winning formats match what's actually running. If it's vague or generic, the context file needs more specifics.

---

## Prompt 4 — Negative Triggers & Landmines

> **"What topics, phrases, or approaches should I absolutely avoid with this client? Include any direct quotes from the client if available."**

**What this checks:** Section 5 (Negative Triggers) is loaded and has real client quotes.
**What to QA:** If Claude gives generic answers instead of client-specific ones, the context file needs enrichment.

---

## Prompt 5 — Test the CRM (Day.ai)

> **"Search Day.ai for this client's organization record. Pull up their most recent meeting recording and summarize the key takeaways."**

**What this checks:** Day.ai MCP connector is working. You can search orgs, pull meetings, and read summaries.
**What to QA:** Confirm the meeting summary matches what actually happened. Note if any meetings are missing.

**Available Day.ai functions:**
- `search_objects` — Find contacts, orgs, opportunities, meetings, tasks, emails, calendar events
- `read_crm_schema` — See all available fields for any object type
- `get_meeting_recording_context` — Pull full meeting context, transcript, summary
- `create_or_update_person_organization` — Add/update contacts and companies
- `create_or_update_action` — Create tasks and follow-ups
- `create_page` / `update_page` — Create and edit notes/documents
- `create_or_update_relationship` — Link objects together (person to org, opp to org, etc.)
- `get_share_url` — Get a shareable link to any CRM object
- `create_or_update_workspace_context` — Update workspace-level context notes
- `assistant_settings` — View/update AI assistant configuration

---

## Prompt 6 — Test Slack

> **"Search Slack for the internal channel for this client. Pull the 10 most recent messages and summarize what the team has been discussing."**

**What this checks:** Slack MCP connector is working and you have access to the right channels.
**What to QA:** Confirm the channel exists and messages are pulling correctly.

**Available Slack functions:**
- `slack_search_channels` — Find channels by name
- `slack_read_channel` — Read messages from a channel
- `slack_read_thread` — Read a specific thread
- `slack_search_public` — Search public channel messages by keyword
- `slack_search_public_and_private` — Search all messages
- `slack_search_users` — Find users
- `slack_read_user_profile` — Get user details
- `slack_send_message` / `slack_send_message_draft` — Send or draft messages
- `slack_schedule_message` — Schedule a message for later
- `slack_create_canvas` / `slack_read_canvas` / `slack_update_canvas` — Work with Slack canvases

---

## Prompt 7 — Test Notion

> **"Find this client's page in Notion. List all the ad concepts currently tracked and their status."**

**What this checks:** Notion MCP connector works and client pages are accessible.
**What to QA:** Confirm the concepts listed match what's actually in Notion.

**Available Notion functions:**
- `notion-search` — Search pages and databases by title
- `notion-fetch` — Read a specific page or database by URL/ID
- `notion-create-pages` — Create new pages in a database
- `notion-update-page` — Update page properties
- `notion-create-database` — Create a new database
- `notion-create-view` / `notion-update-view` — Manage database views
- `notion-get-comments` / `notion-create-comment` — Read and add comments
- `notion-duplicate-page` — Duplicate an existing page
- `notion-move-pages` — Move pages between parents
- `notion-get-users` / `notion-get-teams` — List workspace users and teams

---

## Prompt 8 — Test Meta Ads

> **"Pull the active campaigns for this client from Meta Ads. What's the current daily spend, CPL, and how many ad sets are running?"**

**What this checks:** Pipeboard Meta Ads MCP connector is working and pulling live data.
**What to QA:** Compare numbers against Ads Manager. Flag any discrepancies.

**Available Meta Ads functions (key ones):**
- `get_campaigns` / `get_campaign_details` — List and inspect campaigns
- `get_adsets` / `get_adset_details` — List and inspect ad sets
- `get_ads` / `get_ad_details` — List and inspect individual ads
- `get_ad_creatives` / `get_creative_details` — View creative assets
- `get_insights` / `bulk_get_insights` — Pull performance data (spend, CPL, CTR, etc.)
- `create_campaign` / `create_adset` / `create_ad` — Build new campaigns
- `update_campaign` / `update_adset` / `update_ad` — Modify existing items
- `get_custom_audiences` — View exclusion/lookalike audiences
- `search_interests` / `search_geo_locations` — Targeting research
- `upload_ad_image` / `upload_ad_video` — Upload creative assets
- `get_account_pages` / `get_instagram_accounts` — View connected pages

---

## Prompt 9 — Test Gmail & Calendar

> **"Check my calendar for any upcoming meetings with this client. Also search Gmail for the most recent email thread with them."**

**What this checks:** Google Calendar and Gmail MCP connectors are working.
**What to QA:** Confirm meetings and emails are showing up correctly.

**Available Google Calendar functions:**
- `gcal_list_events` — List upcoming events
- `gcal_get_event` — Get event details
- `gcal_create_event` — Schedule a new event
- `gcal_update_event` / `gcal_delete_event` — Modify or cancel events
- `gcal_find_meeting_times` — Find availability across attendees
- `gcal_find_my_free_time` — Check your open slots
- `gcal_respond_to_event` — Accept/decline invitations
- `gcal_list_calendars` — See all connected calendars

**Available Gmail functions:**
- `gmail_search_messages` — Search emails by query
- `gmail_read_message` — Read a specific email
- `gmail_read_thread` — Read a full email thread
- `gmail_create_draft` — Draft a new email
- `gmail_list_drafts` — View existing drafts
- `gmail_list_labels` — See all labels/folders
- `gmail_get_profile` — View account info

---

## Prompt 10 — End-to-End Workflow Test

> **"I need to prep for this client's next call. Pull their most recent Meta Ads performance (last 7 days), check Day.ai for the last meeting notes, search Slack for any recent flags from the team, and draft a 5-bullet status update I could paste into the external Slack channel."**

**What this checks:** Everything working together. Claude should pull from multiple connectors, synthesize the data, and produce something useful.
**What to QA:** Read the output critically. Is the data accurate? Is the tone right for the client? Would you actually send this?

---

## After Completing All 10

Report back to Jay with:
1. Which prompts worked perfectly
2. Which ones returned incomplete or incorrect data
3. Any context file updates needed (missing info, outdated details, wrong metrics)
4. Any connectors that failed or returned errors

This helps us keep the client intelligence files accurate and the integrations healthy.
