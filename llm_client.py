import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url=os.getenv("ZHIPU_BASE_URL"),
)

MODEL = os.getenv("ZHIPU_MODEL", "glm-5.1")


def call_llm(messages, temperature=0.2, max_tokens=800):
    """
    Call the LLM through an OpenAI-compatible API.

    Returns:
        tuple[str, dict]: generated content and token usage.
    """
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    content = response.choices[0].message.content

    usage = {
        "prompt_tokens": 0,
        "completion_tokens": 0,
        "total_tokens": 0,
    }

    if hasattr(response, "usage") and response.usage:
        usage = {
            "prompt_tokens": getattr(response.usage, "prompt_tokens", 0),
            "completion_tokens": getattr(response.usage, "completion_tokens", 0),
            "total_tokens": getattr(response.usage, "total_tokens", 0),
        }

    return content, usage
