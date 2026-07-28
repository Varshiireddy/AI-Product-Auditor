from app.embeddings.ollama_embedding_provider import OllamaEmbeddingProvider


provider = OllamaEmbeddingProvider()

embedding = provider.embed(
    "Python is a programming language."
)

print("Embedding type:", type(embedding))
print("Embedding length:", len(embedding))
print("First 5 values:", embedding[:5])