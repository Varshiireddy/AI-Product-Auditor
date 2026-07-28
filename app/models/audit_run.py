from dataclasses import dataclass

from app.models.ai_response import AIResponse
from app.models.evaluation_report import EvaluationReport
from app.models.audit_test import AuditTest


@dataclass
class AuditRun:
    test: AuditTest
    response: AIResponse
    result: EvaluationReport
    model_name: str