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

# Stage 5 — Remaining Feature Development

**Status:** In progress.

The same AI-assisted TDD process will be followed for the remaining features:

- Feature 3 — Branching
- Feature 4 — Checkout
- Feature 5 — Merge
- Feature 6 — Conflict Detection

For each feature, this log will record the exact AI prompt, AI response summary, my evaluation, accepted/modified/rejected decisions, RED test result, implementation review, GREEN result, and evidence.

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
