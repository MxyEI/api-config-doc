---
title: "GitHub Copilot Configuration"
description: "Configure Look2Eye via the VS Code extension OAI Compatible Provider for Copilot to use Claude, GPT-4o, Gemini, and leading global models in GitHub Copilot Chat — no editor switching required for multi-model AI coding assistance."
---


# GitHub Copilot Configuration


Using the VS Code extension **OAI Compatible Provider for Copilot**, you can integrate Look2Eye with GitHub Copilot Chat to use Claude, GPT-4o, Gemini, and leading global models right in your familiar editor.


> ⚠️ This extension requires a **GitHub Copilot Individual subscription** and does not support Copilot Business or Enterprise users. If you don’t have a Copilot subscription, consider using [Cursor](/en/cursor/) or [Cherry Studio](/en/cherry-studio/) instead.


## Prerequisites


- A registered Look2Eye account with an API Key ([Get one here](https://api.look2eye.com/console/api-keys))
- [VS Code](https://code.visualstudio.com/) installed
- A valid **GitHub Copilot Individual** subscription (Business / Enterprise not supported)


## Configuration Steps


### Step 1: Install the Extension


Search for **OAI Compatible Provider for Copilot** (by Johnny Zhao) in the VS Code Extension Marketplace and click **Install**.


![Install OAI Compatible Provider for Copilot extension](/assets/copilot/01-install-oai-compatible-provider-for-copilot-extension.webp)


### Step 2: Open the Configuration UI


Press `Cmd+Shift+P` (macOS) / `Ctrl+Shift+P` (Windows/Linux) to open the Command Palette, then type and run:


```http
OAICopilot: Open Configuration UI
```


![Open configuration UI via Command Palette](/assets/copilot/02-open-configuration-ui-via-command-palette.webp)


### Step 3: Fill in the Global Configuration


In the **Global Configuration** section, fill in the following fields and click **Save Global Configuration**:


| Field | Value |
| --- | --- |
| **Global Base URL** | `https://api.api.look2eye.com/v1` |
| **Global API Key** | Your Look2Eye API Key |


![Fill in Global Base URL and API Key then save](/assets/copilot/03-fill-in-global-base-url-and-api-key-then-save.webp)


### Step 4: Add a Provider


In the **Provider Management** section, click **Add Provider** (labeled ①), fill in the following fields in the new row, then click **Save** (labeled ⑥):


| Field | Value |
| --- | --- |
| **Provider ID** (labeled ②) | `look2eye` |
| **Base URL** (labeled ③) | `https://api.api.look2eye.com` |
| **API Key** (labeled ④) | Your Look2Eye API Key |
| **API Mode** (labeled ⑤) | `Anthropic` |


![Add Look2Eye Provider](/assets/copilot/04-add-look2eye-provider.webp)


### Step 5: Add a Model


In the **Model Management** section, click **Add Model** (labeled ①), fill in the following fields, then click **Save Model** (labeled ④):


| Field | Value |
| --- | --- |
| **Provider ID** (labeled ②) | `look2eye` |
| **Model ID** (labeled ③) | Model name, e.g. `anthropic/claude-opus-4.5` |


![Add a custom model](/assets/copilot/05-add-a-custom-model.webp)


You can repeat this step to add multiple models:


```text
anthropic/claude-sonnet-4.6
anthropic/claude-opus-4.6
openai/gpt-4o
openai/gpt-4o-mini
google/gemini-3.1-flash-lite-preview
```


### Step 6: Select a Model in the Chat Panel


Open the Copilot Chat panel, click the model selector, disable **Auto** mode, and find the Look2Eye models you added under **Other Models**.


If you can’t see the models, click **Manage Models…** to go to the model list page.


![Switch to Look2Eye model in the chat panel](/assets/copilot/06-switch-to-look2eye-model-in-the-chat-panel.webp)


### Step 7: Confirm Model and Start Using


In the Language Models panel, the Look2Eye models you added will appear under the **OAI Compatible** group. Select a model in the chat box in the bottom right to start chatting.


![Confirm model appears under OAI Compatible group](/assets/copilot/07-confirm-model-appears-under-oai-compatible-group.webp)


## Recommended Models


For recommended models, see the [Model Marketplace](https://api.look2eye.com/models).


## FAQ


**Q: I can’t find the extension in the marketplace**


Search the full name `OAI Compatible Provider for Copilot`, or search by the author name `Johnny Zhao`.


**Q: I can’t find `OAICopilot: Open Configuration UI` in the Command Palette**


Make sure the extension is installed and enabled. You may need to reload the VS Code window after installation (`Cmd+Shift+P` → `Reload Window`).


**Q: The models I added don’t appear in the chat panel**


In the model selector dropdown, disable **Auto** mode and look under the **Other Models** category, or click **Manage Models…** to check if the models were added correctly.


**Q: “Invalid API Key” error or request failure**


Check the following:


1. Is the Global Base URL exactly `https://api.api.look2eye.com/v1` (no trailing slash)?
2. Was the API Key copied in full from the [Look2Eye Console](https://api.look2eye.com/console/api-keys) (no leading/trailing spaces)?
3. Is the Provider’s API Mode set to `Anthropic`?


**Q: Tab completion still uses the official Copilot model**


This is expected behavior. OAI Compatible Provider currently only affects **Copilot Chat** conversations. Tab code completion is controlled by GitHub Copilot officially.


**Q: I’m a Copilot Business / Enterprise user — can I use this?**


Not currently. This extension only supports **GitHub Copilot Individual** users. Business and Enterprise users will need to wait for future version support.
