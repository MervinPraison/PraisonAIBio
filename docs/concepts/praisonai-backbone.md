# PraisonAI backbone

PraisonAIBio is a **domain plugin** on the PraisonAI SDK — not a second orchestration stack.

```mermaid
flowchart LR
  CLI[praisonai CLI] --> WF[Workflows]
  WF --> Agent[Agent / AgentTeam]
  Agent --> Tools[Bio tools]
  Tools --> API[BioModels / BASICO]
```

## PraisonAI owns

- Agent, workflows (`route`, `parallel`, `approve`)
- Hooks, PolicyEngine, MemoryConfig, EvalSuite
- MCP launcher, recipes, scheduler

## PraisonAIBio owns

- 28 BioModels tools and adapters
- SBML/SED-ML parsing, benchmarks, repro bundles
- Domain workflows under `workflows/`

## Three integration paths

```bash
import praisonai_bio
praisonai workflow run workflows/cookbooks/full_platform_pipeline.yaml
praisonai recipe run biomodels-discovery
```

**Do not duplicate** `praisonai workflow run` in the bio CLI. Bio CLI: `init`, `validate`, `doctor`, `bench`.

See [AGENTS.md](https://github.com/MervinPraison/PraisonAIBio/blob/main/AGENTS.md) in the repository.
