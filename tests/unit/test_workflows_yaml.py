"""Parse all workflow YAML files under workflows/."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
WORKFLOWS = ROOT / "workflows"


def _collect_yaml_paths() -> list[Path]:
    return sorted(WORKFLOWS.rglob("*.yaml"))


def test_all_workflow_yaml_parseable():
    paths = _collect_yaml_paths()
    assert paths, "no workflow yaml files found"
    for path in paths:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert data is not None, path.name


def test_discovery_pipeline_has_domain_route():
    path = WORKFLOWS / "discovery" / "biomodels_discovery_pipeline.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    steps = data.get("steps", [])
    route_steps = [s for s in steps if isinstance(s, dict) and "route" in s]
    assert route_steps, "domain_route step missing"
    scouts_after_route = [
        s for s in steps
        if isinstance(s, dict) and s.get("agent") in {"pathway_scout", "disease_scout", "general_scout"}
        and "route" not in s
    ]
    assert not scouts_after_route, "duplicate scout steps after route"


def test_full_platform_pipeline_exists():
    path = WORKFLOWS / "cookbooks" / "full_platform_pipeline.yaml"
    assert path.exists()
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert "scout" in data.get("agents", {})
