# Workflows

Multi-agent YAML workflows — no Python required.

---

## Discovery (`workflows/discovery/`)

| File | What it does |
|------|--------------|
| `biomodels_discovery_pipeline.yaml` | Question → ranked shortlist |
| `biomodels_assumption_review.yaml` | Assumption review + human approval |
| `biomodels_baseline_simulation.yaml` | Baseline simulation |
| `biomodels_perturbation_study.yaml` | Perturbation scenarios |
| `biomodels_comparison_report.yaml` | Comparison report |
| `biomodels_full_research_workflow.yaml` | All phases (7 steps) |

```bash
praisonai workflow run workflows/discovery/biomodels_discovery_pipeline.yaml
```

---

## Cookbooks (`workflows/cookbooks/`)

| File | Demo |
|------|------|
| `glycolysis_demo.yaml` | BIOMD0000000206 end-to-end |
| `mapk_p53_discovery.yaml` | MAPK / p53 shortlist |

---

## Orchestration patterns

| File | Pattern |
|------|---------|
| `sysbio_route_by_input.yaml` | Route by domain |
| `parallel_sensitivity_scan.yaml` | Parallel scans |
| `team_model_review.yaml` | AgentTeam review |
| `full_platform_showcase.yaml` | Route + Parallel + Memory |
| `precision_medicine_loop.yaml` | Loop: baseline → perturb → compare |

---

## Platform (`workflows/platform/`)

Production patterns — policy, approval, eval, MCP, bots.

| File | What it does |
|------|--------------|
| `approval_assumption_gate.yaml` | Human approval before assumption review |
| `approval_parameter_scan.yaml` | Human approval before parameter scan |
| `policy_guarded_simulation.yaml` | Simulation with export path policy |
| `eval_regression_gate.yaml` | Eval gate on tool selection |
| `mcp_sysbio_server.yaml` | Run sysbio MCP server workflow |
| `botos_sysbio_telegram.yaml` | Telegram bot + sysbio tools (needs token) |
| `botos_stub.yaml` | BotOS wiring stub |

```bash
praisonai workflow run workflows/platform/policy_guarded_simulation.yaml
```

Agent defaults: `workflows/agents/defaults.yaml`

---

## Flow (full research)

```mermaid
graph TD
    A[Intake] --> B[Search BioModels]
    B --> C[Assumption review]
    C --> D[Simulate]
    D --> E[Report]
```

Before running: `python -c "import praisonai_bio"`

See [For researchers](../for-researchers.md) and [Recipes](../recipes.md).
