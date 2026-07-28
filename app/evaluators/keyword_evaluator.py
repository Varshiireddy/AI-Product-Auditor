from app.evaluators.base_evaluator import BaseEvaluator
from app.models.ai_response import AIResponse
from app.models.audit_result import AuditResult
from app.models.evaluation_context import EvaluationContext


class KeywordEvaluator(BaseEvaluator):
    """Checks whether the expected keyword appears in the model response."""

    @property
    def name(self) -> str:
        return "keyword"

    def evaluate(
        self,
        response: AIResponse,
        context: EvaluationContext,
    ) -> AuditResult:
        expected_keyword = context.expected_keyword

        if expected_keyword is None:
            raise ValueError("expected_keyword is required.")

        keyword_found = expected_keyword.lower() in response.text.lower()

        findings = (
            ["Expected keyword found."]
            if keyword_found
            else ["Expected keyword not found."]
        )

        return AuditResult(
            passed=keyword_found,
            score=1.0 if keyword_found else 0.0,
            findings=findings,
        )