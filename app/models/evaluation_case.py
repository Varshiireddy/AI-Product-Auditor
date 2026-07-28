from dataclasses import dataclass

from app.models.audit_test import AuditTest
from app.models.evaluation_context import EvaluationContext


@dataclass
class EvaluationCase:
    test: AuditTest
    context: EvaluationContext