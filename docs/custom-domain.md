# Custom domain — bio.praison.ai

Docs are served at **https://bio.praison.ai** via GitHub Pages.

---

## 1. DNS (praison.ai registrar / Cloudflare)

Add a **CNAME** record:

| Type | Name | Value | TTL |
|------|------|-------|-----|
| CNAME | `bio` | `mervinpraison.github.io` | Auto |

!!! note
    Use `bio` as the host name (not `bio.praison.ai` in the name field on some panels).

If you use **Cloudflare**, proxy (orange cloud) is fine — enable **Full** SSL.

---

## 2. GitHub repo settings

1. Open [PraisonAIBio → Settings → Pages](https://github.com/MervinPraison/PraisonAIBio/settings/pages)
2. **Build and deployment → Source:** Deploy from a branch
3. **Branch:** `gh-pages` · **Folder:** `/ (root)` — **not** `main`
4. **Custom domain:** `bio.praison.ai`
5. Save — wait for DNS check (can take up to 24h, often minutes)
6. Enable **Enforce HTTPS** when available

The `docs` workflow builds MkDocs and pushes to `gh-pages` via `peaceiris/actions-gh-pages` (`cname: bio.praison.ai`).

---

## 3. Repo files (already configured)

- `docs/CNAME` → copied into `site/` on build
- `mkdocs.yml` → `site_url: https://bio.praison.ai/`
- `.github/workflows/docs.yml` → deploy with custom domain

---

## 4. Verify

```bash
dig bio.praison.ai CNAME +short
# expect: mervinpraison.github.io.

curl -I https://bio.praison.ai
```

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| DNS not verified | Wait; confirm CNAME points to `mervinpraison.github.io` |
| Certificate pending | Disable/re-enable Enforce HTTPS after DNS is green |
| Wrong content / old Jekyll theme | Pages source must be **`gh-pages` / (root)**, not `main`. Rebuild: `gh api --method POST repos/MervinPraison/PraisonAIBio/pages/builds` |
| Design not updating after push | Confirm `docs` workflow succeeded and `gh-pages` has MkDocs HTML (`mkdocs-` in page source) |
