import webbrowser
from typing import Any

from app.cli import parse_arguments
from app.connectors.ollama_connector import OllamaConnector
from app.core.audit_runner import AuditRunner
from app.core.dataset_loader import DatasetLoader
from app.embeddings.ollama_embedding_provider import OllamaEmbeddingProvider
from app.evaluators.exact_match_evaluator import ExactMatchEvaluator
from app.evaluators.keyword_evaluator import KeywordEvaluator
from app.evaluators.llm_judge_evaluator import LLMJudgeEvaluator
from app.evaluators.semantic_similarity_evaluator import (
    SemanticSimilarityEvaluator,
)
from app.reports.html_report_generator import HtmlReportGenerator
from app.reports.json_report_generator import JsonReportGenerator


def main() -> None:
    args = parse_arguments()

    dataset_path = f"data/test_sets/{args.dataset}.json"

    loader = DatasetLoader()
    cases = loader.load(dataset_path)

    connector = OllamaConnector(
        model=args.model,
    )

    embedding_provider = OllamaEmbeddingProvider(
        model_name="embeddinggemma",
    )

    evaluators = [
        KeywordEvaluator(),
        ExactMatchEvaluator(),
        SemanticSimilarityEvaluator(
            embedding_provider=embedding_provider,
        ),
        LLMJudgeEvaluator(
            connector=connector,
        ),
    ]

    runner = AuditRunner(
        connector=connector,
        evaluators=evaluators,
    )

    report_results: list[dict[str, Any]] = []

    for case in cases:
        print("\n" + "=" * 60)
        print(f"Test Name : {case.test.name}")
        print(f"Category  : {case.test.category}")
        print(f"Prompt    : {case.test.prompt}")
        print("=" * 60)

        audit_run = runner.run(
            test=case.test,
            context=case.context,
        )

        print(f"\nModel     : {audit_run.model_name}")
        print(f"Response  : {audit_run.response.text}")
        print(f"Latency   : {audit_run.response.latency_ms:.2f} ms")

        evaluator_results: dict[str, dict[str, Any]] = {}

        for evaluator_name, result in audit_run.result.results.items():
            print("\n" + "-" * 50)
            print(f"Evaluator : {evaluator_name}")
            print(f"Passed    : {result.passed}")
            print(f"Score     : {result.score}")
            print(f"Findings  : {result.findings}")

            evaluator_results[evaluator_name] = {
                "passed": result.passed,
                "score": result.score,
                "findings": result.findings,
            }

        report_results.append(
            {
                "test_name": case.test.name,
                "category": case.test.category,
                "prompt": case.test.prompt,
                "model": audit_run.model_name,
                "response": audit_run.response.text,
                "latency_ms": audit_run.response.latency_ms,
                "evaluators": evaluator_results,
            }
        )

    report: dict[str, Any] = {
        "model": connector.model,
        "dataset": args.dataset,
        "total_tests": len(report_results),
        "results": report_results,
    }

    json_report_generator = JsonReportGenerator()
    json_output_file = json_report_generator.generate(report)

    html_report_generator = HtmlReportGenerator()
    html_output_file = html_report_generator.generate(report)

    print("\n" + "=" * 60)
    print("All dataset tests completed.")
    print(f"JSON report saved to: {json_output_file}")
    print(f"HTML report saved to: {html_output_file}")
    print("=" * 60)

    webbrowser.open(html_output_file.resolve().as_uri())


if __name__ == "__main__":
    main()