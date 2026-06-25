# Development

For contributors and CI.

---

## Setup

```bash
pip install -e "src/praisonai-bio[dev,simulation]"
```

---

## Tests

```bash
./scripts/test_all.sh
```

Or step by step:

```bash
pytest tests/unit -q
pytest tests/integration -q      # live BioModels.org
pytest tests/agentic -q          # needs OPENAI_API_KEY
```

---

## Validation

```bash
python scripts/validate_repo.py
bash scripts/check_no_submission.sh
python scripts/generate_catalog.py
```

---

## Docs site

```bash
pip install -r docs/requirements.txt
mkdocs serve    # http://127.0.0.1:8000
mkdocs build    # output in site/
```

---

## Package layout

```
src/praisonai-bio/praisonai_bio/
  adapters/     # BioModels API, BASICO
  tools/        # @tool functions + entry points
  toolsets/     # prebuilt toolsets
  workflows/    # (YAML lives in repo workflows/)
```

See [AGENTS.md](https://github.com/MervinPraison/PraisonAIBio/blob/main/AGENTS.md) on GitHub for contributor rules.
