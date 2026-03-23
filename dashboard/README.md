# Dashboard — GitHub Pages

This directory contains the PCVR Studios web presence, deployable as a **GitHub Pages** site.

## Contents

| File | Description |
|------|-------------|
| `index.html` | PCVR Studios dark-theme landing page with token info, community links, and project overview |

## Enable GitHub Pages

1. Go to **Settings → Pages** in this repository.
2. Set **Source** to `Deploy from a branch`.
3. Set **Branch** to `main` and **Folder** to `/dashboard`.
4. Click **Save**.

Your site will be live at `https://AIVaneer.github.io/AIVaneer-PCVR-Studios/`.

## Auto-Deploy (CI)

The `.github/workflows/pages.yml` workflow automatically deploys this directory to GitHub Pages on every push to `main` that modifies files in `dashboard/`.

## See Also

- [Eve Toolkit dashboard.py](../eve_toolkit/dashboard.py) — local HTTP dashboard server (Chart.js, real-time data)
- [PCVR Website](https://pcvr.lol)
