"""Mini Version Control System.

A simplified, in-memory version control system.
"""

DEFAULT_BRANCH = "main"


class Repository:
    """An in-memory repository."""

    def __init__(self):
        self.branches = {DEFAULT_BRANCH: None}
        self.current_branch = DEFAULT_BRANCH

    def history(self):
        """Return the commits on the current branch."""
        return []