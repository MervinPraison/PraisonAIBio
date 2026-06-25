"""T2B parity benchmark scorer."""

from __future__ import annotations

import json
from pathlib import Path

from praisonai_bio.eval.t2b_scorer import tool_selection_score


def score_case(case: dict, tool_used: str) -> dict:
    expected = case.get("expected_tool", "")
    return {
        "case": case.get("id"),
        "score": tool_selection_score(expected, tool_used),
        "expected": expected,
        "actual": tool_used,
    }


def main() -> None:
    cases_dir = Path(__file__).parent / "cases"
    results = []
    for path in sorted(cases_dir.glob("*.json")):
        case = json.loads(path.read_text(encoding="utf-8"))
        results.append(score_case(case, case.get("mock_tool", case.get("expected_tool", ""))))
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
