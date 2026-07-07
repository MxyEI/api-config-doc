---
title: "安装 Claude Code"
description: "安装 Claude Code 并配置 Look2Eye 作为模型 provider：跨平台安装步骤、鉴权、常见问题排查"
---


Claude Code 是一个由 AI 驱动的编码助手，理解你的整个代码库，可以跨多个文件和工具工作。可在终端、IDE、桌面应用和浏览器中使用。

## 前置要求

-   [Look2Eye API Key](https://api.look2eye.com/console/api-keys) （注册即可获取，无需 Claude 订阅）

## 终端 CLI

功能完整的 CLI，用于直接在终端中使用 Claude Code。


### **原生安装（推荐）**

**macOS / Linux / WSL：**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell：**

前置准备命令
```powershell
#以管理员身份打开 PowerShell，执行以下任一命令
# 允许当前用户运行本地脚本（最安全）
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 或者（若上面不行）允许所有脚本（谨慎使用）
Set-ExecutionPolicy -ExecutionPolicy Unrestricted
```

```powershell
irm https://claude.ai/install.ps1 | iex
```

**Windows CMD：**

```bash
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

> ℹ️ Windows 需要先安装 Git for Windows 。原生安装会自动在后台更新。

**Homebrew**

```bash
brew install --cask claude-code
```

> ⚠️ Homebrew 安装不会自动更新。需定期运行 brew upgrade claude-code 获取最新版本。

**WinGet**

```powershell
winget install Anthropic.ClaudeCode
```

> ⚠️ WinGet 安装不会自动更新。需定期运行 winget upgrade Anthropic.ClaudeCode 获取最新版本。

安装完成后，请先完成 [配置模型供应商](model-provider.md) 再启动使用。

## VS Code / Cursor

在编辑器中直接提供内联差异、@-提及、计划审查和对话历史。

-   [为 VS Code 安装](vscode:extension/anthropic.claude-code)
-   [为 Cursor 安装](cursor:extension/anthropic.claude-code)

或在扩展视图中搜索 **“Claude Code”**（`Cmd+Shift+X` / `Ctrl+Shift+X`）。安装后，打开命令面板（`Cmd+Shift+P` / `Ctrl+Shift+P`），输入 “Claude Code”，选择 **在新标签页中打开**。


### npm 安装 claude code cli

#### mac
```
#如果是小白电脑，需要先执行权限命令，会提示输入电脑开机密码(密码不显示，按 enter 确认)
sudo chown -R $(whoami) /usr/local/lib/node_modules
sudo chown -R $(whoami) /usr/local/bin
sudo chown -R $(whoami) /usr/local/share

npm install -g @anthropic-ai/claude-code
```

#### windows
```
npm install -g @anthropic-ai/claude-code
```

电脑小白如果遇到提示 npm 权限不足，需要赋予权限
```powershell
# 允许当前用户运行本地脚本（最安全）
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

npm cache clean --force

npm cache verify

```

## JetBrains IDE

支持 IntelliJ IDEA、PyCharm、WebStorm 等，具有交互式差异查看和选择上下文共享。

从 JetBrains Marketplace 安装 [Claude Code 插件](https://plugins.jetbrains.com/plugin/27310-claude-code-beta-) ，然后重启 IDE。

## 验证安装

```bash
claude --version
# 正常输出版本号即表示安装成功
```

## 更新与卸载

```bash
# 原生安装自动更新，其他方式手动更新：
brew upgrade claude-code          # Homebrew
winget upgrade Anthropic.ClaudeCode  # WinGet

# 卸载
brew uninstall claude-code   # Homebrew
```

## 下一步

-   [配置模型供应商](model-provider.md) — 使用 Look2Eye 作为 API 提供商
-   [CCometixLine 状态栏](contextline.md) — 实时显示 Git 状态、模型、上下文用量
-   [配置 Skills](skills.md) — 扩展 Claude Code 能力
