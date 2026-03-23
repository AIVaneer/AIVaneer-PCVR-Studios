# PCVR Studios

[![License: MIT](https://img.shields.io/badge/License-MIT-7f5af0.svg)](./LICENSE)
[![CI](https://github.com/AIVaneer/AIVaneer-PCVR-Studios/actions/workflows/ci.yml/badge.svg)](https://github.com/AIVaneer/AIVaneer-PCVR-Studios/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-2cb67d?logo=python&logoColor=white)](https://www.python.org/)
[![Last Commit](https://img.shields.io/github/last-commit/AIVaneer/AIVaneer-PCVR-Studios?color=46b3e6)](https://github.com/AIVaneer/AIVaneer-PCVR-Studios/commits/main)

> **Community-Focused 🚀 PCVR Studios HQ** — iOS arcade games, DeFi tools, and a crypto economy
> toolkit. Built on the **Atlas Nexus Engine** for Pythonista 3. Open source, community driven.

---

## ✨ Overview

| Module | Description |
|---|---|
| [`skyburner/`](./skyburner/) | **SkyBurner Ultimate** — arcade shooter powered by the Atlas Nexus Engine |
| [`eve_toolkit/`](./eve_toolkit/) | **Eve DeFi Toolkit** — market data, risk analytics, whale tracking, dashboard |
| [`project_dont_die/`](./project_dont_die/) | **Token Economy Survival** — treasury, burn schedules, staking for PCVR Coin |
| [`dashboard/`](./dashboard/) | **Web Dashboard** — dark-theme Chart.js UI, GitHub Pages compatible |

## 🏗 Architecture

```
AIVaneer-PCVR-Studios/
├── .github/
│   ├── workflows/ci.yml          # GitHub Actions: flake8 + pytest (Py 3.10–3.12)
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── PULL_REQUEST_TEMPLATE.md
├── skyburner/                    # SkyBurner Ultimate (Atlas Nexus Engine)
│   ├── atlas_nexus.py            #   Core game-engine stub
│   ├── entities.py               #   Player, enemies, projectiles, power-ups
│   └── main_scene.py             #   Entry-point scene
├── eve_toolkit/                  # Eve DeFi Toolkit
│   ├── market.py                 #   Price & OHLCV fetching
│   ├── economy.py                #   Supply/velocity/market-cap analytics
│   ├── risk.py                   #   Volatility & drawdown
│   ├── whale_tracker.py          #   Large-wallet monitoring
│   └── dashboard.py              #   Terminal dashboard renderer
├── project_dont_die/             # Token Economy Survival Tools
│   └── token_economy.py          #   Treasury, BurnSchedule, StakingPool
├── dashboard/
│   └── index.html                # Dark-theme web dashboard (Chart.js)
├── tests/
│   ├── test_skyburner.py
│   ├── test_eve_toolkit.py
│   └── test_project_dont_die.py
├── docs/                         # Tutorials, GIFs, API reference (coming soon)
├── SECURITY.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── LICENSE
└── README.md
```

## ⚡ Quickstart

```bash
# 1. Clone
git clone https://github.com/AIVaneer/AIVaneer-PCVR-Studios.git
cd AIVaneer-PCVR-Studios

# 2. (Optional) virtual environment
python3 -m venv .venv && source .venv/bin/activate

# 3. Install dev tools (only flake8 + pytest — no runtime dependencies)
pip install flake8 pytest

# 4. Lint
flake8 skyburner/ eve_toolkit/ project_dont_die/ tests/ --max-line-length=99

# 5. Test
pytest tests/ -v
```

### Pythonista 3 (iOS)

Copy any module folder directly into your Pythonista 3 `site-packages` or project
directory and import as normal — zero C extensions, zero external dependencies
(only `requests` is optionally used by `eve_toolkit.market`).

## 🎮 Brand

| | |
|---|---|
| **Studio** | PCVR Studios |
| **Token** | PCVR Coin (PCVR) on Cronos |
| **Engine** | Atlas Nexus Engine |
| **Theme** | Dark, professional — gaming × crypto |

## 🤝 Community

| | |
|---|---|
| 💬 Discord | [discord.gg/E7bW3Zh4x](https://discord.gg/E7bW3Zh4x) |
| 🐦 Twitter / X | [@pcvr2024](https://twitter.com/pcvr2024) |
| 🌐 Website | [pcvr.lol](https://pcvr.lol) |
| ❤️ Sponsor | [GitHub Sponsors](https://github.com/sponsors/AIVaneer) |

## 📄 License

MIT © 2026 PCVR STUDIOS — see [LICENSE](./LICENSE).

