---
title: "Gemini CLI 配置"
description: "Gemini CLI 接入 Look2Eye：安装、鉴权与模型 provider 配置"
---


# Gemini CLI 配置

[Gemini CLI](https://github.com/google-gemini/gemini-cli)  是 Google 推出的 Gemini 模型命令行工具。通过 Look2Eye，你可以使用 Gemini 协议的同时获得更丰富的模型选择。

## 配置步骤

### 1\. 安装 Gemini CLI

```bash
npm install -g @google/gemini-cli
```

![安装 Gemini CLI](/assets/gemini-cli/01-安装-gemini-cli.webp)

### 2\. 配置 Look2Eye

Gemini CLI 使用 Gemini 原生协议。通过设置配置文件指向 Look2Eye：

```json filename="~/.gemini/settings.json"
{
  "apiKey": "<你的 LOOK2EYE_API_KEY>",
  "baseUrl": "https://api.look2eye.com"
}
```

或使用环境变量：

```bash filename="~/.zshrc"
export GEMINI_API_KEY=<你的 LOOK2EYE_API_KEY>
```

> ⚠️ Gemini CLI 的 base URL 配置方式可能随版本变化。如果上述方式不生效，请参考 Gemini CLI 最新文档。

### 3\. 验证

```bash
gemini "你好，介绍一下自己"
```

![验证 Gemini CLI](/assets/gemini-cli/02-验证-gemini-cli.webp)

## 可用模型

推荐模型请参考 [Look2Eye 可用渠道](https://api.look2eye.com/available-channels) 。

## 使用场景

-   **代码生成和审查** — Gemini 模型擅长代码理解
-   **长文件分析** — 利用 1M token 上下文窗口
-   **多模态任务** — 分析图片、PDF 等文件

> ℹ️ 通过 Look2Eye 使用 Gemini CLI，你还可以获得故障回退和路由优化的好处。详见[高级功能](https://api.look2eye.com/zh/develop/advanced/fallback)。
