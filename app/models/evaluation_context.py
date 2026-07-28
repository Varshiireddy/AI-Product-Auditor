from dataclasses import dataclass


@dataclass
class EvaluationContext:
    expected_keyword: str | None = None
    reference_answer: str | None = None
    original_prompt: str | None = None