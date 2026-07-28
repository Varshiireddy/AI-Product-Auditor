from abc import ABC, abstractmethod

from app.models.ai_response import AIResponse
from app.models.audit_result import AuditResult
from app.models.evaluation_context import EvaluationContext


class BaseEvaluator(ABC):
    """Abstract base class for all evaluation strategies."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the evaluator's display name."""
        raise NotImplementedError

    @abstractmethod
    def evaluate(
        self,
        response: AIResponse,
        context: EvaluationContext,
    ) -> AuditResult:
        """
        Evaluate the model response and return an AuditResult.
        """
        raise NotImplementedError