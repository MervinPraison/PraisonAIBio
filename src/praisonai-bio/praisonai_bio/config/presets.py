"""Agent presets for discovery, simulation, and orchestration workflows."""

from __future__ import annotations

from typing import Any

try:
    from praisonaiagents import ExecutionConfig, GuardrailConfig, MemoryConfig
except ImportError:  # pragma: no cover - older praisonaiagents
    MemoryConfig = GuardrailConfig = ExecutionConfig = None  # type: ignore[misc, assignment]

from praisonai_bio.guardrails.simulation_output import validate_simulation_output


def _memory(**kwargs: Any) -> Any:
    if MemoryConfig is None:
        return True
    return MemoryConfig(**kwargs)


def _guardrails(**kwargs: Any) -> Any:
    if GuardrailConfig is None:
        return None
    return GuardrailConfig(**kwargs)


def _execution(**kwargs: Any) -> Any:
    if ExecutionConfig is None:
        return None
    return ExecutionConfig(**kwargs)


DISCOVERY_AGENT: dict[str, Any] = {
    "name": "discovery-agent",
    "instructions": (
        "You are a systems biology discovery agent. Search BioModels.org, rank models, "
        "produce trust scorecards, and summarise SBML structure. Prefer curated models."
    ),
    "memory": _memory(backend="file", auto_save="biomodels-discovery", history=True, history_limit=15),
    "guardrails": _guardrails(policies=["policy:bio-public"], max_retries=2),
    "execution": _execution(max_iter=25, max_tool_calls_per_turn=8, context_compaction=False),
}

SIMULATION_AGENT: dict[str, Any] = {
    "name": "simulation-agent",
    "instructions": (
        "You are a simulation engineer. Load SBML models, run time-course simulations, "
        "steady-state analysis, and parameter scans. Report dynamics clearly."
    ),
    "memory": _memory(backend="file", auto_save="biomodels-simulation"),
    "guardrails": (
        validate_simulation_output
        if GuardrailConfig is None
        else GuardrailConfig(
            validator=validate_simulation_output,
            policies=["policy:bio-lab"],
            max_retries=1,
        )
    ),
    "execution": _execution(max_iter=30, max_tool_calls_per_turn=6, code_execution=False),
}

ORCHESTRATOR_AGENT: dict[str, Any] = {
    "name": "orchestrator-agent",
    "instructions": (
        "You coordinate multi-step BioModels workflows: discovery, validation, simulation, "
        "and reporting. Delegate via toolsets and keep a concise audit trail."
    ),
    "memory": _memory(backend="file", auto_save="biomodels-orchestrator", history=True, history_limit=20),
    "guardrails": _guardrails(policies=["policy:bio-public"], max_retries=2),
    "execution": _execution(max_iter=40, max_tool_calls_per_turn=10, context_compaction=False),
}
