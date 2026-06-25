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
2. **Custom domain:** `bio.praison.ai`
3. Save — wait for DNS check (can take up to 24h, often minutes)
4. Enable **Enforce HTTPS** when available

The deploy workflow writes `CNAME` on each push (`cname: bio.praison.ai`).

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
| Wrong content | Ensure Pages source is **GitHub Actions**, not a branch |
| Old URL | Redirect optional: keep `site_url` as bio.praison.ai only |
