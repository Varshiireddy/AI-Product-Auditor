from app.embeddings.base_embedding_provider import BaseEmbeddingProvider
from app.evaluators.base_evaluator import BaseEvaluator
from app.models.ai_response import AIResponse
from app.models.audit_result import AuditResult
from app.models.evaluation_context import EvaluationContext
from app.utils.math_utils import cosine_similarity


class SemanticSimilarityEvaluator(BaseEvaluator):
    """Measures semantic similarity between the reference answer and the model response."""

    def __init__(
        self,
        embedding_provider: BaseEmbeddingProvider,
    ) -> None:
        self.embedding_provider = embedding_provider

    @property
    def name(self) -> str:
        return "semantic_similarity"

    def evaluate(
        self,
        response: AIResponse,
        context: EvaluationContext,
    ) -> AuditResult:
        reference_answer = context.reference_answer

        if reference_answer is None:
            raise ValueError("reference_answer is required.")

        reference_embedding = self.embedding_provider.embed(
            reference_answer,
        )

        response_embedding = self.embedding_provider.embed(
            response.text,
        )

        similarity = cosine_similarity(
            reference_embedding,
            response_embedding,
        )

        passed = similarity >= 0.80

        findings = [
            f"Semantic similarity: {similarity:.3f}"
        ]

        return AuditResult(
            passed=passed,
            score=similarity,
            findings=findings,
        )