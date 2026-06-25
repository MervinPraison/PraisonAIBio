# Tools reference

All 21 tools with **parameters agents can use**. Provide every option explicitly in prompts or YAML — agents do not read env vars or config files.

!!! tip
    Run `python -c "import praisonai_bio"` before calling tools from agents or workflows.

---

## Discovery (read-only)

| Tool | Parameters | Returns |
|------|------------|---------|
| **search_models** | `query` (str), `num_results` (int, default 10), `offset` (int, default 0), `curated_only` (bool, default true) | JSON list of matching models |
| **get_modelinfo** | `model_id` (str, e.g. `BIOMD0000000206`) | Name, authors, description |
| **rank_models** | `query` (str), `num_results` (int, default 10), `research_question` (str, optional) | Ranked models with scores |
| **trust_scorecard** | `model_id` (str) | Curation score and reasons |
| **compare_models** | `model_id_a` (str), `model_id_b` (str) | Side-by-side metadata |
| **get_annotation** | `model_id` (str) | MIRIAM / RDF annotations |
| **query_article** | `model_id` (str) | DOI, PubMed, citation links |
| **ask_question** | `model_id` (str), `question` (str) | Metadata-grounded answer text |
| **sbml_summarise** | `model_id` (str) | Species, compartments, reactions summary |
| **sbml_validate** | `model_id` (str, optional), `sbml_path` (str, optional) — one required | Validation report (structure, units) |
| **sedml_parse** | `model_id` (str), `filename` (str, optional SED-ML file in bundle) | SED-ML tasks and data generators |

---

## Simulation (needs `pip install praisonai-bio[simulation]`)

| Tool | Parameters | Returns |
|------|------------|---------|
| **load_biomodel** | `model_id` (str), `save_path` (str, optional) | Path to downloaded SBML |
| **simulate_model** | `model_id` (str, optional), `sbml_path` (str, optional), `duration` (float, default 100), `step` (float, default 0.1) | Time-course JSON preview |
| **steady_state** | `model_id` (str, optional), `sbml_path` (str, optional) | Steady-state concentrations |
| **parameter_scan** | `model_id` (str), `parameter` (str), `start` (float), `end` (float), `steps` (int, default 10) | Scan table JSON |
| **preview_outcomes** | `model_id` (str), `duration` (float, default 50) | Short baseline simulation |
| **simulate_perturbation** | `model_id` (str), `parameter` (str), `value` (float), `duration` (float, default 100) | Perturbed time-course JSON |
| **custom_plotter** | `data_json` (str), `x_column` (str), `y_column` (str), `title` (str, default `"Simulation plot"`), `output_path` (str, default `plot.png`) | PNG path (needs `[plot]`) |

---

## Reporting & reproducibility

| Tool | Parameters | Returns |
|------|------------|---------|
| **compare_simulations** | `baseline_json` (str), `perturbation_json` (str) | Comparison summary JSON |
| **save_model** | `model_id` (str), `output_path` (str) | Saved SBML path |
| **repro_export** | `model_id` (str), `output_dir` (str), `run_id` (str, optional) | Bundle dir with SBML, metadata, `commands.sh`, checksums |

---

## Python example

```python
import praisonai_bio
from praisonai_bio.tools.search_models import search_models
from praisonai_bio.tools.sbml_validate import sbml_validate

print(search_models.run(query="glycolysis", num_results=5))
print(sbml_validate.run(model_id="BIOMD0000000206"))
```

---

## See also

- [Tools at a glance](tools-at-a-glance.md) — plain-language summary
- [Toolsets](toolsets.md) — named bundles for agents
- [Quick tasks](quick-tasks.md) — copy-paste commands
