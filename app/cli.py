import argparse


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="AI Product Auditor",
    )

    parser.add_argument(
        "--dataset",
        default="factuality",
        help="Dataset name (without .json)",
    )

    parser.add_argument(
        "--model",
        default="qwen2.5:3b",
        help="Ollama model name",
    )

    return parser.parse_args()