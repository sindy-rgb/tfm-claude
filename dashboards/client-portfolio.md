# Client Portfolio Dashboard

## All Clients
```dataview
TABLE
  status AS "Status",
  gm AS "GM",
  esp AS "ESP",
  cpl_target AS "CPL Target",
  current_cpl AS "Current CPL",
  risk_level AS "Risk",
  sentiment AS "Sentiment"
FROM "clients"
WHERE client != null
SORT risk_level DESC
```

## At Risk / High Priority
```dataview
TABLE
  client AS "Client",
  gm AS "GM",
  current_cpl AS "CPL",
  sentiment AS "Sentiment"
FROM "clients"
WHERE risk_level = "HIGH" OR risk_level = "MEDIUM-HIGH" OR risk_level = "MODERATE" OR status = "At Risk"
SORT risk_level DESC
```

## By GM Workload
```dataview
TABLE
  client AS "Client",
  status AS "Status",
  risk_level AS "Risk"
FROM "clients"
WHERE client != null
GROUP BY gm
SORT gm ASC
```

## CPL Performance (Over Target)
```dataview
TABLE
  client AS "Client",
  cpl_target AS "Target",
  current_cpl AS "Actual",
  gm AS "GM"
FROM "clients"
WHERE client != null
SORT current_cpl DESC
```

## Recently Enriched
```dataview
TABLE
  client AS "Client",
  last_enriched AS "Last Updated",
  risk_level AS "Risk"
FROM "clients"
WHERE client != null
SORT last_enriched DESC
```
