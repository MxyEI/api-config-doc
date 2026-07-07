---
title: "配置模型供应商"
description: "使用 CC Switch 配置 Look2Eye API Key 和请求地址，为 Codex 本地客户端接入 Look2Eye。"
---


# 配置模型供应商

推荐先用[平台](https://api.look2eye.com/keys)的一键配置脚本 配好 Look2Eye 供应商和 API Key。直接开启 WebSocket，让 Codex 长时间编码会话更流畅。


## 使用平台的一键配置脚本(推荐)
![平台一键配置脚本](/assets/codex/01-codex-一键配置脚本.png)


## 使用 CC Switch 图形化配置

[CC Switch](https://github.com/farion1231/cc-switch) 是开源的供应商管理工具，适合偏好图形界面的用户。

### 1\. 安装 CC Switch

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

### 2\. 添加 Look2Eye 供应商

### 步骤一：新增供应商

切换到顶部 **Codex** 标签页，点击右上角 **+** 按钮。

![CC Switch Codex 标签页](/assets/codex/01-cc-switch-codex-标签页.webp)

### 步骤二：填写配置

按下表填写，点击 **\+ 添加** 完成。

![CC Switch Codex 供应商配置](/assets/codex/02-cc-switch-codex-供应商配置.webp)

| 配置项 | 值 | 说明 |
| --- | --- | --- |
| ❶ 供应商名称 | `look2eye` | 推荐使用，后续 WebSocket 配置更容易对应 |
| ❷ 官网链接 | `https://api.look2eye.com` | 供应商官网 |
| ❸ API Key | 你的 Look2Eye API Key | 在 [api.look2eye.com/keys](https://api.look2eye.com/keys) 获取 |
| ❹ 请求地址 | `https://api.api.look2eye.com/v1` | 末尾不要加斜杠 |
| ❺ API 格式 | `OpenAI Compatible` | 选择 OpenAI 兼容格式 |
| ❻ 写入通用配置 | ✅ 勾选 | 写入全局配置，所有项目生效 |

> ℹ️ CC Switch 自动写入配置文件，无需手动编辑任何文件。

### 步骤三：启用供应商

添加完成后回到列表，选中 `look2eye`，点击**使用**按钮，看到「切换成功」提示即完成。确认 **写入通用配置** 已勾选，配置会自动写入 `config.toml`。

![CC Switch 写入通用配置](/assets/codex/03-cc-switch-写入通用配置.webp)

## 验证配置

```text
codex "hello"
```

![Codex CLI 运行效果](/assets/codex/04-codex-cli-运行效果.webp)

正常返回 AI 响应即表示配置成功。

## 下一步

-   [开启 WebSocket（推荐）](/zh/codex/websocket/) — 补齐 Responses 协议格式和 WebSocket 长连接配置，让长时间编码会话更流畅

## 指定模型

```text
codex --model <model-id> "重构这个函数"
```

> ⚠️ Codex CLI 需要使用 **Responses 协议格式**（`wire_api = "responses"`）来接收编码任务中的流式响应和工具调用，并非所有模型都支持此格式。选择模型时，请在 [Look2Eye 模型广场](https://api.look2eye.com/models)  确认该模型支持 **Responses** 协议，否则会报错。

推荐模型请参考 [Look2Eye 模型广场](https://api.look2eye.com/models) 。

## 故障排除

**Q: 提示 “Authentication error”**

确认 API Key 已正确填写，并检查请求地址末尾无斜杠。

**Q: 连接超时**

确认请求地址为 `https://api.api.look2eye.com/v1`，末尾不带斜杠。
