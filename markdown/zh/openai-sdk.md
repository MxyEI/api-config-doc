---
title: "OpenAI SDK 兼容"
description: "使用官方 OpenAI SDK 接入 Look2Eye 的 base URL 与 API Key 配置"
---


Look2Eye 完全兼容 OpenAI SDK，从 OpenAI 直连迁移只需修改两个参数：`base_url` 和 `api_key`。

## 迁移步骤

### 只需修改两行代码


**Python**

```python
from openai import OpenAI

# 之前：直连 OpenAI
# client = OpenAI(api_key="sk-openai-xxx")

# 现在：通过 Look2Eye
client = OpenAI(
    base_url="https://api.look2eye.com/v1",    # 新增
    api_key="<你的 LOOK2EYE_API_KEY>"       # 替换
)

# 其他代码完全不变！
response = client.chat.completions.create(
    model="openai/gpt-4o",  # 添加 provider 前缀
    messages=[{"role": "user", "content": "Hello!"}]
)
```

**TypeScript**

```ts

// 之前：直连 OpenAI
// const client = new OpenAI({ apiKey: 'sk-openai-xxx' })

// 现在：通过 Look2Eye
const client = new OpenAI({
  baseURL: 'https://api.look2eye.com/v1',      // 新增
  apiKey: '<你的 LOOK2EYE_API_KEY>'         // 替换
})

// 其他代码完全不变！
```

## 模型命名

Look2Eye 使用 `provider/model-name` 格式标识模型：

| OpenAI 原始名称 | Look2Eye 模型 ID |
| --- | --- |
| `gpt-4o` | `openai/gpt-4o` |
| `gpt-4o-mini` | `openai/gpt-4o-mini` |
| `gpt-5.2` | `openai/gpt-5.4-mini` |
| `text-embedding-3-small` | `openai/text-embedding-3-small` |

通过 Look2Eye，你还可以使用其他厂商的模型，推荐模型请参考 [Look2Eye 可用渠道](https://api.look2eye.com/available-channels)。

## 兼容性

Look2Eye 支持 OpenAI API 的以下功能：

| 功能 | 状态 |
| --- | --- |
| Chat Completions | ✅ 完全兼容 |
| Streaming | ✅ 完全兼容 |
| Function Calling | ✅ 完全兼容 |
| JSON Mode | ✅ 完全兼容 |
| Vision (图像输入) | ✅ 完全兼容 |
| Embeddings | ✅ 完全兼容 |
| Models List | ✅ 完全兼容 |
| Images Generation | ✅ 完全兼容 |

## 框架集成

### LangChain

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="https://api.look2eye.com/v1",
    api_key="<你的 LOOK2EYE_API_KEY>",
    model="openai/gpt-4o"
)
```

### LlamaIndex

```python
from llama_index.llms.openai import OpenAI

llm = OpenAI(
    api_base="https://api.look2eye.com/v1",
    api_key="<你的 LOOK2EYE_API_KEY>",
    model="openai/gpt-4o"
)
```

### Vercel AI SDK

```ts

const look2eye = createOpenAI({
  baseURL: 'https://api.look2eye.com/v1',
  apiKey: '<你的 LOOK2EYE_API_KEY>'
})

const model = look2eye('openai/gpt-4o')
```

> ℹ️ 任何支持 OpenAI SDK 的框架和工具，都可以通过修改 base_url 接入 Look2Eye。
