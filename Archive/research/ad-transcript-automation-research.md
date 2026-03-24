# Ad Transcript Automation Research
## From "Top Spending Meta Ads" to "Transcribed Scripts with Customer Language" — Automatically

**Date:** 2026-03-16
**Purpose:** Evaluate all viable paths to programmatically pull video ad transcripts from competitor/top-performing Meta ads at scale, replacing the current manual workflow (Foreplay > download > transcribe > AI).

---

## TL;DR RECOMMENDATION

**Foreplay API is the clear winner.** It already has transcripts built into the ad object (`full_transcription` + `timestamped_transcription`), covers 100M+ ads, costs 1 credit per ad (10,000-20,000 free/month on existing plans), has a working n8n integration path, and an MCP server available via Gumloop. You can skip the transcription step entirely.

**Recommended stack:** Foreplay API (search + transcripts) > n8n or Claude Code slash command > Claude for customer language extraction and concept ideation.

---

## 1. FOREPLAY API

### What It Does
- Full REST API with access to **100M+ ads** across Meta and TikTok
- **Transcripts are a built-in field** — no separate transcription step needed
- Search by keyword, domain, niche, platform, format, language, running duration
- Sort by `longest_running` (proxy for top-performing/highest spend)
- Filter by `display_format: video`, `live: true`, `publisher_platform`, date ranges

### Key Ad Object Fields for TFM's Use Case
| Field | What It Returns |
|---|---|
| `full_transcription` | Complete transcribed text of the video ad |
| `timestamped_transcription` | Array of `{startTime, endTime, sentence}` objects |
| `headline` | Main ad copy |
| `description` | Body text |
| `cta_title` / `cta_type` | Call-to-action |
| `video` | Direct video URL |
| `emotional_drivers` | Detected emotional elements (AI-enriched) |
| `niches` | Industry/category tags |
| `running_duration` | Days running (proxy for performance) |
| `live` | Currently active (boolean) |
| `link_url` | Landing page URL |
| `ad_library_url` | Direct link to Meta Ad Library |

### API Endpoints
- `GET /api/ad` — Single ad by ID (with all fields above)
- `GET /api/spyder/brand/ads` — All ads from a tracked brand (cursor-based, max 250/page)
- `GET /api/board/ads` — Ads from your saved boards
- `GET /api/brand/getAdsByBrandId` — Ads from multiple brands
- `GET /api/brand/getAdsByPageId` — Ads by Facebook Page ID
- `GET /api/brand/getBrandsByDomain` — Find brands by domain
- **Search/Discovery endpoint** — Search all 100M+ ads by keyword, niche, filters

### Authentication
- API key in `Authorization` header
- Keys generated at https://app.foreplay.co/api-overview

### Pricing
| Plan | Monthly Cost | API Credits/Month | Notes |
|---|---|---|---|
| Basic (monthly) | $59 | 10,000 | 1 credit = 1 ad (all fields included) |
| Basic (annual) | $49/mo | 20,000 | |
| Workflow (monthly) | $175 | 10,000 | 5 users, 15 Spyder brands |
| Workflow (annual) | $149/mo | 20,000 | Unlimited Spyder brands |
| Agency (monthly) | $459 | 10,000 | 10 users, 50 Spyder brands |
| Agency (annual) | $389/mo | 20,000 | Unlimited Spyder brands |
| Enterprise | Custom | Custom | Volume discounts available |

**Cost per transcript:** Effectively $0 incremental — transcripts come bundled with every ad pull. At 10,000 credits/month, that's 10,000 ad transcripts for $0 extra beyond your plan cost.

Additional credits beyond the monthly allotment: pricing not publicly listed — contact Foreplay for volume/enterprise pricing.

### Integration Options
1. **n8n HTTP Request node** — Direct API calls, Foreplay has published n8n workflow examples
2. **Gumloop MCP server** — Foreplay has an official guMCP server with search, brand analytics, and ad retrieval actions
3. **Zapier MCP** — Also available through Zapier's MCP ecosystem
4. **Claude Code** — Direct HTTP calls via bash/scripts, or via MCP server integration
5. **Activepieces** — Community request for native integration exists

### Pros
- **Transcripts are already done** — no transcription API needed
- **Timestamped transcripts** available for hook analysis
- **Emotional drivers** AI-enriched field for customer language extraction
- **100M+ ad database** — massive coverage
- **Sort by longest_running** = proxy for highest spend/best performing
- Already integrated with n8n ecosystem
- MCP server available for Claude Code integration
- 10,000-20,000 free credits/month on existing plans
- TFM likely already has a Foreplay account

### Cons
- No direct "top ad spend" sort — `longest_running` is the best proxy
- 10,000 credits/month may not be enough for large-scale scraping (but fine for targeted research)
- Transcript quality depends on Foreplay's transcription engine (not Whisper-level accuracy guaranteed)
- Manual uploads not returned via API
- No carryover of unused credits month to month

### Limitations
- Max 250 results per page
- Rate limiting (429 responses) — requires exponential backoff
- Transcription field may be null for some older or image-only ads

---

## 2. META AD LIBRARY API / MARKETING API

### What It Does
- Official Meta API for accessing the Ad Library
- Returns ad metadata: page name, spend ranges, impressions, `ad_snapshot_url`, publisher platforms
- The `ad_snapshot_url` links to a rendered preview page — NOT a direct video file

### What It Does NOT Do
- **Does NOT return video files directly** — only snapshot URLs
- **Does NOT provide transcripts**
- **Does NOT return creative assets as downloadable files**
- To get the actual video, you must scrape/parse the `ad_snapshot_url` page

### Access Level Requirements
- **Critical limitation (2026):** The Meta Ad Library API only provides access to **political/social issue ads running in EU countries**
- For commercial ads (which is what TFM needs), the API is essentially useless
- Requires Facebook account with political ads verification
- Standard Marketing API access (which TFM has via Pipeboard) covers your OWN ads, not competitors'

### Workarounds
- **AdDownloader** (open-source Python CLI) — automates the snapshot URL scraping process, but still limited to the API's scope restrictions
- **Apify scrapers** — can scrape the Ad Library web UI, but fragile and against ToS
- Chrome extensions exist for manual one-by-one downloads

### Pricing
- Free (Meta API)
- But effectively non-functional for TFM's use case (commercial ads, US market)

### Integration with Existing Pipeboard MCP
- Pipeboard MCP gives access to **your own ad accounts** (campaign management, insights, etc.)
- It does NOT provide competitor ad library access
- Separate tools/APIs entirely

### Pros
- Free
- Official Meta data source

### Cons
- **Fundamentally limited** — no access to commercial competitor ads in the US
- No video file downloads in API responses
- No transcripts
- Would still need a separate transcription step even if you got the videos
- Scraping workarounds are fragile and against Meta ToS

### Verdict: NOT VIABLE for TFM's use case

---

## 3. DIRECT TRANSCRIPTION TOOLS/APIs

These would only be needed if you had video files/URLs but no transcripts. Since Foreplay already includes transcripts, these become **fallback options** or for transcribing your own creative.

### OpenAI Whisper API
| Attribute | Detail |
|---|---|
| Price | $0.006/min ($0.36/hr) — or GPT-4o Mini at $0.003/min |
| Input | Audio file upload (max 25MB) — does NOT accept URLs |
| Languages | 99 languages |
| Accuracy | 94-96% |
| Free credits | $5 (~833 minutes) |
| Limitation | Must download video, extract audio, chunk if >25MB |
| n8n integration | Yes, via OpenAI node |

### AssemblyAI
| Attribute | Detail |
|---|---|
| Price | $0.15/hr ($0.0025/min) — cheapest option |
| Input | **Accepts publicly accessible URLs** — no download needed |
| Languages | 18+ |
| Accuracy | 96-98% (best for pre-recorded) |
| Free credits | $50 |
| Extras | Speaker diarization (+$0.02/hr), sentiment analysis |
| n8n integration | Available via HTTP Request node |

### Deepgram (Nova-3)
| Attribute | Detail |
|---|---|
| Price | $0.0043/min pre-recorded ($0.258/hr) — or $0.0077/min streaming |
| Input | Accepts URLs or file upload |
| Accuracy | 95%+ |
| Free credits | $200 (~45,000 minutes) |
| Billing | Per-second (no rounding) |
| n8n integration | Available |

### Rev.ai
| Attribute | Detail |
|---|---|
| Price | ~$0.02/min |
| Input | File upload or URL |
| Free | 5 hours free |

### Pricing Comparison for 1,000 30-second ads (500 total minutes)
| Service | Cost |
|---|---|
| **Foreplay (built-in)** | **$0 (500 credits from existing plan)** |
| AssemblyAI | $1.25 |
| Deepgram | $2.15 |
| Whisper (GPT-4o Mini) | $1.50 |
| Whisper (standard) | $3.00 |

### Verdict
Transcription APIs are cheap and effective, but unnecessary if using Foreplay API (which already includes transcripts). They become relevant if:
- You need higher-accuracy transcripts than Foreplay provides
- You're transcribing your own creative (not competitor ads)
- You're pulling videos from a source that doesn't include transcripts

---

## 4. OTHER COMPETITOR AD INTELLIGENCE TOOLS

### Atria
- **25M+ ads** from Meta and TikTok
- **Has video transcript extraction** built into the platform
- **Review mining** feature — extracts customer language from reviews
- **API access: Enterprise only** (not on Core/Plus/Business plans)
- **Pricing:** $129-$479/month depending on plan
- **Tracks up to 200 competitor brands** with real-time alerts
- **No public API for lower tiers** — major limitation
- **Verdict:** Good product but no programmatic access unless Enterprise. Cannot build automations around it.

### MagicBrief
- Auto-transcribes every video ad saved to the platform
- Natural language search across transcripts
- One-click transcript download
- Automatically extracts hooks, CTAs, and copy from winning video ads
- **No public API documented**
- **Verdict:** Good for manual research, not for automation pipelines.

### AdSpy
- Largest Facebook/Instagram ad database (150M+ ads)
- Search by keyword, URL, ad text, comments
- **No transcript feature**
- **No API** — web interface only
- $149/month
- **Verdict:** No transcripts, no API. Not useful for this workflow.

### BigSpy
- 1B+ ad creatives across 10 platforms
- Free tier available
- **No transcript feature documented**
- **No API** documented
- **Verdict:** Volume but no transcription or API access.

### Minea
- Focused on dropshipping/ecommerce product research
- Facebook, Instagram, TikTok, Pinterest ads
- **No transcript feature**
- **No API**
- Starts at $49/month
- **Verdict:** Wrong use case for newsletter growth. No transcripts.

### Motion
- Creative analytics platform (performance reporting)
- Connects to your own ad accounts
- **Not a competitor ad spy tool** — analyzes your own creative performance
- No competitor ad transcripts
- **Verdict:** Complementary tool for analyzing TFM's own ads, not for competitor research.

---

## 5. PARKER.AI (heyparker.ai)

### What It Does
- AI Creative Strategist/Director — not primarily an ad scraping tool
- Analyzes reviews, trends, and competitors to generate ad concepts
- Generates production-ready scripts from video ads ("one click to turn any video into a script")
- Slack integration for daily creative performance summaries
- Autonomous research — scans TikTok for winning ads while you sleep
- Custom workflow templates (weekly performance reviews, iteration reports)
- Trained on "thousands of winning ads and hundreds of pages of direct-response SOPs"

### How Parker Likely Works (Inferred)
- Appears to combine ad library data (likely from Meta/TikTok APIs or a provider like Foreplay) with transcription and AI analysis
- The "one click video to script" feature suggests built-in transcription
- Review mining from public sources (Amazon, app stores, etc.)
- AI layer (likely GPT-based) for concept generation and script writing

### Pricing
- **Custom pricing** — tiers based on your ad spend
- No public pricing page with dollar amounts
- "Let's talk through pricing that fits your needs" — sales-led

### API Access
- **No public API documented**
- Slack integration is the primary programmatic touchpoint
- No n8n or webhook integrations documented

### Pros
- Most "turnkey" solution — handles the full pipeline internally
- Slack integration fits TFM's workflow
- Script generation + concept ideation built in
- Trained on direct-response best practices

### Cons
- **Black box** — you don't control the pipeline or data sources
- **No API** — can't integrate into custom n8n workflows or Claude Code commands
- **Custom pricing** — likely expensive for agency use across 15+ clients
- **Can't customize the AI prompts** — stuck with Parker's interpretation of "good creative"
- Not clear if it covers newsletter-specific ad creative (likely focused on ecommerce/DTC)

### Verdict
Parker is the closest to what TFM wants as a finished product, but without API access, you can't integrate it into your own workflows. Building a Foreplay API + Claude pipeline gives you the same capability with full control.

---

## 6. CREATIVE AUTOMATION PLATFORMS (Combined Pull + Transcribe)

### Foreplay + n8n (DIY)
- **Best option for TFM** — Foreplay API returns transcripts, n8n orchestrates the workflow
- Existing n8n workflow templates available
- n8n already running at TFM: `https://n8n-zwzfv-u62151.vm.elestio.app/`
- Example workflow: Scheduled trigger > Foreplay API search (keyword + longest_running + video) > Extract transcripts > Claude API for customer language analysis > Slack/Notion output

### Foreplay + Claude Code Slash Command (DIY)
- Build a `/competitor-scripts` slash command
- Uses Foreplay API directly from Claude Code
- Immediate analysis without leaving the terminal
- Could use Foreplay's guMCP server for native integration

### Descript + n8n
- Descript has n8n integration for video/audio transcription
- But requires video files as input — doesn't solve the "pulling competitor ads" step
- Better for transcribing TFM's own creative content

### Creatomate + n8n
- Video automation platform with n8n integration
- Focused on video creation/editing, not competitor analysis
- Can auto-add subtitles using transcription
- Not useful for the competitor ad transcript use case

### Apify + n8n + Transcription API
- Apify actors can scrape Meta Ad Library web UI
- Fragile, against Meta ToS, requires maintenance
- Would then need a separate transcription step
- **Not recommended** — Foreplay already solved this

---

## RECOMMENDED ARCHITECTURE FOR TFM

### Option A: n8n Workflow (Best for Scale + Automation)

```
[Scheduled Trigger or Manual Trigger]
        |
        v
[Foreplay API: Search ads]
  - query: "{client niche keywords}"
  - display_format: "video"
  - order: "longest_running"
  - live: true
  - limit: 50
        |
        v
[Extract: full_transcription, headline, description, emotional_drivers, link_url]
        |
        v
[Claude API: Analyze transcripts]
  - Extract customer language patterns
  - Identify winning hooks and angles
  - Map emotional drivers to client brand voice
  - Generate 5-10 concept briefs
        |
        v
[Output to Slack/Notion]
  - Post to #internal-{client} channel
  - Or create Notion page in client's concepts database
```

**Cost:** ~50-250 credits per run (included in existing plan) + Claude API costs (~$0.05-0.20 per analysis)

### Option B: Claude Code Slash Command (Best for On-Demand Research)

Build a `/competitor-scripts {niche}` command that:
1. Calls Foreplay API with niche keywords
2. Pulls top 20-50 longest-running video ads
3. Extracts transcripts + emotional drivers
4. Runs Claude analysis for customer language patterns
5. Outputs structured concept brief

**Cost:** Same credit usage, instant results in terminal

### Option C: Foreplay MCP Server (Most Integrated)

- Add Foreplay guMCP server to Claude Code's MCP config
- Natural language queries: "Find the top 50 longest-running video ads in the personal finance newsletter niche and analyze their scripts for winning hooks"
- Claude handles the entire pipeline conversationally

---

## COST COMPARISON: FULL PIPELINE

| Approach | Monthly Cost | Setup Effort | Automation Level |
|---|---|---|---|
| **Foreplay API + n8n + Claude** | $49-149/mo (Foreplay) + ~$5-20 Claude API | Medium (2-4 hours) | Fully automated |
| **Foreplay API + Claude Code** | $49-149/mo (Foreplay) | Low (1-2 hours) | On-demand |
| **Foreplay MCP + Claude Code** | $49-149/mo (Foreplay) | Low (30 min) | Conversational |
| **Parker.ai** | Unknown (custom, likely $200-500+) | None | Semi-automated (Slack) |
| **Atria Enterprise** | $479+/mo | Low | Limited API |
| **Meta API + Whisper + n8n** | Free (Meta) + ~$3/1000 ads | High (10+ hours) | Fragile, limited scope |
| **Manual (current)** | Time cost only | None | 0% automated |

---

## NEXT STEPS

1. **Confirm TFM's current Foreplay plan** — Check if API access is active and how many credits are available
2. **Test the Foreplay API** — Pull a sample of 10-20 video ads in a newsletter niche, verify transcript quality
3. **Build Option C first** (Foreplay MCP in Claude Code) — fastest to validate the concept
4. **Then build Option A** (n8n workflow) — for automated weekly competitor script analysis per client
5. **Create a Claude prompt template** for customer language extraction from transcripts — tailored to newsletter growth/subscriber acquisition angles

---

## SOURCES

- [Foreplay API Landing Page](https://www.foreplay.co/api)
- [Foreplay API Documentation](https://public.api.foreplay.co/docs)
- [Foreplay API Launch Blog Post](https://www.foreplay.co/post/api-launch)
- [How to Search Ads Using the Foreplay API](https://www.foreplay.co/post/how-to-search-ads-using-the-foreplay-api)
- [Foreplay Pricing](https://www.foreplay.co/pricing)
- [Foreplay guMCP Server](https://www.gumloop.com/mcp/foreplay)
- [Foreplay Zapier MCP](https://zapier.com/mcp/foreplay)
- [Meta Ad Library API](https://www.facebook.com/ads/library/api)
- [AdDownloader (GitHub)](https://github.com/Paularossi/AdDownloader)
- [Meta Ad Library API Guide (Apidog)](https://apidog.com/blog/facebook-ad-library-api/)
- [Meta Ad Library API Guide (adlibrary.com)](https://adlibrary.com/guides/facebook-ad-library-api)
- [AssemblyAI Pricing](https://www.assemblyai.com/pricing)
- [Deepgram Pricing](https://deepgram.com/pricing)
- [OpenAI Whisper Pricing](https://costbench.com/software/ai-transcription-apis/openai-whisper/)
- [Whisper API Pricing Breakdown](https://brasstranscripts.com/blog/openai-whisper-api-pricing-2025-self-hosted-vs-managed)
- [Deepgram Pricing Breakdown](https://brasstranscripts.com/blog/deepgram-pricing-per-minute-2025-real-time-vs-batch)
- [Best Speech-to-Text APIs 2026 (Deepgram)](https://deepgram.com/learn/best-speech-to-text-apis-2026)
- [AssemblyAI vs Deepgram vs Whisper Comparison](https://www.index.dev/skill-vs-skill/ai-whisper-vs-assemblyai-vs-deepgram)
- [Parker.ai (heyparker.ai)](https://heyparker.ai/)
- [Parker AI LinkedIn Announcement](https://www.linkedin.com/posts/alexgoughcooper_introducing-parker-the-worlds-first-ai-activity-7421971283866779650-XWoj)
- [Atria AI](https://www.tryatria.com/)
- [Atria AI Review](https://max-productive.ai/ai-tools/atria/)
- [MagicBrief](https://magicbrief.com/inspire)
- [MagicBrief vs Motion Comparison](https://magicbrief.com/post/magicbrief-vs-motion-the-ultimate-creative-analytics-tool-comparison)
- [Best Ad Spy Tools 2026](https://benly.ai/learn/ai-marketing/best-ad-spy-tools-2026)
- [n8n Foreplay Workflow Template](https://n8n.io/workflows/9986-ai-powered-product-video-generator-foreplay-gemini-sora-2/)
- [n8n Meta Ads Creative Testing Template](https://n8n.io/workflows/6038-automation-of-creative-testing-and-campaign-launching-for-meta-ads/)
- [n8n Competitor Meta Ads Monitor Template](https://n8n.io/workflows/11270-monitor-competitor-meta-ads-creatives-and-send-alerts-with-google-sheets-and-telegram/)
- [n8n $5k Foreplay Bounty](https://community.n8n.io/t/opportunity-5k-bounty-for-advertising-workflow/185771)
