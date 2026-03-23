# Dashboard — GitHub Pages

The `dashboard/` directory contains the PCVR Studios web dashboard
(`index.html`). It is a self-contained, zero-dependency HTML/CSS page that
can be served via **GitHub Pages** or run locally.

---

## Enabling GitHub Pages

1. Go to your repository **Settings → Pages**.
2. Under **Source**, select **GitHub Actions**.
3. The `.github/workflows/pages.yml` workflow deploys `dashboard/` automatically
   on every push to `main`.
4. After the first successful run, your dashboard will be live at:

   ```
   https://<your-username>.github.io/<repo-name>/
   ```

---

## Running Locally

No build step required — just open the file in any browser:

```bash
# macOS
open dashboard/index.html

# Linux
xdg-open dashboard/index.html

# Windows
start dashboard/index.html
```

Or serve it with Python's built-in HTTP server:

```bash
cd dashboard
python3 -m http.server 8080
# Open http://localhost:8080 in your browser
```

---

## Structure

```
dashboard/
├── index.html   # Full PCVR Studios landing page (18KB, self-contained)
└── README.md    # This file
```

---

© PCVR STUDIOS 2026
