# Examples

**Start here:** [minimal/](minimal/) — two lines per script.

```bash
pip install -e "src/praisonai-bio"
python examples/minimal/search.py
```

| Folder | Lines | Needs |
|--------|-------|--------|
| [minimal/](minimal/) | 2–3 | See [minimal/README.md](minimal/README.md) |
| [small/](small/) | Same scripts, numbered 01–10 | Internet; BASICO for 05–06 |
| [big/](big/) | 3 + agent | `OPENAI_API_KEY` |
| [workflows/](../workflows/cookbooks/) | YAML only | `praisonai workflow run …` |

Demo model: **BIOMD0000000206**

```bash
export OPENAI_API_KEY=sk-...   # big/ only
python examples/minimal/agent.py
```
