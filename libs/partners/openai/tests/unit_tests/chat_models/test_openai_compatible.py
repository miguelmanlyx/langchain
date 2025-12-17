"""Test OpenAI-compatible providers like AI Badgr."""

import os

import pytest

from langchain_openai import ChatOpenAI


def test_aibadgr_initialization() -> None:
    """Test that AI Badgr can be initialized with custom base_url."""
    llm = ChatOpenAI(
        base_url="https://aibadgr.com/api/v1",
        api_key="test-key",
        model="premium",
    )
    assert llm.openai_api_base == "https://aibadgr.com/api/v1"
    assert llm.model_name == "premium"


def test_aibadgr_with_env_vars() -> None:
    """Test that AI Badgr can use environment variables."""
    # Set environment variables
    os.environ["AIBADGR_API_KEY"] = "test-api-key"
    os.environ["AIBADGR_BASE_URL"] = "https://aibadgr.com/api/v1"

    llm = ChatOpenAI(
        base_url=os.environ["AIBADGR_BASE_URL"],
        api_key=os.environ["AIBADGR_API_KEY"],
        model="premium",
    )

    assert llm.openai_api_base == "https://aibadgr.com/api/v1"
    assert llm.openai_api_key.get_secret_value() == "test-api-key"

    # Clean up
    del os.environ["AIBADGR_API_KEY"]
    del os.environ["AIBADGR_BASE_URL"]


def test_aibadgr_tier_models() -> None:
    """Test that tier-based model names can be used."""
    tier_models = ["basic", "normal", "premium"]

    for model in tier_models:
        llm = ChatOpenAI(
            base_url="https://aibadgr.com/api/v1",
            api_key="test-key",
            model=model,
        )
        assert llm.model_name == model


def test_openai_compatible_generic() -> None:
    """Test that any OpenAI-compatible endpoint can be configured."""
    llm = ChatOpenAI(
        base_url="https://example.com/v1",
        api_key="test-key",
        model="test-model",
    )
    assert llm.openai_api_base == "https://example.com/v1"
    assert llm.model_name == "test-model"
