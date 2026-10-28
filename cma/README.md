# Private client CMAs

Each client CMA lives in its own folder: `/cma/<street-address-slug>/index.html`
(e.g. `/cma/195-joshua-drive/` -> https://adamdruckgroup.com/cma/195-joshua-drive/).

Rules for every CMA page (keep them private, link-only):
- Include `<meta name="robots" content="noindex, nofollow">` in the `<head>`.
- Never add CMA pages to `sitemap.xml`, the site navigation, or any public page.
- Do not add `/cma/` to `robots.txt` (that would advertise the folder and stop
  Google from seeing the noindex tag).
- Use the ADG / Coldwell Banker branding and the standard "Prepared for" cover line.
- Open as a DRAFT PR; only mark ready after Adam approves (non-draft PRs auto-merge).
