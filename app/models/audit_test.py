from dataclasses import dataclass


@dataclass
class AuditTest:
    name: str
    prompt: str
    category: str