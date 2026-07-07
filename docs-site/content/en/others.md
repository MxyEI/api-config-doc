---
title: "Other Integrations"
description: "Configure Look2Eye in Cursor, Continue, Aider, LangChain, and other AI dev tools — universal setup for any OpenAI/Anthropic-compatible client"
---


# Other Integrations


Look2Eye is compatible with OpenAI / Anthropic / Gemini protocols, which means it works with virtually any tool that uses these protocols. Below are configuration guides for some common tools.


## General Configuration Principles


Regardless of the tool, configuration follows these principles:


| Tool’s Protocol | Base URL | API Key Header |
| --- | --- | --- |
| OpenAI Compatible | `https://api.api.look2eye.com/v1` | `Authorization: Bearer sk-xxx` |
| Anthropic Native | `https://api.api.look2eye.com/anthropic` | `x-api-key: sk-xxx` |
| Gemini Native | `https://api.api.look2eye.com/gemini` | `x-goog-api-key: sk-xxx` |


## Continue (VS Code / JetBrains)


[Continue](https://continue.dev) is an open-source AI coding assistant supporting VS Code and JetBrains IDEs.


```json filename="~/.continue/config.json"
{
  "models": [
    {
      "title": "Look2Eye GPT-4o",
      "provider": "openai",
      "model": "openai/gpt-4o",
      "apiBase": "https://api.api.look2eye.com/v1",
      "apiKey": "<your LOOK2EYE_API_KEY>"
    },
    {
      "title": "Look2Eye Claude Sonnet",
      "provider": "openai",
      "model": "anthropic/claude-sonnet-4.6",
      "apiBase": "https://api.api.look2eye.com/v1",
      "apiKey": "<your LOOK2EYE_API_KEY>"
    }
  ]
}
```


## Aider


[Aider](https://aider.chat) is a command-line AI pair programming tool.


```text filename="~/.zshrc"
export OPENAI_API_KEY=<your LOOK2EYE_API_KEY>
export OPENAI_API_BASE=https://api.api.look2eye.com/v1
```


```text
aider --model openai/gpt-4o
```


## BoltAI (macOS)


[BoltAI](https://boltai.com) is a native macOS AI assistant app.


1. Open BoltAI → **Preferences** → **Providers**
2. Add **Custom OpenAI**
3. Enter Base URL: `https://api.api.look2eye.com/v1`
4. Enter your API Key


## TypingMind


[TypingMind](https://typingmind.com) is an AI chat interface tool.


1. Go to **Settings** → **Custom Endpoint**
2. API Endpoint: `https://api.api.look2eye.com/v1`
3. API Key: Your Look2Eye API Key


## ChatBox


[ChatBox](https://chatboxai.app) is a cross-platform AI desktop client.


1. Open ChatBox → **Settings** → **AI Provider**
2. Select **OpenAI API Compatible**
3. API Domain: `https://api.api.look2eye.com`
4. API Key: Your Look2Eye API Key


## Custom Integration


For other tools not listed here, the general steps are:


1. Find the tool’s API configuration settings
2. Set the API Base URL to `https://api.api.look2eye.com/v1`
3. Set the API Key to your Look2Eye Key
4. Use the `provider/model-name` format for model names


> ℹ️ If you’ve successfully configured Look2Eye in a tool, we welcome PRs to add it to this documentation: [GitHub Repository](https://github.com/look2eye/pohu-docs)
