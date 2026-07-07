---
title: "Gemini CLI Setup"
description: "Set up Look2Eye in Google Gemini CLI to access Gemini and other leading global models through the native Gemini protocol with a single API key"
---


# Gemini CLI Setup


[Gemini CLI](https://github.com/google-gemini/gemini-cli) is Google’s command-line tool for Gemini models. With Look2Eye, you can use the Gemini protocol while gaining access to a broader model selection.


## Setup Steps


### 1. Install Gemini CLI


```text
npm install -g @google/gemini-cli
```


![Install Gemini CLI](/assets/gemini-cli/01-install-gemini-cli.webp)


### 2. Configure Look2Eye


Gemini CLI uses the Gemini native protocol. Point it to Look2Eye via the configuration file:


```json filename="~/.gemini/settings.json"
{
  "apiKey": "<your LOOK2EYE_API_KEY>",
  "baseUrl": "https://api.api.look2eye.com/gemini"
}
```


Or use environment variables:


```text filename="~/.zshrc"
export GEMINI_API_KEY=<your LOOK2EYE_API_KEY>
```


> ⚠️ The base URL configuration method for Gemini CLI may change with version updates. If the above method doesn’t work, refer to the latest Gemini CLI documentation.


### 3. Verify


```text
gemini "Hello, tell me about yourself"
```


![Verify Gemini CLI](/assets/gemini-cli/02-verify-gemini-cli.webp)


## Available Models


For recommended models, see the [Look2Eye Model Marketplace](https://api.look2eye.com/models).


## Use Cases


- **Code generation and review** — Gemini models excel at code understanding
- **Long file analysis** — Leverage the 1M token context window
- **Multimodal tasks** — Analyze images, PDFs, and other files


> ℹ️ Using Gemini CLI through Look2Eye also gives you the benefits of fallback and routing optimization. See [Advanced](https://api.look2eye.com/en/develop/advanced/fallback) for details.
