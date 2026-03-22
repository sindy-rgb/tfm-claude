#!/usr/bin/env python3
"""
Quartz Delivra Data Analyzer
Reads the raw API response files and generates the full analysis report.
This runs offline against data already pulled by delivra-export.py.
"""

import json
import os
from datetime import datetime
from collections import defaultdict

RAW_DIR = "/Users/jay/Documents/the vault/the-feed-media/clients/quartz/delivra-raw"
OUT_DIR = "/Users/jay/Documents/the vault/the-feed-media/clients/quartz"
TODAY = datetime.now().strftime("%Y-%m-%d")
BAKEOFF_START = "2026-02-01"


def load_json(filename):
    path = os.path.join(RAW_DIR, filename)
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


def analyze_contacts():
    """Analyze the category contacts for TFM, BG, GL."""
    results = {}
    for agency_key, name in [("tfm", "TFM"), ("bg", "BG"), ("gl", "GL")]:
        data = load_json(f"{agency_key}_all_contacts.json")
        if not data:
            print(f"  {name}: No data file found")
            results[name] = {"error": "no data"}
            continue

        total = len(data)
        status = defaultdict(int)
        monthly = defaultdict(int)
        bakeoff = []

        for c in data:
            mt = c.get("MemberType_", "unknown")
            status[mt] += 1
            joined = (c.get("DateJoined") or "")[:10]
            if joined >= BAKEOFF_START:
                bakeoff.append(c)
                monthly[joined[:7]] += 1

        results[name] = {
            "total": total,
            "bakeoff": len(bakeoff),
            "status": dict(status),
            "monthly": dict(sorted(monthly.items())),
        }
        print(f"  {name}: {total} total, {len(bakeoff)} bakeoff, status={dict(status)}")

    return results


def analyze_joinrange():
    """Analyze JoinRange data."""
    results = {}
    for agency_key, name in [("tfm", "TFM"), ("bg", "BG"), ("gl", "GL")]:
        data = load_json(f"{agency_key}_joinrange.json")
        if data:
            results[name] = len(data)
            print(f"  {name} JoinRange: {len(data)} contacts")
        else:
            results[name] = 0
    return results


def analyze_mailings():
    """Analyze mailings sent data."""
    data = load_json("mailings_sent.json")
    if not data:
        print("  No mailings_sent.json found")
        return {"mailings": [], "count": 0}

    print(f"  Total mailings: {len(data)}")
    if data:
        print(f"  First mailing keys: {list(data[0].keys())}")
        print(f"  Sample: {json.dumps(data[0], default=str)[:300]}")

    return {"mailings": data, "count": len(data)}


def analyze_per_mailing_reports():
    """Analyze the per-mailing report files (sends, opens, clicks)."""
    # Find all report files
    report_files = [f for f in os.listdir(RAW_DIR) if f.startswith("report_") and f.endswith(".json")]
    mailing_ids = set()
    for f in report_files:
        parts = f.replace("report_", "").replace(".json", "").rsplit("_", 1)
        if len(parts) == 2:
            mailing_ids.add(parts[0])

    print(f"  Found report data for {len(mailing_ids)} mailings")

    mailings_data = load_json("mailings_sent.json") or []
    mailing_lookup = {}
    for m in mailings_data:
        mid = str(m.get("MessageID") or m.get("MailingID") or m.get("ID") or "")
        if mid:
            mailing_lookup[mid] = m

    reports = []
    for mid in sorted(mailing_ids):
        sends = load_json(f"report_{mid}_sends.json") or []
        opens = load_json(f"report_{mid}_opens.json") or []

        mailing_info = mailing_lookup.get(mid, {})
        subject = mailing_info.get("Subject") or mailing_info.get("Name") or "Unknown"
        sent_date = mailing_info.get("DateSent") or mailing_info.get("SentDate") or ""

        open_rate = (len(opens) / len(sends) * 100) if sends else 0

        report = {
            "mailing_id": mid,
            "subject": subject,
            "sent_date": sent_date,
            "sends_count": len(sends),
            "opens_count": len(opens),
            "open_rate": round(open_rate, 1),
        }
        reports.append(report)
        print(f"    Mailing {mid}: {len(sends)} sends, {len(opens)} opens ({open_rate:.1f}% OR) — {subject[:50]}")

    return reports


def cross_reference_broadcasts(contacts_data, mailing_reports):
    """
    Cross-reference mailing sends with agency subscriber lists.
    For each agency's subscribers, check if they appear in any mailing's sends.
    """
    print("\n  Cross-referencing broadcasts with agency subscriber lists...")

    # Build member ID sets for each agency
    agency_members = {}
    for agency_key, name in [("tfm", "TFM"), ("bg", "BG"), ("gl", "GL")]:
        contacts = load_json(f"{agency_key}_all_contacts.json") or []
        ids = set()
        for c in contacts:
            mid = c.get("MemberID_") or c.get("MemberID")
            if mid and mid != 0:
                ids.add(mid)
        agency_members[name] = ids
        print(f"    {name}: {len(ids)} unique member IDs")

    # For each mailing report, check which agency members were sent/opened
    results = {}
    for report in mailing_reports:
        mid = report["mailing_id"]
        sends_data = load_json(f"report_{mid}_sends.json") or []
        opens_data = load_json(f"report_{mid}_opens.json") or []

        send_member_ids = set()
        for s in sends_data:
            smid = s.get("MemberID_") or s.get("MemberID") or s.get("memberID")
            if smid:
                send_member_ids.add(smid)

        open_member_ids = set()
        for o in opens_data:
            omid = o.get("MemberID_") or o.get("MemberID") or o.get("memberID")
            if omid:
                open_member_ids.add(omid)

        mailing_result = {"mailing_id": mid, "subject": report["subject"]}

        for name, members in agency_members.items():
            sent_to = members & send_member_ids
            opened_by = members & open_member_ids
            mailing_result[f"{name}_sent"] = len(sent_to)
            mailing_result[f"{name}_opened"] = len(opened_by)
            mailing_result[f"{name}_open_rate"] = round(len(opened_by) / max(len(sent_to), 1) * 100, 1) if sent_to else 0

        results[mid] = mailing_result

    # Summary per agency
    summary = {}
    for name in ["TFM", "BG", "GL"]:
        total_sent = sum(r.get(f"{name}_sent", 0) for r in results.values())
        total_opened = sum(r.get(f"{name}_opened", 0) for r in results.values())
        mailings_with_sends = sum(1 for r in results.values() if r.get(f"{name}_sent", 0) > 0)

        # Unique members who were sent at least one broadcast
        all_sent_members = set()
        all_open_members = set()
        for mid_key in results:
            sends_data = load_json(f"report_{mid_key}_sends.json") or []
            opens_data = load_json(f"report_{mid_key}_opens.json") or []
            for s in sends_data:
                smid = s.get("MemberID_") or s.get("MemberID") or s.get("memberID")
                if smid and smid in agency_members[name]:
                    all_sent_members.add(smid)
            for o in opens_data:
                omid = o.get("MemberID_") or o.get("MemberID") or o.get("memberID")
                if omid and omid in agency_members[name]:
                    all_open_members.add(omid)

        summary[name] = {
            "total_sends": total_sent,
            "total_opens": total_opened,
            "mailings_with_sends": mailings_with_sends,
            "unique_members_sent": len(all_sent_members),
            "unique_members_opened": len(all_open_members),
            "total_members": len(agency_members[name]),
            "pct_sent_broadcast": round(len(all_sent_members) / max(len(agency_members[name]), 1) * 100, 1),
            "pct_opened_broadcast": round(len(all_open_members) / max(len(agency_members[name]), 1) * 100, 1),
        }

        print(f"\n    {name} Broadcast Summary:")
        print(f"      Members: {len(agency_members[name])}")
        print(f"      Unique sent broadcast: {len(all_sent_members)} ({summary[name]['pct_sent_broadcast']}%)")
        print(f"      Unique opened: {len(all_open_members)} ({summary[name]['pct_opened_broadcast']}%)")
        print(f"      Total send events: {total_sent}, Total open events: {total_opened}")
        print(f"      Mailings with sends to this agency: {mailings_with_sends}")

    return results, summary


def generate_report(contacts, joinrange, mailings_info, mailing_reports, xref_details, xref_summary):
    lines = []
    lines.append("# Quartz Delivra API Export — Full Results")
    lines.append(f"\n*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
    lines.append(f"\n*Bakeoff period: {BAKEOFF_START} to {TODAY}*")

    # === Section 1: Subscriber Counts ===
    lines.append("\n---\n")
    lines.append("## 1. Total Subscriber Counts (PAGINATED — Bug Fixed)")
    lines.append("\nThe previous code returned ~100 contacts because it never paginated. With pagination fixed:")
    lines.append("\n| Agency | Category ID | Total in Category | Bakeoff Subs (since Feb 1) |")
    lines.append("|--------|-------------|------------------|---------------------------|")

    category_ids = {"TFM": 623803, "BG": 623802, "GL": 601833}
    for name in ["TFM", "BG", "GL"]:
        data = contacts.get(name, {})
        if "error" in data:
            lines.append(f"| {name} | {category_ids[name]} | ERROR | ERROR |")
        else:
            lines.append(f"| {name} | {category_ids[name]} | **{data['total']:,}** | **{data['bakeoff']:,}** |")

    # Status breakdown
    lines.append("\n### Status Breakdown")
    lines.append("\n| Agency | Normal (Active) | Held | Unsub | Other |")
    lines.append("|--------|----------------|------|-------|-------|")
    for name in ["TFM", "BG", "GL"]:
        data = contacts.get(name, {})
        if "error" not in data:
            s = data["status"]
            lines.append(f"| {name} | {s.get('normal', 0):,} | {s.get('held', 0):,} | {s.get('unsub', 0):,} | {s.get('confirm', 0) + s.get('other', 0):,} |")

    # Monthly breakdown
    lines.append("\n### Monthly Breakdown (Bakeoff Period)")
    lines.append("\n| Agency | Month | Count |")
    lines.append("|--------|-------|-------|")
    for name in ["TFM", "BG", "GL"]:
        data = contacts.get(name, {})
        if "error" not in data:
            for month, count in data.get("monthly", {}).items():
                lines.append(f"| {name} | {month} | {count:,} |")

    # === Section 2: JoinRange ===
    lines.append("\n---\n")
    lines.append("## 2. JoinRange Endpoint Validation")
    for name in ["TFM", "BG", "GL"]:
        count = joinrange.get(name, 0)
        lines.append(f"\n- **{name}**: {count:,} contacts via JoinRange (should match bakeoff count above)")

    # === Section 3: Account-Wide Status ===
    lines.append("\n---\n")
    lines.append("## 3. Account-Wide Contact Status")
    status_data = load_json("contact_count_by_status.json")
    if status_data and isinstance(status_data, list):
        lines.append("\n| Status | Count |")
        lines.append("|--------|-------|")
        for item in status_data:
            lines.append(f"| {item.get('MemberType_', '?')} | {item.get('MemberCount_', '?'):,} |")
    else:
        lines.append("\n*(Data not available)*")

    # === Section 4: Broadcast Analysis ===
    lines.append("\n---\n")
    lines.append("## 4. Broadcast / Mailing Analysis")
    lines.append(f"\n**Total mailings found:** {mailings_info['count']}")

    if mailing_reports:
        lines.append("\n### Per-Mailing Report (first 20)")
        lines.append("\n| Mailing ID | Subject | Sends | Opens | Open Rate |")
        lines.append("|-----------|---------|-------|-------|-----------|")
        for r in mailing_reports:
            subj = r["subject"][:40]
            lines.append(f"| {r['mailing_id']} | {subj} | {r['sends_count']:,} | {r['opens_count']:,} | {r['open_rate']}% |")

    # === Section 5: Cross-Reference ===
    lines.append("\n---\n")
    lines.append("## 5. Broadcast Engagement by Agency (Cross-Referenced)")
    lines.append("\nThis is the key analysis: for each agency's subscribers, how many were actually sent broadcasts and how many engaged?")

    if xref_summary:
        lines.append("\n### Summary")
        lines.append("\n| Metric | TFM | BG | GL |")
        lines.append("|--------|-----|----|----|")
        metrics = [
            ("Total Members in Category", "total_members"),
            ("Unique Members Sent a Broadcast", "unique_members_sent"),
            ("% Sent a Broadcast", "pct_sent_broadcast"),
            ("Unique Members Who Opened", "unique_members_opened"),
            ("% Who Opened a Broadcast", "pct_opened_broadcast"),
            ("Total Send Events", "total_sends"),
            ("Total Open Events", "total_opens"),
            ("Mailings With Sends to Agency", "mailings_with_sends"),
        ]
        for label, key in metrics:
            vals = []
            for name in ["TFM", "BG", "GL"]:
                v = xref_summary.get(name, {}).get(key, "?")
                if isinstance(v, float):
                    vals.append(f"{v}%")
                elif isinstance(v, int):
                    vals.append(f"{v:,}")
                else:
                    vals.append(str(v))
            lines.append(f"| {label} | {vals[0]} | {vals[1]} | {vals[2]} |")

        # Per-mailing breakdown by agency
        if xref_details:
            lines.append("\n### Per-Mailing Breakdown by Agency")
            lines.append("\n| Mailing ID | Subject | TFM Sent | TFM Opened | TFM OR | BG Sent | BG Opened | BG OR | GL Sent | GL Opened | GL OR |")
            lines.append("|-----------|---------|----------|------------|--------|---------|-----------|-------|---------|-----------|-------|")
            for mid, r in xref_details.items():
                subj = r.get("subject", "?")[:30]
                row = f"| {mid} | {subj}"
                for name in ["TFM", "BG", "GL"]:
                    sent = r.get(f"{name}_sent", 0)
                    opened = r.get(f"{name}_opened", 0)
                    orate = r.get(f"{name}_open_rate", 0)
                    row += f" | {sent:,} | {opened:,} | {orate}%"
                row += " |"
                lines.append(row)

    # === Section 6: Key Answers ===
    lines.append("\n---\n")
    lines.append("## 6. Key Answers")

    tfm = contacts.get("TFM", {})
    bg = contacts.get("BG", {})
    gl = contacts.get("GL", {})
    tfm_summary = xref_summary.get("TFM", {}) if xref_summary else {}

    lines.append("\n### Q1: How many TOTAL TFM subscribers are in Delivra?")
    if "error" not in tfm:
        lines.append(f"\n**{tfm['total']:,}** total contacts in the TFM category (feed-media, ID 623803).")
        lines.append(f"Previously reported as ~100 due to the pagination bug — this is a **{tfm['total']}x increase** over the buggy count.")
    else:
        lines.append("\nCould not determine — API returned an error.")

    lines.append("\n### Q2: What % have been sent broadcasts?")
    if tfm_summary:
        lines.append(f"\n**{tfm_summary.get('pct_sent_broadcast', '?')}%** of TFM subscribers have been sent at least one broadcast.")
        lines.append(f"({tfm_summary.get('unique_members_sent', '?'):,} out of {tfm_summary.get('total_members', '?'):,} unique members)")
    else:
        lines.append("\n*(Cross-reference data not available)*")

    lines.append("\n### Q3: Open/click rates for broadcast recipients?")
    if tfm_summary:
        lines.append(f"\n**{tfm_summary.get('pct_opened_broadcast', '?')}%** of TFM subscribers have opened at least one broadcast.")
        lines.append(f"({tfm_summary.get('unique_members_opened', '?'):,} unique openers)")
    else:
        lines.append("\n*(Cross-reference data not available)*")

    lines.append("\n### Q4: TFM vs BG vs GL comparison?")
    if xref_summary:
        lines.append("\n*(See the cross-reference table in Section 5 above)*")
    lines.append("\n| Metric | TFM | BG | GL |")
    lines.append("|--------|-----|----|----|")
    for name_label, data in [("Total Subs", contacts), ("Bakeoff Subs", contacts)]:
        vals = []
        for n in ["TFM", "BG", "GL"]:
            d = data.get(n, {})
            if name_label == "Total Subs":
                vals.append(f"{d.get('total', '?'):,}" if isinstance(d.get('total'), int) else "?")
            else:
                vals.append(f"{d.get('bakeoff', '?'):,}" if isinstance(d.get('bakeoff'), int) else "?")
        lines.append(f"| {name_label} | {vals[0]} | {vals[1]} | {vals[2]} |")

    lines.append("\n### Q5: Engagement by join date?")
    lines.append("\n*(See the monthly breakdown table in Section 1)*")

    # === Section 7: Raw files ===
    lines.append("\n---\n")
    lines.append("## 7. Raw Data Files")
    lines.append(f"\nAll raw API responses saved to: `delivra-raw/`")
    raw_files = sorted(os.listdir(RAW_DIR))
    for f in raw_files:
        size = os.path.getsize(os.path.join(RAW_DIR, f))
        lines.append(f"- `{f}` ({size:,} bytes)")

    return "\n".join(lines)


def main():
    print("=" * 60)
    print("Quartz Delivra Data Analyzer")
    print("=" * 60)

    print("\n--- Analyzing contacts ---")
    contacts = analyze_contacts()

    print("\n--- Analyzing JoinRange ---")
    joinrange = analyze_joinrange()

    print("\n--- Analyzing mailings ---")
    mailings_info = analyze_mailings()

    print("\n--- Analyzing per-mailing reports ---")
    mailing_reports = analyze_per_mailing_reports()

    print("\n--- Cross-referencing broadcasts with agency members ---")
    xref_details, xref_summary = cross_reference_broadcasts(contacts, mailing_reports)

    print("\n--- Generating report ---")
    report = generate_report(contacts, joinrange, mailings_info, mailing_reports, xref_details, xref_summary)

    report_path = os.path.join(OUT_DIR, "delivra-export-results.md")
    with open(report_path, "w") as f:
        f.write(report)

    print(f"\nReport saved to: {report_path}")
    print("Done!")


if __name__ == "__main__":
    main()
