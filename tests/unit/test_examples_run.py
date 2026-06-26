"""Smoke-run every repository example script."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]

OFFLINE = {
    "examples/small/08_compare_sims.py",
    "examples/minimal/compare_runs.py",
}

NETWORK = {
    "examples/small/01_search.py",
    "examples/small/02_model_info.py",
    "examples/small/03_trust_score.py",
    "examples/small/04_validate_sbml.py",
    "examples/small/07_compare_models.py",
    "examples/small/09_repro_export.py",
    "examples/small/10_sbml_graph.py",
    "examples/minimal/search.py",
    "examples/minimal/info.py",
    "examples/minimal/trust.py",
    "examples/minimal/validate.py",
    "examples/minimal/graph.py",
    "examples/minimal/compare_models.py",
    "examples/minimal/export.py",
}

BASICO = {
    "examples/small/05_simulate.py",
    "examples/small/06_perturb.py",
    "examples/minimal/simulate.py",
    "examples/minimal/perturb.py",
}

AGENT = {
    "examples/minimal/agent.py",
    "examples/minimal/agent_simulate.py",
    "examples/big/01_find_models.py",
    "examples/big/02_summarise_model.py",
    "examples/big/03_discovery_study.py",
    "examples/big/04_glycolysis_demo.py",
    "examples/big/05_perturb_compare.py",
    "examples/big/06_full_repro_study.py",
    "examples/big/07_agent_with_configs.py",
    "examples/python/team_model_review.py",
}

MCP = {"examples/mcp/sysbio_client.py"}

ALL_EXAMPLES = sorted(OFFLINE | NETWORK | BASICO | AGENT | MCP)


def _skip_reason(rel: str) -> str | None:
    if rel in OFFLINE:
        return None
    if os.environ.get("SKIP_NETWORK") == "1" and rel not in OFFLINE:
        return "SKIP_NETWORK=1"
    if rel in BASICO:
        from praisonai_bio.adapters.basico_adapter import check_basico_available

        ok, _ = check_basico_available()
        if not ok:
            return "BASICO not installed"
    if rel in AGENT | MCP:
        if not os.environ.get("OPENAI_API_KEY"):
            return "OPENAI_API_KEY not set"
    if rel in MCP and not shutil.which("praisonai-bio-mcp"):
        return "praisonai-bio-mcp not on PATH"
    return None


def _timeout(rel: str) -> int:
    if rel.startswith("examples/python/"):
        return 300
    if rel.startswith("examples/big/"):
        return 180
    if rel.startswith("examples/mcp/"):
        return 120
    return 90


@pytest.fixture(autouse=True)
def _import_bio():
    import praisonai_bio  # noqa: F401


@pytest.mark.parametrize("rel", ALL_EXAMPLES)
def test_example_runs(rel: str):
    reason = _skip_reason(rel)
    if reason:
        pytest.skip(reason)

    script = ROOT / rel
    assert script.is_file(), rel

    env = os.environ.copy()
    env["PYTHONPATH"] = f"{ROOT / 'src' / 'praisonai-bio'}{os.pathsep}{env.get('PYTHONPATH', '')}"
    env["PYTHONWARNINGS"] = "ignore"

    proc = subprocess.run(
        [sys.executable, str(script)],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
        timeout=_timeout(rel),
    )
    assert proc.returncode == 0, f"{rel} failed:\n{proc.stderr[-2000:]}"
    assert proc.stdout.strip(), f"{rel} produced no stdout"
