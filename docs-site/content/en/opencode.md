---
title: "OpenCode Configuration"
description: "Configure Look2Eye in OpenCode terminal AI coding tool, access leading global models via OpenAI-compatible mode, with complete installation and configuration steps"
---


# OpenCode Configuration


[OpenCode](https://github.com/opencode-ai/opencode) is an open-source terminal AI coding tool, similar to an open-source alternative to Claude Code. By integrating with Look2Eye, you can use any model.


## Configuration Steps


### 1. Install OpenCode


```text
# macOS / Linux
curl -fsSL https://opencode.ai/install | bash

# Or install with Go
go install github.com/opencode-ai/opencode@latest
```


![Install OpenCode](/assets/opencode/01-install-opencode.webp)


### 2. Configure Environment Variables


OpenCode supports multiple Provider configurations. The OpenAI-compatible mode is recommended:


```text filename="~/.zshrc"
# OpenAI-compatible mode
export OPENAI_API_KEY=<your LOOK2EYE_API_KEY>
export OPENAI_BASE_URL=https://api.api.look2eye.com/v1
```


If you primarily use Claude models, you can also configure Anthropic mode:


```text filename="~/.zshrc"
export ANTHROPIC_API_KEY=<your LOOK2EYE_API_KEY>
export ANTHROPIC_BASE_URL=https://api.api.look2eye.com/anthropic
```


### 3. Configuration File


You can also configure via OpenCode’s configuration file:


```toml filename="~/.config/opencode/config.toml"
[providers.look2eye]
api_key = "<your LOOK2EYE_API_KEY>"
base_url = "https://api.api.look2eye.com/v1"

[models.default]
provider = "look2eye"
model = "anthropic/claude-sonnet-4.6"
```


### 4. Verify


```text
opencode "Hello, how are you?"
```


![Running Result](/assets/opencode/02-running-result.webp)


## Recommended Models


For recommended models, see the [Model Marketplace](https://api.look2eye.com/models).


> ℹ️ The specific configuration of OpenCode may change with version updates. Please refer to the [OpenCode official documentation](https://github.com/opencode-ai/opencode).
