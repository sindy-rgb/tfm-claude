#!/usr/bin/env python3
"""
Quartz Delivra API Export — Full Subscriber + Broadcast Engagement Data
Fixes the pagination bug and pulls complete datasets for TFM, BG, GL.
"""

import requests
import json
import os
import sys
from datetime import datetime, timedelta
from collections import defaultdict

# === CONFIG ===
BASE_URL = "https://integration.delivra.com/DelivraRESTServices/Services.svc"
USERNAME = "aroggio+newsletter-ops@qz.com"
PASSWORD = "N3ws-Qu@rtz-Ops"
LISTNAME = "quartz-prod"
PAGE_SIZE = 10000

AGENCIES = [
    {"name": "TFM", "category_id": 623803, "category_name": "feed-media"},
    {"name": "BG", "category_id": 623802, "category_name": "boletin"},
    {"name": "GL", "category_id": 601833, "category_name": "paid-acquisition"},
]

BAKEOFF_START = "2026-02-01"
TODAY = datetime.now().strftime("%Y-%m-%d")

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.join(OUT_DIR, "delivra-raw")
os.makedirs(RAW_DIR, exist_ok=True)

HEADERS = {
    "username": USERNAME,
    "password": PASSWORD,
    "listname": LISTNAME,
    "Accept": "application/json",
    "Content-Type": "application/json",
}


def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")


def save_raw(filename, data):
    path = os.path.join(RAW_DIR, filename)
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)
    log(f"  Saved raw: {filename} ({len(data) if isinstance(data, list) else 'obj'})")
    return path


def parse_delivra_json(text):
    """Parse Delivra API response, stripping BOM and handling edge cases."""
    # Strip UTF-8 BOM (byte order mark) - Delivra prepends this
    clean = text.lstrip('\ufeff').strip()
    if not clean:
        return None
    return json.loads(clean)


def api_get(endpoint, params=None, label="", timeout=120):
    """Make a GET request to the Delivra API with error handling."""
    url = f"{BASE_URL}{endpoint}"
    try:
        resp = requests.get(url, headers=HEADERS, params=params, timeout=timeout)
        log(f"  {label or endpoint} -> HTTP {resp.status_code} ({len(resp.content)} bytes)")
        if resp.status_code == 200:
            try:
                return parse_delivra_json(resp.text), None
            except (json.JSONDecodeError, ValueError) as e:
                log(f"  JSON parse error: {e}")
                log(f"  First 200 chars: {resp.text[:200]}")
                return resp.text, None
        else:
            return None, f"HTTP {resp.status_code}: {resp.text[:500]}"
    except requests.exceptions.RequestException as e:
        return None, f"Request error: {str(e)}"


def paginated_get(endpoint, params=None, label="", timeout=120):
    """Paginate through a Delivra API endpoint."""
    all_items = []
    page = 1
    if params is None:
        params = {}

    while True:
        params["pageSize"] = PAGE_SIZE
        params["pageNumber"] = page
        data, err = api_get(endpoint, params=params, label=f"{label} page {page}", timeout=timeout)
        if err:
            log(f"  ERROR on page {page}: {err}")
            break
        if not isinstance(data, list):
            log(f"  Non-list response on page {page}: {type(data)}")
            if isinstance(data, dict) and "Results" in data:
                items = data["Results"]
            else:
                break
        else:
            items = data

        all_items.extend(items)
        log(f"  Page {page}: {len(items)} items (total so far: {len(all_items)})")

        if len(items) < PAGE_SIZE:
            break
        page += 1

    return all_items


# === PHASE 1: Pull All Category Contacts (Paginated) ===
def phase1_category_contacts():
    log("=" * 60)
    log("PHASE 1: Pulling ALL category contacts with pagination")
    log("=" * 60)

    results = {}

    for agency in AGENCIES:
        log(f"\n--- {agency['name']} (category {agency['category_id']}) ---")

        contacts = paginated_get(
            f"/Categories/{agency['category_id']}/Contacts",
            label=f"{agency['name']} contacts"
        )
        save_raw(f"{agency['name'].lower()}_all_contacts.json", contacts)

        # Filter to bakeoff period
        bakeoff = []
        status_counts = defaultdict(int)
        monthly = defaultdict(int)

        for c in contacts:
            joined = (c.get("DateJoined") or "")[:10]
            member_type = (c.get("MemberType") or c.get("memberType") or "unknown").lower()
            status_counts[member_type] += 1

            if joined >= BAKEOFF_START:
                bakeoff.append(c)
                month_key = joined[:7]  # YYYY-MM
                monthly[month_key] += 1

        results[agency["name"]] = {
            "total_in_category": len(contacts),
            "bakeoff_subs": len(bakeoff),
            "status_breakdown": dict(status_counts),
            "monthly_breakdown": dict(sorted(monthly.items())),
            "contacts": contacts,
            "bakeoff_contacts": bakeoff,
        }

        log(f"  Total: {len(contacts)}, Bakeoff: {len(bakeoff)}")
        log(f"  Status: {dict(status_counts)}")
        log(f"  Monthly: {dict(sorted(monthly.items()))}")

    return results


# === PHASE 1B: Try JoinRange Endpoint ===
def phase1b_join_range():
    log("\n" + "=" * 60)
    log("PHASE 1B: Trying JoinRange endpoint for bakeoff period")
    log("=" * 60)

    results = {}

    for agency in AGENCIES:
        log(f"\n--- {agency['name']} JoinRange ---")

        contacts = paginated_get(
            f"/Categories/{agency['category_id']}/Contacts/JoinRange",
            params={"startDate": BAKEOFF_START, "endDate": TODAY},
            label=f"{agency['name']} JoinRange"
        )
        save_raw(f"{agency['name'].lower()}_joinrange.json", contacts)
        results[agency["name"]] = {"joinrange_count": len(contacts), "contacts": contacts}
        log(f"  JoinRange total: {len(contacts)}")

    return results


# === PHASE 1C: Try ContactCountByStatus ===
def phase1c_contact_counts():
    log("\n" + "=" * 60)
    log("PHASE 1C: Trying ContactCountByStatus endpoint")
    log("=" * 60)

    data, err = api_get("/Contacts/ContactCountByStatus", label="ContactCountByStatus")
    if err:
        log(f"  ERROR: {err}")
    else:
        save_raw("contact_count_by_status.json", data if isinstance(data, (list, dict)) else {"raw": data})
        log(f"  Result: {data}")
    return data


# === PHASE 2: Broadcast / Mailing Data ===
def phase2_broadcasts():
    log("\n" + "=" * 60)
    log("PHASE 2: Pulling broadcast/mailing data")
    log("=" * 60)

    results = {"mailings": [], "reports": {}}

    # Try /Mailings/Sent
    log("\n--- Mailings/Sent ---")
    mailings = paginated_get(
        "/Mailings/Sent",
        params={"startDate": BAKEOFF_START, "endDate": TODAY},
        label="Mailings/Sent"
    )
    if not mailings:
        # Try without date params
        log("  Trying without date params...")
        mailings, err = api_get("/Mailings/Sent", label="Mailings/Sent (no dates)")
        if err:
            log(f"  ERROR: {err}")
            mailings = []
        elif isinstance(mailings, list):
            pass
        else:
            mailings = []

    save_raw("mailings_sent.json", mailings if isinstance(mailings, list) else [mailings])
    results["mailings"] = mailings if isinstance(mailings, list) else []
    log(f"  Total mailings found: {len(results['mailings'])}")

    # Try alternative mailing endpoints
    for alt_endpoint in ["/Mailings", "/Mailings/All", "/Mailings/Scheduled"]:
        log(f"\n--- Trying {alt_endpoint} ---")
        data, err = api_get(alt_endpoint, label=alt_endpoint)
        if err:
            log(f"  ERROR: {err}")
        else:
            save_raw(f"mailings_{alt_endpoint.split('/')[-1].lower()}.json",
                      data if isinstance(data, (list, dict)) else {"raw": data})
            if isinstance(data, list):
                log(f"  Found {len(data)} items")

    # For each mailing, try to get report data
    mailing_list = results["mailings"][:20]  # Cap at 20 to avoid rate limits
    for mailing in mailing_list:
        mailing_id = mailing.get("MessageID") or mailing.get("MailingID") or mailing.get("ID") or mailing.get("id")
        if not mailing_id:
            log(f"  Skipping mailing with no ID: {list(mailing.keys())[:5]}")
            continue

        mailing_name = mailing.get("Subject") or mailing.get("Name") or mailing.get("name") or str(mailing_id)
        log(f"\n  --- Report for mailing {mailing_id}: {mailing_name[:50]} ---")

        report = {"mailing_id": mailing_id, "name": mailing_name}

        # Sends
        sends, err = api_get(f"/Reports/{mailing_id}/Sends",
                              params={"pageSize": PAGE_SIZE, "pageNumber": 1},
                              label=f"Sends for {mailing_id}")
        if err:
            report["sends_error"] = err
        else:
            if isinstance(sends, list):
                report["sends_count"] = len(sends)
                save_raw(f"report_{mailing_id}_sends.json", sends)
            else:
                report["sends_data"] = sends

        # Opens
        opens, err = api_get(f"/Reports/{mailing_id}/Opens",
                              params={"pageSize": PAGE_SIZE, "pageNumber": 1},
                              label=f"Opens for {mailing_id}")
        if err:
            report["opens_error"] = err
        else:
            if isinstance(opens, list):
                report["opens_count"] = len(opens)
                save_raw(f"report_{mailing_id}_opens.json", opens)
            else:
                report["opens_data"] = opens

        # Clickthroughs
        clicks, err = api_get(f"/Reports/{mailing_id}/Clickthroughs",
                               params={"pageSize": PAGE_SIZE, "pageNumber": 1},
                               label=f"Clicks for {mailing_id}")
        if err:
            report["clicks_error"] = err
        else:
            if isinstance(clicks, list):
                report["clicks_count"] = len(clicks)
            else:
                report["clicks_data"] = clicks

        results["reports"][mailing_id] = report

    return results


# === PHASE 2B: Account-Wide Reports ===
def phase2b_account_reports():
    log("\n" + "=" * 60)
    log("PHASE 2B: Account-wide report endpoints")
    log("=" * 60)

    results = {}
    date_params = {"startDate": BAKEOFF_START, "endDate": TODAY}

    for report_type in ["Sends", "Opens", "Clickthroughs", "SubscriberActivity"]:
        log(f"\n--- /Reports/{report_type} ---")
        data = paginated_get(
            f"/Reports/{report_type}",
            params=dict(date_params),
            label=f"Reports/{report_type}",
            timeout=180
        )
        if data:
            save_raw(f"account_report_{report_type.lower()}.json", data)
            results[report_type] = {"count": len(data), "sample": data[:3] if data else []}
        else:
            # Try without dates
            log(f"  Retrying without dates...")
            data, err = api_get(f"/Reports/{report_type}", label=f"Reports/{report_type} (no dates)")
            if err:
                results[report_type] = {"error": err}
            else:
                save_raw(f"account_report_{report_type.lower()}.json",
                          data if isinstance(data, (list, dict)) else {"raw": data})
                results[report_type] = {"data": str(data)[:200] if data else "empty"}

    return results


# === PHASE 3: Cross-Reference Engagement ===
def phase3_cross_reference(phase1_results, phase2_results):
    log("\n" + "=" * 60)
    log("PHASE 3: Cross-referencing engagement data")
    log("=" * 60)

    analysis = {}

    for agency_name, agency_data in phase1_results.items():
        contacts = agency_data["contacts"]
        member_ids = {c.get("MemberID_") or c.get("MemberID") or c.get("memberID")
                      for c in contacts if c.get("MemberID_") or c.get("MemberID")}

        engagement_scores = []
        for c in contacts:
            eng = c.get("Engagement") or c.get("engagement")
            if eng is not None:
                try:
                    engagement_scores.append(float(eng))
                except (ValueError, TypeError):
                    pass

        # Engagement score distribution
        eng_dist = {"zero": 0, "low_0_25": 0, "mid_25_50": 0, "high_50_75": 0, "very_high_75_100": 0}
        for score in engagement_scores:
            if score == 0:
                eng_dist["zero"] += 1
            elif score <= 25:
                eng_dist["low_0_25"] += 1
            elif score <= 50:
                eng_dist["mid_25_50"] += 1
            elif score <= 75:
                eng_dist["high_50_75"] += 1
            else:
                eng_dist["very_high_75_100"] += 1

        analysis[agency_name] = {
            "total_contacts": len(contacts),
            "unique_member_ids": len(member_ids),
            "contacts_with_engagement": len(engagement_scores),
            "avg_engagement": round(sum(engagement_scores) / max(len(engagement_scores), 1), 2),
            "engagement_distribution": eng_dist,
        }

        log(f"\n  {agency_name}:")
        log(f"    Total: {len(contacts)}, With engagement data: {len(engagement_scores)}")
        if engagement_scores:
            log(f"    Avg engagement: {analysis[agency_name]['avg_engagement']}")
            log(f"    Distribution: {eng_dist}")

    return analysis


# === PHASE 4: Try Additional Discovery Endpoints ===
def phase4_discovery():
    log("\n" + "=" * 60)
    log("PHASE 4: Trying additional discovery endpoints")
    log("=" * 60)

    results = {}

    endpoints = [
        "/Segments",
        "/Categories",
        "/Contacts/HeldRange",
        "/Contacts/ListModified",
    ]

    for ep in endpoints:
        log(f"\n--- {ep} ---")
        params = {}
        if "Range" in ep or "Modified" in ep:
            params = {"startDate": BAKEOFF_START, "endDate": TODAY}

        data, err = api_get(ep, params=params if params else None, label=ep)
        if err:
            log(f"  ERROR: {err}")
            results[ep] = {"error": err}
        else:
            if isinstance(data, list):
                save_raw(f"discovery_{ep.replace('/', '_').strip('_')}.json", data)
                log(f"  Found {len(data)} items")
                results[ep] = {"count": len(data), "sample": data[:3]}
            elif isinstance(data, dict):
                save_raw(f"discovery_{ep.replace('/', '_').strip('_')}.json", data)
                log(f"  Dict response: {list(data.keys())[:10]}")
                results[ep] = data
            else:
                log(f"  Response: {str(data)[:200]}")
                results[ep] = {"raw": str(data)[:500]}

    return results


# === GENERATE MARKDOWN REPORT ===
def generate_report(phase1, phase1b, phase1c, phase2, phase2b, phase3, phase4):
    lines = []
    lines.append("# Quartz Delivra API Export — Full Results")
    lines.append(f"\n*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
    lines.append(f"\n*Bakeoff period: {BAKEOFF_START} to {TODAY}*")

    # Phase 1: Subscriber Counts
    lines.append("\n---\n")
    lines.append("## 1. Total Subscriber Counts (Paginated)")
    lines.append("\n| Agency | Total in Category | Bakeoff Subs | Status Breakdown |")
    lines.append("|--------|------------------|--------------|------------------|")
    for agency_name, data in phase1.items():
        status_str = ", ".join(f"{k}: {v}" for k, v in sorted(data["status_breakdown"].items()))
        lines.append(f"| {agency_name} | {data['total_in_category']:,} | {data['bakeoff_subs']:,} | {status_str} |")

    # Monthly breakdown
    lines.append("\n### Monthly Breakdown")
    lines.append("\n| Agency | Month | Count |")
    lines.append("|--------|-------|-------|")
    for agency_name, data in phase1.items():
        for month, count in data["monthly_breakdown"].items():
            lines.append(f"| {agency_name} | {month} | {count:,} |")

    # Phase 1B: JoinRange
    lines.append("\n---\n")
    lines.append("## 2. JoinRange Endpoint Results")
    if phase1b:
        for agency_name, data in phase1b.items():
            lines.append(f"\n- **{agency_name}**: {data.get('joinrange_count', 'N/A')} contacts via JoinRange")

    # Phase 1C: ContactCountByStatus
    lines.append("\n---\n")
    lines.append("## 3. ContactCountByStatus")
    if phase1c:
        lines.append(f"\n```json\n{json.dumps(phase1c, indent=2, default=str)}\n```")
    else:
        lines.append("\nEndpoint returned no data or errored.")

    # Phase 2: Broadcasts
    lines.append("\n---\n")
    lines.append("## 4. Broadcast / Mailing Data")
    if phase2.get("mailings"):
        lines.append(f"\n**Total mailings found during bakeoff period:** {len(phase2['mailings'])}")
        lines.append("\n### Mailing Details")
        for mailing in phase2["mailings"][:20]:
            mid = mailing.get("MessageID") or mailing.get("MailingID") or mailing.get("ID") or "?"
            subj = mailing.get("Subject") or mailing.get("Name") or "Unknown"
            sent = mailing.get("DateSent") or mailing.get("SentDate") or "?"
            lines.append(f"\n- **{subj}** (ID: {mid}, Sent: {sent})")

            report = phase2.get("reports", {}).get(mid, {})
            if "sends_count" in report:
                lines.append(f"  - Sends: {report['sends_count']:,}")
            if "opens_count" in report:
                lines.append(f"  - Opens: {report['opens_count']:,}")
            if "clicks_count" in report:
                lines.append(f"  - Clicks: {report['clicks_count']:,}")
            if "sends_error" in report:
                lines.append(f"  - Sends error: {report['sends_error'][:100]}")
            if "opens_error" in report:
                lines.append(f"  - Opens error: {report['opens_error'][:100]}")
    else:
        lines.append("\nNo mailings returned from API.")

    # Phase 2B: Account Reports
    lines.append("\n---\n")
    lines.append("## 5. Account-Wide Report Data")
    if phase2b:
        for report_type, data in phase2b.items():
            if "count" in data:
                lines.append(f"\n- **{report_type}**: {data['count']:,} events")
            elif "error" in data:
                lines.append(f"\n- **{report_type}**: ERROR — {data['error'][:100]}")
            else:
                lines.append(f"\n- **{report_type}**: {str(data)[:200]}")

    # Phase 3: Cross-Reference
    lines.append("\n---\n")
    lines.append("## 6. Engagement Analysis by Agency")
    if phase3:
        lines.append("\n| Agency | Total | With Engagement | Avg Score | Zero Eng | Low | Mid | High | Very High |")
        lines.append("|--------|-------|----------------|-----------|----------|-----|-----|------|-----------|")
        for agency_name, data in phase3.items():
            ed = data["engagement_distribution"]
            lines.append(
                f"| {agency_name} | {data['total_contacts']:,} | {data['contacts_with_engagement']:,} "
                f"| {data['avg_engagement']} | {ed['zero']:,} | {ed['low_0_25']:,} "
                f"| {ed['mid_25_50']:,} | {ed['high_50_75']:,} | {ed['very_high_75_100']:,} |"
            )

    # Phase 4: Discovery
    lines.append("\n---\n")
    lines.append("## 7. Discovery Endpoints")
    if phase4:
        for ep, data in phase4.items():
            if isinstance(data, dict) and "error" in data:
                lines.append(f"\n- `{ep}`: ERROR — {data['error'][:100]}")
            elif isinstance(data, dict) and "count" in data:
                lines.append(f"\n- `{ep}`: {data['count']} items")
                if data.get("sample"):
                    lines.append(f"  - Sample: `{json.dumps(data['sample'][0], default=str)[:200]}`")
            else:
                lines.append(f"\n- `{ep}`: {str(data)[:200]}")

    # Key Findings
    lines.append("\n---\n")
    lines.append("## 8. Key Findings & Answers")
    lines.append("\n### Q1: How many TOTAL TFM subscribers are in Delivra?")
    tfm = phase1.get("TFM", {})
    lines.append(f"\n**{tfm.get('total_in_category', 'Unknown'):,}** total contacts in the TFM category "
                 f"(previously capped at ~100 due to pagination bug).")

    lines.append("\n### Q2: What % have been sent broadcasts?")
    lines.append("\n*(Derived from Reports API data above — see section 4 and 5)*")

    lines.append("\n### Q3: Open/click rates for those who received broadcasts?")
    lines.append("\n*(See per-mailing report data in section 4)*")

    lines.append("\n### Q4: TFM vs BG vs GL comparison?")
    lines.append("\n| Metric | TFM | BG | GL |")
    lines.append("|--------|-----|----|----|")
    for metric in ["total_in_category", "bakeoff_subs"]:
        tfm_v = phase1.get("TFM", {}).get(metric, "?")
        bg_v = phase1.get("BG", {}).get(metric, "?")
        gl_v = phase1.get("GL", {}).get(metric, "?")
        fmt = lambda v: f"{v:,}" if isinstance(v, int) else str(v)
        lines.append(f"| {metric} | {fmt(tfm_v)} | {fmt(bg_v)} | {fmt(gl_v)} |")

    if phase3:
        for metric in ["avg_engagement", "contacts_with_engagement"]:
            tfm_v = phase3.get("TFM", {}).get(metric, "?")
            bg_v = phase3.get("BG", {}).get(metric, "?")
            gl_v = phase3.get("GL", {}).get(metric, "?")
            fmt = lambda v: f"{v:,}" if isinstance(v, int) else str(v)
            lines.append(f"| {metric} | {fmt(tfm_v)} | {fmt(bg_v)} | {fmt(gl_v)} |")

    lines.append("\n### Q5: Engagement by join date?")
    lines.append("\n*(See monthly breakdown in section 1)*")

    lines.append("\n---\n")
    lines.append("## 9. Raw Data Files")
    lines.append(f"\nAll raw API responses saved to: `{RAW_DIR}/`")

    return "\n".join(lines)


# === MAIN ===
def main():
    log("Starting Quartz Delivra API Export")
    log(f"Base URL: {BASE_URL}")
    log(f"Bakeoff period: {BAKEOFF_START} to {TODAY}")

    # Phase 1: Category contacts with pagination
    phase1 = phase1_category_contacts()

    # Phase 1B: JoinRange endpoint
    phase1b = phase1b_join_range()

    # Phase 1C: ContactCountByStatus
    phase1c = phase1c_contact_counts()

    # Phase 2: Broadcast data
    phase2 = phase2_broadcasts()

    # Phase 2B: Account-wide reports
    phase2b = phase2b_account_reports()

    # Phase 3: Cross-reference engagement
    phase3 = phase3_cross_reference(phase1, phase2)

    # Phase 4: Discovery endpoints
    phase4 = phase4_discovery()

    # Generate report
    log("\n" + "=" * 60)
    log("Generating final report...")
    report = generate_report(phase1, phase1b, phase1c, phase2, phase2b, phase3, phase4)

    report_path = os.path.join(OUT_DIR, "delivra-export-results.md")
    with open(report_path, "w") as f:
        f.write(report)

    log(f"\nReport saved to: {report_path}")
    log("Done!")


if __name__ == "__main__":
    main()
