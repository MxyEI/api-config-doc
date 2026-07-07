---
title: "OpenClaw"
description: "Configure Look2Eye in OpenClaw — one API key unlocks leading global models for your personal AI assistant on WhatsApp, Telegram, and Slack"
---


# OpenClaw


[OpenClaw](https://openclaw.ai) is an open-source local AI assistant that interacts with you through WhatsApp, Telegram, Slack, and other messaging apps. It can perform real actions — managing emails, calendars, flight check-ins, browsing the web, and more. It runs entirely locally, so your data never leaves your device.


## Why Pair with Look2Eye?


- **Leading Global Models** — One API Key for Claude, GPT, Gemini, Qwen, Doubao, and all major models
- **Flexible agent strategies** — Assign different models to different agents: Sonnet for primary, Opus for reasoning, Haiku for lightweight tasks
- **99.9% SLA** — Multi-node redundancy with automatic failover
- **Cost control** — Unified billing dashboard with real-time token consumption monitoring


> ⚠️ As an agentic AI assistant, OpenClaw’s per-task token consumption is relatively high (typically 10K-100K+ tokens). We recommend choosing models based on task complexity to avoid unnecessary costs. This guide provides three configuration options for reference.


## Installation


```text filename="macOS / Linux"
curl -sSL https://openclaw.ai/install.sh | bash
```


```text filename="Windows (PowerShell)"
& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1)))
```


## Quick Start


### 1. Get an API Key


Go to the [Look2Eye Console](https://api.look2eye.com/keys) to create an API Key.


### 2. Run the Setup Wizard


OpenClaw provides an interactive wizard. Run the following command to get started:


```text
openclaw onboard
```


In the wizard, select **Custom Provider** and enter the following:


| Setting | Value |
| --- | --- |
| **Provider Type** | `anthropic-messages` |
| **Base URL** | `https://api.api.look2eye.com/anthropic` |
| **API Key** | Your Look2Eye API Key |
| **Model** | `anthropic/claude-sonnet-4.6` |


### 3. Start and Verify


```text
openclaw start
```


Send a message to OpenClaw to test connectivity. If you receive a normal response, the setup is complete.


> ℹ️ The wizard automatically generates an `openclaw.json` configuration file. For more fine-grained control, see the full configuration below.


## Full Configuration


OpenClaw manages all configuration through `~/.openclaw/openclaw.json` (supports JSON5 format with comments).


### Provider Configuration


Providers are defined under `models.providers`. Each provider needs an API protocol type, URL, and key:


```json filename="~/.openclaw/openclaw.json"
{
  "models": {
    "providers": {
      "look2eye-anthropic": {
        "baseUrl": "https://api.api.look2eye.com/anthropic",
        "apiKey": "${LOOK2EYE_API_KEY}",
        "api": "anthropic-messages",
        "models": []
      },
      "look2eye-openai": {
        "baseUrl": "https://api.api.look2eye.com/v1",
        "apiKey": "${LOOK2EYE_API_KEY}",
        "api": "openai-responses",
        "models": []
      },
      "look2eye-gemini": {
        "baseUrl": "https://api.api.look2eye.com/gemini",
        "apiKey": "${LOOK2EYE_API_KEY}",
        "api": "google-generative-ai",
        "models": []
      }
    }
  }
}
```


> ℹ️ `apiKey` supports `${ENV_VAR}` syntax to reference environment variables, avoiding plaintext keys in config files. Three protocols correspond to different model families: Claude uses `look2eye-anthropic` (`anthropic-messages`), OpenAI uses `look2eye-openai` (`openai-responses`), Gemini uses `look2eye-gemini` (`google-generative-ai`). Other models can connect through `look2eye-openai`.


### Models Configuration


Models are defined in the `models` array of their corresponding provider. We provide three configurations based on your needs:


**Premium Setup**

**All-Claude lineup** — Maximum capability for demanding scenarios.


```jsonc filename="openclaw.json — models.providers"
{
  "models": {
    "providers": {
      "look2eye-anthropic": {
        "baseUrl": "https://api.api.look2eye.com/anthropic",
        "apiKey": "${LOOK2EYE_API_KEY}",
        "api": "anthropic-messages",
        "models": [
          {
            "id": "anthropic/claude-sonnet-4.6",
            "name": "Claude Sonnet 4.6",
            "input": ["text", "image", "file"],
            "contextWindow": 200000,
            "maxTokens": 64000
          },
          {
            "id": "anthropic/claude-opus-4.6",
            "name": "Claude Opus 4.6",
            "reasoning": true,
            "input": ["text", "image", "file"],
            "contextWindow": 200000,
            "maxTokens": 128000
          },
          {
            "id": "anthropic/claude-haiku-4.5",
            "name": "Claude Haiku 4.5",
            "input": ["text", "image", "file"],
            "contextWindow": 200000,
            "maxTokens": 64000
          }
        ]
      }
    }
  }
}
```


| Model | Role | Use Case |
| --- | --- | --- |
| `anthropic/claude-sonnet-4.6` | Primary | Daily chat, task execution, code generation |
| `anthropic/claude-opus-4.6` | Deep reasoning | Complex analysis, long-chain reasoning, research |
| `anthropic/claude-haiku-4.5` | Fast response | Simple queries, quick replies, lightweight tasks |

> ℹ️ Claude thinking configuration is version-specific. Sonnet 4.5 uses `enabled + budget_tokens`; Sonnet 4.6 / Opus 4.6 should use `adaptive`. See [Claude Thinking Modes in the Anthropic Messages API](https://api.look2eye.com/en/api/anthropic/messages#claude-thinking-modes) for the full matrix.

**Balanced Setup**

**OpenAI Codex combo** — Strong coding capabilities with balanced general performance.


```jsonc filename="openclaw.json — models.providers"
{
  "models": {
    "providers": {
      "look2eye-openai": {
        "baseUrl": "https://api.api.look2eye.com/v1",
        "apiKey": "${LOOK2EYE_API_KEY}",
        "api": "openai-responses",
        "models": [
          {
            "id": "openai/gpt-5.3-codex",
            "name": "GPT 5.3 Codex",
            "reasoning": true,
            "input": ["text", "image", "audio", "file"],
            "contextWindow": 512000,
            "maxTokens": 128000
          },
          {
            "id": "openai/gpt-5.1-codex-mini",
            "name": "GPT 5.1 Codex Mini",
            "input": ["text", "image", "audio", "file"],
            "contextWindow": 256000,
            "maxTokens": 65536
          }
        ]
      }
    }
  }
}
```


| Model | Role | Use Case |
| --- | --- | --- |
| `openai/gpt-5.3-codex` | Primary + reasoning | Daily chat, complex tasks, code refactoring |
| `openai/gpt-5.1-codex-mini` | Fast response | Lightweight tasks, code completion, quick Q&A |


> ℹ️ OpenAI models connect through the `look2eye-openai` provider using the `openai-responses` protocol.

**Cost-Effective Setup**

**Budget-friendly choice** — Low token prices, ideal for high-frequency daily use.


```jsonc filename="openclaw.json — models.providers"
{
  "models": {
    "providers": {
      "look2eye-openai": {
        "baseUrl": "https://api.api.look2eye.com/v1",
        "apiKey": "${LOOK2EYE_API_KEY}",
        "api": "openai-responses",
        "models": [
          {
            "id": "bailian/qwen3.5-plus",
            "name": "Qwen 3.5 Plus",
            "input": ["text", "image"],
            "contextWindow": 1000000,
            "maxTokens": 64000
          },
          {
            "id": "volcengine/doubao-seed-2.0-code",
            "name": "Doubao Seed 2.0 Code",
            "input": ["text", "image"],
            "contextWindow": 256000,
            "maxTokens": 128000
          }
        ]
      }
    }
  }
}
```


| Model | Role | Use Case |
| --- | --- | --- |
| `bailian/qwen3.5-plus` | Primary + reasoning | Daily chat, general tasks, Chinese-optimized |
| `volcengine/doubao-seed-2.0-code` | Code + fast | Code generation, debugging, quick replies |


### Agents Configuration


OpenClaw uses `agents.defaults` for global defaults and `agents.list` to define different agents, each of which can override default settings:


```json filename="openclaw.json — agents section"
{
  "agents": {
    "defaults": {
      "model": {
        "primary": "look2eye-anthropic/anthropic/claude-sonnet-4.6",
        "fallbacks": ["look2eye-anthropic/anthropic/claude-haiku-4.5"]
      },
      "models": {
        "look2eye-anthropic/anthropic/claude-opus-4.6": { "alias": "opus" },
        "look2eye-anthropic/anthropic/claude-sonnet-4.6": { "alias": "sonnet" },
        "look2eye-anthropic/anthropic/claude-haiku-4.5": { "alias": "haiku" }
      },
      "thinkingDefault": "low",
      "timeoutSeconds": 600,
      "maxConcurrent": 3
    },
    "list": [
      {
        "id": "main",
        "default": true
      },
      {
        "id": "research",
        "model": {
          "primary": "look2eye-anthropic/anthropic/claude-opus-4.6"
        }
      },
      {
        "id": "quick",
        "model": {
          "primary": "look2eye-anthropic/anthropic/claude-haiku-4.5"
        }
      }
    ]
  }
}
```


| Agent | Model | Purpose |
| --- | --- | --- |
| **main** | `claude-sonnet-4.6` (inherits defaults) | Default agent for all daily tasks |
| **research** | `claude-opus-4.6` | Deep research, complex reasoning, long-form analysis |
| **quick** | `claude-haiku-4.5` | Simple Q&A, fast responses, low cost |


> ℹ️ Model references use the format `provider-name/model-id` (e.g. `look2eye-anthropic/anthropic/claude-sonnet-4.6`). The `models` field in `defaults` defines model aliases for quick switching in conversations with `/model opus`. Agents in `list` inherit all `defaults` configuration and only need to override fields that differ.


## Full Configuration Example


Here’s a complete `openclaw.json` combining Provider, Models, and Agents configuration (premium setup):


```json filename="~/.openclaw/openclaw.json"
{
  "models": {
    "providers": {
      "look2eye-anthropic": {
        "baseUrl": "https://api.api.look2eye.com/anthropic",
        "apiKey": "${LOOK2EYE_API_KEY}",
        "api": "anthropic-messages",
        "models": [
          {
            "id": "anthropic/claude-sonnet-4.6",
            "name": "Claude Sonnet 4.6",
            "input": ["text", "image", "file"],
            "contextWindow": 200000,
            "maxTokens": 64000
          },
          {
            "id": "anthropic/claude-opus-4.6",
            "name": "Claude Opus 4.6",
            "reasoning": true,
            "input": ["text", "image", "file"],
            "contextWindow": 200000,
            "maxTokens": 128000
          },
          {
            "id": "anthropic/claude-haiku-4.5",
            "name": "Claude Haiku 4.5",
            "input": ["text", "image", "file"],
            "contextWindow": 200000,
            "maxTokens": 64000
          }
        ]
      },
      "look2eye-gemini": {
        "baseUrl": "https://api.api.look2eye.com/gemini",
        "apiKey": "${LOOK2EYE_API_KEY}",
        "api": "google-generative-ai",
        "models": [
          {
            "id": "models/google/gemini-2.5-flash",
            "name": "Gemini 2.5 Flash",
            "reasoning": true,
            "input": ["text", "image"],
            "contextWindow": 1000000,
            "maxTokens": 64000
          },
          {
            "id": "models/google/gemini-2.5-pro",
            "name": "Gemini 2.5 Pro",
            "reasoning": true,
            "input": ["text", "image"],
            "contextWindow": 1000000,
            "maxTokens": 64000
          }
        ]
      }
    }
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "look2eye-anthropic/anthropic/claude-sonnet-4.6",
        "fallbacks": ["look2eye-anthropic/anthropic/claude-haiku-4.5"]
      },
      "models": {
        "look2eye-anthropic/anthropic/claude-opus-4.6": { "alias": "opus" },
        "look2eye-anthropic/anthropic/claude-sonnet-4.6": { "alias": "sonnet" },
        "look2eye-anthropic/anthropic/claude-haiku-4.5": { "alias": "haiku" }
      },
      "thinkingDefault": "low",
      "timeoutSeconds": 600,
      "maxConcurrent": 3
    },
    "list": [
      {
        "id": "main",
        "default": true
      },
      {
        "id": "research",
        "model": {
          "primary": "look2eye-anthropic/anthropic/claude-opus-4.6"
        }
      },
      {
        "id": "quick",
        "model": {
          "primary": "look2eye-anthropic/anthropic/claude-haiku-4.5"
        }
      }
    ]
  }
}
```


## Use Cases


Once configured, send commands to OpenClaw through your messaging app:


- **Email management** — “Help me organize today’s unread emails by priority”
- **Schedule management** — “Schedule a team meeting tomorrow at 3 PM”
- **Information retrieval** — “Search for recent articles about AI Agents and summarize the key points”
- **Code assistance** — “Help me review this Python code for security issues”
- **Workflow automation** — “Send a daily team report to Slack #general channel every morning at 9 AM”


## Troubleshooting


**Cannot connect to Look2Eye**


Verify the `baseUrl` configuration is correct:


- Anthropic protocol: `https://api.api.look2eye.com/anthropic`
- OpenAI-Response protocol: `https://api.api.look2eye.com/v1`
- Gemini protocol: `https://api.api.look2eye.com/gemini`


**Model not found**


Verify the model ID format is correct. When defining models in `models.providers`, use the full ID returned by Look2Eye (e.g. `anthropic/claude-sonnet-4.6`). When referencing models in `agents`, add the provider name prefix: `look2eye-anthropic/anthropic/claude-sonnet-4.6`.


**High token consumption**


OpenClaw’s per-task consumption is relatively high. Recommendations:


1. Use `claude-haiku-4.5` or cost-effective models for daily tasks
2. Only switch to the `research` agent (using `claude-opus-4.6`) for complex tasks
3. Monitor usage in the [Look2Eye Console](https://api.look2eye.com/console/analytics)


**How to quickly switch models**


Use aliases in conversations: `/model opus`, `/model sonnet`, `/model haiku` (requires configuring aliases in `agents.defaults.models`).
