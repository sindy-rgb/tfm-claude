# Claude Extensions, Connectors & MCP Servers for TFM

**Research date:** 2026-03-21
**Plan:** Claude Max ($200/month)
**Goal:** Maximize value from Claude ecosystem for newsletter growth agency operations

---

## Currently Connected (7 Integrations)

| Integration | What It Does for TFM |
|---|---|
| Day.ai | CRM, meeting recordings, workspace notes |
| Slack | Internal/external client channels |
| Notion | Client pages, SOPs, concepts, creatives, reporting |
| Pipeboard (Meta Ads) | Campaign management, ad creation, insights, audiences |
| Gmail | Client communication, drafts |
| Google Calendar | Meeting scheduling, availability |
| Google Drive | Creative folders, scripts, ad reports |

---

## Priority 1: High-Impact Additions

### 1. n8n MCP Server
**What:** Connect Claude directly to your self-hosted n8n instance to create, manage, and trigger workflows via natural language.
**Top repo:** `leonardsellem/n8n-mcp-server` (1.6k stars)
**Also notable:** `salacoste/mcp-n8n-workflow-builder` (219 stars) -- lets Claude build n8n workflows from natural language descriptions.
**TFM use cases:**
- Claude builds Friday report automation workflows by talking to n8n directly
- Trigger client onboarding sequences from Claude
- Build webhook-based alert workflows (e.g., CPL spikes, budget pacing) without leaving Claude Code
- Manage existing workflows -- pause, modify, debug
**Install:** Local MCP server via npm/pip, configured in Claude Code's MCP settings
**Impact: Very High** -- You already run n8n; this removes the friction of building/managing workflows manually.

### 2. Google Analytics 4 MCP Server
**What:** Query GA4 data directly from Claude -- pageviews, conversion rates, traffic sources, landing page performance.
**Top repo:** `surendranb/google-analytics-mcp` (193 stars, Python)
**Also:** `saurabhsharma2u/search-console-mcp` (66 stars) -- combines GA4 + Google Search Console + Bing Webmaster.
**TFM use cases:**
- Pull landing page CVR data during creative QA (benchmark: 40%+ for newsletters)
- Cross-reference Meta ad traffic with GA4 on-site behavior
- Analyze which UTM campaigns drive highest-quality traffic
- Automate client reporting with real conversion data
- Diagnose landing page issues when CPL rises but CTR is fine
**Install:** Local Python MCP server, requires GA4 API credentials
**Impact: Very High** -- Landing page CVR is a critical metric TFM tracks; having it in-context during media buying decisions is a major upgrade.

### 3. Playwright MCP Server (Browser Automation)
**What:** Full browser automation -- navigate pages, take screenshots, fill forms, scrape content, execute JavaScript.
**Repo:** `executeautomation/mcp-playwright` (well-maintained, npm package)
**Features:** 143 device emulations, screenshot capture, web scraping, JavaScript execution, auto browser install.
**TFM use cases:**
- Screenshot client landing pages for creative QA without leaving Claude
- Test landing page load times and mobile rendering
- Scrape competitor ad libraries (Meta Ad Library)
- Verify UTM parameters are firing correctly on landing pages
- Check that newsletter signup forms work across devices
- Automated visual QA of ad creative mockups
**Install:** `npm install -g @executeautomation/playwright-mcp-server`
**Impact: High** -- Visual QA and landing page verification are frequent TFM tasks.

### 4. Airtable MCP Server
**What:** Read/write Airtable bases from Claude -- query, create, update records.
**Top repo:** `domdomegg/airtable-mcp-server` (429 stars, TypeScript)
**Also:** `rashidazarang/airtable-ai-agent` -- 33 MCP tools for comprehensive Airtable operations.
**TFM use cases:**
- If TFM moves any tracking to Airtable (creative pipelines, client databases)
- Build quick reporting dashboards that pull from structured data
- Sync data between Airtable and Notion
**Impact: Medium** -- Depends on whether TFM adopts Airtable; high if so.

---

## Priority 2: Valuable for Specific Workflows

### 5. Beehiiv MCP Server
**What:** Manage Beehiiv newsletter publications, subscriptions, posts, segments, and automations.
**Top repo:** `mrhinkle/beehiiv-mcp-server` (TypeScript, 34 tools)
**Also:** `danvega/beehiiv-mcp-server` (18 stars, Java)
**TFM use cases:**
- Pull subscriber counts and growth data for Beehiiv clients directly
- Verify subscriber exclusion lists match what's in Meta
- Check post performance and engagement rates
- Cross-reference ESP data with Meta ad performance
**Impact: Medium-High** -- Depends on how many TFM clients use Beehiiv. Direct ESP data access would improve reporting accuracy significantly.

### 6. Mailchimp MCP Server
**What:** Full Mailchimp control -- audiences, campaigns, automations, analytics.
**Top repo:** `damientilman/mailchimp-mcp-server` (53 tools, Python)
**Also:** `livemau5/mailchimp-mcp` (282 endpoints via 2 tools)
**TFM use cases:**
- Pull subscriber lists for exclusion audience syncing
- Check email open rates and engagement for clients using Mailchimp
- Verify newsletter signup confirmation flows
- Cross-reference email engagement with Meta ad acquisition quality
**Impact: Medium** -- Same as Beehiiv; valuable for clients on Mailchimp.

### 7. HubSpot MCP Server
**What:** Interact with HubSpot CRM data -- contacts, deals, companies, pipelines.
**Top repo:** `peakmojo/mcp-hubspot` (117 stars)
**Official:** `HubSpot/mcp-server` (3 stars, but official)
**TFM use cases:**
- If any clients use HubSpot as their CRM, pull conversion/lead data
- Track client relationship data if TFM considers HubSpot for internal CRM
**Impact: Low-Medium** -- TFM uses Day.ai for CRM; only relevant if clients use HubSpot.

### 8. Linear MCP Server
**What:** Project management integration -- create/manage issues, projects, cycles.
**Top repo:** `jerhadf/linear-mcp-server` (347 stars)
**TFM use cases:**
- If TFM adopts Linear for internal project tracking (alternative to Notion tasks)
- Could be useful for structured creative pipeline management
**Impact: Low** -- TFM currently uses Notion for project management.

---

## Priority 3: Claude Code Plugins (Already Available)

These are official plugins from the Claude Code repo that can be installed immediately:

| Plugin | What It Does | TFM Relevance |
|---|---|---|
| **commit-commands** | `/commit`, `/commit-push-pr`, `/clean_gone` | Streamlines vault git workflow |
| **code-review** | Automated PR reviews with 5 parallel agents | Useful for reviewing n8n workflow code, automation scripts |
| **security-guidance** | Detects security issues in code | Protects API keys, tokens in automation scripts |
| **pr-review-toolkit** | Comprehensive PR analysis with 6 specialized agents | For any code changes to TFM automation |

**Install:** Via `/plugin` command in Claude Code or configure in `.claude/settings.json`

---

## Priority 4: Claude Max Plan Features to Maximize

### What Max ($200/month) Includes
- **20x more usage** than Pro ($20/month) plan
- **Access to all models:** Claude Opus 4, Claude Sonnet 4, Haiku
- **Extended thinking:** Longer, deeper reasoning chains -- use this for complex media buying analysis, multi-client strategy sessions
- **Projects:** Shared project spaces with custom instructions (you're already using this via CLAUDE.md)
- **Artifacts:** Interactive code, documents, and visualizations in chat
- **MCP integrations:** All 7 currently connected, plus ability to add more
- **Claude Code:** Included with Max -- terminal-based agent (what you're using now)
- **Priority access:** During high-traffic periods
- **Early access:** To new features and models

### Features You Should Be Using More
1. **Extended thinking** -- For complex multi-variable decisions (budget allocation across 25 clients, creative strategy pivots)
2. **Projects with team sharing** -- Could share TFM project with team members if they get Pro/Max seats
3. **Artifacts** -- Generate interactive dashboards, client presentation slides, creative briefs as artifacts
4. **Multiple model switching** -- Use Opus for deep analysis, Haiku for quick tasks to stay within limits

---

## Priority 5: GitHub + Claude Integration

### Claude GitHub App
**What:** Runs Claude Code directly from GitHub PRs and Issues. Acts as a virtual teammate.
**Capabilities:**
- Responds to PR reviewer feedback automatically
- Fixes CI errors on PRs
- Modifies code based on issue discussions
- Works as an automated code reviewer
**TFM use case:** If TFM's `tfm-vault` repo gets more complex automation code (n8n configs, scripts), this auto-reviews changes.
**Setup:** Install from github.com/apps/claude on the `thefeedmedia/tfm-vault` repo.
**Impact: Low-Medium** -- More useful if TFM builds more code-based automation.

### GitHub Actions with Claude
- Use Claude API in GitHub Actions to auto-generate commit summaries
- Auto-QA markdown files in vault for formatting/consistency
- Trigger Claude analysis on push (e.g., validate client intelligence files)

---

## Priority 6: Obsidian + AI Integrations

### Smart Connections (Already Available)
**What it does:**
- Surfaces semantically related notes using AI embeddings
- **Connections View:** Shows notes related to current note, ranked by similarity
- **Lookup View:** Semantic search across entire vault
- **Smart Context:** Copy connected content to clipboard for AI context
- Works with Claude, ChatGPT, Gemini APIs or local models
- Privacy-first: runs locally by default
**TFM use cases:**
- When writing creative for Client X, automatically surface winning signals from similar clients
- Find cross-client patterns (what works for finance newsletters might work for investing newsletters)
- Surface relevant SOPs and frameworks when working on specific tasks
**Impact: Medium-High** -- Your vault has deep client intelligence; semantic connections would surface insights humans miss.

### Obsidian Copilot Plus (Already Purchased)
**Capabilities to leverage:**
- Chat with your vault using Claude as the backend
- Summarize notes, generate content from vault context
- Cross-reference multiple notes in conversation
- Use as a quick-lookup tool for team members who don't use Claude Code

### Other Notable Obsidian AI Plugins
- **Text Generator** -- Generate/rewrite text in notes using AI APIs
- **AI Assistant** -- Chat interface within Obsidian
- **Templater + AI** -- Auto-populate templates with AI-generated content (useful for client file creation)

---

## Priority 7: Automation Opportunities

### n8n + Claude API Workflows (High Priority)
You already have n8n self-hosted. Key automations to build:

1. **Friday Report Automation**
   - Trigger: Cron (Friday morning)
   - Steps: Pull Meta Ads data via API -> Claude API summarizes performance -> Posts to Notion -> Sends Slack notification

2. **Creative QA Pipeline**
   - Trigger: New Google Drive file in creative folder
   - Steps: Claude API analyzes creative against client NEVER rules -> Flags issues in Slack -> Updates Notion status

3. **Client Intelligence Auto-Update**
   - Trigger: After client call (Day.ai meeting recording)
   - Steps: Claude API extracts key updates from transcript -> Updates client intelligence file -> Alerts GM in Slack

4. **CPL Alert System**
   - Trigger: Daily cron
   - Steps: Pull Meta Ads CPL data -> Compare against client benchmarks -> Alert in Slack if > 20% above target

5. **Landing Page CVR Monitor**
   - Trigger: Daily cron
   - Steps: Pull GA4 data -> Check newsletter signup CVR -> Alert if below 40% threshold

### Webhook-Based Integrations
- n8n webhook -> Claude API -> Slack/Notion for any event-driven workflow
- Meta Ads webhook (via Pipeboard) -> n8n -> Claude analysis -> Team alerts

---

## Summary: Recommended Installation Order

| Priority | Integration | Effort | Impact |
|---|---|---|---|
| 1 | n8n MCP Server | Medium (config n8n API) | Very High |
| 2 | Google Analytics 4 MCP | Medium (GA4 API creds) | Very High |
| 3 | Playwright MCP | Low (npm install) | High |
| 4 | Beehiiv MCP Server | Low-Medium | Medium-High (if clients use it) |
| 5 | Mailchimp MCP Server | Low-Medium | Medium (if clients use it) |
| 6 | Claude GitHub App | Low (one-click install) | Medium |
| 7 | Claude Code plugins (commit-commands, security) | Low | Medium |
| 8 | Smart Connections (Obsidian) | Low (already available) | Medium-High |
| 9 | Airtable MCP | Low | Medium (if adopted) |
| 10 | n8n + Claude API automations | High (building workflows) | Very High |

---

## Not Yet Available (Watch List)

These don't have mature MCP servers yet but would be valuable when they appear:

| Tool | Why TFM Wants It |
|---|---|
| **ConvertKit / Kit MCP** | Several newsletter clients likely use Kit |
| **Frame.io MCP** | TFM uses Frame.io V4 for creative review |
| **Adobe Creative Cloud MCP** | Direct creative asset management |
| **Meta Business Suite MCP** (beyond Pipeboard) | Page management, organic content |
| **Stripe MCP** | If TFM ever tracks client revenue attribution |
| **Zapier/Make MCP** | Alternative automation platforms (less needed since TFM uses n8n) |

---

## Quick-Start: Install Top 3 Today

### 1. Playwright MCP (5 minutes)
```bash
npm install -g @executeautomation/playwright-mcp-server
```
Then add to Claude Code MCP config.

### 2. n8n MCP Server (15 minutes)
```bash
# Clone and configure
git clone https://github.com/leonardsellem/n8n-mcp-server
# Set N8N_API_URL to your Elestio instance
# Set N8N_API_KEY from n8n settings
```
Add to Claude Code MCP config pointing to your n8n instance at `https://n8n-zwzfv-u62151.vm.elestio.app/`

### 3. Google Analytics 4 MCP (20 minutes)
```bash
pip install google-analytics-mcp
# Requires: GA4 property ID + Google Cloud service account with Analytics API enabled
```

---

*This research will be updated as new MCP servers mature. Check github.com/modelcontextprotocol/servers and mcp.so periodically for new additions.*
