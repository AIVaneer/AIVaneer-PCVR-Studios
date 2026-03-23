# Adding New Modules to Eve Toolkit

**PCVR Studios — Contribution guide for new eve_toolkit modules**

---

## Overview

Every module in `eve_toolkit/` follows a consistent set of conventions so that
all modules work together, run safely in Pythonista 3, and integrate cleanly
with `atlas_omega.py`.

---

## 1. Graceful Import Pattern

Pythonista 3 does not include every Python standard library module. Use
`try/except` for any import that might be unavailable:

```python
try:
    import requests
    _HAS_REQUESTS = True
except ImportError:
    _HAS_REQUESTS = False
```

Then guard usage:

```python
def fetch_price(token):
    if not _HAS_REQUESTS:
        return 0.0
    response = requests.get(f"https://api.example.com/price/{token}")
    return response.json().get("price", 0.0)
```

This ensures the module imports and runs on both desktop Python and Pythonista 3
without crashing.

---

## 2. `_DIR` Pattern for File Paths

Never hard-code absolute paths. Use the `_DIR` pattern to locate files relative
to the module itself:

```python
import os

_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(_DIR, "data", "prices.json")
```

This works correctly whether the module is imported from the repo root,
`site-packages`, or a Pythonista project folder.

---

## 3. `report()` Function Convention

Every module should expose a `report()` function that returns a human-readable
string summarising its current state. This is how `atlas_omega.py` polls all
registered modules:

```python
def report() -> str:
    """Return a one-line status string for the atlas_omega dashboard."""
    return f"MyModule: status=OK, value={_current_value}"
```

Conventions:

- Return a single string (may contain `\n` for multi-line output).
- Never raise exceptions inside `report()` — catch and include errors in the
  string instead.
- Keep it fast — `report()` is called frequently.

---

## 4. Registering in `atlas_omega.py`

After writing your module, register it in `atlas_omega.py` so it appears in the
master command center:

1. Import your module at the top of `atlas_omega.py`:

   ```python
   try:
       from eve_toolkit import my_module
   except ImportError:
       my_module = None
   ```

2. Add it to the `MODULES` list:

   ```python
   MODULES = [
       # ... existing modules ...
       ("MyModule", my_module),
   ]
   ```

3. The `run_all()` function in `atlas_omega.py` will call `my_module.report()`
   automatically and display the result.

---

## 5. Checklist for New Modules

- [ ] Graceful `try/except` imports for all optional dependencies
- [ ] `_DIR` pattern used for any file paths
- [ ] `report()` function implemented
- [ ] Module registered in `atlas_omega.py`
- [ ] Unit tests added in `tests/test_eve_toolkit.py`
- [ ] Module listed in `eve_toolkit/__init__.py` exports
- [ ] No hard-coded absolute paths
- [ ] No mandatory external dependencies (keep it Pythonista-compatible)

---

© PCVR STUDIOS 2026
