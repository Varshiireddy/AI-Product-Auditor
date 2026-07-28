import re

from app.connectors.base_connector import BaseConnector
from app.evaluators.base_evaluator import BaseEvaluator
from app.models.ai_response import AIResponse
from app.models.audit_result import AuditResult
from app.models.evaluation_context import EvaluationContext


class LLMJudgeEvaluator(BaseEvaluator):
    """Uses an LLM to evaluate correctness, relevance, and clarity."""

    def __init__(self, connector: BaseConnector) -> None:
        self.connector = connector

    @property
    def name(self) -> str:
        return "llm_judge"

    def evaluate(
        self,
        response: AIResponse,
        context: EvaluationContext,
    ) -> AuditResult:
        original_prompt = context.original_prompt

        if original_prompt is None:
            raise ValueError("original_prompt is required.")

        judge_prompt = f"""
You are an AI evaluator.

Question:
{original_prompt}

Answer:
{response.text}

Evaluate the answer for correctness, relevance, and clarity.

Return only in this exact format:

Score: <number from 0 to 10>
Reason: <one sentence>
""".strip()

        judge_response = self.connector.generate_response(judge_prompt)
        judge_text = judge_response.text.strip()

        score_match = re.search(
            r"Score:\s*(\d+(?:\.\d+)?)",
            judge_text,
            re.IGNORECASE,
        )

        reason_match = re.search(
            r"Reason:\s*(.+)",
            judge_text,
            re.IGNORECASE,
        )

        if score_match is None:
            raise ValueError(
                f"Could not find judge score in response: {judge_text}"
            )

        score_out_of_ten = float(score_match.group(1))
        score_out_of_ten = max(0.0, min(score_out_of_ten, 10.0))

        normalized_score = score_out_of_ten / 10.0
        passed = normalized_score >= 0.70

        reason = (
            reason_match.group(1).strip()
            if reason_match
            else "The judge did not provide a reason."
        )

        findings = [reason]

        return AuditResult(
            passed=passed,
            score=normalized_score,
            findings=findings,
        )