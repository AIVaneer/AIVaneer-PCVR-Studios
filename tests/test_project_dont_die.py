"""Pytest stubs for the project_dont_die module."""

from project_dont_die.token_economy import BurnSchedule, StakingPool, Treasury


class TestTreasury:
    def test_initial_balance(self):
        t = Treasury(balance=10_000.0, monthly_burn=1_000.0)
        assert t.balance == 10_000.0

    def test_runway(self):
        t = Treasury(balance=12_000.0, monthly_burn=1_000.0)
        assert t.runway_months == 12.0

    def test_runway_zero_burn(self):
        t = Treasury(balance=5_000.0, monthly_burn=0.0)
        assert t.runway_months == float("inf")

    def test_deposit(self):
        t = Treasury(balance=1_000.0)
        t.deposit(500.0)
        assert t.balance == 1_500.0

    def test_withdraw(self):
        t = Treasury(balance=1_000.0)
        t.withdraw(400.0)
        assert t.balance == 600.0

    def test_withdraw_clamps_to_zero(self):
        t = Treasury(balance=100.0)
        t.withdraw(999.0)
        assert t.balance == 0.0


class TestBurnSchedule:
    def test_initial_supply(self):
        bs = BurnSchedule(initial_supply=1_000_000)
        assert bs.supply == 1_000_000

    def test_apply_burn_reduces_supply(self):
        bs = BurnSchedule(initial_supply=1_000_000, burn_rate_pct=10.0)
        new_supply = bs.apply_burn(periods=1)
        assert new_supply == 900_000.0

    def test_apply_burn_multiple_periods(self):
        bs = BurnSchedule(initial_supply=1_000, burn_rate_pct=50.0)
        bs.apply_burn(periods=2)
        assert bs.supply == 250.0

    def test_total_burned(self):
        bs = BurnSchedule(initial_supply=1_000_000, burn_rate_pct=10.0)
        bs.apply_burn(periods=1)
        assert bs.total_burned(1_000_000) == 100_000.0


class TestStakingPool:
    def test_empty_pool(self):
        sp = StakingPool()
        assert sp.total_staked() == 0.0

    def test_stake_adds_balance(self):
        sp = StakingPool()
        sp.stake("0xALICE", 1_000.0)
        assert sp.total_staked() == 1_000.0

    def test_unstake_removes_balance(self):
        sp = StakingPool()
        sp.stake("0xALICE", 1_000.0)
        amount = sp.unstake("0xALICE")
        assert amount == 1_000.0
        assert sp.total_staked() == 0.0

    def test_unstake_unknown_address(self):
        sp = StakingPool()
        assert sp.unstake("0xNOBODY") == 0.0

    def test_reward_calculation(self):
        sp = StakingPool(apy_pct=12.0)
        sp.stake("0xBOB", 12_000.0)
        # 12% APY, 1 period at monthly fraction -> 12000 * 0.12 * 1 / 12 = 120
        reward = sp.reward("0xBOB", periods=1, period_fraction=1 / 12)
        assert abs(reward - 120.0) < 1e-9
