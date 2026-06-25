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

Expected: 21 tools, toolsets including `sysbio-full`.

---

## Environment

| Variable | Purpose |
|----------|---------|
| `OPENAI_API_KEY` | Agent examples (big/) |
| `BIOMODELS_BASE_URL` | Default `https://www.biomodels.org` |
| `TELEGRAM_BOT_TOKEN` | Optional — `botos_sysbio_telegram.yaml` workflow |

---

## Documentation site

Live docs: [https://bio.praison.ai](https://bio.praison.ai)

Local preview:

```bash
pip install -r docs/requirements.txt
mkdocs serve
```

Next: [Get started](get-started.md)
