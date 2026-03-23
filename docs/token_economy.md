# PCVR Token Economy

> Combined from PROJECT_DONT_DIE.md and WHITEPAPER.md (Eve-Repository)

---

## The Don't Die Philosophy

Every token has a lifecycle. Most die from neglect, manipulation, or economic collapse. Project Don't Die exists to prevent exactly that.

```
Earn → Hold → Spend → Buy → Earn
```

If any link in that chain breaks, the token dies. The toolkit exists to ensure it never does.

---

## Token Details

| Field | Value |
|-------|-------|
| Name | PCVR Coin |
| Symbol | PCVR |
| Chain | Cronos |
| Contract | `0x05c870C5C6E7AF4298976886471c69Fc722107e4` |
| Pair | `0x5a84Add7Ad701409F16C2c5B1CE213b024BCE68a` |
| DEX | [DexScreener](https://dexscreener.com/cronos/0x5a84Add7Ad701409F16C2c5B1CE213b024BCE68a) |
| Explorer | [CronoScan](https://cronoscan.com/token/0x05c870C5C6E7AF4298976886471c69Fc722107e4) |
| Website | [pcvr.lol](https://pcvr.lol) |

---

## The Economic Loop

### Earn
Players and holders earn PCVR through:
- In-game rewards (SkyBurner, Warp Protocol, etc.)
- Community events and tournaments
- Staking vault returns (from real revenue)

Daily emission cap enforced by `economy.py` to prevent inflation.

### Hold
Holders stake PCVR in the 90-day Earnings Vault (`vault.py`):
- Real revenue (store sales, tournament fees) fills the vault
- Stakers earn proportional yield
- Lock ratio target: >20% of circulating supply

### Spend
Every in-game purchase (`store.py`) automatically:
- Burns 15–30% of the purchase price (by category)
- Deposits 10% to the staking vault
- Records the event in the transaction ledger

### Buy
The Earn → Hold → Spend cycle creates natural buy pressure:
- Burn reduces circulating supply
- Vault yield attracts new holders
- Store demand requires PCVR to purchase

---

## Risk System

The `alert.py` and `detector.py` modules implement a multi-tier risk engine:

| Level | Color | Trigger |
|-------|-------|---------|
| Info | ℹ️ | Volume spike, milestone reached |
| Warning | ⚠️ | Health < 0.7, lock ratio < 10% |
| Danger | 🔴 | Health < 0.5, high concentration |
| Critical | 🚨 | Health < 0.2, death spiral detected |

---

## Tokenomics Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| Health | `spent / emitted` | ≥ 0.7 |
| Burn Ratio | `burned / emitted` | ≥ 15% |
| Lock Ratio | `locked / circ` | ≥ 20% |
| Gini Coefficient | wallet concentration | ≤ 0.6 |

---

## Automation Rules

The `automation.py` engine runs 10 rules on every tick:

| Rule | Trigger | Action |
|------|---------|--------|
| `dump_alert` | Price drop >15% in 1h | CRITICAL alert |
| `low_liquidity` | Liquidity < $10,000 | HIGH alert |
| `whale_dump` | Single wallet sells >2% supply | HIGH alert |
| `high_concentration` | Top 10 wallets >80% supply | MEDIUM alert |
| `volume_spike` | Volume >5× 24h average | INFO alert |
| `burn_milestone` | Burn crosses threshold | Log + celebrate |
| `vault_unlock` | Large unlock approaching | WARNING |
| `scenario_death_spiral` | Multiple risk factors | CRITICAL + escalate |
| `arbitrage_opportunity` | Price gap >3% cross-chain | Log opportunity |
| `sentiment_crash` | Sentiment < −0.5 | WARNING |

---

## Multi-Chain Tracking

PCVR is tracked across 8 chains via `multichain.py`:

| Chain | Role |
|-------|------|
| Cronos | Primary chain |
| Ethereum | Bridge target |
| BSC | Bridge target |
| Polygon | Bridge target |
| Arbitrum | Bridge target |
| Optimism | Bridge target |
| Avalanche | Bridge target |
| Base | Bridge target |

---

## Roadmap

| Version | Status | Highlights |
|---------|--------|------------|
| V1–V3 | ✅ | Market data, tokenomics, staking vault |
| V4–V6 | ✅ | Risk engine, whale tracking, simulation |
| V7 | ✅ | Store, ledger, token constants |
| V8 | ✅ | GitHub sync, validation, live market data |
| V9 | ✅ | Atlas Omega command center, graph engine |
| V10 | ✅ | AI intelligence, dashboard, automation, iOS UI, multi-chain |
| V11 | 🔮 | Advanced AI predictions, social monitoring |
| V12 | 🔮 | DAO integration, on-chain governance |
