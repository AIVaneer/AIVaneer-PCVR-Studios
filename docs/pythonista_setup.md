# Pythonista 3 Setup — PCVR Studios

This guide covers running both the **Eve Toolkit** and **SkyBurner** on iOS via Pythonista 3.

---

## Requirements

- iPhone or iPad running iOS 15+
- [Pythonista 3](https://apps.apple.com/app/pythonista-3/id1085978097) (paid, ~$10) from the App Store
- Internet connection (for market data features)

---

## Getting the Files

### Option A — GitHub (Recommended)

Use the built-in GitHub integration in Pythonista or the [StaSh](https://github.com/ywangd/stash) shell:

```bash
# In StaSh:
git clone https://github.com/AIVaneer/AIVaneer-PCVR-Studios.git
```

### Option B — Manual Copy

1. Open each file on GitHub (phone browser).
2. Copy the raw content.
3. In Pythonista, create a new file and paste.

---

## Eve Toolkit Setup

1. Create a folder in Pythonista (e.g., `eve_toolkit`).
2. Copy all `.py` and `.html` files from `eve_toolkit/` into it.
3. Open `run_all.py` and tap ▶ to verify everything loads.

### Important Notes

- All data files (`.json`, `.csv`) are created automatically in the same folder as the modules.
- **Do not store API keys in the script** — use the interactive prompts or `integration_keys.json` (gitignored).
- The `requests` module is included in Pythonista 3 — no `pip install` needed.

### First Run

```python
# Open run_all.py and run it — you should see:
# ✅ All modules loaded
# Running full system check...
```

---

## SkyBurner Setup

1. Create a folder (e.g., `skyburner`).
2. Copy these 3 files:
   - `skyburner/atlas_nexus.py`
   - `skyburner/entities.py`
   - `skyburner/skyburner.py`
3. Open `skyburner.py` and tap ▶.

The game runs in full screen using Pythonista's `scene` module — no external assets needed.

---

## iOS-Specific Tips

### Performance
- Close other apps before running the game for best frame rate.
- The dashboard auto-refresh interval can be increased in `wkapp_ui.py` if the device gets warm.

### Paths
All modules use `_DIR = os.path.dirname(os.path.abspath(__file__))` so data files are always saved next to the script, regardless of working directory.

### Modules Not Available on iOS
The following modules gracefully degrade if imports fail on iOS:
- `multiprocessing` — automation runs in single-thread mode
- `subprocess` — github_sync falls back to API-only mode

All failures are handled with `try/except` — nothing crashes.

---

## Native iOS UI

`wkapp_ui.py` provides a native iOS interface using Pythonista's `ui` module and `WKWebView`:

```python
import wkapp_ui
# Opens a full-screen WKWebView dashboard
```

This embeds the `dashboard_template.html` directly in iOS, giving you a responsive chart dashboard without needing a separate server.

---

## Community Support

If you run into iOS-specific issues, post in the **#pythonista** channel on our Discord:

🔗 [https://discord.gg/E7bW3Zh4x](https://discord.gg/E7bW3Zh4x)
