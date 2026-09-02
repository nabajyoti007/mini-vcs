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

    def create_branch(self, name):
        """Create a branch starting from the current branch's head."""
        if not name.strip():
            raise ValueError("Branch name cannot be empty")

        if name in self.branches:
            raise ValueError(f"Branch '{name}' already exists")

        self.branches[name] = self.branches[self.current_branch]
        self._commits[name] = list(self._commits[self.current_branch])

        return name

    def checkout(self, name):
        """Switch the current branch to an existing branch."""
        if name not in self.branches:
            raise ValueError(f"Branch '{name}' does not exist")

        self.current_branch = name

    def merge(self, source_branch):
        """Merge changes from another branch into the current branch."""
        if source_branch not in self.branches:
            raise ValueError(f"Branch '{source_branch}' does not exist")

        if source_branch == self.current_branch:
            raise ValueError("Cannot merge a branch into itself")

        current_commits = self._commits[self.current_branch]
        source_commits = self._commits[source_branch]

        current_ids = {
            commit["id"] for commit in current_commits
        }

        source_ids = {
            commit["id"] for commit in source_commits
        }

        our_changes = self._changes_since_divergence(
            current_commits,
            source_ids
        )

        their_changes = self._changes_since_divergence(
            source_commits,
            current_ids
        )

        conflicts = [
            filename
            for filename, content in their_changes.items()
            if filename in our_changes
            and our_changes[filename] != content
        ]

        if conflicts:
            conflicts.sort()

            raise ValueError(
                f"Merge conflict detected in: {', '.join(conflicts)}"
            )

        self.commit(
            f"Merge branch '{source_branch}'",
            their_changes
        )

    @staticmethod
    def _changes_since_divergence(commits, other_ids):
        """Return accumulated changes not shared with the other branch."""
        changes = {}

        for commit in commits:
            if commit["id"] not in other_ids:
                changes.update(commit["changes"])

        return changes