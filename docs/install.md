# Install

## From GitHub

```bash
git clone https://github.com/MervinPraison/PraisonAIBio.git
cd PraisonAIBio
pip install -e "src/praisonai-bio"
python -c "import praisonai_bio"
```

!!! tip "Required once per session"
    Always run `import praisonai_bio` before YAML or CLI toolsets.

---

## Optional extras

=== "Simulation (BASICO/COPASI)"

```bash
pip install -e "src/praisonai-bio[simulation]"
```

=== "Plotting"

```bash
pip install -e "src/praisonai-bio[plot]"
```

=== "Everything"

```bash
pip install -e "src/praisonai-bio[all,dev]"
```

---

## PraisonAI CLI (workflows)

Install the [PraisonAI](https://github.com/MervinPraison/PraisonAI) wrapper for YAML workflows and agents:

```bash
pip install praisonai
```

---

## Verify

```bash
praisonai-bio validate check
praisonai-bio tools validate
```

Expected: 21 tools, toolsets including `sysbio-full`.

---

## Environment

| Variable | Purpose |
|----------|---------|
| `OPENAI_API_KEY` | Agent examples (big/) |
| `BIOMODELS_BASE_URL` | Default `https://www.biomodels.org` |

Next: [Get started](get-started.md)
