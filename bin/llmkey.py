#!/usr/bin/env python3
# Shared LLM key library for utility scripts

import keyring
import openai
from typing import TypeVar, Type
import inspect
import asyncio

T = TypeVar("T", openai.OpenAI, openai.AsyncOpenAI)


async def _get_ai(client_cls: Type[T], provider: str) -> openai.OpenAI:
    key = keyring.get_password("llmkey", provider)
    if provider == "siliconflow":
        ai = client_cls(base_url="https://api.siliconflow.cn/v1", api_key="placeholder")
    else:
        raise ValueError(f"Unknown provider: {provider}")
    if key is None:
        key = input("Enter your API key: ").strip()
    # Check if it works
    retries = 10
    while True:
        ai.api_key = key
        try:
            maybe_coro = ai.models.list()
            if inspect.isawaitable(maybe_coro):
                await maybe_coro
            # key ok, save it
            keyring.set_password("llmkey", provider, key)
            return ai
        except openai.AuthenticationError:
            print("Invalid API key. Please try again.")
            key = input("Enter your API key: ").strip()
        except Exception:
            if retries > 0:
                print("Error occurred. Retrying...")
                retries -= 1
            else:
                raise


def get_ai(provider: str = "siliconflow") -> openai.OpenAI:
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(_get_ai(openai.OpenAI, provider))
    else:
        return loop.run_until_complete(_get_ai(openai.AsyncOpenAI, provider))


async def aget_ai(provider: str = "siliconflow") -> openai.AsyncOpenAI:
    return await _get_ai(openai.AsyncOpenAI, provider)
