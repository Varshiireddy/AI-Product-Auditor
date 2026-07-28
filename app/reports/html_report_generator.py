from datetime import datetime
from html import escape
from pathlib import Path


class HtmlReportGenerator:
    def generate(self, report: dict) -> Path:
        output_dir = Path("data/generated_reports")
        output_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = output_dir / f"audit_report_{timestamp}.html"

        summary = report["summary"]

        result_cards = self._build_result_cards(report["results"])

        html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >
    <title>AI Product Auditor Report</title>

    <style>
        * {{
            box-sizing: border-box;
        }}

        body {{
            margin: 0;
            padding: 40px 20px;
            background: #f4f6f8;
            color: #1f2937;
            font-family: Arial, sans-serif;
        }}

        .container {{
            max-width: 1100px;
            margin: 0 auto;
        }}

        h1 {{
            margin-bottom: 8px;
        }}

        .subtitle {{
            margin-top: 0;
            color: #6b7280;
        }}

        .summary-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 16px;
            margin: 30px 0;
        }}

        .summary-card {{
            background: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
        }}

        .summary-label {{
            color: #6b7280;
            font-size: 14px;
            margin-bottom: 8px;
        }}

        .summary-value {{
            font-size: 24px;
            font-weight: bold;
        }}

        .test-card {{
            background: white;
            margin-bottom: 24px;
            padding: 24px;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
        }}

        .test-header {{
            display: flex;
            justify-content: space-between;
            gap: 20px;
            align-items: center;
        }}

        .status {{
            display: inline-block;
            padding: 6px 12px;
            border-radius: 999px;
            font-weight: bold;
            font-size: 14px;
        }}

        .pass {{
            color: #166534;
            background: #dcfce7;
        }}

        .fail {{
            color: #991b1b;
            background: #fee2e2;
        }}

        .section {{
            margin-top: 18px;
        }}

        .section-title {{
            color: #6b7280;
            font-size: 13px;
            font-weight: bold;
            text-transform: uppercase;
            margin-bottom: 6px;
        }}

        .content-box {{
            background: #f9fafb;
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            padding: 14px;
            line-height: 1.5;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 12px;
        }}

        th,
        td {{
            border-bottom: 1px solid #e5e7eb;
            padding: 12px;
            text-align: left;
            vertical-align: top;
        }}

        th {{
            background: #f9fafb;
        }}

        .score {{
            font-weight: bold;
        }}

        .meta {{
            color: #6b7280;
            font-size: 14px;
        }}
    </style>
</head>

<body>
    <div class="container">
        <h1>AI Product Auditor Report</h1>

        <p class="subtitle">
            Model: {escape(str(report["model"]))}
            |
            Dataset: {escape(str(report["dataset"]))}
        </p>

        <div class="summary-grid">
            <div class="summary-card">
                <div class="summary-label">Total Tests</div>
                <div class="summary-value">
                    {summary["total_tests"]}
                </div>
            </div>

            <div class="summary-card">
                <div class="summary-label">Tests Passed</div>
                <div class="summary-value">
                    {summary["tests_passed"]}
                </div>
            </div>

            <div class="summary-card">
                <div class="summary-label">Tests Failed</div>
                <div class="summary-value">
                    {summary["tests_failed"]}
                </div>
            </div>

            <div class="summary-card">
                <div class="summary-label">Average Score</div>
                <div class="summary-value">
                    {summary["average_score"]}
                </div>
            </div>

            <div class="summary-card">
                <div class="summary-label">Average Latency</div>
                <div class="summary-value">
                    {summary["average_latency_ms"]:.2f} ms
                </div>
            </div>

            <div class="summary-card">
                <div class="summary-label">Evaluator Checks</div>
                <div class="summary-value">
                    {summary["evaluator_checks"]}
                </div>
            </div>
        </div>

        <h2>Detailed Results</h2>

        {result_cards}
    </div>
</body>
</html>
"""

        with output_file.open("w", encoding="utf-8") as file:
            file.write(html)

        return output_file

    def _build_result_cards(self, results: list[dict]) -> str:
        cards = []

        for result in results:
            evaluators = result["evaluators"]
            test_passed = all(
                evaluator["passed"]
                for evaluator in evaluators.values()
            )

            status_text = "PASS" if test_passed else "FAIL"
            status_class = "pass" if test_passed else "fail"

            evaluator_rows = self._build_evaluator_rows(evaluators)

            card = f"""
<div class="test-card">
    <div class="test-header">
        <div>
            <h3>{escape(str(result["test_name"]))}</h3>
            <div class="meta">
                Category: {escape(str(result["category"]))}
                |
                Latency: {result["latency_ms"]:.2f} ms
            </div>
        </div>

        <span class="status {status_class}">
            {status_text}
        </span>
    </div>

    <div class="section">
        <div class="section-title">Prompt</div>
        <div class="content-box">
            {escape(str(result["prompt"]))}
        </div>
    </div>

    <div class="section">
        <div class="section-title">Model Response</div>
        <div class="content-box">
            {escape(str(result["response"]))}
        </div>
    </div>

    <div class="section">
        <div class="section-title">Evaluator Results</div>

        <table>
            <thead>
                <tr>
                    <th>Evaluator</th>
                    <th>Status</th>
                    <th>Score</th>
                    <th>Findings</th>
                </tr>
            </thead>

            <tbody>
                {evaluator_rows}
            </tbody>
        </table>
    </div>
</div>
"""
            cards.append(card)

        return "\n".join(cards)

    def _build_evaluator_rows(self, evaluators: dict) -> str:
        rows = []

        for evaluator_name, evaluator in evaluators.items():
            passed = evaluator["passed"]
            status_text = "PASS" if passed else "FAIL"
            status_class = "pass" if passed else "fail"

            findings = evaluator["findings"]

            if isinstance(findings, list):
                findings_text = ", ".join(str(item) for item in findings)
            else:
                findings_text = str(findings)

            row = f"""
<tr>
    <td>{escape(str(evaluator_name))}</td>
    <td>
        <span class="status {status_class}">
            {status_text}
        </span>
    </td>
    <td class="score">
        {float(evaluator["score"]):.3f}
    </td>
    <td>{escape(findings_text)}</td>
</tr>
"""
            rows.append(row)

        return "\n".join(rows)