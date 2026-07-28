import time

import ollama

from app.connectors.base_connector import BaseConnector
from app.models.ai_response import AIResponse


class OllamaConnector(BaseConnector):
    """Generates responses using a local Ollama model."""

    def __init__(self, model: str = "qwen2.5:3b") -> None:
        self.model = model

    def generate_response(self, prompt: str) -> AIResponse:
        """Generate a response for the given prompt."""

        if not prompt.strip():
            raise ValueError("Prompt cannot be empty.")

        start_time = time.perf_counter()

        response = ollama.generate(
            model=self.model,
            prompt=prompt,
        )

        latency_ms = (time.perf_counter() - start_time) * 1000
        response_text = response["response"]

        return AIResponse(
            text=response_text,
            latency_ms=latency_ms,
        )