---
title: "NextChat Setup"
description: "Configure Look2Eye in NextChat with OpenAI, Anthropic, and Google protocols to access GPT, Claude, Gemini, and other leading global models with one API Key."
---


# NextChat Setup


[NextChat](https://nextchat.dev) (formerly ChatGPT-Next-Web) is a popular open-source AI client supporting Web, desktop (macOS, Windows, Linux) deployment, with a clean interface and support for multiple AI providers.


By configuring Look2Eye as your provider, you can use GPT, Claude, Gemini, and other leading global models in NextChat with a single API Key.


NextChat supports three protocols with Look2Eye:


| Protocol | Provider | Endpoint | Supported Models |
| --- | --- | --- | --- |
| **OpenAI Chat** | OpenAI | `https://api.api.look2eye.com` | All models (with `provider/` prefix) |
| **Anthropic** | Anthropic | `https://api.api.look2eye.com/anthropic` | Claude series |
| **Google Gemini** | Google | `https://api.api.look2eye.com/gemini` | Gemini series |


## Prerequisites


- An Look2Eye account with an API Key ([Get one here](https://api.look2eye.com/console/api-keys))
- NextChat installed ([Download](https://nextchat.dev)) or use the web version


## Setup Steps


### Step 1: Open Settings


Launch NextChat and click the **Settings** icon in the bottom left.


![Open NextChat Settings](/assets/nextchat/01-open-nextchat-settings.webp)


### Step 2: Configure Model Provider and API Key


In the settings page, find the **Model Provider** dropdown, select the corresponding provider, and fill in the API endpoint and API Key.


Fill in the configuration based on your chosen provider:


**OpenAI (supports all models)**


| Field | Value |
| --- | --- |
| **Model Provider** | OpenAI |
| **API Endpoint** | `https://api.api.look2eye.com` |
| **API Key** | Your Look2Eye API Key |
| **Custom Model Names** | e.g. `openai/gpt-5.3-chat,anthropic/claude-sonnet-4.6,deepseek/deepseek-v3.2` |


**Anthropic (Claude series)**


| Field | Value |
| --- | --- |
| **Model Provider** | Anthropic |
| **API Endpoint** | `https://api.api.look2eye.com/anthropic` |
| **API Key** | Your Look2Eye API Key |
| **Custom Model Names** | e.g. `claude-sonnet-4.6,claude-opus-4.6,claude-haiku-4.5` |


**Google (Gemini series)**


| Field | Value |
| --- | --- |
| **Model Provider** | Google |
| **API Endpoint** | `https://api.api.look2eye.com/gemini` |
| **API Key** | Your Look2Eye API Key |
| **Custom Model Names** | e.g. `google/gemini-3.1-pro-preview,google/gemini-3.1-flash-lite-preview` |


![Configure Model Provider and API Key](/assets/nextchat/02-configure-model-provider-and-api-key.webp)


> ℹ️ The **Custom Model Names** field supports multiple models separated by commas. These models will appear in the **Model** dropdown for selection.


> ⚠️ When using the OpenAI provider, set the API Endpoint to `https://api.api.look2eye.com` (without `/v1`). NextChat appends the path automatically. Using `https://api.api.look2eye.com/v1` will cause a duplicate path error.


### Step 3: Select a Model


After configuration, in the **Model** dropdown at the bottom of the settings page, you can see the custom models you just entered.


![Select model after configuration](/assets/nextchat/03-select-model-after-configuration.webp)


Click the dropdown to see all available providers and models.


![Model list](/assets/nextchat/04-model-list.webp)


## Start Using


Close settings and go back to the main screen. Select your model and start chatting.


![Start chatting](/assets/nextchat/05-start-chatting.webp)


## Available Model Examples


For recommended models, see the [Look2Eye Model Marketplace](https://api.look2eye.com/models).


## Troubleshooting


**Q: Error `No providers support endpoint 'chat_completions'`**


The model name is incorrect or your account doesn’t have access to that model. Check the model name or try a different one.


**Q: Error `Unsupported OpenAI API endpoint`**


The API Endpoint is set to `https://api.api.look2eye.com/v1`, causing a duplicate path. Change it to `https://api.api.look2eye.com` (without `/v1`).


**Q: Can the OpenAI provider call Claude and Gemini models?**


Yes. When using the OpenAI provider, enter the full model name with provider prefix in Custom Model Names (e.g. `anthropic/claude-sonnet-4.6`), and Look2Eye will route to the correct provider.


**Q: Do Anthropic and Google provider model names need a prefix?**


For Anthropic, enter just `claude-sonnet-4.6` (no prefix). For Google, enter `google/gemini-3.1-pro-preview` (with `google/` prefix).
