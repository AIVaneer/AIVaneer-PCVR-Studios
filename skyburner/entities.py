"""
entities — Game entity definitions for SkyBurner Ultimate.

Contains player ship, enemy, projectile, and power-up entity stubs.
This module is a placeholder; full implementation is in progress.
"""


class Entity:
    """Base class for all game entities."""

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        self.active = True

    def update(self, dt):
        """Update entity state. Override in subclasses."""

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"


class PlayerShip(Entity):
    """The player-controlled ship."""

    def __init__(self, x=0.0, y=0.0, lives=3):
        super().__init__(x, y)
        self.lives = lives
        self.score = 0


class Enemy(Entity):
    """A generic enemy entity."""

    def __init__(self, x=0.0, y=0.0, health=1):
        super().__init__(x, y)
        self.health = health


class Projectile(Entity):
    """A bullet or missile entity."""

    def __init__(self, x=0.0, y=0.0, speed=5.0, owner=None):
        super().__init__(x, y)
        self.speed = speed
        self.owner = owner


class PowerUp(Entity):
    """A collectible power-up entity."""

    def __init__(self, x=0.0, y=0.0, kind="shield"):
        super().__init__(x, y)
        self.kind = kind
