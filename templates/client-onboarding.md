---
type: onboarding
client: "<% tp.system.prompt("Client name") %>"
slug: "<% tp.system.prompt("Client slug (lowercase-hyphenated)") %>"
date_started: <% tp.date.now("YYYY-MM-DD") %>
gm: "<% tp.system.prompt("Assigned GM") %>"
tags: [onboarding, new-client]
---

# <% tp.system.prompt("Client name") %> — Onboarding Checklist

**Start Date:** <% tp.date.now("YYYY-MM-DD") %>
**GM:** <% tp.system.prompt("Assigned GM") %>

---

## Phase 1: Account Setup (Day 1-2)

### Slack Channels
- [ ] Create #internal-<% tp.system.prompt("Client slug (lowercase-hyphenated)") %>
- [ ] Create #thefeed-<% tp.system.prompt("Client slug (lowercase-hyphenated)") %> (shared with client)
- [ ] Add all TFM team members to internal channel
- [ ] Add client contacts to external channel
- [ ] Post welcome message in external channel

### Notion
- [ ] Create client page from template
- [ ] Build OneSheet (audience research)
- [ ] Create Concept Database
- [ ] Create Creative Database
- [ ] Link to client hub

### Meta Ads
- [ ] Request ad account access (Partner ID: 730307861597413)
- [ ] Verify Meta Pixel is installed on landing page
- [ ] Set up UTM tracking: `?utm_source=facebookads&utm_medium={{adset.name}}&utm_campaign={{ad.name}}`
- [ ] Create exclusion audience (existing subscribers)
- [ ] Verify conversion event is firing

### ESP Access
- [ ] Get ESP login (Beehiiv / Kit / Mailchimp / other)
- [ ] Verify subscriber export capability
- [ ] Set up exclusion list sync process

### Google Drive
- [ ] Create "Creative - [Client Name]" folder
- [ ] Create weekly ad report spreadsheet
- [ ] Share folder with GM + media buyer

---

## Phase 2: Intelligence Gathering (Day 2-5)

### Client Intelligence File
- [ ] Create `clients/[slug]/[slug].md` with 6-category framework
- [ ] Section 1: Client Overview (contacts, ESP, channels, budget)
- [ ] Section 2: North Star Metric (KPI + target + quality definition)
- [ ] Section 3: Brand Voice Rules (NEVER rules first, approved language)
- [ ] Section 4: Winning Creative Signals (formats, hooks, angles)
- [ ] Section 5: Negative Triggers (kills, patterns to avoid)
- [ ] Section 6: Relationship Health (sentiment, risk, continuity)

### Client Config
- [ ] Create `clients/[slug]/client-config.md` with YAML frontmatter

### Research
- [ ] Analyze client landing page (CVR signals, mobile, CTA)
- [ ] Competitor research (3-5 competing newsletters/products)
- [ ] Review client's existing ads (Facebook Ad Library)
- [ ] Read kick-off call recording (Day.ai)

---

## Phase 3: Creative Launch (Day 5-10)

### First Concepts
- [ ] Develop 5 initial concepts using /concept framework
- [ ] Build designer briefs for each concept
- [ ] Submit for internal review
- [ ] Submit for client approval
- [ ] Launch first ads

### Campaign Setup
- [ ] Create CBO campaign in Meta
- [ ] Set up ad sets per concept ($10/day minimum each)
- [ ] Configure Advantage+ Audience (broad) unless client requires interests
- [ ] Set optimization event
- [ ] Double-check exclusion audiences

---

## Phase 4: Reporting & Cadence (Day 10+)

### Communication Setup
- [ ] Schedule bi-weekly client call (Google Calendar)
- [ ] Confirm day/time with client
- [ ] Set up Friday report cadence
- [ ] Create first Friday report
- [ ] Create first bi-weekly prep doc

### Claude Chat Project
- [ ] Build `claude-chat-project.md` with /friday, /bi-weekly, /recap, /concept skills
- [ ] Paste into Claude.ai project

---

## Handoff Notes
*Add any important context for continuity:*

