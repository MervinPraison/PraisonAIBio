#!/usr/bin/env python3
"""Generate example doc pages with embedded tested output snippets."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAGES = [
    {
        "md": "docs/examples/small/01-search.md",
        "title": "Search BioModels",
        "cat": "Small (no AI)",
        "script": "examples/small/01_search.py",
        "minimal": "examples/minimal/search.py",
        "desc": "Search curated glycolysis models on BioModels.org.",
        "run": "python examples/small/01_search.py",
        "needs": "Internet. No API key.",
        "out": "docs/examples/small/01-search/output.txt",
    },
    {
        "md": "docs/examples/small/02-model-info.md",
        "title": "Model metadata",
        "cat": "Small (no AI)",
        "script": "examples/small/02_model_info.py",
        "minimal": "examples/minimal/info.py",
        "desc": "Metadata for **BIOMD0000000206** (Teusink / Wolf glycolysis).",
        "run": "python examples/small/02_model_info.py",
        "needs": "Internet.",
        "out": "docs/examples/small/02-model-info/output.txt",
    },
    {
        "md": "docs/examples/small/03-trust-score.md",
        "title": "Trust scorecard",
        "cat": "Small (no AI)",
        "script": "examples/small/03_trust_score.py",
        "minimal": "examples/minimal/trust.py",
        "desc": "Curation trust check for **BIOMD0000000206**.",
        "run": "python examples/small/03_trust_score.py",
        "needs": "Internet.",
        "out": "docs/examples/small/03-trust-score/output.txt",
    },
    {
        "md": "docs/examples/small/04-validate-sbml.md",
        "title": "Validate SBML",
        "cat": "Small (no AI)",
        "script": "examples/small/04_validate_sbml.py",
        "minimal": "examples/minimal/validate.py",
        "desc": "Check SBML structure for **BIOMD0000000206**.",
        "run": "python examples/small/04_validate_sbml.py",
        "needs": "Internet.",
        "out": "docs/examples/small/04-validate-sbml/output.txt",
    },
    {
        "md": "docs/examples/small/05-simulate.md",
        "title": "Simulate",
        "cat": "Small (no AI)",
        "script": "examples/small/05_simulate.py",
        "minimal": "examples/minimal/simulate.py",
        "desc": "10 time-unit baseline simulation of **BIOMD0000000206**.",
        "run": "python examples/small/05_simulate.py",
        "needs": "Internet + BASICO (`pip install -e \"src/praisonai-bio[simulation]\"`).",
        "out": "docs/examples/small/05-simulate/output.txt",
    },
    {
        "md": "docs/examples/small/06-perturb.md",
        "title": "Perturb parameter",
        "cat": "Small (no AI)",
        "script": "examples/small/06_perturb.py",
        "minimal": "examples/minimal/perturb.py",
        "desc": "Change **vGAPD** and re-simulate **BIOMD0000000206**.",
        "run": "python examples/small/06_perturb.py",
        "needs": "Internet + BASICO.",
        "out": "docs/examples/small/06-perturb/output.txt",
    },
    {
        "md": "docs/examples/small/07-compare-models.md",
        "title": "Compare models",
        "cat": "Small (no AI)",
        "script": "examples/small/07_compare_models.py",
        "minimal": "examples/minimal/compare_models.py",
        "desc": "Compare **BIOMD0000000206** vs **BIOMD0000000064**.",
        "run": "python examples/small/07_compare_models.py",
        "needs": "Internet.",
        "out": "docs/examples/small/07-compare-models/output.txt",
    },
    {
        "md": "docs/examples/small/08-compare-sims.md",
        "title": "Compare simulations",
        "cat": "Small (no AI)",
        "script": "examples/small/08_compare_sims.py",
        "minimal": "examples/minimal/compare_runs.py",
        "desc": "Compare two simulation outputs (RMSE, AUC). **Works offline.**",
        "run": "python examples/small/08_compare_sims.py",
        "needs": "None — offline.",
        "out": "docs/examples/small/08-compare-sims/output.txt",
    },
    {
        "md": "docs/examples/small/09-repro-export.md",
        "title": "Repro export",
        "cat": "Small (no AI)",
        "script": "examples/small/09_repro_export.py",
        "minimal": "examples/minimal/export.py",
        "desc": "Export repro bundle to `/tmp/glycolysis_bundle`.",
        "run": "python examples/small/09_repro_export.py",
        "needs": "Internet.",
        "out": "docs/examples/small/09-repro-export/output.txt",
    },
    {
        "md": "docs/examples/small/10-sbml-graph.md",
        "title": "SBML reaction graph",
        "cat": "Small (no AI)",
        "script": "examples/small/10_sbml_graph.py",
        "minimal": "examples/minimal/graph.py",
        "desc": "Reaction map for **BIOMD0000000206**.",
        "run": "python examples/small/10_sbml_graph.py",
        "needs": "Internet.",
        "out": "docs/examples/small/10-sbml-graph/output.txt",
    },
    {
        "md": "docs/examples/big/01-find-models.md",
        "title": "Agent finds models",
        "cat": "Big (AI agent)",
        "script": "examples/big/01_find_models.py",
        "minimal": "examples/minimal/agent.py",
        "desc": "Agent searches BioModels for curated yeast glycolysis models.",
        "run": "export OPENAI_API_KEY=sk-...\npython examples/big/01_find_models.py",
        "needs": "Internet + OpenAI API key.",
        "out": "docs/examples/big/01-find-models/output.txt",
    },
    {
        "md": "docs/examples/big/02-summarise-model.md",
        "title": "Agent summarises model",
        "cat": "Big (AI agent)",
        "script": "examples/big/02_summarise_model.py",
        "desc": "Plain-English summary of **BIOMD0000000206**.",
        "run": "export OPENAI_API_KEY=sk-...\npython examples/big/02_summarise_model.py",
        "needs": "Internet + OpenAI API key.",
        "out": "docs/examples/big/02-summarise-model/output.txt",
    },
    {
        "md": "docs/examples/big/03-discovery-study.md",
        "title": "Discovery study",
        "cat": "Big (AI agent)",
        "script": "examples/big/03_discovery_study.py",
        "desc": "Agent picks the best curated MAPK model.",
        "run": "export OPENAI_API_KEY=sk-...\npython examples/big/03_discovery_study.py",
        "needs": "Internet + OpenAI API key.",
        "out": "docs/examples/big/03-discovery-study/output.txt",
    },
    {
        "md": "docs/examples/big/04-glycolysis-demo.md",
        "title": "Glycolysis demo",
        "cat": "Big (AI agent)",
        "script": "examples/big/04_glycolysis_demo.py",
        "desc": "Summarise and simulate **BIOMD0000000206** in one agent run.",
        "run": "export OPENAI_API_KEY=sk-...\npython examples/big/04_glycolysis_demo.py",
        "needs": "Internet + OpenAI API key + BASICO for simulation.",
        "out": "docs/examples/big/04-glycolysis-demo/output.txt",
    },
    {
        "md": "docs/examples/big/05-perturb-compare.md",
        "title": "Perturb and compare",
        "cat": "Big (AI agent)",
        "script": "examples/big/05_perturb_compare.py",
        "desc": "Agent compares baseline vs perturbed simulation for **BIOMD0000000206**.",
        "run": "export OPENAI_API_KEY=sk-...\npython examples/big/05_perturb_compare.py",
        "needs": "Internet + OpenAI API key + BASICO.",
        "out": "docs/examples/big/05-perturb-compare/output.txt",
    },
    {
        "md": "docs/examples/big/06-full-repro-study.md",
        "title": "Full repro study",
        "cat": "Big (AI agent)",
        "script": "examples/big/06_full_repro_study.py",
        "desc": "Agent exports a reproducibility bundle for **BIOMD0000000206**.",
        "run": "export OPENAI_API_KEY=sk-...\npython examples/big/06_full_repro_study.py",
        "needs": "Internet + OpenAI API key.",
        "out": "docs/examples/big/06-full-repro-study/output.txt",
    },
    {
        "md": "docs/examples/big/07-agent-with-configs.md",
        "title": "Agent with presets + skills",
        "cat": "Big (AI agent)",
        "script": "examples/big/07_agent_with_configs.py",
        "desc": "Discovery preset, policy guardrails, and bio skills on one agent.",
        "run": "export OPENAI_API_KEY=sk-...\npython examples/big/07_agent_with_configs.py",
        "needs": "Internet + OpenAI API key.",
        "out": "docs/examples/big/07-agent-with-configs/output.txt",
    },
]


def render(page: dict) -> str:
    gh = "https://github.com/MervinPraison/PraisonAIBio/blob/main"
    script = page["script"]
    minimal = page.get("minimal")
    out = page["out"]
    run_block = page["run"]
    if "\n" in run_block:
        run_md = "```bash\npip install -e \"src/praisonai-bio\"\n" + run_block + "\n```"
    else:
        run_md = f"```bash\npip install -e \"src/praisonai-bio\"\n{run_block}\n```"

    minimal_line = ""
    if minimal:
        minimal_line = f"\n**Minimal (2 lines):** [`{minimal}`]({gh}/{minimal})"

    return f"""# Example — {page["title"]}

**Category:** {page["cat"]} · **Script:** [`{script}`]({gh}/{script}){minimal_line}

{page["desc"]}

---

## How to run

{run_md}

**Needs:** {page["needs"]}

---

## Tested output

Live capture from `./scripts/capture_example_outputs.sh`.

??? "Click to view full output"
    ```text
    --8<-- "{out}"
    ```

---

[← All examples](../index.md)
"""


def main() -> None:
    for page in PAGES:
        path = ROOT / page["md"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render(page), encoding="utf-8")
        print(f"Wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
