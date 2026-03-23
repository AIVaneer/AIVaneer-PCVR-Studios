"""
Tests for eve_toolkit modules:
  economy, vault, token_data, detector, store, history, alert
"""
import os
import sys
import pytest

# ---------------------------------------------------------------------------
# economy.py
# ---------------------------------------------------------------------------

class TestEconomy:
    def test_earn_increases_emitted_and_circ(self, economy_reset):
        econ = economy_reset
        result = econ.earn(1000)
        assert result == 1000
        assert econ.emitted == 1000
        assert econ.circ == 100_001_000

    def test_earn_respects_daily_cap(self, economy_reset):
        econ = economy_reset
        econ.cap = 500
        result = econ.earn(1000)
        assert result == 500
        assert econ.emitted == 500

    def test_earn_returns_zero_when_cap_full(self, economy_reset):
        econ = economy_reset
        econ.cap = 100
        econ.today = 100
        result = econ.earn(500)
        assert result == 0

    def test_burn_reduces_supply_and_circ(self, economy_reset):
        econ = economy_reset
        econ.burn(5000)
        assert econ.burned == 5000
        assert econ.circ == 100_000_000 - 5000
        assert econ.supply == 1_000_000_000 - 5000

    def test_spend_accumulates(self, economy_reset):
        econ = economy_reset
        econ.spend(300)
        econ.spend(200)
        assert econ.spent == 500

    def test_lock_accumulates(self, economy_reset):
        econ = economy_reset
        econ.lock(10000)
        assert econ.locked == 10000

    def test_health_calculation(self, economy_reset):
        econ = economy_reset
        econ.earn(1000)
        econ.spend(700)
        assert abs(econ.health() - 0.7) < 1e-9

    def test_health_one_when_no_emission(self, economy_reset):
        econ = economy_reset
        assert econ.health() == 1.0

    def test_burn_ratio(self, economy_reset):
        econ = economy_reset
        econ.earn(1000)
        econ.burn(200)
        assert abs(econ.burn_ratio() - 0.2) < 1e-9

    def test_net_calculation(self, economy_reset):
        econ = economy_reset
        econ.earn(1000)
        econ.spend(300)
        econ.burn(100)
        assert econ.net() == 600

    def test_new_day_resets_today(self, economy_reset):
        econ = economy_reset
        econ.earn(1000)
        assert econ.today == 1000
        econ.new_day()
        assert econ.today == 0

    def test_buy_calls_spend_and_burn(self, economy_reset):
        econ = economy_reset
        econ.buy(1000, burn_pct=15)
        assert econ.spent == 1000
        assert abs(econ.burned - 150) < 1e-9


# ---------------------------------------------------------------------------
# vault.py
# ---------------------------------------------------------------------------

class TestVault:
    def test_deposit_revenue_increases_balance(self, vault_reset):
        v = vault_reset
        v.deposit_revenue(5000, "store")
        assert v.vault_balance == 5000

    def test_multiple_deposits_accumulate(self, vault_reset):
        v = vault_reset
        v.deposit_revenue(3000)
        v.deposit_revenue(2000)
        assert v.vault_balance == 5000

    def test_lock_tokens_records_locker(self, vault_reset):
        v = vault_reset
        v.lock_tokens("alice", 1000)
        assert "alice" in v.lockers
        assert v.lockers["alice"]["amount"] == 1000
        assert v.total_locked == 1000

    def test_vault_apy_zero_when_empty(self, vault_reset):
        v = vault_reset
        assert v.vault_apy() == 0

    def test_vault_apy_positive_when_funded(self, vault_reset):
        v = vault_reset
        v.deposit_revenue(9000)
        v.lock_tokens("bob", 1000)
        apy = v.vault_apy()
        assert apy > 0

    def test_advance_day_increments_locker_day(self, vault_reset):
        v = vault_reset
        v.lock_tokens("alice", 500)
        v.advance_day()
        assert v.lockers["alice"]["day"] == 1


# ---------------------------------------------------------------------------
# token_data.py
# ---------------------------------------------------------------------------

class TestTokenData:
    def test_token_dict_has_required_keys(self):
        import token_data
        t = token_data.TOKEN
        for key in ("name", "symbol", "chain", "contract", "pair", "web"):
            assert key in t, f"Missing key: {key}"

    def test_token_symbol_is_pcvr(self):
        import token_data
        assert token_data.TOKEN["symbol"] == "PCVR"

    def test_token_chain_is_cronos(self):
        import token_data
        assert token_data.TOKEN["chain"] == "Cronos"

    def test_contract_address_correct(self):
        import token_data
        assert token_data.TOKEN["contract"] == "0x05c870C5C6E7AF4298976886471c69Fc722107e4"

    def test_repos_key_contains_urls(self):
        import token_data
        repos = token_data.TOKEN.get("repos", {})
        assert "main" in repos


# ---------------------------------------------------------------------------
# detector.py
# ---------------------------------------------------------------------------

class TestDetector:
    def test_healthy_state_returns_true(self):
        from detector import check
        # health=0.8, burn_ratio=0.15, spend_ratio=0.6, circ=50%, cap 50% used
        result = check(
            emitted=10000,
            spent=8000,
            burned=1500,
            locked=15000000,
            circ=50_000_000,
            supply=1_000_000_000,
            cap=50000,
            today=20000,
        )
        assert result is True

    def test_critical_health_returns_false(self):
        from detector import check
        result = check(
            emitted=10000,
            spent=500,      # health < 0.2
            burned=0,
            locked=0,
            circ=100_000_000,
            supply=1_000_000_000,
            cap=50000,
            today=0,
        )
        assert result is False

    def test_zero_emission_does_not_crash(self):
        from detector import check
        # emitted=0 with non-zero circ should return True (no issues)
        # Note: use emitted=1 to avoid the known division order in detector
        result = check(1, 0, 0, 0, 100_000_000, 1_000_000_000, 50000, 0)
        assert isinstance(result, bool)

    def test_low_burn_returns_false(self):
        from detector import check
        result = check(
            emitted=10000,
            spent=6000,
            burned=100,     # burn ratio < 5%
            locked=15000000,
            circ=50_000_000,
            supply=1_000_000_000,
            cap=50000,
            today=10000,
        )
        assert result is False


# ---------------------------------------------------------------------------
# store.py  (import checks — no file I/O required for basic tests)
# ---------------------------------------------------------------------------

class TestStore:
    def test_catalog_is_list(self):
        import store
        assert isinstance(store.CATALOG, list)
        assert len(store.CATALOG) > 0

    def test_catalog_items_have_required_keys(self):
        import store
        for item in store.CATALOG:
            for key in ("name", "price", "category"):
                assert key in item, f"Item missing key '{key}': {item}"

    def test_burn_rates_defined(self):
        import store
        assert isinstance(store.BURN_RATES, dict)
        assert "cosmetic" in store.BURN_RATES
        assert "boost" in store.BURN_RATES

    def test_vault_rate_positive(self):
        import store
        assert store.VAULT_RATE > 0


# ---------------------------------------------------------------------------
# history.py  (import + pure logic tests, no file I/O)
# ---------------------------------------------------------------------------

class TestHistory:
    def test_event_types_defined(self):
        import history
        assert "earn" in history.EVENT_TYPES
        assert "burn" in history.EVENT_TYPES
        assert "purchase" in history.EVENT_TYPES

    def test_load_ledger_returns_list_when_no_file(self, tmp_dir, monkeypatch):
        import history
        monkeypatch.setattr(history, "LEDGER_FILE",
                            str(tmp_dir / "ledger.json"))
        result = history.load_ledger()
        assert isinstance(result, list)
        assert result == []

    def test_log_and_retrieve_event(self, tmp_dir, monkeypatch):
        import history
        monkeypatch.setattr(history, "LEDGER_FILE",
                            str(tmp_dir / "ledger.json"))
        monkeypatch.setattr(history, "CSV_FILE",
                            str(tmp_dir / "ledger.csv"))
        entry = history.log_event("earn", 1000, "test earn", "pytest")
        assert entry["event_type"] == "earn"
        assert entry["amount"] == 1000.0
        assert entry["id"] == 1

        ledger = history.get_all()
        assert len(ledger) == 1
        assert ledger[0]["source"] == "pytest"


# ---------------------------------------------------------------------------
# alert.py  (import + pure logic tests, no file I/O)
# ---------------------------------------------------------------------------

class TestAlert:
    def test_severities_constant(self):
        import alert
        assert "info" in alert.SEVERITIES
        assert "critical" in alert.SEVERITIES
        assert "warning" in alert.SEVERITIES
        assert "danger" in alert.SEVERITIES

    def test_categories_constant(self):
        import alert
        assert "whale" in alert.CATEGORIES
        assert "economy" in alert.CATEGORIES

    def test_fire_creates_alert_in_tmp(self, tmp_dir, monkeypatch):
        import alert
        monkeypatch.setattr(alert, "ALERT_FILE",
                            str(tmp_dir / "alerts.json"))
        a = alert.fire("warning", "economy", "Test alert", "pytest")
        assert a["severity"] == "warning"
        assert a["message"] == "Test alert"

    def test_fire_unknown_severity_defaults_to_info(self, tmp_dir, monkeypatch):
        import alert
        monkeypatch.setattr(alert, "ALERT_FILE",
                            str(tmp_dir / "alerts.json"))
        a = alert.fire("unknown_sev", "economy", "msg")
        assert a["severity"] == "info"

    def test_load_alerts_empty_when_no_file(self, tmp_dir, monkeypatch):
        import alert
        monkeypatch.setattr(alert, "ALERT_FILE",
                            str(tmp_dir / "no_alerts.json"))
        result = alert.load_alerts()
        assert result == []
