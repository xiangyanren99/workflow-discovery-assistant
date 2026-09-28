import json
from pathlib import Path

from app.analyzer import analyze_workflow
from tests.evaluation_cases import EVALUATION_CASES

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RESULTS_DIR = PROJECT_ROOT / "evaluations"
RESULTS_PATH = RESULTS_DIR / "baseline-results.json"


def run_evaluations() -> list[dict]:
    results = []

    for test_case in EVALUATION_CASES:
        print(f"Running {test_case['id']}: {test_case['name']}...")

        try:
            analysis = analyze_workflow(test_case["notes"])

            results.append(
                {
                    "id": test_case["id"],
                    "name": test_case["name"],
                    "status": "SUCCESS",
                    "analysis": analysis.model_dump(),
                }
            )

            print("  SUCCESS")

        except Exception as error:
            results.append(
                {
                    "id": test_case["id"],
                    "name": test_case["name"],
                    "status": "ERROR",
                    "error": str(error),
                }
            )

            print(f"  ERROR: {error}")

    return results


def save_results(results: list[dict]) -> None:
    RESULTS_DIR.mkdir(exist_ok=True)

    RESULTS_PATH.write_text(
        json.dumps(results, indent=2),
        encoding="utf-8",
    )

    print(f"\nResults saved to: {RESULTS_PATH}")


if __name__ == "__main__":
    evaluation_results = run_evaluations()
    save_results(evaluation_results)