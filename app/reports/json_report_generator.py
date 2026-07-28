import json
from datetime import datetime
from pathlib import Path
from typing import Any


class JsonReportGenerator:
    """Builds audit summaries and saves reports as JSON files."""

    def build_summary(
        self,
        report: dict[str, Any],
    ) -> dict[str, int | float]:
        results = report["results"]
        total_tests = len(results)

        tests_passed = 0
        tests_failed = 0
        evaluator_passes = 0
        evaluator_failures = 0

        total_score = 0.0
        total_latency = 0.0

        for result in results:
            total_latency += result["latency_ms"]

            evaluator_scores: list[float] = []
            all_passed = True

            for evaluator in result["evaluators"].values():
                evaluator_scores.append(evaluator["score"])

                if evaluator["passed"]:
                    evaluator_passes += 1
                else:
                    evaluator_failures += 1
                    all_passed = False

            if evaluator_scores:
                average_test_score = sum(evaluator_scores) / len(
                    evaluator_scores
                )
                total_score += average_test_score

            if all_passed:
                tests_passed += 1
            else:
                tests_failed += 1

        average_score = (
            round(total_score / total_tests, 3)
            if total_tests
            else 0.0
        )

        average_latency_ms = (
            round(total_latency / total_tests, 2)
            if total_tests
            else 0.0
        )

        return {
            "total_tests": total_tests,
            "tests_passed": tests_passed,
            "tests_failed": tests_failed,
            "evaluator_checks": evaluator_passes + evaluator_failures,
            "evaluator_passes": evaluator_passes,
            "evaluator_failures": evaluator_failures,
            "average_score": average_score,
            "average_latency_ms": average_latency_ms,
        }

    def generate(
        self,
        report: dict[str, Any],
    ) -> Path:
        report["summary"] = self.build_summary(report)

        output_directory = Path("data/generated_reports")
        output_directory.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = output_directory / f"audit_report_{timestamp}.json"

        with output_file.open("w", encoding="utf-8") as file:
            json.dump(report, file, indent=4)

        return output_file