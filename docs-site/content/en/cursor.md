---
title: "Cursor Compatibility Notice"
description: "Cursor has restricted third-party API providers, making inline completion, Agent mode, and other features unavailable with custom models. We recommend Claude Code or Codex CLI with CC Switch to connect to Look2Eye instead."
---


# Cursor Compatibility Notice


> 🚫 **Cursor has restricted third-party API providers**
> 
> Recent versions of Cursor have introduced strict limitations on custom API providers, resulting in the following incompatibilities when using Look2Eye:
> 
> 
> - **Inline completion (Tab completion) is completely unavailable** — Cursor’s Tab completion is hardcoded to use official models and cannot be replaced
> - **Agent mode is unavailable** — Background Agent does not support third-party API providers
> - **Auto model selection is broken** — Auto mode bypasses custom configuration and falls back to official models
> - **Cursor Pro paywall** — Even with a successful configuration, free-tier users cannot use custom models
> 
> 
> Given these limitations, **Cursor is not a suitable tool for connecting to Look2Eye at this time**.


## Recommended Alternatives


The following tools have full support for Look2Eye with no feature restrictions:

  - [Claude Code + CC Switch](/en/claude-code/)
  - [Codex CLI + CC Switch](/en/codex/)

## Keep Using Cursor as Your Editor


If you’re used to Cursor’s editing experience and don’t want to switch editors, you can run Claude Code or Codex CLI in **Cursor’s built-in terminal** — Cursor stays as your editor, AI power comes from Look2Eye, no conflict.


Open Cursor’s built-in terminal (<code>Ctrl+`</code>), then use as normal:


```text
# Using Claude Code
claude "refactor this function"

# Using Codex CLI
codex "refactor this function"
```


Claude Code and Codex CLI read the current directory’s code and complete AI coding tasks directly in the terminal, syncing in real time with the files you have open in Cursor.


## Why Doesn’t Cursor Work Properly?


### Inline Completion Is Locked


Cursor’s Tab completion is one of its core features, but it is **hardcoded to use Cursor’s official models** and does not read any custom API configuration. Even if you correctly configure Look2Eye’s Base URL and API Key, Tab completion will still route through Cursor’s official channel.


### Agent Mode Doesn’t Support Third Parties


Cursor’s Background Agent is architecturally tied to the official API. Third-party providers cannot be plugged in.


### Auto Mode Overrides Custom Configuration


Cursor’s Auto mode automatically selects the “best” model, but that selection logic prioritizes official models and will bypass any custom Base URL you’ve entered.


### Free Tier Cannot Use Custom Models


Even with a Cursor Pro subscription, support for custom API providers has been steadily tightening. Cursor’s business model depends on official model consumption — third-party integration is not a design goal.
