# Changelog

All notable changes to the PCVR Studios monorepo are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [Unreleased]

### Added
- Unified PCVR Studios monorepo consolidating Eve-Repository and SkyBurner-Ultimate-pythonista-game-
- `eve_toolkit/` package (V10.0.0) with all 20+ DeFi toolkit modules
- `skyburner/` package (V1.0.0) with Atlas Nexus Engine and game files
- `dashboard/` static site (GitHub Pages ready)
- `.github/` infrastructure: CI workflow, Pages deployment, issue templates, PR template, FUNDING.yml
- `tests/` full pytest suite — 99 tests covering eve_toolkit and skyburner
- `docs/` documentation hub: quickstart, architecture, token economy, Pythonista setup, adding modules
- Unified `CONTRIBUTING.md` and `CHANGELOG.md`
- Comprehensive `.gitignore`
- Master `README.md` with badges, architecture diagram, and full documentation

---

## Eve Toolkit History

### [10.0.0] — 2026-03-21

#### Added
- V10: `smart_integrations.py` — AI intelligence via Tavily and Firecrawl
- V10: `dashboard.py` + `dashboard_template.html` — web dashboard with Chart.js
- V10: `automation.py` — automation engine with 10 built-in rules
- V10: `wkapp_ui.py` — iOS native UI via WKWebView
- V10: `multichain.py` — multi-chain tracker covering 8 blockchains

### [9.0.0] — 2026-01-15

#### Added
- V9: `atlas_omega.py` — unified command center (19 commands)
- V9: `atlas_graph_core.py` — economy graph engine

### [8.0.0] — 2025-11-01

#### Added
- V8: `github_sync.py` — GitHub repository integration
- V8: `validate.py` — system health validation
- V8: `live_data.py` — live market data from DexScreener/Binance

### [7.0.0] — 2025-09-01

#### Added
- V7: `store.py` — in-game store with auto-burn on purchase
- V7: `history.py` — persistent transaction ledger
- V7: `token_data.py` — PCVR token constants and metadata

### [6.0.0] — 2025-07-01

#### Added
- V6: `scenario.py` — simulation engine with 7 scenarios
- V6: `detector.py` — debasement pattern detection

### [5.0.0] — 2025-05-01

#### Added
- V5: `whale_tracker.py` — whale analysis and Gini coefficient

### [4.0.0] — 2025-03-01

#### Added
- V4: `alert.py` — risk engine and alert system

### [3.0.0] — 2025-01-15

#### Added
- V3: `vault.py` — staking vault (90-day lock)

### [2.0.0] — 2024-12-01

#### Added
- V2: `economy.py` — tokenomics engine (Earn → Hold → Spend → Buy → Earn)

### [1.0.0] — 2024-10-01

#### Added
- V1: `live_data.py` (initial) — market data from DexScreener

---

## SkyBurner History

### [1.0.0] — 2026-03-21

#### Added
- Initial public release of SkyBurner Ultimate
- Atlas Nexus Engine — custom entity-component system with AABB collision
- 4 weapon tiers: Single laser → Dual cannon → Triple spread → Homing missiles
- 3 enemy types: Fighter, Cruiser, Boss (every 5th wave)
- Multi-phase boss system: Entry → Attack 1 → Attack 2 → Rage mode
- Combo system with kill-streak multiplier (up to ×8)
- 5 power-up types: Weapon, shield, health, bomb, speed
- 115-star parallax scrolling starfield
- Full HUD: Score, high-score, health, shield, lives, bombs, wave, boss health
- Touch controls: Drag to move, tap to bomb, auto-fire

---

*© PCVR STUDIOS 2026 — Contract: `0x05c870C5C6E7AF4298976886471c69Fc722107e4`*
