# The Feed Media — 6-Category Client Intelligence Framework

## Framework Purpose
Every client file uses this exact structure. Consistent structure = fast parsing, easy comparison across accounts, reliable Claude Code sessions.

---

## Category 1: CLIENT OVERVIEW
**What goes here:** Contacts, internal stakeholders, active status, key links  
**Priority fields:** Primary contact + email, GM assigned, Day AI analysis page URL, Notion page URL, Slack channels  
**Flag if missing:** Contact email, Day AI page link  

---

## Category 2: NORTH STAR METRIC
**What goes here:** The ONE metric that defines success for this client  
**Priority fields:** Metric name + target number, quality definition (what makes a subscriber worth having), client's own words on what "winning" looks like  
**Flag if missing:** Any client who only has CPL as their KPI — dig for downstream metric  
**Key question:** Would optimizing this KPI logically improve the client's actual business?  

---

## Category 3: BRAND VOICE RULES
**What goes here:** Approved and rejected language, tone aspiration, copy feedback patterns  
**Priority fields:** NEVER list first (hardest rules), then USE/APPROVED list, then one client quote about copy that failed  
**Flag if missing:** Any client without a documented copy rejection — they will have one, it just hasn't been captured yet  

---

## Category 4: WINNING CREATIVE SIGNALS
**What goes here:** Formats and angles with documented performance AND positive client reaction  
**Priority fields:** Top 2-3 proven formats, what makes each work (the mechanism), any specific DCT numbers if notable  
**Note:** Performance data alone is insufficient — must have client validation too. CPL-efficient ads that generate bad subscribers are not "winning."  

---

## Category 5: NEGATIVE TRIGGERS
**What goes here:** What has caused explicit negative client reactions, low-quality outcomes, creative kills  
**Priority fields:** Most emotionally charged client quote first, then pattern list  
**Include:** Specific creative kills with reason, copy patterns client has flagged, subscriber quality issues  

---

## Category 6: RELATIONSHIP HEALTH
**What goes here:** Current sentiment, stakeholder map, operational notes  
**Priority fields:** Sentiment trend (improving/stable/at risk), optimal outreach timing, biggest continuity risk, creative involvement preference  
**Flag if missing:** Any recent stakeholder change (transition risk)  

---

## Intelligence Gap Flags

Use these inline flags throughout client files:

- `[GAP: KPI]` — no downstream metric documented, CPL only  
- `[GAP: VOICE]` — no copy rejection pattern on record  
- `[GAP: CREATIVE]` — no validated winning format yet  
- `[GAP: CONTACT]` — contact info incomplete or outdated  
- `[GAP: NOTION]` — Notion page not yet parsed  
- `[RISK: TRANSITION]` — stakeholder change in progress  
- `[RISK: QUALITY]` — CPL is good but subscriber quality concerns raised  

---

## File Header Format

Every client file must start with **YAML frontmatter** followed by the markdown header:

```yaml
---
client: "Client Display Name"
slug: "client-slug"
status: Active | Onboarding | At Risk | Paused
gm: "GM Name"
media_buyer: "Rabii"
esp: "beehiiv | Substack | Kit | Mailchimp | etc."
cpl_target: "$X.XX"
current_cpl: "$X.XX"
risk_level: LOW | MEDIUM | HIGH
sentiment: "Description"
last_enriched: YYYY-MM-DD
---
```

Below the frontmatter:

```
# [CLIENT NAME] — Client Intelligence
**Last Updated:** [Month Year]
**Status:** Active | Onboarding | At Risk | Paused
**Day AI:** [URL]
**Notion:** [URL]
**Slack Internal:** #[channel-name]
**Slack External:** #[channel-name]
```

---

## Deep Enrichment Files

For clients with extensive intelligence, a separate deep enrichment file may exist at:
`clients/[client-name]/[client-name]-deep-enrichment.md`

These files contain extended analysis (sales call transcripts, audience research, competitive intelligence) that supplements the core 6-category file without bloating it.

---

## Source of Truth: Google Drive

Ad scripts, creative briefs, and designer-facing documents live in Google Drive as the shared source of truth. The client intelligence files in this repo track strategy and context; Google Drive holds the production assets and approved scripts that designers and editors work from.
