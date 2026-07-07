---
title: "Cherry Studio Configuration"
description: "Configure Look2Eye in Cherry Studio cross-platform AI desktop client, supporting OpenAI Chat, OpenAI Response, Claude, and Gemini protocols to access leading global models."
---


# Cherry Studio Configuration


[Cherry Studio](https://cherry-ai.com) is a cross-platform AI desktop client (supports Windows, macOS, Linux) with multi-model conversations, knowledge base, and workflow support — one of the most feature-rich open-source AI clients available.


By configuring Look2Eye as your provider, you can use GPT, Claude, Gemini, DeepSeek, and other leading global models in Cherry Studio with just one API Key.


## Protocol Overview


Cherry Studio supports connecting to Look2Eye via four protocols:


**OpenAI Chat** — Based on `/v1/chat/completions`, for GPT series models such as `openai/gpt-4.1`, `openai/gpt-5.3-chat`.


**OpenAI Response** — Based on `/v1/responses`, for GPT series models such as `openai/gpt-4.1`, `openai/gpt-5.4-mini`.


**Claude** — Based on `/anthropic/v1/messages`, for Claude series models such as `anthropic/claude-sonnet-4.6`, `anthropic/claude-opus-4.6`.


**Gemini** — Based on `/gemini/v1beta/models`, for Gemini series models such as `google/gemini-3.1-pro-preview`, `google/gemini-3.1-flash-lite-preview`.


## Prerequisites


- An Look2Eye account with an API Key ([Get one here](https://api.look2eye.com/keys))
- Cherry Studio installed ([Download](https://cherry-ai.com))


## Configuration Steps


### Step 1: Open Settings


Launch Cherry Studio and click the **Settings** icon in the bottom-left corner.


![Open Cherry Studio Settings](/assets/cherry-studio/01-open-cherry-studio-settings.webp)


### Step 2: Add a Model Provider


Go to **Model Services** in the left sidebar, scroll to the bottom, and click **+ Add**. In the dialog, enter a provider name and select the corresponding provider type.


**OpenAI Chat**


Select `OpenAI` as the provider type and click OK.


![Add OpenAI Chat Provider](/assets/cherry-studio/02-add-openai-chat-provider.webp)


**OpenAI Response**


Select `OpenAI` as the provider type (enable Response mode on the config page later) and click OK.


![Add OpenAI Response Provider](/assets/cherry-studio/03-add-openai-response-provider.webp)


**Claude**


Select `Anthropic` as the provider type and click OK.


![Add Claude Provider](/assets/cherry-studio/04-add-claude-provider.webp)


**Gemini**


Select `Gemini` as the provider type and click OK.


![Add Gemini Provider](/assets/cherry-studio/05-add-gemini-provider.webp)


### Step 3: Enter API Configuration


Fill in the API key and API address on the provider’s configuration page.


**OpenAI Chat**


| Field | Value |
| --- | --- |
| **API Key** | Your Look2Eye API Key |
| **API Address** | `https://api.look2eye.com/v1` |


![OpenAI Chat Configuration](/assets/cherry-studio/06-openai-chat-configuration.webp)


**OpenAI Response**


| Field | Value |
| --- | --- |
| **API Key** | Your Look2Eye API Key |
| **API Address** | `https://api.look2eye.com/v1` |


![OpenAI Response Configuration](/assets/cherry-studio/07-openai-response-configuration.webp)


**Claude**


| Field | Value |
| --- | --- |
| **API Key** | Your Look2Eye API Key |
| **API Address** | `https://api.look2eye.com/anthropic` |


![Claude Configuration](/assets/cherry-studio/08-claude-configuration.webp)


**Gemini**


| Field | Value |
| --- | --- |
| **API Key** | Your Look2Eye API Key |
| **API Address** | `https://api.look2eye.com/gemini` |


![Gemini Configuration](/assets/cherry-studio/09-gemini-configuration.webp)


> ⚠️ Make sure the toggle in the top-right corner of the page is **ON**, otherwise the provider will not appear in the model selector.


### Step 4: Add Models


Click the **Manage** button in the model section to automatically fetch the model list, then click **+** next to a model to add it to the enabled list.


**OpenAI Chat**


![OpenAI Chat Model List](/assets/cherry-studio/10-openai-chat-model-list.webp)


**OpenAI Response**


![OpenAI Response Model List](/assets/cherry-studio/11-openai-response-model-list.webp)


**Claude**


![Claude Model List](/assets/cherry-studio/12-claude-model-list.webp)


**Gemini**


![Gemini Model List](/assets/cherry-studio/13-gemini-model-list.webp)


### Step 5: Verify Configuration


Click the **Test** button, select any model to test. A passing result means the configuration is successful.


**OpenAI Chat**


![OpenAI Chat Verification](/assets/cherry-studio/14-openai-chat-verification.webp)


**OpenAI Response**


![OpenAI Response Verification](/assets/cherry-studio/15-openai-response-verification.webp)


**Claude**


![Claude Verification](/assets/cherry-studio/16-claude-verification.webp)


**Gemini**


![Gemini Verification](/assets/cherry-studio/17-gemini-verification.webp)


## Start Using


Return to the main interface, click the model selector at the top of the chat, and choose a model under the corresponding provider group to start chatting.


![Select Model to Start Chat](/assets/cherry-studio/18-select-model-to-start-chat.webp)


## Image Generation


Cherry Studio supports generating images via the Gemini protocol using Look2Eye’s image generation models, directly within conversations.


### Step 1: Add a Gemini Provider


Go to **Model Services** and click **+ Add** at the bottom.


![Add Provider](/assets/cherry-studio/19-add-provider.webp)


In the dialog, select **Gemini** as the provider type and click OK.


![Select Gemini Type](/assets/cherry-studio/20-select-gemini-type.webp)


### Step 2: Configure and Fetch Image Models


Set the API address to `https://api.look2eye.com/gemini`, then click **Fetch Model List** and add the following image generation models:


- `Google: Nano Banana Pro (Gemini 3 Pro Image Preview)`
- `Google: Nano Banana (Gemini 2.5 Flash Image)`
- `Google: Nano Banana 2 (Gemini 3.1 Flash Image Preview)`


![Fetch Image Models](/assets/cherry-studio/21-fetch-image-models.webp)


### Step 3: Edit Assistant and Configure Image Parameters


Right-click an assistant on the main interface and select **Edit Assistant**.


![Edit Assistant](/assets/cherry-studio/22-edit-assistant.webp)


On the edit page:


1. Set the **Default Model** to the image generation model you just added
2. Click **+ Add Parameter** and add the following two custom parameters:


| Parameter | Type | Value |
| --- | --- | --- |
| `responseModalities` | JSON | `["IMAGE"]` |
| `imageConfig` | JSON | `{"aspectRatio": "1:1", "imageSize": "1K"}` |


You can adjust the aspect ratio and resolution in `imageConfig`. For 2K images, change `imageSize` to `"2K"`.


![Configure Image Parameters](/assets/cherry-studio/23-configure-image-parameters.webp)


### Step 4: Start Generating


After saving the configuration, enter an image description in the chat to generate images.


![Image Generation Result](/assets/cherry-studio/24-image-generation-result.webp)


## FAQ


**Q: The model list is empty after clicking “Manage”**


Check that the API address is correct (no trailing slash) and that the API key was copied completely without extra spaces.


**Q: Connection failed during verification**


1. Confirm the API Key was copied completely from the [Look2Eye Console](https://api.look2eye.com/keys) without extra spaces
2. Confirm the API address is correct
3. Confirm your network connection is working


**Q: The provider doesn’t appear in the model selector**


Check that the toggle in the top-right corner of the configuration page is enabled.
