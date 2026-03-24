# n8n Workflow: YouTube Transcript → Vault Pipeline

## Overview
Drop a YouTube URL into #ai-stuff → n8n extracts the full transcript → writes it to GitHub → Obsidian Git syncs it to your vault. Process later with Claude Code for free on your Max plan.

**Instance:** `n8n-zwzfv-u62151.vm.elestio.app`
**Estimated build time:** 15-20 minutes
**Community nodes required:** Super Data
**Cost per execution:** $0

---

## Prerequisites

### 1. Install Super Data Community Node
In n8n: Settings → Community Nodes → Install → search `n8n-nodes-superdata` → Install

### 2. Add GitHub Credential
In n8n: Credentials → Add Credential → GitHub API
- Token: a GitHub personal access token with `repo` scope for `thefeedmedia/tfm-vault`

### 3. Slack Bot Credential
Already configured (same one the N8N bot uses for Friday reports).

---

## Workflow: 4 Nodes

```
[1. Slack Trigger] → [2. Extract URL] → [3. Super Data] → [4. GitHub: Write File]
```

---

### Node 1: Slack Trigger
**Type:** Slack Trigger
**Event:** `message` in channel
**Channel:** `#ai-stuff`
**Filter:** Message contains `youtube.com` OR `youtu.be`

---

### Node 2: Extract URL (Code Node)
**Type:** Code

```javascript
const message = $input.first().json.text || "";

const urlPatterns = [
  /https?:\/\/(?:www\.)?youtube\.com\/watch\?v=([a-zA-Z0-9_-]+)/,
  /https?:\/\/youtu\.be\/([a-zA-Z0-9_-]+)/,
  /https?:\/\/(?:www\.)?youtube\.com\/live\/([a-zA-Z0-9_-]+)/
];

let videoId = null;
let videoUrl = null;

for (const pattern of urlPatterns) {
  const match = message.match(pattern);
  if (match) {
    videoId = match[1];
    videoUrl = match[0];
    break;
  }
}

if (!videoId) {
  throw new Error("No YouTube URL found in message");
}

return [{
  json: {
    videoId,
    videoUrl,
    originalMessage: message,
    user: $input.first().json.user,
    timestamp: new Date().toISOString().split("T")[0]
  }
}];
```

---

### Node 3: Super Data — Get Transcript
**Type:** Super Data
**Operation:** Get YouTube Transcript
**Video ID:** `{{ $json.videoId }}`
**Language:** `en` (fallback: auto)

**Output fields used downstream:**
- `transcript` — full text
- `title` — video title
- `channel` — channel name
- `duration` — video length

---

### Node 4: GitHub — Write File
**Type:** GitHub
**Operation:** Create File
**Repository Owner:** `thefeedmedia`
**Repository Name:** `tfm-vault`
**File Path:** `research/youtube-transcripts/{{ $json.title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').substring(0, 60) }}.md`

**Commit Message:** `youtube-transcript: {{ $json.title }}`

**File Content:**
```
---
title: "{{ $json.title }}"
channel: "{{ $json.channel }}"
url: "{{ $('Extract URL').first().json.videoUrl }}"
duration: "{{ $json.duration }}"
captured: "{{ $('Extract URL').first().json.timestamp }}"
processed: false
---

# {{ $json.title }}
**Channel:** {{ $json.channel }}
**URL:** {{ $('Extract URL').first().json.videoUrl }}
**Duration:** {{ $json.duration }}

---

## Raw Transcript

{{ $json.transcript }}
```

---

## Error Handling

Add an Error Trigger node that catches failures and posts to #ai-stuff:

```
"Couldn't process that video: {{ $json.errorMessage }}"
```

Common failures:
- No transcript available (live streams, private videos, no captions)
- GitHub token expired
- Super Data node not installed

---

## Processing Transcripts in Claude Code

Once transcripts land in `research/youtube-transcripts/`, process them in any Claude Code session:

```
Read the unprocessed transcripts in research/youtube-transcripts/
(where processed: false in frontmatter) and extract insights relevant
to TFM's setup. Update the frontmatter to processed: true when done.
Save insights to memory/external-ai-tooling-knowledge.md.
```

Or build a `/process-transcripts` skill that does this automatically and can be added to the Sunday cron alongside `/weekly-enrichment`.

---

## Testing

1. [ ] Install Super Data community node
2. [ ] Add GitHub credential with repo scope
3. [ ] Create `research/youtube-transcripts/` folder in repo (or let the first commit create it)
4. [ ] Post a YouTube URL in #ai-stuff
5. [ ] Verify: transcript file appears in GitHub within 30 seconds
6. [ ] Verify: Obsidian Git pulls it on next sync
7. [ ] Test error: post a non-YouTube URL, confirm error message

## Test URLs
- Any recent Claude Code tutorial
- Any Simon Scrapes or Chase H AI video
