# Material theme options

PraisonAIBio uses **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)** with several built-in colour palettes. No custom CSS theme — just Material’s native `primary` and `accent` colours.

## Switch themes on the site

Click the **palette icon** in the header (next to search). Each click cycles:

| # | Name | Light | Dark | Primary | Accent | Best for |
|---|------|-------|------|---------|--------|----------|
| 1 | **Praison** | `default` | `slate` | red | teal | Brand — biology + Praison red |
| 2 | **Indigo** | `default` | `slate` | indigo | indigo | Classic Material look |
| 3 | **Forest** | `default` | `slate` | green | light-green | Scientific / eco tone |
| 4 | **Midnight** | `default` | `slate` | black | teal | Minimal, high contrast |
| 5 | **Deep purple** | `default` | `slate` | deep-purple | amber | Enterprise / long-form docs |
| 6 | **Cyan** | `default` | `slate` | cyan | cyan | API / developer docs |

Light and dark are separate steps in the cycle (e.g. Praison light → Praison dark → Indigo light → …).

Your OS may pick **Praison** automatically on first visit (`prefers-color-scheme`).

## Set the default in `mkdocs.yml`

Edit the first `palette` block under `theme:` in [`mkdocs.yml`](https://github.com/MervinPraison/PraisonAIBio/blob/main/mkdocs.yml):

```yaml
theme:
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: green        # change this
      accent: light-green   # change this
```

## All Material colours

Material supports these **primary** and **accent** values (same list for both):

| | | | |
|---|---|---|---|
| red | pink | purple | deep-purple |
| indigo | blue | light-blue | cyan |
| teal | green | light-green | lime |
| yellow | amber | orange | deep-orange |
| brown | grey | blue-grey | black |
| white | | | |

Reference: [Material — Changing the colours](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/)

## Live Material demos

| Demo | URL |
|------|-----|
| Official Material docs | https://squidfunk.github.io/mkdocs-material/ |
| MkDocs theme gallery (Material) | https://pawamoy.github.io/mkdocs-gallery/themes/material/ |
| MaterialX fork | https://jaywhj.github.io/mkdocs-materialx/ |

## Preview locally

```bash
cd PraisonAIBio
mkdocs serve
```

Open http://127.0.0.1:8000 and use the header palette toggle to compare themes.
