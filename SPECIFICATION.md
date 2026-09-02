# MiniVCS — Software Specification

A simplified, in-memory version control system.

**Scope.** Six features only: commit, checkout, branching, merge, conflict detection, commit history. No persistence to disk, no remote repositories, no multi-user support.

---

## 1. Functional Requirements

| ID | Requirement |
|---|---|
| FR1 | The system shall create a repository containing a default branch named `main`. |
| FR2 | The system shall track a single current branch at all times. |
| FR3 | The system shall create a commit consisting of a message and a set of file changes. |
| FR4 | The system shall assign every commit a unique identifier. |
| FR5 | The system shall reject a commit whose message is empty or whitespace only. |
| FR6 | The system shall record each commit against the branch that is current at the time. |
| FR7 | The system shall return the commit history of the current branch in chronological order. |
| FR8 | The system shall create a new branch from the state of the current branch. |
| FR9 | The system shall reject a branch name that is empty, whitespace only, or already in use. |
| FR10 | The system shall switch the current branch to a named existing branch. |
| FR11 | The system shall reject a checkout of a branch that does not exist. |
| FR12 | The system shall preserve each branch's own file state and history across checkouts. |
| FR13 | The system shall merge a named branch into the current branch. |
| FR14 | The system shall reject a merge of a branch that does not exist. |
| FR15 | The system shall reject a merge of a branch into itself. |
| FR16 | The system shall detect a conflict when a file has been changed to different content in both branches since they diverged, and shall report the conflicting file names. |
| FR17 | The system shall leave both branches unchanged when a merge is rejected because of a conflict. |

---

## 2. Non-Functional Requirements

| ID | Requirement |
|---|---|
| NFR1 | The system shall be implemented in Python 3. |
| NFR2 | Application code and test code shall reside in separate files. |
| NFR3 | The system shall raise descriptive exceptions rather than failing silently or returning error codes. |
| NFR4 | The system shall be organised into small functions and methods that can be tested independently. |
| NFR5 | The automated test suite shall be executable using a single pytest command. |
| NFR6 | The system shall depend only on the Python standard library and pytest. |

---

## 3. Assumptions

- A file is a name/content pair; content is a plain string.
- Repository state exists only in memory for the lifetime of the process. Nothing is written to disk.
- A single user operates a single local repository. There are no remotes, no push or pull, and no authentication.
- Merging is whole-file. A file is either taken wholly from one branch or flagged as a conflict; no line-level merging is attempted. This is a deliberate simplification, adopted so that conflict detection can be specified and tested precisely.
- A conflict is reported rather than resolved. The system does not write conflict markers or offer resolution.
- Commits are immutable once created. There is no amend, revert, or delete.

---

## 4. Constraints

- The application must be developed using an AI-assisted Test-Driven Development workflow, with tests written before implementation for every feature.
- All AI interactions must be recorded as they occur.
- The project must be version-controlled in a GitHub repository with incremental commits.
- Scope is limited to the six listed features. No additional feature may be added.
- The work must be completable within the assignment period by one student.

---

## 5. Expected System Behaviours

| # | Behaviour |
|---|---|
| EB1 | A new repository has `main` as its only branch and as the current branch. |
| EB2 | A new repository has an empty commit history. |
| EB3 | A commit with a valid message is stored and appears in the history. |
| EB4 | Two commits made in sequence receive different identifiers. |
| EB5 | A commit with an empty or whitespace-only message is refused and the history is unchanged. |
| EB6 | History is returned oldest first. |
| EB7 | A new branch is created and appears alongside the existing branches. |
| EB8 | A branch created from `main` starts with the same files and history as `main`. |
| EB9 | Creating a branch with a name already in use is refused and the existing branch is untouched. |
| EB10 | Checking out an existing branch changes the current branch. |
| EB11 | Checking out a branch that does not exist is refused and the current branch is unchanged. |
| EB12 | Commits made on one branch do not appear in the history of another. |
| EB13 | Merging a branch that changed only files the current branch did not touch succeeds, and those files appear in the current branch. |
| EB14 | Merging a branch that changed a file to different content than the current branch is reported as a conflict naming that file. |
| EB15 | A branch that changed a file to the same content as the current branch merges without conflict. |
| EB16 | A merge rejected for conflict leaves the current branch's files exactly as they were. |
| EB17 | The source branch is unchanged by a successful merge. |

---

## 6. Boundary Conditions

| Input | Boundary |
|---|---|
| Commit message | Single character |
| Commit message | Long message (accepted; no maximum length is imposed) |
| Commit message | Leading and trailing whitespace around real text |
| Branch name | Single character |
| Commit changes | No files changed (empty change set) |
| Commit changes | One file changed |
| History | Zero commits |
| History | Exactly one commit |
| Branches | Only `main` exists |
| Merge | Source branch has no commits since divergence |
| Merge | Every changed file conflicts |
| Merge | Exactly one file conflicts among several changed |

---

## 7. Invalid Input Scenarios

| Call | Expected result |
|---|---|
| `commit("")` | Error — message required |
| `commit("   ")` | Error — message required |
| `create_branch("")` | Error — name required |
| `create_branch("   ")` | Error — name required |
| `create_branch("main")` | Error — name already exists |
| `checkout("nonexistent")` | Error — no such branch |
| `merge("nonexistent")` | Error — no such branch |
| `merge(current_branch)` | Error — cannot merge a branch into itself |

All invalid operations raise an exception carrying a message that identifies the problem. None fail silently.
