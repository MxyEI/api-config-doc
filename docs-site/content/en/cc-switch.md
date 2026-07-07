---
title: "CC-Switch Configuration"
description: "Configure CC-Switch to use Look2Eye models with real-time usage tracking and monitoring across leading global models in a unified interface."
---


# CC-Switch Configuration


CC-Switch is a powerful multi-model management tool that integrates Look2Eye and other AI providers in a single interface. With **usage query support**, you can now monitor your Look2Eye API consumption in real-time.


## Prerequisites


- Registered Look2Eye account with API Key ([Get API Key](https://api.look2eye.com/console/api-keys))
- Installed and configured [CC-Switch](https://github.com/cc-dayx/cc-switch)


## Configuration Steps


### Step 1: Add Look2Eye Provider


Add a new provider in CC-Switch with the following configuration:


| Configuration | Value |
| --- | --- |
| **Provider Name** | `look2eye-claude` (or custom name) |
| **API Base URL** | `https://api.api.look2eye.com/v1` |
| **API Key** | Your Look2Eye API Key |


### Step 2: Enable Usage Query


The image below shows how to configure usage query in CC-Switch:


![CC-Switch Usage Query Configuration](/assets/cc-switch/01-cc-switch-usage-query-configuration.webp)


**Configuration highlights:**


1. **Enable Usage Query** — Toggle the green switch on the right (see image marker ②)
2. **API Key** — Enter your Look2Eye API Key (marker ③)
3. **Request Endpoint** — Set to `https://api.api.look2eye.com/v1` (marker ④)
4. **Template** — Select **Universal Template** for best compatibility


### Step 3: Verify Configuration


After configuration, you can:


- View real-time usage statistics in the CC-Switch dashboard
- Monitor API call counts and token consumption
- Track costs and budget usage


> ℹ️ Usage query works by periodically calling the Look2Eye API to fetch account statistics. Ensure your API Key has sufficient permissions.


> ⚠️ Never commit API Keys to public repositories. Use environment variables or secure key management systems to store your API Key.


## Supported Models


Through Look2Eye, CC-Switch can access leading global models. See [Look2Eye Model Marketplace](https://api.look2eye.com/models) for details.


## FAQ


**Q: How frequently does usage data update?**


Usage data typically updates within a few minutes after API calls, depending on Look2Eye’s processing speed.


**Q: How do I disable usage query?**


Simply toggle off the usage query switch for the provider in CC-Switch. This won’t affect normal API calls.


**Q: Does usage query consume API quota?**


No. Usage query uses a dedicated statistics API and does not count against your API call limits.


**Q: Can I add multiple Look2Eye accounts?**


Yes. You can add multiple Look2Eye provider configurations in CC-Switch using different API Keys.
