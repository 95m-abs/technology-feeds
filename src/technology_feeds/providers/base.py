from typing import Protocol

class LLMProvider(Protocol):
    """Control that every LLM provider must satisfy."""

    def generate(self, prompt: str) -> str:
        """Generate a text response from a prompt"""
        ...
