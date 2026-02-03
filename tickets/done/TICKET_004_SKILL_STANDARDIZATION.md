# Ticket 004: Standardize Skill Library

> **Status**: Backlog
> **Type**: Architecture/Refactoring
> **Workstream**: TBD

## 1. Context
We have a set of skills in `skills/` (`architectural-design`, `code-implementation`, `code-review`, `cortex`, `system-diagnosis`).
We recently adopted a standard guide for writing skills: `specs/98-how-to-write-skill.md`.
We need to ensure all existing skills and any new ones created with `skill-creator` (if we build it) adhere to this standard.

## 2. Requirements

### A. Create `skill-creator` Skill
- **Goal**: Implement the "Meta-Skill" described in the guide.
- **Function**: Interactive guide to build new skills.
- **Location**: `skills/skill-creator/`

### B. Audit & Refactor Existing Skills
- **Scope**:
    - `cortex`
    - `architectural-design`
    - `code-implementation`
    - `code-review`
    - `system-diagnosis`
- **Checklist**:
    1.  [ ] **Frontmatter**: `name`, `description` (actionable + specific triggers).
    2.  [ ] **Structure**: `SKILL.md` (instructions), `scripts/`, `references/`.
    3.  [ ] **Progressive Disclosure**: Detailed docs moved to `references/`.
    4.  [ ] **Examples**: "User says X -> Action Y".

## 3. Implementation Plan

1.  **Phase 1: Meta-Skill**
    - Build `skills/skill-creator/SKILL.md`.
    - It should know how to read `specs/98-how-to-write-skill.md` as its source of truth.

2.  **Phase 2: Standardization Sprint**
    - Iterate through each existing skill.
    - Update Frontmatter to be strictly `kebab-case` compliant and rich in triggers.
    - Move long sections (like "Communication Protocol") to shared references if possible, or keep them compact.

## 4. Acceptance Criteria
- [x] `skills/skill-creator` exists and can "scaffold" a new skill.
- [x] ALL `skills/*/SKILL.md` pass the "Structure Check" from `specs/98-how-to-write-skill.md`.
