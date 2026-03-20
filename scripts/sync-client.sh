#!/bin/bash
# The Feed Media — Client Intelligence Sync Script
# Run after completing a new client analysis to update local files

# Usage: ./sync-client.sh [client-name]
# Example: ./sync-client.sh houck

CLIENT=$1
CLIENTS_DIR="$(dirname "$0")/../clients"
TIMESTAMP=$(date +"%B %Y")

if [ -z "$CLIENT" ]; then
  echo "Usage: ./sync-client.sh [client-name]"
  echo ""
  echo "Available clients:"
  ls $CLIENTS_DIR | sed 's/.md//'
  exit 1
fi

FILE="$CLIENTS_DIR/${CLIENT}.md"

if [ ! -f "$FILE" ]; then
  echo "Client file not found: $FILE"
  echo "Creating new file from template..."
  cp "$CLIENTS_DIR/../system/client-template.md" "$FILE"
  echo "Created: $FILE"
  echo "Now paste your analysis content into this file."
else
  echo "File exists: $FILE"
  echo "Last updated: $(head -3 $FILE | grep 'Last Updated')"
  echo ""
  echo "To update, paste the new analysis content into:"
  echo "  $FILE"
  echo ""
  echo "Then update the 'Last Updated' header to: $TIMESTAMP"
fi
