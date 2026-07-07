---
title: "Cline Configuration"
description: "Configure Look2Eye in Cline (VS Code AI coding plugin) to access GPT and other leading global models via OpenAI Compatible protocol"
---


# Cline Configuration


[Cline](https://github.com/cline/cline) is a popular VS Code AI coding plugin (formerly Claude Dev). By integrating with Look2Eye, you can use a variety of models.


## Prerequisites


- Registered Look2Eye account with an API Key ([Get one here](https://api.look2eye.com/keys))
- [VS Code](https://code.visualstudio.com/) installed


## Configuration Steps


### Step 1: Install Cline


Search for **Cline** in the VS Code Extension Marketplace and install it.


![Install Cline](/assets/cline/01-install-cline.webp)


### Step 2: Open Settings


Click the **Cline icon** in the left activity bar to open the Cline panel, then click the **Settings icon** in the top right corner.


![Open Cline Settings](/assets/cline/02-open-cline-settings.webp)


### Step 3: Fill in Configuration and Save


Fill in the following information on the API Configuration page, then click **Done** in the top right corner:


| Field | Value |
| --- | --- |
| **API Provider** | `OpenAI Compatible` |
| **Base URL** | `https://api.look2eye.com/v1` |
| **OpenAI Compatible API Key** | Your Look2Eye API Key |
| **Model ID** | `openai/gpt-4.1` (or another model) |


![Fill in configuration](/assets/cline/03-fill-in-configuration.webp)


> ℹ️ Cline also supports Anthropic and Gemini protocols. The corresponding Base URLs are `https://api.look2eye.com/anthropic` and `https://api.look2eye.com/gemini`.


## Recommended Models


For recommended models, see the [Model Marketplace](https://api.look2eye.com/models).


## FAQ


**Q: Model not supported error**


Make sure the Model ID format is correct. When using OpenAI Compatible, the model name must include the `vendor/` prefix, e.g. `openai/gpt-4.1`.


**Q: Unable to use Tool Use feature**


Switch the API Provider to Anthropic and change the Base URL to `https://api.look2eye.com/anthropic` for full Tool Use support.
