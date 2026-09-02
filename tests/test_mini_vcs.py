from src.mini_vcs import Repository


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