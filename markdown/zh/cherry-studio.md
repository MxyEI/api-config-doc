---
title: "Cherry Studio 配置"
description: "在 Cherry Studio 中配置 Look2Eye 多协议模型服务，并启用聊天、视觉和图片生成能力。"
---


# Cherry Studio 配置

[Cherry Studio](https://cherry-ai.com)  是一款跨平台的 AI 桌面客户端（支持 Windows、macOS、Linux），支持多模型对话、知识库和工作流，是目前功能最丰富的开源 AI 客户端之一。

通过配置 Look2Eye 作为服务商，你可以在 Cherry Studio 中使用 GPT、Claude、Gemini、DeepSeek 等全球顶级模型，只需一个 API Key。

## 四种协议说明

Cherry Studio 支持通过以下四种协议接入 Look2Eye：

**OpenAI Chat** — 基于 `/v1/chat/completions`，适用于 GPT 系列模型，如 `openai/gpt-4.1`、`openai/gpt-5.3-chat`。

**OpenAI Response** — 基于 `/v1/responses`，适用于 GPT 系列模型，如 `openai/gpt-4.1`、`openai/gpt-5.4-mini`。

**Claude** — 基于 `/anthropic/v1/messages`，适用于 Claude 系列模型，如 `anthropic/claude-sonnet-4.6`、`anthropic/claude-opus-4.6`。

**Gemini** — 基于 `/gemini/v1beta/models`，适用于 Gemini 系列模型，如 `google/gemini-3.1-pro-preview`、`google/gemini-3.1-flash-lite-preview`。

## 前提条件

-   已注册 Look2Eye 账号并获取 API Key（[前往获取](https://api.look2eye.com/keys) ）
-   已安装 Cherry Studio（[下载地址](https://cherry-ai.com) ）

## 配置步骤

### 第 1 步：打开设置

启动 Cherry Studio，点击左下角的 **设置** 图标。

![打开 Cherry Studio 设置](../assets/cherry-studio/01-打开-cherry-studio-设置.webp)

### 第 2 步：添加模型提供商

进入左侧 **模型服务**，滚动到底部，点击 **\+ 添加**。在弹出的对话框中填写提供商名称，并选择对应的提供商类型。

**OpenAI Chat**

提供商类型选择 `OpenAI`，点击确定。

![添加 OpenAI Chat 提供商](../assets/cherry-studio/02-添加-openai-chat-提供商.webp)

**OpenAI Response**

提供商类型选择 `OpenAI`（后续在配置页开启 Response 模式），点击确定。

![添加 OpenAI Response 提供商](../assets/cherry-studio/03-添加-openai-response-提供商.webp)

**Claude**

提供商类型选择 `Anthropic`，点击确定。

![添加 Claude 提供商](../assets/cherry-studio/04-添加-claude-提供商.webp)

**Gemini**

提供商类型选择 `Gemini`，点击确定。

![添加 Gemini 提供商](../assets/cherry-studio/05-添加-gemini-提供商.webp)

### 第 3 步：填写 API 配置

在对应提供商的配置页中填写 API 密钥和 API 地址。

**OpenAI Chat**

| 配置项 | 值 |
| --- | --- |
| **API 密钥** | 你的 Look2Eye API Key |
| **API 地址** | `https://api.look2eye.com` |

![OpenAI Chat 配置](../assets/cherry-studio/06-openai-chat-配置.webp)

**OpenAI Response**

| 配置项 | 值 |
| --- | --- |
| **API 密钥** | 你的 Look2Eye API Key |
| **API 地址** | `https://api.look2eye.com` |

![OpenAI Response 配置](../assets/cherry-studio/07-openai-response-配置.webp)

**Claude**

| 配置项 | 值 |
| --- | --- |
| **API 密钥** | 你的 Look2Eye API Key |
| **API 地址** | `https://api.look2eye.com` |

![Claude 配置](../assets/cherry-studio/08-claude-配置.webp)

**Gemini**

| 配置项 | 值 |
| --- | --- |
| **API 密钥** | 你的 Look2Eye API Key |
| **API 地址** | `https://api.look2eye.com` |

![Gemini 配置](../assets/cherry-studio/09-gemini-配置.webp)

> ⚠️ 确认页面右上角的开关处于 **开启（ON）** 状态，否则该提供商不会出现在模型选择器中。

### 第 4 步：添加模型

点击模型区域的 **管理** 按钮自动拉取模型列表，点击模型右侧的 **+** 添加到启用列表。

**OpenAI Chat**

![OpenAI Chat 模型列表](../assets/cherry-studio/10-openai-chat-模型列表.webp)

**OpenAI Response**

![OpenAI Response 模型列表](../assets/cherry-studio/11-openai-response-模型列表.webp)

**Claude**

![Claude 模型列表](../assets/cherry-studio/12-claude-模型列表.webp)

**Gemini**

![Gemini 模型列表](../assets/cherry-studio/13-gemini-模型列表.webp)

### 第 5 步：验证配置

点击 **检测** 按钮，选择任意模型进行测试，显示检测通过即配置成功。

**OpenAI Chat**

![OpenAI Chat 验证](../assets/cherry-studio/14-openai-chat-验证.webp)

**OpenAI Response**

![OpenAI Response 验证](../assets/cherry-studio/15-openai-response-验证.webp)

**Claude**

![Claude 验证](../assets/cherry-studio/16-claude-验证.webp)

**Gemini**

![Gemini 验证](../assets/cherry-studio/17-gemini-验证.webp)

## 开始使用

回到主界面，点击对话顶部的模型选择器，在对应提供商分组下选择模型，即可开始对话。

![选择模型开始对话](../assets/cherry-studio/18-选择模型开始对话.webp)

## 图片生成

Cherry Studio 支持通过 Gemini 协议调用 Look2Eye 的图片生成模型，在对话中直接生成图片。

### 第 1 步：添加 Gemini 提供商

进入 **模型服务**，点击底部 **\+ 添加**。

![添加提供商](../assets/cherry-studio/19-添加提供商.webp)

在弹出的对话框中，提供商类型选择 **Gemini**，点击确定。

![选择 Gemini 类型](../assets/cherry-studio/20-选择-gemini-类型.webp)

### 第 2 步：配置并获取生图模型

API 地址填写 `https://api.look2eye.com/gemini`，点击 **获取模型列表**，添加以下生图模型：

-   `Google: Nano Banana Pro (Gemini 3 Pro Image Preview)`
-   `Google: Nano Banana (Gemini 2.5 Flash Image)`
-   `Google: Nano Banana 2 (Gemini 3.1 Flash Image Preview)`

![获取生图模型](../assets/cherry-studio/21-获取生图模型.webp)

### 第 3 步：编辑助手，配置生图参数

在主界面右键点击助手，选择 **编辑助手**。

![编辑助手](../assets/cherry-studio/22-编辑助手.webp)

在编辑页面中：

1.  **默认模型** 选择刚添加的生图模型
2.  点击 **\+ 添加参数**，添加以下两个自定义参数：

| 参数名 | 类型 | 值 |
| --- | --- | --- |
| `responseModalities` | JSON | `["IMAGE"]` |
| `imageConfig` | JSON | `{"aspectRatio": "1:1", "imageSize": "1K"}` |

`imageConfig` 中可以调整图片的宽高比和分辨率，如需 2K 图片，将 `imageSize` 改为 `"2K"`。

![配置生图参数](../assets/cherry-studio/23-配置生图参数.webp)

### 第 4 步：开始生图

保存配置后，在对话框中输入图片描述，即可生成图片。

![生图效果](../assets/cherry-studio/24-生图效果.webp)

## 常见问题

**Q: 点击「管理」后模型列表为空**

检查 API 地址是否填写正确（末尾不加斜杠），以及 API 密钥是否完整复制，无多余空格。

**Q: 检测时提示连接失败**

1.  确认 API Key 从 [Look2Eye 控制台](https://api.look2eye.com/keys)  完整复制，无多余空格
2.  确认 API 地址填写正确
3.  确认网络连接正常

**Q: 提供商不出现在模型选择器中**

检查配置页右上角的开关是否已开启。
