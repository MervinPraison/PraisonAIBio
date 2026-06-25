"""Register PraisonAIBio hooks with the PraisonAI hook system."""

from __future__ import annotations

_wired = False


def wire_bio_hooks() -> None:
    """Attach before_tool and after_tool hooks for BioModels workflows."""
    global _wired
    if _wired:
        return

    from praisonaiagents.hooks import add_hook

    from praisonai_bio.hooks.biomodels_hooks import log_biomodels_call
    from praisonai_bio.hooks.policy_gate import bio_policy_gate
    from praisonai_bio.hooks.simulation_hooks import after_simulation, approval_gate, before_simulation

    add_hook("before_tool", bio_policy_gate)
    add_hook("before_tool", approval_gate, matcher="parameter_scan|simulate_perturbation")
    add_hook("before_tool", before_simulation, matcher="simulate_model|simulate_perturbation|sedml_simulate")
    add_hook("after_tool", log_biomodels_call)
    add_hook("after_tool", after_simulation, matcher="simulate_model|simulate_perturbation|sedml_simulate")
    _wired = True
