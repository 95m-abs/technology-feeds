from openai import OpenAI

from technology_feeds.providers.base import LLMProvider

class OpenAIAdapter:
    """Adapts OpenAI's API to our common interface"""
    def __init__(self, api_key: str, model: str) -> None:
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def generate(self, prompt: str) -> str:
        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )

        return response.output_text
