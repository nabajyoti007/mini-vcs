# AI-Assisted Development Log

## Mini Version Control System (MiniVCS)

**Project:** Mini Version Control System  
**Development Approach:** AI-Assisted Test-Driven Development (AI-TDD)  
**AI Tool Used:** Claude  
**Language:** Python 3  
**Testing Framework:** pytest  

---

## Purpose of This Log

This document records how artificial intelligence was used during the development of MiniVCS. For each stage, it records the purpose of the AI interaction, the prompt used, a summary of the AI response, my evaluation of that response, the decision I made, and any changes made before accepting the output.

The final implementation and testing decisions remain my responsibility. AI-generated suggestions are reviewed before being incorporated into the project.

---

# Stage 1 — Requirements Analysis

## 1.1 Purpose

The first AI interaction was used to analyse the assignment requirements before writing implementation code. The aim was to define a clear and testable scope for MiniVCS and identify functional requirements, non-functional requirements, assumptions, constraints, expected behaviours, boundary conditions, and invalid-input scenarios.

## 1.2 Initial AI Prompt

> I am developing a university software unit testing assignment using an AI-assisted Test-Driven Development workflow.
>
> I have selected the Mini Version Control System. The required features are:
> - commit
> - checkout
> - branching
> - merge
> - conflict detection
> - commit history
>
> Before writing any implementation code, help me analyse the requirements.
>
> Please produce:
> 1. Functional requirements
> 2. Non-functional requirements
> 3. Assumptions
> 4. Constraints
> 5. At least 10 expected system behaviours
> 6. Boundary conditions
> 7. Invalid input scenarios
>
> Keep the scope small and suitable for a university assignment. Do not generate implementation code yet.

## 1.3 AI Response Summary

Claude produced an initial requirements specification containing functional and non-functional requirements, assumptions, constraints, expected system behaviours, boundary conditions, and invalid-input scenarios.

The response provided a useful starting point, but it also introduced several decisions that were not explicitly required by the assignment. Examples included branch deletion, fixed character limits for branch names and commit messages, and specific rules for whitespace-padded branch names.

## 1.4 My Evaluation

I did not accept the first response unchanged. I identified that some AI-generated requirements unnecessarily expanded the project beyond the six required features. In particular:

- Branch deletion was outside the required project scope.
- A 100-character branch-name limit was introduced without a clear requirement.
- A commit-message length limit was introduced without sufficient justification.
- Some non-functional requirements were difficult to measure objectively.
- Whole-file merging was a useful simplification, but it needed to be treated as a deliberate project decision rather than an unstated assumption.

Because the assignment focuses on reviewing and improving AI output, I decided to ask the AI to critically evaluate its own first response before finalising the specification.

## 1.5 Decision

**Decision: Modified**

The initial AI-generated requirements were useful as a draft, but they required review and modification before acceptance.

---

# Stage 2 — Critical Review of AI-Generated Requirements

## 2.1 Purpose

The second AI interaction was used to identify unnecessary, arbitrary, ambiguous, or out-of-scope requirements introduced during the initial requirements analysis.

## 2.2 Review Prompt

> I have reviewed your requirements analysis for my Mini Version Control System.
>
> I want to keep the project small and strictly aligned with the assignment brief.
>
> Please critically review your previous requirements and identify anything that you introduced that was not explicitly required by the project scope.
>
> Specifically review:
> 1. Functional requirements
> 2. Non-functional requirements
> 3. Assumptions
> 4. Constraints
> 5. Expected behaviours
> 6. Boundary conditions
> 7. Invalid input scenarios
>
> For each item that may be unnecessary, arbitrary, ambiguous, or outside the required scope, explain why.
>
> Important:
> - The six main features are only:
>   1. commit
>   2. checkout
>   3. branching
>   4. merge
>   5. conflict detection
>   6. commit history
> - Do not add new major features.
> - Do not generate implementation code.
> - Do not generate unit tests yet.
> - Pay particular attention to branch deletion, character limits, branch-name rules, and whole-file merging.
> - Recommend what should be kept, modified, or removed.
>
> I want this review to help me demonstrate critical evaluation of AI-generated requirements in my university assignment.

## 2.3 AI Response Summary

The AI review confirmed several problems in the initial output. It recommended removing branch deletion and the arbitrary branch-name length limit. It also recommended revising vague non-functional requirements and treating whole-file merging as an explicit design/scope decision.

## 2.4 My Evaluation and Changes

I agreed with the review and made the following decisions:

- **Removed branch deletion:** It would create a seventh feature and was not required by the assignment.
- **Removed the arbitrary branch-name length limit:** There was no project requirement supporting a fixed maximum.
- **Removed an arbitrary maximum commit-message length:** The final specification accepts long messages rather than inventing a limit only to create a boundary.
- **Clarified testability requirements:** The final specification states that the system should use small functions and methods that can be tested independently.
- **Retained whole-file merging:** I accepted this as a deliberate simplification because line-level merging would add unnecessary complexity.
- **Kept invalid empty/whitespace commit messages:** This provides a clear invalid-input scenario.
- **Kept failed-operation state protection:** Invalid or conflicting operations should not silently alter repository state.

## 2.5 Decision

**Decision: Accepted with modifications**

The review helped distinguish useful requirements from AI-generated scope expansion.

---

# Stage 3 — Final Requirements Specification

## 3.1 Purpose

After reviewing the earlier AI outputs, a final concise specification was requested using only the agreed project scope.

## 3.2 Finalisation Prompt

> Based on your previous review, give me ONLY the final revised requirements specification.
>
> Keep the scope limited to:
> 1. Commit
> 2. Checkout
> 3. Branching
> 4. Merge
> 5. Conflict detection
> 6. Commit history
>
> Remove branch deletion and unnecessary/invented requirements.
>
> Include only:
> - Functional requirements
> - Non-functional requirements
> - Assumptions
> - Constraints
> - 10-15 expected behaviours
> - Boundary conditions
> - Invalid input scenarios
>
> Keep it concise and suitable for a university assignment.
> Do not include explanations, commentary, or implementation code.

## 3.3 Final Result

The resulting specification was reviewed again before being saved as `SPECIFICATION.md`.

The final project is limited to six features:

1. Commit
2. Checkout
3. Branching
4. Merge
5. Conflict detection
6. Commit history

The final specification also establishes that:

- The project is implemented in Python 3.
- Application code and test code remain separate.
- The repository is in-memory only.
- Files are represented using names and string content.
- Whole-file merging is used instead of line-level merging.
- Conflicts are reported rather than automatically resolved.
- Tests are written before implementation for each feature.
- Development is recorded incrementally using Git.

## 3.4 Overall Evaluation of AI During Requirements Analysis

AI was effective at quickly identifying possible requirements, edge cases, and invalid-input scenarios. However, it also demonstrated a tendency to expand familiar software concepts beyond the requested scope. Branch deletion was the clearest example because it is common in real version-control systems but was not required for MiniVCS.

This stage demonstrated why AI output should not be accepted automatically. Reviewing and modifying the output kept the project smaller, clearer, and aligned with the assignment.

---

# Stage 4 — Test Design and Implementation

## Feature 1 — Repository Creation

### 4.1 Feature Description

The first feature developed using TDD was repository creation.

The required behaviour was:

- A new repository contains a default branch named `main`.
- `main` is the current branch.
- A new repository has no commits.
- The initial repository contains only one branch.

No commit, checkout, branching, merge, or conflict-detection functionality was implemented at this stage.

### 4.2 Initial AI Test-Design Prompt

The following prompt was given to Claude before writing the implementation:

> I am starting Test-Driven Development for Feature 1: Repository Creation in my Mini Version Control System.
>
> Requirements:
> - A new repository must contain a default branch named "main".
> - "main" must be the current branch.
> - A new repository must have no commits.
> - A new repository must have no files.
>
> Generate ONLY the pytest unit-test design for this feature.
>
> For each test, include:
> 1. Test name
> 2. What it checks
> 3. Why it is necessary
>
> Do not write implementation code.
> Do not write the Repository class.
> Do not include tests for commit, checkout, branching, merge, conflict detection, or history beyond the empty initial history.
> Keep the response concise.

### 4.3 AI Test-Design Response Summary

Claude proposed five tests:

1. `test_new_repository_has_main_branch`
2. `test_main_is_the_current_branch`
3. `test_new_repository_has_exactly_one_branch`
4. `test_new_repository_has_no_commits`
5. `test_new_repository_has_no_files`

Claude also suggested using a pytest fixture to create a fresh `Repository` object for each test.

### 4.4 My Evaluation of the AI-Generated Tests

I reviewed the proposed tests before adding them to the project.

I accepted the first four tests because they directly test the initial repository requirements.

I did not use the proposed `test_new_repository_has_no_files` test. The AI assumed that the application would provide a `get_files()` method, but this method had not been defined in the specification. Adding this test would therefore introduce an additional API based on an AI assumption rather than an existing requirement.

I also decided not to use the suggested pytest fixture at this stage. The test suite was very small, and creating a new `Repository()` directly inside each test kept the tests simple and easy to understand.

### Decision

**Modified**

Four of the five proposed tests were accepted. One test was rejected/postponed because it depended on an unspecified `get_files()` method.

### 4.5 Initial Automated Tests

The following four tests were added to `tests/test_mini_vcs.py` before implementing the `Repository` class:

```python
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
```

### 4.6 RED Stage — Initial Test Execution

The tests were executed before the `Repository` class was implemented using:

```text
python -m pytest -v
```

The test run failed during test collection with:

```text
ImportError: cannot import name 'Repository' from 'src.mini_vcs'
```

This failure was expected because `src/mini_vcs.py` existed but the `Repository` class had not yet been implemented.

This provided evidence that the automated tests were created and executed before the implementation.

### Result

**RED — Expected failure**

### Evidence

`screenshots/01_repository_red.png`

### 4.7 AI Implementation Prompt

After recording the RED result, the following prompt was given to Claude:

> I am following Test-Driven Development.
>
> These pytest tests already exist for Feature 1: Repository Creation:
>
> ```python
> from src.mini_vcs import Repository
>
>
> def test_new_repository_has_main_branch():
>     repo = Repository()
>     assert "main" in repo.branches
>
>
> def test_main_is_the_current_branch():
>     repo = Repository()
>     assert repo.current_branch == "main"
>
>
> def test_new_repository_has_exactly_one_branch():
>     repo = Repository()
>     assert len(repo.branches) == 1
>
>
> def test_new_repository_has_no_commits():
>     repo = Repository()
>     assert repo.history() == []
> ```
>
> The tests currently fail because Repository has not been implemented.
>
> Please provide the smallest Python implementation necessary to make ONLY these tests pass.
>
> Requirements:
> - class name: Repository
> - default branch: "main"
> - current branch must be "main"
> - new repository must have no commits
> - do not implement commit, checkout, branching, merge, or conflict detection yet
> - keep the code simple and readable
> - explain briefly why each part is necessary
>
> Do not add extra features.

### 4.8 AI Implementation Response Summary

Claude proposed:

- A `DEFAULT_BRANCH` constant containing `"main"`.
- A `Repository` class.
- A `branches` dictionary containing the initial `main` branch.
- A `current_branch` attribute set to `main`.
- A `history()` method returning an empty list.
- A `get_files()` method returning an empty dictionary.

The proposed implementation was intentionally small because only the Feature 1 tests needed to pass.

### 4.9 My Evaluation of the AI Implementation

I did not accept the AI-generated implementation unchanged.

The `DEFAULT_BRANCH`, `Repository`, `branches`, `current_branch`, and `history()` suggestions were relevant to the four reviewed tests.

However, Claude again included a `get_files()` method because its earlier test design had proposed a fifth test for empty file state. Since I had already rejected that test and `get_files()` was not required by the current specification or test suite, I removed the method.

This prevented unnecessary functionality from being implemented before it was required by a test.

### Decision

**Modified**

The AI-generated implementation was simplified to contain only the functionality required to satisfy the four existing tests.

### 4.10 Final Feature 1 Implementation

The reviewed implementation added to `src/mini_vcs.py` was:

```python
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
```

### 4.11 GREEN Stage — Test Execution

After implementing the minimum required functionality, the complete test suite was executed again using:

```text
python -m pytest -v
```

All four Feature 1 tests passed.

### Result

**GREEN — 4 tests passed**

### Evidence

`screenshots/02_repository_green.png`

### 4.12 Feature 1 Reflection

The AI was useful for identifying the main behaviours that should be tested for repository creation. However, it also introduced a `get_files()` interface that had not been defined in the specification.

Reviewing the AI output prevented an unnecessary method from becoming part of the application design. This demonstrated an important part of the AI-assisted TDD process: AI suggestions were treated as proposals rather than automatically accepted implementation decisions.

Feature 1 successfully completed the TDD cycle:

**Requirements → AI test design → Human review → Tests → RED → AI implementation → Human review/modification → GREEN**

---

## Feature 2 — Commit and Commit History

### 4.13 Feature Description

The second feature developed using TDD was commit creation and commit history.

The required behaviour was:

- A commit contains a message and a dictionary of file changes.
- A valid commit is stored on the current branch.
- Every commit receives a unique identifier.
- Commit history is returned in oldest-first order.
- Empty commit messages are rejected.
- Whitespace-only commit messages are rejected.
- A commit with an empty changes dictionary is valid.
- A rejected commit must not modify repository history.

Checkout, new branch creation, merge, and conflict detection were not implemented during this feature.

---

### 4.14 Initial AI Test-Design Prompt

The following prompt was given to Claude before implementing Feature 2:

> I am continuing Test-Driven Development for my Mini Version Control System.
>
> Feature 2 is Commit and Commit History.
>
> Existing functionality:
> - Repository starts with a single "main" branch.
> - "main" is the current branch.
> - A new repository has no commits.
>
> Requirements for this feature:
> - A commit has a message and a dictionary of file changes.
> - A valid commit must be stored on the current branch.
> - Every commit must have a unique identifier.
> - Commit history must be returned oldest first.
> - An empty or whitespace-only commit message must be rejected.
> - If a commit is rejected, repository history must remain unchanged.
>
> Generate ONLY the pytest unit-test design for this feature.
>
> For each test, include:
> 1. Test name
> 2. What it checks
> 3. Why it is necessary
>
> Include:
> - normal cases
> - boundary cases
> - invalid cases
> - regression-relevant cases
>
> Do not write implementation code.
> Do not write the commit method.
> Do not design tests for checkout, branching, merge, or conflict detection.
> Keep the response concise.

---

### 4.15 AI Test-Design Response Summary

Claude proposed thirteen tests covering normal, boundary, invalid, and regression-related behaviour:

1. `test_valid_commit_returns_an_id`
2. `test_commit_is_added_to_history`
3. `test_commit_stores_file_contents`
4. `test_history_is_ordered_oldest_first`
5. `test_later_commit_overwrites_earlier_file_content`
6. `test_single_character_commit_message_is_accepted`
7. `test_commit_with_no_changes_is_allowed`
8. `test_message_with_surrounding_whitespace_is_accepted`
9. `test_empty_commit_message_is_rejected`
10. `test_whitespace_only_commit_message_is_rejected`
11. `test_each_commit_has_a_unique_id`
12. `test_commit_ids_stay_unique_across_many_commits`
13. `test_rejected_commit_leaves_history_unchanged`

Claude also raised design questions about whether surrounding whitespace should be preserved in commit messages and what type of commit identifier should be used.

---

### 4.16 My Evaluation of the AI-Generated Tests

I reviewed the thirteen proposed tests before adding them to the project.

I accepted tests covering:

- A valid commit being added to history.
- History being returned oldest first.
- A single-character message being accepted.
- An empty changes dictionary being accepted.
- An empty message being rejected.
- A whitespace-only message being rejected.
- Different commits receiving unique identifiers.
- A rejected commit leaving history unchanged.

I did not use `test_commit_stores_file_contents` and `test_later_commit_overwrites_earlier_file_content` because both relied on a `get_files()` method. This public API was not defined in the specification and had already been rejected during Feature 1.

I did not include the surrounding-whitespace test because the specification requires whitespace-only messages to be rejected but does not define whether surrounding whitespace in an otherwise valid message should be trimmed or preserved.

I also did not include the fifty-commit uniqueness test. Two commits with different identifiers were sufficient to test the current uniqueness requirement without adding unnecessary test volume.

The proposed `test_valid_commit_returns_an_id` also overlapped with the unique-ID test because comparing the values returned by two commits already verifies that the method returns identifiers.

### Decision

**Modified**

The AI proposed thirteen tests. After reviewing their relevance, assumptions, and overlap, eight tests were selected for Feature 2.

---

### 4.17 Initial Automated Tests

The following eight tests were added to `tests/test_mini_vcs.py` before implementing `commit()`:

```python
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
```

The existing four Feature 1 tests remained in the test file so they could also act as regression tests.

---

### 4.18 RED Stage — Initial Test Execution

Before implementing `commit()`, the complete test suite was executed using:

```text
python -m pytest -v
```

Pytest collected twelve tests.

The four existing Feature 1 tests passed, while all eight new Feature 2 tests failed.

The main failure was:

```text
AttributeError: 'Repository' object has no attribute 'commit'
```

The result was:

```text
8 failed, 4 passed
```

This was the expected RED stage because the Feature 2 tests were written and executed before the `commit()` method existed.

The four Feature 1 tests continuing to pass also confirmed that the existing repository-creation functionality remained working.

### Result

**RED — 8 failed, 4 passed**

### Evidence

`screenshots/03_commit_red.png`

---

### 4.19 AI Implementation Prompt

After recording the RED result, the following prompt was given to Claude:

> I am following AI-assisted Test-Driven Development for my Mini Version Control System.
>
> I am now implementing Feature 2: Commit and Commit History.
>
> The following pytest tests already exist and were executed before implementation:
>
> ```python
> def test_commit_is_added_to_history():
>     repo = Repository()
>
>     repo.commit("Initial commit", {"file.txt": "Hello"})
>
>     assert len(repo.history()) == 1
>     assert repo.history()[0]["message"] == "Initial commit"
>
>
> def test_history_is_ordered_oldest_first():
>     repo = Repository()
>
>     repo.commit("First", {"a.txt": "A"})
>     repo.commit("Second", {"b.txt": "B"})
>     repo.commit("Third", {"c.txt": "C"})
>
>     messages = [commit["message"] for commit in repo.history()]
>
>     assert messages == ["First", "Second", "Third"]
>
>
> def test_single_character_commit_message_is_accepted():
>     repo = Repository()
>
>     repo.commit("x", {})
>
>     assert len(repo.history()) == 1
>
>
> def test_commit_with_no_changes_is_allowed():
>     repo = Repository()
>
>     repo.commit("Empty change set", {})
>
>     assert len(repo.history()) == 1
>
>
> def test_empty_commit_message_is_rejected():
>     repo = Repository()
>
>     with pytest.raises(ValueError):
>         repo.commit("", {"file.txt": "Hello"})
>
>
> def test_whitespace_only_commit_message_is_rejected():
>     repo = Repository()
>
>     with pytest.raises(ValueError):
>         repo.commit("   ", {"file.txt": "Hello"})
>
>
> def test_each_commit_has_a_unique_id():
>     repo = Repository()
>
>     first_id = repo.commit("First", {})
>     second_id = repo.commit("Second", {})
>
>     assert first_id != second_id
>
>
> def test_rejected_commit_leaves_history_unchanged():
>     repo = Repository()
>
>     repo.commit("Valid commit", {})
>
>     with pytest.raises(ValueError):
>         repo.commit("   ", {})
>
>     assert len(repo.history()) == 1
> ```
>
> Current test result:
>
> 8 failed, 4 passed.
>
> The existing Feature 1 tests still pass. The 8 new tests fail because:
>
> AttributeError: 'Repository' object has no attribute 'commit'
>
> Please provide the smallest Python implementation necessary to make these Feature 2 tests pass while keeping all existing Feature 1 tests passing.
>
> Requirements:
> - A commit has a message and a dictionary of file changes.
> - A valid commit must be stored on the current branch.
> - Every commit must have a unique identifier.
> - Commit history must be returned oldest first.
> - Empty commit messages must raise ValueError.
> - Whitespace-only commit messages must raise ValueError.
> - A commit with an empty changes dictionary is valid.
> - A rejected commit must not modify history.
> - Do not implement checkout, new branch creation, merge, or conflict detection yet.
> - Do not add get_files() or other APIs that are not required by the current tests.
> - Keep the implementation small, readable, and suitable for the current TDD stage.
>
> Also briefly explain:
> 1. What you changed
> 2. Why each change is necessary
> 3. Any assumptions you made
>
> Do not add functionality beyond what is required by the existing tests.

---

### 4.20 AI Implementation Response Summary

Claude proposed expanding the `Repository` class with:

- An `_commits` dictionary containing commit history for each branch.
- An `itertools.count()` counter for generating sequential unique commit IDs.
- A `commit()` method.
- Validation for empty and whitespace-only commit messages.
- Storage of commit IDs, messages, and file state.
- A revised `history()` method that returns stored commits.
- A `get_files()` method for retrieving the current file state.
- An explicit `TypeError` for non-string commit messages.
- Updating `branches[current_branch]` to store the latest commit ID.

Claude also suggested storing complete file snapshots in each commit.

---

### 4.21 My Evaluation of the AI Implementation

I reviewed the proposed implementation before adding it to `src/mini_vcs.py`.

I accepted:

- Using `_commits` to replace the hardcoded Feature 1 history.
- Using a counter to generate simple unique commit identifiers.
- Validating the message before modifying history.
- Using `message.strip()` to detect empty and whitespace-only messages.
- Updating `branches[current_branch]` with the latest commit ID.
- Returning history in insertion order.

However, I did not accept the implementation unchanged.

Claude again added `get_files()`, even though the implementation prompt specifically stated not to add this API. Since none of the current tests required it, I removed it.

Claude also added explicit `TypeError` handling for non-string commit messages. This behaviour was not defined in the current specification or covered by the Feature 2 tests, so I removed it rather than introducing untested behaviour.

The AI proposed storing complete file snapshots by calling `get_files()` and applying the new changes. This was more functionality than the current TDD stage required. Instead, each commit stores a copy of its supplied `changes` dictionary. More advanced file-state behaviour can be introduced later when branching, checkout, and merge tests require it.

### Decision

**Modified**

The core commit-history design was retained, but unnecessary APIs, validation, and premature snapshot functionality were removed.

---

### 4.22 Final Feature 2 Implementation

The reviewed implementation added to `src/mini_vcs.py` was:

```python
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
```

---

### 4.23 GREEN Stage — Test Execution

After the reviewed implementation was added, the complete test suite was executed again using:

```text
python -m pytest -v
```

Pytest collected twelve tests and all twelve passed:

```text
12 passed
```

This included:

- 4 Feature 1 repository-creation tests
- 8 Feature 2 commit/history tests

The successful Feature 1 tests acted as regression tests and confirmed that adding Feature 2 had not broken the previously implemented repository-creation behaviour.

### Result

**GREEN — 12 passed**

### Evidence

`screenshots/04_commit_green.png`

---

### 4.24 Feature 2 Reflection

Feature 2 demonstrated the importance of reviewing AI-generated tests and implementation rather than accepting them automatically.

The AI identified useful test cases such as whitespace-only messages, unique identifiers, empty change sets, and ensuring that rejected commits do not alter history.

However, the AI repeatedly attempted to introduce `get_files()` even though that API was not part of the current specification. It also proposed non-string message validation and full file-snapshot behaviour that were not required by the current tests.

Removing these additions kept the implementation aligned with the current requirements and with the TDD principle of implementing only the functionality required by the reviewed tests.

Feature 2 successfully completed the TDD cycle:

**Requirements → AI test design → Human review → 8 selected tests → RED (8 failed, 4 passed) → AI implementation → Human review/modification → GREEN (12 passed) → Regression confirmed**

---

## Feature 3 — Branching

### 4.25 Feature Description

The third feature developed using TDD was branch creation.

The required behaviour was:

- A new branch can be created from the current branch.
- The new branch inherits the current branch's head at the time of creation.
- Creating a branch does not automatically switch the current branch.
- A branch can be created before any commits exist.
- Empty branch names are rejected.
- Whitespace-only branch names are rejected.
- Duplicate branch names are rejected.
- A rejected branch creation must not modify existing branch state.
- Branch state must remain independent after creation.

Checkout, merge, and conflict detection were not implemented during this feature.

---

### 4.26 Initial AI Test-Design Prompt

The following prompt was given to Claude before implementing Feature 3:

> I am continuing AI-assisted Test-Driven Development for my Mini Version Control System.
>
> Feature 3 is Branching.
>
> Existing functionality:
> - A new repository starts with a single branch named "main".
> - "main" is the current branch.
> - Commits can be created on the current branch.
> - Commit history is returned oldest first.
> - Each commit has a unique identifier.
>
> Requirements for Feature 3:
> - A new branch must be created from the current branch.
> - The new branch must inherit the current branch's existing commit history.
> - The new branch must inherit the current branch's current state at the time it is created.
> - Creating a branch must not automatically switch the current branch.
> - An empty branch name must be rejected.
> - A whitespace-only branch name must be rejected.
> - A duplicate branch name must be rejected.
> - A rejected branch creation must not modify the existing repository state.
>
> Generate ONLY the pytest unit-test design for this feature.
>
> For each test, include:
> 1. Test name
> 2. What it checks
> 3. Why it is necessary
>
> Include:
> - normal cases
> - boundary cases
> - invalid cases
> - regression-relevant cases
>
> Do not write implementation code.
> Do not write the branch creation method.
> Do not design tests for checkout, merge, or conflict detection.
> Do not invent new public APIs unless they are clearly necessary from the existing specification.
> Keep the response concise.

---

### 4.27 AI Test-Design Response Summary

Claude proposed thirteen tests:

1. `test_branch_can_be_created`
2. `test_branch_count_increases_by_one`
3. `test_new_branch_inherits_commit_history`
4. `test_new_branch_inherits_current_file_state`
5. `test_creating_a_branch_does_not_switch_to_it`
6. `test_branch_created_from_empty_repository_has_no_commits`
7. `test_single_character_branch_name_is_accepted`
8. `test_empty_branch_name_is_rejected`
9. `test_whitespace_only_branch_name_is_rejected`
10. `test_duplicate_branch_name_is_rejected`
11. `test_creating_a_branch_named_main_is_rejected`
12. `test_rejected_branch_creation_leaves_branches_unchanged`
13. `test_branches_are_independent_after_creation`

Claude also suggested changing `history()` to support an optional branch parameter and again suggested using `get_files()` so that a branch other than the current branch could be inspected.

Claude highlighted a possible Python list-aliasing problem if two branches shared the same commit-history list.

---

### 4.28 My Evaluation of the AI-Generated Tests

I reviewed the proposed tests before adding them to the project.

I accepted the tests covering:

- Successful branch creation.
- Branch count increasing without removing `main`.
- Creating a branch without automatically switching to it.
- Creating a branch before any commits exist.
- A single-character branch name.
- Empty branch-name rejection.
- Whitespace-only branch-name rejection.
- Duplicate branch-name rejection.
- Repository state remaining unchanged after rejected branch creation.

Some tests required modification.

Claude proposed testing inherited commit history by changing the existing `history()` API to accept a branch name. I decided not to expand the public API only to make a test easier to write.

Instead, I modified this behaviour to verify that a newly created branch receives the same head commit identifier as the current branch:

```python
assert repo.branches["feature"] == repo.branches["main"]
```

Claude's branch-independence test also required inspecting another branch's history. I modified it to test independence using branch head identifiers. After creating a branch and making another commit on `main`, the new `main` head must differ from the unchanged `feature` head.

I did not use the proposed file-state inheritance test because it again depended on a `get_files()` API that was not defined in the current specification.

I also did not include a separate test for creating a branch named `main`. The existing duplicate-name test already verifies the general rule that an existing branch name cannot be created again.

### Decision

**Modified**

Claude proposed thirteen tests. After reviewing API assumptions, overlap, and project scope, eleven tests were selected or modified for Feature 3.

---

### 4.29 Initial Automated Tests

The following eleven tests were added to `tests/test_mini_vcs.py` before implementing `create_branch()`:

```python
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
```

The twelve existing Feature 1 and Feature 2 tests remained unchanged and continued to act as regression tests.

---

### 4.30 RED Stage — Initial Test Execution

Before implementing `create_branch()`, the complete automated test suite was executed using:

```text
python -m pytest -v
```

Pytest collected twenty-three tests.

The twelve existing tests from Features 1 and 2 passed, while all eleven new Feature 3 tests failed.

The main failure was:

```text
AttributeError: 'Repository' object has no attribute 'create_branch'
```

The result was:

```text
11 failed, 12 passed
```

This was the expected RED stage because the branching tests were written and executed before `create_branch()` was implemented.

The twelve existing tests continuing to pass confirmed that the previously implemented repository and commit functionality had not been affected.

### Result

**RED — 11 failed, 12 passed**

### Evidence

`screenshots/05_branching_red.png`

---

### 4.31 AI Implementation Prompt

After recording the RED result, the following prompt was given to Claude:

> I am following AI-assisted Test-Driven Development for my Mini Version Control System.
>
> I am now implementing Feature 3: Branching.
>
> The following 11 pytest tests already exist and were executed before implementation:
>
> ```python
> def test_branch_can_be_created():
>     repo = Repository()
>     repo.create_branch("feature")
>     assert "feature" in repo.branches
>
>
> def test_branch_count_increases_by_one():
>     repo = Repository()
>     repo.create_branch("feature")
>     assert len(repo.branches) == 2
>     assert "main" in repo.branches
>
>
> def test_new_branch_inherits_current_head():
>     repo = Repository()
>     repo.commit("First commit", {"file.txt": "Hello"})
>     repo.create_branch("feature")
>     assert repo.branches["feature"] == repo.branches["main"]
>
>
> def test_creating_a_branch_does_not_switch_to_it():
>     repo = Repository()
>     repo.create_branch("feature")
>     assert repo.current_branch == "main"
>
>
> def test_branch_created_before_any_commit_has_no_head():
>     repo = Repository()
>     repo.create_branch("feature")
>     assert repo.branches["feature"] is None
>
>
> def test_single_character_branch_name_is_accepted():
>     repo = Repository()
>     repo.create_branch("f")
>     assert "f" in repo.branches
>
>
> def test_empty_branch_name_is_rejected():
>     repo = Repository()
>     with pytest.raises(ValueError):
>         repo.create_branch("")
>
>
> def test_whitespace_only_branch_name_is_rejected():
>     repo = Repository()
>     with pytest.raises(ValueError):
>         repo.create_branch("   ")
>
>
> def test_duplicate_branch_name_is_rejected():
>     repo = Repository()
>     repo.create_branch("feature")
>     with pytest.raises(ValueError):
>         repo.create_branch("feature")
>
>
> def test_rejected_branch_creation_leaves_branches_unchanged():
>     repo = Repository()
>     repo.create_branch("feature")
>     branches_before = dict(repo.branches)
>
>     with pytest.raises(ValueError):
>         repo.create_branch("feature")
>
>     assert repo.branches == branches_before
>
>
> def test_branch_head_is_independent_after_creation():
>     repo = Repository()
>     first_id = repo.commit("First commit", {"file.txt": "Hello"})
>     repo.create_branch("feature")
>
>     repo.commit("Second commit", {"other.txt": "World"})
>
>     assert repo.branches["feature"] == first_id
>     assert repo.branches["main"] != repo.branches["feature"]
> ```
>
> Current test result:
>
> 11 failed, 12 passed.
>
> All 12 existing Feature 1 and Feature 2 tests still pass.
>
> The 11 new Feature 3 tests fail because:
>
> AttributeError: 'Repository' object has no attribute 'create_branch'
>
> Please provide the smallest Python implementation necessary to make these Feature 3 tests pass while keeping all 12 existing tests passing.
>
> Requirements:
> - A new branch is created from the current branch.
> - The new branch must inherit the current branch's current head.
> - Creating a branch must not automatically switch the current branch.
> - A branch created before any commits must have no head.
> - Empty branch names must raise ValueError.
> - Whitespace-only branch names must raise ValueError.
> - Duplicate branch names must raise ValueError.
> - Rejected branch creation must not modify existing branch state.
> - Branch state must be independent after creation.
> - Do not implement checkout, merge, or conflict detection yet.
> - Do not add get_files().
> - Do not add an optional branch parameter to history().
> - Do not introduce new public APIs that are not required by these tests.
> - Keep the implementation small and readable.
>
> Important:
> The existing Repository implementation already has:
> - self._commits
> - self.branches
> - self.current_branch
> - self._counter
> - commit()
> - history()
>
> Do not unnecessarily rewrite working Feature 1 or Feature 2 functionality.
>
> Also briefly explain:
> 1. What you changed
> 2. Why each change is necessary
> 3. Any assumptions you made
> 4. Whether any part of your proposed implementation goes beyond the current tests
>
> Do not add functionality beyond what is required by the existing tests.

---

### 4.32 AI Implementation Response Summary

Claude proposed adding a single `create_branch()` method to the existing `Repository` class.

The proposed method:

- Checked whether the branch name was a string.
- Rejected empty and whitespace-only branch names.
- Rejected duplicate branch names.
- Copied the current branch's head commit ID to the new branch.
- Copied the current branch's commit-history list using `list()`.
- Returned the new branch name.

Claude correctly pointed out that directly assigning the existing commit-history list would cause both branches to share the same Python list object.

Claude also acknowledged that its explicit `TypeError` for non-string branch names went beyond the current tests.

---

### 4.33 My Evaluation of the AI Implementation

I accepted most of Claude's proposed branching implementation because it was small and directly related to the current Feature 3 requirements.

The validation for empty, whitespace-only, and duplicate branch names was accepted.

I also accepted:

```python
self.branches[name] = self.branches[self.current_branch]
```

This gives the newly created branch the same head commit as the current branch at the moment of creation.

An important part of the AI response was:

```python
self._commits[name] = list(self._commits[self.current_branch])
```

Using `list()` creates a separate commit-history list for the new branch. Without the copy, both branch names could reference the same mutable list. Later commits could then incorrectly appear in both branches.

However, Claude also proposed:

```python
if not isinstance(name, str):
    raise TypeError("Branch name must be a string")
```

No current specification requirement or Feature 3 test defines behaviour for non-string branch names. I therefore removed this additional validation rather than introducing untested behaviour.

Claude also referred again to `get_files()` from its earlier design, but this API was not added because it was not part of the reviewed implementation.

### Decision

**Modified**

The main branching implementation was accepted, but the unnecessary non-string `TypeError` validation was removed.

---

### 4.34 Final Feature 3 Implementation

The following method was added to the existing `Repository` class:

```python
def create_branch(self, name):
    """Create a branch starting from the current branch's head."""
    if not name.strip():
        raise ValueError("Branch name cannot be empty")

    if name in self.branches:
        raise ValueError(f"Branch '{name}' already exists")

    self.branches[name] = self.branches[self.current_branch]
    self._commits[name] = list(self._commits[self.current_branch])

    return name
```

The existing Feature 1 and Feature 2 implementation was kept unchanged.

---

### 4.35 GREEN Stage — Test Execution

After adding the reviewed `create_branch()` implementation, the complete test suite was executed again:

```text
python -m pytest -v
```

Pytest collected twenty-three tests and all twenty-three passed:

```text
23 passed
```

This included:

- 4 Feature 1 repository-creation tests
- 8 Feature 2 commit/history tests
- 11 Feature 3 branching tests

The successful execution of all previous tests confirmed that the new branching implementation did not introduce regressions into the earlier functionality.

### Result

**GREEN — 23 passed**

### Evidence

`screenshots/06_branching_green.png`

---

### 4.36 Feature 3 Reflection

Feature 3 showed another example of why AI-generated test and implementation designs need human review.

Claude correctly identified important branching risks, particularly the possibility of a Python aliasing bug when copying a mutable commit-history list. Its use of:

```python
list(self._commits[self.current_branch])
```

helped ensure that the new branch received an independent history list.

However, the AI also attempted to expand the existing public API during test design by suggesting an optional branch parameter for `history()` and again referring to `get_files()`. These additions were not necessary for the current feature and were rejected.

The implementation response also introduced non-string branch-name validation that was not required by the specification or tests. This was removed before the implementation was accepted.

The Feature 3 TDD cycle was:

**Requirements → AI test design → Human review → 11 selected/modified tests → RED (11 failed, 12 passed) → AI implementation → Human review/modification → GREEN (23 passed) → Regression confirmed**

---

## Feature 4 — Checkout

### 4.37 Feature Description

The fourth feature developed using TDD was branch checkout.

The required behaviour was:

- `checkout(branch_name)` switches the current branch to an existing branch.
- The user can switch from `main` to another branch and back to `main`.
- Checking out the current branch is allowed.
- Checkout must not create, delete, or modify branches.
- Checkout must preserve the target branch's commit history.
- Commits created after checkout must be recorded on the currently checked-out branch.
- Different branches must maintain independent commit histories.
- Checking out a non-existent branch must raise `ValueError`.
- A failed checkout must leave the current branch unchanged.
- Checkout itself must not create commits or modify branch history.

Merge and conflict detection were not implemented during this feature.

---

### 4.38 Initial AI Test-Design Prompt

The following prompt was given to Claude before implementing Feature 4:

> I am continuing AI-assisted Test-Driven Development for my Mini Version Control System.
>
> Feature 4 is Checkout.
>
> Existing functionality:
> - A new repository starts with a single branch named "main".
> - Commits can be created on the current branch.
> - Commit history is returned oldest first.
> - New branches can be created from the current branch.
> - A newly created branch inherits the current branch's head and commit history.
> - Creating a branch does not automatically switch the current branch.
>
> Requirements for Feature 4:
> - checkout(branch_name) must switch the current branch to an existing branch.
> - Checking out "main" or another existing branch must update current_branch.
> - Checking out a non-existent branch must raise ValueError.
> - If checkout fails, current_branch must remain unchanged.
> - Checking out a branch must preserve that branch's own commit history.
> - Commits made after checkout must be recorded only on the currently checked-out branch.
> - Switching between branches must preserve each branch's independent history.
> - Checkout itself must not create a commit or modify branch history.
>
> Generate ONLY the pytest unit-test design for this feature.
>
> For each test, include:
> 1. Test name
> 2. What it checks
> 3. Why it is necessary
>
> Include:
> - normal cases
> - boundary cases
> - invalid cases
> - regression-relevant cases
>
> Do not write implementation code.
> Do not write the checkout method.
> Do not design tests for merge or conflict detection.
> Do not add get_files().
> Do not add optional parameters to history().
> Do not invent new public APIs unless clearly required by the existing specification.
> Keep the response concise.

---

### 4.39 AI Test-Design Response Summary

Claude proposed thirteen checkout tests:

1. `test_checkout_switches_current_branch`
2. `test_can_checkout_back_to_main`
3. `test_checkout_does_not_change_branch_count`
4. `test_checkout_preserves_history_of_the_target_branch`
5. `test_commit_after_checkout_is_recorded_on_the_new_branch`
6. `test_commit_after_checkout_does_not_affect_the_other_branch`
7. `test_branches_keep_separate_histories_across_multiple_switches`
8. `test_checkout_current_branch_is_allowed`
9. `test_checkout_branch_with_no_commits`
10. `test_checkout_of_nonexistent_branch_is_rejected`
11. `test_checkout_of_empty_branch_name_is_rejected`
12. `test_failed_checkout_leaves_current_branch_unchanged`
13. `test_failed_checkout_leaves_history_intact`

Claude identified `test_commit_after_checkout_does_not_affect_the_other_branch` as particularly important because it could expose a mutable-list aliasing problem from branch creation.

It also highlighted the recurring testing pattern of validating input before changing repository state.

---

### 4.40 My Evaluation of the AI-Generated Tests

I reviewed the thirteen proposed tests before adding them to the test suite.

I accepted tests covering:

- Switching to an existing branch.
- Returning to `main`.
- Preserving the target branch's history.
- Recording commits on the checked-out branch.
- Keeping commits isolated between branches.
- Maintaining separate histories across multiple branch switches.
- Checking out the current branch.
- Checking out a branch with no commits.
- Rejecting a non-existent branch.
- Keeping `current_branch` unchanged after a failed checkout.

I modified the proposed branch-count test. Instead of only checking that the number of branches remained the same, I stored a copy of the complete `branches` dictionary before checkout and compared it afterward:

```python
branches_before = dict(repo.branches)
repo.checkout("feature")
assert repo.branches == branches_before
```

This provides stronger evidence that checkout does not modify branch state.

I did not include a separate empty-name checkout test because an empty string is already a non-existent branch and is therefore covered by the existing invalid-branch behaviour.

I also did not include a separate failed-checkout-history test because the selected tests already verify that checkout does not modify branches and that failed checkout leaves the selected branch unchanged.

### Decision

**Modified**

Claude proposed thirteen tests. After reviewing overlap and test value, eleven tests were selected or modified for Feature 4.

---

### 4.41 Initial Automated Tests

The following eleven tests were added to `tests/test_mini_vcs.py` before implementing `checkout()`:

```python
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
```

The twenty-three tests from Features 1, 2, and 3 remained in the suite as regression tests.

---

### 4.42 RED Stage — Initial Test Execution

Before implementing `checkout()`, the complete test suite was executed using:

```text
python -m pytest -v
```

Pytest collected thirty-four tests.

All twenty-three existing tests passed, while the eleven new Feature 4 tests failed.

The main failure was:

```text
AttributeError: 'Repository' object has no attribute 'checkout'
```

The result was:

```text
11 failed, 23 passed
```

This was the expected RED stage because the checkout tests were written and executed before the checkout method existed.

The twenty-three existing tests continuing to pass confirmed that repository creation, commits, history, and branch creation remained functional.

### Result

**RED — 11 failed, 23 passed**

### Evidence

`screenshots/07_checkout_red.png`

---

### 4.43 AI Implementation Prompt

After recording the RED result, the following prompt was given to Claude:

> I am following AI-assisted Test-Driven Development for my Mini Version Control System.
>
> I am now implementing Feature 4: Checkout.
>
> The 11 Feature 4 pytest tests already exist and were executed before implementation.
>
> Current test result:
>
> 11 failed, 23 passed.
>
> All 23 existing Feature 1, Feature 2, and Feature 3 tests still pass.
>
> The 11 new Feature 4 tests fail because:
>
> AttributeError: 'Repository' object has no attribute 'checkout'
>
> Please provide the smallest Python implementation necessary to make these Feature 4 tests pass while keeping all 23 existing tests passing.
>
> Requirements:
> - checkout(branch_name) must switch current_branch to an existing branch.
> - It must be possible to switch from main to another branch and back to main.
> - Checking out the current branch is allowed and should behave as a no-op.
> - Checking out a branch must not create, delete, or otherwise modify branches.
> - Existing branch history must remain unchanged by checkout.
> - Commits after checkout must be recorded only on the checked-out branch.
> - Different branches must maintain independent histories.
> - Checking out a non-existent branch must raise ValueError.
> - A failed checkout must leave current_branch unchanged.
> - Do not implement merge or conflict detection yet.
> - Do not add get_files().
> - Do not add optional parameters to history().
> - Do not introduce new public APIs that are not required by these tests.
> - Keep the implementation small and readable.
>
> Important:
> The existing Repository implementation already contains:
> - self._commits
> - self.branches
> - self.current_branch
> - self._counter
> - commit()
> - history()
> - create_branch()
>
> Do not unnecessarily rewrite the working Feature 1, Feature 2, or Feature 3 functionality.
>
> Also briefly explain:
> 1. What you changed.
> 2. Why each change is necessary.
> 3. Any assumptions you made.
> 4. Whether any part of the proposed implementation goes beyond the current tests.
>
> Do not add functionality beyond what is required by the existing tests.

---

### 4.44 AI Implementation Response Summary

Claude proposed adding one small `checkout()` method:

```python
def checkout(self, name):
    """Switch the current branch to an existing branch."""
    if name not in self.branches:
        raise ValueError(f"Branch '{name}' does not exist")

    self.current_branch = name
    return name
```

The AI explained that validation must happen before changing `current_branch`. This ensures that a failed checkout does not leave the repository pointing to a branch that does not exist.

Claude also explained that no special case is required for checking out the branch that is already current. Assigning the same branch name again naturally behaves as a no-op.

The AI did not add type validation because dictionary membership checking already handles values that are not existing branch keys.

Claude identified `return name` as behaviour that was not required by any current test.

---

### 4.45 My Evaluation of the AI Implementation

The proposed implementation was appropriately small and closely matched the current Feature 4 requirements.

I accepted:

```python
if name not in self.branches:
    raise ValueError(f"Branch '{name}' does not exist")
```

The validation occurs before any state change. This is important because assigning `current_branch` before validation could leave the repository in an invalid state even though an exception was raised.

I also accepted:

```python
self.current_branch = name
```

No other repository state needs to change during checkout. The existing `commit()` and `history()` methods already use `current_branch`, so switching this value automatically redirects later operations to the selected branch.

Claude also proposed:

```python
return name
```

No requirement or Feature 4 test defines a return value for `checkout()`. I therefore removed this line to keep the implementation limited to tested behaviour.

### Decision

**Modified**

The core AI-generated implementation was accepted, but the unnecessary return value was removed.

---

### 4.46 Final Feature 4 Implementation

The following method was added to the existing `Repository` class:

```python
def checkout(self, name):
    """Switch the current branch to an existing branch."""
    if name not in self.branches:
        raise ValueError(f"Branch '{name}' does not exist")

    self.current_branch = name
```

No existing Feature 1, Feature 2, or Feature 3 implementation was changed.

---

### 4.47 GREEN Stage — Test Execution

After adding the reviewed `checkout()` implementation, the complete test suite was executed again:

```text
python -m pytest -v
```

All thirty-four tests passed:

```text
34 passed in 0.13s
```

This included:

- 4 Feature 1 repository-creation tests
- 8 Feature 2 commit/history tests
- 11 Feature 3 branching tests
- 11 Feature 4 checkout tests

The successful execution of all previous tests confirmed that checkout functionality did not introduce regressions into repository creation, commits, history, or branch creation.

### Result

**GREEN — 34 passed**

### Evidence

`screenshots/08_checkout_green.png`

---

### 4.48 Feature 4 Reflection

Feature 4 demonstrated how a small implementation can still require meaningful test design.

The final `checkout()` implementation only validates the requested branch and changes `current_branch`. However, the tests verify more than this direct behaviour. They confirm that branch histories remain independent, checkout does not modify the branch structure, commits are redirected to the selected branch, invalid checkout attempts do not change state, and switching repeatedly between branches preserves their histories.

An important regression test was:

```python
test_commit_after_checkout_does_not_affect_other_branch
```

This test also provided stronger evidence that the `list()` copy introduced during Feature 3 branch creation was necessary. If two branches shared the same mutable commit-history list, a commit on the checked-out feature branch could incorrectly appear in `main`.

The AI implementation was mostly appropriate, but it returned the branch name even though no current requirement or test required a return value. Removing this line kept the implementation aligned with the TDD principle of adding only currently required behaviour.

A recurring testing strategy is now visible across multiple features: **validate before mutating repository state**. Tests for rejected commits, rejected branch creation, and failed checkout all verify that invalid operations do not partially modify the repository.

The Feature 4 TDD cycle was:

**Requirements → AI test design → Human review → 11 selected/modified tests → RED (11 failed, 23 passed) → AI implementation → Human review/modification → GREEN (34 passed) → Regression confirmed**

---

# Stage 5 — Remaining Feature Development

**Status:** In progress.

The same AI-assisted TDD process will be followed for the remaining features:

- Feature 5 — Merge
- Feature 6 — Conflict Detection

For each feature, this log will record the AI prompt, AI response summary, my evaluation, accepted/modified/rejected decisions, RED test result, implementation review, GREEN result, and evidence.
---

# Stage 6 — Evaluation and Improvement of AI Output

**Status:** To be completed during development.

This section will document specific examples where AI-generated code or tests contained incorrect assumptions, defects, missing cases, or maintainability issues. Where appropriate, before-and-after examples and regression tests will be recorded.

---

# Stage 7 — Final Testing and Reflection

**Status:** To be completed after all features are implemented.

The final section will record:

- Full automated test result
- Test coverage result
- Final GitHub repository evidence
- Areas where AI performed well
- Areas where AI was incorrect or incomplete
- How TDD affected development
- How the test suite improved during development
- Improvements that could be made with additional time

---

## Feature-Level Development Record Template

### Feature
[Feature name]

### AI Prompt
[Exact prompt used]

### AI Response Summary
[Short summary]

### My Evaluation
[What was correct, incorrect, missing, or unnecessary]

### Decision
Accepted / Modified / Rejected

### Changes Made
[Changes made after reviewing AI output]

### Tests Executed
[pytest command]

### Result
RED / GREEN / Regression passed

### Evidence
[Screenshot filename and/or Git commit]
