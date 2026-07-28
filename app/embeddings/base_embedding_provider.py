from abc import ABC, abstractmethod


class BaseEmbeddingProvider(ABC):
    @abstractmethod
    def embed(self, text: str) -> list[float]:
        """
        Convert text into a vector representation.
        """
        pass