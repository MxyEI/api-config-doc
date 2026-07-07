---
title: "OpenClaw"
description: "OpenClaw 客户端接入 Look2Eye 的配置指南"
---


[OpenClaw](https://openclaw.ai)  是一款开源的本地 AI 助手，通过 WhatsApp、Telegram、Slack 等消息应用与你交互，能执行实际操作 — 管理邮件、日历、航班值机、浏览网页等。它完全在本地运行，数据不离开你的设备。

## 为什么搭配 Look2Eye？

-   **全球顶级模型统一调用** — 一个 API Key 访问 Claude、GPT、Gemini、Qwen、豆包等所有主流模型
-   **灵活的 Agent 策略** — 不同 Agent 分配不同模型，主力用 Sonnet、推理用 Opus、轻量用 Haiku
-   **99.9% SLA** — 多节点冗余，自动故障切换
-   **成本可控** — 统一计费面板，实时监控 Token 消耗

> ⚠️ OpenClaw 作为 Agentic AI 助手，单次任务的 Token 消耗较大（通常 10K-100K+ tokens）。建议根据任务复杂度选择模型，避免不必要的成本。本文提供三种配置方案供参考。

## 安装

```bash filename="macOS / Linux"
curl -sSL https://openclaw.ai/install.sh | bash
```

```powershell filename="Windows (PowerShell)"
& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1)))
```

## 快速开始

### 1\. 获取 API Key

前往 [Look2Eye 控制台](https://api.look2eye.com/keys)  创建 API Key。

### 2\. 运行配置向导

OpenClaw 提供交互式向导，输入以下命令即可快速完成配置：

```bash
openclaw onboard
```

在向导中选择 **Custom Provider**，填入以下信息：

| 配置项 | 值 |
| --- | --- |
| **Provider Type** | `anthropic-messages` |
| **Base URL** | `https://api.api.look2eye.com/anthropic` |
| **API Key** | 你的 Look2Eye API Key |
| **Model** | `anthropic/claude-sonnet-4.6` |

### 3\. 启动验证

```bash
openclaw start
```

向 OpenClaw 发送一条消息测试连通性。如果收到正常回复，配置成功。

> ℹ️ 向导会自动生成 openclaw.json 配置文件。如果你需要更细粒度的控制，请参考下方的完整配置。

## 完整配置

OpenClaw 通过 `~/.openclaw/openclaw.json` 管理所有配置（支持 JSON5 格式，可写注释）。

### Provider 配置

Provider 定义在 `models.providers` 下，每个 Provider 需要指定 API 协议类型、地址和密钥：

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

> ℹ️ apiKey 支持 `${ENV_VAR}` 语法引用环境变量，避免明文写入配置文件。三种协议对应不同模型系列：Claude 使用 look2eye-anthropic（anthropic-messages），OpenAI 使用 look2eye-openai（openai-responses），Gemini 使用 look2eye-gemini（google-generative-ai），其余模型可通过 look2eye-openai 接入。

### Models 配置

模型定义在对应 Provider 的 `models` 数组中。我们提供三套方案，根据你的需求选择：


**最强配置**

**全 Claude 阵容** — 追求最强能力，适合高要求场景。

```json filename="openclaw.json — models.providers"
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

| 模型 | 角色定位 | 适用场景 |
| --- | --- | --- |
| `anthropic/claude-sonnet-4.6` | 主力模型 | 日常对话、任务执行、代码生成 |
| `anthropic/claude-opus-4.6` | 深度推理 | 复杂分析、长链推理、研究任务 |
| `anthropic/claude-haiku-4.5` | 快速响应 | 简单查询、快速回复、轻量任务 |

> ℹ️ Claude 思考模式需要按模型版本配置。Sonnet 4.5 使用 `enabled + budget_tokens`，Sonnet 4.6 / Opus 4.6 推荐 `adaptive`。完整规则见 [Anthropic Messages API 的 Claude 思考模式](https://api.look2eye.com/zh/api/anthropic/messages#claude-思考模式)。

**平衡组合**

**OpenAI Codex 组合** — 代码能力突出，通用任务均衡。

```json filename="openclaw.json — models.providers"
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

| 模型 | 角色定位 | 适用场景 |
| --- | --- | --- |
| `openai/gpt-5.3-codex` | 主力 + 推理 | 日常对话、复杂任务、代码重构 |
| `openai/gpt-5.1-codex-mini` | 快速响应 | 轻量任务、代码补全、快速问答 |

> ℹ️ OpenAI 模型通过 look2eye-openai Provider 接入，使用 openai-responses 协议。

**最具性价比**

**国产模型性价比之选** — Token 单价低，适合高频日常使用。

```json filename="openclaw.json — models.providers"
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
            "name": "豆包 Seed 2.0 Code",
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

| 模型 | 角色定位 | 适用场景 |
| --- | --- | --- |
| `bailian/qwen3.5-plus` | 主力 + 推理 | 日常对话、通用任务、中文优化 |
| `volcengine/doubao-seed-2.0-code` | 代码 + 快速 | 代码生成、调试、快速回复 |

### Agents 配置

OpenClaw 通过 `agents.defaults` 设置全局默认，通过 `agents.list` 数组定义不同 Agent，每个 Agent 可覆盖默认配置：

```json filename="openclaw.json — agents 部分"
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

| Agent | 模型 | 用途 |
| --- | --- | --- |
| **main** | `claude-sonnet-4.6`（继承 defaults） | 默认 Agent，日常所有任务 |
| **research** | `claude-opus-4.6` | 深度研究、复杂推理、长文分析 |
| **quick** | `claude-haiku-4.5` | 简单问答、快速响应、低成本 |

> ℹ️ 模型引用格式为 provider名/model-id（如 look2eye-anthropic/anthropic/claude-sonnet-4.6）。defaults 中的 models 字段定义模型别名，可在对话中用 /model opus 快速切换。list 中的 Agent 会继承 defaults 的所有配置，只需覆盖需要变更的字段。

## 完整配置示例

以下是一份完整的 `openclaw.json`，整合了 Provider、Models 和 Agents 配置（最强配置方案）：

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

## 使用场景

配置完成后，通过消息应用向 OpenClaw 发送指令：

-   **邮件管理** — “帮我整理今天未读的邮件，按优先级排序”
-   **日程安排** — “明天下午 3 点安排一个团队会议”
-   **信息检索** — “搜索最近关于 AI Agent 的技术文章，总结要点”
-   **代码辅助** — “帮我 review 这段 Python 代码，检查安全问题”
-   **工作流自动化** — “每天早上 9 点发送团队日报到 Slack #general 频道”

## 故障排除

**无法连接 Look2Eye**

确认 `baseUrl` 配置正确：

-   Anthropic 协议：`https://api.api.look2eye.com/anthropic`
-   OpenAI-Response 协议：`https://api.api.look2eye.com/v1`
-   Gemini 协议：`https://api.api.look2eye.com/gemini`

**模型不存在**

确认模型 ID 格式正确。在 `models.providers` 中定义模型时，`id` 使用 Look2Eye 返回的完整 ID（如 `anthropic/claude-sonnet-4.6`）。在 `agents` 中引用模型时需要加 Provider 名前缀：`look2eye-anthropic/anthropic/claude-sonnet-4.6`。

**Token 消耗过高**

OpenClaw 单次任务消耗较大，建议：

1.  日常任务使用 `claude-haiku-4.5` 或性价比模型
2.  仅在复杂任务时切换到 `research` Agent（使用 `claude-opus-4.6`）
3.  在 [Look2Eye 控制台](https://api.look2eye.com/console/analytics)  监控用量

**如何快速切换模型**

在对话中使用别名切换：`/model opus`、`/model sonnet`、`/model haiku`（需要在 `agents.defaults.models` 中配置别名）。
