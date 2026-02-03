# Ticket 002: Skill Alignment (Self-Improvement)

> **Status**: Ready for Development  
> **Type**: Chore/Refactor  
> **Workstream**: wk-init  

## 1. Context
The system has recently updated its **Specs** (`01-ARCHITECTURE`, `10-WORKFLOW_LOOP`, `00-GLOSSARY`) to include:
1.  **Context Isolation** (`$wk-current`, `meta.json`).
2.  **Identity Banner** (S0-S4 Status display).
3.  **Session Control** ("Hi Cortex"/"Bye Cortex").

However, the individual `SKILL.md` files (the implementation of the agent's brain) may not fully reflect these specs *verbatim*, or may have slight inconsistencies (e.g., `system-diagnosis` might be missing the Banner logic).

## 2. Requirements

### A. Skill Audit & Update
For each skill in `skills/`:
- `architectural-design/SKILL.md`
- `code-implementation/SKILL.md`
- `code-review/SKILL.md`
- `system-diagnosis/SKILL.md`
- `cortex/SKILL.md`

**Action**:
1.  Verify **Identity Banner** is present and strictly follows the Spec format.
2.  Verify **$wk-current** is used instead of hardcoded paths.
3.  Verify **State Transitions** align with `10-WORKFLOW_LOOP.md`.

### B. System Diagnosis Specific
- Check `system-diagnosis/SKILL.md`: It was not recently edited. It likely uses old paths or missing the Banner. **Fix it.**

## 3. Acceptance Criteria
- [ ] All `SKILL.md` files contain the identical Identity Banner template.
- [ ] No `SKILL.md` file contains hardcoded `.agent/workstreams/` paths (except Cortex).
- [ ] `system-diagnosis` is updated to modern standards.
