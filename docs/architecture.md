# System Architecture — PCVR Studios

> Migrated and expanded from `APP_ARCHITECTURE.md` (Eve-Repository)

---

## Monorepo Structure

```
AIVaneer-PCVR-Studios/
├── .github/                    # CI/CD, issue templates, PR template
│   ├── workflows/
│   │   ├── ci.yml              # flake8 lint + pytest (Python 3.8–3.12)
│   │   └── pages.yml           # Deploy dashboard/ to GitHub Pages
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── FUNDING.yml
│
├── eve_toolkit/                # PCVR DeFi Toolkit (V10)
│   ├── atlas_omega.py          # V9 Command Center — 19 commands
│   ├── live_data.py            # V8 DexScreener/Binance market data
│   ├── economy.py              # V7 Tokenomics engine
│   ├── vault.py                # V7 Staking vault
│   ├── alert.py                # V8 Risk engine
│   ├── whale_tracker.py        # V8 Whale analysis, Gini
│   ├── scenario.py             # V7/8 Simulation (7 scenarios)
│   ├── detector.py             # V8 Debasement detection
│   ├── store.py                # V7 In-game store
│   ├── history.py              # V7 Transaction ledger
│   ├── token_data.py           # V7 Token constants
│   ├── github_sync.py          # V9 GitHub integration
│   ├── validate.py             # V9 Health validation
│   ├── atlas_graph_core.py     # V9 Economy graph
│   ├── smart_integrations.py   # V10 AI (Tavily, Firecrawl)
│   ├── dashboard.py            # V10 HTTP dashboard server
│   ├── dashboard_template.html # V10 Chart.js template
│   ├── automation.py           # V10 Automation engine
│   ├── wkapp_ui.py             # V10 iOS WKWebView UI
│   ├── multichain.py           # V10 8-chain tracker
│   └── run_all.py              # System runner
│
├── skyburner/                  # SkyBurner Ultimate (V1.0)
│   ├── atlas_nexus.py          # Atlas Nexus Engine core
│   ├── entities.py             # Game entities
│   └── skyburner.py            # Main game scene
│
├── dashboard/                  # GitHub Pages static site
│   └── index.html
│
├── tests/                      # Pytest test suite (99 tests)
│   ├── conftest.py
│   ├── test_eve_toolkit.py
│   ├── test_skyburner.py
│   └── test_atlas_omega.py
│
└── docs/                       # Documentation
```

---

## Eve Toolkit — Layer Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    ATLAS OMEGA V9                        │
│              Unified Command Center (19 cmds)            │
└─────────┬───────────────────────┬───────────────────────┘
          │                       │
┌─────────▼─────────┐   ┌────────▼──────────────────────┐
│   V10 LAYER       │   │      V8/V9 LAYER               │
│ smart_integrations│   │  live_data  validate            │
│ dashboard         │   │  whale_tracker  alert           │
│ automation        │   │  github_sync  detector          │
│ wkapp_ui          │   │  atlas_graph_core               │
│ multichain        │   └────────────────────────────────┘
└─────────┬─────────┘
          │
┌─────────▼──────────────────────────────────────────────┐
│                   V7 FOUNDATION                         │
│   economy  vault  store  history  token_data  scenario  │
└────────────────────────────────────────────────────────┘
```

---

## Atlas Nexus Engine — Component Architecture

```
┌───────────────────────────────────────────┐
│           AtlasNexusEngine                │
│  entity_manager   collision_manager       │
│  score_manager    wave_manager            │
└────────┬──────────────┬───────────────────┘
         │              │
┌────────▼──────┐  ┌────▼──────────────────┐
│ EntityManager │  │  ScoreManager          │
│  Entity[]     │  │  WaveManager           │
│  tag index    │  │  CollisionManager      │
└────────┬──────┘  └───────────────────────┘
         │
┌────────▼──────────────────────────────────┐
│             Entity                         │
│  TransformComponent  HealthComponent       │
│  WeaponComponent     ShieldComponent       │
└───────────────────────────────────────────┘
```

---

## Data Flow — Eve Toolkit

```
External APIs (DexScreener, Binance, Cronos RPC)
    │
    ▼
live_data.py ──→ raw_market_data
    │
    ├──→ alert.py      (risk scoring, threshold detection)
    ├──→ whale_tracker (wallet concentration, Gini)
    ├──→ scenario.py   (what-if simulations)
    └──→ atlas_omega   (aggregation, reporting)
            │
            ├──→ dashboard.py  (HTTP server, Chart.js)
            ├──→ automation.py (rule engine, responses)
            └──→ wkapp_ui.py   (iOS WKWebView)

economy.py ↔ vault.py ↔ store.py ↔ history.py
    (token loop: Earn → Hold → Spend → Buy → Earn)
```

---

## CI Pipeline

```
git push
    │
    ▼
GitHub Actions (ci.yml)
    │
    ├── Python 3.8  ─┐
    ├── Python 3.9  ─┤─→ flake8 (syntax + style)
    ├── Python 3.10 ─┤─→ pytest tests/ (99 tests)
    ├── Python 3.11 ─┤
    └── Python 3.12 ─┘

On main push:
    └──→ pages.yml → Deploy dashboard/ to GitHub Pages
```

---

## Principles

1. **Pythonista 3 first** — all code runs on iOS via Pythonista 3
2. **Graceful imports** — `try/except` on every cross-module import
3. **Standard library preferred** — `requests` is the only external dependency
4. **Self-contained modules** — each module works standalone
5. **`_DIR`-relative paths** — data files written next to the module
6. **Earn → Hold → Spend → Buy → Earn** — every feature reinforces this loop
