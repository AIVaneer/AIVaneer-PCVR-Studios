"""
dashboard — Terminal dashboard renderer for Eve DeFi Toolkit.

Renders a live, colour-coded market summary to stdout using only stdlib.

This module is a placeholder; full implementation is in progress.
"""

import datetime


class TerminalDashboard:
    """Simple text-based dashboard for DeFi metrics."""

    def __init__(self, title="Eve DeFi Toolkit — PCVR Studios"):
        self.title = title
        self._rows = []

    def add_row(self, label, value):
        """Append a labelled metric row."""
        self._rows.append((label, value))

    def clear(self):
        """Remove all rows."""
        self._rows.clear()

    def render(self):
        """Return the dashboard as a formatted string."""
        width = 50
        now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        lines = [
            "=" * width,
            self.title.center(width),
            now.center(width),
            "-" * width,
        ]
        for label, value in self._rows:
            lines.append(f"  {label:<22} {str(value):>22}")
        lines.append("=" * width)
        return "\n".join(lines)

    def display(self):
        """Print the dashboard to stdout."""
        print(self.render())
