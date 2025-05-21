#!/usr/bin/env python3
# Shared LLM key library for utility scripts

import keyring
import openai

def get_ai(provider: str = "siliconflow") -> openai.OpenAI:
    key = keyring.get_password("llmkey", provider)
    if provider == "siliconflow":
        ai = openai.OpenAI(base_url="https://api.siliconflow.cn/v1", api_key="placeholder")
    else:
        raise ValueError(f"Unknown provider: {provider}")
    if key is None:
        key = input("Enter your API key: ").strip()
    # Check if it works
    retries = 10
    while True:
        ai.api_key = key
        try:
            ai.models.list()
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
