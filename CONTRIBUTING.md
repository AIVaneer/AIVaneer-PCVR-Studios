# Contributing to PCVR Studios

Thank you for your interest in contributing! 🎮🚀

## Ground Rules

1. **Be respectful** — follow the [Code of Conduct](./CODE_OF_CONDUCT.md).
2. **Keep it pure Python 3** — zero external dependencies, except `requests`.  
   All code must run in **Pythonista 3 on iOS** without modification.
3. **Follow PEP 8** — maximum line length 99 characters.  
   Run `flake8 --max-line-length=99 <module>/` before submitting.
4. **Write tests** — every new function or class should have a corresponding stub  
   in `tests/` using `pytest`.
5. **Small, focused PRs** — one feature or bug fix per pull request.

## Getting Started

```bash
# Clone the repo
git clone https://github.com/AIVaneer/AIVaneer-PCVR-Studios.git
cd AIVaneer-PCVR-Studios

# (Optional) create a virtual environment
python3 -m venv .venv && source .venv/bin/activate

# Install dev dependencies
pip install flake8 pytest

# Lint
flake8 skyburner/ eve_toolkit/ project_dont_die/ tests/ --max-line-length=99

# Test
pytest tests/ -v
```

## Pull Request Process

1. Fork the repository and create a branch:  
   `git checkout -b feature/my-awesome-feature`
2. Make your changes and add tests.
3. Ensure `flake8` and `pytest` pass locally.
4. Fill out the [PR template](./.github/PULL_REQUEST_TEMPLATE.md).
5. Open a PR against `main`.

## Module Ownership

| Module             | Description                          |
|--------------------|--------------------------------------|
| `skyburner/`       | SkyBurner Ultimate — Atlas Nexus Engine |
| `eve_toolkit/`     | Eve DeFi Toolkit (market, risk, etc.) |
| `project_dont_die/`| Token Economy Survival Tools         |
| `dashboard/`       | Web Dashboard (GitHub Pages)         |

## Style Guide

- **Docstrings**: Google-style or NumPy-style, module-level and class/function-level.
- **Type hints**: encouraged but not required.
- **No f-strings with side effects** — keep formatting pure.
- **No C extensions** — must work in Pythonista 3's sandboxed environment.

## Community

- 💬 [Discord](https://discord.gg/E7bW3Zh4x)
- 🐦 [Twitter / X @pcvr2024](https://twitter.com/pcvr2024)
- 🌐 [pcvr.lol](https://pcvr.lol)
