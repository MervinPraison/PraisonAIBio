# Example — Agent finds models

**Category:** Big (AI agent) · **Script:** [`examples/big/01_find_models.py`](https://github.com/MervinPraison/PraisonAIBio/blob/main/examples/big/01_find_models.py)

An agent searches BioModels.org using the `biomodels-readonly` toolset.

---

## How to run

```bash
pip install -e "src/praisonai-bio"
export OPENAI_API_KEY=sk-...
python -c "import praisonai_bio"
python examples/big/01_find_models.py
```

---

## Sample output

```
Here are the curated yeast glycolysis model IDs:

1. BIOMD0000000471
2. BIOMD0000000472
3. BIOMD0000000473
4. BIOMD0000000691
5. BIOMD0000000064
6. BIOMD0000000254
7. BIOMD0000000172
```

The agent calls `search_models` internally, then formats IDs for you.

??? "Full captured output"
    [`output.txt`](01-find-models/output.txt)

---

[← All examples](../index.md)
