# Quickstart Guide

**PCVR Studios — AIVaneer-PCVR-Studios**

---

## Prerequisites

- Python 3.8 or higher (3.10+ recommended)
- `git` installed
- For iOS: Pythonista 3 from the App Store

---

## 1. Cloning the Repository

```bash
git clone https://github.com/AIVaneer/AIVaneer-PCVR-Studios.git
cd AIVaneer-PCVR-Studios
```

---

## 2. Running on Desktop (Python 3.8+)

### Install dev tools

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install flake8 pytest
```

### Lint

```bash
flake8 skyburner/ eve_toolkit/ project_dont_die/ tests/ --max-line-length=99
```

### Run tests

```bash
pytest tests/ -v
```

---

## 3. Running on Pythonista 3 (iOS)

Pythonista 3 runs Python 3.6+ natively on iPhone and iPad with zero external
dependencies required for any PCVR Studios module.

1. Install **Pythonista 3** from the App Store.
2. Clone or copy the module folders you need (`skyburner/`, `eve_toolkit/`,
   `project_dont_die/`) into your Pythonista project directory.
3. Open any entry-point file and tap **Run** (▶).

See [`docs/pythonista_setup.md`](./pythonista_setup.md) for the full iOS
tutorial.

---

## 4. Running Atlas Omega Command Center

`atlas_omega.py` is the master command center that ties all Eve Toolkit
modules together. On desktop:

```bash
python eve_toolkit/atlas_omega.py
```

On Pythonista 3, open `atlas_omega.py` in the editor and tap **Run**.

---

## 5. Running SkyBurner Ultimate

SkyBurner Ultimate is designed for Pythonista 3 on iOS. The entry point is
`skyburner/main_scene.py` (or `skyburner.py` in the standalone repo).

On Pythonista 3:

1. Open `skyburner/main_scene.py`.
2. Tap **Run** (▶).
3. The game launches in full-screen on your device.

On desktop (headless / test mode):

```bash
python -c "from skyburner.atlas_nexus import AtlasNexusEngine; e = AtlasNexusEngine(); e.start(); print('Engine OK'); e.stop()"
```

---

## 6. Community & Support

| | |
|---|---|
| 💬 Discord | [discord.gg/E7bW3Zh4x](https://discord.gg/E7bW3Zh4x) |
| 🐦 Twitter / X | [@pcvr2024](https://twitter.com/pcvr2024) |
| 🌐 Website | [pcvr.lol](https://pcvr.lol) |

---

© PCVR STUDIOS 2026
