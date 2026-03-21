#!/usr/bin/env python3
"""
Pipeboard Performance Cache — Local SQLite store for Meta Ads data.

Usage from Claude Code:
    python3 system/pipeboard-cache.py init          # Create DB + tables
    python3 system/pipeboard-cache.py ingest <json>  # Ingest a Pipeboard API response
    python3 system/pipeboard-cache.py query <sql>    # Run a SQL query
    python3 system/pipeboard-cache.py summary        # Portfolio summary from cache
    python3 system/pipeboard-cache.py freshness      # Show last snapshot date per client
    python3 system/pipeboard-cache.py trends <ad_id> # Show 4-week trend for an ad

DB location: system/data/pipeboard.db
"""

import sqlite3
import json
import sys
import os
from datetime import datetime, timedelta

DB_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
DB_PATH = os.path.join(DB_DIR, "pipeboard.db")


def get_db():
    os.makedirs(DB_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS snapshots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            snapshot_date TEXT NOT NULL,
            client_slug TEXT NOT NULL,
            campaign_id TEXT,
            campaign_name TEXT,
            level TEXT NOT NULL DEFAULT 'campaign',
            date_start TEXT,
            date_stop TEXT,
            created_at TEXT DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS campaign_metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            snapshot_id INTEGER NOT NULL,
            campaign_id TEXT NOT NULL,
            campaign_name TEXT,
            client_slug TEXT NOT NULL,
            date_start TEXT,
            date_stop TEXT,
            impressions INTEGER,
            clicks INTEGER,
            spend REAL,
            cpc REAL,
            cpm REAL,
            ctr REAL,
            reach INTEGER,
            frequency REAL,
            conversions INTEGER,
            cpl REAL,
            conversion_type TEXT,
            FOREIGN KEY (snapshot_id) REFERENCES snapshots(id)
        );

        CREATE TABLE IF NOT EXISTS ad_metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            snapshot_id INTEGER NOT NULL,
            ad_id TEXT NOT NULL,
            ad_name TEXT,
            campaign_id TEXT,
            client_slug TEXT NOT NULL,
            date_start TEXT,
            date_stop TEXT,
            impressions INTEGER,
            clicks INTEGER,
            spend REAL,
            cpc REAL,
            cpm REAL,
            ctr REAL,
            reach INTEGER,
            frequency REAL,
            conversions INTEGER,
            cpl REAL,
            conversion_type TEXT,
            FOREIGN KEY (snapshot_id) REFERENCES snapshots(id)
        );

        CREATE INDEX IF NOT EXISTS idx_campaign_metrics_slug ON campaign_metrics(client_slug, date_start);
        CREATE INDEX IF NOT EXISTS idx_campaign_metrics_campaign ON campaign_metrics(campaign_id, date_start);
        CREATE INDEX IF NOT EXISTS idx_ad_metrics_slug ON ad_metrics(client_slug, date_start);
        CREATE INDEX IF NOT EXISTS idx_ad_metrics_ad ON ad_metrics(ad_id, date_start);
        CREATE INDEX IF NOT EXISTS idx_snapshots_slug ON snapshots(client_slug, snapshot_date);
    """)
    conn.commit()
    conn.close()
    print(f"Database initialized at {DB_PATH}")


def ingest_response(json_str, client_slug, level="campaign", snapshot_date=None):
    """Ingest a Pipeboard API response into the cache."""
    if snapshot_date is None:
        snapshot_date = datetime.now().strftime("%Y-%m-%d")

    data = json.loads(json_str)
    if isinstance(data, str):
        data = json.loads(data)
    if "result" in data:
        data = json.loads(data["result"])

    records = data.get("data", [])
    if not records:
        print("No data records found in response")
        return

    conn = get_db()
    cursor = conn.cursor()

    # Create snapshot
    cursor.execute(
        "INSERT INTO snapshots (snapshot_date, client_slug, level, date_start, date_stop) VALUES (?, ?, ?, ?, ?)",
        (snapshot_date, client_slug, level,
         records[0].get("date_start"), records[0].get("date_stop"))
    )
    snapshot_id = cursor.lastrowid

    for record in records:
        # Extract best conversion metric
        conversions = 0
        cpl = None
        conv_type = None

        # Priority order for conversion events
        conv_priorities = [
            "onsite_web_lead", "offsite_conversion.fb_pixel_lead",
            "complete_registration", "offsite_conversion.fb_pixel_complete_registration",
            "offsite_conversion.fb_pixel_custom", "lead",
            "mobile_app_install"
        ]

        for action in record.get("actions", []):
            if action["action_type"] in conv_priorities:
                if conv_type is None or conv_priorities.index(action["action_type"]) < conv_priorities.index(conv_type):
                    conv_type = action["action_type"]
                    conversions = int(action["value"])

        for cost in record.get("cost_per_action_type", []):
            if cost["action_type"] == conv_type:
                cpl = float(cost["value"])
                break

        common = {
            "snapshot_id": snapshot_id,
            "client_slug": client_slug,
            "date_start": record.get("date_start"),
            "date_stop": record.get("date_stop"),
            "impressions": int(record.get("impressions", 0)),
            "clicks": int(record.get("clicks", 0)),
            "spend": float(record.get("spend", 0)),
            "cpc": float(record.get("cpc", 0)) if record.get("cpc") else None,
            "cpm": float(record.get("cpm", 0)) if record.get("cpm") else None,
            "ctr": float(record.get("ctr", 0)) if record.get("ctr") else None,
            "reach": int(record.get("reach", 0)) if record.get("reach") else None,
            "frequency": float(record.get("frequency", 0)) if record.get("frequency") else None,
            "conversions": conversions,
            "cpl": cpl,
            "conversion_type": conv_type,
        }

        if level == "ad":
            cursor.execute("""
                INSERT INTO ad_metrics
                (snapshot_id, ad_id, ad_name, campaign_id, client_slug, date_start, date_stop,
                 impressions, clicks, spend, cpc, cpm, ctr, reach, frequency,
                 conversions, cpl, conversion_type)
                VALUES (:snapshot_id, :ad_id, :ad_name, :campaign_id, :client_slug, :date_start, :date_stop,
                        :impressions, :clicks, :spend, :cpc, :cpm, :ctr, :reach, :frequency,
                        :conversions, :cpl, :conversion_type)
            """, {**common,
                  "ad_id": record.get("ad_id", ""),
                  "ad_name": record.get("ad_name", ""),
                  "campaign_id": record.get("campaign_id", "")})
        else:
            cursor.execute("""
                INSERT INTO campaign_metrics
                (snapshot_id, campaign_id, campaign_name, client_slug, date_start, date_stop,
                 impressions, clicks, spend, cpc, cpm, ctr, reach, frequency,
                 conversions, cpl, conversion_type)
                VALUES (:snapshot_id, :campaign_id, :campaign_name, :client_slug, :date_start, :date_stop,
                        :impressions, :clicks, :spend, :cpc, :cpm, :ctr, :reach, :frequency,
                        :conversions, :cpl, :conversion_type)
            """, {**common,
                  "campaign_id": record.get("campaign_id", record.get("account_id", "")),
                  "campaign_name": record.get("campaign_name", record.get("account_name", ""))})

    conn.commit()
    print(f"Ingested {len(records)} {level}-level records for {client_slug} (snapshot {snapshot_id})")
    conn.close()


def show_freshness():
    conn = get_db()
    rows = conn.execute("""
        SELECT client_slug,
               MAX(snapshot_date) as last_snapshot,
               MAX(date_stop) as data_through,
               COUNT(DISTINCT snapshot_date) as total_snapshots
        FROM snapshots
        GROUP BY client_slug
        ORDER BY last_snapshot DESC
    """).fetchall()
    conn.close()

    if not rows:
        print("No data in cache yet.")
        return

    print(f"{'Client':<25} {'Last Snapshot':<15} {'Data Through':<15} {'Snapshots':<10}")
    print("-" * 65)
    for r in rows:
        print(f"{r['client_slug']:<25} {r['last_snapshot']:<15} {r['data_through'] or 'N/A':<15} {r['total_snapshots']:<10}")


def show_summary():
    conn = get_db()
    # Get latest snapshot per client
    rows = conn.execute("""
        SELECT cm.client_slug,
               SUM(cm.spend) as total_spend,
               SUM(cm.impressions) as total_impressions,
               SUM(cm.conversions) as total_conversions,
               CASE WHEN SUM(cm.conversions) > 0
                    THEN SUM(cm.spend) / SUM(cm.conversions)
                    ELSE NULL END as avg_cpl,
               cm.date_start, cm.date_stop
        FROM campaign_metrics cm
        INNER JOIN (
            SELECT client_slug, MAX(snapshot_id) as max_snap
            FROM campaign_metrics
            GROUP BY client_slug
        ) latest ON cm.client_slug = latest.client_slug AND cm.snapshot_id = latest.max_snap
        GROUP BY cm.client_slug
        ORDER BY total_spend DESC
    """).fetchall()
    conn.close()

    if not rows:
        print("No campaign data in cache.")
        return

    total_spend = sum(r["total_spend"] for r in rows)
    print(f"Portfolio Summary (from cache) — Total spend: ${total_spend:,.2f}")
    print()
    print(f"{'Client':<25} {'Spend':<12} {'Impressions':<14} {'Conversions':<13} {'CPL':<10} {'Period'}")
    print("-" * 90)
    for r in rows:
        cpl_str = f"${r['avg_cpl']:.2f}" if r['avg_cpl'] else "N/A"
        print(f"{r['client_slug']:<25} ${r['total_spend']:>9,.2f} {r['total_impressions']:>12,} {r['total_conversions']:>11,} {cpl_str:<10} {r['date_start']} to {r['date_stop']}")


def show_trends(ad_id):
    conn = get_db()
    rows = conn.execute("""
        SELECT date_start, date_stop, impressions, clicks, spend, ctr, cpm, cpl, frequency, ad_name
        FROM ad_metrics
        WHERE ad_id = ?
        ORDER BY date_start
    """, (ad_id,)).fetchall()
    conn.close()

    if not rows:
        print(f"No data found for ad_id {ad_id}")
        return

    print(f"Trend for: {rows[0]['ad_name']}")
    print(f"{'Period':<25} {'Spend':<10} {'Impressions':<13} {'CTR':<8} {'CPM':<10} {'CPL':<10} {'Freq'}")
    print("-" * 85)
    for r in rows:
        cpl_str = f"${r['cpl']:.2f}" if r['cpl'] else "N/A"
        print(f"{r['date_start']} to {r['date_stop']}  ${r['spend']:>7,.2f} {r['impressions']:>11,} {r['ctr']:>6.2f}% ${r['cpm']:>7.2f} {cpl_str:<10} {r['frequency']:.2f}")


def run_query(sql):
    conn = get_db()
    try:
        rows = conn.execute(sql).fetchall()
        if rows:
            headers = rows[0].keys()
            print("\t".join(headers))
            for r in rows:
                print("\t".join(str(r[h]) for h in headers))
        else:
            print("No results.")
    except Exception as e:
        print(f"Error: {e}")
    conn.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "init":
        init_db()
    elif cmd == "freshness":
        show_freshness()
    elif cmd == "summary":
        show_summary()
    elif cmd == "trends" and len(sys.argv) >= 3:
        show_trends(sys.argv[2])
    elif cmd == "query" and len(sys.argv) >= 3:
        run_query(" ".join(sys.argv[2:]))
    elif cmd == "ingest":
        # Read JSON from stdin, client_slug and level from args
        if len(sys.argv) < 4:
            print("Usage: pipeboard-cache.py ingest <client_slug> <level> [snapshot_date]")
            print("  Reads JSON from stdin")
            sys.exit(1)
        client_slug = sys.argv[2]
        level = sys.argv[3]
        snapshot_date = sys.argv[4] if len(sys.argv) >= 5 else None
        json_str = sys.stdin.read()
        ingest_response(json_str, client_slug, level, snapshot_date)
    else:
        print(__doc__)
