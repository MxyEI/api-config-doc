---
title: "OpenCat Setup"
description: "Configure Look2Eye in OpenCat AI client using the OpenAI-compatible protocol to access GPT, Claude, Gemini, DeepSeek, and other leading global models with one API Key."
---


# OpenCat Setup


[OpenCat](https://opencat.app) is a clean and smooth AI client (macOS, iOS) designed for everyday AI conversations, supporting custom API providers, multi-model switching, and conversation history.


By configuring Look2Eye as your provider, you can use GPT, Claude, Gemini, DeepSeek, and other leading global models in OpenCat with a single API Key.


## Prerequisites


- An Look2Eye account with an API Key ([Get one here](https://api.look2eye.com/keys))
- OpenCat installed ([Download](https://opencat.app))


## Setup Steps


### Step 1: Open Settings


Launch OpenCat and click the **Settings** icon in the bottom left.


![Open OpenCat Settings](/assets/opencat/01-open-opencat-settings.webp)


### Step 2: Go to Providers and Select OpenAI Compatible


Click **Providers** in the sidebar, then find and click **OpenAI Compatible**.


![Select OpenAI Compatible](/assets/opencat/02-select-openai-compatible.webp)


> ℹ️ Select **OpenAI Compatible**, not the native OpenAI option. The native OpenAI option tries to fetch the model list from OpenAI’s official API, which is incompatible with Look2Eye’s model format.


### Step 3: Fill in the Configuration


Fill in the following:


| Field | Value |
| --- | --- |
| **Base URL** | `https://api.api.look2eye.com/v1` |
| **API Key** | Your Look2Eye API Key |
| **Custom Models** | Enter model names manually, e.g. `openai/gpt-4.1` |


![Fill in configuration](/assets/opencat/03-fill-in-configuration.webp)


> ℹ️ Custom models use the `provider/model-name` format. You can add multiple models at once for easy switching during conversations.


### Step 4: Validate and Save


Click the **Validate** button. Once you see “**Validate Success**”, click **Save** in the top right.


![Validate Success](/assets/opencat/04-validate-success.webp)


## Start Using


After setup, go back to the main screen to start chatting. The current model name is shown at the top.


![Start chatting](/assets/opencat/05-start-chatting.webp)


## Available Model Examples


For recommended models, see the [Look2Eye Model Marketplace](https://api.look2eye.com/models).


## Troubleshooting


**Q: Validation fails**


1. Make sure Base URL is `https://api.api.look2eye.com/v1` (no trailing slash)
2. Make sure your API Key is copied in full from the [Look2Eye Console](https://api.look2eye.com/keys) with no extra spaces
3. Check your network connection


**Q: Why use OpenAI Compatible instead of native OpenAI?**


The native OpenAI provider in OpenCat automatically calls `/v1/models` to fetch the model list, but Look2Eye’s model names include provider prefixes like `openai/` that OpenCat can’t recognize. Using **OpenAI Compatible** with manually entered model names works around this issue.


**Q: Can I add multiple models at once?**


Yes — enter multiple model names line by line in the Custom Models field. After saving, you can switch between them during conversations.
