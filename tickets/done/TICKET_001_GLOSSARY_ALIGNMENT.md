# Ticket 1: Glossary Alignment Refactor

> **Status**: Ready for Dev
> **Type**: Refactor (Tech Debt)
> **Owner**: `code-implementation`

## 1. Goal
Refactor existing `SKILL.md` files to align with the new **"Single Agent, Multi-Persona"** terminology defined in `specs/00-GLOSSARY.md` and the **State Machine** in `specs/10-WORKFLOW_LOOP.md`.

## 2. Scope
- [ ] `skills/cortex/SKILL.md`: Update intent analysis to reference the new States (S0-S4).
- [ ] `skills/system-diagnosis/SKILL.md`: Add the "Self-Healing" capabilities trigger.
- [ ] `skills/code-implementation/SKILL.md`: Ensure it references the `spec/` immutability rule.

## 3. References
- `specs/00-GLOSSARY.md` (The Law)
- `specs/10-WORKFLOW_LOOP.md` (The Logic)

## 4. Acceptance Criteria
- [ ] All `SKILL.md` files use "Persona" instead of "Agent".
- [ ] `cortex` explicitly mentions the S0-S4 States.
- [ ] No "Multi-Agent" references remain.
