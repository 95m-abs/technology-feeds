from google import genai
from technology_feeds.providers.base import LLMProvider

class GeminiAdapter:
    """Adapters google's gemini api to our common interface"""
    def __init__(self, api_key: str, model: str) -> None:
        self.client = genai.Client(api_key=api_key)
        self.model = model

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        if response.text is None:
            raise RuntimeError("Gemini returned no text response")

        return response.text
