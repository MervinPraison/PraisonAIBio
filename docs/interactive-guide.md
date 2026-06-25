# Interactive guide

**Who this is for:** researchers and lab scientists — not developers.

**Last checked:** automated tests on PraisonAIBio v0.2.0 (51 checks passed, repo validated, benchmarks green).

---

## At a glance

| Area | Status | Plain English |
|------|--------|---------------|
| Find models | ✅ | Search and rank BioModels in minutes |
| Read model structure | ✅ | Summarise SBML and reaction maps |
| Simulate | ⚠️ | Works when **BASICO** is installed |
| Compare & trust | ✅ | Score curation and diff simulations |
| Export a study bundle | ✅ | Zip SBML, notes, and rerun commands |
| Safety rules | ✅ | Blocks risky saves in public mode |
| Ready-made workflows | ✅ | 32 YAML pipelines (8-step demo included) |
| Recipes | ✅ | 5 packaged studies |
| How-to skills | ✅ | 16 short guides |
| Connect to other apps | ✅ | 28 tools via MCP |

!!! tip "One model to try"
    **BIOMD0000000206** — yeast glycolysis. Used in examples, cookbooks, and benchmarks.

---

## Which path should I take?

=== "Quick lookup (no chat)"

**Best when:** you know what you want (search, one model ID, trust check).

1. [Install](install.md) → `pip install -e src/praisonai-bio`
2. Pick a [quick task](quick-tasks.md) — copy, paste, run
3. Start with `examples/small/01_search.py`

**Needs internet** to BioModels.org. No OpenAI key.

=== "Ask an AI agent"

**Best when:** your question is open-ended (“models for p53 under DNA damage?”).

1. Install + set `OPENAI_API_KEY`
2. Run `examples/big/01_find_models.py`
3. Or: `praisonai workflow run workflows/discovery/biomodels_discovery_pipeline.yaml`

=== "Full automated study"

**Best when:** you want discovery → check → simulate → report in one go.

```bash
praisonai workflow run workflows/cookbooks/full_platform_pipeline.yaml
```

Eight steps: find → inspect → map → **you approve** → simulate → perturb → compare → export.

=== "Packaged recipe"

**Best when:** you repeat the same study type.

```bash
export PRAISONAI_RECIPE_PATH=recipes/bio
praisonai recipe run biomodels-discovery
```

See [Recipes](recipes.md) for all five.

---

## Do I need BASICO?

Answer three quick questions:

??? question "Will you run time-course simulations on your machine?"
    **Yes** → install simulation extras:
    ```bash
    pip install -e "src/praisonai-bio[simulation]"
    ```
    **No** → discovery, trust scores, SBML maps, and workflows still work.

??? question "Will you only search and read models?"
    **Yes** → no BASICO needed. Use small examples 01–04 and 10.

??? question "Will you use Jupyter notebooks?"
    Notebooks **01–02** work without BASICO. **03–04** need BASICO + network.

---

## What does the trust score mean?

??? info "Curated vs non-curated"
    **Curated** = manually checked on BioModels. Prefer these for publications.  
    **Non-curated** = use with extra caution.

??? info "Trust scorecard (tool)"
    Run `examples/small/03_trust_score.py` — returns curation status, publication links, and flags.

??? info "Human approval step"
    Full workflows pause before simulation so you can reject bad assumptions. Look for **approve** steps in YAML.

---

## Your first glycolysis study (5 steps)

```mermaid
graph LR
  A[Search] --> B[Trust check]
  B --> C[SBML map]
  C --> D[Simulate]
  D --> E[Export bundle]
  classDef step fill:#8B0000,color:#fff
  class A,B,C,D,E step
```

| Step | You do | Command / workflow |
|------|--------|-------------------|
| 1 | Search | `python examples/small/01_search.py` |
| 2 | Trust | `python examples/small/03_trust_score.py` |
| 3 | Map | `python examples/small/10_sbml_graph.py` |
| 4 | Simulate | `python examples/small/05_simulate.py` *(BASICO)* |
| 5 | Export | `python examples/small/09_repro_export.py` |

Or one workflow: `workflows/cookbooks/glycolysis_demo.yaml`

---

## Feature checklist (test results)

<details markdown="1">
<summary><strong>Search & discovery</strong> — ✅ Works</summary>

- Search BioModels by keyword  
- Rank and filter curated models  
- Advanced field search  

**Try:** [Quick task 1](quick-tasks.md#task-1-find-models)
</details>

<details markdown="1">
<summary><strong>SBML & reaction maps</strong> — ✅ Works</summary>

- Summarise model contents  
- Validate SBML structure  
- Build reaction graph (local or download PNG/SVG)  

**Try:** `examples/small/04_validate_sbml.py`, `10_sbml_graph.py`
</details>

<details markdown="1">
<summary><strong>Simulation</strong> — ⚠️ Needs BASICO</summary>

- Baseline time-course  
- Parameter perturbation  
- SED-ML-aware runs (when SED-ML file exists)  

**Install:** `pip install -e "src/praisonai-bio[simulation]"`  
**Try:** `examples/small/05_simulate.py`
</details>

<details markdown="1">
<summary><strong>Compare & trust</strong> — ✅ Works</summary>

- Compare two models (metadata + structure)  
- Compare two simulation runs (RMSE-style metrics)  
- Trust scorecards  

**Try:** `examples/small/07_compare_models.py`, `08_compare_sims.py` *(08 works offline)*
</details>

<details markdown="1">
<summary><strong>Export & reproducibility</strong> — ✅ Works</summary>

- Repro bundle with checksums and rerun script  
- COMBINE archive when BioModels provides it  

**Try:** `examples/small/09_repro_export.py`
</details>

<details markdown="1">
<summary><strong>Safety & policies</strong> — ✅ Works</summary>

| Mode | You can… |
|------|----------|
| `bio-public` | Search and read — no saving |
| `bio-lab` | Simulate, perturb, export |

Set: `export PRAISONAI_POLICY_PACK=bio-public`
</details>

<details markdown="1">
<summary><strong>Workflows & recipes</strong> — ✅ Works</summary>

- **32** workflow files validated  
- **8-step** full platform pipeline  
- **5** recipes (`biomodels-discovery`, `research`, `simulate`, `perturb`, `report`)  

[Workflows guide](concepts/workflows.md) · [Recipes](recipes.md)
</details>

<details markdown="1">
<summary><strong>Skills (16 guides)</strong> — ✅ Works</summary>

Short how-tos for agents — search, simulate, orchestrate, repro, and more.  
[Full skills list](skills.md)
</details>

<details markdown="1">
<summary><strong>Benchmarks & quality</strong> — ✅ Works</summary>

- 10 Talk2BioModels-style routing checks — pass  
- Simulation accuracy check — pass  
- 51 automated unit checks — pass  

*(For developers: `python benchmarks/run_all.py`)*
</details>

---

## Something failed?

??? failure "Install errors"
    Use GitHub install until PyPI publish:
    ```bash
    git clone https://github.com/MervinPraison/PraisonAIBio.git
    cd PraisonAIBio && pip install -e "src/praisonai-bio[dev]"
    ```

??? failure "Network / BioModels"
    Check internet and `https://www.biomodels.org`. Optional: `BIOMODELS_BASE_URL`.

??? failure "Simulation failed"
    Install BASICO: `pip install -e "src/praisonai-bio[simulation]"`.  
    Confirm model ID (try **BIOMD0000000206**).

??? failure "Agent / workflow errors"
    Run `import praisonai_bio` first. Set `OPENAI_API_KEY` for LLM steps.  
    Install wrapper: `pip install praisonai`.

??? failure "Permission / save blocked"
    Switch policy: `export PRAISONAI_POLICY_PACK=bio-lab` for export and save tools.

---

## Talk2BioModels & ClawBio

| Tool | Role |
|------|------|
| [vs Talk2BioModels](concepts/vs-t2b.md) | Same 11 core tools + discovery extras |
| [vs ClawBio](concepts/vs-clawbio.md) | ClawBio = genomics; PraisonAIBio = mechanistic models — use together |

---

## Next steps

- [Quick tasks](quick-tasks.md) — copy-paste commands  
- [For researchers](for-researchers.md) — study flow diagram  
- [Tools at a glance](tools-at-a-glance.md) — what each tool does in plain English  
- [Notebooks](examples/notebooks/index.md) — interactive Jupyter path  
