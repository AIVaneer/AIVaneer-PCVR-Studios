"""
Shared pytest fixtures for the PCVR Studios test suite.
"""
import os
import sys
import pytest

# Ensure both packages are importable from the repo root
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

# Add eve_toolkit and skyburner to path for direct module imports
EVE_PATH = os.path.join(REPO_ROOT, "eve_toolkit")
SKY_PATH = os.path.join(REPO_ROOT, "skyburner")
for p in (EVE_PATH, SKY_PATH):
    if p not in sys.path:
        sys.path.insert(0, p)


@pytest.fixture
def tmp_dir(tmp_path):
    """Provide a temporary directory that is cleaned up after each test."""
    return tmp_path


@pytest.fixture
def economy_reset():
    """Reset the economy module state between tests."""
    import economy as econ
    econ.supply = 1_000_000_000
    econ.circ = 100_000_000
    econ.emitted = 0
    econ.burned = 0
    econ.spent = 0
    econ.locked = 0
    econ.cap = 50000
    econ.today = 0
    yield econ
    # Reset again after the test
    econ.supply = 1_000_000_000
    econ.circ = 100_000_000
    econ.emitted = 0
    econ.burned = 0
    econ.spent = 0
    econ.locked = 0
    econ.cap = 50000
    econ.today = 0


@pytest.fixture
def vault_reset():
    """Reset the vault module state between tests."""
    import vault as v
    v.vault_balance = 0
    v.total_locked = 0
    v.lockers = {}
    yield v
    v.vault_balance = 0
    v.total_locked = 0
    v.lockers = {}


@pytest.fixture
def score_manager():
    """Return a fresh ScoreManager instance."""
    from atlas_nexus import ScoreManager
    return ScoreManager()


@pytest.fixture
def wave_manager():
    """Return a fresh WaveManager instance."""
    from atlas_nexus import WaveManager
    return WaveManager()


@pytest.fixture
def entity_manager():
    """Return a fresh EntityManager instance."""
    from atlas_nexus import EntityManager
    return EntityManager()


@pytest.fixture
def atlas_engine():
    """Return a fresh AtlasNexusEngine instance."""
    from atlas_nexus import AtlasNexusEngine
    return AtlasNexusEngine()
