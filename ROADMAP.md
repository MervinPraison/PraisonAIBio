# PraisonAIBio Roadmap

## Phase 0/1 — Done (scaffold)

- [x] 21 BioModels tools + 10 toolsets
- [x] Discovery, orchestration, platform, and cookbook workflows
- [x] Skills catalog + MCP sysbio server (11 T2B tools)
- [x] MkDocs site at [bio.praison.ai](https://bio.praison.ai)
- [x] Benchmark manifests + T2B parity cases
- [x] Examples with captured output

## Phase 1 polish (in progress)

- [x] Session persistence wired in `repro_export`
- [x] Recipe `TEMPLATE.yaml` for PraisonAI recipe runner
- [x] Route step in discovery pipeline
- [x] HITL gate documented and linked in full research workflow
- [ ] Hooks/trace wired into tool execution hot path
- [ ] Knowledge/RAG article index (beyond stub)
- [ ] MCP resources/prompts exposed in server code
- [ ] Policy packs `bio-public` / `bio-lab` enforced in workflows

## Phase 2 — Deferred

| Item | Notes |
|------|-------|
| OLS adapter | Ontology lookup via EBI OLS |
| MCP Docker image | `mcp/sysbio-server/Dockerfile` |
| ClawBio bridge | Full skill/script bridge |
| BotOS Telegram demo | Production bot deployment |
| Cross-model comparison engine | Multi-model orchestration |
| 312-question benchmark | Extended eval suite |
| PyPI publish | `praisonai-bio` on PyPI |

## How to propose work

1. Check [docs/plan-validation.md](docs/plan-validation.md) for known gaps.
2. Open a GitHub issue describing the gap and proposed approach.
3. Follow [CONTRIBUTING.md](CONTRIBUTING.md) for PRs.
