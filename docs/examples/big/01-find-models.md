# Example — Agent finds models

**Category:** Big (AI agent) · **Script:** [`examples/big/01_find_models.py`](https://github.com/MervinPraison/PraisonAIBio/blob/main/examples/big/01_find_models.py)
**Minimal (2 lines):** [`examples/minimal/agent.py`](https://github.com/MervinPraison/PraisonAIBio/blob/main/examples/minimal/agent.py)

Agent searches BioModels for curated yeast glycolysis models.

---

## How to run

```bash
pip install -e "src/praisonai-bio"
export OPENAI_API_KEY=sk-...
python examples/big/01_find_models.py
```

**Needs:** Internet + OpenAI API key.

---

## Tested output

Live capture from `./scripts/capture_example_outputs.sh`.

??? "Click to view full output"
    ```text
    --8<-- "docs/examples/big/01-find-models/output.txt"
    ```

---

[← All examples](../index.md)
