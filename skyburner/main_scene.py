"""
main_scene — Entry point scene for SkyBurner Ultimate.

Wires up the Atlas Nexus Engine with the initial game entities and
launches the main game loop.

This module is a placeholder; full implementation is in progress.
"""

from skyburner.atlas_nexus import AtlasNexusEngine
from skyburner.entities import PlayerShip


class MainScene:
    """Top-level game scene for SkyBurner Ultimate."""

    def __init__(self):
        self.engine = AtlasNexusEngine()
        self.player = PlayerShip(x=187.0, y=50.0)
        self.entities = [self.player]

    def setup(self):
        """Initialise assets and state before the game loop begins."""
        self.engine.start()

    def update(self, dt=0.016):
        """Advance all entities by *dt* seconds."""
        for entity in self.entities:
            entity.update(dt)

    def teardown(self):
        """Clean up resources when the scene exits."""
        self.engine.stop()
