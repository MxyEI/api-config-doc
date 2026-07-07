---
title: "OpenCode 配置"
description: "OpenCode 接入 Look2Eye 作为模型 provider 的配置步骤"
---


# OpenCode 配置

[OpenCode](https://github.com/opencode-ai/opencode)  是一款开源的终端 AI 编码工具，类似 Claude Code 的开源替代品。通过 Look2Eye 接入，可以使用任意模型。

## 配置步骤

### 1\. 安装 OpenCode

```bash
# macOS / Linux
curl -fsSL https://opencode.ai/install | bash

# 或使用 Go 安装
go install github.com/opencode-ai/opencode@latest
```

![安装 OpenCode](/assets/opencode/01-安装-opencode.webp)

### 2\. 配置环境变量

OpenCode 支持多种 Provider 配置。推荐使用 OpenAI 兼容模式：

```bash filename="~/.zshrc"
# OpenAI 兼容模式
export OPENAI_API_KEY=<你的 LOOK2EYE_API_KEY>
export OPENAI_BASE_URL=https://api.api.look2eye.com/v1
```

如果主要使用 Claude 模型，也可以配置 Anthropic 模式：

```bash filename="~/.zshrc"
export ANTHROPIC_API_KEY=<你的 LOOK2EYE_API_KEY>
export ANTHROPIC_BASE_URL=https://api.api.look2eye.com/anthropic
```

### 3\. 配置文件

也可以通过 OpenCode 的配置文件设置：

```toml filename="~/.config/opencode/config.toml"
[providers.look2eye]
api_key = "<你的 LOOK2EYE_API_KEY>"
base_url = "https://api.api.look2eye.com/v1"

[models.default]
provider = "look2eye"
model = "anthropic/claude-sonnet-4.6"
```

### 4\. 验证

```bash
opencode "Hello, 你好吗？"
```

![运行效果](/assets/opencode/02-运行效果.webp)

## 推荐模型

推荐模型请参考 [模型广场](https://api.look2eye.com/models) 。

> ℹ️ OpenCode 的具体配置方式可能随版本更新变化，请参考 [OpenCode 官方文档](https://github.com/opencode-ai/opencode) 。
