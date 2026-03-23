# Changelog

All notable changes to PCVR Studios are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- `skyburner/` — SkyBurner Ultimate game module placeholder
  - `atlas_nexus.py`: `AtlasNexusEngine` stub (start/stop, dimensions, fps)
  - `entities.py`: `Entity`, `PlayerShip`, `Enemy`, `Projectile`, `PowerUp` stubs
  - `main_scene.py`: `MainScene` wiring engine + player
- `eve_toolkit/` — Eve DeFi Toolkit module placeholder
  - `market.py`: `MarketClient` (price, OHLCV, order-book stubs)
  - `economy.py`: `EconomyAnalytics` (circulation ratio, velocity, market cap)
  - `risk.py`: `RiskCalculator` (volatility, max drawdown, risk score)
  - `whale_tracker.py`: `WhaleTracker` (threshold-based wallet monitoring)
  - `dashboard.py`: `TerminalDashboard` (stdout renderer)
- `project_dont_die/` — Token Economy Survival Toolkit placeholder
  - `token_economy.py`: `Treasury`, `BurnSchedule`, `StakingPool` stubs
- `dashboard/index.html` — Dark-theme web dashboard (Chart.js ready, GitHub Pages)
- `tests/` — pytest stubs for all three modules
- `.github/workflows/ci.yml` — GitHub Actions CI (flake8 + pytest, Python 3.10–3.12)
- `.github/ISSUE_TEMPLATE/bug_report.md`
- `.github/ISSUE_TEMPLATE/feature_request.md`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `docs/README.md` — Documentation placeholder
- `SECURITY.md` — Vulnerability reporting policy
- `CONTRIBUTING.md` — Contribution guidelines
- `CODE_OF_CONDUCT.md` — Contributor Covenant v2.1
- `LICENSE` — MIT License, copyright PCVR STUDIOS 2026
- `README.md` — Professional README with badges, architecture, quickstart

---

[Unreleased]: https://github.com/AIVaneer/AIVaneer-PCVR-Studios/compare/HEAD...HEAD
