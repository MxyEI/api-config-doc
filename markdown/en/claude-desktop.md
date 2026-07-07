---
title: "Claude Desktop Setup"
description: "Enable third-party inference gateway in Claude Desktop and access Claude models through Look2Eye's Anthropic-compatible protocol."
---


[Claude Desktop](https://claude.com) is Anthropic's official desktop client. It has a built-in "Third-Party Inference" feature that can forward inference requests to Look2Eye through an Anthropic-compatible gateway, giving you access to top models worldwide.

## Prerequisites

- A Look2Eye account with an API Key ([get one here](https://api.look2eye.com/keys))
- Claude Desktop installed ([download](https://claude.com))

## Setup Steps
### Step 1:
Install and open Claude Desktop.

### Step 2: Open the Third-Party Inference Settings

In the menu bar, click **Developer → Configure Third-Party Inference…** to open the configuration panel.

![Open the configuration panel](../assets/claude-desktop/001-ccdesktp-config1.webp)

### Step 3: Select Gateway

On the **Connection** page, select **Gateway (Anthropic-compatible)**.



### Step 4: Fill in Credentials and Apply

In the **GATEWAY CREDENTIALS** section, fill in the following information, then click **Apply locally**:

| Field | Value |
| --- |----------------------------|
| Gateway base URL | `https://api.look2eye.com` |
| Gateway API key | Your Look2Eye API Key |
| Gateway auth scheme | `bearer` |

![Fill in credentials and apply](../assets/claude-desktop/002-ccdesktop-config2.webp)

When the status indicator in the top-right corner turns green, the connection is established.

### Step 5: Browse Available Models

Once connected, you can browse all available models in Claude Desktop. Visit [Look2Eye Available Channels](https://api.look2eye.com/available-channels) for the full list of supported models and their capabilities.

![Browse available models](../assets/claude-desktop/003-ccdesktop-models.webp)

### Step 6: Select Your Model

Pick the specific model you want to use in the Claude Desktop interface. You can switch between models at any time. The selected model will be used for all inference requests.

![Select your model](../assets/claude-desktop/003-ccdesktop-models.webp)

### Step 7: Verify and Start Using

Setup complete! Claude Desktop will forward all inference requests through the Look2Eye gateway using your selected model. You can now use Claude Desktop normally — all requests are handled by Look2Eye's infrastructure.


## Getting Started

Once the configuration takes effect, all Claude Desktop inference requests are forwarded through the Look2Eye gateway. Visit [Look2Eye Available Channels](https://api.look2eye.com/available-channels) to see the list of supported models.

## FAQ

**Q: The status indicator doesn't turn green after clicking Apply locally / connection fails**

1. Confirm the Gateway base URL is `https://api.look2eye.com` with no trailing slash
2. Confirm the Gateway auth scheme is set to `bearer`
3. Confirm the API Key is copied in full from the Look2Eye console, with no extra spaces
4. Confirm your network connection is working
