---
title: "OpenAI SDK Compatible"
description: "Migrate from OpenAI to Look2Eye in one line — just change the base URL to access leading global models with full OpenAI SDK compatibility in Python and Node.js"
---


# OpenAI SDK Compatible


Look2Eye is fully compatible with the OpenAI SDK. Migrating from a direct OpenAI connection requires changing just two parameters: `base_url` and `api_key`.


## Migration Steps


### Just Change Two Lines of Code


**Python**

```python
from openai import OpenAI

# Before: direct OpenAI connection
# client = OpenAI(api_key="sk-openai-xxx")

# Now: through Look2Eye
client = OpenAI(
    base_url="https://api.api.look2eye.com/v1",    # Added
    api_key="<your LOOK2EYE_API_KEY>"       # Replaced
)

# Everything else stays the same!
response = client.chat.completions.create(
    model="openai/gpt-4o",  # Add provider prefix
    messages=[{"role": "user", "content": "Hello!"}]
)
```

**TypeScript**

```python

// Before: direct OpenAI connection
// const client = new OpenAI({ apiKey: 'sk-openai-xxx' })

// Now: through Look2Eye
const client = new OpenAI({
  baseURL: 'https://api.api.look2eye.com/v1',      // Added
  apiKey: '<your LOOK2EYE_API_KEY>'         // Replaced
})

// Everything else stays the same!
```


## Model Naming


Look2Eye uses the `provider/model-name` format for model identifiers:


| OpenAI Original Name | Look2Eye Model ID |
| --- | --- |
| `gpt-4o` | `openai/gpt-4o` |
| `gpt-4o-mini` | `openai/gpt-4o-mini` |
| `gpt-5.2` | `openai/gpt-5.4-mini` |
| `text-embedding-3-small` | `openai/text-embedding-3-small` |


Through Look2Eye, you can also access models from other providers. For recommended models, see the [Look2Eye Model Marketplace](https://api.look2eye.com/models).


## Compatibility


Look2Eye supports the following OpenAI API features:


| Feature | Status |
| --- | --- |
| Chat Completions | ✅ Fully compatible |
| Streaming | ✅ Fully compatible |
| Function Calling | ✅ Fully compatible |
| JSON Mode | ✅ Fully compatible |
| Vision (image input) | ✅ Fully compatible |
| Embeddings | ✅ Fully compatible |
| Models List | ✅ Fully compatible |
| Images Generation | ✅ Fully compatible |


## Framework Integration


### LangChain


```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="https://api.api.look2eye.com/v1",
    api_key="<your LOOK2EYE_API_KEY>",
    model="openai/gpt-4o"
)
```


### LlamaIndex


```python
from llama_index.llms.openai import OpenAI

llm = OpenAI(
    api_base="https://api.api.look2eye.com/v1",
    api_key="<your LOOK2EYE_API_KEY>",
    model="openai/gpt-4o"
)
```


### Vercel AI SDK


```python

const look2eye = createOpenAI({
  baseURL: 'https://api.api.look2eye.com/v1',
  apiKey: '<your LOOK2EYE_API_KEY>'
})

const model = look2eye('openai/gpt-4o')
```


> ℹ️ Any framework or tool that supports the OpenAI SDK can integrate with Look2Eye by changing the `base_url`.
