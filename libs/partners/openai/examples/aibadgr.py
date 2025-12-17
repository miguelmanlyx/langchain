"""Example: Using AI Badgr as an OpenAI-compatible provider.

AI Badgr is a budget/utility provider that offers OpenAI-compatible API endpoints.
This example shows how to use it with langchain-openai.
"""

import os

from langchain_openai import ChatOpenAI


def main() -> None:
    """Demonstrate AI Badgr usage with tier-based model names."""
    # Configure AI Badgr credentials
    # In production, set these via environment variables
    api_key = os.environ.get("AIBADGR_API_KEY", "your-api-key-here")
    base_url = os.environ.get("AIBADGR_BASE_URL", "https://aibadgr.com/api/v1")

    # Initialize ChatOpenAI with AI Badgr endpoint
    llm = ChatOpenAI(
        base_url=base_url,
        api_key=api_key,
        model="premium",  # Tier-based naming: basic, normal, premium
        temperature=0.7,
    )

    # Basic invocation
    print("=== Basic Usage ===")
    response = llm.invoke("What is the capital of France?")
    print(f"Response: {response.content}\n")

    # Streaming response
    print("=== Streaming Usage ===")
    for chunk in llm.stream("Tell me a short joke."):
        print(chunk.content, end="", flush=True)
    print("\n")

    # Batch processing
    print("=== Batch Usage ===")
    messages_batch = [
        "What is 2+2?",
        "What is the largest planet?",
        "Name a programming language.",
    ]
    responses = llm.batch(messages_batch)
    for i, response in enumerate(responses, 1):
        print(f"{i}. {response.content}")


if __name__ == "__main__":
    main()
