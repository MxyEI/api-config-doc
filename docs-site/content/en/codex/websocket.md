---
title: "Enable WebSocket"
description: "Enable the recommended WebSocket connection for Codex local clients while keeping the Look2Eye API key in CC Switch"
---


# Enable WebSocket

Complete [Configure Model Provider](/en/codex/model-provider/) first, then run the one-line command to enable the Codex Responses protocol format and WebSocket connection. The script only updates connection capability. It does not read, save, or overwrite your API key.

## Enable WebSocket in One Command (Recommended)

```bash
curl -fsSL https://api.look2eye.com/install/codex.sh | bash
```

The script backs up `~/.codex/config.toml`, finds the Look2Eye provider written by CC Switch when possible, and adds these fields to the existing provider block. The example below uses `look2eye` as the provider name; if your local provider uses another name, replace `look2eye` with that name:

```toml
[model_providers.look2eye]
wire_api = "responses"
supports_websockets = true
```

> ℹ️ `wire_api = "responses"` tells Codex to use the Responses protocol format; `supports_websockets = true` tells Codex this provider supports a WebSocket connection. Together, they let Codex connect to Look2Eye through the recommended path.
> 
> The API key stays in the CC Switch Codex provider settings. This command only enables the Codex protocol format and WebSocket connection.
> 
> If your config uses an inline table under `[model_providers]`, the script updates the existing provider entry instead of forcing another TOML layout.
