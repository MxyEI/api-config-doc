---
title: "Configure Model Provider"
description: "Configure the Look2Eye API key and request URL in CC Switch for Codex local clients"
---


# Configure Model Provider


We recommend using the [platform](https://api.look2eye.com/keys)'s one-click configuration script to set up the Look2Eye provider and API key first. Then enable WebSocket for smoother long Codex coding sessions.


## Method 1: Use the Platform One-Click Script (Recommended)

![Platform one-click configuration script](/assets/claude-code/01-cc-一键配置脚本.webp)

Select **Codex CLI**, download the script, and run it.

Windows

```
Run the downloaded .bat script directly
```

macOS

```
Drag the .sh script into Terminal to run it. If permission is denied, run: chmod +x script.sh
```


## Method 2: Use CC Switch Visual Setup


[CC Switch](https://github.com/farion1231/cc-switch) is an open-source provider management tool for users who prefer a visual interface.


### 1. Install CC Switch


### macOS


```text
brew install --cask cc-switch
```


Or go to [Releases](https://github.com/farion1231/cc-switch/releases) to download the `.dmg` for manual installation.


### Windows


Go to [Releases](https://github.com/farion1231/cc-switch/releases) to download the `.msi` installer.


### Linux


```text
# Debian / Ubuntu
sudo dpkg -i CC-Switch-*.deb

# Fedora / RHEL
sudo rpm -i CC-Switch-*.rpm

# AppImage
chmod +x CC-Switch-*.AppImage && ./CC-Switch-*.AppImage
```


> ℹ️ Supports macOS 12+, Windows 10+, Ubuntu 22.04+ / Debian 11+ / Fedora 34+


### 2. Add Look2Eye Provider


### Step 1: Add a New Provider


Switch to the **Codex** tab at the top, then click the **+** button in the top-right corner.


![CC Switch add provider](/assets/codex/01-cc-switch-codex-标签页.webp)


### Step 2: Fill in the Configuration


Fill in the fields as shown below, then click **+ Add** to complete.


![CC Switch provider configuration](/assets/codex/02-cc-switch-codex-供应商配置.webp)


| Field | Value | Description |
| --- | --- | --- |
| ❶ Provider Name | `look2eye` | Recommended name, easier to match with the WebSocket settings |
| ❷ Website URL | `https://api.look2eye.com` | Provider website |
| ❸ API Key | Your Look2Eye API Key | Get it at [api.look2eye.com/keys](https://api.look2eye.com/keys) |
| ❹ Request URL | `https://api.look2eye.com/v1` | Do not add a trailing slash |
| ❺ API Format | `OpenAI Compatible` | Select OpenAI compatible format |
| ❻ Write to Global Config | ✅ Checked | Writes to global config, applies to all projects |


> ℹ️ CC Switch automatically writes to the config file — no manual file editing required.


### Step 3: Activate the Provider


After adding, go back to the list, select `look2eye`, and click **Use**. Make sure **Write to global config** is checked — the settings will be automatically written to `config.toml`.


![CC Switch activate provider](/assets/codex/03-cc-switch-写入通用配置.webp)


## Verify Configuration


```text
codex "hello"
```


![Codex CLI running](/assets/codex/04-codex-cli-运行效果.webp)


A normal AI response confirms the configuration is working.


## Next Step


- [Enable WebSocket (Recommended)](/en/codex/websocket/) — Add the Responses protocol format and WebSocket settings for smoother long coding sessions


## Specify a Model


```text
codex --model <model-id> "Refactor this function"
```


> ⚠️ Codex CLI uses the **Responses protocol format** (`wire_api = "responses"`) for streaming coding responses and tool calls. Not all models support this format. When selecting a model, confirm it supports the **Responses** protocol on the [Look2Eye Model Marketplace](https://api.look2eye.com/models) — otherwise you will get an error.


For recommended models, see the [Look2Eye Model Marketplace](https://api.look2eye.com/models).


## Troubleshooting


**Q: “Authentication error” message**


Confirm the API Key is correctly filled in and the request URL has no trailing slash.


**Q: Connection timeout**


Verify the request URL is `https://api.look2eye.com/v1` with no trailing slash.
