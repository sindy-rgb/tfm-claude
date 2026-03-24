# n8n Self-Healing Workflow Monitor

## Overview

A monitoring workflow that runs on the TFM n8n instance (`https://n8n-zwzfv-u62151.vm.elestio.app/`). When any workflow fails, an Error Trigger captures the failure, a Claude AI agent diagnoses the root cause, and the results are posted to `#tfm-ops` in Slack. For non-critical transient errors, the workflow can auto-retry after a configurable delay.

---

## Architecture

```
Error Trigger
    |
    v
Get Workflow Details (HTTP Request - n8n internal API)
    |
    v
Format Error Context (Set node - merge error + workflow data)
    |
    v
AI Diagnostician (AI Agent + Claude Model)
    |
    v
Parse AI Response (Code node - extract structured JSON)
    |
    v
Check Severity (IF node)
    |
    +-- TRUE (CRITICAL / WARNING) --> Notify Slack
    |                                     |
    |                                     v
    |                              Should Auto-Retry? (IF node)
    |                                     |
    |                                +-- TRUE --> Wait --> Retry Failed Workflow (HTTP Request)
    |                                +-- FALSE --> (end)
    |
    +-- FALSE (INFO only) --> Info Only - No Action (NoOp)
```

---

## Node-by-Node Explanation

### 1. Error Trigger (`n8n-nodes-base.errorTrigger`)
- **Purpose**: Entry point. Fires whenever ANY workflow on this n8n instance fails.
- **Output data**: `execution.error.message`, `execution.error.node.name`, `execution.workflow.id`, `execution.workflow.name`, `execution.id`
- **Configuration**: None required -- it listens automatically.
- **Note**: This workflow must be set as the **Error Workflow** in n8n Settings, or each individual workflow must reference this workflow's ID in its error workflow setting.

### 2. Get Workflow Details (`n8n-nodes-base.httpRequest`)
- **Purpose**: Fetch the full workflow JSON from the n8n API so the AI agent can see the node configuration that failed.
- **Method**: GET
- **URL**: `https://n8n-zwzfv-u62151.vm.elestio.app/api/v1/workflows/{{ $json.execution.workflow.id }}`
- **Auth**: Uses an `httpHeaderAuth` credential with the n8n API key (`X-N8N-API-KEY`).
- **Why**: The Error Trigger only provides the error message and node name. The full workflow JSON lets the AI see how the failed node was configured.

### 3. Format Error Context (`n8n-nodes-base.set`)
- **Purpose**: Merge error details and workflow JSON into a clean object for the AI agent.
- **Fields extracted**:
  - `error_message` -- from Error Trigger
  - `failed_node` -- from Error Trigger
  - `workflow_name` -- from Error Trigger
  - `workflow_id` -- from Error Trigger
  - `workflow_json` -- truncated to 3000 chars from Get Workflow Details
  - `execution_url` -- constructed link to the failed execution

### 4. AI Diagnostician (`@n8n/n8n-nodes-langchain.agent`)
- **Purpose**: Claude-powered AI agent that analyzes the error and produces a structured diagnosis.
- **Agent type**: Conversational Agent
- **System prompt**: Contains a comprehensive lookup table of common n8n failure patterns (ECONNREFUSED, 401, 404, 429, SPREADSHEET_NOT_FOUND, undefined property access, etc.) with severity ratings and retry guidance.
- **User prompt**: Receives the formatted error context and asks for a JSON response with: diagnosis, severity, suggested_fix, auto_retry, retry_delay_minutes.
- **Connected model**: Claude (Anthropic) via `@n8n/n8n-nodes-langchain.lmChatAnthropic` on the `ai_languageModel` port.

### 5. Claude Model (`@n8n/n8n-nodes-langchain.lmChatAnthropic`)
- **Purpose**: The LLM powering the AI agent.
- **Model**: `claude-sonnet-4-20250514` (fast, cost-effective for diagnostic tasks)
- **Temperature**: 0.2 (low -- we want deterministic diagnostics)
- **Max tokens**: 1024
- **Connection**: Wired to AI Diagnostician via `ai_languageModel` port.

### 6. Parse AI Response (`n8n-nodes-base.code`)
- **Purpose**: Extract structured JSON from the AI agent's text output. Includes fallback handling if the AI returns malformed JSON.
- **Logic**:
  1. Attempt to parse the AI output as JSON
  2. If parsing fails, use regex to find a JSON object in the text
  3. If all parsing fails, create a fallback object with severity=WARNING
  4. Merge parsed diagnosis with context fields (workflow_name, workflow_id, execution_url)

### 7. Check Severity (`n8n-nodes-base.if`)
- **Purpose**: Route based on severity level.
- **Condition**: `severity != "INFO"`
  - TRUE (output 0) --> CRITICAL or WARNING errors go to Slack
  - FALSE (output 1) --> INFO-level issues go to NoOp (logged but not alerted)

### 8. Notify Slack (`n8n-nodes-base.slack`)
- **Purpose**: Post the diagnostic report to `#tfm-ops`.
- **Channel**: `#tfm-ops`
- **Message format**: Structured alert with workflow name, failed node, severity, error message, AI diagnosis, suggested fix, auto-retry status, and a link to view the execution.
- **Auth**: Uses Slack OAuth2 credential configured in n8n.

### 9. Should Auto-Retry? (`n8n-nodes-base.if`)
- **Purpose**: Determine if the workflow should be automatically retried.
- **Conditions** (AND):
  - `auto_retry == true` (AI recommended retry)
  - `severity != "CRITICAL"` (never auto-retry critical failures)
- **TRUE**: Proceed to wait and retry
- **FALSE**: End (human intervention needed)

### 10. Wait Before Retry (`n8n-nodes-base.wait`)
- **Purpose**: Pause before retrying. Duration comes from the AI's `retry_delay_minutes` field (typically 15 minutes for transient errors).
- **Amount**: Dynamic from `{{ $json.retry_delay_minutes }}`
- **Unit**: Minutes

### 11. Retry Failed Workflow (`n8n-nodes-base.httpRequest`)
- **Purpose**: Re-execute the failed workflow via the n8n API.
- **Method**: POST
- **URL**: `https://n8n-zwzfv-u62151.vm.elestio.app/api/v1/workflows/{{ $json.workflow_id }}/run`
- **Auth**: Same `httpHeaderAuth` credential as Get Workflow Details.
- **Note**: This triggers a new execution of the failed workflow. If it fails again, the Error Trigger will fire again, creating a feedback loop. The auto-retry logic only fires for non-CRITICAL transient errors, so infinite loops are unlikely but should be monitored.

### 12. Info Only - No Action (`n8n-nodes-base.noOp`)
- **Purpose**: Terminus for INFO-level errors. These are logged in execution history but do not generate Slack alerts.

---

## Complete Workflow JSON

Copy and paste this into n8n via **Import from JSON** (Settings menu > Import from File/URL > paste JSON).

```json
{
  "name": "Self-Healing Workflow Monitor",
  "nodes": [
    {
      "id": "error-trigger-1",
      "name": "Error Trigger",
      "type": "n8n-nodes-base.errorTrigger",
      "typeVersion": 1,
      "position": [250, 300],
      "parameters": {}
    },
    {
      "id": "get-workflow-1",
      "name": "Get Workflow Details",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [480, 300],
      "parameters": {
        "method": "GET",
        "url": "=https://n8n-zwzfv-u62151.vm.elestio.app/api/v1/workflows/{{ $json.execution.workflow.id }}",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "options": {}
      }
    },
    {
      "id": "format-context-1",
      "name": "Format Error Context",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [710, 300],
      "parameters": {
        "mode": "manual",
        "duplicateItem": false,
        "assignments": {
          "assignments": [
            {
              "id": "error_message",
              "name": "error_message",
              "value": "={{ $('Error Trigger').item.json.execution.error.message }}",
              "type": "string"
            },
            {
              "id": "failed_node",
              "name": "failed_node",
              "value": "={{ $('Error Trigger').item.json.execution.error.node.name }}",
              "type": "string"
            },
            {
              "id": "workflow_name",
              "name": "workflow_name",
              "value": "={{ $('Error Trigger').item.json.execution.workflow.name }}",
              "type": "string"
            },
            {
              "id": "workflow_id",
              "name": "workflow_id",
              "value": "={{ $('Error Trigger').item.json.execution.workflow.id }}",
              "type": "string"
            },
            {
              "id": "workflow_json",
              "name": "workflow_json",
              "value": "={{ JSON.stringify($('Get Workflow Details').item.json).substring(0, 3000) }}",
              "type": "string"
            },
            {
              "id": "execution_url",
              "name": "execution_url",
              "value": "={{ 'https://n8n-zwzfv-u62151.vm.elestio.app/workflow/' + $('Error Trigger').item.json.execution.workflow.id + '/executions/' + $('Error Trigger').item.json.execution.id }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      }
    },
    {
      "id": "ai-agent-1",
      "name": "AI Diagnostician",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "typeVersion": 1.7,
      "position": [940, 300],
      "parameters": {
        "agent": "conversationalAgent",
        "promptType": "define",
        "text": "=A workflow has failed. Diagnose the issue and provide a structured response.\n\n**Workflow:** {{ $json.workflow_name }}\n**Failed Node:** {{ $json.failed_node }}\n**Error Message:** {{ $json.error_message }}\n**Workflow Config (truncated):** {{ $json.workflow_json }}\n\nRespond ONLY with valid JSON in this exact format (no markdown, no code fences):\n{\n  \"diagnosis\": \"Plain English root cause explanation\",\n  \"failed_node\": \"Name of the failed node\",\n  \"severity\": \"CRITICAL or WARNING or INFO\",\n  \"suggested_fix\": \"Specific fix instructions\",\n  \"auto_retry\": true or false,\n  \"retry_delay_minutes\": 15\n}",
        "systemMessage": "You are an n8n workflow debugger for The Feed Media (TFM), a newsletter growth agency. When a workflow fails, you diagnose the root cause and suggest a fix.\n\nCommon failure patterns:\n- \"ECONNREFUSED\" or \"ETIMEDOUT\" → External service is down. Suggest retry in 15 minutes. Severity: WARNING. auto_retry: true.\n- \"401 Unauthorized\" or \"403 Forbidden\" → Expired token or revoked access. Identify which credential and suggest re-authentication. Severity: CRITICAL. auto_retry: false.\n- \"404 Not Found\" → Wrong endpoint URL or deleted resource (sheet ID, page ID, etc.). Severity: CRITICAL. auto_retry: false.\n- \"429 Too Many Requests\" → Rate limited. Suggest adding a Wait node or reducing batch size. Severity: WARNING. auto_retry: true.\n- \"SPREADSHEET_NOT_FOUND\" or \"Sheet not found\" → Google Sheet ID is wrong or was deleted. Severity: CRITICAL. auto_retry: false.\n- \"Cannot read properties of undefined\" → Data mapping issue. Previous node output doesn't match expected structure. Severity: WARNING. auto_retry: false.\n- \"Workflow could not be activated\" → Trigger node misconfigured. Severity: CRITICAL. auto_retry: false.\n- \"ENOTFOUND\" → DNS resolution failed. Service hostname wrong or DNS is down. Severity: WARNING. auto_retry: true.\n- \"socket hang up\" or \"ECONNRESET\" → Connection dropped mid-request. Severity: WARNING. auto_retry: true.\n\nFor each error, your JSON response must include:\n1. diagnosis: Root cause in plain English\n2. failed_node: Which node failed and why\n3. severity: CRITICAL (blocks operations, needs human), WARNING (degraded, may self-resolve), INFO (cosmetic/non-blocking)\n4. suggested_fix: Specific fix instructions\n5. auto_retry: Whether automatic retry is appropriate\n6. retry_delay_minutes: How long to wait before retry (if applicable)\n\nAlways respond with raw JSON only. No markdown formatting, no code fences, no explanation outside the JSON.",
        "options": {}
      }
    },
    {
      "id": "parse-response-1",
      "name": "Parse AI Response",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [1170, 300],
      "parameters": {
        "jsCode": "const aiOutput = $input.first().json.output || $input.first().json.text || '';\n\nlet parsed;\ntry {\n  // Try to parse the AI response as JSON\n  const jsonMatch = aiOutput.match(/\\{[\\s\\S]*\\}/);\n  parsed = JSON.parse(jsonMatch ? jsonMatch[0] : aiOutput);\n} catch (e) {\n  // Fallback if AI didn't return valid JSON\n  parsed = {\n    diagnosis: aiOutput,\n    failed_node: $('Format Error Context').item.json.failed_node || 'Unknown',\n    severity: 'WARNING',\n    suggested_fix: 'Review the error manually.',\n    auto_retry: false,\n    retry_delay_minutes: 0\n  };\n}\n\n// Merge with context from earlier nodes\nreturn [{\n  json: {\n    ...parsed,\n    workflow_name: $('Format Error Context').item.json.workflow_name,\n    workflow_id: $('Format Error Context').item.json.workflow_id,\n    error_message: $('Format Error Context').item.json.error_message,\n    execution_url: $('Format Error Context').item.json.execution_url\n  }\n}];"
      }
    },
    {
      "id": "if-severity-1",
      "name": "Check Severity",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [1400, 300],
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict",
            "version": 2
          },
          "conditions": [
            {
              "id": "severity-check",
              "leftValue": "={{ $json.severity }}",
              "rightValue": "INFO",
              "operator": {
                "type": "string",
                "operation": "notEquals"
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      }
    },
    {
      "id": "slack-notify-1",
      "name": "Notify Slack",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1650, 200],
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#tfm-ops",
        "text": "=:wrench: *n8n Workflow Error — Auto-Diagnosed*\n\n*Workflow:* {{ $json.workflow_name }}\n*Failed Node:* {{ $json.failed_node }}\n*Severity:* {{ $json.severity }}\n\n*Error:* {{ $json.error_message }}\n\n*Diagnosis:* {{ $json.diagnosis }}\n\n*Suggested Fix:* {{ $json.suggested_fix }}\n\n*Auto-Retry:* {{ $json.auto_retry ? 'Yes (' + $json.retry_delay_minutes + ' min)' : 'No — manual intervention needed' }}\n\n<{{ $json.execution_url }}|View Execution>",
        "otherOptions": {}
      }
    },
    {
      "id": "if-retry-1",
      "name": "Should Auto-Retry?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [1900, 200],
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict",
            "version": 2
          },
          "conditions": [
            {
              "id": "retry-check-1",
              "leftValue": "={{ $json.auto_retry }}",
              "rightValue": true,
              "operator": {
                "type": "boolean",
                "operation": "equals"
              }
            },
            {
              "id": "retry-check-2",
              "leftValue": "={{ $json.severity }}",
              "rightValue": "CRITICAL",
              "operator": {
                "type": "string",
                "operation": "notEquals"
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      }
    },
    {
      "id": "wait-1",
      "name": "Wait Before Retry",
      "type": "n8n-nodes-base.wait",
      "typeVersion": 1.1,
      "position": [2150, 100],
      "parameters": {
        "amount": "={{ $json.retry_delay_minutes }}",
        "unit": "minutes"
      }
    },
    {
      "id": "retry-workflow-1",
      "name": "Retry Failed Workflow",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [2400, 100],
      "parameters": {
        "method": "POST",
        "url": "=https://n8n-zwzfv-u62151.vm.elestio.app/api/v1/workflows/{{ $json.workflow_id }}/run",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "sendBody": false,
        "options": {}
      }
    },
    {
      "id": "noop-info-1",
      "name": "Info Only - No Action",
      "type": "n8n-nodes-base.noOp",
      "typeVersion": 1,
      "position": [1650, 450],
      "parameters": {}
    },
    {
      "id": "anthropic-model-1",
      "name": "Claude Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatAnthropic",
      "typeVersion": 1.2,
      "position": [960, 520],
      "parameters": {
        "model": "claude-sonnet-4-20250514",
        "options": {
          "maxTokensToSample": 1024,
          "temperature": 0.2
        }
      }
    }
  ],
  "connections": {
    "Error Trigger": {
      "main": [
        [
          {
            "node": "Get Workflow Details",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Workflow Details": {
      "main": [
        [
          {
            "node": "Format Error Context",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Format Error Context": {
      "main": [
        [
          {
            "node": "AI Diagnostician",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AI Diagnostician": {
      "main": [
        [
          {
            "node": "Parse AI Response",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Parse AI Response": {
      "main": [
        [
          {
            "node": "Check Severity",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Check Severity": {
      "main": [
        [
          {
            "node": "Notify Slack",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Info Only - No Action",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Notify Slack": {
      "main": [
        [
          {
            "node": "Should Auto-Retry?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Should Auto-Retry?": {
      "main": [
        [
          {
            "node": "Wait Before Retry",
            "type": "main",
            "index": 0
          }
        ],
        []
      ]
    },
    "Wait Before Retry": {
      "main": [
        [
          {
            "node": "Retry Failed Workflow",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Claude Model": {
      "ai_languageModel": [
        [
          {
            "node": "AI Diagnostician",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1",
    "saveManualExecutions": true,
    "callerPolicy": "workflowsFromSameOwner",
    "errorWorkflow": ""
  }
}
```

---

## Setup Prerequisites

### 1. Anthropic API Key Credential

In n8n, go to **Credentials** > **New Credential** > search for **Anthropic**.

- **Name**: `Anthropic API` (or similar)
- **API Key**: Your Anthropic API key
- After saving, assign this credential to the **Claude Model** node.

### 2. Slack OAuth2 Credential

In n8n, go to **Credentials** > **New Credential** > search for **Slack**.

- **Name**: `TFM Slack` (or similar)
- **Auth type**: OAuth2
- Follow the Slack OAuth2 flow to authorize
- **Required scopes**: `chat:write`, `channels:read`
- After saving, assign this credential to the **Notify Slack** node.

### 3. n8n API Key (HTTP Header Auth)

This is used by the "Get Workflow Details" and "Retry Failed Workflow" HTTP Request nodes to call the n8n internal API.

In n8n, go to **Credentials** > **New Credential** > search for **Header Auth**.

- **Name**: `n8n API Key`
- **Header Name**: `X-N8N-API-KEY`
- **Header Value**: Your n8n API key (generate one in n8n Settings > API > Create API Key)
- After saving, assign this credential to both HTTP Request nodes.

### 4. Slack Channel

Ensure the `#tfm-ops` channel exists in Slack and the Slack bot has been invited to it. If using a different channel, update the channel name in the **Notify Slack** node.

---

## How to Deploy

### Step 1: Import the Workflow

1. Open your n8n instance: `https://n8n-zwzfv-u62151.vm.elestio.app/`
2. Click **+ Add Workflow** (or use the menu)
3. Click the **...** menu (top right) > **Import from JSON**
4. Paste the complete workflow JSON from above
5. Click **Import**

### Step 2: Assign Credentials

After import, each node requiring credentials will show a warning. Click each node and assign:

| Node | Credential Type | Credential to Assign |
|------|----------------|---------------------|
| Get Workflow Details | Header Auth | `n8n API Key` |
| Claude Model | Anthropic | `Anthropic API` |
| Notify Slack | Slack OAuth2 | `TFM Slack` |
| Retry Failed Workflow | Header Auth | `n8n API Key` |

### Step 3: Configure as Error Workflow

**Option A (Global)**: In n8n Settings, set this workflow as the global error workflow. All workflow failures will trigger it.

**Option B (Per-workflow)**: In each workflow's settings, set the "Error Workflow" field to this workflow's ID. More granular control.

### Step 4: Test

1. Create a test workflow with a node that intentionally fails (e.g., HTTP Request to an invalid URL)
2. Run the test workflow
3. Verify the Error Trigger fires and a Slack message appears in `#tfm-ops`
4. Check the diagnosis quality

### Step 5: Activate

1. Toggle the workflow to **Active** (top right switch)
2. The workflow will now automatically process all workflow failures

---

## Operational Notes

### Avoiding Infinite Loops

The auto-retry feature could theoretically create a loop (workflow fails -> monitor retries -> fails again -> monitor retries...). Safeguards:

1. **CRITICAL errors never auto-retry** -- the IF node blocks them
2. **Transient errors typically self-resolve** -- the 15-minute wait gives services time to recover
3. **Monitor the execution history** of this workflow itself for repeated retries of the same workflow

**Future improvement**: Add a Code node before the retry that checks execution history and stops retrying after N attempts.

### Cost Considerations

- Each failure diagnosis costs one Claude API call (~1K input tokens, ~200 output tokens)
- At TFM's scale (25 clients, ~10-20 active workflows), expect 5-20 failures per week
- Estimated monthly cost: $1-5 in API usage

### Extending the Diagnostics

To add new failure patterns, update the system prompt in the **AI Diagnostician** node. The AI will learn from the patterns in the prompt to better classify errors.

### Data Passed Through Wait Node

The Wait node in n8n preserves the input data. After the wait period, `$json.workflow_id` is still available for the retry HTTP Request.

---

## Severity Definitions

| Severity | Meaning | Slack Alert | Auto-Retry |
|----------|---------|-------------|------------|
| CRITICAL | Blocks operations, needs human intervention (auth failures, deleted resources, misconfig) | Yes | Never |
| WARNING | Degraded service, may self-resolve (timeouts, rate limits, connection drops) | Yes | If AI recommends |
| INFO | Cosmetic or non-blocking (minor data issues, optional features) | No (logged only) | No |
