---
title: "Zed Editor with Look2Eye Setup Guide"
description: "Set up Look2Eye in Zed Editor for AI-assisted coding — one API key unlocks Claude, GPT, Gemini, and other leading global models with inline completions and chat"
---


# Zed Editor


<img src="/docs/images/en/integrations/zed/01-configure-look2eye-in-zed-editor.webp" alt="Configure Look2Eye in Zed Editor" width="70%" />


## Why Zed?


[Zed](https://zed.dev) offers one of the most complete AI coding experiences available:


- **Native agent support** — Built-in Claude Code, Codex CLI, and Gemini CLI as external agents
- **Custom LLM Provider** — Connect any model via OpenAI compatible protocol
- **High performance** — Written in Rust, fast startup and low resource usage


Paired with Look2Eye, one API Key gives you access to leading global models in Zed.


## Quick Start


### 1. Get an API Key


Go to the [Look2Eye Console](https://api.look2eye.com/keys) to create an API Key.


### 2. Add Provider


**Agent Panel (Recommended)**

Add visually through the Agent Panel without editing JSON.


1. Press `⌘ + Shift + A` to open the Agent Panel
2. Click **+ Add Provider** in the LLM Providers area
3. Fill in the configuration as shown:


<img src="/docs/images/en/integrations/zed/02-add-look2eye-provider-in-zed.webp" alt="Add Look2Eye Provider in Zed" width="70%" />


| Label | Field | Value |
| --- | --- | --- |
| ① | Provider Name | `Look2Eye` |
| ② | API URL | `https://api.api.look2eye.com/v1` |
| ③ | API Key | Your Look2Eye API Key |
| ④ | Model Name | `openai/gpt-5.4-mini` |
| ⑤ | Max Completion Tokens | `512000` |
| ⑥ | Capabilities | Check the capabilities supported by the model |


Click **+ Add Model** to add more models.

**settings.json**

Batch-configure all models via `settings.json`.


1. Press `⌘ + ,` to open settings, click **Edit in settings.json** in the top right
2. Add the following configuration:


```json filename="~/.config/zed/settings.json"
{
  "language_models": {
    "openai_compatible": {
      "Look2Eye": {
        "api_url": "https://api.api.look2eye.com/v1",
        "available_models": [
          {
            "name": "openai/gpt-5.3-codex",
            "display_name": "GPT-5.3 Codex",
            "max_tokens": 512000,
            "max_output_tokens": 65536,
            "capabilities": {
              "tools": true,
              "images": true
            }
          },
          {
            "name": "openai/gpt-5-mini",
            "display_name": "GPT-5 Mini",
            "max_tokens": 256000,
            "max_output_tokens": 32768,
            "capabilities": {
              "tools": true,
              "images": true
            }
          },
          {
            "name": "moonshotai/kimi-k2.5",
            "display_name": "Kimi K2.5",
            "max_tokens": 262144,
            "max_output_tokens": 262144,
            "capabilities": {
              "tools": true,
              "images": true
            }
          },
          {
            "name": "bailian/qwen3-max",
            "display_name": "Qwen3 Max",
            "max_tokens": 256000,
            "max_output_tokens": 64000,
            "capabilities": {
              "tools": true,
              "images": false
            }
          }
        ]
      }
    }
  }
}
```


1. After saving, Zed will prompt you to enter your API Key


> ℹ️ `settings.json` is ideal for batch-adding models. Add or remove models by editing the `available_models` array.


> ℹ️ The API Key is securely stored in the system keychain (macOS Keychain / Linux Secret Service) and is never written in plaintext to config files.


## Getting Started


Zed’s Agent Panel has two modes:


| Mode | Description |
| --- | --- |
| **Zed Agent** | Built-in AI assistant using your configured LLM Provider (e.g. Look2Eye) |
| **External Agents** | External agents (Claude Code, Codex CLI, Gemini CLI), run independently |


Start a conversation with **Zed Agent**:


<img src="/docs/images/en/integrations/zed/03-zed-agent-panel-model-selection.webp" alt="Zed Agent Panel model selection" width="70%" />


| Step | Action |
| --- | --- |
| ① | Click **+** → Select **Zed Agent** (`⌘ + N`) |
| ② | External Agents area shows connected external agents |
| ③ | Bottom-right model selector → **Look2Eye** group → Select model |


<img src="/docs/images/en/integrations/zed/04-zed-agent-conversation-demo.webp" alt="Zed Agent conversation demo" width="70%" />


## Recommended Models


For recommended models, see the [Model Marketplace](https://api.look2eye.com/models).


## Adding More Models


Each model requires the following parameters:


| Field | Required | Description |
| --- | --- | --- |
| `name` | Yes | Model ID, e.g. `openai/gpt-5.4-mini` |
| `display_name` | No | UI display name |
| `max_tokens` | Yes | Context window size |
| `max_output_tokens` | No | Maximum output token count |
| `capabilities.tools` | No | Whether Function Calling is supported |
| `capabilities.images` | No | Whether image input is supported |


### Pro Tip


Manually filling parameters too slow? Click **Copy Page** in the top right of this page (or send this page URL directly), along with `https://api.api.look2eye.com/v1/models`, to an AI and have it auto-generate the complete `settings.json` configuration.


Go to settings → Click **Edit in settings.json** in the top right to paste:


<img src="/docs/images/en/integrations/zed/05-edit-in-settings-json.webp" alt="Edit in settings.json" width="70%" />


## Troubleshooting


**Look2Eye not showing in model list**


Verify `settings.json` format is correct, then restart Zed.


**Authentication error**


Command Palette `⌘ + Shift + P` → Search `language model: reset credentials` → Re-enter your API Key.


**Model doesn’t support tool calling**


Set `capabilities.tools` to `false`.
