---
title: "其他工具集成"
description: "其他 OpenAI 兼容客户端接入 Look2Eye 的通用配置：base URL、API Key 规范"
---


Look2Eye 兼容 OpenAI / Anthropic / Gemini 三大协议，理论上支持任何使用这些协议的工具。以下是一些常见工具的配置方式。

## 通用配置原则

无论使用什么工具，配置方式都遵循以下原则：

| 工具使用的协议 | Base URL | API Key Header |
| --- | --- | --- |
| OpenAI 兼容 | `https://api.look2eye.com/v1` | `Authorization: Bearer sk-xxx` |
| Anthropic 原生 | `https://api.look2eye.com/anthropic` | `x-api-key: sk-xxx` |
| Gemini 原生 | `https://api.look2eye.com/gemini` | `x-goog-api-key: sk-xxx` |

## Continue (VS Code / JetBrains)

[Continue](https://continue.dev)  是一款开源的 AI 编码助手，支持 VS Code 和 JetBrains IDE。

```json filename="~/.continue/config.json"
{
  "models": [
    {
      "title": "Look2Eye GPT-4o",
      "provider": "openai",
      "model": "openai/gpt-4o",
      "apiBase": "https://api.look2eye.com/v1",
      "apiKey": "<你的 LOOK2EYE_API_KEY>"
    },
    {
      "title": "Look2Eye Claude Sonnet",
      "provider": "openai",
      "model": "anthropic/claude-sonnet-4.6",
      "apiBase": "https://api.look2eye.com/v1",
      "apiKey": "<你的 LOOK2EYE_API_KEY>"
    }
  ]
}
```

## Aider

[Aider](https://aider.chat)  是一款命令行 AI 配对编程工具。

```bash filename="~/.zshrc"
export OPENAI_API_KEY=<你的 LOOK2EYE_API_KEY>
export OPENAI_API_BASE=https://api.look2eye.com/v1
```

```bash
aider --model openai/gpt-4o
```

## BoltAI (macOS)

[BoltAI](https://boltai.com)  是 macOS 原生的 AI 助手应用。

1.  打开 BoltAI → **Preferences** → **Providers**
2.  添加 **Custom OpenAI**
3.  填写 Base URL: `https://api.look2eye.com/v1`
4.  填写 API Key

## TypingMind

[TypingMind](https://typingmind.com)  是一款 AI 聊天界面工具。

1.  进入 **Settings** → **Custom Endpoint**
2.  API Endpoint: `https://api.look2eye.com/v1`
3.  API Key: 你的 Look2Eye API Key

## ChatBox

[ChatBox](https://chatboxai.app)  是一款跨平台的 AI 桌面客户端。

1.  打开 ChatBox → **设置** → **AI 提供商**
2.  选择 **OpenAI API 兼容**
3.  API 域名: `https://api.look2eye.com`
4.  API Key: 你的 Look2Eye API Key

## 自定义集成

对于其他未列出的工具，一般遵循以下步骤：

1.  找到工具的 API 配置设置
2.  将 API Base URL 设置为 `https://api.look2eye.com/v1`
3.  将 API Key 设置为你的 Look2Eye Key
4.  模型名称使用 `provider/model-name` 格式

> ℹ️ 如果你成功在某个工具中配置了 Look2Eye，欢迎提交 PR 补充到本文档： GitHub 仓库
