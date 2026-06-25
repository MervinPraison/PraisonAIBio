# Toolsets

Toolsets are named bundles of tools for agents and YAML workflows.

!!! important
    Run `python -c "import praisonai_bio"` before using toolsets in YAML or CLI.

---

## Toolsets

| Toolset | Use when |
|---------|----------|
| `biomodels-readonly` | Search and metadata only (safe) |
| `sbml_analysis` | Load and summarise SBML |
| `sysbio-core` | Discovery + basic simulation |
| `simulation` | Run models (needs BASICO) |
| `reporting` | Compare and report |
| `sysbio-full` | All 21 tools |
| `sysbio-orchestrator` | Multi-step discovery agent |
| `sysbio-safe` | Read-only, no writes or simulation |
| `repro` | Reproducibility bundles |
| `genomics-bridge` | v2 stub — ClawBio genomics bridge (empty until external tools registered) |

---

## Python

```python
import praisonai_bio
from praisonaiagents import Agent

agent = Agent(
    name="scout",
    toolsets=["biomodels-readonly"],
    llm="gpt-4o-mini",
)
agent.start("Find curated MAPK models")
```

---

## YAML

```yaml
agents:
  scout:
    role: BioModels Scout
    toolsets:
      - biomodels-readonly
```

---

## Tools in `sysbio-full`

**T2B (11):** search_models, get_modelinfo, load_biomodel, simulate_model, ask_question, steady_state, parameter_scan, custom_plotter, get_annotation, query_article, save_model

**Discovery:** rank_models, trust_scorecard, compare_models, preview_outcomes, sbml_summarise, sbml_validate, sedml_parse, simulate_perturbation, compare_simulations, repro_export

Details: [Tools at a glance](tools-at-a-glance.md) · [Tools reference](tools-reference.md)
