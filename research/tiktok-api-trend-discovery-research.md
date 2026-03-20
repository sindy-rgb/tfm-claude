# TikTok API & Trend Discovery Research

**Date:** March 16, 2026
**Purpose:** Evaluate all options for programmatically pulling TikTok trending content, ads, sounds, and scripts to feed into an AI concept ideation engine alongside Foreplay (Meta ads) and Meta Ad Library data.
**Goal:** Rebuild a tool similar to Parker.ai by combining TikTok trends + Foreplay + Meta Ad Library.

---

## Table of Contents

1. [TikTok Creative Center (No Official API)](#1-tiktok-creative-center)
2. [TikTok Commercial Content API](#2-tiktok-commercial-content-api)
3. [TikTok Marketing API (Business API)](#3-tiktok-marketing-api)
4. [TikTok Research API](#4-tiktok-research-api)
5. [Foreplay API (Best-in-Class for Meta Ads)](#5-foreplay-api)
6. [Meta Ad Library API](#6-meta-ad-library-api)
7. [Third-Party Ad Spy Tools](#7-third-party-ad-spy-tools)
8. [Apify Scrapers (Best Option for TikTok Creative Center)](#8-apify-scrapers)
9. [TikTok Transcript APIs](#9-tiktok-transcript-apis)
10. [Open-Source Scrapers](#10-open-source-scrapers)
11. [Data365 (Unified Social API)](#11-data365)
12. [Parker.ai Analysis](#12-parker-ai-analysis)
13. [Recommended Architecture](#13-recommended-architecture)

---

## 1. TikTok Creative Center

**URL:** https://ads.tiktok.com/business/creativecenter/pc/en

### What It Offers (Browser-Only)
- **Top Ads Dashboard** — Filter by country, industry, objective, ad format; see top-performing auction ads with video previews
- **Trending Hashtags** — By country, 7-day trend charts, view counts, post counts, rank changes
- **Trending Songs/Sounds** — Commercial music trending by country with audience insights
- **Trending Videos** — Viral organic content with engagement metrics
- **Trending Creators** — Top creator accounts by country/industry
- **Keyword Insights** — Search volume, keyword trends, related terms (requires Business Account)
- **Symphony AI Tools** — AI-powered creative assistance (script writing, etc.)

### API Availability
**No official API exists.** The Creative Center is a browser-only tool. No programmatic access is provided by TikTok. This is the single biggest gap.

### Access Requirements
- Free to use without login for most features
- Business Account required for Keyword Insights and Symphony
- No API keys, no developer program for Creative Center specifically

### Workaround
Apify scrapers (see Section 8) can extract all Creative Center data programmatically.

---

## 2. TikTok Commercial Content API

**URL:** https://developers.tiktok.com/products/commercial-content-api
**Docs:** https://developers.tiktok.com/doc/commercial-content-api-getting-started

### What It Provides
- Search ads by **keyword, advertiser name, or advertiser ID**
- Ad metadata: published date, last seen date, targeting info, impression counts
- Disapproved ad details
- Advertiser information and commercial entity data

### Key Endpoints
- **Query Ads** — Search with filters for date ranges, countries, keywords
- **Get Ad Details** — Full metadata for a specific ad
- **Query Advertisers** — Search advertiser entities
- **Get Ad Report** — Performance/reach data for specific ads

### Access Requirements
- Create TikTok for Developers account (official email required)
- Submit application at `/application/commercial-content-api`
- Approval in ~2 business days
- Contact: commercial-research-questions@tiktok.com

### Limitations
- **EU data only** (Phase 1) — Only ads shown in EU countries are currently available
- Designed for **transparency/research**, not commercial competitive intelligence
- Data retention: ads available for up to 1 year after last shown
- No video transcripts included
- No performance metrics beyond impression counts
- Rate limits not publicly documented
- **Verdict: Useful for EU competitor research only. Not sufficient for US-focused newsletter ads.**

---

## 3. TikTok Marketing API (Business API)

**URL:** https://business-api.tiktok.com/portal
**SDK:** https://github.com/tiktok/tiktok-business-api-sdk

### What It Provides
- Full campaign management (create, edit, pause ads)
- Creative upload and management
- Reporting on **your own ad account's** performance
- Audience management
- Conversion tracking

### Key Capabilities
- Upload and manage creative materials through consolidated interface
- Reporting endpoint: `https://business-api.tiktok.com/open_api/v1.2/reports/integrated/get`
- GMV Max Reporting API for campaign performance across products, creatives
- Upgraded Smart+ API (legacy deprecated March 31, 2026)

### Access Requirements
- TikTok Ads Manager account required
- Developer application through Business API portal
- OAuth-based authentication

### Limitations
- **Only your own ad account data** — Cannot see competitor ads, competitor creatives, or competitor performance
- No trend discovery features
- No access to other advertisers' content
- **Verdict: Not useful for competitive research. Only for managing TFM's own TikTok campaigns (if we run TikTok ads).**

---

## 4. TikTok Research API

**URL:** https://developers.tiktok.com/products/research-api/

### What It Provides
- Public user profiles, followers, following lists
- Video and engagement metrics on public posts
- Hashtag performance and trends (aggregated)
- Topic-level aggregated data
- TikTok Shop data

### Access Requirements (Very Restrictive)
- **Academic institutions only** in US, EEA, UK, or Switzerland
- EU-based not-for-profit research organizations (beta)
- Brazilian academic/nonprofits researching youth safety
- Must demonstrate research expertise
- Must be independent from commercial interests
- Must disclose funding sources
- Must provide defined research proposals
- Must obtain ethical research review approval
- Approval takes ~4 weeks
- Data accessed through Virtual Compute Environment (VCE)
- Data must be refreshed every 15 days

### Limitations
- **Not available for commercial use** — Explicitly requires non-commercial basis
- High-engagement posts are over-represented in data
- Inconsistent data delivery reported
- No ad-specific data
- **Verdict: Not viable for TFM. Academic-only access with no commercial use allowed.**

---

## 5. Foreplay API (Best-in-Class for Meta Ads)

**URL:** https://www.foreplay.co/api
**Docs:** https://public.api.foreplay.co/docs
**OpenAPI Spec:** https://public.api.foreplay.co/openapi.json

### What It Provides
Foreplay is the strongest option for Meta ad competitive intelligence with a production-ready API.

### Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /api/swipefile/ads` | Your saved ad collection with full filtering |
| `GET /api/boards` | List all boards |
| `GET /api/board/ads` | Ads from a specific board |
| `GET /api/spyder/brands` | Brands you're tracking |
| `GET /api/spyder/brand/ads` | All ads from a tracked brand |
| `GET /api/ad/{ad_id}` | **Full ad details including transcription** |
| `GET /api/ad/duplicates/{ad_id}` | Find duplicate creatives |
| `GET /api/brand/getAdsByBrandId` | Ads for multiple brands |
| `GET /api/brand/getAdsByPageId` | Ads by Facebook Page ID |
| `GET /api/brand/getBrandsByDomain` | Look up brands by domain URL |

### Ad Object Fields (Key)
- `full_transcription` — Complete video transcript
- `timestamped_transcription` — Timestamped transcript segments
- `video`, `image`, `thumbnail` — Media URLs
- `headline`, `description`, `cta_title`, `cta_type` — Ad copy
- `display_format` — Video, image, carousel, DCO, DPA
- `publisher_platform` — Facebook, Instagram, Audience Network, Messenger
- `link_url` — Landing page
- `creative_targeting` — Targeting info
- `emotional_drivers` — AI-detected emotional angles
- `started_running`, `running_duration` — Timing data
- `niches`, `categories`, `market_target`, `languages` — Classification

### Filtering Options
- Date ranges, live/inactive status, display format
- Publisher platform, niches, market target, languages
- Video duration min/max, running duration min/max days
- Sorting: newest, oldest, longest_running, most_relevant

### Pricing
| Plan | Monthly Cost |
|------|-------------|
| 10,000 credits (free with any plan) | $0 |
| 100,000 credits | $99/mo |
| 250,000 credits | $189/mo |
| 500,000 credits | $349/mo |
| Enterprise | Custom (up to 80% savings) |

- 1 credit = 1 ad retrieval (includes all metadata + transcript)
- Credits don't roll over

### Authentication
- API key in `Authorization` header
- Generate from https://app.foreplay.co/api-overview

### Integrations
- **n8n** (confirmed integration)
- Zapier, Make.com, Gumloop, Clay

### Limitations
- **Meta platforms only** (Facebook, Instagram, Messenger, Audience Network)
- **No TikTok ads** in Foreplay's database
- 100M+ ad database from 300,000+ brands
- Max 250 ads per request

### Verdict
**This is the foundation for Meta ad intelligence.** Full transcripts, emotional drivers, and n8n integration make it ideal. But it covers Meta only — TikTok data must come from elsewhere.

---

## 6. Meta Ad Library API

**URL:** https://www.facebook.com/ads/library/api

### What It Provides
- Search all active and inactive ads on Meta platforms
- Filter by page ID, keyword, country
- Ad creative preview, spend estimates, reach data
- Targeting information for political/social issue ads

### Access Requirements
- Meta Developer account
- Ad Library API access (separate from Marketing API)
- Rate limit: **200 calls per hour**

### Limitations
- Officially intended for researchers/journalists, not commercial competitive intelligence
- Limited creative data (no transcripts, no full video downloads)
- Rate-limited at 200/hour
- **Foreplay is a better option** — it wraps Meta Ad Library data with transcripts, emotional analysis, and better filtering

---

## 7. Third-Party Ad Spy Tools

### PiPiADS (TikTok-Focused)
**URL:** https://www.pipiads.com/

| Feature | Details |
|---------|---------|
| Database | 50M+ TikTok ads, 500K+ added daily |
| Platforms | TikTok (primary), Facebook |
| Data | Ad creatives, video URLs, engagement metrics, landing pages, advertiser info |
| Filtering | Country, industry, date range, engagement level, ad format |
| API | **No public API documented** |
| Pricing | Starter ~$77/mo, VIP ~$155/mo, Pro ~$263/mo, Enterprise custom |
| Transcripts | Not confirmed |
| **Verdict** | Best TikTok ad database but no API = cannot automate. Browser-only tool. |

### BigSpy
**URL:** https://bigspy.com/

| Feature | Details |
|---------|---------|
| Database | 1B+ ads from 71 countries, 23 languages |
| Platforms | 10 platforms: Facebook, Instagram, TikTok, YouTube, Pinterest, Twitter, etc. |
| Data | Ad creatives, engagement metrics, targeting info, posting times |
| API | **Enterprise API available** (undocumented publicly, contact sales) |
| Pricing | $9-$99/mo standard; Enterprise custom for API access |
| Transcripts | Not confirmed |
| **Verdict** | Widest platform coverage. API exists but only for enterprise. Worth inquiring about API pricing for TikTok ad data specifically. |

### Minea
**URL:** https://www.minea.com/

| Feature | Details |
|---------|---------|
| Database | Millions of ads across platforms |
| Platforms | Facebook, Instagram, TikTok, Pinterest |
| Focus | Dropshipping/ecommerce product ads |
| API | **No public API** |
| Pricing | Basic EUR49/mo, Premium EUR99/mo (TikTok only in Premium) |
| **Verdict** | Ecommerce-focused, not relevant for newsletter ads. No API. |

### AdSpy
**URL:** https://adspy.com/

| Feature | Details |
|---------|---------|
| Database | Large Meta ad database |
| Platforms | Facebook, Instagram primarily |
| API | **No public API** |
| Pricing | $149/mo |
| **Verdict** | No TikTok. No API. Foreplay is better for Meta. |

---

## 8. Apify Scrapers (Best Option for TikTok Creative Center)

**URL:** https://apify.com/store/collections/tiktok-scrapers

This is the most viable path for programmatic TikTok Creative Center data. Apify provides hosted scrapers (called "Actors") that run on their cloud and expose RESTful APIs.

### Available TikTok Creative Center Actors

#### a) TikTok Creative Center Scraper (`doliz/tiktok-creative-center-scraper`)
- **Data:** Top Ads, Trending Videos, Trending Creators, Trending Songs, Trending Hashtags
- **Output:** Structured JSON with all metadata
- **Features:** Multi-country (73+ countries), industry filtering, 7-day trend charts, rank changes

#### b) TikTok Creative Center Top Ads Scraper (`codebyte/tiktok-creative-center-top-ads`)
- **Data:** Top-performing auction ads from Creative Center
- **Fields:** Ad creatives, video URLs, CTR rankings, brand names, budget data
- **Capacity:** 20-40 ads per filter combination per run
- **No login required**

#### c) TikTok Ad Library Spy & Creative Center Scraper (`beyondops/tiktok-ad-library-scraper`)
- **Data:** High-performing ads from Creative Center
- **Fields:** Ad creatives, video URLs, CTR rankings, brand names, budget data
- **Countries:** 50+ supported
- **Cost:** ~$0.30 per 100 ads extracted

#### d) TikTok Trends Scraper (`clockworks/tiktok-trends-scraper`)
- **Data:** Trending hashtags, videos, challenges
- **Output:** Captions, hashtags, creators, sounds, metrics, timestamps

#### e) TikTok Trends API (`data_xplorer/tiktok-trends`)
- **Pricing:** Pay-per-event model
- **Data:** Current trending content

### Apify Pricing
| Plan | Monthly Cost | Included |
|------|-------------|----------|
| Free | $0 | $5 platform credits/mo |
| Starter | $49/mo | $49 credits |
| Scale | $499/mo | $499 credits |
| Enterprise | Custom | Custom |

Each Actor run costs fractions of a dollar. A typical Creative Center scrape of 100 ads costs ~$0.30.

### API Access
Every Apify Actor exposes a REST API:
```
POST https://api.apify.com/v2/acts/{actorId}/runs
GET https://api.apify.com/v2/actor-runs/{runId}/dataset/items
```
- Authentication via API token
- Webhooks available for completion notifications
- Output in JSON, CSV, Excel, XML, RSS

### n8n Integration
- **Apify has an official n8n node** — can trigger Actor runs, wait for completion, and retrieve results
- Can schedule daily/weekly scrapes via n8n cron triggers
- Pipe results into Google Sheets, Notion, Slack, or custom AI pipelines

### Limitations
- Scraping is inherently fragile — TikTok can change their HTML/APIs
- Rate limiting by TikTok may affect scraper reliability
- No guaranteed uptime/data freshness (depends on Actor maintainer)
- No transcripts of ad videos (need separate transcript extraction)

### Verdict
**This is the primary path for TikTok trend/ad data.** Combine Apify Creative Center scrapers with a TikTok transcript API (Section 9) to get the full picture.

---

## 9. TikTok Transcript APIs

### Supadata.ai
**URL:** https://supadata.ai/tiktok-transcript-api

| Feature | Details |
|---------|---------|
| What it does | Extracts transcripts from TikTok videos via URL or video ID |
| Output | Text segments with timestamps (duration + offset in ms), language detection |
| Languages | Any available language, auto-generated and manual captions |
| Auth | API key via `x-api-key` header |
| Rate limits | 1-500 req/sec depending on plan |
| Pricing | Not publicly listed (likely usage-based) |
| Coverage | "Billions of TikTok videos" — unclear if ads are included |
| No TikTok API key required | Yes |

### SocialKit
**URL:** https://www.socialkit.dev/

| Feature | Details |
|---------|---------|
| Free tier | 20 requests/month |
| Focus | TikTok-specific transcript challenges |
| Output | Timestamped transcript segments |

### ScrapeCreators
**URL:** https://scrapecreators.com/tiktok-api

| Feature | Details |
|---------|---------|
| What it does | TikTok transcript extraction as part of broader social API suite |
| Also provides | Stats, details, metrics for TikTok content |

### DIY Approach
- Download video via Apify scraper (video URL included in output)
- Run through Whisper (OpenAI) or other speech-to-text locally
- Most reliable for ad videos since transcript APIs may not cover ad content

### Verdict
**Supadata or SocialKit for quick transcript extraction.** For ad videos specifically, downloading + Whisper is the most reliable path since ad video transcripts may not be indexed by these services.

---

## 10. Open-Source Scrapers

### drawrowfly/tiktok-scraper (Node.js)
**GitHub:** https://github.com/drawrowfly/tiktok-scraper
- Download video posts, collect user/trend/hashtag/music feed metadata
- Sign URLs programmatically
- Most starred TikTok scraper on GitHub

### Q-Bukold/TikTok-Content-Scraper (Python)
**GitHub:** https://github.com/Q-Bukold/TikTok-Content-Scraper
- No API key needed, minimal dependencies
- Downloads videos (MP4), slides (JPEG), and full metadata
- Hashtags, content, interactions, music data

### networkdynamics/pytok (Python + Playwright)
**GitHub:** https://github.com/networkdynamics/pytok
- Browser automation with automatic CAPTCHA solving
- Academic research tool

### tadeubanzato/TikTok-Scraper (Python + Selenium)
**GitHub:** https://github.com/tadeubanzato/TikTok-Scraper
- Selenium-based puppeteering approach
- Handles TikTok's dynamic rendering

### Limitations of Open Source
- Constantly breaking as TikTok updates anti-bot measures
- TikTok moved US operations to USDS Joint Venture (Oracle) in 2026, changing data handling
- Require maintenance and infrastructure
- None specifically target the Creative Center
- **Verdict: Use Apify instead.** The hosted scrapers handle maintenance, anti-bot measures, and infrastructure. Open-source is only worth it if building a deeply custom pipeline.

---

## 11. Data365 (Unified Social API)

**URL:** https://data365.co/tiktok

| Feature | Details |
|---------|---------|
| Platforms | Instagram, TikTok, YouTube, LinkedIn, Twitter, Reddit |
| TikTok data | Trending videos, views, likes, comments, shares, hashtags, sounds, user demographics |
| Data source | TikTok Discover page, user profiles, public pages |
| Output | Consistent JSON format across all platforms |
| Pricing | Custom/volume-based (not publicly listed) |
| Trial | 14-day free trial |
| API style | RESTful, unified across platforms |

### Verdict
Worth evaluating if you want a single API for TikTok + Instagram + YouTube trends. But custom pricing and lack of Creative Center/ad-specific data may limit usefulness. Better suited for organic trend discovery than ad intelligence.

---

## 12. Parker.ai Analysis

**URL:** https://heyparker.ai/

Parker.ai (heyparker.ai) is an AI-powered ad creative research and ideation tool. Based on research:

### What It Does
- Researches competitors and aggregates ad performance data
- Uses AI trained on frameworks/formulas of top advertisers
- Generates hooks, scripts, angles, and briefs from research
- Pulls from reviews, TikTok trends, and ad data
- Organizes everything in one place

### How It Likely Works (Reverse-Engineered)
1. **TikTok Trends:** Most likely scrapes TikTok Creative Center (possibly via Apify-style scrapers or custom scraping) for trending sounds, hashtags, and top ads
2. **Meta Ads:** Likely uses Meta Ad Library API and/or Foreplay-style data aggregation
3. **AI Layer:** Passes collected data through LLMs to extract patterns, generate scripts, and suggest creative angles
4. **No public API** available

### What TFM Can Replicate
Parker's core value prop is: **data collection + AI analysis + creative generation.** Each component can be built:
- Data collection: Apify (TikTok) + Foreplay API (Meta) + Meta Ad Library API
- AI analysis: Claude/GPT for pattern extraction and script generation
- Creative generation: Claude with brand voice rules and winning creative signals

---

## 13. Recommended Architecture

### Data Sources (Priority Order)

| Source | What It Gets | Tool | Cost | Integration |
|--------|-------------|------|------|-------------|
| **Foreplay API** | Meta ad creatives, transcripts, emotional drivers, landing pages | Direct API | $99-349/mo | n8n native, Claude Code via HTTP |
| **Apify TikTok Creative Center** | Top ads, trending sounds, trending hashtags, trending videos | Apify API | ~$49/mo (Starter) | n8n native (Apify node) |
| **Supadata / Whisper** | TikTok video transcripts | API or local | ~$20-50/mo | n8n HTTP node |
| **Meta Ad Library API** | Raw Meta ad data (supplement to Foreplay) | Direct API | Free | n8n HTTP node |
| **BigSpy API** | TikTok + multi-platform ad data | Enterprise API (contact sales) | Unknown | n8n HTTP node |
| **TikTok Commercial Content API** | EU competitor ad data | Official API | Free | n8n HTTP node |

### Proposed Pipeline

```
[Daily n8n Cron Trigger]
    |
    +---> [Apify: TikTok Creative Center Scraper]
    |         |
    |         +---> Top Ads (by industry: media/publishing)
    |         +---> Trending Sounds
    |         +---> Trending Hashtags
    |         +---> Trending Videos
    |
    +---> [Foreplay API: Spyder + Discovery]
    |         |
    |         +---> Competitor brand ads (newsletter competitors)
    |         +---> New ads from tracked brands
    |         +---> Full transcripts + emotional drivers
    |
    +---> [TikTok Video Transcript Extraction]
              |
              +---> Download top ad videos from Apify output
              +---> Extract transcripts via Supadata API or Whisper
    |
    v
[Data Aggregation Layer]
    |
    +---> Store in Notion database (structured)
    +---> Store raw data in Google Sheets (backup)
    |
    v
[AI Concept Ideation Engine]
    |
    +---> Claude API with:
    |       - Trending TikTok hooks/sounds/formats
    |       - Competitor Meta ad transcripts + copy
    |       - Client brand voice rules (from client intelligence files)
    |       - Winning creative signals (from client files)
    |       - DCT 4-3-2-2 format requirements
    |
    +---> Output: New ad concept briefs per client
    +---> Post to Slack for team review
```

### Phase 1 (Quick Win — 1-2 weeks)
1. Set up Foreplay API in n8n (they have native integration)
2. Set up Apify TikTok Creative Center scraper in n8n (native Apify node)
3. Build daily automated pull of trending TikTok data + competitor Meta ads
4. Store in Notion

### Phase 2 (AI Layer — 2-3 weeks)
1. Add transcript extraction (Supadata API or Whisper)
2. Build Claude-powered concept ideation workflow
3. Feed client brand voice + winning signals into prompts
4. Output structured ad briefs to Notion/Slack

### Phase 3 (Scale — Ongoing)
1. Evaluate BigSpy Enterprise API for additional TikTok ad data
2. Add TikTok Commercial Content API for EU coverage
3. Build client-specific dashboards
4. Train the system on what concepts actually perform (feedback loop from Meta Ads performance data via Pipeboard)

### Estimated Monthly Cost
| Item | Cost |
|------|------|
| Foreplay API (100K credits) | $99/mo |
| Apify (Starter) | $49/mo |
| Supadata or similar transcript API | $20-50/mo |
| Claude API usage | $30-100/mo |
| **Total** | **~$200-300/mo** |

---

## Key Takeaways

1. **There is no single API that does what Parker.ai does.** It must be assembled from multiple sources.
2. **Foreplay API is the strongest single piece** — production-ready, includes transcripts, native n8n integration, covers Meta ads comprehensively.
3. **TikTok Creative Center has no official API** — Apify scrapers are the best workaround and are reliable/cheap.
4. **TikTok's official APIs are either too restrictive (Research API = academic only) or too limited (Commercial Content API = EU only, Marketing API = own account only).**
5. **No major ad spy tool (PiPiADS, Minea, AdSpy) offers a public API** — BigSpy has an enterprise API worth investigating.
6. **Video transcript extraction is a solved problem** — Supadata, SocialKit, or Whisper can handle it.
7. **The full pipeline is buildable in n8n** with Apify node + HTTP nodes + Claude API, at ~$200-300/mo total cost.

---

## Sources

- [TikTok Commercial Content API](https://developers.tiktok.com/products/commercial-content-api)
- [TikTok Research API](https://developers.tiktok.com/products/research-api/)
- [TikTok Business API](https://business-api.tiktok.com/portal)
- [Foreplay API](https://www.foreplay.co/api)
- [Foreplay API Docs](https://public.api.foreplay.co/docs)
- [Apify TikTok Creative Center Scraper](https://apify.com/doliz/tiktok-creative-center-scraper)
- [Apify TikTok Creative Center Top Ads](https://apify.com/codebyte/tiktok-creative-center-top-ads)
- [Apify TikTok Ad Library Scraper](https://apify.com/beyondops/tiktok-ad-library-scraper)
- [Apify TikTok Trends Scraper](https://apify.com/clockworks/tiktok-trends-scraper)
- [Supadata TikTok Transcript API](https://supadata.ai/tiktok-transcript-api)
- [SocialKit TikTok Transcript API](https://www.socialkit.dev/blog/best-tiktok-transcript-apis-2025)
- [Data365 TikTok API](https://data365.co/tiktok)
- [PiPiADS](https://www.pipiads.com/)
- [BigSpy](https://bigspy.com/)
- [Minea](https://www.minea.com/)
- [Parker.ai](https://heyparker.ai/)
- [Meta Ad Library API](https://www.facebook.com/ads/library/api)
- [TikTok Creative Center](https://ads.tiktok.com/business/creativecenter/pc/en)
- [drawrowfly/tiktok-scraper (GitHub)](https://github.com/drawrowfly/tiktok-scraper)
- [Q-Bukold/TikTok-Content-Scraper (GitHub)](https://github.com/Q-Bukold/TikTok-Content-Scraper)
- [ScrapFly TikTok Scraping Guide](https://scrapfly.io/blog/posts/how-to-scrape-tiktok-python-json)
