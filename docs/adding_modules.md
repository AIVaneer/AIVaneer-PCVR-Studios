# Adding New Modules — Eve Toolkit

> Adapted from `CONTRIBUTING.md` (Eve-Repository)

This guide explains how to add a new Python module to the Eve Toolkit in a way that integrates fully with Atlas Omega, run_all, and the test suite.

---

## Step 1 — Create the Module File

Create `eve_toolkit/your_module.py` following this template:

```python
# © PCVR Studios 2026 — Your Module vX.Y
# VN Short description — one line

import os

_DIR = os.path.dirname(os.path.abspath(__file__))

# Graceful imports (required for Pythonista 3 compatibility)
try:
    import requests
    _REQUESTS_OK = True
except ImportError:
    _REQUESTS_OK = False

# Cross-module imports also use try/except
try:
    from token_data import TOKEN
    _TOKEN_OK = True
except ImportError:
    _TOKEN_OK = False


def report():
    """Return formatted string report. Called by atlas_omega and run_all."""
    lines = [
        "=" * 50,
        "  Your Module Report",
        "=" * 50,
        f"  Status: ...",
        "=" * 50,
    ]
    return "\n".join(lines)


def _cli():
    """CLI entry point."""
    print(report())


if __name__ == "__main__":
    _cli()
```

### Rules

| Rule | Requirement |
|------|------------|
| `_DIR` variable | All file paths relative to `_DIR` — never `os.getcwd()` |
| Graceful imports | Every import in `try/except` |
| `report()` | Returns formatted string (box style) |
| `_cli()` | Runs when called directly or from atlas_omega |
| File naming | `snake_case.py` |
| Data files | `pcvr_yourmodule.json` or `yourmodule_cache.json` |

---

## Step 2 — Register in Atlas Omega

Edit `eve_toolkit/atlas_omega.py` and add to `_MODULE_META`:

```python
_MODULE_META = {
    # ... existing entries ...
    "your_module": "VN",
}
```

Then add a command method to `OmegaEngine`:

```python
def quick_yourmodule(self):
    """Print your module summary."""
    mod = self.modules.get("your_module")
    if not mod:
        print("  ⚠️  your_module not loaded")
        return
    try:
        print(mod.report())
    except Exception as exc:
        print(f"  ⚠️  Error: {exc}")
```

---

## Step 3 — Add to run_all.py

Edit `eve_toolkit/run_all.py` and add:

```python
try:
    import your_module as _your_module
    _YOUR_MODULE_AVAILABLE = True
except Exception:
    _YOUR_MODULE_AVAILABLE = False

# In the main runner section:
if _YOUR_MODULE_AVAILABLE:
    try:
        print(_your_module.report())
    except Exception as exc:
        print(f"[your_module] error: {exc}")
```

---

## Step 4 — Document in MODULES.md

Add a section to `eve_toolkit/MODULES.md`:

```markdown
## your_module — VN Description

Short description of the module.

### Functions

| Function | Returns | Description |
|----------|---------|-------------|
| `report()` | `str` | Full formatted report |
| `your_function(arg)` | `type` | Description |

### CLI

```bash
python your_module.py
```

### Data Files

| File | Description |
|------|-------------|
| `pcvr_yourmodule.json` | Cached data |
```

---

## Step 5 — Add Tests

Add a test class to `tests/test_eve_toolkit.py`:

```python
class TestYourModule:
    def test_report_returns_string(self):
        import your_module
        result = your_module.report()
        assert isinstance(result, str)
        assert len(result) > 0

    def test_your_function_basic(self):
        import your_module
        result = your_module.your_function(arg)
        assert result == expected
```

Run: `pytest tests/test_eve_toolkit.py -v`

---

## Step 6 — Add to .gitignore

If your module writes data files, add them to `.gitignore`:

```
pcvr_yourmodule.json
yourmodule_cache.json
```

---

## Checklist

- [ ] Module file created in `eve_toolkit/`
- [ ] `_DIR` variable set
- [ ] All imports wrapped in `try/except`
- [ ] `report()` function implemented
- [ ] `_cli()` function implemented
- [ ] Registered in `_MODULE_META` in `atlas_omega.py`
- [ ] Added to `run_all.py` with graceful fallback
- [ ] Documented in `MODULES.md`
- [ ] Tests added in `tests/test_eve_toolkit.py`
- [ ] Data files added to `.gitignore`
- [ ] `pytest tests/` passes
- [ ] `flake8 eve_toolkit/ --max-line-length=120` passes
