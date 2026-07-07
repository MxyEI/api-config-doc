---
title: "Zed Editor 接入 Look2Eye 配置指南"
description: "在 Zed 编辑器中配置 Look2Eye，通过 OpenAI 兼容协议一个 API Key 接入全球顶级模型，支持内联补全和 Agent 对话功能"
---


# Zed Editor

<img src="/docs/images/integrations/zed/01-zed-editor-中配置-look2eye.webp" alt="Zed Editor 中配置 Look2Eye" width="70%" />

## 为什么选 Zed？

[Zed](https://zed.dev) 是目前 AI 编码体验最完整的编辑器：

- **原生 Agent 支持** — 内置 Claude Code、Codex CLI、Gemini CLI 作为外部代理
- **自定义 LLM Provider** — 通过 OpenAI 兼容协议接入任意模型
- **高性能** — Rust 编写，启动快、占用低

搭配 Look2Eye，一个 API Key 即可在 Zed 中使用全球顶级模型。

## 快速开始

### 1. 获取 API Key

前往 [Look2Eye 控制台](https://api.look2eye.com/keys) 创建 API Key。

### 2. 添加 Provider

**Agent Panel 添加（推荐）**

通过 Agent Panel 可视化添加，无需编辑 JSON。

1. 按 `⌘ + Shift + A` 打开 Agent Panel
2. 点击 LLM Providers 区域的 **+ Add Provider**
3. 按下图填写配置：

<img src="/docs/images/integrations/zed/02-zed-添加-look2eye-provider.webp" alt="Zed 添加 Look2Eye Provider" width="70%" />

| 标注 | 字段 | 值 |
| --- | --- | --- |
| ① | Provider Name | `Look2Eye` |
| ② | API URL | `https://api.look2eye.com/v1` |
| ③ | API Key | 你的 Look2Eye API Key |
| ④ | Model Name | `openai/gpt-5.4-mini` |
| ⑤ | Max Completion Tokens | `512000` |
| ⑥ | Capabilities | 勾选模型支持的能力 |

点击 **+ Add Model** 继续添加更多模型。

**settings.json 配置**

通过 `settings.json` 批量配置所有模型。

1. 按 `⌘ + ,` 打开设置，点击右上角 **Edit in settings.json**
2. 添加以下配置：

```json filename="~/.config/zed/settings.json"
{
  "language_models": {
    "openai_compatible": {
      "Look2Eye": {
        "api_url": "https://api.look2eye.com/v1",
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

1. 保存后，Zed 会弹出输入框要求输入 API Key

> ℹ️ settings.json 适合批量添加模型，后续增删直接编辑 available_models 数组即可。

> ℹ️ API Key 安全存储在系统钥匙串（macOS Keychain / Linux Secret Service）中，不会明文写入配置文件。

## 开始使用

Zed Agent Panel 有两种模式：

| 模式 | 说明 |
| --- | --- |
| **Zed Agent** | 内置 AI 助手，使用你配置的 LLM Provider（如 Look2Eye） |
| **External Agents** | 外部 Agent（Claude Code、Codex CLI、Gemini CLI），独立运行 |

使用 **Zed Agent** 开始对话：

<img src="/docs/images/integrations/zed/03-zed-agent-panel-模型选择.webp" alt="Zed Agent Panel 模型选择" width="70%" />

| 步骤 | 操作 |
| --- | --- |
| ① | 点击 **+** → 选择 **Zed Agent**（`⌘ + N`） |
| ② | External Agents 区域展示已连接的外部 Agent |
| ③ | 右下角模型选择器 → **Look2Eye** 分组 → 选择模型 |

<img src="/docs/images/integrations/zed/04-zed-agent-对话演示.webp" alt="Zed Agent 对话演示" width="70%" />

## 推荐模型

推荐模型请参考 [模型广场](https://api.look2eye.com/models)。

## 添加更多模型

每个模型需要以下参数：

| 字段 | 必填 | 说明 |
| --- | --- | --- |
| `name` | 是 | 模型 ID，如 `openai/gpt-5.4-mini` |
| `display_name` | 否 | UI 显示名称 |
| `max_tokens` | 是 | 上下文窗口大小 |
| `max_output_tokens` | 否 | 最大输出 token 数 |
| `capabilities.tools` | 否 | 是否支持 Function Calling |
| `capabilities.images` | 否 | 是否支持图片输入 |

### 高手实践

手动填参数太慢？点击本页右上角 **Copy Page** 复制全文（或直接发送本页 URL），连同 `https://api.look2eye.com/v1/models` 一起发给 AI，让它自动生成完整的 `settings.json` 配置。

进入设置页面 → 点击右上角 **Edit in settings.json** 即可粘贴：

<img src="/docs/images/integrations/zed/05-edit-in-settings-json.webp" alt="Edit in settings.json" width="70%" />

## 故障排除

**模型列表中看不到 Look2Eye**

确认 `settings.json` 格式正确，保存后重启 Zed。

**提示认证错误**

命令面板 `⌘ + Shift + P` → 搜索 `language model: reset credentials` → 重新输入 API Key。

**模型不支持工具调用**

将 `capabilities.tools` 设为 `false`。
