# PCVR Studios

[![License: MIT](https://img.shields.io/badge/License-MIT-7f5af0.svg)](./LICENSE)
[![CI](https://github.com/AIVaneer/AIVaneer-PCVR-Studios/actions/workflows/ci.yml/badge.svg)](https://github.com/AIVaneer/AIVaneer-PCVR-Studios/actions/workflows/ci.yml)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-2cb67d?logo=python&logoColor=white)](https://www.python.org/)
[![Pythonista 3](https://img.shields.io/badge/Pythonista%203-iOS-blue?logo=apple&logoColor=white)](https://omz-software.com/pythonista/)
[![20+ Modules](https://img.shields.io/badge/Eve%20Toolkit-20%2B%20modules-5b8dee)](./eve_toolkit/)

> **Community-Focused 🚀 PCVR Studios HQ** — Games, DeFi tools, and crypto economy systems.
> Built on the **Atlas Nexus Engine** for iOS Pythonista 3. Open source, community driven.

---

## "Don't Die" Philosophy

Every play-to-earn project dies the same way: token launches, players earn for free, players
sell immediately, price crashes, community leaves. **We refuse to let that happen.**

The PCVR Coin economy is built around a closed loop — **Earn → Hold → Spend → Buy** — where
the token is the *currency* of the ecosystem, not just a reward. Burns on every purchase,
real-revenue-backed staking, and anti-farming controls keep the economy alive. Read the full
plan in [`docs/token_economy.md`](./docs/token_economy.md).

---

## ✨ Module Overview

| Module | Description |
|---|---|
| [`skyburner/`](./skyburner/) | **SkyBurner Ultimate** — arcade space-shooter powered by the Atlas Nexus Engine |
| [`eve_toolkit/`](./eve_toolkit/) | **Eve DeFi Toolkit v10** — 20+ modules: market data, risk analytics, whale tracking, automation, multichain, smart integrations, and more |
| [`project_dont_die/`](./project_dont_die/) | **Token Economy Survival** — treasury, burn schedules, and staking for PCVR Coin |
| [`dashboard/`](./dashboard/) | **Web Dashboard** — dark-theme landing page, GitHub Pages compatible |

### Eve Toolkit Modules

| Module | Description |
|---|---|
| `atlas_omega.py` | Master command center — runs all modules |
| `dashboard.py` | Terminal dashboard renderer |
| `economy.py` | Supply / velocity / market-cap analytics |
| `market.py` | Live price & OHLCV data |
| `whale_tracker.py` | Large-wallet monitoring |
| `risk.py` | Volatility & drawdown calculations |
| `scenario.py` | What-if scenario modelling |
| `automation.py` | Automated trading / task runner |
| `multichain.py` | Multi-blockchain support |
| `smart_integrations.py` | Third-party API integrations |
| `github_sync.py` | GitHub data sync & reporting |
| `validate.py` | Data validation utilities |
| `store.py` | In-game store economy |
| `history.py` | Historical data storage |
| `token_data.py` | Token metadata & on-chain data |
| `atlas_graph_core.py` | Graph / charting core |
| `detector.py` | Anomaly & pattern detection |
| `vault.py` | Vault & wallet management |
| `alert.py` | Price & event alerts |
| `run_all.py` | Batch runner |
| `wkapp_ui.py` | Pythonista UI components |

---

## 🎮 Games Library

### SkyBurner Ultimate — Flagship Title

> **Platform:** Pythonista 3 / iOS (iPhone & iPad)
> **Engine:** Atlas Nexus Engine v1.0
> **Language:** 100% Python — zero external assets

A high-octane, vertical-scrolling arcade space-shooter. Three clean Python files power the
entire experience — every sprite, explosion, and star is drawn with Python's built-in modules.

| Feature | Detail |
|---|---|
| 🔫 Weapon Tiers | Single laser → Dual cannon → Triple spread → Homing missiles |
| 👾 Enemy Types | Fighter, Cruiser & Boss (every 5th wave) |
| 💥 Multi-Phase Bosses | Entry → Attack 1 → Attack 2 → Rage mode |
| ⚡ Combo System | Kill-streak multiplier up to ×8 |
| 🛡 Power-Ups | Weapon upgrade, shield boost, health pack, extra bomb, speed burst |
| 🌌 Starfield | 115-star parallax scrolling backdrop |
| 📱 Touch Controls | Drag to move, tap to bomb — auto-fire |

**Downloads (via Discord):**
- 🎮 [Game Download](https://discord.com/channels/1316937801995911198/1484003872178573495/1484552464639332605)
- 🎵 [Music Download](https://discord.com/channels/1316937801995911198/1484003872178573495/1484595490828845229)

**Repository:** [SkyBurner-Ultimate-pythonista-game-](https://github.com/AIVaneer/SkyBurner-Ultimate-pythonista-game-)

---

## 🏗 Architecture

```
AIVaneer-PCVR-Studios/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml            # flake8 + pytest (Python 3.10–3.12)
│   │   └── pages.yml         # GitHub Pages deployment
│   ├── FUNDING.yml           # GitHub Sponsors
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── PULL_REQUEST_TEMPLATE.md
├── skyburner/                # SkyBurner Ultimate (Atlas Nexus Engine)
│   ├── atlas_nexus.py        #   Core game engine
│   ├── entities.py           #   Player, enemies, projectiles, power-ups
│   └── main_scene.py         #   Entry-point scene
├── eve_toolkit/              # Eve DeFi Toolkit v10 (20+ modules)
│   ├── atlas_omega.py        #   Master command center
│   ├── dashboard.py          #   Terminal dashboard
│   ├── economy.py            #   Analytics
│   └── ...                   #   20+ more modules
├── project_dont_die/         # Token Economy Survival Tools
│   └── token_economy.py      #   Treasury, BurnSchedule, StakingPool
├── dashboard/
│   ├── index.html            #   Full PCVR Studios web dashboard (18KB)
│   └── README.md             #   GitHub Pages setup guide
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_skyburner.py
│   ├── test_eve_toolkit.py
│   └── test_project_dont_die.py
├── docs/
│   ├── quickstart.md         # Getting started guide
│   ├── architecture.md       # App architecture plan
│   ├── token_economy.md      # "Don't Die" economy plan
│   ├── pythonista_setup.md   # iOS setup tutorial
│   └── adding_modules.md     # How to contribute modules
├── LEGALITY.md               # Legality & compliance
├── WHITEPAPER.md             # PCVR Studios white paper v2.0
├── vault_code_repository     # Vault dashboard (Pythonista UI)
├── SECURITY.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── LICENSE
└── README.md
```

---

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

Copy any module folder directly into your Pythonista 3 project directory and run — zero C
extensions, zero mandatory external dependencies. See [`docs/pythonista_setup.md`](./docs/pythonista_setup.md).

---

## 💰 PCVR Coin

| | |
|---|---|
| **Token** | PCVR Coin (PCVR) |
| **Blockchain** | Cronos |
| **Contract** | `0x05c870C5C6E7AF4298976886471c69Fc722107e4` |
| **DexScreener** | [View Chart](https://dexscreener.com/cronos/0x5a84Add7Ad701409F16C2c5B1CE213b024BCE68a) |
| **Status** | ✅ Live & Tradeable |

---

## 🤝 Community

| | |
|---|---|
| 💬 Discord | [discord.gg/E7bW3Zh4x](https://discord.gg/E7bW3Zh4x) |
| 🐦 Twitter / X | [@pcvr2024](https://twitter.com/pcvr2024) |
| 🌐 Website | [pcvr.lol](https://pcvr.lol) |
| ❤️ Sponsor | [GitHub Sponsors](https://github.com/sponsors/AIVaneer) |

---

## 📄 License

MIT — see [LICENSE](./LICENSE).

© PCVR STUDIOS 2026

