---
title: "Immersive Translate Setup"
description: "Configure Look2Eye in the Immersive Translate browser extension with OpenAI Chat, OpenAI Response, and Claude protocols to access leading global models for high-quality bilingual translation."
---


# Immersive Translate Setup


[Immersive Translate](https://immersivetranslate.com) is a popular browser translation extension supporting bilingual side-by-side display, capable of translating web pages, PDFs, subtitles, and input fields across Chrome, Firefox, and Safari.


By configuring Look2Eye as your translation service, you can use GPT, Claude, Gemini, DeepSeek, and other leading global models with a single API Key.


## Prerequisites


- An Look2Eye account with an API Key ([Get one here](https://api.look2eye.com/keys))
- Immersive Translate installed ([Download](https://immersivetranslate.com))


## Supported Protocols


Immersive Translate supports three protocols with Look2Eye:


| Protocol | Setup Method | Custom API Endpoint | Supported Models |
| --- | --- | --- | --- |
| **OpenAI Chat** | Custom service | `https://api.api.look2eye.com/v1/chat/completions` | All models |
| **OpenAI Response** | Custom service | `https://api.api.look2eye.com/v1/responses` | All models |
| **Claude** | Built-in Claude provider | `https://api.api.look2eye.com/anthropic` | Claude series |
| **Gemini (via OpenAI Chat)** | Custom service | `https://api.api.look2eye.com/v1/chat/completions` | Gemini series |


> ℹ️ The built-in Gemini provider in Immersive Translate uses `x-goog-api-key` authentication, which is incompatible with Look2Eye’s `Authorization: Bearer` method. To use Gemini models, use the OpenAI Chat custom service and enter the Gemini model name in the custom model field (e.g. `google/gemini-3.1-flash-lite-preview`, `google/gemini-3.1-pro-preview`, etc.).


## Setup Steps


### Step 1: Open Translation Service Settings


Click the Immersive Translate icon in your browser toolbar, go to Settings, then click the **Translation Service** tab at the top.


![Open translation service settings](/assets/immersive-translate/01-open-translation-service-settings.webp)


### Step 2: Find the Custom Service Entry


Scroll down to the **Other/Custom** section on the Translation Service page.


![Translation service list](/assets/immersive-translate/02-translation-service-list.webp)


Click the **Add Custom Translation Service** button in the top right.


![Add custom translation service](/assets/immersive-translate/03-add-custom-translation-service.webp)


### Step 3: Fill in the Configuration


Fill in the details based on your chosen protocol:


**OpenAI Chat (supports all models including Gemini)**


| Field | Value |
| --- | --- |
| **Service Name** | `look2eye` (or any name) |
| **Custom API Endpoint** | `https://api.api.look2eye.com/v1/chat/completions` |
| **API Key** | Your Look2Eye API Key |
| **Model** | Check “Enter custom model name”, e.g. `openai/gpt-4.1` |


**OpenAI Response**


| Field | Value |
| --- | --- |
| **Service Name** | `look2eye-response` (or any name) |
| **Custom API Endpoint** | `https://api.api.look2eye.com/v1/responses` |
| **API Key** | Your Look2Eye API Key |
| **Model** | Check “Enter custom model name”, e.g. `openai/gpt-4.1` |


**Claude (Anthropic native protocol)**


Use the built-in **Claude** provider — no need to add a custom service:


| Field | Value |
| --- | --- |
| **API Key** | Your Look2Eye API Key |
| **Custom API Endpoint** | `https://api.api.look2eye.com/anthropic` |
| **Model** | Check “Enter custom model name”, fill in `claude-sonnet-4.6` |


Click **Test Service**, and once it passes click **Save**.


![Fill in configuration](/assets/immersive-translate/04-fill-in-configuration.webp)


### Step 4: Set as Default and Start Translating


In the translation service list, toggle the switch next to your configured service to set it as **current default**. Then open any webpage and press `Alt + A` (Mac: `Option + A`) to translate.


## Translation Result


After setup, pages display original and translated text side by side.


![Translation result](/assets/immersive-translate/05-translation-result.webp)


## Available Model Examples


For recommended models, see the [Look2Eye Model Marketplace](https://api.look2eye.com/models).


## Troubleshooting


**Q: Error `String contains non ISO-8859-1 code point` during test**


Your API Key contains non-ASCII characters (e.g. full-width spaces). Re-copy the API Key from the [Look2Eye Console](https://api.look2eye.com/keys) and make sure there are no extra characters.


**Q: Can the built-in Gemini provider connect to Look2Eye?**


No. The built-in Gemini provider uses `x-goog-api-key` authentication, incompatible with Look2Eye’s `Authorization: Bearer`. Use the OpenAI Chat custom service and enter the Gemini model name in the custom model field (e.g. `google/gemini-3.1-flash-lite-preview`, `google/gemini-3.1-pro-preview`, etc.).


**Q: How do I switch between translation services?**


On the **Translation Service** page, toggle the switch next to the service you want to use as the current default.
