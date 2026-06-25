# Minimal examples

Two lines each. `import praisonai_bio` registers all tools.

```bash
pip install -e "src/praisonai-bio"
```

| Run | Does |
|-----|------|
| `python examples/minimal/search.py` | Find models |
| `python examples/minimal/info.py` | One model’s details |
| `python examples/minimal/trust.py` | Curation score |
| `python examples/minimal/validate.py` | Check SBML |
| `python examples/minimal/graph.py` | Reaction map |
| `python examples/minimal/compare_models.py` | Two models side by side |
| `python examples/minimal/compare_runs.py` | Two sim outputs *(offline)* |
| `python examples/minimal/export.py` | Repro bundle → `/tmp/glycolysis_bundle` |
| `python examples/minimal/simulate.py` | Short simulation *(needs BASICO)* |
| `python examples/minimal/perturb.py` | Change one parameter *(BASICO)* |
| `python examples/minimal/agent.py` | AI search *(needs OPENAI_API_KEY)* |
| `python examples/minimal/agent_simulate.py` | AI simulation *(API key + BASICO)* |

Demo model: **BIOMD0000000206** (yeast glycolysis).
