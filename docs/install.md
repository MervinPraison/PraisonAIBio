# Install

## From GitHub (development)

```bash
git clone https://github.com/MervinPraison/PraisonAIBio.git
cd PraisonAIBio
pip install -e "src/praisonai-bio"
python -c "import praisonai_bio"
```

## From PyPI (when published)

```bash
pip install praisonai-bio
python -c "import praisonai_bio"
```

!!! note
    PyPI releases track tagged versions on GitHub. Until the first publish, use the GitHub install above.

!!! tip "Required once per session"
    Always run `import praisonai_bio` before YAML or CLI toolsets.

---

## Optional extras

=== "Simulation (BASICO/COPASI)"

```bash
pip install -e "src/praisonai-bio[simulation]"
# or: pip install "praisonai-bio[simulation]"
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

Scaffold local agent config:

```bash
praisonai-bio init   # creates .praisonai/config.yaml + agent templates
```

---

## Verify

```bash
praisonai-bio validate check
praisonai-bio tools validate
```

Expected: 26 tools, toolsets including `sysbio-full`.

## Recipes (PraisonAI wrapper)

Do not use a custom bio recipe CLI. Point the wrapper at this repo:

```bash
export PRAISONAI_RECIPE_PATH=recipes/bio
praisonai recipe run biomodels-discovery --policy bio-public
```

Available recipes: `biomodels-discovery`, `biomodels-research`, `biomodels-simulate`, `biomodels-perturb`, `biomodels-report`.

---

## Environment

| Variable | Purpose |
|----------|---------|
| `OPENAI_API_KEY` | Agent examples (big/) |
| `BIOMODELS_BASE_URL` | Default `https://www.biomodels.org` |
| `PRAISONAI_POLICY_PACK` | `bio-public` or `bio-lab` — loads policy/packs/*.yaml |
| `PRAISONAI_RECIPE_PATH` | Set to `recipes/bio` for wrapper recipes |

---

## Documentation site

Live docs: [https://bio.praison.ai](https://bio.praison.ai)

Local preview:

```bash
pip install -r docs/requirements.txt
mkdocs serve
```

Next: [Get started](get-started.md)
