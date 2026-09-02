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
- A commit-message length limit was also introduced without sufficient justification.
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
> Specifically review the functional requirements, non-functional requirements, assumptions, constraints, expected behaviours, boundary conditions, and invalid input scenarios.
>
> The six main features are only commit, checkout, branching, merge, conflict detection, and commit history.
>
> Do not add new major features or generate implementation code.

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
> Keep the scope limited to commit, checkout, branching, merge, conflict detection, and commit history.
>
> Remove branch deletion and unnecessary/invented requirements.
>
> Include functional requirements, non-functional requirements, assumptions, constraints, expected behaviours, boundary conditions, and invalid input scenarios.
>
> Keep it concise and suitable for a university assignment. Do not include implementation code.

## 3.3 Final Result

The resulting specification was reviewed again before being saved as `SPECIFICATION.md`.

The final project is limited to six features:

1. Commit
2. Checkout
3. Branching
4. Merge
5. Conflict detection
6. Commit history

The final specification also establishes that application and test code remain separate, the repository is in-memory only, files use names and string content, merging is whole-file rather than line-level, conflicts are reported rather than automatically resolved, and tests are written before implementation for each feature.

## 3.4 Overall Evaluation

AI was effective at quickly identifying possible requirements, edge cases, and invalid-input scenarios. However, it also tended to expand familiar software concepts beyond the requested scope. Branch deletion was the clearest example because it is common in real version-control systems but was not required for MiniVCS.

This stage demonstrated why AI output should not be accepted automatically. Reviewing and modifying the output kept the project smaller, clearer, and aligned with the assignment.

---

# Stage 4 — Test Design

**Status:** To be completed during development.

For each feature, record the feature, AI prompt, proposed tests, accepted/modified/rejected tests, reasons for changes, final tests, initial failing result (RED), and evidence.

---

# Stage 5 — AI-Assisted Implementation

**Status:** To be completed during development.

For each feature, record the failing tests supplied to AI, implementation prompt, AI response summary, accepted/modified/rejected code, manual changes, passing result (GREEN), and evidence.

---

# Stage 6 — Evaluation and Improvement of AI Output

**Status:** To be completed during development.

Document examples where AI-generated code or tests contained incorrect assumptions, defects, missing cases, or maintainability issues. Record regression tests and before/after examples where appropriate.

---

# Stage 7 — Final Testing and Reflection

**Status:** To be completed after all features are implemented.

Record the complete automated test result, coverage result, GitHub evidence, areas where AI performed well or poorly, TDD lessons, testing improvements, and possible future improvements.

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
