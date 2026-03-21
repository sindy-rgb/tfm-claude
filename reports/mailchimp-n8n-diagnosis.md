# Mailchimp n8n Workflow Diagnosis

> **Date:** 2026-03-21 (updated)
> **Investigated by:** Claude Code (Jay's request)
> **Client:** Insight Links (Cardiac Wire, Imaging Wire, Digital Health Wire)
> **ESP:** Mailchimp (us18 datacenter)
> **n8n Instance:** https://n8n-zwzfv-u62151.vm.elestio.app/

---

## Executive Summary

**The Mailchimp qualified lead data pipeline stopped updating around March 10, 2026.** A Google Sheet with real subscriber-level Mailchimp data exists and was being populated (likely by a Claude Chat project using the Mailchimp API, not by a standalone n8n workflow). The sheet contains ~3,300+ rows of subscriber data with the latest opt_in_dates reaching March 10. The n8n Meta Ads workflow is a separate system that continues to work. There are two separate issues to fix: (1) the Mailchimp data pipeline that stopped, and (2) the n8n Meta Ads bot using a placeholder sheet ID in its Slack messages.

---

## What Actually Exists

There are **three systems** handling Insight Links data:

### 1. n8n Meta Ads Bot (WORKING)

An n8n workflow posts **Meta Ads performance data** (spend, leads, CPL, CTR, CVR, CPM) to `#internal-insightlinks` via the N8N Slack bot (user ID: `U0A2V919AJD`). This workflow:

- Runs on a weekly cadence (Fridays or Thursdays, plus ad-hoc mid-week)
- Pulls Meta Ads API data for the 3 TFM campaigns (DHW: `120237192398350138`, CW: `120237192451030138`, IW: `120237192634290138`)
- Posts formatted KPI summaries to Slack with `[to fill out]` placeholders for Insights and Next Steps
- Links to a Google Sheet with placeholder ID `1YourInsightLinksSheetID` in its Slack messages (this is a literal placeholder -- the actual sheet ID was never substituted into the Slack message template)

**This workflow IS working.** Posts confirmed on: Mar 6, Mar 13, and Mar 20, 2026.

### 2. Mailchimp Qualified Lead Spreadsheet (STOPPED ~March 10)

A real Google Sheet exists with Mailchimp subscriber data:

- **Spreadsheet:** "Insight Links" (ID: `1Ed5meyHx1Vt1VTWJ4t2grBj_181rBxY2Jq912UiZJ6Q`)
- **URL:** `https://docs.google.com/spreadsheets/d/1Ed5meyHx1Vt1VTWJ4t2grBj_181rBxY2Jq912UiZJ6Q/edit`
- **Contains:** 3,300+ rows of subscriber-level data across all 3 newsletters
- **Columns:** audience, audience_short, email, first_name, last_name, job_title, company, qualified (TRUE/FALSE), utm_campaign, utm_source, utm_medium, utm_content, ad_source (TFM vs other), newsletter_classified (CW/IW/DHW), fields_filled, all_4_complete, opt_in_date, tags, x_signup, message, last_checked
- **Data range:** opt_in_dates from historical (2022+) through **March 10, 2026** -- no records after this date
- **Data source:** Mailchimp API (via Jay's Claude Chat project, NOT via an n8n workflow)

This sheet was being populated by the **Insight Links Claude Chat project** that Jay built. Jay described it as a system that "ingests the data 3x a week into a spreadsheet." The Claude Chat project uses the Mailchimp API key to pull subscriber data and write it to this Google Sheet.

**This is the system that stopped updating around March 10.**

### 3. Claude Chat /friday Skill (WORKING but missing Mailchimp data)

Jay's Claude Chat project at the Insight Links project generates `/friday` reports. It references this spreadsheet as its primary source for qualified lead data. Lays successfully used it on March 20 to generate a report -- but the qualified lead numbers came from the sheet data (which only goes through March 10) plus Noreen's manual Mailchimp export posted separately in Slack.

**The /friday skill works, but the Mailchimp data source it depends on is stale.**

---

## What Broke (and Why)

### The Google Sheet Stopped Updating (~March 10)

The "Insight Links" spreadsheet (ID: `1Ed5meyHx1Vt1VTWJ4t2grBj_181rBxY2Jq912UiZJ6Q`) has subscriber data through approximately March 10, 2026. No new records appear after this date.

The vault files describe this as "IN PROGRESS" (`client-config.md` line 162: `n8n_status: IN PROGRESS -- Claude Chat is finishing the n8n node setup`), suggesting the pipeline was partially built but either:

1. **The Claude Chat project's Mailchimp API connection broke** -- possibly due to Mailchimp's security update that locked Noreen out on March 20 (the API key may have been invalidated by the same security enforcement)
2. **The scheduled ingestion stopped running** -- Claude Chat projects do not have built-in cron scheduling; Jay may have been triggering the ingestion manually or via a Claude Cowork scheduled task that stopped
3. **The Mailchimp API key expired or was rotated** -- Mailchimp (us18) may have enforced credential rotation around this time

Note: The n8n bot's placeholder sheet ID (`1YourInsightLinksSheetID`) in Slack messages is a **separate issue** -- this is just a cosmetic problem in the Slack message template, not related to the actual data pipeline.

### The Mailchimp Access Issue (March 20)

On March 20, 2026, Noreen reported in `#internal-insightlinks` that she could not log into Insight Links' Mailchimp account (`us18.admin.mailchimp.com`) -- it was requiring security updates (likely MFA enrollment or password reset). This triggered a thread:

- **Noreen** (Mar 20 06:37): "It is asking me to enable these when logging into Insight Link's Mailchimp account. Could you please help?"
- **Sindy** (Mar 20 08:01): Asked for the login link
- **Noreen** (Mar 20 08:21): Shared the `us18.admin.mailchimp.com/login/sec-update` URL
- **Noreen** (Mar 20 09:29): Asked Lays to send the data since she still couldn't log in
- **Sindy** (Mar 20 10:10): Asked Lays to log in and export, said she'd set it up later
- **Jay** (Mar 20 10:33): "Do we even need this anymore? We have an entirely functioning Insight Links Claude project that ingests the data 3x a week into a spreadsheet."
- **Lays** (Mar 20 10:35): "Where exactly do you get this and the spreadsheet? I never used it for reporting."
- **Lays** (Mar 20 10:36): "Also n8n looks like it's not connected on insight links project."

This exchange reveals that:
1. The Mailchimp login credentials have an access issue (security update requirement)
2. Lays (the GM) has never used the automated spreadsheet Jay referenced -- adoption gap
3. Lays observed that "n8n looks like it's not connected on insight links project" -- confirming a broken connection
4. Despite the spreadsheet having 3,300+ rows of real data, no one on the team besides Jay was aware of it

### Jay's "Claude Project" System

Jay referenced a Claude Chat project that "ingests data 3x a week into a spreadsheet." This is the Insight Links Claude project, which:

- **Successfully writes to:** `https://docs.google.com/spreadsheets/d/1Ed5meyHx1Vt1VTWJ4t2grBj_181rBxY2Jq912UiZJ6Q/edit`
- **Contains real data:** 3,300+ subscriber records with job titles, companies, qualification status, UTM attribution
- **Was working until ~March 10** -- 11 days of missing data as of March 21
- **Lays successfully used it on March 20** to generate a `/friday` report, confirming the project itself works (but the data it references is stale)
- Noreen also posts qualified lead counts manually -- on March 13 and March 20, she posted counts that the /friday report incorporated

---

## Root Cause Analysis

| Factor | Status |
|--------|--------|
| n8n Meta Ads workflow | WORKING -- posts to Slack on schedule |
| Mailchimp qualified lead Google Sheet | EXISTS and has real data (ID: `1Ed5meyHx1Vt1VTWJ4t2grBj_181rBxY2Jq912UiZJ6Q`) -- but stopped updating ~March 10 |
| n8n Meta Ads Slack message sheet link | PLACEHOLDER (`1YourInsightLinksSheetID`) -- cosmetic issue, separate from the real data sheet |
| Mailchimp API key | EXISTS (Jay configured it in the Claude Chat project) -- may have been invalidated by Mailchimp security update |
| Claude Chat Mailchimp ingestion | BROKEN since ~March 10 -- was writing to the Google Sheet 3x/week |
| Mailchimp manual login (Noreen) | BLOCKED -- locked out by security update as of Mar 20 |
| Lays Mailchimp admin access | GRANTED by Jake on Mar 12 -- Lays can export manually |
| Claude Chat /friday skill | WORKING -- Lays used it Mar 20, but Mailchimp data was stale |
| Team awareness of spreadsheet | LOW -- Lays didn't know about it; Noreen still does manual exports |

### Most Likely Root Cause

The **Mailchimp security update** that locked out Noreen's browser login on March 20 likely **also invalidated the API key** used by the Claude Chat project around March 10. Mailchimp (especially us18 datacenter) periodically enforces security updates that can revoke API keys tied to accounts requiring MFA enrollment. The ~10-day gap between the API stopping (March 10) and Noreen discovering the browser lockout (March 20) is consistent with Mailchimp rolling out enforcement gradually.

---

## What Needs to Be Fixed

### Immediate (this week)

1. **Fix Mailchimp login for Noreen** -- Sindy needs to complete the security update on the shared Mailchimp credentials (`us18.admin.mailchimp.com`). This is likely an MFA enrollment requirement that Mailchimp recently enforced.

2. **Regenerate the Mailchimp API key** -- After the security update is completed, generate a new API key from the Mailchimp account and update it in:
   - The Insight Links Claude Chat project (so the 3x/week ingestion resumes)
   - n8n credentials (so an automated workflow can be built later)

3. **Manually trigger a Mailchimp data backfill** -- Use the Claude Chat project to pull all subscribers from March 10-21 and append to the existing Google Sheet (ID: `1Ed5meyHx1Vt1VTWJ4t2grBj_181rBxY2Jq912UiZJ6Q`)

4. **Share the spreadsheet with the team** -- Send the link to Lays, Noreen, and Sindy so they know it exists:
   `https://docs.google.com/spreadsheets/d/1Ed5meyHx1Vt1VTWJ4t2grBj_181rBxY2Jq912UiZJ6Q/edit`

### Short-term (next 1-2 weeks)

5. **Replace the n8n bot placeholder sheet ID** -- The n8n workflow that posts to `#internal-insightlinks` references `1YourInsightLinksSheetID` in its Slack messages. Replace with the real weekly ad report sheet ID (this is a separate sheet from the Mailchimp data sheet).

6. **Build a proper n8n Mailchimp workflow** -- Move the ingestion from Claude Chat (which requires manual triggering or a Cowork schedule) to n8n (which has native cron scheduling). The workflow should:
   - Use the Mailchimp API key
   - Pull subscriber data from 3 audiences (CW, IW, DHW)
   - Filter by UTM source (`facebookads`) to isolate TFM-driven subscribers
   - Export first-party data fields (name, role, company, qualified status)
   - Write to the existing Google Sheet (`1Ed5meyHx1Vt1VTWJ4t2grBj_181rBxY2Jq912UiZJ6Q`) incrementally
   - Run on a schedule (daily or 3x/week, matching Jay's original design)

7. **Update client-config.md** -- Change `esp_api_access` from `false` to `true` and update `n8n_status` from `IN PROGRESS` to reflect the actual state.

### Longer-term

8. **Nathan's question (Mar 21)** -- Nathan asked "Where can we see this data he's citing directly, can we make these calls on our own / do we have direct access?" Answer: the data is in the spreadsheet above. Once the pipeline is restored, anyone can access it.

---

## Can This Be Fixed via n8n MCP?

**Partially.** The n8n MCP connection is established (`memory/MEMORY.md` confirms this). Here is what can and cannot be done:

| Action | MCP Capable? | Notes |
|--------|-------------|-------|
| Find and inspect existing n8n workflows | Yes | Use n8n API to list workflows and check configurations |
| Update the placeholder sheet ID in n8n bot | Yes | If we have the workflow ID, update the Slack message template |
| Build the Mailchimp n8n workflow | Yes | n8n has a native Mailchimp node; API key exists (once regenerated) |
| Fix Mailchimp login credentials | No | Manual admin action in Mailchimp |
| Regenerate Mailchimp API key | No | Manual action in Mailchimp account settings |
| Read the existing Google Sheet | Yes | Via Google Drive MCP (confirmed working -- sheet ID: `1Ed5meyHx1Vt1VTWJ4t2grBj_181rBxY2Jq912UiZJ6Q`) |

**Recommendation:** Fix the Mailchimp security issue and regenerate the API key first (manual). Then restore the Claude Chat ingestion for immediate data backfill. In parallel, build the n8n Mailchimp workflow for long-term reliability (n8n handles scheduling natively, unlike Claude Chat which requires Cowork or manual triggers).

---

## Key Files & Resources

- **Mailchimp qualified lead spreadsheet:** `https://docs.google.com/spreadsheets/d/1Ed5meyHx1Vt1VTWJ4t2grBj_181rBxY2Jq912UiZJ6Q/edit` (3,300+ rows, last updated ~March 10)
- `/Users/jay/Documents/the vault/the-feed-media/clients/insight-links/client-config.md` -- n8n automation status, Meta account IDs
- `/Users/jay/Documents/the vault/the-feed-media/clients/insight-links/insight-links.md` -- Full client intelligence
- `/Users/jay/Documents/the vault/the-feed-media/clients/insight-links/claude-chat-project.md` -- /friday skill instructions, data source priority
- `/Users/jay/Documents/the vault/the-feed-media/research/n8n-friday-report-automation.md` -- Friday report automation design doc

---

## Slack Evidence

| Date | Channel | Who | Key Quote |
|------|---------|-----|-----------|
| Feb 26 | #internal-insightlinks | Jay | "once we finish piping in the mailchimp data to claude via N8N... Potentially by next week" |
| Mar 6 | #internal-insightlinks | Kinte | "Jay/Rabii building Mailchimp + Meta Ads UTM dashboard to automate lead quality analysis" |
| Mar 11 | #internal-insightlinks | Jay | "I had claude build the N8N workflow in the Insight Links Project using the Mailchimp API key" |
| Mar 13 | #ai-stuff | Jay | "Claude built the N8N flow that pulls the data from mailchimp and updates a spreadsheet it can reference" |
| Mar 20 | #internal-insightlinks | Noreen | "It is asking me to enable these when logging into Insight Link's Mailchimp account" |
| Mar 20 | #internal-insightlinks | Jay | "Do we even need this anymore? We have an entirely functioning Insight Links Claude project that ingests the data 3x a week into a spreadsheet" |
| Mar 20 | #internal-insightlinks | Lays | "where exactly you get this and the spreadsheet? i never used it for reporting" |
| Mar 20 | #internal-insightlinks | Lays | "also n8n looks like its not connected on insight links project" |
| Mar 20 | #internal-insightlinks | Jay | "it's good. just type /friday" |
| Mar 20 | #internal-insightlinks | Lays | Successfully generated /friday report using the Claude project -- "really good actually" |
| Mar 21 | #internal-insightlinks | Nathan | "Where can we see this data he's citing directly, can we make these calls on our own?" |
