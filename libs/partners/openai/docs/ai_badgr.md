# Using AI Badgr with LangChain

AI Badgr is an OpenAI-compatible API provider that offers budget-friendly model access. You can use AI Badgr with LangChain's `ChatOpenAI` class by configuring a custom base URL.

## Setup

Install the LangChain OpenAI integration:

```bash
pip install langchain-openai
```

Set your AI Badgr API key as an environment variable:

```bash
export OPENAI_API_KEY="sk-aibadgr-your-actual-api-key-here"
# Optional: override the default base URL
export OPENAI_API_BASE="https://aibadgr.com/api/v1"
```

## Basic Usage

AI Badgr supports tier-based model names (`basic`, `normal`, `premium`) that automatically map to appropriate models:

```python
from langchain_openai import ChatOpenAI

# Using tier names (recommended)
llm = ChatOpenAI(
    model="premium",
    base_url="https://aibadgr.com/api/v1"
)

response = llm.invoke("Hello, how are you?")
print(response.content)
```

## Model Tiers

AI Badgr offers three model tiers:

- `basic` - Budget-tier models suitable for simple tasks
- `normal` - Balanced performance and cost
- `premium` - High-performance models (recommended for examples)

Specific model names are also supported:
- `phi-3-mini` (basic tier)
- `mistral-7b` (normal tier)
- `llama3-8b-instruct` (premium tier)

OpenAI model names like `gpt-4` or `gpt-3.5-turbo` are also accepted by the AI Badgr API.

## Environment Variables

- `OPENAI_API_KEY` - Your AI Badgr API key (required)
- `OPENAI_API_BASE` - AI Badgr base URL (optional override)

## Example with Streaming

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="premium",
    base_url="https://aibadgr.com/api/v1",
    streaming=True
)

for chunk in llm.stream("Write a short poem about AI"):
    print(chunk.content, end="", flush=True)
```

## Example with Tool Calling

```python
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

@tool
def get_weather(location: str) -> str:
    """Get the weather for a location."""
    return f"The weather in {location} is sunny."

llm = ChatOpenAI(
    model="premium",
    base_url="https://aibadgr.com/api/v1"
)

llm_with_tools = llm.bind_tools([get_weather])
response = llm_with_tools.invoke("What's the weather in San Francisco?")
print(response)
```

## Notes

- AI Badgr provides another OpenAI-compatible endpoint option for users who want a budget provider.
- All standard `ChatOpenAI` parameters are supported.
- Authentication uses the standard `Authorization: Bearer <API_KEY>` header.
- For more details on `ChatOpenAI` capabilities, see the [LangChain OpenAI documentation](https://docs.langchain.com/oss/python/integrations/providers/openai).
