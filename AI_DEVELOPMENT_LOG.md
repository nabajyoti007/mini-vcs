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

## Feature 5 — Merge

### 5.1 Feature Description

The fifth feature developed using AI-assisted TDD was branch merging.

The required behaviour was:

- `merge(source_branch)` merges a named source branch into the current branch.
- The source branch must exist.
- A branch cannot be merged into itself.
- A successful merge creates one new commit on the current branch.
- Changes made on the source branch after divergence are included in the merge commit.
- Multiple source commits are combined into the merge commit.
- If the same file is changed multiple times on the source branch, the latest source value is used.
- Existing current-branch history must be preserved.
- The source branch must remain unchanged.
- If the source branch has no new commits, a merge commit with an empty `changes` dictionary is still created.
- Conflict detection is not handled in this feature and is deferred to Feature 6.

---

### 5.2 Initial AI Test-Design Prompt

The following prompt was given to Claude before implementing merge:

> I am continuing AI-assisted Test-Driven Development for my Mini Version Control System.
>
> Feature 5 is Merge.
>
> Existing functionality:
> - A repository starts on "main".
> - Commits can be created on the current branch.
> - Commit history is returned oldest first.
> - Branches can be created from the current branch.
> - A new branch inherits the current branch's head and commit history.
> - Checkout switches between existing branches.
> - Different branches maintain independent commit histories.
>
> Current commit representation:
> - Each commit stores:
>   - "id"
>   - "message"
>   - "changes"
> - "changes" is a dictionary mapping file names to their new contents.
> - There is currently no get_files() public API.
>
> Requirements for Feature 5:
> - merge(source_branch) merges a named source branch into the current branch.
> - The source branch must exist.
> - A branch must not be merged into itself.
> - A successful non-conflicting merge must update the current branch.
> - The source branch must remain unchanged after a successful merge.
> - Merge must preserve existing commit history.
> - If the source branch contains changes that do not conflict with the current branch, those changes should be incorporated into the current branch.
> - The merge operation should create a new commit on the current branch representing the merge.
> - Merge behaviour must work when the source branch has no new commits since divergence.
> - Do not implement automatic conflict resolution in this feature.
> - Conflict detection will be handled as Feature 6.
>
> Generate ONLY the pytest unit-test design for Feature 5.
>
> For each test, include:
> 1. Test name
> 2. What it checks
> 3. Why it is necessary
>
> Include normal, boundary, invalid and regression-relevant cases.
>
> Do not write implementation code.
> Do not write the merge method.
> Do not add get_files().
> Do not add optional parameters to history().
> Do not invent new public APIs unless clearly required.
> Do not design automatic conflict resolution yet.

---

### 5.3 AI Test-Design Response Summary

Claude proposed fourteen possible merge tests covering:

- creation of a merge commit,
- merge commit IDs,
- incorporation of source changes,
- preservation of current-branch changes,
- preservation of source branch state,
- history ordering,
- source branches with no new commits,
- branches with no commits,
- single and multiple file changes,
- missing source branches,
- self-merge rejection,
- state preservation after a failed merge,
- branch-list preservation,
- repeated merges.

Claude also identified an important design issue: merge needs a way to distinguish commits inherited when the branch was created from commits added to the source branch after divergence.

The AI discussed several possible approaches, including replaying source changes, comparing final states, and performing a three-way merge using a common ancestor.

---

### 5.4 My Evaluation of the AI-Generated Tests

I reviewed the proposed tests and reduced the set to nine tests that directly matched the current Feature 5 requirements and existing public API.

I selected tests covering:

1. Creation of exactly one merge commit.
2. Incorporation of source changes.
3. Preservation of current-branch history.
4. Preservation of the source branch.
5. Merge when the source has no new commits.
6. Multiple source changes.
7. Rejection of a non-existent source branch.
8. Rejection of merging a branch into itself.
9. Preservation of repository state after a failed merge.

I did not include a separate test requiring `merge()` to return a commit ID because the specification did not require a merge return value.

I also did not include repeated-merge behaviour because the current specification does not define how already-merged ancestry should be tracked.

The AI initially raised uncertainty about whether commits stored `"files"` or `"changes"`. I verified the actual implementation and confirmed that commits store:

```python
{
    "id": commit_id,
    "message": message,
    "changes": dict(changes),
}
```

Therefore, the tests were designed against the actual `"changes"` representation rather than an invented snapshot API.

### Decision

**Modified**

The AI-generated design was useful, but I selected a smaller set of tests and kept them aligned with the existing specification and implementation.

---

### 5.5 Initial Automated Tests

Nine merge tests were added to `tests/test_mini_vcs.py` before implementation.

The tests covered normal, boundary, invalid, and regression-relevant behaviour.

Examples included:

```python
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
```

Source changes were also verified:

```python
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
```

Invalid merge behaviour was tested using:

```python
def test_merge_of_nonexistent_branch_is_rejected():
    repo = Repository()

    with pytest.raises(ValueError):
        repo.merge("does_not_exist")


def test_merge_branch_into_itself_is_rejected():
    repo = Repository()

    with pytest.raises(ValueError):
        repo.merge("main")
```

A regression test also confirmed that a failed merge does not partially modify repository state.

---

### 5.6 RED Stage — Initial Test Execution

Before implementing `merge()`, the complete test suite was executed:

```text
python -m pytest -v
```

The thirty-four tests from Features 1–4 continued to pass.

All nine new Feature 5 tests failed because `merge()` did not yet exist.

The main error was:

```text
AttributeError: 'Repository' object has no attribute 'merge'
```

The result was:

```text
9 failed, 34 passed in 0.43s
```

This was the expected RED stage and demonstrated that the merge tests existed and were executed before implementation.

### Result

**RED — 9 failed, 34 passed**

### Evidence

`screenshots/09_merge_red.png`

---

### 5.7 AI Implementation Prompt

After recording the RED stage, Claude was asked to provide the smallest implementation required to satisfy the nine merge tests.

The prompt specified that:

- only source changes after divergence should be merged,
- inherited commits must not be merged again,
- multiple source commits should be combined,
- the latest source value should win if a file appears in multiple source commits,
- validation must happen before state modification,
- the source branch must remain unchanged,
- conflict detection must not yet be implemented,
- no `get_files()` or new public APIs should be introduced,
- existing Features 1–4 should not be unnecessarily rewritten.

The current RED result of `9 failed, 34 passed` was also provided to the AI.

---

### 5.8 AI Implementation Response Summary

Claude proposed determining source-side commits by comparing commit IDs.

The current branch's commit IDs were collected into a set. Source commits whose IDs were not present in that set were treated as commits made after divergence.

The proposed logic was conceptually:

```python
current_ids = {
    commit["id"] for commit in self._commits[self.current_branch]
}

merged_changes = {}

for commit in self._commits[source_branch]:
    if commit["id"] not in current_ids:
        merged_changes.update(commit["changes"])
```

Claude recommended using the existing `commit()` method to create the merge commit instead of manually creating another commit structure.

The AI correctly noted that repeated calls to `dict.update()` mean the latest source-side value is retained when the same file appears in multiple source commits.

Claude also identified an important limitation: this is a simplified set-difference approach rather than a complete Git-style common-ancestor algorithm.

---

### 5.9 My Evaluation of the AI Implementation

The proposed approach was appropriate for the current simplified MiniVCS requirements and the Feature 5 tests.

I accepted the following ideas:

- Validate the source branch before changing repository state.
- Reject merging the current branch into itself.
- Compare commit IDs to avoid treating inherited commits as new source changes.
- Combine source changes in chronological order.
- Use `dict.update()` so later source changes overwrite earlier source changes for the same file.
- Reuse the already-tested `commit()` method to create the merge commit.
- Leave the source branch unchanged.

I also reviewed an important limitation of the approach.

The implementation does not perform true three-way merge analysis. It determines source-side commits using commit-ID membership. This works for the current simple branching structure but may not correctly represent ancestry after more complicated repeated merges.

The implementation also does not detect files modified differently on both branches. At this stage, such a situation could allow source changes to be included without detecting that the current branch also modified the same file.

This limitation was intentionally left for Feature 6, where conflict-detection tests will be written before improving the implementation.

### Decision

**Modified / Accepted for current Feature 5 scope**

The core AI approach was accepted, while unnecessary return-value behaviour was avoided and the ancestry/conflict limitations were explicitly documented.

---

### 5.10 Final Feature 5 Implementation

The following method was added to the existing `Repository` class:

```python
def merge(self, source_branch):
    """Merge changes from another branch into the current branch."""
    if source_branch not in self.branches:
        raise ValueError(f"Branch '{source_branch}' does not exist")

    if source_branch == self.current_branch:
        raise ValueError("Cannot merge a branch into itself")

    current_ids = {
        commit["id"] for commit in self._commits[self.current_branch]
    }

    merged_changes = {}

    for commit in self._commits[source_branch]:
        if commit["id"] not in current_ids:
            merged_changes.update(commit["changes"])

    self.commit(
        f"Merge branch '{source_branch}'",
        merged_changes
    )
```

No existing Feature 1–4 methods were replaced.

---

### 5.11 GREEN Stage — Test Execution

After adding the reviewed `merge()` implementation, the complete test suite was executed again:

```text
python -m pytest -v
```

The result was:

```text
43 passed in 0.15s
```

All previous tests continued to pass and all nine new merge tests passed.

### Result

**GREEN — 43 passed**

### Evidence

`screenshots/10_merge_green.png`

---

### 5.12 Critical Observation Before Feature 6

Although all forty-three tests pass, the merge implementation is not yet complete according to the final MiniVCS specification.

The current implementation does not determine whether the same file was changed differently on both branches after divergence.

For example:

```text
Base:
config.txt = "A"

main:
config.txt = "B"

feature:
config.txt = "C"
```

The current Feature 5 implementation does not identify this as a conflict.

This is an important example of why passing tests does not automatically mean the complete system is correct. The Feature 5 tests were deliberately scoped to non-conflicting merge behaviour.

Feature 6 will introduce tests that expose this missing behaviour before conflict detection is implemented.

---

### 5.13 Feature 5 Reflection

Feature 5 showed that merge behaviour requires more reasoning than the previous repository operations.

The AI correctly identified that inherited commits should not simply be treated as new source changes. Commit IDs were therefore used to distinguish shared history from source-side commits.

The human review was important because the AI initially questioned the actual commit representation. Checking the existing source code confirmed that the system stores `"changes"` rather than `"files"`.

The final implementation passed all forty-three tests, but analysis identified that successful tests only demonstrate the behaviours currently tested. Conflict scenarios remain intentionally unsupported.

The Feature 5 TDD cycle was:

**Requirements → AI test design → Human review → 9 selected tests → RED (9 failed, 34 passed) → AI implementation → Human review → GREEN (43 passed) → Limitation identified for Feature 6**

---

# Stage 6 — Conflict Detection

**Status:** Not started.

Feature 6 will use the same AI-assisted TDD process to implement the remaining conflict-detection requirements:

- Detect when the same file was modified differently on both branches after divergence.
- Report the conflicting filename or filenames.
- Prevent creation of a merge commit when conflicts exist.
- Leave both branches unchanged after a conflicting merge.
- Allow identical changes to the same file without treating them as conflicts.
- Continue supporting non-conflicting merges.
---

# Stage 6 — Feature 6: Conflict Detection

## 6.1 Feature Description

The sixth feature developed using AI-assisted Test-Driven Development was conflict detection during branch merging.

Feature 5 provided non-conflicting merge functionality, but it did not detect situations where both branches modified the same file differently after divergence.

The requirements for Feature 6 were:

- A conflict occurs when the same file is modified differently on both branches after divergence.
- Changes made before divergence must not be considered conflicts.
- If only one branch modifies a file, the merge must succeed.
- If both branches modify the same file to the same content, it must not be treated as a conflict.
- If both branches add the same new file with different contents, it is a conflict.
- Multiple conflicting filenames must be reported.
- One conflict among several changes must cause the whole merge to fail.
- A conflicting merge must not create a merge commit.
- A conflicting merge must leave the current branch unchanged.
- A conflicting merge must leave the source branch unchanged.
- Existing Features 1–5 must continue to work.

---

## 6.2 Initial AI Test-Design Prompt

Before modifying the existing merge implementation, Claude was asked to design tests for conflict detection.

The prompt explained the existing commit structure:

```python
{
    "id": commit_id,
    "message": message,
    "changes": dict(changes)
}
```

It also explained that the existing `merge(source_branch)` implementation could merge source-side changes but did not yet detect conflicts.

Claude was specifically asked to generate only pytest test designs covering:

- normal non-conflicting cases,
- direct conflict cases,
- identical-change cases,
- multiple-file cases,
- state-preservation cases,
- regression-relevant cases.

The prompt also instructed the AI:

- not to implement conflict detection yet,
- not to modify `merge()`,
- not to add `get_files()`,
- not to add optional parameters to `history()`,
- not to invent unnecessary public APIs,
- and to consider all existing 43 tests from Features 1–5.

---

## 6.3 AI Test-Design Response Summary

Claude proposed fifteen possible tests.

The proposed tests covered:

- different files changed on different branches,
- source-only changes,
- the same file changed differently,
- identifying conflicting filenames,
- the same new file added differently,
- identical changes to the same file,
- identical additions,
- one conflict among multiple changes,
- multiple conflicts,
- preservation of history after conflict,
- preservation of branch heads,
- preservation of the source branch,
- regression tests for invalid merges,
- and recovery after a conflict.

Claude also suggested introducing a new exception:

```python
MergeConflictError
```

with a `files` attribute for accessing conflicting filenames.

The AI identified several limitations of the current data model, including the absence of a full Git-style common-ancestor representation and the fact that commits store changes rather than complete snapshots.

---

## 6.4 My Evaluation of the AI-Generated Test Design

The AI-generated test design provided useful conflict scenarios, but I modified it before implementation.

I selected ten tests that directly matched the specification and the existing MiniVCS API.

The selected tests covered:

1. Different files merging without conflict.
2. A source-only change not being considered a conflict.
3. The same file changed differently producing a conflict.
4. The conflict error identifying the filename.
5. The same file changed to the same content not producing a conflict.
6. A new file added differently on both branches producing a conflict.
7. One conflict among multiple changes failing the whole merge.
8. Multiple conflicting filenames being reported.
9. A conflicting merge leaving both branches unchanged.
10. The same new file added with identical content not producing a conflict.

I rejected the proposed `MergeConflictError` API at the test-design stage.

The existing project already used `ValueError` for invalid operations, and the specification required conflicting filenames to be reported but did not require a new public exception class.

Therefore, the tests used:

```python
with pytest.raises(ValueError) as error:
    repo.merge("feature")
```

and checked the error message when necessary:

```python
assert "shared.txt" in str(error.value)
```

Existing Feature 5 tests already covered missing branches and self-merges, so duplicate regression tests for these behaviours were not added.

### Decision

**Modified**

The AI-generated test ideas were useful, but the proposed public exception API and some redundant tests were rejected.

---

## 6.5 Feature 6 Automated Tests

Ten new tests were added to `tests/test_mini_vcs.py` before conflict-detection implementation.

A direct conflict was tested using a scenario where both branches changed the same file differently:

```python
def test_same_file_changed_differently_is_a_conflict():
    repo = Repository()

    repo.commit("Base", {"shared.txt": "original"})
    repo.create_branch("feature")

    repo.commit("Main change", {"shared.txt": "main version"})

    repo.checkout("feature")
    repo.commit("Feature change", {"shared.txt": "feature version"})

    repo.checkout("main")

    with pytest.raises(ValueError):
        repo.merge("feature")
```

The filename-reporting requirement was tested separately:

```python
with pytest.raises(ValueError) as error:
    repo.merge("feature")

assert "shared.txt" in str(error.value)
```

The tests also checked that identical changes were not incorrectly classified as conflicts.

For example:

```python
repo.commit("Main change", {"shared.txt": "same"})

repo.checkout("feature")
repo.commit("Feature change", {"shared.txt": "same"})
```

The merge was expected to succeed because both branches reached the same content.

Multiple-file scenarios were also tested to ensure that one conflicting file caused the entire merge to fail and that multiple conflicting filenames were reported.

---

## 6.6 RED Stage — Initial Test Execution

After adding the ten Feature 6 tests, the complete test suite was executed before changing `merge()`:

```text
python -m pytest -v
```

The result was:

```text
6 failed, 47 passed in 0.48s
```

This was an important RED result because not all ten new tests failed.

Four new tests already passed because the existing Feature 5 merge implementation correctly handled several non-conflicting scenarios.

The six failing tests specifically exposed the missing conflict-detection behaviour:

```text
test_same_file_changed_differently_is_a_conflict
test_conflict_error_identifies_filename
test_new_file_added_differently_on_both_branches_is_conflict
test_one_conflict_among_multiple_changes_fails_whole_merge
test_multiple_conflicting_filenames_are_reported
test_conflicting_merge_leaves_current_branch_unchanged
```

The common failure was that the existing implementation did not raise `ValueError` when conflicting changes were encountered.

For example:

```text
Failed: DID NOT RAISE ValueError
```

### Result

**RED — 6 failed, 47 passed**

### Evidence

`screenshots/11_conflict_red.png`

This RED result demonstrated that the previous features remained functional while the newly specified conflict behaviour was not yet implemented.

---

## 6.7 AI Implementation Prompt

After recording the RED result, Claude was asked to provide the smallest implementation change needed to make the Feature 6 tests pass.

The AI was given:

- the existing `Repository` implementation,
- the current `merge()` implementation,
- the result of `6 failed, 47 passed`,
- the names of all six failing tests,
- and the complete conflict-detection requirements.

The prompt specifically required:

- conflict detection based on changes after divergence,
- identical changes not to produce false conflicts,
- validation before repository mutation,
- preservation of both branches after conflict,
- use of `ValueError`,
- no `MergeConflictError`,
- no `get_files()`,
- no new public APIs,
- and preservation of all Features 1–5.

---

## 6.8 AI Implementation Response Summary

Claude proposed calculating post-divergence changes on both branches.

It introduced the idea of:

```python
our_changes
```

for changes made on the current branch and:

```python
their_changes
```

for changes made on the source branch.

The AI proposed collecting the commit IDs from both histories and accumulating changes from commits that were not shared with the other branch.

The main conflict condition proposed by Claude was:

```python
name in our_changes and our_changes[name] != content
```

This means a conflict occurs only when:

1. both branches changed the same filename after divergence, and
2. the final changed contents are different.

The AI also proposed collecting all conflicts before raising an exception so that multiple conflicting filenames could be reported together.

However, despite the explicit instruction not to introduce a new exception class, Claude proposed:

```python
class MergeConflictError(Exception):
```

and:

```python
raise MergeConflictError(conflicts)
```

---

## 6.9 Critical Evaluation and Modification of AI Output

The conflict-detection algorithm proposed by Claude was useful, but its exception design was rejected.

The implementation prompt explicitly stated:

```text
Do NOT introduce MergeConflictError.
Continue using ValueError for conflicts.
```

Claude nevertheless introduced `MergeConflictError`, which directly contradicted the requirement.

There was also a functional problem with the proposed class:

```python
class MergeConflictError(Exception):
```

It inherited from `Exception`, not `ValueError`.

Therefore, tests written as:

```python
with pytest.raises(ValueError):
    repo.merge("feature")
```

would still fail.

I rejected the new exception class and retained the useful conflict-detection algorithm.

The AI-generated code:

```python
raise MergeConflictError(conflicts)
```

was changed to:

```python
conflicts.sort()

raise ValueError(
    f"Merge conflict detected in: {', '.join(conflicts)}"
)
```

This satisfied both requirements:

- the merge raises `ValueError`, and
- the error message identifies all conflicting filenames.

### Decision

**Modified**

This was an important example of why AI-generated code required human review rather than being copied directly.

---

## 6.10 Final Conflict-Detection Implementation

The existing `merge()` method was replaced with a conflict-aware version.

The implementation now obtains the commit histories of both branches:

```python
current_commits = self._commits[self.current_branch]
source_commits = self._commits[source_branch]
```

It then obtains the commit IDs on each branch:

```python
current_ids = {
    commit["id"] for commit in current_commits
}

source_ids = {
    commit["id"] for commit in source_commits
}
```

Post-divergence changes are calculated for both branches:

```python
our_changes = self._changes_since_divergence(
    current_commits,
    source_ids
)

their_changes = self._changes_since_divergence(
    source_commits,
    current_ids
)
```

Conflicts are identified using:

```python
conflicts = [
    filename
    for filename, content in their_changes.items()
    if filename in our_changes
    and our_changes[filename] != content
]
```

If conflicts exist, they are sorted and reported before any merge commit is created:

```python
if conflicts:
    conflicts.sort()

    raise ValueError(
        f"Merge conflict detected in: {', '.join(conflicts)}"
    )
```

Only when no conflicts exist is the merge commit created:

```python
self.commit(
    f"Merge branch '{source_branch}'",
    their_changes
)
```

A private helper was added:

```python
@staticmethod
def _changes_since_divergence(commits, other_ids):
    """Return accumulated changes not shared with the other branch."""
    changes = {}

    for commit in commits:
        if commit["id"] not in other_ids:
            changes.update(commit["changes"])

    return changes
```

The helper avoids duplicating the same change-accumulation logic for both branches.

---

## 6.11 Why Identical Changes Are Not Conflicts

The conflict condition checks both filename presence and content:

```python
if filename in our_changes
and our_changes[filename] != content
```

If both branches change:

```text
shared.txt
```

to:

```text
same
```

then:

```python
our_changes["shared.txt"] == their_changes["shared.txt"]
```

Therefore, no conflict is reported.

This prevents false-positive conflicts when both branches independently arrive at the same result.

---

## 6.12 State Preservation

Conflict detection happens before:

```python
self.commit(...)
```

Therefore, when a conflict is found:

- no merge commit is created,
- the current branch history remains unchanged,
- the current branch head remains unchanged,
- the source branch remains unchanged.

This follows the validate-before-mutate strategy used throughout the project.

The same testing pattern was used for invalid commits, invalid branch creation, failed checkout, failed merge, and conflicting merge operations.

---

## 6.13 GREEN Stage — Final Test Execution

After modifying the AI-generated implementation, the complete test suite was executed again:

```text
python -m pytest -v
```

The result was:

```text
53 passed in 0.15s
```

All tests from Features 1–6 passed.

### Result

**GREEN — 53 passed**

### Evidence

`screenshots/12_conflict_green.png`

This confirmed that conflict detection was added without introducing regressions into repository creation, commits, history, branching, checkout, or non-conflicting merge behaviour.

---

## 6.14 Limitation Identified During Review

The final implementation uses commit-ID comparison to approximate divergence.

It works correctly for the simplified branching scenarios covered by this project, but it is not a complete Git-style three-way merge algorithm.

For example, a file could be changed and later changed back to its original value on one branch. The current implementation still records that filename as having been changed after divergence.

The current model also does not support file deletion, so delete-versus-modify conflicts cannot be represented.

These limitations are outside the defined MiniVCS scope but are possible future improvements.

---

## 6.15 Feature 6 Reflection

Feature 6 provided one of the clearest examples of the value of both TDD and human review of AI-generated software.

The Feature 5 implementation passed all forty-three existing tests but still silently allowed one branch's version of a conflicting file to overwrite the other branch's work.

The new Feature 6 tests exposed this missing behaviour:

```text
6 failed, 47 passed
```

The AI then proposed a useful algorithm for comparing changes on both branches after divergence.

However, the AI also ignored an explicit constraint and introduced `MergeConflictError` despite being instructed to continue using `ValueError`.

Instead of copying the response directly, I reviewed and modified it. The useful conflict-detection algorithm was retained while the unnecessary exception class was removed.

After the correction:

```text
53 passed in 0.15s
```

This demonstrates that AI was used as a development assistant rather than as an unquestioned source of code.

The Feature 6 TDD cycle was:

**Requirements → AI test design → Human review → 10 selected tests → RED (6 failed, 47 passed) → AI implementation → Human review → AI error identified → Implementation modified → GREEN (53 passed)**

---

# Stage 7 — Final Testing, Coverage and Reflection

## 7.1 Final Regression Testing

After completing all six required features, I executed the complete automated test suite to verify that the final implementation did not introduce regressions into previously completed functionality.

The command used was:

```powershell
python -m pytest -v
```

The final result was:

```text
53 passed in 0.16s
```

All tests for the following features passed:

- Repository creation
- Commit and commit history
- Branching
- Checkout
- Merge
- Conflict detection

### Result

**GREEN — 53 tests passed, 0 failed**

### Evidence

`screenshots/13_final_tests.png`

---

## 7.2 Test Coverage

After confirming that the complete test suite passed, I measured statement coverage using `pytest-cov`.

The command used was:

```powershell
python -m pytest --cov=src --cov-report=term-missing
```

The result was:

```text
Name               Stmts   Miss   Cover
----------------------------------------
src\__init__.py        0      0    100%
src\mini_vcs.py       53      0    100%
----------------------------------------
TOTAL                 53      0    100%

53 passed
```

The final MiniVCS implementation achieved:

- **53 statements**
- **0 missed statements**
- **100% statement coverage**
- **53 passing automated tests**

### Evidence

`screenshots/14_coverage.png`

### Result

**100% statement coverage**

The coverage result confirms that every executable statement in the final MiniVCS source code was exercised by at least one automated test.

However, 100% statement coverage does not automatically mean that every possible behaviour or logical combination has been tested. The test suite was therefore designed using requirements, boundary conditions, invalid inputs, state-preservation checks, and regression scenarios rather than relying only on the coverage percentage.

---

## 7.3 Final Test Summary

| Feature | Tests Added | Final Status |
|---|---:|---|
| Repository Creation | 4 | Passed |
| Commit and Commit History | 8 | Passed |
| Branching | 11 | Passed |
| Checkout | 11 | Passed |
| Merge | 9 | Passed |
| Conflict Detection | 10 | Passed |
| **Total** | **53** | **53 Passed** |

The complete regression suite confirmed that adding later functionality did not break the behaviour implemented in earlier TDD cycles.

---

## 7.4 Evaluation of AI Contribution

AI was useful throughout the project for:

- generating initial requirement ideas,
- suggesting normal, boundary, invalid, and regression test cases,
- proposing minimal implementations after RED test results,
- identifying possible defects such as shared mutable branch-history lists,
- and explaining alternative implementation approaches.

However, AI output was not always aligned with the specification.

Several examples required human correction:

1. AI proposed branch deletion even though it was outside the six required features.
2. AI introduced arbitrary limits for branch names and commit messages.
3. AI repeatedly suggested a `get_files()` API that was not required.
4. AI proposed non-string `TypeError` validation without tests or requirements supporting it.
5. AI suggested expanding `history()` to accept a branch parameter mainly to make testing easier.
6. AI proposed `MergeConflictError` even after being explicitly instructed to continue using `ValueError`.
7. The Feature 5 merge implementation passed its tests but did not detect conflicting changes until Feature 6 tests exposed the missing behaviour.

These examples demonstrate why AI-generated output required critical review before being included in the software.

---

## 7.5 Strengths of AI-Assisted Development

The main strengths of AI during the project were speed and idea generation.

AI helped identify edge cases that could easily be overlooked, including:

- whitespace-only input,
- rejected operations modifying state,
- branch-history aliasing,
- identical changes on two branches,
- multiple conflicting files,
- and state preservation after failed merge operations.

AI was also useful for explaining why particular tests were valuable rather than simply generating test code.

This supported a more systematic test-design process.

---

## 7.6 Weaknesses of AI-Assisted Development

The main weakness was that AI frequently inferred behaviour from real version-control systems instead of remaining strictly within the MiniVCS specification.

This resulted in suggestions for:

- unnecessary APIs,
- additional validation,
- unsupported operations,
- and more complex designs than the current TDD stage required.

AI responses also sometimes referred to outdated assumptions from earlier stages, such as the existence of `get_files()`.

Therefore, every AI response had to be compared with:

- the specification,
- current tests,
- current source code,
- and the required feature scope.

---

## 7.7 Lessons Learned from TDD

The project demonstrated the importance of the RED → GREEN cycle.

Writing tests before implementation made the expected behaviour explicit and created evidence that implementation was driven by requirements.

The RED stages showed exactly what functionality was missing.

Examples included:

```text
Feature 2:
8 failed, 4 passed

Feature 3:
11 failed, 12 passed

Feature 4:
11 failed, 23 passed

Feature 5:
9 failed, 34 passed

Feature 6:
6 failed, 47 passed
```

After each implementation stage, the complete test suite was rerun.

This ensured that new functionality did not break earlier features.

The project also showed that a GREEN test suite is only as strong as the behaviours represented by its tests. Feature 5 passed all forty-three tests at the time but still lacked conflict detection. Feature 6 tests exposed that missing behaviour and drove the next implementation change.

---

## 7.8 Testing Improvements During Development

The test suite improved progressively throughout the project.

Early tests focused mainly on direct behaviour, such as the initial branch and empty history.

Later tests became more defensive and checked repository state before and after failed operations.

A recurring pattern developed:

**Validate first → mutate only after validation succeeds**

This was tested for:

- invalid commits,
- duplicate branch creation,
- failed checkout,
- invalid merge,
- and conflicting merge.

Regression testing also became increasingly important because every new feature was tested together with all previous features.

By the final stage, the suite contained 53 automated tests covering the complete MiniVCS implementation.

---

## 7.9 Remaining Limitations and Future Improvements

The final MiniVCS is intentionally simplified.

Current limitations include:

- Repository data exists only in memory.
- There is no disk persistence.
- There are no remote repositories.
- There is no authentication or multi-user support.
- File deletion is not represented.
- Merge operates at whole-file level rather than line level.
- Conflicts are detected but not automatically resolved.
- Commit-ID comparison provides a simplified form of divergence detection rather than a complete Git-style commit graph.
- Complex repeated merge ancestry is not fully represented.

Possible future improvements include:

- persistent repository storage,
- explicit commit-parent relationships,
- true common-ancestor calculation,
- three-way merge,
- file deletion support,
- line-level conflict detection,
- and richer repository inspection tools.

These improvements were intentionally excluded from the current assignment scope.

---

## 7.10 Final Reflection

The project showed that AI can be useful in software development when combined with structured testing and human review.

AI accelerated requirements analysis, test brainstorming, implementation suggestions, and defect identification. However, several AI outputs contained unnecessary assumptions or violated explicit constraints.

TDD provided a controlled way to evaluate these suggestions.

Instead of accepting generated code because it appeared reasonable, behaviour was defined through tests first, the implementation was executed against those tests, and previous tests were retained as regression protection.

The final project completed all six required MiniVCS features with:

- **53 automated tests**
- **53 passing tests**
- **0 failed tests**
- **100% statement coverage**

The most important lesson from the project was that AI output should be treated as a proposal that must be tested, reviewed, and justified rather than as automatically correct software.