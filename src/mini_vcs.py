"""Mini Version Control System.

A simplified, in-memory version control system.
"""

import itertools

DEFAULT_BRANCH = "main"


class Repository:
    """An in-memory repository."""

    def __init__(self):
        self._commits = {DEFAULT_BRANCH: []}
        self.branches = {DEFAULT_BRANCH: None}
        self.current_branch = DEFAULT_BRANCH
        self._counter = itertools.count(1)

    def commit(self, message, changes=None):
        """Record a commit on the current branch and return its identifier."""
        if not message.strip():
            raise ValueError("Commit message cannot be empty")

        changes = {} if changes is None else changes

        commit_id = f"c{next(self._counter):04d}"

        self._commits[self.current_branch].append({
            "id": commit_id,
            "message": message,
            "changes": dict(changes),
        })

        self.branches[self.current_branch] = commit_id

        return commit_id

    def history(self):
        """Return the commits on the current branch, oldest first."""
        return list(self._commits[self.current_branch])