# Weekly Review Dashboard

## Open Tasks Across All Clients
```tasks
not done
sort by due
group by filename
```

## Clients Needing Attention This Week
```dataview
TABLE
  client AS "Client",
  risk_level AS "Risk",
  sentiment AS "Sentiment",
  gm AS "GM"
FROM "clients"
WHERE risk_level = "HIGH" OR risk_level = "MEDIUM-HIGH" OR risk_level = "MEDIUM" OR status = "At Risk"
SORT risk_level DESC
```

## Deep Enrichment Status
```dataview
TABLE
  client AS "Client",
  last_enriched AS "Last Enriched"
FROM "clients"
WHERE client != null
SORT last_enriched ASC
```
