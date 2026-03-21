# n8n Friday Ad Report Automation -- Workflow Design Document

> **Author:** Jay Warner (with Claude Code)
> **Date:** 2026-03-21
> **n8n Instance:** https://n8n-zwzfv-u62151.vm.elestio.app/
> **Status:** Design complete -- ready to build

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Client Registry](#client-registry)
3. [Credentials Required](#credentials-required)
4. [Workflow Architecture](#workflow-architecture)
5. [Node-by-Node Build Guide](#node-by-node-build-guide)
6. [Code Node: Calculations & Report Generation](#code-node-calculations--report-generation)
7. [Markdown Report Template](#markdown-report-template)
8. [Slack Message Format](#slack-message-format)
9. [Google Sheets Output](#google-sheets-output)
10. [Error Handling](#error-handling)
11. [Step-by-Step Build Instructions](#step-by-step-build-instructions)
12. [Future Enhancements](#future-enhancements)

---

## Executive Summary

This workflow automates the Friday weekly ad reports that GMs currently build manually. It runs every Friday at 8 AM EST, pulls 7-day and prior-7-day Meta Ads data for each client with an active ad account, calculates WoW changes, identifies top/bottom performers, flags anomalies, generates a markdown report, writes it to Google Sheets, saves a markdown file path for the Obsidian vault, and posts a summary to each client's internal Slack channel.

**Scope:** 20 clients with active Meta ad accounts (5 excluded: Daily Drop has no Meta access, Jay Shetty account not accessible, MDhair no direct access, Student Loan Planner account ID unknown, 1636 Forum/Franklin's Forum no client-config yet).

**Time savings:** ~3-5 hours per Friday across all GMs (Noreen, Mariely, Lays, Luiz, Kinte, Aubree, Rabii).

---

## Client Registry

### Clients WITH Meta Ad Account Access (20 accounts, 18 clients)

| Client | Display Name | Meta Account ID | TFM Campaign IDs | Internal Slack | GM |
|--------|-------------|-----------------|-------------------|----------------|-----|
| creator-spotlight | Creator Spotlight | `act_727705002666774` | `120216624988160734` | `#internal-creatorspotlight` (C07HZJJMA15) | Kinte |
| workweek-ihih | Workweek IHIH | `act_3186358998360632` | `120238290253090498, 120208519540300498` | `#internal-workweek` (C09UD5BV2BF) | Lays |
| workweek-tmm | Workweek TMM | `act_579954186820640` | `120241087157250671` | `#internal-workweek` (C09UD5BV2BF) | Lays |
| workweek-ftt | Workweek FTT | `act_1079516909306359` | `120238837962440504` | `#internal-workweek` (C09UD5BV2BF) | Lays |
| workweek-hospitalogy | Workweek Hospitalogy | `act_718612189266939` | `120238302528030086` | `#internal-workweek` (C09UD5BV2BF) | Lays |
| workweek-gtm | Workweek GTM | `act_4673797136057796` | `120240688746600606` | `#internal-workweek` (C09UD5BV2BF) | Lays |
| insight-links | Insight Links | `act_507049163040180` | `120237192634290138, 120237192451030138, 120237192398350138` | `#internal-insightlinks` (C0A42KZ2LQJ) | Lays |
| status-news | Status (News) | `act_455914147435901` | `120243366378750523, 120241815669990523, 120241057099280523, 120239876632620523, 120238873439040523, 120238644813440523, 120235752231100523` | `#internal-status` (C0984JRVDSP) | Mariely |
| stocks-news | Stocks.News | `act_966430194860576` | `120242193401400071, 120242023971680071, 120241993404490071, 120241992974490071, 120240942718220071` | `#internal-stocksnews` (C0A2ZMQTCFR) | Luiz |
| the-points-guy | The Points Guy | `act_2130099530351734` | N/A (client-managed, pull all campaigns) | `#internal-thepointsguy` (C0839CZFUUV) | TBD |
| houck | Houck | `act_601589271801820` | `120238584953010261, 120200529584720261` | `#internal-houck` (C09TT2ZSH32) | Luiz |
| rnt-fitness | RNT Fitness | `act_537505457933105` | `120240247632280778, 120240119514690778` | `#internal-rntfitness` (C0ACV5VHUPK) | Kinte |
| open-source-ceo | Open Source CEO | `act_2116667552418074` | `6958020369131, 6950633724531` | TBD | Aubree |
| how-to-ai | How to AI | `act_816391071105542` | `120239700230400357, 120240547128120357, 120240395655420357, 120239378125600357, 120239308381030357` | `#internal-howtoai` (C09KU3F7VHC) | Lays |
| points-path | Points Path | `act_1308877270502995` | `120248511369720001, 120248430244050001, 120238756601280001, 120238261305450001, 120237662807030001` | `#internal-pointspath` (C096YCS758C) | Mariely |
| experiential-hospitality | Experiential Hospitality | `act_1644253359451312` | `120233091829250773, 120235106631360773, 120234731663350773, 120228669798540773, 120223232332080773, 120222985791330773, 120222543868400773` | `#internal-experientialhospitality` (C08Q8MBH0U9) | Mariely |
| quartz | Quartz | `act_757128750591828` | `120239976753120549` | `#internal-quartz` (C0A4Y7GG230) | Mariely |
| big-desk-energy | Big Desk Energy | `act_1402347147137781` | `120209659764470257, 120236433611840257, 120219966944520257, 120218640282360257, 120210326422460257, 120209553752630257` | `#internal-bigdeskenergy` (C07Q8KK2ED6) | Mariely |
| stocks-and-income | Stocks & Income | `act_24102682642704582` | `120241316704030382` | `#internal-stocksandincome` (C0AEBKGNTS5) | Luiz |
| contrarian-thinking | Contrarian Thinking | `act_1329828287615052` | `120240521788490641, 120240516863300641` | `#internal-contrarianthinking` (C0AD4PEDQGL) | Luiz |
| marketbeat | MarketBeat | `act_1129788478833121` | `120234644644600565` | `#internal-marketbeat` (C09EDCNGFD0) | Rabii |
| vendry | Vendry | `act_1283376772272478` | TBD -- needs campaign ID lookup | `#internal-vendry` (C08HB4N8WP7) | Aubree |
| just-womens-sports | Just Women's Sports | Partner ID `730307861597413` | TBD -- needs campaign ID lookup | `#internal-justwsports` | TBD |

### Clients EXCLUDED from automation

| Client | Reason |
|--------|--------|
| daily-drop | Creative-only engagement -- TFM does not run media |
| jay-shetty | Meta account not accessible via TFM Pipeboard token |
| mdhair | No direct Meta ad account access |
| student-loan-planner | Meta account ID not in client config (needs lookup) |
| 1636-forum | No client-config.md yet (needs Meta account ID) |
| franklins-forum | No client-config.md yet (needs Meta account ID) |

> **Action item:** Before building, look up Meta account IDs for 1636 Forum, Franklin's Forum, Student Loan Planner, JWS, and Vendry campaign IDs via Pipeboard MCP or Meta Ads Manager.

---

## Credentials Required

| Credential | Type | Used For | Setup Notes |
|------------|------|----------|-------------|
| **Meta Marketing API** | OAuth 2.0 / System User Token | Pulling ad performance data | Need a long-lived System User token from TFM Business Manager with `ads_read` permission. A single token with partner access to all client ad accounts is ideal. Alternatively use one token per account. |
| **Google Sheets** | OAuth 2.0 | Writing report data | n8n built-in Google Sheets node. Requires OAuth setup (currently blocked per session log -- resolve this first). |
| **Slack** | OAuth 2.0 / Bot Token | Posting summaries | n8n Slack node. Use the TFM Slack workspace bot token. Needs `chat:write` scope and membership in all `#internal-*` channels. |

### Meta API Token Setup

1. Go to Meta Business Manager > Business Settings > System Users
2. Create or select a System User (e.g., "n8n-reporting")
3. Assign `ads_read` permission for each client ad account
4. Generate a long-lived token (60-day expiry, or use a Page token that does not expire)
5. Store in n8n as an "HTTP Header Auth" credential: `Authorization: Bearer {token}`

> **Important:** The token must have read access to ALL client ad accounts listed above. For partner/shared accounts (Creator Spotlight, Quartz, Stocks.News, MarketBeat, etc.), the System User needs partner-level read access.

---

## Workflow Architecture

```
[Cron Trigger: Friday 8AM EST]
        |
        v
[Function Node: Client Registry]
        |
        v
[Split In Batches] -----> (for each client)
        |
        v
[HTTP Request: Meta Ads - This Week]
        |
        v
[HTTP Request: Meta Ads - Last Week]
        |
        v
[HTTP Request: Meta Ads - Ad-Level This Week]
        |
        v
[Code Node: Calculate WoW + Anomalies + Report]
        |
        +--> [Google Sheets: Write Report Data]
        |
        +--> [Slack: Post Summary to #internal-{client}]
        |
        +--> [Function: Generate Markdown File Content]
                |
                v
        [Write Binary File: Save .md to vault] (optional)
        |
[Merge: Collect all results]
        |
        v
[Slack: Post master summary to #internal-operations]
```

### Flow Description

1. **Cron** fires every Friday at 8:00 AM America/New_York
2. **Client Registry** node outputs an array of client objects with Meta account IDs, campaign filters, Slack channels, CPL targets, and display names
3. **Split In Batches** iterates through each client (batch size 1, with a 2-second delay to respect Meta rate limits)
4. For each client, **three HTTP requests** pull data from Meta Marketing API:
   - Account-level metrics for this week (last 7 days)
   - Account-level metrics for previous week (8-14 days ago)
   - Ad-level metrics for this week (for top/bottom performer identification)
5. **Code Node** crunches the numbers: WoW changes, top 3 / bottom 3 by CPL, anomaly flags
6. **Three outputs** in parallel:
   - Google Sheets row per client
   - Slack message to internal channel
   - Markdown report content (for Obsidian vault)
7. After all clients are processed, a **master summary** goes to `#internal-operations` or a designated reporting channel

---

## Node-by-Node Build Guide

### Node 1: Schedule Trigger (Cron)

- **Node type:** Schedule Trigger
- **Configuration:**
  - Mode: `Cron`
  - Cron Expression: `0 8 * * 5` (Every Friday at 8:00)
  - Timezone: `America/New_York`

### Node 2: Client Registry (Code Node)

- **Node type:** Code
- **Purpose:** Outputs one item per client with all config needed for the API calls

```javascript
const clients = [
  {
    slug: "creator-spotlight",
    displayName: "Creator Spotlight",
    accountId: "act_727705002666774",
    campaignFilter: ["120216624988160734"],
    slackChannel: "C07HZJJMA15",
    cplTarget: 2.25,
    gm: "Kinte",
    conversionAction: "offsite_conversion.fb_pixel_lead",
    notes: "Shared account with BG -- filter to TFM campaigns only"
  },
  {
    slug: "workweek-ihih",
    displayName: "Workweek - IHIH",
    accountId: "act_3186358998360632",
    campaignFilter: ["120238290253090498", "120208519540300498"],
    slackChannel: "C09UD5BV2BF",
    cplTarget: 45.0,
    gm: "Lays",
    conversionAction: "offsite_conversion.fb_pixel_lead",
    notes: "V-CAC is the real KPI -- raw CPL is a proxy. Post Slack with V-CAC caveat."
  },
  {
    slug: "workweek-tmm",
    displayName: "Workweek - TMM",
    accountId: "act_579954186820640",
    campaignFilter: ["120241087157250671"],
    slackChannel: "C09UD5BV2BF",
    cplTarget: 40.0,
    gm: "Lays",
    conversionAction: "offsite_conversion.fb_pixel_lead",
    notes: "V-CAC client"
  },
  {
    slug: "workweek-ftt",
    displayName: "Workweek - FTT",
    accountId: "act_1079516909306359",
    campaignFilter: ["120238837962440504"],
    slackChannel: "C09UD5BV2BF",
    cplTarget: 55.0,
    gm: "Lays",
    conversionAction: "offsite_conversion.fb_pixel_lead",
    notes: "V-CAC client"
  },
  {
    slug: "workweek-hospitalogy",
    displayName: "Workweek - Hospitalogy",
    accountId: "act_718612189266939",
    campaignFilter: ["120238302528030086"],
    slackChannel: "C09UD5BV2BF",
    cplTarget: 40.0,
    gm: "Lays",
    conversionAction: "offsite_conversion.fb_pixel_lead",
    notes: "V-CAC client"
  },
  {
    slug: "workweek-gtm",
    displayName: "Workweek - GTM",
    accountId: "act_4673797136057796",
    campaignFilter: ["120240688746600606"],
    slackChannel: "C09UD5BV2BF",
    cplTarget: 170.0,
    gm: "Lays",
    conversionAction: "offsite_conversion.fb_pixel_lead",
    notes: "V-CAC client. 3.7% convert rate on verification funnel."
  },
  {
    slug: "insight-links",
    displayName: "Insight Links",
    accountId: "act_507049163040180",
    campaignFilter: ["120237192634290138", "120237192451030138", "120237192398350138"],
    slackChannel: "C0A42KZ2LQJ",
    cplTarget: 5.0,
    gm: "Lays",
    conversionAction: "offsite_conversion.fb_pixel_lead",
    notes: "Bake-off vs Growletter. 3 newsletters (DHW, CW, IW). Qualified CPL is the real KPI."
  },
  {
    slug: "status-news",
    displayName: "Status (News)",
    accountId: "act_455914147435901",
    campaignFilter: ["120243366378750523", "120241815669990523"],
    slackChannel: "C0984JRVDSP",
    cplTarget: 1.50,
    gm: "Mariely",
    conversionAction: "offsite_conversion.fb_pixel_lead",
    notes: "Qualified funnel only. Premium conversion is real KPI."
  },
  {
    slug: "stocks-news",
    displayName: "Stocks.News",
    accountId: "act_966430194860576",
    campaignFilter: ["120242193401400071", "120241993404490071", "120241992974490071", "120240942718220071"],
    slackChannel: "C0A2ZMQTCFR",
    cplTarget: 10.0,
    gm: "Luiz",
    conversionAction: "offsite_conversion.fb_pixel_lead",
    notes: "Shared account with GrowJoy. CPT (Cost Per Trial) is real KPI at <$50."
  },
  {
    slug: "the-points-guy",
    displayName: "The Points Guy",
    accountId: "act_2130099530351734",
    campaignFilter: [],  // Pull all -- client-managed but TFM tracks
    slackChannel: "C0839CZFUUV",
    cplTarget: 4.00,
    gm: "TBD",
    conversionAction: "offsite_conversion.fb_pixel_lead",
    notes: "Largest account. Client-managed. 6-week ROAS is real KPI."
  },
  {
    slug: "houck",
    displayName: "Houck (Founding Journey)",
    accountId: "act_601589271801820",
    campaignFilter: ["120238584953010261", "120200529584720261"],
    slackChannel: "C09TT2ZSH32",
    cplTarget: 10.0,
    gm: "Luiz",
    conversionAction: "offsite_conversion.fb_pixel_lead",
    notes: "Qualified leads are the real KPI -- 50%+ must be founders."
  },
  {
    slug: "rnt-fitness",
    displayName: "RNT Fitness",
    accountId: "act_537505457933105",
    campaignFilter: ["120240247632280778"],
    slackChannel: "C0ACV5VHUPK",
    cplTarget: null,
    gm: "Kinte",
    conversionAction: "offsite_conversion.fb_pixel_lead",
    notes: "CPL target unconfirmed. Account in GBP. New client."
  },
  {
    slug: "open-source-ceo",
    displayName: "Open Source CEO",
    accountId: "act_2116667552418074",
    campaignFilter: ["6958020369131"],
    slackChannel: null,  // No Slack channel set up yet
    cplTarget: 3.0,
    gm: "Aubree",
    conversionAction: "offsite_conversion.fb_pixel_lead",
    notes: "ANZ targeting only."
  },
  {
    slug: "how-to-ai",
    displayName: "How to AI",
    accountId: "act_816391071105542",
    campaignFilter: ["120239700230400357"],
    slackChannel: "C09KU3F7VHC",
    cplTarget: 2.0,
    gm: "Lays",
    conversionAction: "offsite_conversion.fb_pixel_lead",
    notes: "Currently above target ($3.47 vs $2.00)."
  },
  {
    slug: "points-path",
    displayName: "Points Path",
    accountId: "act_1308877270502995",
    campaignFilter: ["120248511369720001", "120248430244050001", "120238756601280001"],
    slackChannel: "C096YCS758C",
    cplTarget: 1.50,
    gm: "Mariely",
    conversionAction: "offsite_conversion.fb_pixel_lead",
    notes: "Extension install CVR is secondary KPI."
  },
  {
    slug: "experiential-hospitality",
    displayName: "Experiential Hospitality",
    accountId: "act_1644253359451312",
    campaignFilter: ["120233091829250773"],
    slackChannel: "C08Q8MBH0U9",
    cplTarget: 6.0,
    gm: "Mariely",
    conversionAction: "offsite_conversion.fb_pixel_lead",
    notes: "Webinar registrations. ROAS is secondary KPI."
  },
  {
    slug: "quartz",
    displayName: "Quartz",
    accountId: "act_757128750591828",
    campaignFilter: ["120239976753120549"],
    slackChannel: "C0A4Y7GG230",
    cplTarget: 2.50,
    gm: "Mariely",
    conversionAction: "offsite_conversion.fb_pixel_lead",
    notes: "Bake-off account. TFM campaign only. Currently $3.63 vs $2.50 target."
  },
  {
    slug: "big-desk-energy",
    displayName: "Big Desk Energy",
    accountId: "act_1402347147137781",
    campaignFilter: ["120209659764470257"],
    slackChannel: "C07Q8KK2ED6",
    cplTarget: 3.0,
    gm: "Mariely",
    conversionAction: "offsite_conversion.fb_pixel_lead",
    notes: "Shared account. Open rate is critical secondary KPI."
  },
  {
    slug: "stocks-and-income",
    displayName: "Stocks & Income",
    accountId: "act_24102682642704582",
    campaignFilter: ["120241316704030382"],
    slackChannel: "C0AEBKGNTS5",
    cplTarget: 2.0,
    gm: "Luiz",
    conversionAction: "offsite_conversion.fb_pixel_lead",
    notes: "After Offers co-reg revenue matters. At $1.50 CPL, profitable day one."
  },
  {
    slug: "contrarian-thinking",
    displayName: "Contrarian Thinking",
    accountId: "act_1329828287615052",
    campaignFilter: ["120240521788490641", "120240516863300641"],
    slackChannel: "C0AD4PEDQGL",
    cplTarget: 5.5,
    gm: "Luiz",
    conversionAction: "offsite_conversion.fb_pixel_lead",
    notes: "90-day trial. Currently zero ads live as of Mar 10."
  },
  {
    slug: "marketbeat",
    displayName: "MarketBeat",
    accountId: "act_1129788478833121",
    campaignFilter: ["120234644644600565"],
    slackChannel: "C09EDCNGFD0",
    cplTarget: 14.0,
    gm: "Rabii",
    conversionAction: "offsite_conversion.fb_pixel_lead",
    notes: "ROAS is real KPI. RegistrationCode tracking. Runs under Early Bird Publishing."
  },
  {
    slug: "vendry",
    displayName: "Vendry",
    accountId: "act_1283376772272478",
    campaignFilter: [],  // TBD -- needs campaign ID lookup
    slackChannel: "C08HB4N8WP7",
    cplTarget: null,
    gm: "Aubree",
    conversionAction: "offsite_conversion.fb_pixel_lead",
    notes: "Campaign IDs need lookup before enabling."
  }
];

return clients.map(c => ({ json: c }));
```

### Node 3: Split In Batches

- **Node type:** SplitInBatches
- **Configuration:**
  - Batch Size: `1`
  - Options > Reset: `false`

> **Rate limiting:** Add a 2-second Wait node after each batch to stay under Meta's 200 calls/hour/ad-account limit.

### Node 4: Set Date Range (Code Node)

- **Node type:** Code
- **Purpose:** Calculate the date ranges for "this week" and "last week"

```javascript
const now = new Date();
// "This week" = last 7 completed days (yesterday back 7 days)
const thisWeekEnd = new Date(now);
thisWeekEnd.setDate(thisWeekEnd.getDate() - 1); // yesterday
const thisWeekStart = new Date(thisWeekEnd);
thisWeekStart.setDate(thisWeekStart.getDate() - 6); // 7 days total

// "Last week" = the 7 days before that
const lastWeekEnd = new Date(thisWeekStart);
lastWeekEnd.setDate(lastWeekEnd.getDate() - 1);
const lastWeekStart = new Date(lastWeekEnd);
lastWeekStart.setDate(lastWeekStart.getDate() - 6);

const fmt = (d) => d.toISOString().split('T')[0];

const client = $input.first().json;

return [{
  json: {
    ...client,
    thisWeekStart: fmt(thisWeekStart),
    thisWeekEnd: fmt(thisWeekEnd),
    lastWeekStart: fmt(lastWeekStart),
    lastWeekEnd: fmt(lastWeekEnd),
    reportDateRange: `${fmt(thisWeekStart)} to ${fmt(thisWeekEnd)}`
  }
}];
```

### Node 5: HTTP Request -- Meta Ads (This Week, Account Level)

- **Node type:** HTTP Request
- **Method:** `GET`
- **URL:** `https://graph.facebook.com/v21.0/{{ $json.accountId }}/insights`
- **Authentication:** HTTP Header Auth (Meta token)
- **Query Parameters:**
  - `time_range`: `{"since":"{{ $json.thisWeekStart }}","until":"{{ $json.thisWeekEnd }}"}`
  - `fields`: `spend,impressions,clicks,ctr,cpc,cpm,actions,cost_per_action_type,website_ctr,inline_link_clicks,inline_link_click_ctr`
  - `filtering`: `[{"field":"campaign.id","operator":"IN","value":{{ $json.campaignFilter }}}]` (only if campaignFilter is non-empty)
  - `level`: `account`
  - `access_token`: `{{ $credentials.metaToken }}`

> **Note on campaign filtering:** For clients with `campaignFilter: []` (empty), omit the `filtering` parameter to pull all campaigns. For shared accounts, the filter ensures we only get TFM data.

**Handling the filtering parameter dynamically:**

If campaignFilter is empty, do NOT include the filtering param. Use an IF node before this, or handle it in the URL construction via a Code node:

```javascript
const client = $input.first().json;
const baseUrl = `https://graph.facebook.com/v21.0/${client.accountId}/insights`;
const fields = "spend,impressions,clicks,ctr,cpc,cpm,actions,cost_per_action_type,inline_link_clicks,inline_link_click_ctr";

let url = `${baseUrl}?fields=${fields}&time_range={"since":"${client.thisWeekStart}","until":"${client.thisWeekEnd}"}&level=account&access_token={{META_TOKEN}}`;

if (client.campaignFilter && client.campaignFilter.length > 0) {
  const filterJson = JSON.stringify([{
    field: "campaign.id",
    operator: "IN",
    value: client.campaignFilter
  }]);
  url += `&filtering=${encodeURIComponent(filterJson)}`;
}

return [{ json: { ...client, thisWeekUrl: url } }];
```

### Node 6: HTTP Request -- Meta Ads (Last Week, Account Level)

- **Same as Node 5** but with `lastWeekStart` and `lastWeekEnd` in the time_range.

### Node 7: HTTP Request -- Meta Ads (This Week, Ad Level)

- **Node type:** HTTP Request
- **Method:** `GET`
- **URL:** `https://graph.facebook.com/v21.0/{{ $json.accountId }}/insights`
- **Query Parameters:**
  - `time_range`: `{"since":"{{ $json.thisWeekStart }}","until":"{{ $json.thisWeekEnd }}"}`
  - `fields`: `ad_name,adset_name,campaign_name,spend,impressions,clicks,actions,cost_per_action_type,inline_link_clicks,inline_link_click_ctr`
  - `filtering`: (same campaign filter logic)
  - `level`: `ad`
  - `limit`: `100`
  - `sort`: `spend_descending`

> This gives us per-ad breakdown to identify top and bottom performers.

### Node 8: Code Node -- Calculate WoW + Anomalies + Report

This is the core logic node. It takes the three API responses and produces the report.

```javascript
// Input: client config + thisWeekData + lastWeekData + adLevelData
const client = $input.first().json;

// Parse API responses (adjust based on actual node output names)
// In n8n, you'd reference these via $('Node Name').first().json
const thisWeekRaw = $('Meta This Week').first().json;
const lastWeekRaw = $('Meta Last Week').first().json;
const adLevelRaw = $('Meta Ad Level').all().map(i => i.json);

// ========== HELPER FUNCTIONS ==========

function getActionValue(actions, actionType) {
  if (!actions || !Array.isArray(actions)) return 0;
  const found = actions.find(a => a.action_type === actionType);
  return found ? parseFloat(found.value) : 0;
}

function getCostPerAction(costPerActions, actionType) {
  if (!costPerActions || !Array.isArray(costPerActions)) return 0;
  const found = costPerActions.find(a => a.action_type === actionType);
  return found ? parseFloat(found.value) : 0;
}

function pctChange(current, previous) {
  if (!previous || previous === 0) return current > 0 ? 100 : 0;
  return ((current - previous) / previous * 100);
}

function fmtPct(val) {
  if (val === null || val === undefined) return "N/A";
  const prefix = val > 0 ? "+" : "";
  return `${prefix}${val.toFixed(1)}%`;
}

function fmtDollar(val) {
  if (val === null || val === undefined || isNaN(val)) return "$0.00";
  return `$${val.toFixed(2)}`;
}

// ========== PARSE THIS WEEK ==========

const tw = thisWeekRaw.data ? thisWeekRaw.data[0] : thisWeekRaw;
const twSpend = parseFloat(tw?.spend || 0);
const twImpressions = parseInt(tw?.impressions || 0);
const twClicks = parseInt(tw?.inline_link_clicks || tw?.clicks || 0);
const twCtr = parseFloat(tw?.inline_link_click_ctr || tw?.ctr || 0);
const twCpm = parseFloat(tw?.cpm || 0);
const twConversions = getActionValue(tw?.actions, client.conversionAction);
const twCpl = twConversions > 0 ? twSpend / twConversions : 0;
const twCvr = twClicks > 0 ? (twConversions / twClicks * 100) : 0;

// ========== PARSE LAST WEEK ==========

const lw = lastWeekRaw.data ? lastWeekRaw.data[0] : lastWeekRaw;
const lwSpend = parseFloat(lw?.spend || 0);
const lwImpressions = parseInt(lw?.impressions || 0);
const lwClicks = parseInt(lw?.inline_link_clicks || lw?.clicks || 0);
const lwCtr = parseFloat(lw?.inline_link_click_ctr || lw?.ctr || 0);
const lwConversions = getActionValue(lw?.actions, client.conversionAction);
const lwCpl = lwConversions > 0 ? lwSpend / lwConversions : 0;
const lwCvr = lwClicks > 0 ? (lwConversions / lwClicks * 100) : 0;

// ========== WOW CHANGES ==========

const wowSpend = pctChange(twSpend, lwSpend);
const wowImpressions = pctChange(twImpressions, lwImpressions);
const wowClicks = pctChange(twClicks, lwClicks);
const wowCtr = pctChange(twCtr, lwCtr);
const wowCpl = pctChange(twCpl, lwCpl);
const wowCvr = pctChange(twCvr, lwCvr);
const wowConversions = pctChange(twConversions, lwConversions);

// ========== AD-LEVEL ANALYSIS ==========

const ads = (adLevelRaw.data || adLevelRaw || []).map(ad => {
  const adSpend = parseFloat(ad.spend || 0);
  const adClicks = parseInt(ad.inline_link_clicks || ad.clicks || 0);
  const adConversions = getActionValue(ad.actions, client.conversionAction);
  const adCpl = adConversions > 0 ? adSpend / adConversions : 999999;
  const adCtr = parseFloat(ad.inline_link_click_ctr || ad.ctr || 0);
  const adCvr = adClicks > 0 ? (adConversions / adClicks * 100) : 0;
  return {
    name: ad.ad_name || "Unknown",
    adsetName: ad.adset_name || "",
    campaignName: ad.campaign_name || "",
    spend: adSpend,
    conversions: adConversions,
    cpl: adCpl,
    ctr: adCtr,
    cvr: adCvr,
    clicks: adClicks
  };
}).filter(a => a.spend > 0);

// Sort by CPL (best first)
const adsByCpl = [...ads].sort((a, b) => a.cpl - b.cpl);
const top3 = adsByCpl.filter(a => a.conversions > 0).slice(0, 3);
const bottom3 = adsByCpl.filter(a => a.conversions > 0).reverse().slice(0, 3);

// ========== ANOMALY DETECTION ==========

const anomalies = [];

// CPL spike > 30%
if (wowCpl > 30 && lwCpl > 0) {
  anomalies.push(`CPL spiked ${fmtPct(wowCpl)} WoW (${fmtDollar(lwCpl)} -> ${fmtDollar(twCpl)})`);
}

// CPL above target
if (client.cplTarget && twCpl > client.cplTarget * 1.2) {
  anomalies.push(`CPL (${fmtDollar(twCpl)}) is ${((twCpl / client.cplTarget - 1) * 100).toFixed(0)}% above target (${fmtDollar(client.cplTarget)})`);
}

// Spend pacing issue (>20% drop)
if (wowSpend < -20) {
  anomalies.push(`Spend dropped ${fmtPct(wowSpend)} WoW -- check budget pacing`);
}

// CTR drop > 25% (creative fatigue signal)
if (wowCtr < -25 && lwCtr > 0) {
  anomalies.push(`CTR dropped ${fmtPct(wowCtr)} WoW -- possible creative fatigue`);
}

// CVR drop > 20% (landing page issue)
if (wowCvr < -20 && lwCvr > 0) {
  anomalies.push(`CVR dropped ${fmtPct(wowCvr)} WoW -- check landing page`);
}

// Zero conversions
if (twConversions === 0 && twSpend > 50) {
  anomalies.push(`Zero conversions this week despite ${fmtDollar(twSpend)} spend`);
}

// ========== BUILD REPORT OBJECT ==========

const report = {
  client: client.slug,
  displayName: client.displayName,
  gm: client.gm,
  slackChannel: client.slackChannel,
  cplTarget: client.cplTarget,
  dateRange: client.reportDateRange,
  thisWeek: {
    spend: twSpend,
    impressions: twImpressions,
    clicks: twClicks,
    conversions: twConversions,
    cpl: twCpl,
    ctr: twCtr,
    cvr: twCvr,
    cpm: twCpm
  },
  lastWeek: {
    spend: lwSpend,
    impressions: lwImpressions,
    clicks: lwClicks,
    conversions: lwConversions,
    cpl: lwCpl,
    ctr: lwCtr,
    cvr: lwCvr
  },
  wow: {
    spend: wowSpend,
    impressions: wowImpressions,
    clicks: wowClicks,
    conversions: wowConversions,
    cpl: wowCpl,
    ctr: wowCtr,
    cvr: wowCvr
  },
  top3: top3,
  bottom3: bottom3,
  anomalies: anomalies,
  notes: client.notes
};

return [{ json: report }];
```

### Node 9: Code Node -- Generate Markdown Report

```javascript
const r = $input.first().json;
const fmtD = (v) => `$${v.toFixed(2)}`;
const fmtP = (v) => `${v.toFixed(2)}%`;
const fmtWow = (v) => {
  const prefix = v > 0 ? "+" : "";
  return `${prefix}${v.toFixed(1)}%`;
};
const fmtN = (v) => v.toLocaleString();

// Top performers table rows
const topRows = r.top3.map(a =>
  `| ${a.name} | ${fmtD(a.spend)} | ${a.conversions} | ${fmtD(a.cpl)} | ${fmtP(a.ctr)} |`
).join("\n");

// Bottom performers table rows
const bottomRows = r.bottom3.map(a => {
  let reason = "";
  if (a.cpl > (r.cplTarget || 999) * 1.5) reason = "CPL >50% above target";
  else if (a.ctr < 0.5) reason = "Low CTR";
  else if (a.cvr < 1) reason = "Low CVR";
  else reason = "Underperforming";
  return `| ${a.name} | ${reason} | Review / Pause |`;
}).join("\n");

// Anomaly bullets
const anomalyBullets = r.anomalies.length > 0
  ? r.anomalies.map(a => `- **FLAG:** ${a}`).join("\n")
  : "- No anomalies detected this week.";

const cplVsTarget = r.cplTarget
  ? `\n> **CPL vs Target:** ${fmtD(r.thisWeek.cpl)} vs ${fmtD(r.cplTarget)} target (${r.thisWeek.cpl <= r.cplTarget ? "ON TRACK" : "ABOVE TARGET"})`
  : "";

const markdown = `---
type: friday-report
client: "${r.displayName}"
date: ${r.dateRange.split(" to ")[1]}
week_of: ${r.dateRange}
tags: [report, friday, automated]
gm: ${r.gm}
---

# ${r.displayName} -- Weekly Ad Report

**Week of:** ${r.dateRange}
**GM:** ${r.gm}
**Generated:** ${new Date().toISOString().split("T")[0]} (automated via n8n)
${cplVsTarget}

## Performance Summary

| Metric | This Week | Last Week | WoW Change |
|--------|-----------|-----------|------------|
| Spend | ${fmtD(r.thisWeek.spend)} | ${fmtD(r.lastWeek.spend)} | ${fmtWow(r.wow.spend)} |
| Sign-ups | ${fmtN(r.thisWeek.conversions)} | ${fmtN(r.lastWeek.conversions)} | ${fmtWow(r.wow.conversions)} |
| CPL | ${fmtD(r.thisWeek.cpl)} | ${fmtD(r.lastWeek.cpl)} | ${fmtWow(r.wow.cpl)} |
| CTR | ${fmtP(r.thisWeek.ctr)} | ${fmtP(r.lastWeek.ctr)} | ${fmtWow(r.wow.ctr)} |
| CVR | ${fmtP(r.thisWeek.cvr)} | ${fmtP(r.lastWeek.cvr)} | ${fmtWow(r.wow.cvr)} |
| CPM | ${fmtD(r.thisWeek.cpm)} | -- | -- |

## Top Performers
| Creative | Spend | Results | CPL | CTR |
|----------|-------|---------|-----|-----|
${topRows || "| No data | -- | -- | -- | -- |"}

## Underperformers / Paused
| Creative | Reason | Action |
|----------|--------|--------|
${bottomRows || "| None flagged | -- | -- |"}

## Notes / Flags
${anomalyBullets}

## Client Notes
- ${r.notes || "No special notes."}

---
*Auto-generated by n8n Friday Report Workflow*
`;

return [{ json: { ...r, markdownReport: markdown } }];
```

### Node 10: Google Sheets -- Write Report Data

- **Node type:** Google Sheets
- **Operation:** Append Row
- **Spreadsheet:** Create a spreadsheet called "TFM Friday Reports" with one sheet per week (or a running log)
- **Sheet:** `Reports`
- **Columns to map:**

| Column | Value |
|--------|-------|
| Date | `{{ $json.dateRange }}` |
| Client | `{{ $json.displayName }}` |
| GM | `{{ $json.gm }}` |
| Spend | `{{ $json.thisWeek.spend }}` |
| Sign-ups | `{{ $json.thisWeek.conversions }}` |
| CPL | `{{ $json.thisWeek.cpl }}` |
| CTR | `{{ $json.thisWeek.ctr }}` |
| CVR | `{{ $json.thisWeek.cvr }}` |
| CPM | `{{ $json.thisWeek.cpm }}` |
| WoW Spend | `{{ $json.wow.spend }}` |
| WoW CPL | `{{ $json.wow.cpl }}` |
| WoW Conversions | `{{ $json.wow.conversions }}` |
| CPL Target | `{{ $json.cplTarget }}` |
| Anomalies | `{{ $json.anomalies.join("; ") }}` |
| Top 1 | `{{ $json.top3[0]?.name }}` |
| Top 1 CPL | `{{ $json.top3[0]?.cpl }}` |

### Node 11: Slack -- Post Summary

- **Node type:** Slack
- **Operation:** Send Message
- **Channel:** `{{ $json.slackChannel }}`
- **Message format:** See [Slack Message Format](#slack-message-format) below
- **Condition:** Only send if `slackChannel` is not null

### Node 12: Wait Node (Rate Limiting)

- **Node type:** Wait
- **Duration:** 2 seconds
- **Purpose:** Prevent hitting Meta API rate limits between clients

### Node 13 (Final): Master Summary to Operations Channel

After all clients are processed, send a single summary to `#internal-operations` or a reporting channel.

---

## Slack Message Format

```javascript
const r = $input.first().json;
const fmtD = (v) => `$${v.toFixed(2)}`;
const fmtP = (v) => `${v.toFixed(1)}%`;
const arrow = (v) => v > 0 ? ":arrow_up:" : v < 0 ? ":arrow_down:" : ":left_right_arrow:";
const fmtWow = (v) => `${arrow(v)} ${v > 0 ? "+" : ""}${v.toFixed(1)}%`;

const cplStatus = r.cplTarget
  ? (r.thisWeek.cpl <= r.cplTarget ? ":white_check_mark:" : ":warning:")
  : "";

const anomalyText = r.anomalies.length > 0
  ? "\n\n:rotating_light: *Flags:*\n" + r.anomalies.map(a => `> ${a}`).join("\n")
  : "";

const topText = r.top3.length > 0
  ? r.top3.map((a, i) => `${i+1}. *${a.name}* -- ${fmtD(a.cpl)} CPL (${a.conversions} leads)`).join("\n")
  : "No top performers with conversions this week.";

const message = `*${r.displayName} -- Weekly Ad Report*
_${r.dateRange}_

*Performance Summary:*
> Spend: *${fmtD(r.thisWeek.spend)}* ${fmtWow(r.wow.spend)}
> Sign-ups: *${r.thisWeek.conversions.toLocaleString()}* ${fmtWow(r.wow.conversions)}
> CPL: *${fmtD(r.thisWeek.cpl)}* ${fmtWow(r.wow.cpl)} ${cplStatus}
> CTR: *${fmtP(r.thisWeek.ctr)}* ${fmtWow(r.wow.ctr)}
> CVR: *${fmtP(r.thisWeek.cvr)}* ${fmtWow(r.wow.cvr)}

*Top Performers (by CPL):*
${topText}
${anomalyText}

_Auto-generated by n8n | Full report in Google Sheets_`;

return [{ json: { ...r, slackMessage: message } }];
```

---

## Google Sheets Output

### Spreadsheet Structure

**Spreadsheet name:** `TFM Friday Reports -- Automated`

**Sheet 1: Weekly Data (running log)**

| Date Range | Client | GM | Spend | Sign-ups | CPL | CTR | CVR | CPM | WoW Spend % | WoW CPL % | WoW Conversions % | CPL Target | CPL vs Target | Anomalies | Top Creative 1 | Top 1 CPL | Top Creative 2 | Top 2 CPL | Top Creative 3 | Top 3 CPL |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

**Sheet 2: Anomaly Log**

| Date | Client | Anomaly Type | Description | Severity |
|---|---|---|---|---|

This gives Noreen and the GMs a single source of truth for historical performance data and makes it easy to pull into Notion or charts.

---

## Error Handling

### Per-Client Error Handling

Wrap each client's API call sequence in a try/catch pattern using n8n's Error Trigger:

1. **API failures:** If a Meta API call fails (token expired, account suspended, rate limit), catch the error and:
   - Log the client name + error to an "Errors" sheet in Google Sheets
   - Post a warning to `#internal-operations`: `:x: Friday report failed for {client}: {error}`
   - Continue to the next client (do not halt the entire workflow)

2. **Empty data:** If a client has zero spend for the week (e.g., Contrarian Thinking with no live ads), generate a minimal report:
   - "No active spend this week. No ads running."
   - Still post to Slack so the GM is aware

3. **Rate limiting:** The 2-second Wait node between clients should prevent this. If you still hit rate limits:
   - Meta returns HTTP 429 with `error.code: 32`
   - Add retry logic: n8n HTTP node has built-in retry (set to 3 retries, 5-second delay)

### Global Error Handling

- Add an **Error Trigger** workflow that catches any unhandled errors and posts to `#internal-operations`
- Include the workflow execution URL so Jay can debug

### Token Expiry Monitoring

Meta System User tokens expire after 60 days. Add a separate small workflow:
- **Cron:** Every Monday at 9 AM EST
- **HTTP Request:** `GET https://graph.facebook.com/debug_token?input_token={TOKEN}&access_token={TOKEN}`
- **Check:** If `expires_at` is within 7 days, post a warning to `#internal-operations`

---

## Step-by-Step Build Instructions

### Prerequisites

1. **Resolve Google Sheets OAuth** -- This is currently the main blocker. Go to n8n > Credentials > Google Sheets > create new OAuth2 credential following Google's setup guide.
2. **Generate Meta System User Token** -- See [Credentials Required](#credentials-required) section.
3. **Set up Slack Bot** -- Create a Slack app in the TFM workspace with `chat:write` scope. Add the bot to all `#internal-*` channels.
4. **Create Google Spreadsheet** -- Create "TFM Friday Reports -- Automated" with the two sheets described above.

### Build Sequence

**Phase 1: Single client test (30 min)**

1. Create new workflow in n8n: "Friday Ad Report -- Automated"
2. Add Schedule Trigger node (Cron: `0 8 * * 5`, TZ: America/New_York)
3. Add a Code node with JUST the MarketBeat entry from the Client Registry (simplest to test -- single campaign, known data)
4. Add the Date Range Code node
5. Add three HTTP Request nodes for Meta API (this week account-level, last week account-level, this week ad-level)
6. Add the Calculation Code node
7. Test manually by clicking "Execute Workflow" -- verify the data looks correct
8. Compare against Rabii's most recent MarketBeat Friday report in Slack

**Phase 2: Report generation (30 min)**

8. Add the Markdown Generation Code node
9. Add the Slack Message Code node
10. Add Google Sheets Append node
11. Add Slack Send Message node
12. Test: run for MarketBeat, verify Slack message looks correct (post to a test channel first!)
13. Test: verify Google Sheets row is written correctly

**Phase 3: Multi-client loop (30 min)**

14. Expand the Client Registry to include all 21 clients
15. Add SplitInBatches node between Registry and Date Range
16. Add Wait node (2 seconds) after the Slack/Sheets outputs
17. Wire the Wait node back to the SplitInBatches node (loop)
18. Add an IF node to skip clients with `slackChannel: null`
19. Test with 3-4 clients manually

**Phase 4: Error handling + master summary (30 min)**

20. Add error handling: wrap HTTP nodes in try/catch (use n8n's "Continue on Fail" setting on each HTTP node)
21. Add a Code node after the loop ends that collects all results and builds a master summary
22. Add a Slack node to post master summary to `#internal-operations`
23. Add the Error Trigger workflow for token expiry monitoring

**Phase 5: Go live (15 min)**

24. Activate the workflow
25. Let it run on the next Friday
26. Monitor the Slack channels and Google Sheet
27. Adjust any API response parsing issues based on real data

### Total estimated build time: ~2.5 hours

---

## Meta Ads API Reference

### Endpoints Used

| Endpoint | Purpose |
|----------|---------|
| `GET /{account_id}/insights` | Account-level or ad-level performance data |
| `GET /debug_token` | Token expiry check |

### Key Fields

| Field | Description |
|-------|-------------|
| `spend` | Total amount spent |
| `impressions` | Number of times ads were shown |
| `clicks` | Total clicks (all types) |
| `inline_link_clicks` | Clicks on links in the ad (more accurate than `clicks`) |
| `inline_link_click_ctr` | CTR based on link clicks |
| `ctr` | Click-through rate (all clicks) |
| `cpc` | Cost per click |
| `cpm` | Cost per 1,000 impressions |
| `actions` | Array of action objects (leads, purchases, etc.) |
| `cost_per_action_type` | Array of cost-per-action objects |

### Action Types for Newsletter Leads

Most clients use `offsite_conversion.fb_pixel_lead` as the conversion event. Some variations:

| Client | Likely Action Type | Notes |
|--------|-------------------|-------|
| Most clients | `offsite_conversion.fb_pixel_lead` | Standard pixel lead event |
| Stocks.News | `offsite_conversion.fb_pixel_lead` + app installs may use `mobile_app_install` | Check both |
| TPG | `offsite_conversion.fb_pixel_lead` | Client-managed campaigns |
| EH | `offsite_conversion.fb_pixel_lead` | Webinar registrations |

> **Important:** The exact action_type depends on how each client's pixel and conversion events are configured. During Phase 1 testing, inspect the raw `actions` array for each client to confirm the correct action_type. Update the Client Registry accordingly.

### Rate Limits

- Standard Marketing API: 200 calls per hour per ad account
- With 21 accounts and 3 calls each = 63 calls total
- Well within limits even without the Wait node, but keep the delay as a safety margin

---

## Future Enhancements

### Phase 2 Additions (after v1 is stable)

1. **ESP data integration** -- For clients with beehiiv API access, pull open rates and add to reports. This closes the "Open Rate" row in the performance summary table.
2. **Notion page creation** -- Use the Notion API to create Friday report pages in each client's Notion space (currently reports go to Notion manually).
3. **Client-facing Slack posts** -- After GM review, auto-post a client-facing version to `#thefeed-{client}` channels (require manual approval trigger).
4. **Creative fatigue detection** -- Track CTR decay over 3+ weeks per ad. Flag when CTR drops >15% from first-week CTR.
5. **Budget pacing alerts** -- Compare actual spend to `budget_pacing_target` from client config. Fire mid-week alerts (Wednesday) if pacing is >15% off.
6. **MarketBeat ROAS integration** -- Pull from the existing n8n daily ROAS report (partner dashboard scraper) and include ROAS in the MarketBeat Friday report.
7. **Workweek V-CAC calculation** -- If Workweek provides verification data via API or spreadsheet, auto-calculate V-CAC instead of raw CPL.
8. **Insight Links qualified leads** -- Once the Mailchimp n8n workflow is live, pull qualified lead counts and include in the report.
9. **Markdown file write to vault** -- Use n8n's "Write Binary File" node to save the markdown report to a specific path that Obsidian Git syncs. Path: `/reports/friday/{client}/{date}.md`
10. **Competitor comparison** -- For shared accounts (Creator Spotlight, Quartz, Stocks.News, MarketBeat), pull competitor campaign data and include a comparison table.

### Phase 3: AI-Powered Insights

11. **AI summary generation** -- Send the report data to Claude API or OpenAI and generate a 3-sentence executive summary with specific recommendations. Include in both Slack and markdown reports.
12. **Trend detection** -- After 4+ weeks of data in Google Sheets, run weekly trend analysis (is CPL trending up/down over 4 weeks? Is a client's best ad losing steam?).

---

## Appendix: Quick Reference

### n8n Node Types Used

| Node | n8n Type | Count |
|------|----------|-------|
| Schedule Trigger | `n8n-nodes-base.scheduleTrigger` | 1 |
| Code | `n8n-nodes-base.code` | 5 |
| HTTP Request | `n8n-nodes-base.httpRequest` | 3 (per client) |
| SplitInBatches | `n8n-nodes-base.splitInBatches` | 1 |
| Wait | `n8n-nodes-base.wait` | 1 |
| IF | `n8n-nodes-base.if` | 1 |
| Google Sheets | `n8n-nodes-base.googleSheets` | 1 |
| Slack | `n8n-nodes-base.slack` | 2 |

### Key Blockers to Resolve Before Building

| Blocker | Owner | Status |
|---------|-------|--------|
| Google Sheets OAuth setup in n8n | Jay | Blocked (since Mar 17) |
| Meta System User token generation | Jay / Nathan | Not started |
| Slack bot creation + channel access | Jay | Not started |
| Missing client Meta account IDs (1636, FF, SLP, JWS campaign IDs, Vendry campaigns) | Jay | Needs Pipeboard lookup |
| Confirm conversion action_type per client | Jay / Rabii | Needs API inspection |

---

*Document generated 2026-03-21 by Claude Code. Ready for build.*
