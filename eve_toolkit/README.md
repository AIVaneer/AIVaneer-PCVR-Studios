# Eve Toolkit — PCVR DeFi Toolkit

> Part of the [PCVR Studios monorepo](../README.md)

The Eve Toolkit is a 20+ module Python system for monitoring, analyzing, and automating the PCVR token economy on Cronos. All modules run on **Pythonista 3 (iOS)** and desktop Python 3.8+.

**Philosophy:** *Earn → Hold → Spend → Buy → Earn*

**Contract:** `0x05c870C5C6E7AF4298976886471c69Fc722107e4` (Cronos)

---

## Modules

| Module | Version | Description |
|--------|---------|-------------|
| `atlas_omega.py` | V9 | Unified Command Center — 19 commands |
| `live_data.py` | V8 | Market data from DexScreener/Binance |
| `economy.py` | V7 | Tokenomics engine |
| `vault.py` | V7 | Staking vault (90-day lock) |
| `alert.py` | V8 | Risk engine and alerts |
| `whale_tracker.py` | V8 | Whale analysis, Gini coefficient |
| `scenario.py` | V7/V8 | Simulation engine (7 scenarios) |
| `detector.py` | V8 | Debasement pattern detection |
| `store.py` | V7 | In-game store with auto-burn |
| `history.py` | V7 | Persistent transaction ledger |
| `token_data.py` | V7 | PCVR token constants |
| `github_sync.py` | V9 | GitHub repository integration |
| `validate.py` | V9 | System health validation |
| `atlas_graph_core.py` | V9 | Economy graph engine |
| `smart_integrations.py` | V10 | AI intelligence (Tavily, Firecrawl) |
| `dashboard.py` | V10 | Web dashboard server |
| `dashboard_template.html` | V10 | Dashboard HTML template |
| `automation.py` | V10 | Automation engine (10 rules) |
| `wkapp_ui.py` | V10 | iOS native UI via WKWebView |
| `multichain.py` | V10 | Multi-chain tracker (8 blockchains) |
| `run_all.py` | All | Full system runner |

See [MODULES.md](MODULES.md) for full API documentation.

---

## Quick Start

### Desktop

```bash
cd eve_toolkit
pip install requests
python run_all.py          # Full system check
python atlas_omega.py      # Command center
python dashboard.py        # Web dashboard at localhost:8080
```

### Pythonista 3 (iOS)

```python
import sys
sys.path.insert(0, '/path/to/eve_toolkit')
import run_all
import atlas_omega
import wkapp_ui
```

---

## See Also

- [MODULES.md](MODULES.md) — Full module API reference
- [../docs/quickstart.md](../docs/quickstart.md) — Getting started guide
- [../docs/token_economy.md](../docs/token_economy.md) — PCVR token economy deep dive
