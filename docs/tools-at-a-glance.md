# Tools at a glance

What each tool does — no code required to understand.

---

## Discovery (safe, read-only)

| Tool | You ask… | You get… |
|------|----------|----------|
| **search_models** | “Find p53 models” | List from BioModels.org |
| **get_modelinfo** | “Details for BIOMD…” | Name, authors, description |
| **rank_models** | “Best fit for my question?” | Ranked list with scores |
| **trust_scorecard** | “Is this curated?” | Trust score + reasons |
| **compare_models** | “How do A and B differ?” | Side-by-side metadata |
| **sbml_summarise** | “What’s in the model?” | Species, reactions summary |
| **get_annotation** | “What databases link to this?” | MIRIAM annotations |
| **query_article** | “Which paper?” | DOI / PubMed links |

---

## Simulation (needs `pip install praisonai-bio[simulation]`)

| Tool | You ask… | You get… |
|------|----------|----------|
| **load_biomodel** | “Load this ID” | SBML on disk |
| **simulate_model** | “Run for 100 time units” | Time-course preview |
| **steady_state** | “Steady state?” | Concentrations |
| **parameter_scan** | “Scan parameter X” | Scan table |
| **preview_outcomes** | “Quick preview” | Short simulation |
| **simulate_perturbation** | “Change one parameter” | Perturbed run |
| **custom_plotter** | “Plot results” | PNG file |

---

## Reporting & reproducibility

| Tool | You ask… | You get… |
|------|----------|----------|
| **compare_simulations** | “Baseline vs perturbed?” | Comparison summary |
| **save_model** | “Save SBML” | File on disk |
| **repro_export** | “Repro bundle” | Folder with SBML + checksums |
| **ask_question** | “Explain this model” | Metadata for the agent to reason over |

---

## Toolsets (bundles)

| Toolset | Who it's for |
|---------|--------------|
| **biomodels-readonly** | Discovery only — safe |
| **sysbio-core** | Discovery + basic simulation |
| **simulation** | Running models |
| **sysbio-orchestrator** | Multi-step discovery agent |

Use in agents: `toolsets=["biomodels-readonly"]`

Always run `import praisonai_bio` first.
