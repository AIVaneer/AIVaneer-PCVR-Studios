# Contributing to PCVR Studios

> **First, read our [Code of Conduct](CODE_OF_CONDUCT.md)**. By contributing, you agree to abide by it.

This monorepo contains two projects:

| Package | Description |
|---------|-------------|
| `eve_toolkit/` | PCVR DeFi toolkit — 20+ Python modules for Cronos monitoring |
| `skyburner/` | SkyBurner Ultimate arcade shooter — Atlas Nexus Engine |

All code must run on **Pythonista 3 (iOS)** and **desktop Python 3.8+**. The only allowed external dependency is `requests`.

---

## Getting Started

1. **Fork and clone:**

```bash
git clone https://github.com/AIVaneer/AIVaneer-PCVR-Studios.git
cd AIVaneer-PCVR-Studios
pip install requests pytest flake8
```

2. **Run the test suite:**

```bash
pytest tests/ -v
```

3. **Try the toolkit:**

```bash
cd eve_toolkit
python run_all.py
python atlas_omega.py
```

4. **Try the game** (requires Pythonista 3 on iOS):
   - Copy `skyburner/` files into a Pythonista project
   - Open `skyburner.py` and tap ▶ Run

---

## Development Workflow

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes (see guidelines below)
3. Run tests: `pytest tests/`
4. Run lint: `flake8 eve_toolkit/ skyburner/ tests/ --max-line-length=120`
5. Commit with a descriptive message: `git commit -m "feat: add X to eve_toolkit"`
6. Open a Pull Request against `main`

---

## Eve Toolkit — Module Guidelines

### Adding a New Module

1. Create `eve_toolkit/your_module.py`:

```python
# © PCVR Studios 2026 — Your Module vX.Y
# VN Description — one line purpose

import os

_DIR = os.path.dirname(os.path.abspath(__file__))

# Graceful imports (required for Pythonista 3)
try:
    import requests
    _REQUESTS_OK = True
except ImportError:
    _REQUESTS_OK = False


def report():
    """Return formatted string report. Called by atlas_omega and run_all."""
    pass


def _cli():
    """CLI entry point."""
    print(report())


if __name__ == "__main__":
    _cli()
```

2. Register in `eve_toolkit/atlas_omega.py` → `_MODULE_META`
3. Add import to `eve_toolkit/run_all.py` with graceful fallback
4. Document in `eve_toolkit/MODULES.md`
5. Add tests in `tests/test_eve_toolkit.py`

### Code Rules

- **Pythonista 3 compatible** — no C extensions, no compiled packages
- **Graceful imports** — always use `try/except` for cross-module imports
- **`requests` only** — the sole allowed external dependency
- **`_DIR`-relative paths** — all data files saved relative to `_DIR`
- **`snake_case.py`** for file names, `PCVR_` prefix for data files
- **PEP 8 style**, max line length 120 (for phone screens)

---

## SkyBurner — Game Engine Guidelines

The Atlas Nexus Engine (`skyburner/atlas_nexus.py`) is the foundation. When adding features:

- Use the Entity/Component pattern — new behaviour = new `Component` subclass
- Keep all rendering in the Pythonista `scene` layer (`skyburner.py`)
- Engine code (`atlas_nexus.py`) must be pure Python — zero Pythonista imports
- Maintain zero external dependencies

---

## Tests

All new code should have corresponding tests in `tests/`:

- `tests/test_eve_toolkit.py` — eve_toolkit modules
- `tests/test_skyburner.py` — atlas_nexus engine
- `tests/test_atlas_omega.py` — command center

Run with: `pytest tests/ -v`

---

## Pull Request Guidelines

- One feature per PR
- PR title: `feat:` / `fix:` / `docs:` prefix
- Fill in the PR template checklist
- All tests must pass
- Lint must pass (no syntax errors)

---

## Community

- 💬 **Discord:** [https://discord.gg/E7bW3Zh4x](https://discord.gg/E7bW3Zh4x)
- 🐦 **Twitter/X:** [@pcvr2024](https://x.com/pcvr2024)
- 🐛 **Bugs:** use the bug report issue template
- 💡 **Features:** use the feature request issue template

---

*© PCVR STUDIOS 2026 — Contract: `0x05c870C5C6E7AF4298976886471c69Fc722107e4`*
