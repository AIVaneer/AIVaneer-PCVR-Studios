# Quick Start — PCVR Studios

This guide gets you running both the **Eve Toolkit** (DeFi tools) and **SkyBurner** (arcade game) in under 5 minutes.

---

## Prerequisites

| Platform | Requirements |
|----------|-------------|
| Desktop | Python 3.8+, `pip install requests pytest` |
| iOS | Pythonista 3 from the App Store |

---

## Desktop — Eve Toolkit

```bash
# 1. Clone the monorepo
git clone https://github.com/AIVaneer/AIVaneer-PCVR-Studios.git
cd AIVaneer-PCVR-Studios

# 2. Install the only external dependency
pip install requests

# 3. Run the full system check
cd eve_toolkit
python run_all.py

# 4. Launch the command center
python atlas_omega.py

# 5. Start the web dashboard (localhost:8080)
python dashboard.py
```

---

## Desktop — Tests

```bash
# From the repo root
pip install pytest
pytest tests/ -v
```

---

## Pythonista 3 (iOS) — Eve Toolkit

1. Open **Pythonista 3** → tap **+** to create a new project.
2. Copy all files from `eve_toolkit/` into the project.
3. Open `run_all.py` and tap ▶ to run.

For the native iOS UI:

```python
# In Pythonista's interactive console or a script:
import wkapp_ui
```

See [pythonista_setup.md](pythonista_setup.md) for detailed iOS setup.

---

## Pythonista 3 (iOS) — SkyBurner Game

1. Open **Pythonista 3** → create a new project.
2. Copy these files into it:
   - `skyburner/atlas_nexus.py`
   - `skyburner/entities.py`
   - `skyburner/skyburner.py`
3. Open `skyburner.py` and tap ▶.

---

## Web Dashboard (GitHub Pages)

The `dashboard/index.html` is a standalone dark-theme page ready for GitHub Pages. No build step required.

Enable in **Settings → Pages → Branch: main, Folder: /dashboard**.

---

## Next Steps

- [architecture.md](architecture.md) — Full system architecture
- [token_economy.md](token_economy.md) — PCVR token economy deep dive
- [pythonista_setup.md](pythonista_setup.md) — iOS setup tutorial
- [adding_modules.md](adding_modules.md) — How to add new modules
