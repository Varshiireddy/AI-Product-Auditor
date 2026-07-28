from abc import ABC, abstractmethod

from app.models.ai_response import AIResponse


class BaseConnector(ABC):
    @abstractmethod
    def generate_response(self, prompt: str) -> AIResponse:
        pass