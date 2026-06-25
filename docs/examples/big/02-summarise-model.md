# Example — Agent summarises a model

**Category:** Big (AI agent) · **Script:** [`examples/big/02_summarise_model.py`](https://github.com/MervinPraison/PraisonAIBio/blob/main/examples/big/02_summarise_model.py)

Plain-language summary of **BIOMD0000000206** for biologists.

---

## How to run

```bash
pip install -e "src/praisonai-bio"
export OPENAI_API_KEY=sk-...
python -c "import praisonai_bio"
python examples/big/02_summarise_model.py
```

Uses toolset `sbml_analysis` (`get_modelinfo`, `sbml_summarise`, etc.).

---

## Sample output

```
The model Wolf2000_Glycolytic_Oscillations simulates the dynamics of ATP and NADH
in yeast glycolysis, particularly showcasing the oscillatory behavior of these
molecules. It successfully reproduces the patterns seen in a figure from a
supporting paper and was tested using software tools Jarnac and MathSBML.

This model uses ordinary differential equations to describe the interactions
within the glycolytic process. It highlights how populations of yeast cells can
exhibit synchronized glycolytic oscillations due to intercellular signaling
through acetaldehyde.

Key publication details include:
- Title: Transduction of intracellular and intercellular dynamics in yeast
  glycolytic oscillations.
- Authors: Jana Wolf et al.
- Published in: Biophysical Journal, March 2000.
```

??? "Full captured output"
    [`output.txt`](02-summarise-model/output.txt)

---

[← All examples](../index.md)
