from dataclasses import dataclass


@dataclass
class AuditResult:
    """Stores the outcome of a single evaluator."""
    passed: bool
    score: float
    findings: list[str]