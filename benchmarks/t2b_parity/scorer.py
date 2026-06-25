"""T2B parity benchmark scorer."""

from __future__ import annotations

import json
from pathlib import Path

from praisonai_bio.eval.t2b_scorer import score_case


def main() -> None:
    cases_dir = Path(__file__).parent / "cases"
    results = []
    for path in sorted(cases_dir.glob("*.json")):
        case = json.loads(path.read_text(encoding="utf-8"))
        actual = case.get("actual_tool")
        results.append(score_case(case, tool_used=actual))
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
