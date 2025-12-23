# langchain-openai

[![PyPI - Version](https://img.shields.io/pypi/v/langchain-openai?label=%20)](https://pypi.org/project/langchain-openai/#history)
[![PyPI - License](https://img.shields.io/pypi/l/langchain-openai)](https://opensource.org/licenses/MIT)
[![PyPI - Downloads](https://img.shields.io/pepy/dt/langchain-openai)](https://pypistats.org/packages/langchain-openai)
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/langchainai.svg?style=social&label=Follow%20%40LangChainAI)](https://twitter.com/langchainai)

Looking for the JS/TS version? Check out [LangChain.js](https://github.com/langchain-ai/langchainjs).

## Quick Install

```bash
pip install langchain-openai
```

## 🤔 What is this?

This package contains the LangChain integrations for OpenAI through their `openai` SDK.

## 📖 Documentation

For full documentation, see the [API reference](https://reference.langchain.com/python/integrations/langchain_openai/). For conceptual guides, tutorials, and examples on using these classes, see the [LangChain Docs](https://docs.langchain.com/oss/python/integrations/providers/openai).

## 🔌 Using OpenAI-Compatible Providers

This package supports any OpenAI-compatible API endpoint through the `base_url` parameter. This allows you to use alternative providers that implement the OpenAI API specification.

### AI Badgr (Budget/Utility Provider)

AI Badgr is an OpenAI-compatible provider that offers budget-friendly model access with tier-based naming.

```python
from langchain_openai import ChatOpenAI
import os

# Set your AI Badgr API key
os.environ["AIBADGR_API_KEY"] = "your-api-key-here"

# Initialize with AI Badgr endpoint
llm = ChatOpenAI(
    base_url="https://aibadgr.com/api/v1",
    api_key=os.environ["AIBADGR_API_KEY"],
    model="premium",  # Use tier names: basic, normal, premium
)

# Use it like any other LangChain chat model
response = llm.invoke("Hello, how are you?")
print(response.content)
```

**Supported Models (Tier-first naming):**
- `basic` - Entry-level model
- `normal` - Standard model  
- `premium` - Advanced model (recommended)

**Advanced:** OpenAI model names are also accepted and mapped automatically. For power users:
- `phi-3-mini` → maps to `basic`
- `mistral-7b` → maps to `normal`
- `llama3-8b-instruct` → maps to `premium`

## 📕 Releases & Versioning

See our [Releases](https://docs.langchain.com/oss/python/release-policy) and [Versioning](https://docs.langchain.com/oss/python/versioning) policies.

## 💁 Contributing

As an open-source project in a rapidly developing field, we are extremely open to contributions, whether it be in the form of a new feature, improved infrastructure, or better documentation.

For detailed information on how to contribute, see the [Contributing Guide](https://docs.langchain.com/oss/python/contributing/overview).
