from app.connectors.base_connector import BaseConnector
from app.evaluators.base_evaluator import BaseEvaluator
from app.models.audit_run import AuditRun
from app.models.audit_test import AuditTest
from app.models.evaluation_context import EvaluationContext
from app.models.evaluation_report import EvaluationReport


class AuditRunner:
    """
    Runs an audit by generating a model response and
    evaluating it using all configured evaluators.
    """

    def __init__(
        self,
        connector: BaseConnector,
        evaluators: list[BaseEvaluator],
    ) -> None:
        self.connector = connector
        self.evaluators = evaluators

    def run(
        self,
        test: AuditTest,
        context: EvaluationContext,
    ) -> AuditRun:
        response = self.connector.generate_response(test.prompt)

        results = {}

        for evaluator in self.evaluators:
            results[evaluator.name] = evaluator.evaluate(
                response=response,
                context=context,
            )

        report = EvaluationReport(results=results)

        return AuditRun(
            test=test,
            response=response,
            result=report,
            model_name=self.connector.model,
        )