import json
from pathlib import Path

from app.models.audit_test import AuditTest
from app.models.evaluation_case import EvaluationCase
from app.models.evaluation_context import EvaluationContext


class DatasetLoader:
    """Loads evaluation datasets from JSON files."""

    def load(self, file_path: str) -> list[EvaluationCase]:
        path = Path(file_path)

        with path.open("r", encoding="utf-8") as file:
            dataset = json.load(file)

        cases: list[EvaluationCase] = []

        for test_case in dataset:
            test = AuditTest(
                name=test_case["name"],
                prompt=test_case["prompt"],
                category=test_case["category"],
            )

            context = EvaluationContext(
                expected_keyword=test_case["expected_keyword"],
                reference_answer=test_case["reference_answer"],
                original_prompt=test_case["prompt"],
            )

            cases.append(
                EvaluationCase(
                    test=test,
                    context=context,
                )
            )

        return cases