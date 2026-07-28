import ollama

from app.embeddings.base_embedding_provider import BaseEmbeddingProvider


class OllamaEmbeddingProvider(BaseEmbeddingProvider):
    """Generates text embeddings using a local Ollama embedding model."""

    def __init__(self, model_name: str = "embeddinggemma") -> None:
        self.model_name = model_name

    def embed(self, text: str) -> list[float]:
        """Return the embedding vector for the given text."""

        response = ollama.embed(
            model=self.model_name,
            input=text,
        )

        embedding = response["embeddings"][0]

        return embedding