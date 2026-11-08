from technology_feeds.config import get_setting
from technology_feeds.providers.base import LLMProvider
from technology_feeds.providers.openai import OpenAIAdapter
from technology_feeds.providers.gemini import GeminiAdapter

def create_llm_provider() -> LLMProvider:
    """create the configured LLM provider"""

    provider = get_setting("LLM_PROVIDER").lower()

    if provider == "gemini":
        return GeminiAdapter(
            api_key=get_setting("GEMINI_API_KEY"),
            model=get_setting("GEMINI_MODEL"),
        )

    if provier == "openai":
        return OpenAIAdapter(
            api_key=get_setting("OPENAI_API_KEY"),
            model=get_setting("OPENAI_MODEL")
        )

    raise ValueError(f"Unsupported LLM Provider: {provider}")
