# Creator Spotlight -- Deep Enrichment Report

**Compiled:** March 21, 2026
**Sources:** Google Drive, Notion, Web (creatorspotlight.com, beehiiv.com, competitor sites), existing client intelligence

---

## TASK 1: Google Drive Creative Audit

### Key Assets Found

**Spreadsheets:**
- **Creator Spotlight - Weekly Ad Report** (Google Sheets) -- Weekly performance tracking spreadsheet
- **Creator Spotlight Hub** (Google Sheets) -- Central creative/campaign hub spreadsheet

**Folders:**
- `Creative - Creator Spotlight` (2 instances -- likely one per Drive structure)
- `Creator Spotlight` (main client folder)
- `creator-spotlight` (2 instances -- project-level folders)

**Documents:**
- **Onboarding doc - Creator Spotlight** -- Original client onboarding documentation
- **Creator spotlight - meeting notes** -- Running meeting notes
- **Creator spotlight research** -- Background research (shortcut)

**Audio:**
- `CreatorSpotlight102024-final (1).wav` -- October 2024 meeting/call recording
- `Creator spotlight onboarding.m4a` -- Onboarding call recording

### DCT Creative Inventory (from Google Drive)

| DCT # | Name / Concept | Format | Contents |
|-------|---------------|--------|----------|
| **DCT 115** | Highlighting Creator Spotlight | Image (static) | 3 image variations (a, b, c JPGs) + concept doc. Text-heavy image ad highlighting newsletter value props: growth strategies, real revenue numbers, action items, time-saving tools. 3 headline variations targeting different angles. |
| **DCT 128** | Insider Knowledge | Video | 3 video variations (.mp4) -- appears duplicated (6 files total, likely version history). "Insider Knowledge M..." naming suggests insider/exclusive knowledge angle. |
| **DCT 132** | (Untitled) | Video | 3 video variations (.mp4). No descriptive name in file titles. |
| **DCT 134** | The Creator Economy | Video | 3 video variations (.mp4). Creator economy framing -- broader industry angle. |
| **DCT 135** | There Has to Be a Reason | Video | 3 video variations (.mp4). Curiosity/confession-style framing. |
| **DCT 137** | 0-10K Lead Magnet | Video | 3 video variations (.mp4). Lead magnet format targeting growth-stage creators (0-10k followers). Known scale driver per client intelligence. |
| **DCT 141** | Collab | Video | 1 video file (.mp4). Collaboration-themed concept. |
| **DCT 167** | I Discovered Creator Spotlight | Image (static) | Folder + 3 image variations (a1, a2, a3 JPGs). Discovery/testimonial angle -- "Then a friend sent me a newsletter called Creator Spotlight." **Strongest early quality signal of March batch: 55.32% OR.** |

### Additional Creative Assets
- `creator spotlight ig .jpg` -- Instagram-formatted creative asset

### Notes on Drive Structure
- Google Sheets API is not enabled for the MCP integration, so spreadsheet contents (Weekly Ad Report, Hub) could not be read directly. These contain performance data and campaign tracking that would further enrich DCT-level analysis.
- Video creatives follow the naming convention: `Creator Spotlight DCT [#].[variation#] [concept name].mp4`
- Image creatives follow: `DCT_[#]_[concept name] [variation].jpg`

---

## TASK 2: Notion Concept Database

### Database 1: Creator Spotlight Creative Hub

**Location:** Notion > The Feed Media > Creator Spotlight > Creator Spotlight Creative Hub
**Database URL:** `https://www.notion.so/1caf4a126e0680298149cc9fb2f383bf`
**Data Source:** `collection://1a6f4a12-6e06-807c-bfd5-000b191a937a`

**Schema (key fields for CS):**
| Field | Type | Options |
|-------|------|---------|
| Concept name | Title | -- |
| Client | Select | Creator Spotlight (+ other clients share this DB) |
| Format | Select | Video, Image |
| Status | Select | Inspiration, Concept, Writing, Copy Review, Creator matching, Filming/shooting, Editing, Final review, **Approved/launched** |
| Outcome | Select | **Winner, Loser, Scaled, Testing** |
| Messaging angle | Multi-select | Social proof, 0-10k lead magnet, Monetization playbook, Insider knowledge, Creator story, De-bunking Myths, Motivational, Behind the scenes, Business ideas, Relatable truth, Burnout, Education, Exclusive, and more |
| Style | Multi-select | Text over video, Static, Notes, Meme, Tweet, iMessage, POV, UGC - Regular, UGC - AI, Carousel, Voiceover b-roll, Feature static, Testimonial, LinkedIn Post, Listicle, Advertorial, Slack, AMA |
| Type | Select | New, Iteration |
| Deadline to client | Date | -- |
| Prioritized | Checkbox | -- |

**Views configured for CS:**
1. **New concepts** -- Table filtered to Client=Creator Spotlight, Status=Concept, Prioritized=false
2. **Prioritized** -- Table filtered to Client=Creator Spotlight, Prioritized=true, Status=Concept
3. **Board view** -- Kanban board grouped by Status, filtered to CS + Prioritized
4. **Schedule** -- Timeline view sorted by Deadline to client

### Database 2: Concept Validation Creator Spotlight

**Location:** Notion > The Feed Media Agency > Team Hub > Company Databases > Creator Spotlight & The Feed media > Concept Validation Creator Spotlight
**Database URL:** `https://www.notion.so/317f4a126e06800d9d66ee52748b8554`
**Data Source:** `collection://317f4a12-6e06-8002-83c4-000bf27c98f4`

**Schema:**
| Field | Type | Options |
|-------|------|---------|
| Name | Title | -- |
| DCT | Text | DCT number reference |
| Format | Select | Video, Image, UGC |
| Style | Select | Social Hacking, UGC Reaction Video, Text Over Video, Arcad avatars, Static, Carousel, Tweet, Before & after, Comparaison, UGC Regular, Meme, Apple Notes, Podcast, Voiceover, POV, Animation, Weavy AI, Motion |
| Status | Status | Concept > 2-Concept (Internal Validation) > 3-Concept (To Send to Client) > 4-Concept (Client Validation) > 5-Script (To Write) > 6-Script (Writing) > 7-Script (Internal Validation) > 8-Script (To Send to Client) > 9-Script (Client Validation) > 10-To Execute > 11-Executing > 12-Execution (Internal Validation) > 13-Design (To Prepare) > 14-Design (Preparing) > Sent to designer > **Backlog** / **Rejected** |
| Type | Select | New, Iteration |
| Deadline to client | Date | -- |
| Strategist Deadline | Date | -- |
| Design Max | Date | -- |
| Creative Folder | Text | Link to Google Drive folder |

**Pipeline stages (14 steps):** This DB uses a granular 14-step creative production pipeline from initial concept through design completion, with both internal and client validation gates at concept, script, and execution phases.

### Key Notion Pages Found

| Page | ID | Description |
|------|-----|-------------|
| Creator Spotlight (beehiiv) -- Client Intelligence | `31df4a12...` | Main client intelligence page in Notion |
| Creator Spotlight -- Meta Ads Media Buying SOP | `261f4a12...` | SOP for media buying, DCT naming conventions |
| Creator Spotlight Creative Hub | `1caf4a12...` | Central creative database (shared across clients) |
| Concept Validation Creator Spotlight | `317f4a12...` | Creative pipeline/validation database |
| Creator Spotlight & The Feed media | `317f4a12...80cd` | Shared workspace with client |
| Bi-Weekly Reports | Multiple | March 9, Feb 23, Feb 10, Jan 26, Jan 12, Dec 15, Dec 1, Nov 3 |
| Creator Spotlight -- Q4 TOTF Insights | `2f9f4a12...` | Q4 2025 top-of-funnel analysis |
| Creator Spotlight: Sponsor Analysis | `2f9f4a12...8151` | Sponsor click rate analysis |
| QA Issue Log V3 | `328f4a12...` | Exhaustive QA training reference (Oct 2025-Mar 2026) |

### DCT Concepts Referenced in Notion (with known performance data)

| DCT | Name | Status | Performance |
|-----|------|--------|-------------|
| 106 | Confession (Anti-Guru) | Approved/Launched | CPL $2.07, CTR 3.39%, CVR ~55%, OR 41.34%, unsub 3.14% |
| 115 | Highlighting Creator Spotlight | Approved/Launched | Early concept -- text-heavy image ad |
| 128 | Insider Knowledge | Approved/Launched | Video format |
| 131 | Creator Spotlight Feature | Approved/Launched | Referenced in meetings |
| 132 | (Untitled) | Approved/Launched | Video format |
| 134 | The Creator Economy | Approved/Launched | Video format |
| 135 | There Has to Be a Reason | Approved/Launched | Video format |
| 137 | 0-10K Lead Magnet | Approved/Launched | Scale driver, lead magnet angle |
| 141 | Collab | Approved/Launched | Video format |
| 143 | Building a Social Following is HARD | **Scaled** | CPL $2.08, OR 42.76%, CVR ~57%, unsub 6.83%. Reliable quality anchor. |
| 152 | Scrolling Blurred Grid | **Winner** | Best CTR + lowest unsub. Francis: "best ad we've run." |
| 155 | Making Money as a Creator is Hard | **Loser** | Switched off. Two weeks below 28% OR. |
| 156 | (Monetization) | Loser/Paused | Lower quality, spend shifted away |
| 158 | Creators Are Reading This | **Scaled** | CPL $2.05, CTR 3.46%, CVR ~50%, **OR 48.79%**, unsub 2.90%. Strongest quality. |
| 159 | (Social Proof variant) | Active | Mid-funnel social proof |
| 164 | Apology to the Fake Gurus | **Winner** | **50% OR** across 93 sign-ups. Strongest quality signal. |
| 165 | Learn How to Earn as a Creator | **Loser** | Volume leader CPL $1.85 but only 37-38% OR base. "Copy makes me cringe." |
| 167 | I Discovered Creator Spotlight | **Testing** | 42 sign-ups, **55.32% OR**. Strongest early quality of March batch. |
| 168 | To Do List | Testing | Approved and launched March 2026 |
| 169 | Creator DM | Testing | 34 sign-ups, 40.48% OR. Francis: "This is strong creative." |
| 170 | Millennial Meme | Testing | Approved and launched March 2026 |
| 171 | POV Problem + Solution | Testing | Approved by Francis 3/12 |
| 172 | Explanation from a Friend | Testing | Approved by Francis 3/12 |
| 173 | (Smart Angle) | **Watch** | 2nd highest spend but only 32.14% OR. Francis liked angle but quality below benchmark. |

### Creative Production Insights from Notion

**Messaging angles that work for CS (from Creative Hub schema):**
- Social proof (DCT 158, highest quality)
- 0-10k lead magnet (DCT 143, scale driver)
- Monetization playbook (high-intent)
- De-bunking Myths / Anti-guru (DCT 106, DCT 164)
- Creator story (authentic narrative)
- Relatable truth

**Styles that work for CS:**
- Text over video (dominant format)
- Static (text-heavy)
- Notes (Apple Notes aesthetic)
- iMessage
- POV
- Meme (tested carefully -- Francis dislikes clickbait)

---

## TASK 3: Website / Newsletter Analysis

### Website: creatorspotlight.com

**Platform:** beehiiv (redirects from creator-spotlight.beehiiv.com)
**Primary Color:** Orange (#e73d00) -- beehiiv brand alignment
**Design:** Modern, responsive, Tailwind CSS with dark/light theme support. Uses Inter, Archivo, and Work Sans fonts. Clean editorial layout.
**Payment Integration:** Stripe (for potential premium content)
**Security:** Cloudflare Turnstile bot protection
**Calendar:** Cal.com OAuth integration (likely for booking creator interviews)

**Note:** The website is a JavaScript-heavy SPA (single-page application) that renders content dynamically, making static HTML extraction limited. Key content is loaded client-side.

### Newsletter Content & Format

**Tagline:** "Your guide to growing and monetizing creator-first businesses"

**Publishing Cadence:**
- **Tuesdays:** New creator interview/profile (podcast + written)
- **Fridays:** New analysis/written issue
- 2025 output: 51 podcast episodes + 39 written-only issues = ~90 issues/year

**Content Structure (per issue):**
- Deep-dive creator profiles (primary format)
- Full interview transcripts/summaries
- Revenue breakdowns and real numbers
- Growth strategy breakdowns
- "Tactic section to steal and implement"
- ~15-minute read time per issue

**Content Categories:**
- Creator growth strategies
- Revenue/monetization breakdowns
- Platform-specific tactics
- Creator economy trends and analysis
- Behind-the-scenes of creator businesses
- Year-end retrospectives and "best of" compilations

**Featured Creator Examples:**
- Ryan Duffy -- "Covering the business and policy of space"
- Smart Nonsense -- "Zero to 10,000 Subscribers in One Month on beehiiv"
- Roland Frasier -- "32,000 Subscribers in 3 Months on beehiiv"
- Lia Haberman -- "The 3-year creator shelf life"
- Deuxmoi -- 2M Instagram followers, multi-platform

**Social Proof:**
- ~370K subscribers (post-cleaning Jan 2026, down from ~421K)
- Companion podcast on Apple Podcasts, YouTube
- Social presence: Twitter (@creator__spot), Instagram (@creator__spotlight), LinkedIn, TikTok (@creator_spotlight)
- beehiiv's flagship owned newsletter -- institutional credibility

**Monetization Model:**
- Primarily through sponsorships (sponsor click rate tracked: 0.38% for FB ads subscribers)
- Not directly monetized via subscriptions (free newsletter)
- Cross-promotes podcast and YouTube as distribution channels
- Serves as brand/credibility asset for beehiiv ecosystem

**Signup Flow:**
- Standard beehiiv subscribe page at creatorspotlight.com/subscribe
- Email input with subscribe CTA
- No visible lead magnet on homepage (lead magnets used in ad creatives: "0-10K guide")

**Author:** Francis Zierer (editor and primary contact)

### Value Proposition Analysis

**What CS promises:** Access to real creator stories with actionable insights -- the behind-the-scenes of how creators actually grow and make money.

**What CS actually delivers:** Long-form creator profiles combining interview content with tactical breakdowns. Not generic advice -- specific revenue numbers, growth timelines, and implementable strategies from real creators.

**Positioning:** "Real journalism" about the creator economy. Positioned as the antithesis of guru/hustle culture content. Editorial quality aspirations comparable to NYT/New Yorker.

**Key differentiator vs. competitors:** CS goes deep on individual creators (full profiles + podcast) rather than covering news or offering generic advice. It's the only major creator economy newsletter owned by a platform (beehiiv), giving it institutional backing and access.

---

## TASK 4: Competitor Research

### 1. The Publish Press

| Attribute | Detail |
|-----------|--------|
| **Founded by** | Colin Rosenblum & Samir Chaudry (Colin and Samir) |
| **Launched** | April 2021 |
| **Subscribers** | ~160K+ (2026 estimate) |
| **Platform** | beehiiv (migrated from Substack) |
| **Frequency** | Twice weekly (Tuesdays & Fridays) |
| **Format** | Curated news briefing -- top 3 creator economy news stories per issue |
| **Positioning** | "News about Creators by Creators" -- created by two long-time creators for career creators, aspiring creators, and industry professionals |
| **Value prop** | Quick, curated creator economy news with context on why it matters. "Finish each issue more educated and empowered to press publish yourself." |
| **Monetization** | Sponsorships |
| **Key differentiator** | Founded by prominent YouTube creators (Colin and Samir have 4M+ YouTube subscribers), giving them industry credibility and insider access |

**CS vs. The Publish Press:**
- TPP covers *news*; CS covers *people* (creator profiles/interviews)
- TPP is brief/curated (top 3 stories); CS is long-form/deep-dive (~15 min read)
- TPP has smaller but highly engaged audience; CS has 2x+ the subscriber base
- Both target creator economy professionals but at different stages of the content funnel (TPP = staying informed; CS = learning strategy)

### 2. ICYMI by Lia Haberman

| Attribute | Detail |
|-----------|--------|
| **Founded by** | Lia Haberman (UCLA lecturer, consultant) |
| **Subscribers** | ~45-47K (across LinkedIn + Substack) |
| **Platform** | Substack |
| **Frequency** | Weekly |
| **Format** | Weekly debrief of platform updates, social and creator marketing news, audience insights |
| **Positioning** | Expert analysis at the intersection of social media, creator economy, and influencer marketing |
| **Value prop** | "Keep track of weekly platform updates, brand social and creator marketing news, and audience insights" |
| **Recognition** | Buffer Best Marketing Newsletter (2023-2025), Business Insider Top Creator Economy Expert, Google top result for "Creator Economy Expert" |
| **Key differentiator** | Academic credibility (UCLA) + practitioner perspective. More marketing/brand-focused than creator-focused. |

**CS vs. ICYMI:**
- ICYMI targets *marketers and brands* working with creators; CS targets *creators themselves*
- ICYMI covers platform/industry analysis; CS covers individual creator journeys
- CS has 8x the subscriber base but different audience composition
- ICYMI is positioned as expert commentary; CS is positioned as journalistic storytelling

### 3. Passionfruit (The Daily Dot)

| Attribute | Detail |
|-----------|--------|
| **Publisher** | Fragment Media Group LLC (registered benefit company), via The Daily Dot |
| **Editor** | Grace Stanley |
| **Subscribers** | Not publicly disclosed |
| **Platform** | Custom (passionfru.it) |
| **Frequency** | Twice weekly |
| **Format** | Creator profiles, interviews with business leaders, creator advice, internet trend deep-dives |
| **Positioning** | "The aspiring creator's guide for navigating the booming, ever-changing creator economy" -- independent journalistic newsletter |
| **Value prop** | The inside scoop on the creator economy; learn to "thrive as a small business with big influence." Covers contracts, money, and labor dynamics. |
| **Key differentiator** | Independent journalism angle (benefit company). Covers underrepresented creator subcultures. More labor/business-of-creation focused. |

**CS vs. Passionfruit:**
- Both do creator profiles/interviews but CS focuses on *growth/revenue success stories* while Passionfruit covers *labor dynamics, contracts, and underrepresented voices*
- CS has institutional backing (beehiiv); Passionfruit has editorial independence (benefit company)
- CS targets aspiring/active creators; Passionfruit targets the same but with more emphasis on business navigation
- CS has significantly larger audience

### 4. The Leap (by Thinkific)

| Attribute | Detail |
|-----------|--------|
| **Publisher** | Thinkific |
| **Subscribers** | Not publicly disclosed |
| **Platform** | Custom (theleap.co) |
| **Frequency** | Weekly (Thursdays) |
| **Format** | 5-minute breakdown of advice, tips, and stories |
| **Positioning** | Actionable creator advice for making money online -- emphasizes first-dollar moments |
| **Value prop** | "Analyzes trends, helps monetize, provides tips on audience growth, and keeps you informed of the biggest news in the creator economy" |
| **Origin** | Started as a TikTok account, grew into digital media property |
| **Key differentiator** | Part of Thinkific ecosystem (course platform). Targets earliest-stage creators. Short, actionable format. Emphasizes "making your first leap." |

**CS vs. The Leap:**
- The Leap targets *pre-revenue/earliest-stage creators*; CS targets *aspiring to established creators*
- The Leap is brief (5 min); CS is deep (15 min)
- The Leap is advice-driven; CS is story-driven
- The Leap has platform backing (Thinkific); CS has platform backing (beehiiv) -- similar institutional dynamics
- The Leap's TikTok-first origin attracts younger demos; CS's audience skews 35-55, 70% female

### Competitive Landscape Summary

| Newsletter | Subscribers | Format | Frequency | Primary Angle | ICP Overlap with CS |
|-----------|------------|--------|-----------|---------------|-------------------|
| **Creator Spotlight** | ~370K | Deep-dive profiles | 2x/week | Creator success stories + tactics | -- |
| **The Publish Press** | ~160K | News briefing | 2x/week | Creator economy news | Medium -- different content type |
| **ICYMI** | ~47K | Weekly analysis | Weekly | Platform/marketing analysis | Low -- different audience (marketers) |
| **Passionfruit** | Undisclosed | Profiles + analysis | 2x/week | Creator labor/business | High -- similar format, different tone |
| **The Leap** | Undisclosed | Quick tips | Weekly | Beginner monetization | Medium -- overlaps with "Aspiring Alex" ICP |

### Competitive Positioning Map

```
                    NEWS/ANALYSIS ←→ STORIES/PROFILES
                         |
    ICYMI .............. | ........................ Passionfruit
    (marketer-focused)   |                        (labor-focused)
                         |
    The Publish Press .. |
    (news briefing)      |
                         |
                         |          CREATOR SPOTLIGHT
                         |          (success stories +
                         |           deep tactical profiles)
                         |
    The Leap ........... |
    (beginner tips)      |
                         |
              BEGINNER ←→ ESTABLISHED
```

### Competitive Advantages for Creator Spotlight

1. **Scale:** ~370K subscribers dwarfs all competitors in the creator economy newsletter space
2. **Institutional backing:** beehiiv ownership provides platform credibility and data access
3. **Depth:** Full podcast + written profiles provide the deepest creator coverage
4. **Dual format:** Newsletter + podcast creates multiple engagement touchpoints
5. **Real numbers:** Revenue breakdowns and growth timelines provide tangible value competitors often lack
6. **Editorial quality:** "Real journalism" standard sets a higher bar than advice-driven competitors

### Competitive Vulnerabilities

1. **Budget constraints:** $2K/week ceiling limits paid growth while competitors scale
2. **Audience fatigue:** ~370K plateau for over a year suggests organic ceiling
3. **Platform dependency:** Being beehiiv-owned may limit perceived editorial independence
4. **Narrow format:** Profile-only format could feel repetitive vs. news-driven competitors
5. **Subscriber quality:** List cleaning (421K to 366K) revealed engagement challenges

---

## Strategic Implications for Ad Creative

### What competitors tell us about CS positioning in ads:

1. **Lean into the "depth" angle:** No competitor goes as deep on individual creators. Ad copy should emphasize "the full story" vs. "quick tips" or "news briefs."

2. **"Real journalism" is the moat:** The Publish Press is creator-made news; ICYMI is expert analysis; Passionfruit is independent journalism. CS's unique position is *beehiiv-backed editorial journalism* -- combine institutional access with editorial quality.

3. **The Leap overlap is the biggest ICP threat:** Both target aspiring creators with platform backing. But CS's audience (35-55, 70% female) is distinctly different from The Leap's younger, TikTok-native audience. Ad creative should speak to the "Aspiring Alex" and "Pivoting Pat" ICPs specifically.

4. **Passionfruit is the closest content competitor:** Similar format (profiles + interviews) but different editorial lens. CS can differentiate by emphasizing *success and possibility* vs. Passionfruit's *labor and challenges* framing.

5. **Anti-guru positioning remains powerful:** No competitor occupies the "anti-guru" space as aggressively as CS's best-performing ads (DCT 106, DCT 164). This is white space in the competitive landscape.

---

*Sources: Google Drive (45 files across 3 search queries), Notion (25+ pages including Creative Hub DB, Concept Validation DB, bi-weekly reports, client intelligence), creatorspotlight.com, beehiiv.com/newsletter-glossary/creator-spotlight, emailtooltester.com, publishpress.substack.com, passionfru.it, theleap.co, liahaberman.substack.com, web search results. Compiled March 21, 2026.*
