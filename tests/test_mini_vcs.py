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

# Feature 3: Branching

def test_branch_can_be_created():
    repo = Repository()

    repo.create_branch("feature")

    assert "feature" in repo.branches


def test_branch_count_increases_by_one():
    repo = Repository()

    repo.create_branch("feature")

    assert len(repo.branches) == 2
    assert "main" in repo.branches


def test_new_branch_inherits_current_head():
    repo = Repository()

    repo.commit("First commit", {"file.txt": "Hello"})
    repo.create_branch("feature")

    assert repo.branches["feature"] == repo.branches["main"]


def test_creating_a_branch_does_not_switch_to_it():
    repo = Repository()

    repo.create_branch("feature")

    assert repo.current_branch == "main"


def test_branch_created_before_any_commit_has_no_head():
    repo = Repository()

    repo.create_branch("feature")

    assert repo.branches["feature"] is None


def test_single_character_branch_name_is_accepted():
    repo = Repository()

    repo.create_branch("f")

    assert "f" in repo.branches


def test_empty_branch_name_is_rejected():
    repo = Repository()

    with pytest.raises(ValueError):
        repo.create_branch("")


def test_whitespace_only_branch_name_is_rejected():
    repo = Repository()

    with pytest.raises(ValueError):
        repo.create_branch("   ")


def test_duplicate_branch_name_is_rejected():
    repo = Repository()

    repo.create_branch("feature")

    with pytest.raises(ValueError):
        repo.create_branch("feature")


def test_rejected_branch_creation_leaves_branches_unchanged():
    repo = Repository()

    repo.create_branch("feature")
    branches_before = dict(repo.branches)

    with pytest.raises(ValueError):
        repo.create_branch("feature")

    assert repo.branches == branches_before


def test_branch_head_is_independent_after_creation():
    repo = Repository()

    first_id = repo.commit("First commit", {"file.txt": "Hello"})
    repo.create_branch("feature")

    repo.commit("Second commit", {"other.txt": "World"})

    assert repo.branches["feature"] == first_id
    assert repo.branches["main"] != repo.branches["feature"]

# Feature 4: Checkout

def test_checkout_switches_current_branch():
    repo = Repository()
    repo.create_branch("feature")

    repo.checkout("feature")

    assert repo.current_branch == "feature"


def test_can_checkout_back_to_main():
    repo = Repository()
    repo.create_branch("feature")

    repo.checkout("feature")
    repo.checkout("main")

    assert repo.current_branch == "main"


def test_checkout_does_not_modify_branches():
    repo = Repository()
    repo.create_branch("feature")
    branches_before = dict(repo.branches)

    repo.checkout("feature")

    assert repo.branches == branches_before


def test_checkout_preserves_history_of_target_branch():
    repo = Repository()

    repo.commit("First", {"a.txt": "A"})
    repo.commit("Second", {"b.txt": "B"})
    repo.create_branch("feature")

    repo.checkout("feature")

    messages = [commit["message"] for commit in repo.history()]

    assert messages == ["First", "Second"]


def test_commit_after_checkout_is_recorded_on_new_branch():
    repo = Repository()
    repo.create_branch("feature")
    repo.checkout("feature")

    repo.commit("Feature work", {"feature.txt": "data"})

    assert repo.history()[-1]["message"] == "Feature work"


def test_commit_after_checkout_does_not_affect_other_branch():
    repo = Repository()

    repo.commit("Base", {"base.txt": "A"})
    repo.create_branch("feature")

    repo.checkout("feature")
    repo.commit("Feature work", {"feature.txt": "B"})

    repo.checkout("main")

    messages = [commit["message"] for commit in repo.history()]

    assert messages == ["Base"]


def test_branches_keep_separate_histories_across_switches():
    repo = Repository()

    repo.commit("Base", {"base.txt": "A"})
    repo.create_branch("feature")

    repo.checkout("feature")
    repo.commit("Feature work", {"feature.txt": "B"})

    repo.checkout("main")
    repo.commit("Main work", {"main.txt": "C"})

    main_messages = [commit["message"] for commit in repo.history()]

    repo.checkout("feature")
    feature_messages = [commit["message"] for commit in repo.history()]

    assert main_messages == ["Base", "Main work"]
    assert feature_messages == ["Base", "Feature work"]


def test_checkout_current_branch_is_allowed():
    repo = Repository()

    repo.checkout("main")

    assert repo.current_branch == "main"


def test_checkout_branch_with_no_commits():
    repo = Repository()
    repo.create_branch("feature")

    repo.checkout("feature")

    assert repo.history() == []


def test_checkout_of_nonexistent_branch_is_rejected():
    repo = Repository()

    with pytest.raises(ValueError):
        repo.checkout("does_not_exist")


def test_failed_checkout_leaves_current_branch_unchanged():
    repo = Repository()

    with pytest.raises(ValueError):
        repo.checkout("does_not_exist")

    assert repo.current_branch == "main"

# Feature 5: Merge

def test_merge_adds_commit_to_current_branch():
    repo = Repository()

    repo.commit("Base", {"base.txt": "A"})
    repo.create_branch("feature")

    repo.checkout("feature")
    repo.commit("Feature work", {"feature.txt": "B"})

    repo.checkout("main")
    history_before = len(repo.history())

    repo.merge("feature")

    assert len(repo.history()) == history_before + 1


def test_merge_commit_contains_source_changes():
    repo = Repository()

    repo.commit("Base", {"base.txt": "A"})
    repo.create_branch("feature")

    repo.checkout("feature")
    repo.commit("Feature work", {"feature.txt": "B"})

    repo.checkout("main")
    repo.merge("feature")

    merge_commit = repo.history()[-1]

    assert merge_commit["changes"] == {"feature.txt": "B"}


def test_merge_preserves_current_branch_history():
    repo = Repository()

    repo.commit("Base", {"base.txt": "A"})
    repo.create_branch("feature")

    repo.commit("Main work", {"main.txt": "M"})

    repo.checkout("feature")
    repo.commit("Feature work", {"feature.txt": "F"})

    repo.checkout("main")
    repo.merge("feature")

    messages = [commit["message"] for commit in repo.history()]

    assert messages[0] == "Base"
    assert messages[1] == "Main work"
    assert len(messages) == 3


def test_source_branch_is_unchanged_after_merge():
    repo = Repository()

    repo.commit("Base", {"base.txt": "A"})
    repo.create_branch("feature")

    repo.checkout("feature")
    repo.commit("Feature work", {"feature.txt": "B"})

    source_history_before = list(repo.history())
    source_head_before = repo.branches["feature"]

    repo.checkout("main")
    repo.merge("feature")

    repo.checkout("feature")

    assert repo.history() == source_history_before
    assert repo.branches["feature"] == source_head_before


def test_merge_when_source_has_no_new_commits_creates_merge_commit():
    repo = Repository()

    repo.commit("Base", {"base.txt": "A"})
    repo.create_branch("feature")

    history_before = len(repo.history())

    repo.merge("feature")

    assert len(repo.history()) == history_before + 1
    assert repo.history()[-1]["changes"] == {}


def test_merge_multiple_source_changes():
    repo = Repository()

    repo.commit("Base", {"base.txt": "A"})
    repo.create_branch("feature")

    repo.checkout("feature")
    repo.commit("First feature change", {"a.txt": "1"})
    repo.commit("Second feature change", {"b.txt": "2", "c.txt": "3"})

    repo.checkout("main")
    repo.merge("feature")

    assert repo.history()[-1]["changes"] == {
        "a.txt": "1",
        "b.txt": "2",
        "c.txt": "3",
    }


def test_merge_of_nonexistent_branch_is_rejected():
    repo = Repository()

    with pytest.raises(ValueError):
        repo.merge("does_not_exist")


def test_merge_branch_into_itself_is_rejected():
    repo = Repository()

    with pytest.raises(ValueError):
        repo.merge("main")


def test_failed_merge_leaves_current_branch_unchanged():
    repo = Repository()

    repo.commit("Base", {"base.txt": "A"})

    history_before = list(repo.history())
    head_before = repo.branches["main"]

    with pytest.raises(ValueError):
        repo.merge("does_not_exist")

    assert repo.history() == history_before
    assert repo.branches["main"] == head_before
    assert repo.current_branch == "main"