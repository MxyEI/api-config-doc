---
title: "Install Claude Code"
description: "Claude Code installation guide supporting Terminal CLI, VS Code, desktop app, JetBrains, and browser"
---


# Install Claude Code


Claude Code is an AI-powered coding assistant that understands your entire codebase and can work across multiple files and tools. It is available in the terminal, IDEs, desktop apps, and browsers.


## Prerequisites


- [Look2Eye API Key](https://api.look2eye.com/console/api-keys) (sign up to get one — no Claude subscription required)


## Terminal CLI


A fully featured CLI for using Claude Code directly in your terminal.


**Native Install (Recommended)**

**macOS / Linux / WSL:**


```text
curl -fsSL https://claude.ai/install.sh | bash
```


**Windows PowerShell:**


```text
irm https://claude.ai/install.ps1 | iex
```


**Windows CMD:**


```text
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```


> ℹ️ Windows requires [Git for Windows](https://git-scm.com/downloads/win) to be installed first. The native install will auto-update in the background.

**Homebrew**

```text
brew install --cask claude-code
```


> ⚠️ The Homebrew install does not auto-update. Run `brew upgrade claude-code` periodically to get the latest version.

**WinGet**

```text
winget install Anthropic.ClaudeCode
```


> ⚠️ The WinGet install does not auto-update. Run `winget upgrade Anthropic.ClaudeCode` periodically to get the latest version.


After installation, complete the [Model Provider Configuration](/en/claude-code/model-provider/) before starting.


## VS Code / Cursor


Provides inline diffs, @-mentions, plan review, and conversation history directly in your editor.


- [Install for VS Code](vscode:extension/anthropic.claude-code)
- [Install for Cursor](cursor:extension/anthropic.claude-code)


Or search for **“Claude Code”** in the Extensions view (`Cmd+Shift+X` / `Ctrl+Shift+X`). After installation, open the Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`), type “Claude Code”, and select **Open in New Tab**.


## JetBrains IDE


Supports IntelliJ IDEA, PyCharm, WebStorm, and more, with interactive diff viewing and selection context sharing.


Install the [Claude Code plugin](https://plugins.jetbrains.com/plugin/27310-claude-code-beta-) from the JetBrains Marketplace, then restart the IDE.


## Verify Installation


```text
claude --version
# A version number output indicates successful installation
```


## Update & Uninstall


```text
# Native install auto-updates; for other methods, update manually:
brew upgrade claude-code          # Homebrew
winget upgrade Anthropic.ClaudeCode  # WinGet

# Uninstall
brew uninstall claude-code   # Homebrew
```


## Next Steps


- [Configure Model Provider](/en/claude-code/model-provider/) — Use Look2Eye as the API provider
- [CCometixLine Status Bar](/en/claude-code/contextline/) — Real-time display of Git status, model, and context usage
- [Configure Skills](/en/claude-code/skills/) — Extend Claude Code capabilities
