---
title: "Claude Coworks Configuration"
description: "Configure Look2Eye in Claude Coworks using the Gateway feature with the Anthropic-compatible protocol to access leading global models."
---


# Claude Coworks Configuration


[Claude Coworks](https://claude.ai/download) is Anthropic’s official desktop client. Its built-in third-party inference feature lets you route inference requests to Look2Eye via an Anthropic-compatible Gateway, giving you access to leading global models.


## Prerequisites


- A registered Look2Eye account with an API Key ([Get one here](https://api.look2eye.com/keys))
- Claude Coworks installed ([Download](https://claude.ai/download))


## Configuration Steps


### Step 1: Enable Developer Mode


In the menu bar, click **Help** → **Troubleshooting** → **Enable Developer Mode**.


![Enable Developer Mode](/assets/claude-coworks/01-enable-developer-mode.webp)


> ℹ️ After enabling Developer Mode, a **Developer** menu will appear in the menu bar.


### Step 2: Open the Third-Party Inference Settings


In the menu bar, click **Developer** → **Configure Third-Party Inference…** to open the configuration panel.


![Open Configuration Panel](/assets/claude-coworks/02-open-configuration-panel.webp)


### Step 3: Select Gateway


On the **Connection** page, select **Gateway** (Anthropic-compatible).


![Select Gateway](/assets/claude-coworks/03-select-gateway.webp)


### Step 4: Enter Credentials and Apply


Fill in the GATEWAY CREDENTIALS section, then click **Apply locally**:


| Field | Value |
| --- | --- |
| **Gateway base URL** | `https://api.api.look2eye.com/anthropic` |
| **Gateway API key** | Your Look2Eye API Key |
| **Gateway auth scheme** | `x-api-key` |


![Enter Credentials and Apply](/assets/claude-coworks/04-enter-credentials-and-apply.webp)


When the status indicator in the top-right turns green, the connection is active.


### Step 5: Browse Available Models


Once your connection is established, you can now view all available models through Claude Coworks. Visit the [Look2Eye Model Marketplace](https://api.look2eye.com/models) to explore the complete list of supported models and their capabilities.


![Browse Available Models](/assets/claude-coworks/05-browse-available-models.webp)


### Step 6: Select Your Model


In the Claude Coworks interface, select the specific model you want to use. You can switch between different models at any time depending on your needs. The selected model will be used for all your inference requests.


![Select Your Model](/assets/claude-coworks/06-select-your-model.webp)


### Step 7: Verify and Start Using


Your setup is now complete! Claude Coworks will route all inference requests through the Look2Eye Gateway using your selected model. You can now start using Claude Coworks normally, and all requests will be processed through Look2Eye’s infrastructure.


![Verification Complete](/assets/claude-coworks/07-verification-complete.webp)


## Getting Started


Once configured, all inference requests from Claude Coworks will be routed through the Look2Eye Gateway. Visit the [Look2Eye Model Marketplace](https://api.look2eye.com/models) to browse available models.


## FAQ


**Q: I can’t find the Developer menu in the menu bar**


You need to complete Step 1 first. The Developer menu only appears after Developer Mode is enabled.


**Q: The status indicator didn’t turn green after clicking Apply locally / Connection failed**


1. Confirm the Gateway base URL is `https://api.api.look2eye.com/anthropic` with no trailing slash
2. Confirm the Gateway auth scheme is set to `x-api-key`
3. Confirm the API Key was copied in full from the [Look2Eye Console](https://api.look2eye.com/keys) with no extra spaces
4. Check that your network connection is working
