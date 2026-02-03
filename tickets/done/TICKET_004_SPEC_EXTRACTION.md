# Ticket 004: Spec Extraction

> **Status**: Active
> **Type**: Refactor/Documentation
> **Workstream**: wk-spec-extraction

## 1. Context
Critical system protocols (Git workflows, Review criteria) are currently buried within `skills/` definitions. These should be "System Laws" (Specs), not just "Persona Instructions". This duplication creates maintenance risks and violates the "Single Source of Truth" principle.

## 2. Requirements

### A. New Specs
1.  **`specs/30-GIT_PROTOCOL.md`**:
    -   Define Atomic Ticket Locking (Claim/Release).
    -   Define Commit Message Format (Conventional + Spec Reference).
    -   Define Workstream Lifecycle (Creation/Deletion).
2.  **`specs/20-QUALITY_ASSURANCE.md`**:
    -   Define Review Modes (Feature, Refactor, Test).
    -   Define Core Quality Checklist.
    -   Define Test Strategy (Contract vs Unit).

### B. Refactoring (Pruning)
1.  **`specs/10-WORKFLOW_LOOP.md`**:
    -   Remove Section 4 (Git/Commit Protocol).
    -   Replace with reference to `30-GIT_PROTOCOL.md`.
2.  **`skills/code-implementation/SKILL.md`**:
    -   Remove detailed Git commands.
    -   Refer to `specs/30-GIT_PROTOCOL.md`.
3.  **`skills/code-review/SKILL.md`**:
    -   Remove detailed Checklists/Modes.
    -   Refer to `specs/20-QUALITY_ASSURANCE.md`.

## 3. Acceptance Criteria
- [ ] `specs/30-GIT_PROTOCOL.md` exists and covers all Git logic.
- [ ] `specs/20-QUALITY_ASSURANCE.md` exists and covers all Review logic.
- [ ] `specs/10-WORKFLOW_LOOP.md` no longer duplicates Git rules.
- [ ] Skills are significantly shorter and point to Specs.
