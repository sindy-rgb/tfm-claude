#!/usr/bin/env bash
# =============================================================================
# Pipeboard DB Refresh Script
# Refreshes the last 7 days of Meta Ads data for all TFM clients
#
# Usage:
#   ./refresh.sh                  # Refresh all clients, last 7 days
#   ./refresh.sh --client houck   # Refresh single client
#   ./refresh.sh --days 14        # Refresh last 14 days
#   ./refresh.sh --dry-run        # Show what would be refreshed without doing it
#
# Requirements:
#   - Claude Code CLI (claude) installed and authenticated
#   - Pipeboard MCP connection active
#   - sqlite3 available
#
# This script works by generating a Claude Code prompt that uses the Pipeboard
# MCP tools to pull data and write it to SQLite. It cannot call Pipeboard
# directly — it delegates to Claude Code which has the MCP connection.
# =============================================================================

set -euo pipefail

# --- Configuration ---
DB_PATH="$(cd "$(dirname "$0")" && pwd)/pipeboard.db"
LOG_DIR="$(cd "$(dirname "$0")" && pwd)/logs"
LOG_FILE="${LOG_DIR}/refresh-$(date +%Y%m%d-%H%M%S).log"
DAYS=7
DRY_RUN=false
SINGLE_CLIENT=""

# --- Parse Arguments ---
while [[ $# -gt 0 ]]; do
    case $1 in
        --client)
            SINGLE_CLIENT="$2"
            shift 2
            ;;
        --days)
            DAYS="$2"
            shift 2
            ;;
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --help)
            head -20 "$0" | grep '^#' | sed 's/^# \?//'
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# --- Setup ---
mkdir -p "$LOG_DIR"

log() {
    local msg="[$(date '+%Y-%m-%d %H:%M:%S')] $1"
    echo "$msg" | tee -a "$LOG_FILE"
}

log "=== Pipeboard DB Refresh Started ==="
log "DB: $DB_PATH"
log "Days: $DAYS"
log "Dry run: $DRY_RUN"

# --- Verify DB exists ---
if [[ ! -f "$DB_PATH" ]]; then
    log "ERROR: Database not found at $DB_PATH"
    exit 1
fi

# --- Calculate date range ---
if [[ "$(uname)" == "Darwin" ]]; then
    DATE_START=$(date -v-${DAYS}d +%Y-%m-%d)
else
    DATE_START=$(date -d "-${DAYS} days" +%Y-%m-%d)
fi
DATE_END=$(date +%Y-%m-%d)

log "Date range: $DATE_START to $DATE_END"

# --- Get client list from DB ---
if [[ -n "$SINGLE_CLIENT" ]]; then
    CLIENTS="$SINGLE_CLIENT"
    log "Single client mode: $SINGLE_CLIENT"
else
    CLIENTS=$(sqlite3 "$DB_PATH" "SELECT client_slug FROM account_mapping ORDER BY client_slug;")
    CLIENT_COUNT=$(echo "$CLIENTS" | wc -l | tr -d ' ')
    log "Found $CLIENT_COUNT clients in account_mapping"
fi

# --- Show stale clients ---
log ""
log "--- Current Data Staleness ---"
sqlite3 -header -column "$DB_PATH" "
SELECT client_slug,
       MAX(date_stop) as latest_data,
       ROUND(julianday('now') - julianday(MAX(date_stop)), 1) as days_stale
FROM campaign_metrics
GROUP BY client_slug
HAVING days_stale > 1
ORDER BY days_stale DESC;
" 2>/dev/null | while IFS= read -r line; do log "  $line"; done

STALE_NOMATCH=$(sqlite3 "$DB_PATH" "
SELECT am.client_slug
FROM account_mapping am
LEFT JOIN campaign_metrics cm ON am.client_slug = cm.client_slug
WHERE cm.id IS NULL;
" 2>/dev/null)

if [[ -n "$STALE_NOMATCH" ]]; then
    log ""
    log "--- Clients with NO data ---"
    echo "$STALE_NOMATCH" | while IFS= read -r line; do log "  $line"; done
fi

if [[ "$DRY_RUN" == "true" ]]; then
    log ""
    log "DRY RUN — would refresh these clients for $DATE_START to $DATE_END:"
    echo "$CLIENTS" | while IFS= read -r client; do
        ACCT_ID=$(sqlite3 "$DB_PATH" "SELECT account_id FROM account_mapping WHERE client_slug = '$client';")
        CONV_TYPE=$(sqlite3 "$DB_PATH" "SELECT conversion_type FROM account_mapping WHERE client_slug = '$client';")
        log "  $client | $ACCT_ID | conversion: $CONV_TYPE"
    done
    log ""
    log "DRY RUN complete. No data was modified."
    exit 0
fi

# --- Generate the Claude Code prompt ---
# This builds a prompt that Claude Code can execute with MCP tools
PROMPT_FILE="${LOG_DIR}/refresh-prompt-$(date +%Y%m%d-%H%M%S).md"

cat > "$PROMPT_FILE" << PROMPT_EOF
# Pipeboard DB Refresh — Automated

Refresh the Pipeboard SQLite database at \`$DB_PATH\` with the latest data.

## Instructions

For each client below, use the Pipeboard \`bulk_get_insights\` or \`get_insights\` MCP tool to pull campaign-level data for **$DATE_START to $DATE_END** with \`time_increment=7\` (weekly).

Then write the results to the SQLite database:
1. Delete existing rows in \`campaign_metrics\` where \`client_slug\` matches AND \`date_start >= '$DATE_START'\` AND \`date_stop <= '$DATE_END'\`
2. Insert fresh rows with the new data
3. Create a snapshot row in \`snapshots\` for each pull

### Clients to Refresh

PROMPT_EOF

echo "$CLIENTS" | while IFS= read -r client; do
    ACCT_ID=$(sqlite3 "$DB_PATH" "SELECT account_id FROM account_mapping WHERE client_slug = '$client';")
    CONV_TYPE=$(sqlite3 "$DB_PATH" "SELECT conversion_type FROM account_mapping WHERE client_slug = '$client';")
    echo "- **$client**: account_id=\`$ACCT_ID\`, conversion_type=\`$CONV_TYPE\`" >> "$PROMPT_FILE"
done

cat >> "$PROMPT_FILE" << 'PROMPT_EOF'

### For each client, execute this pattern:

```
1. Call get_insights with:
   - account_id: (from list above)
   - level: "campaign"
   - time_range: {"since": "DATE_START", "until": "DATE_END"}
   - time_increment: 7
   - fields: ["campaign_name", "impressions", "clicks", "spend", "cpc", "cpm", "ctr", "reach", "frequency"]
   - action_breakdowns: ["action_type"]

2. Extract conversions by matching the conversion_type from account_mapping

3. Write to SQLite:
   DELETE FROM campaign_metrics
   WHERE client_slug = '{slug}'
     AND date_start >= 'DATE_START'
     AND date_stop <= 'DATE_END'
     AND julianday(date_stop) - julianday(date_start) <= 7;

   INSERT INTO campaign_metrics (snapshot_id, campaign_id, campaign_name, client_slug,
     date_start, date_stop, impressions, clicks, spend, cpc, cpm, ctr, reach, frequency,
     conversions, cpl, conversion_type)
   VALUES (...);
```

### After all clients are refreshed:

1. Run `SELECT * FROM v_stale_clients;` to verify no clients are stale
2. Run `SELECT client_slug, tw_spend, tw_cpl FROM v_wow_comparison ORDER BY tw_spend DESC;` to show the latest WoW comparison
3. Report what was updated and any errors
PROMPT_EOF

log ""
log "Generated Claude Code prompt at: $PROMPT_FILE"
log ""

# --- Execute via Claude Code (if available) ---
if command -v claude &> /dev/null; then
    log "Executing refresh via Claude Code CLI..."
    log "Command: claude --print < $PROMPT_FILE"
    log ""
    log "NOTE: This requires an active Claude Code session with Pipeboard MCP."
    log "If running from cron, ensure the MCP connection is available."
    log ""

    # Uncomment the line below to auto-execute:
    # claude --print < "$PROMPT_FILE" 2>&1 | tee -a "$LOG_FILE"

    log "Auto-execution is disabled by default. To enable:"
    log "  1. Edit refresh.sh and uncomment the claude --print line"
    log "  2. Or run manually: claude --print < $PROMPT_FILE"
else
    log "Claude Code CLI not found. To refresh manually:"
    log "  1. Open Claude Code in the vault directory"
    log "  2. Paste the contents of: $PROMPT_FILE"
    log "  3. Or run: claude --print < $PROMPT_FILE"
fi

log ""
log "=== Pipeboard DB Refresh Script Complete ==="
log "Log saved to: $LOG_FILE"
