from app.evaluators.base_evaluator import BaseEvaluator
from app.models.ai_response import AIResponse
from app.models.audit_result import AuditResult
from app.models.evaluation_context import EvaluationContext


class ExactMatchEvaluator(BaseEvaluator):
    """Checks whether the model response exactly matches the reference answer."""

    @property
    def name(self) -> str:
        return "exact_match"

    def evaluate(
        self,
        response: AIResponse,
        context: EvaluationContext,
    ) -> AuditResult:
        expected = context.reference_answer.strip().lower()
        actual = response.text.strip().lower()

        passed = expected == actual
        score = 1.0 if passed else 0.0

        findings = (
            ["Exact match."]
            if passed
            else ["Response does not exactly match the reference answer."]
        )

        return AuditResult(
            passed=passed,
            score=score,
            findings=findings,
        )