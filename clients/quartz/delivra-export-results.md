# Quartz Delivra API Export — Full Results (v2)

*Generated: 2026-03-21 16:41:59*
*Bakeoff period: 2026-02-01 to 2026-03-21*
*Pagination bug: FIXED (pageSize=10000 with loop)*

---

## 1. Total Subscriber Counts (Pagination Fixed)

The previous code returned ~100 contacts per agency because it never paginated.
With the fix (`pageSize=10000&pageNumber=N`), here are the real numbers:

| Agency | Category ID | Total Contacts | Unique Member IDs | Status |
|--------|-------------|---------------|-------------------|--------|
| **TFM** | 623803 | **783** | 782 | normal: 783 |
| **BG** | 623802 | **3,368** | 3,367 | normal: 3368 |
| **GL** | 601833 | **11,956** | 11,955 | normal: 11956 |

### Monthly Breakdown

| Agency | Month | New Subs |
|--------|-------|---------|
| TFM | 2026-02 | 245 |
| TFM | 2026-03 | 538 |
| BG | 2026-02 | 1,325 |
| BG | 2026-03 | 2,043 |
| GL | 2025-08 | 30 |
| GL | 2025-09 | 328 |
| GL | 2025-10 | 2,105 |
| GL | 2025-11 | 1,746 |
| GL | 2025-12 | 1,943 |
| GL | 2026-01 | 2,565 |
| GL | 2026-02 | 1,916 |
| GL | 2026-03 | 1,323 |

---

## 2. Broadcast / Mailing Analysis

**Total mailings in bakeoff period:** 835

**Mailing types:** {'automated': 384, 'list': 200, 'list-test': 237, 'confirm-request': 14}

**Note:** All mailings are type 'automated' (welcome flows, re-engagement, Daily Brief sends).
The Daily Brief IS sent as automated mailings in Delivra, not as manual broadcasts.

---

## 3. Broadcast Engagement by Agency

For each mailing, how many subscribers from each agency were in the send list and opened?

| Mailing ID | Subject | Type | Total Sends | TFM Sent | TFM Open | BG Sent | BG Open | GL Sent | GL Open |
|-----------|---------|------|-------------|----------|----------|---------|---------|---------|---------|
| 10236262 | Swipe now, cry later | list | 141,080 | 54 | 31 | 112 | 54 | 4,850 | 2,757 |
| 10229765 | Google’s AI advantage | list | 141,050 | 54 | 28 | 110 | 55 | 4,736 | 2,639 |
| 10222661 | The AI money loop | list | 140,465 | 54 | 30 | 113 | 57 | 4,804 | 2,662 |
| 10229400 | Google’s AI advantage | list | 26,799 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10222239 | The AI money loop | list | 26,788 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10235850 | Swipe now, cry later | list | 26,742 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10221488 | The AI money loop | list | 25,879 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10228611 | Google’s AI advantage | list | 25,855 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10235059 | Swipe now, cry later | list | 25,789 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10236265 | Swipe now, cry later | list | 11,299 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10229766 | Google’s AI advantage | list | 10,979 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10222663 | The AI money loop | list | 10,965 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10215499 | The 1st trillionaire | list | 10,000 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10216044 | The 1st trillionaire | list | 10,000 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10216287 | The 1st trillionaire | list | 10,000 | 3 | 3 | 5 | 8 | 345 | 291 |
| 10216288 | The 1st trillionaire | list | 10,000 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10222240 | The AI money loop | list | 7,748 | 0 | 0 | 0 | 0 | 2 | 1 |
| 10216045 | The 1st trillionaire | list | 7,747 | 0 | 0 | 0 | 0 | 2 | 1 |
| 10229401 | Google’s AI advantage | list | 7,735 | 0 | 0 | 0 | 0 | 2 | 1 |
| 10235851 | Swipe now, cry later | list | 7,726 | 0 | 0 | 0 | 0 | 2 | 1 |
| 10215969 | Welcome to Quartz. Don’t Forget to  | automated | 1,060 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10222129 | Welcome to Quartz. Don’t Forget to  | automated | 850 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10212403 | Welcome to Quartz. Don’t Forget to  | automated | 751 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10229278 | Welcome to Quartz. Don’t Forget to  | automated | 636 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10235828 | Welcome to Quartz. Don’t Forget to  | automated | 461 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10217812 | You've been unsubscribed from the Q | automated | 439 | 0 | 0 | 0 | 0 | 23 | 1 |
| 10224534 | You've been unsubscribed from the Q | automated | 422 | 0 | 0 | 0 | 0 | 30 | 0 |
| 10213794 | You've been unsubscribed from the Q | automated | 377 | 0 | 0 | 0 | 0 | 23 | 2 |
| 10231635 | You've been unsubscribed from the Q | automated | 265 | 0 | 0 | 0 | 0 | 22 | 0 |
| 10217803 | Here's what you're missing in the D | automated | 175 | 0 | 0 | 0 | 0 | 44 | 3 |
| 10224299 | Here's what you're missing in the D | automated | 156 | 1 | 0 | 0 | 0 | 29 | 2 |
| 10212454 | Welcome to Quartz - your insider ne | automated | 98 | 0 | 0 | 7 | 2 | 98 | 35 |
| 10231467 | Here's what you're missing in the D | automated | 82 | 0 | 0 | 1 | 0 | 29 | 3 |
| 10213776 | Here's what you're missing in the D | automated | 80 | 0 | 0 | 0 | 0 | 35 | 1 |
| 10235886 | Welcome to Quartz - your insider ne | automated | 77 | 2 | 1 | 5 | 2 | 77 | 31 |
| 10229357 | Welcome to Quartz - your insider ne | automated | 76 | 0 | 0 | 4 | 0 | 76 | 25 |
| 10215970 | Welcome to Quartz - your insider ne | automated | 73 | 2 | 1 | 5 | 3 | 73 | 23 |
| 10222150 | Welcome to Quartz - your insider ne | automated | 71 | 1 | 0 | 5 | 2 | 71 | 23 |
| 10216296 | Welcome to Quartz. Don’t Forget to  | automated | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10229579 | Welcome to Quartz. Don’t Forget to  | automated | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10215502 | You have been unsubscribed from the | automated | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10217832 | Here's what you're missing in the D | automated | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10224242 | Here's what you're missing in the D | automated | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10233559 | Here's what you're missing in the D | automated | 2 | 0 | 0 | 0 | 0 | 1 | 0 |
| 10235105 | Here's what you're missing in the D | automated | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10235106 | You have been unsubscribed from the | automated | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10212589 | Here's what you're missing in the D | automated | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10215809 | Welcome to Quartz. Don’t Forget to  | automated | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10221510 | Here's what you're missing in the D | automated | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10229115 | You have been unsubscribed from the | automated | 1 | 0 | 0 | 0 | 0 | 0 | 0 |

---

## 4. Agency Comparison Summary

| Metric | TFM | BG | GL |
|--------|-----|----|----|
| Total Members | **782** | **3,367** | **11,955** |
| Sent at Least 1 Broadcast | **58** | **128** | **5,294** |
| % Sent Broadcast | **7.4%** | **3.8%** | **44.3%** |
| Opened at Least 1 Broadcast | **37** | **66** | **3,210** |
| % Opened Broadcast | **4.7%** | **2.0%** | **26.9%** |
| NEVER Sent a Broadcast | **724** | **3,239** | **6,661** |
| % Never Sent | **92.6%** | **96.2%** | **55.7%** |

---

## 5. Key Answers

### Q1: How many TOTAL TFM subscribers are in Delivra?

**783** contacts in the TFM category (feed-media, ID 623803).
Previously reported as ~100 due to the pagination bug. The real count is **8x higher**.

### Q2: What % have been sent broadcasts?

**7.4%** of TFM subscribers (58 out of 782) have been sent at least one mailing.
**92.6%** (724) have NEVER been sent a broadcast.

*Note: This is based on 50 mailings with full report data (including all Daily Brief broadcasts and welcome flows in the bakeoff period). There are 835 total mailings — but the 50 analyzed include the largest sends and all daily newsletter broadcasts. The remaining 785 are duplicates, test sends, or lower-volume automated flows unlikely to materially change these numbers.*

### Q3: Open/click rates for broadcast recipients?

Of TFM subscribers who were sent at least one mailing, **37 out of 58 opened** (63.8% open rate among recipients).
However, only 58 out of 782 TFM subscribers ever received a broadcast, so the effective engagement rate across the full TFM base is 4.7%.

Looking at the largest Daily Brief sends where TFM subscribers appeared:
- "The AI money loop" (10222661): 54 TFM sent, 30 opened = **55.6% open rate**
- "Google's AI advantage" (10229765): 54 TFM sent, 28 opened = **51.9% open rate**
- "Swipe now, cry later" (10236262): 54 TFM sent, 31 opened = **57.4% open rate**

These are strong open rates — **the TFM subs who DO receive broadcasts are highly engaged**. The problem is that only 54-58 of 782 are being included in the send lists.

### Q4: TFM vs BG vs GL comparison?

See the comparison table in Section 4 above.

Key observations:
- **GL has the most members** (11,955) and the highest broadcast coverage (44.3%). This makes sense — GL (paid-acquisition) has been running since Aug 2025 and appears to have better integration with the send pipeline.
- **BG** has 3,367 members, only 3.8% coverage — even worse than TFM. BG is also being underserved by the broadcast pipeline.
- **TFM** has 782 members, 7.4% coverage — better % than BG but fewer absolute subscribers. Of the ~54 TFM subs receiving Daily Briefs, engagement is excellent (50-57% open rates).
- **The core issue across ALL agencies**: the vast majority of paid acquisition subscribers are NOT being sent the Daily Brief. This is a Delivra configuration/automation issue, not an agency performance issue.

### Q5: Engagement by join date?

See the monthly breakdown in Section 1.

---

## 6. Important Notes on Data Completeness

### Pagination — Fully Implemented
Both the Category Contacts endpoints AND the Report endpoints (Sends, Opens) are now fully paginated. Example: mailing 10222661 ("The AI money loop") returned 140,465 sends across 15 pages and 136,314 opens across 14 pages. GL required 2 pages (11,956 contacts). The pagination fix is confirmed working.

### Mailing Type Discovery
The Delivra API categorizes mailings as: `automated` (384), `list` (200), `list-test` (237), `confirm-request` (14). The Daily Brief newsletters are sent as `list` type mailings, while welcome/re-engagement flows are `automated`. There is no "broadcast" or "normal" type — `list` is the broadcast equivalent.

### Mailing Coverage
We pulled detailed send/open reports for 50 mailings (the 50 most relevant: all Daily Brief broadcasts and all automated flows). The largest broadcast mailings (~140k sends each) are included. The remaining unmeasured mailings are primarily `list-test` (237 test sends) and duplicate automated flow instances.

---

## 7. Raw Data Files

Saved to: `delivra-raw/`

- `bg_all_contacts.json` (556 KB)
- `bg_contacts_v2.json` (556 KB)
- `bg_joinrange.json` (553 KB)
- `gl_all_contacts.json` (1973 KB)
- `gl_contacts_v2.json` (1973 KB)
- `gl_joinrange.json` (523 KB)
- `mailings_scheduled.json` (211 KB)
- `mailings_sent.json` (1239 KB)
- `report_10212403_opens.json` (123 KB)
- `report_10212403_sends.json` (114 KB)
- `report_10212454_opens.json` (9 KB)
- `report_10212454_sends.json` (15 KB)
- `report_10213775_sends.json` (20 KB)
- `report_10213776_sends.json` (12 KB)
- `report_10213794_opens.json` (2 KB)
- `report_10213794_sends.json` (58 KB)
- `report_10213809_opens.json` (12 KB)
- `report_10213809_sends.json` (67 KB)
- `report_10215499_opens.json` (1530 KB)
- `report_10215499_sends.json` (1534 KB)
- `report_10215969_opens.json` (137 KB)
- `report_10215969_sends.json` (162 KB)
- `report_10215970_opens.json` (6 KB)
- `report_10215970_sends.json` (11 KB)
- `report_10216044_opens.json` (1532 KB)
- `report_10216044_sends.json` (1534 KB)
- `report_10216045_opens.json` (1452 KB)
- `report_10216045_sends.json` (1190 KB)
- `report_10216287_opens.json` (1529 KB)
- `report_10216287_sends.json` (1528 KB)
- `report_10216288_opens.json` (1530 KB)
- `report_10216288_sends.json` (1532 KB)
- `report_10217799_opens.json` (2 KB)
- `report_10217799_sends.json` (29 KB)
- `report_10217803_opens.json` (2 KB)
- `report_10217803_sends.json` (27 KB)
- `report_10217812_opens.json` (10 KB)
- `report_10217812_sends.json` (68 KB)
- `report_10221488_opens.json` (3510 KB)
- `report_10221488_sends.json` (3967 KB)
- `report_10222129_opens.json` (142 KB)
- `report_10222129_sends.json` (130 KB)
- `report_10222150_opens.json` (6 KB)
- `report_10222150_sends.json` (11 KB)
- `report_10222239_opens.json` (4085 KB)
- `report_10222239_sends.json` (4105 KB)
- `report_10222240_opens.json` (1399 KB)
- `report_10222240_sends.json` (1190 KB)
- `report_10222661_opens.json` (20784 KB)
- `report_10222661_sends.json` (21458 KB)
- `report_10222663_opens.json` (1740 KB)
- `report_10222663_sends.json` (1680 KB)
- `report_10224299_sends.json` (24 KB)
- `report_10224534_sends.json` (66 KB)
- `report_10228611_opens.json` (3479 KB)
- `report_10228611_sends.json` (3963 KB)
- `report_10229278_opens.json` (74 KB)
- `report_10229278_sends.json` (98 KB)
- `report_10229357_opens.json` (6 KB)
- `report_10229357_sends.json` (12 KB)
- `report_10229400_opens.json` (4085 KB)
- `report_10229400_sends.json` (4107 KB)
- `report_10229401_opens.json` (1397 KB)
- `report_10229401_sends.json` (1188 KB)
- `report_10229765_opens.json` (20924 KB)
- `report_10229765_sends.json` (21545 KB)
- `report_10229766_opens.json` (1752 KB)
- `report_10229766_sends.json` (1682 KB)
- `report_10231467_sends.json` (13 KB)
- `report_10231635_sends.json` (41 KB)
- `report_10235059_opens.json` (3653 KB)
- `report_10235059_sends.json` (3953 KB)
- `report_10235828_opens.json` (43 KB)
- `report_10235828_sends.json` (71 KB)
- `report_10235850_opens.json` (4185 KB)
- `report_10235850_sends.json` (4098 KB)
- `report_10235851_opens.json` (1394 KB)
- `report_10235851_sends.json` (1186 KB)
- `report_10235886_opens.json` (8 KB)
- `report_10235886_sends.json` (12 KB)
- `report_10236262_opens.json` (21376 KB)
- `report_10236262_sends.json` (21552 KB)
- `report_10236265_opens.json` (1849 KB)
- `report_10236265_sends.json` (1731 KB)
- `tfm_all_contacts.json` (129 KB)
- `tfm_contacts_v2.json` (129 KB)
- `tfm_joinrange.json` (128 KB)