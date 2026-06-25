# Contributing to PraisonAIBio

Thank you for helping improve PraisonAIBio. This repo extends [PraisonAI](https://github.com/MervinPraison/PraisonAI) with BioModels.org tools, workflows, and skills.

## Quick start

```bash
git clone https://github.com/MervinPraison/PraisonAIBio.git
cd PraisonAIBio
pip install -e "src/praisonai-bio[simulation,dev]"
python scripts/validate_repo.py
./scripts/test_all.sh
```

## What to contribute

| Area | Location |
|------|----------|
| Tools | `src/praisonai-bio/praisonai_bio/tools/` |
| Adapters | `src/praisonai-bio/praisonai_bio/adapters/` |
| Workflows | `workflows/` |
| Skills | `skills/` (see `docs/skills.md`) |
| Examples | `examples/` |
| Docs | `docs/` (MkDocs site) |

## Development rules

1. **Protocol-first** — adapters implement protocols in `protocols/`.
2. **Lazy imports** — optional deps (BASICO, Chroma) inside functions only.
3. **Three surfaces** — Python tools, YAML workflows, CLI where applicable.
4. **Tests** — unit tests in `tests/unit/`; agentic tests need `OPENAI_API_KEY`.
5. **No grant content** — do not commit internal grant proposals (`grant/` is gitignored).

## Pull request checklist

- [ ] `python scripts/validate_repo.py` passes
- [ ] `./scripts/test_all.sh` passes (or document skips)
- [ ] New tools registered via `pyproject.toml` entry points and toolsets
- [ ] Docs updated if user-facing behaviour changes
- [ ] British English in prose where you edit docs

## Reporting issues

Open an issue at [github.com/MervinPraison/PraisonAIBio/issues](https://github.com/MervinPraison/PraisonAIBio/issues) with:

- Python version and OS
- `praisonai-bio validate check` output
- Minimal repro (script or workflow YAML)

## Code of conduct

Be respectful and constructive. We follow the same standards as the main PraisonAI project.
