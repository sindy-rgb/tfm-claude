# Quartz Delivra API Export — Full Results

*Generated: 2026-03-21 16:22:28*

*Bakeoff period: 2026-02-01 to 2026-03-21*

---

## 1. Total Subscriber Counts (Paginated)

| Agency | Total in Category | Bakeoff Subs | Status Breakdown |
|--------|------------------|--------------|------------------|
| TFM | 0 | 0 |  |
| BG | 0 | 0 |  |
| GL | 0 | 0 |  |

### Monthly Breakdown

| Agency | Month | Count |
|--------|-------|-------|

---

## 2. JoinRange Endpoint Results

- **TFM**: 0 contacts via JoinRange

- **BG**: 0 contacts via JoinRange

- **GL**: 0 contacts via JoinRange

---

## 3. ContactCountByStatus

```json
"\ufeff[{\"MemberType_\":\"unsub\",\"MemberCount_\":26804},{\"MemberType_\":\"normal\",\"MemberCount_\":694111},{\"MemberType_\":\"confirm\",\"MemberCount_\":183},{\"MemberType_\":\"held\",\"MemberCount_\":40020}]"
```

---

## 4. Broadcast / Mailing Data

No mailings returned from API.

---

## 5. Account-Wide Report Data

- **Sends**: ERROR — HTTP 400: Failed to populate datatable.

- **Opens**: ERROR — HTTP 400: Failed to populate datatable.

- **Clickthroughs**: ERROR — HTTP 400: Failed to populate datatable.

- **SubscriberActivity**: ERROR — HTTP 400: The added or subtracted value results in an un-representable DateTime.
Parameter name: va

---

## 6. Engagement Analysis by Agency

| Agency | Total | With Engagement | Avg Score | Zero Eng | Low | Mid | High | Very High |
|--------|-------|----------------|-----------|----------|-----|-----|------|-----------|
| TFM | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 |
| BG | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 |
| GL | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 |

---

## 7. Discovery Endpoints

- `/Segments`: {'raw': '\ufeff[{"ClauseFrom":"","ClauseOrderBy":"","ClauseSelect":"","Description":"Finding contacts that belong to all groups selected.","List":"quartz-prod","Name":"_DLVRA example 1","SegmentType":

- `/Categories`: {'raw': '\ufeff[{"ID":596174,"List_":"quartz-prod","Name":"07-02-2025-Unsubscribe","SubsetID_":640763,"Description":"Import ID 908469, 07/02/2025 06:51:55","IsImport":true,"IsReadOnly":false,"Director

- `/Contacts/HeldRange`: {'raw': '\ufeff[{"DateHeld":"2026-03-12T10:20:00.0000000Z","DateJoined":"2025-06-12T22:26:00.0000000Z","DomainName":"icloud.com","EmailAddress":"shehanilangahoon@icloud.com","List":"quartz-prod","Mail

- `/Contacts/ListModified`: {'raw': '\ufeff[{"DateJoined":"2026-02-01T05:01:00.0000000Z","DomainName":"gmail.com","EmailAddress":"janicemancia@gmail.com","List":"quartz-prod","MailFormatPreferred":"M","MemberID":228905089,"Membe

---

## 8. Key Findings & Answers

### Q1: How many TOTAL TFM subscribers are in Delivra?

**0** total contacts in the TFM category (previously capped at ~100 due to pagination bug).

### Q2: What % have been sent broadcasts?

*(Derived from Reports API data above — see section 4 and 5)*

### Q3: Open/click rates for those who received broadcasts?

*(See per-mailing report data in section 4)*

### Q4: TFM vs BG vs GL comparison?

| Metric | TFM | BG | GL |
|--------|-----|----|----|
| total_in_category | 0 | 0 | 0 |
| bakeoff_subs | 0 | 0 | 0 |
| avg_engagement | 0.0 | 0.0 | 0.0 |
| contacts_with_engagement | 0 | 0 | 0 |

### Q5: Engagement by join date?

*(See monthly breakdown in section 1)*

---

## 9. Raw Data Files

All raw API responses saved to: `/Users/jay/Documents/the vault/the-feed-media/clients/quartz/delivra-raw/`