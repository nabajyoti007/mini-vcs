import pytest

from src.mini_vcs import Repository


# Feature 1: Repository Creation

def test_new_repository_has_main_branch():
    repo = Repository()
    assert "main" in repo.branches


def test_main_is_the_current_branch():
    repo = Repository()
    assert repo.current_branch == "main"


def test_new_repository_has_exactly_one_branch():
    repo = Repository()
    assert len(repo.branches) == 1


def test_new_repository_has_no_commits():
    repo = Repository()
    assert repo.history() == []


# Feature 2: Commit and Commit History

def test_commit_is_added_to_history():
    repo = Repository()

    repo.commit("Initial commit", {"file.txt": "Hello"})

    assert len(repo.history()) == 1
    assert repo.history()[0]["message"] == "Initial commit"


def test_history_is_ordered_oldest_first():
    repo = Repository()

    repo.commit("First", {"a.txt": "A"})
    repo.commit("Second", {"b.txt": "B"})
    repo.commit("Third", {"c.txt": "C"})

    messages = [commit["message"] for commit in repo.history()]

    assert messages == ["First", "Second", "Third"]


def test_single_character_commit_message_is_accepted():
    repo = Repository()

    repo.commit("x", {})

    assert len(repo.history()) == 1


def test_commit_with_no_changes_is_allowed():
    repo = Repository()

    repo.commit("Empty change set", {})

    assert len(repo.history()) == 1


def test_empty_commit_message_is_rejected():
    repo = Repository()

    with pytest.raises(ValueError):
        repo.commit("", {"file.txt": "Hello"})


def test_whitespace_only_commit_message_is_rejected():
    repo = Repository()

    with pytest.raises(ValueError):
        repo.commit("   ", {"file.txt": "Hello"})


def test_each_commit_has_a_unique_id():
    repo = Repository()

    first_id = repo.commit("First", {})
    second_id = repo.commit("Second", {})

    assert first_id != second_id


def test_rejected_commit_leaves_history_unchanged():
    repo = Repository()

    repo.commit("Valid commit", {})

    with pytest.raises(ValueError):
        repo.commit("   ", {})

    assert len(repo.history()) == 1