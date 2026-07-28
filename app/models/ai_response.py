from dataclasses import dataclass


@dataclass
class AIResponse:
    """Stores the model response and the time taken to generate it."""
    text: str
    latency_ms: float