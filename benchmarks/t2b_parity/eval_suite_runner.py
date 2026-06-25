"""Deterministic EvalSuite-style runner for T2B tool-selection parity."""

from __future__ import annotations

import json
from pathlib import Path

from praisonai_bio.eval.t2b_scorer import score_case


def load_cases(limit: int | None = None) -> list[dict]:
    cases_dir = Path(__file__).parent / "cases"
    extra = Path(__file__).parent.parent / "t2b_312" / "cases"
    paths = sorted(cases_dir.glob("[0-9]*.json"))
    if extra.exists():
        paths.extend(sorted(extra.glob("*.json")))
    cases = [json.loads(p.read_text(encoding="utf-8")) for p in paths]
    return cases[:limit] if limit else cases


def run_deterministic_suite() -> dict:
    """Score prompt routing without calling an LLM."""
    scores = []
    for case in load_cases():
        result = score_case(case)
        scores.append({"id": case.get("id"), "score": result["score"], "actual": result["actual"]})
    mean = sum(s["score"] for s in scores) / len(scores) if scores else 0.0
    return {"cases": len(scores), "mean_score": mean, "scores": scores}


def run_eval_suite_agentic() -> dict:
    """Optional LLM path using SDK ReliabilityEvaluator when OPENAI_API_KEY is set."""
    import os

    if not os.environ.get("OPENAI_API_KEY"):
        return {"skipped": True, "reason": "OPENAI_API_KEY not set"}
    try:
        import praisonai_bio  # noqa: F401
        from praisonaiagents import Agent
        from praisonaiagents.eval import EvalSuite, ReliabilityEvaluator
    except ImportError as exc:
        return {"skipped": True, "reason": str(exc)}

    suite = EvalSuite(name="t2b-parity")
    for case in load_cases(limit=3):
        agent = Agent(
            name="t2b-eval",
            instructions="Call exactly one BioModels tool.",
            toolsets=["sysbio-full"],
            model="gpt-4o-mini",
        )
        suite.add(
            ReliabilityEvaluator(
                agent=agent,
                input_text=case["prompt"],
                expected_tools=[case["expected_tool"]],
                name=case["id"],
            )
        )
    result = suite.run(print_summary=False)
    return {"skipped": False, "overall_score": result.overall_score}


def main() -> None:
    report = run_deterministic_suite()
    print(json.dumps(report, indent=2))
    if report["mean_score"] < 0.9:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
