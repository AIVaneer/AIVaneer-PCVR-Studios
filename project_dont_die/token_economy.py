"""
token_economy — PCVR Coin token economy survival tools.

Models burn schedules, staking rewards, treasury runway, and
break-even metrics for the PCVR token on Cronos.

This module is a placeholder; full implementation is in progress.
"""


class Treasury:
    """Manage and simulate a project treasury balance."""

    def __init__(self, balance=0.0, monthly_burn=0.0):
        self.balance = balance
        self.monthly_burn = monthly_burn

    @property
    def runway_months(self):
        """Return months until treasury is exhausted (0 if already empty)."""
        if self.monthly_burn <= 0:
            return float("inf")
        return max(0.0, self.balance / self.monthly_burn)

    def deposit(self, amount):
        """Add *amount* to the treasury."""
        self.balance += amount

    def withdraw(self, amount):
        """Remove *amount* from the treasury (clamped to 0)."""
        self.balance = max(0.0, self.balance - amount)


class BurnSchedule:
    """Model a token burn-rate schedule."""

    def __init__(self, initial_supply, burn_rate_pct=1.0):
        """
        Parameters
        ----------
        initial_supply : float
            Starting token supply.
        burn_rate_pct : float
            Percentage of remaining supply burned each period.
        """
        self.supply = initial_supply
        self.burn_rate_pct = burn_rate_pct

    def apply_burn(self, periods=1):
        """Apply the burn rate for *periods* and return the new supply."""
        for _ in range(periods):
            self.supply *= 1 - (self.burn_rate_pct / 100)
        return self.supply

    def total_burned(self, initial_supply):
        """Return total tokens burned since *initial_supply*."""
        return max(0.0, initial_supply - self.supply)


class StakingPool:
    """Simulate a simple staking reward pool."""

    def __init__(self, apy_pct=12.0):
        self.apy_pct = apy_pct
        self._stakes = {}

    def stake(self, address, amount):
        """Add *amount* to the stake for *address*."""
        self._stakes[address] = self._stakes.get(address, 0.0) + amount

    def unstake(self, address):
        """Remove all staked tokens for *address* and return them."""
        return self._stakes.pop(address, 0.0)

    def reward(self, address, periods=1, period_fraction=1 / 12):
        """Return the reward for *address* over *periods* (monthly by default)."""
        stake = self._stakes.get(address, 0.0)
        return stake * (self.apy_pct / 100) * periods * period_fraction

    def total_staked(self):
        """Return the total amount currently staked."""
        return sum(self._stakes.values())
