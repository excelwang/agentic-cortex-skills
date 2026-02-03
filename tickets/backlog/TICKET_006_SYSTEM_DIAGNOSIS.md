# Ticket 006: System Diagnosis Modernization

> **Status**: Backlog
> **Type**: Refactor
> **Workstream**: TBD

## 1. Context
`skills/system-diagnosis/SKILL.md` (The Detective) is currently imperative and "command-heavy".
It duplicates test running logic found in `code-implementation` and defines "Self-Healing" steps that might violate the new `30-GIT_PROTOCOL.md` (e.g., ad-hoc merges).

## 2. Requirements

### A. Skill Refactor
-   **Remove**: Hardcoded `git merge --abort` etc. Replace with "Follow safe recovery protocols" or reference Git Spec.
-   **Remove**: Specific test command strings (unless unique to diagnosis).
-   **Add**: Explicit reference to `specs/20-QUALITY_ASSURANCE.md` for "Contract Test Integrity".
-   **Add**: Integration with `scripts/record_lesson.py` (Dependency on Ticket 005).

### B. New Spec? (Optional)
-   Consider extracting "RCA Loop" and "Chaos Testing" into `specs/40-DIAGNOSIS_PROTOCOL.md`.
    -   *Decision*: Let's keep it in the Skill for now, but clean up the "Self-Healing" section to be less "cowboy".

## 3. Acceptance Criteria
- [ ] `skills/system-diagnosis/SKILL.md` is aligned with `20-QUALITY_ASSURANCE.md`.
- [ ] Safe Git operations are enforced.
- [ ] "Actions" section is streamlined.
