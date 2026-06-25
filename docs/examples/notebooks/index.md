# Notebooks

Jupyter notebooks for interactive systems biology workflows.

| Notebook | Topic |
|----------|-------|
| [01_search_rank.ipynb](../../examples/notebooks/01_search_rank.ipynb) | Search and rank BioModels |
| [02_sbml_graph.ipynb](../../examples/notebooks/02_sbml_graph.ipynb) | SBML summarise and reaction graph |
| [03_simulate_glycolysis.ipynb](../../examples/notebooks/03_simulate_glycolysis.ipynb) | Baseline simulation (BASICO) |
| [04_perturb_compare.ipynb](../../examples/notebooks/04_perturb_compare.ipynb) | Perturbation and comparison |
| [05_repro_bundle.ipynb](../../examples/notebooks/05_repro_bundle.ipynb) | Repro bundle export |

Convert a notebook to repro metadata:

```bash
python scripts/notebook_to_repro.py examples/notebooks/05_repro_bundle.ipynb
```
