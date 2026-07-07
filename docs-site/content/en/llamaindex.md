---
title: "LlamaIndex Configuration"
description: "Configure Look2Eye in LlamaIndex to access leading global models including GPT, Claude, Gemini, and DeepSeek via OpenAI-compatible protocol."
---


# LlamaIndex Configuration


[LlamaIndex](https://www.llamaindex.ai) is a data framework for building LLM applications, focused on RAG (Retrieval-Augmented Generation) and AI Agent scenarios. Since Look2Eye is fully compatible with the OpenAI protocol, you only need to change the `api_base` to get started.


## Prerequisites


- An Look2Eye account with an API Key ([Get one here](https://api.look2eye.com/keys))
- Python 3.10+ installed


## Configuration Steps


### Step 1: Install Dependencies


```text
pip3 install llama-index llama-index-llms-openai-like
```


![Install LlamaIndex](/assets/llamaindex/01-install-llamaindex.webp)


### Step 2: Configure and Run


Create a file `test_llamaindex.py`:


```python filename="test_llamaindex.py"
from llama_index.llms.openai_like import OpenAILike

llm = OpenAILike(
    model="openai/gpt-4.1",
    api_base="https://api.look2eye.com/v1",
    api_key="<YOUR_LOOK2EYE_API_KEY>",
    is_chat_model=True
)

response = llm.complete("Hello, introduce yourself")
print(response)
```


Run:


```text
python3 -W ignore test_llamaindex.py
```


![Run Result](/assets/llamaindex/02-run-result.webp)


## Available Models


For recommended models, see the [Look2Eye Model Marketplace](https://api.look2eye.com/models).


> ℹ️ LlamaIndex APIs may change across versions. Please refer to the [LlamaIndex official documentation](https://docs.llamaindex.ai).


## FAQ


**Q: `ModuleNotFoundError: No module named 'llama_index'`**


Run `pip3 install llama-index llama-index-llms-openai-like` to install the dependencies.


**Q: `TypeError: unsupported operand type(s) for |`**


Your Python version is too old. Please upgrade to Python 3.10 or above.


**Q: API Key is invalid**


Make sure the `api_key` is your Look2Eye API Key, which you can get from the [Look2Eye Console](https://api.look2eye.com/keys).
