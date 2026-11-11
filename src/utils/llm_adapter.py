import os
from typing import Any


def get_llm() -> Any:
    provider = os.getenv("LLM_PROVIDER")
    model = os.getenv("LLM_MODEL")

    if not provider:
        raise RuntimeError(
            "A variável de ambiente LLM_PROVIDER não foi definida.")
    if not model:
        raise RuntimeError(
            "A variável de ambiente LLM_MODEL não foi definida.")

    provider = provider.lower()

    if provider == "openai":
        from langchain_openai import ChatOpenAI

        return ChatOpenAI(model=model)

    if provider == "groq":
        from langchain_groq import ChatGroq

        return ChatGroq(model=model)

    if provider == "anthropic":
        from langchain_anthropic import ChatAnthropic

        return ChatAnthropic(model=model)

    if provider == "google":
        from langchain_google_genai import ChatGoogleGenerativeAI

        return ChatGoogleGenerativeAI(model=model)

    raise ValueError(f"Provedor de LLM não suportado: {provider}")