"""
Tests for eve_toolkit/atlas_omega.py — Atlas Omega V9 Command Center.
"""
import os
import sys
import pytest

# Ensure eve_toolkit/ is importable
EVE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "eve_toolkit",
)
if EVE_PATH not in sys.path:
    sys.path.insert(0, EVE_PATH)


class TestModuleMeta:
    """atlas_omega._MODULE_META should list all V7–V10 modules."""

    def test_module_meta_contains_core_modules(self):
        import atlas_omega
        meta = atlas_omega._MODULE_META
        for name in ("economy", "vault", "token_data", "detector", "alert",
                     "store", "history", "whale_tracker", "scenario"):
            assert name in meta, f"Missing module in _MODULE_META: {name}"

    def test_module_meta_contains_v10_modules(self):
        import atlas_omega
        meta = atlas_omega._MODULE_META
        for name in ("smart_integrations", "multichain",
                     "validate", "github_sync", "live_data"):
            assert name in meta, f"Missing V10 module in _MODULE_META: {name}"

    def test_versions_are_strings(self):
        import atlas_omega
        for name, version in atlas_omega._MODULE_META.items():
            assert isinstance(version, str), \
                f"Version for {name} should be a string"


class TestTryImport:
    """_try_import should return (module, None) or (None, error_str)."""

    def test_import_real_module(self):
        import atlas_omega
        mod, err = atlas_omega._try_import("economy")
        assert mod is not None
        assert err is None

    def test_import_nonexistent_returns_none(self):
        import atlas_omega
        mod, err = atlas_omega._try_import("nonexistent_module_xyz_123")
        assert mod is None
        assert isinstance(err, str)


class TestOmegaEngine:
    """OmegaEngine instantiation and core methods."""

    @pytest.fixture
    def engine(self):
        import atlas_omega
        return atlas_omega.OmegaEngine()

    def test_engine_instantiates(self, engine):
        assert engine is not None

    def test_status_dict_populated(self, engine):
        """status dict should have an entry for every module in META."""
        import atlas_omega
        for name in atlas_omega._MODULE_META:
            assert name in engine.status

    def test_core_modules_loaded(self, engine):
        """Lightweight modules (economy, vault, token_data, detector)
        must always import successfully in the test environment."""
        for name in ("economy", "vault", "token_data", "detector"):
            assert engine.status.get(name) is True, \
                f"Module '{name}' failed to load: {engine.errors.get(name)}"

    def test_module_status_prints(self, engine, capsys):
        engine.module_status()
        captured = capsys.readouterr()
        assert "MODULE STATUS" in captured.out

    def test_quick_status_returns_string(self, engine):
        result = engine.quick_status()
        assert isinstance(result, str)
        assert "PCVR" in result

    def test_economy_data_dict(self, engine):
        data = engine._economy_data()
        assert isinstance(data, dict)

    def test_risk_data_dict(self, engine):
        data = engine._risk_data()
        assert isinstance(data, dict)

    def test_whale_data_dict(self, engine):
        data = engine._whale_data()
        assert isinstance(data, dict)

    def test_omega_report_runs(self, engine, capsys):
        """omega_report() should not raise."""
        try:
            engine.omega_report()
        except Exception as exc:
            pytest.fail(f"omega_report() raised an exception: {exc}")
