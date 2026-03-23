# PCVR Studios — Unified Monorepo

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/AIVaneer/AIVaneer-PCVR-Studios/actions/workflows/ci.yml/badge.svg)](https://github.com/AIVaneer/AIVaneer-PCVR-Studios/actions/workflows/ci.yml)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Pythonista 3](https://img.shields.io/badge/Platform-Pythonista%203%20%7C%20iOS-orange.svg)](http://omz-software.com/pythonista/)
[![Modules](https://img.shields.io/badge/Modules-20%2B-blueviolet.svg)]()
[![Chains](https://img.shields.io/badge/Chains-8-green.svg)]()
[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ea4aaa.svg)](https://github.com/sponsors/AIVaneer)

> **PCVR Studios** — Games, DeFi tools, and crypto economy systems.  
> Built on the **Atlas Nexus Engine** for iOS Pythonista 3. Open source. Community driven.

**Contract:** `0x05c870C5C6E7AF4298976886471c69Fc722107e4` (Cronos)  
**Website:** [pcvr.lol](https://pcvr.lol) · **Discord:** [discord.gg/E7bW3Zh4x](https://discord.gg/E7bW3Zh4x) · **Twitter:** [@pcvr2024](https://x.com/pcvr2024)

---

## Table of Contents

- [What is this?](#-what-is-this)
- [The Don't Die Philosophy](#-the-dont-die-philosophy)
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [Eve Toolkit — Module Overview](#-eve-toolkit--module-overview)
- [Games Library](#-games-library)
- [API Reference](#-api-reference--dashboard-endpoints)
- [Roadmap](#-roadmap)
- [Community](#-community)
- [License](#-license)

---

## 🎮 What is this?

**PCVR Studios** is the unified home for all PCVR projects:

| Package | Description |
|---------|-------------|
| [`eve_toolkit/`](eve_toolkit/) | 20+ Python modules for monitoring, analyzing, and automating the PCVR token economy on Cronos |
| [`skyburner/`](skyburner/) | SkyBurner Ultimate — full arcade space-shooter powered by the Atlas Nexus Engine |
| [`dashboard/`](dashboard/) | Dark-theme GitHub Pages site — PCVR web presence |

All code runs on **Pythonista 3 (iOS)** and **desktop Python 3.8+**. The only external dependency is `requests`.

---

## 💀 The "Don't Die" Philosophy

Every token has a lifecycle. Most die from neglect, manipulation, or economic collapse. **Project Don't Die** exists to prevent exactly that.

```
Earn → Hold → Spend → Buy → Earn
```

If any link in that chain breaks, the token dies. The toolkit watches the chain 24/7, spots danger before it becomes a crisis, and automates the responses that humans would be too slow — or too distracted — to execute.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  ATLAS OMEGA V9                          │
│           Unified Command Center (19 commands)           │
└──────────┬────────────────────────┬─────────────────────┘
           │                        │
┌──────────▼──────────┐  ┌──────────▼────────────────────┐
│    V10 LAYER         │  │       V8/V9 LAYER              │
│  smart_integrations  │  │  live_data   validate          │
│  dashboard           │  │  whale_tracker  alert          │
│  automation          │  │  github_sync  detector         │
│  wkapp_ui  multichain│  │  atlas_graph_core              │
└──────────┬──────────┘  └───────────────────────────────┘
           │
┌──────────▼─────────────────────────────────────────────┐
│                  V7 FOUNDATION                          │
│   economy  vault  store  history  token_data  scenario  │
└────────────────────────────────────────────────────────┘

SkyBurner / Atlas Nexus Engine (separate package):
┌──────────────────────────────────────────────────────────┐
│  AtlasNexusEngine                                        │
│    EntityManager  CollisionManager                       │
│    ScoreManager   WaveManager                            │
│    Entity → [TransformComponent, HealthComponent, ...]   │
└──────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### Desktop — Eve Toolkit

```bash
git clone https://github.com/AIVaneer/AIVaneer-PCVR-Studios.git
cd AIVaneer-PCVR-Studios
pip install requests

cd eve_toolkit
python run_all.py          # Full system check
python atlas_omega.py      # Command center (19 commands)
python dashboard.py        # Web dashboard at localhost:8080
python automation.py       # Start automation engine
```

### Pythonista 3 (iOS)

```python
# Copy eve_toolkit/ files to your Pythonista project, then:
import run_all          # Full system check
import atlas_omega      # Command center
import wkapp_ui         # Native iOS interface
```

### SkyBurner (Pythonista 3)

1. Copy `skyburner/atlas_nexus.py`, `entities.py`, `skyburner.py` to Pythonista
2. Open `skyburner.py` → tap ▶ Run

### Run Tests

```bash
pip install pytest
pytest tests/ -v   # 99 tests
```

---

## 📦 Eve Toolkit — Module Overview

| Module | Version | Description |
|--------|---------|-------------|
| `atlas_omega.py` | V9 | Unified Command Center — 19 commands |
| `live_data.py` | V8 | Market data from DexScreener/Binance |
| `economy.py` | V7 | Tokenomics engine (Earn→Hold→Spend→Buy) |
| `vault.py` | V7 | Staking vault with 90-day lock |
| `alert.py` | V8 | Risk engine — 4 severity levels |
| `whale_tracker.py` | V8 | Wallet concentration, Gini coefficient |
| `scenario.py` | V7/V8 | Simulation engine — 7 scenarios |
| `detector.py` | V8 | Debasement pattern detection |
| `store.py` | V7 | In-game store with auto-burn |
| `history.py` | V7 | Persistent transaction ledger |
| `token_data.py` | V7 | PCVR token constants & metadata |
| `github_sync.py` | V9 | GitHub repository integration |
| `validate.py` | V9 | System health validation |
| `atlas_graph_core.py` | V9 | Economy graph engine |
| `smart_integrations.py` | V10 | AI intelligence (Tavily, Firecrawl) |
| `dashboard.py` | V10 | Web dashboard server (Chart.js) |
| `dashboard_template.html` | V10 | Dashboard HTML template |
| `automation.py` | V10 | Automation engine — 10 built-in rules |
| `wkapp_ui.py` | V10 | iOS native UI via WKWebView |
| `multichain.py` | V10 | Multi-chain tracker (8 blockchains) |
| `run_all.py` | All | Full system runner |

Full API docs: [eve_toolkit/MODULES.md](eve_toolkit/MODULES.md)

---

## 🎮 Games Library

| Game | Platform | Description |
|------|----------|-------------|
| 🚀 **SkyBurner Ultimate** | Pythonista 3 / iOS | 100% Python arcade space-shooter. Atlas Nexus Engine. 4 weapon tiers, multi-phase bosses, ×8 combo system. |
| 🌀 **Warp Protocol** | Pythonista 3 / iOS | Fast-paced arcade shooter with cinematic intro, dynamic starfield, and enemy archetypes. |
| 🎮 **PCVR Game Shell** | Oculus Quest 3 | Foundational 2D VR game framework. Open-source under MIT. |

### Downloads

Downloads are hosted on Discord — [join free](https://discord.gg/E7bW3Zh4x) to access them.

---

## 📡 API Reference — Dashboard Endpoints

The `dashboard.py` HTTP server exposes these endpoints at `http://localhost:8080`:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Dashboard web UI (Chart.js) |
| `/api/data` | GET | Aggregated snapshot — all modules |
| `/api/market` | GET | Price, volume, liquidity from DexScreener |
| `/api/economy` | GET | Economy state: emitted, burned, health |
| `/api/risk` | GET | Risk score and active alerts |
| `/api/whale` | GET | Wallet concentration and Gini |
| `/api/sentiment` | GET | Sentiment analysis data |
| `/api/health` | GET | System health and module status |

All endpoints return `Content-Type: application/json`. The `/api/data` endpoint aggregates all others.

---

## 🗺️ Roadmap

| Version | Status | Highlights |
|---------|--------|------------|
| V1–V3 | ✅ Complete | Market data, tokenomics, staking vault |
| V4–V6 | ✅ Complete | Risk engine, whale tracking, simulation, pattern detection |
| V7 | ✅ Complete | In-game store, transaction ledger, event history |
| V8 | ✅ Complete | GitHub sync, system validation, live market data |
| V9 | ✅ Complete | Atlas Omega command center, graph engine |
| V10 | ✅ Complete | AI intelligence, web dashboard, automation, iOS UI, multi-chain |
| V11 | 🔮 Future | Advanced AI predictions, social media monitoring, predictive analytics |
| V12 | 🔮 Future | DAO integration, on-chain governance, community tools |

---

## 🤝 Community

| Platform | Link |
|----------|------|
| 💬 Discord | [discord.gg/E7bW3Zh4x](https://discord.gg/E7bW3Zh4x) |
| 🐦 Twitter/X | [@pcvr2024](https://x.com/pcvr2024) |
| 🌐 Website | [pcvr.lol](https://pcvr.lol) |
| 💰 GitHub Sponsors | [Sponsor AIVaneer](https://github.com/sponsors/AIVaneer) |

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

*© PCVR STUDIOS 2026 — Contract: `0x05c870C5C6E7AF4298976886471c69Fc722107e4` (Cronos)*

