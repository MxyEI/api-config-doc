---
title: "配置模型供应商"
description: "配置模型供应商：Look2Eye 文档页面，说明接口用途、请求方式、响应字段和接入注意事项。"
---


# 配置模型供应商

推荐使用[平台](https://api.look2eye.com/keys)的一键配置脚本 完成配置
或者使用 ccswitch —— 一款开源的供应商管理工具，可视化操作，无需手动编辑 JSON 或环境变量。

## 使用平台的一键配置脚本(推荐)



## 1\. 安装 CC Switch

### macOS

```text
brew install --cask cc-switch
```

或前往 [Releases](https://github.com/farion1231/cc-switch/releases)  下载 `.dmg` 手动安装。

### Windows

前往 [Releases](https://github.com/farion1231/cc-switch/releases)  下载 `.msi` 安装程序。

### Linux

```text
# Debian / Ubuntu
sudo dpkg -i CC-Switch-*.deb

# Fedora / RHEL
sudo rpm -i CC-Switch-*.rpm

# AppImage
chmod +x CC-Switch-*.AppImage && ./CC-Switch-*.AppImage
```

> ℹ️ 支持 macOS 12+、Windows 10+、Ubuntu 22.04+ / Debian 11+ / Fedora 34+

## 2\. 添加 Look2Eye 供应商

### 步骤一：新增供应商

打开 CC Switch，进入供应商管理页，点击右上角 **+** 按钮。

![CC Switch 添加供应商](/assets/claude-code/01-cc-switch-添加供应商.webp)

### 步骤二：填写配置

按下图标注填写，点击 **\+ 添加** 完成。

![CC Switch 供应商配置](/assets/claude-code/02-cc-switch-供应商配置.webp)

| 配置项 | 值 | 说明 |
| --- | --- | --- |
| ❶ 供应商名称 | `look2eye-claude` | 自定义，方便识别 |
| ❷ 官网链接 | `https://api.look2eye.com` | 供应商官网 |
| ❸ API Key | 你的 Look2Eye API Key | 在 [api.look2eye.com/keys](https://api.look2eye.com/keys) 获取 |
| ❹ 请求地址 | `https://api.api.look2eye.com/anthropic` | 末尾不要加斜杠 |
| ❺ API 格式 / 认证字段 | `Anthropic Messages (原生)` / `ANTHROPIC_AUTH_TOKEN（默认）` | 保持默认 |
| ❻ 模型配置 | 留空 | 留空使用默认 Claude 模型 |
| ❼ 选项 | 勾选「隐藏 AI 署名」和「Teammates 模式」 | 按需勾选 |
| ❽ 写入通用配置 | ✅ 勾选 | 写入全局配置，所有项目生效 |

> ℹ️ CC Switch 自动写入 `~/.claude/settings.json`，无需手动编辑任何文件。

### 步骤三：启用供应商

添加完成后回到列表，选中 `look2eye-claude`，点击**使用**按钮，看到「切换成功」提示即完成。

![CC Switch 启用供应商](/assets/claude-code/03-cc-switch-启用供应商.webp)

## 3\. 验证配置

进入项目目录，启动 Claude Code：

```text
cd your-project
claude
```

首次启动按 `Esc` 跳过登录。启动后注意顶部信息栏，确认显示 **API Usage Billing**（❶）表示已通过 Look2Eye 计费：

![Claude Code 启动界面](/assets/claude-code/04-claude-code-启动界面.webp)

以上信息确认无误，即配置成功。

## 4\. 使用其他模型

通过 Look2Eye，你可以在 Claude Code 中使用非 Claude 模型（如 Qwen、GLM、DeepSeek 等）。只需在模型广场筛选兼容模型，然后配置模型映射即可。

### 步骤一：筛选兼容模型

前往 [Look2Eye 模型广场](https://api.look2eye.com/models) ，在左侧 **API 协议** 中选择 **Anthropic**，筛选出支持 Anthropic 协议的模型。

![模型广场筛选 Anthropic 协议](/assets/claude-code/05-模型广场筛选-anthropic-协议.webp)

### 步骤二：复制模型名称

点击目标模型卡片，模型名称旁有 **复制按钮**，一键复制模型 ID（如 `bailian/qwen3.6-plus`）。

![一键复制模型名称](/assets/claude-code/06-一键复制模型名称.webp)

### 步骤三：配置模型映射

回到 CC Switch，在供应商配置中找到 **模型映射** 部分。将复制的模型名称填入对应的模型槽位，可前往 [Look2Eye 模型广场](https://api.look2eye.com/models)  浏览可用模型：

| 映射槽位 | 说明 |
| --- | --- |
| **主模型** | Claude Code 默认使用的模型 |
| **推理模型 (Thinking)** | 用于深度推理的模型 |
| **Haiku 默认模型** | 轻量级任务模型 |
| **Sonnet 默认模型** | 中等复杂度任务模型 |
| **Opus 默认模型** | 高复杂度任务模型 |

> ℹ️ Claude 思考模式的 API 参数取决于模型版本：Sonnet 4.5 使用 `enabled + budget_tokens`，Sonnet 4.6 / Opus 4.6 推荐 `adaptive`。完整规则见 [Anthropic Messages API 的 Claude 思考模式](https://api.look2eye.com/zh/api/anthropic/messages#claude-思考模式)。

> ℹ️ 如果供应商原生提供 Claude 系列模型，通常无需配置模型映射。仅在需要将请求映射到不同模型名称时填写。

## 故障排除

遇到问题时，在 Claude Code 终端中运行 `/status` 检查配置：

```text
/status
```

确认以下关键字段：

-   **❶ Anthropic base URL** 为 `https://api.api.look2eye.com/anthropic`
-   **❷ Model** 显示当前使用的模型

![Claude Code /status 输出](/assets/claude-code/07-claude-code-status-输出.webp)

**Q: 提示 “Authentication error”**

确认 `Anthropic base URL` 正确，并检查 API Key 是否有效。

**Q: 连接超时**

确认请求地址填写为 `https://api.api.look2eye.com/anthropic`，末尾不带斜杠。

**Q: 流式响应卡顿**

Look2Eye 已内置全球加速，通常为本地网络问题，检查本地连接后重试。
