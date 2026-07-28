from dataclasses import dataclass

from app.models.audit_result import AuditResult


@dataclass
class EvaluationReport:
    results: dict[str, AuditResult]