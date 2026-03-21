# Quartz Delivra API v2 — Root Cause Analysis & New Approach

*Generated: March 21, 2026*

---

## 1. WHAT WAS WRONG WITH THE PREVIOUS APPROACH

### The Bug: No Pagination

Every single code file (`delivra-n8n-final.js`, `delivra-n8n-code.js`, `delivra-n8n-all-in-one.js`, etc.) calls the endpoint the same way:

```
GET /Categories/{category_id}/Contacts
```

**With zero query parameters.** No `pageSize`, no `pageNumber`.

The Delivra API documentation confirms that `/Categories/{categoryNameOrId}/Contacts` accepts:
- `pageSize` (Int32, Optional) — *"The requested page size. Maximum of 10,000."*
- `pageNumber` (Int32, Optional) — *"The page number to retrieve."*

**When you omit these parameters, the API returns its default page size** — which appears to be ~100 contacts. That is exactly why the code was only pulling ~100 subscribers. The API was returning page 1 of N, and the code never asked for page 2.

This is a classic pagination bug. The code treats the response as a complete dataset (`allContacts = Array.isArray(resp) ? resp : []`) when it is actually just the first page.

### Secondary Issue: No Date-Range Endpoint Used

The API has a purpose-built endpoint for exactly what we need:

```
GET /Categories/{categoryNameOrId}/Contacts/JoinRange?startDate=...&endDate=...&pageSize=10000&pageNumber=1
```

This returns contacts who joined the category within a date range — exactly what the "bakeoff contacts" filter was trying to do client-side by looping through DateJoined values. Using this endpoint would be faster, more accurate, and server-side filtered.

### Third Issue: Individual Contact Detail Lookups Are Wasteful

The code samples 50-100 contacts and makes individual `GET /Contacts/{MemberID}` calls to check MemberType and Engagement. This is slow (50+ sequential HTTP calls) and gets rate-limited. The Reports endpoints provide this data in bulk.

---

## 2. THE NEW APPROACH

### Strategy A: Fix Pagination on Category Contacts (Quick Win)

Replace the unpaginated call with a loop that fetches all pages:

```javascript
// n8n Code Node — Paginated Category Contacts
var BASE_URL = "https://integration.delivra.com/DelivraRESTServices/Services.svc";
var USERNAME = "aroggio+newsletter-ops@qz.com";
var PASSWORD = "N3ws-Qu@rtz-Ops";
var LISTNAME = "quartz-prod";
var PAGE_SIZE = 10000; // API maximum

var AGENCIES = [
  { name: "TFM", category_id: 623803, category_name: "feed-media" },
  { name: "BG", category_id: 623802, category_name: "boletin" },
  { name: "GL", category_id: 601833, category_name: "paid-acquisition" }
];

var results = [];
var today = new Date().toISOString().split("T")[0];

for (var i = 0; i < AGENCIES.length; i++) {
  var agency = AGENCIES[i];
  var allContacts = [];
  var pageNumber = 1;
  var keepGoing = true;

  while (keepGoing) {
    try {
      var resp = await $http.request({
        method: "GET",
        url: BASE_URL + "/Categories/" + agency.category_id + "/Contacts"
          + "?pageSize=" + PAGE_SIZE
          + "&pageNumber=" + pageNumber,
        headers: {
          "username": USERNAME,
          "password": PASSWORD,
          "listname": LISTNAME
        },
        json: true
      });

      var page = Array.isArray(resp) ? resp : [];
      allContacts = allContacts.concat(page);

      if (page.length < PAGE_SIZE) {
        keepGoing = false; // Last page
      } else {
        pageNumber++;
      }
    } catch (err) {
      keepGoing = false;
    }
  }

  // Filter to bakeoff period
  var bakeoffContacts = allContacts.filter(function(c) {
    var joined = (c.DateJoined || "").substring(0, 10);
    return joined >= "2026-02-01" && c.MemberID_ !== 0;
  });

  results.push({
    json: {
      date: today,
      agency: agency.name,
      category: agency.category_name,
      total_in_tag: allContacts.length,
      bakeoff_subs: bakeoffContacts.length
    }
  });
}

return results;
```

### Strategy B: Use JoinRange Endpoint (Better)

Skip client-side date filtering entirely. Use the server-side date-range endpoint:

```javascript
// Use the JoinRange endpoint — server-side date filtering + pagination
var startDate = "2026-02-01";
var endDate = new Date().toISOString().split("T")[0];

var url = BASE_URL + "/Categories/" + agency.category_id + "/Contacts/JoinRange"
  + "?startDate=" + startDate
  + "&endDate=" + endDate
  + "&pageSize=10000"
  + "&pageNumber=1";

var resp = await $http.request({
  method: "GET",
  url: url,
  headers: {
    "username": USERNAME,
    "password": PASSWORD,
    "listname": LISTNAME
  },
  json: true
});
// This returns ONLY contacts who joined during the bakeoff period
```

### Strategy C: Use Reports Endpoints for Broadcast Data (The Real Answer)

The original investigation found that 80.5% of TFM subs never received a broadcast. Instead of checking individual contacts, query the Reports service for broadcast-level engagement data:

```javascript
// Step 1: Get all sent mailings during the bakeoff period
var mailingsUrl = BASE_URL + "/Mailings/Sent"
  + "?startDate=2026-02-01"
  + "&endDate=2026-03-21"
  + "&pageSize=10000"
  + "&pageNumber=1";

var mailings = await $http.request({
  method: "GET",
  url: mailingsUrl,
  headers: { "username": USERNAME, "password": PASSWORD, "listname": LISTNAME },
  json: true
});

// Step 2: For each mailing, get the Sends (who was sent the email)
for (var m = 0; m < mailings.length; m++) {
  var mailingId = mailings[m].MessageID; // or whatever the ID field is

  var sendsUrl = BASE_URL + "/Reports/" + mailingId + "/Sends"
    + "?pageSize=10000&pageNumber=1";

  var sends = await $http.request({
    method: "GET",
    url: sendsUrl,
    headers: { "username": USERNAME, "password": PASSWORD, "listname": LISTNAME },
    json: true
  });

  // Step 3: Get Opens for that mailing
  var opensUrl = BASE_URL + "/Reports/" + mailingId + "/Opens"
    + "?pageSize=10000&pageNumber=1";

  var opens = await $http.request({
    method: "GET",
    url: opensUrl,
    headers: { "username": USERNAME, "password": PASSWORD, "listname": LISTNAME },
    json: true
  });

  // Cross-reference sends against TFM subscriber list to see who was/wasn't sent
}
```

This approach answers the core question: "Which broadcasts were sent to TFM subscribers, and what were their open/click rates?" — without relying on the per-contact Engagement score field.

### Strategy D: Account-Wide Reports (Broadest View)

Use the account-wide report endpoints to get all engagement events during the bakeoff:

```javascript
// All sends across the account in the bakeoff period
var allSends = await $http.request({
  method: "GET",
  url: BASE_URL + "/Reports/Sends?startDate=2026-02-01&endDate=2026-03-21&pageSize=10000&pageNumber=1",
  headers: { "username": USERNAME, "password": PASSWORD, "listname": LISTNAME },
  json: true
});

// All opens
var allOpens = await $http.request({
  method: "GET",
  url: BASE_URL + "/Reports/Opens?startDate=2026-02-01&endDate=2026-03-21&pageSize=10000&pageNumber=1",
  headers: { "username": USERNAME, "password": PASSWORD, "listname": LISTNAME },
  json: true
});

// All clicks
var allClicks = await $http.request({
  method: "GET",
  url: BASE_URL + "/Reports/Clickthroughs?startDate=2026-02-01&endDate=2026-03-21&pageSize=10000&pageNumber=1",
  headers: { "username": USERNAME, "password": PASSWORD, "listname": LISTNAME },
  json: true
});
```

Then cross-reference these event lists with the TFM subscriber MemberIDs to compute:
- How many TFM subs were sent at least one broadcast
- How many opened
- How many clicked
- Per-broadcast engagement rates for TFM vs BG vs GL

---

## 3. ADDITIONAL ENDPOINTS WE MISSED

| Endpoint | What It Gives Us |
|----------|-----------------|
| `/Contacts/ContactCountByStatus` | Quick count of active/held/unsub without sampling |
| `/Contacts/JoinRange` | All contacts who joined in a date range (account-wide) |
| `/Contacts/HeldRange` | Contacts held in a date range |
| `/Contacts/ListModified` | Recently modified contacts since a given date |
| `/Reports/SubscriberActivity` | Contact activity statistics for a date range |
| `/Reports/{mailingID}/FullOpens` | Detailed open events (includes contact identifiers) |
| `/Reports/{mailingID}/Clickstream` | Full clickstream data per mailing |
| `/Reports/{mailingID}/Successes` | Success events per mailing |
| `/Segments` | List all segments — could reveal if there are segments beyond categories |

---

## 4. RECOMMENDED IMPLEMENTATION PLAN

### Phase 1: Fix the Count (30 minutes)
1. Deploy Strategy A (paginated category contacts) to n8n
2. Run it once for all 3 agencies
3. Compare `total_in_tag` with the old ~100 number
4. This immediately tells us if pagination was the issue

### Phase 2: Broadcast Analysis (1-2 hours)
1. Deploy Strategy C (Reports endpoints) to n8n
2. Get the list of all sent mailings during bakeoff period
3. For each mailing, pull Sends and Opens
4. Cross-reference with TFM/BG/GL subscriber lists
5. Build a per-broadcast view: "Mailing X was sent to Y TFM subs, Z opened"
6. This definitively answers whether Quartz is sending broadcasts to TFM subs

### Phase 3: Automated Daily Tracker (1 hour)
1. Combine Phase 1 + Phase 2 into a single n8n workflow
2. Schedule daily at 8am ET
3. Post results to #internal-quartz
4. Track trends over time

### Fallback: Playwright Dashboard Scraping
If the API still returns incomplete data (auth issues, permission scoping), use Playwright MCP to:
1. Log into Delivra's web dashboard
2. Navigate to the segment/category views
3. Screenshot the subscriber counts
4. Extract the numbers from the UI

This is a last resort but would bypass any API-level data restrictions.

---

## 5. WHAT TO TELL ARMANDO

If the paginated API confirms that TFM has significantly more subscribers than the ~100 originally returned:

> "We identified a pagination issue in our initial API integration that was causing us to only retrieve the first page of subscriber data. We've corrected this and can now see the full picture. We'd like to share our updated analysis — and separately, we've built a broadcast-level engagement tracker using the Reports API that can show exactly which mailings were sent to our subscribers and their open/click rates."

This positions TFM as technically sophisticated and proactive — reinforcing the "most data-driven agency" narrative from Jay's original Delivra analysis.

---

*Next step: Deploy Strategy A to n8n and run it. If it returns significantly more than ~100 contacts for TFM, the pagination fix is confirmed and we move to Phase 2.*
