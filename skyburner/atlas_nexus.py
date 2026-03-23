"""
atlas_nexus — Core game engine for SkyBurner Ultimate.

The Atlas Nexus Engine drives the arcade game loop, rendering pipeline,
and input handling optimised for Pythonista 3 on iOS.

This module is a placeholder; full implementation is in progress.
"""


class AtlasNexusEngine:
    """Minimal stub for the Atlas Nexus game engine."""

    def __init__(self, width=375, height=667, fps=60):
        self.width = width
        self.height = height
        self.fps = fps
        self._running = False

    def start(self):
        """Start the engine loop."""
        self._running = True

    def stop(self):
        """Stop the engine loop."""
        self._running = False

    @property
    def is_running(self):
        """Return True if the engine is currently running."""
        return self._running
