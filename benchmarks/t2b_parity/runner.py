"""Agentic T2B parity benchmark runner."""

from __future__ import annotations

import json
import os
from pathlib import Path

import pytest


def run_agentic_case(prompt: str, toolset: str = "sysbio-full") -> str:
    import praisonai_bio  # noqa: F401
    from praisonaiagents import Agent

    agent = Agent(
        name="t2b-benchmark",
        instructions="Use BioModels tools. Be concise.",
        llm="gpt-4o-mini",
        toolsets=[toolset],
    )
    return str(agent.start(prompt))


def main() -> None:
    if not os.environ.get("OPENAI_API_KEY"):
        print("SKIP — set OPENAI_API_KEY for agentic benchmark")
        return
    cases_dir = Path(__file__).parent / "cases"
    for path in sorted(cases_dir.glob("*.json"))[:3]:
        case = json.loads(path.read_text(encoding="utf-8"))
        print(f"Running {case['id']}...")
        print(run_agentic_case(case["prompt"]))


if __name__ == "__main__":
    main()
