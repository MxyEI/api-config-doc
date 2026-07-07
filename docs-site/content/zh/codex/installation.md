---
title: "安装 Codex CLI"
description: "安装 OpenAI Codex CLI，并确认本机可以运行 codex 命令。"
---


# 安装 Codex CLI

Codex CLI 是 OpenAI 推出的 AI 编码命令行工具，可在终端中直接进行 AI 辅助编码。

> ℹ️ 如果你已经安装 Codex 本地客户端，并且终端中可以运行 `codex` 命令，可直接进入下一步配置模型供应商。

## 前置要求

-   [Look2Eye API Key](https://api.look2eye.com/keys) （注册即可获取）
-   [Node.js](https://nodejs.org) （建议 v18+）

## 安装

```text
npm install -g @openai/codex
```

![安装 Codex CLI](/assets/codex/01-安装-codex-cli.webp)

## 验证安装

```text
codex --version
# 正常输出版本号即表示安装成功
```


```
codex

进入后输入 /status
```
出现以下配置信息就是正确

![验证安装](/assets/codex/02-验证安装.webp)

> ℹ️ 如提示 `command not found`，请确认 Node.js 已正确安装（`node --version`），然后重新运行安装命令。

## 下一步

-   [配置模型供应商](/zh/codex/model-provider/) — 使用 CC Switch 管理 Look2Eye API Key 和请求地址
