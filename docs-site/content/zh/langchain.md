---
title: "LangChain 配置"
description: "在 LangChain Python 和 JavaScript 项目中使用 Look2Eye OpenAI 兼容接口。"
---


LangChain 是一个用于构建 AI 应用的开发框架，支持 Python 和 JavaScript。由于 Look2Eye 完全兼容 OpenAI 协议，只需修改 `openai_api_base` 即可接入。

## 前提条件

- 已注册 Look2Eye 账号并获取 API Key（[前往获取](https://api.look2eye.com/keys) ）
- 已安装 Python 3.8+

## 配置步骤

### 第 1 步：安装依赖

```text
pip3 install langchain langchain-openai
```

![安装 LangChain](/assets/langchain/01-安装-langchain-依赖.webp)

### 第 2 步：配置并运行

**Python**

```python filename="example.py"
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="openai/gpt-5.4-mini",
    api_key="YOUR_LOOK2EYE_API_KEY",
    base_url="https://api.look2eye.com",
)

response = llm.invoke("用一句话介绍 Look2Eye Gateway")
print(response.content)
```

运行：

```text
python3 -W ignore example.py
```

**JavaScript**

```js filename="example.js"

const llm = new ChatOpenAI({
  model: "openai/gpt-5.4-mini",
  apiKey: "YOUR_LOOK2EYE_API_KEY",
  configuration: {
    baseURL: "https://api.look2eye.com/v1",
  },
});

const response = await llm.invoke("用一句话介绍 Look2Eye Gateway");
console.log(response.content);
```

![运行效果](/assets/langchain/02-运行-langchain-示例.webp)

## 可用模型示例

推荐模型请参考 [Look2Eye 可用渠道](https://api.look2eye.com/available-channels) 。

## 常见问题

**Q: 提示 `ModuleNotFoundError: No module named 'langchain_openai'`**

运行 `pip3 install langchain-openai` 安装缺失的包。

**Q: 提示 API Key 无效**

确认 `openai_api_key` 填写的是 Look2Eye 的 API Key，而不是 OpenAI 官方的 Key。
