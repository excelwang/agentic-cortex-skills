# Skill Library Sanitization Walkthrough

This walkthrough details the changes made to the `agentic-cortex-skills` library to remove project-specific references and ensure it remains a generic framework.

## Changes Overview

The following skills and templates were updated:
- `architectural-design/SKILL.md`
- `architectural-design/references/TICKET_TEMPLATE.md`
- `code-implementation/SKILL.md`
- `code-review/SKILL.md`
- `code-review/references/REVIEW_REPORT_TEMPLATE.md`
- `system-diagnosis/SKILL.md`

## Detailed Changes

### 1. Architectural Design
- **SKILL.md**: Replaced specific agreement test path `it/specs/...` with `tests/contracts/...`.
- **TICKET_TEMPLATE.md**: Removed references to "Pusher" and `uv run`. Generalized `it/specs/consistency/` to `tests/contracts/`.

### 2. Code Implementation
- **SKILL.md**: Generalized `it/` directory references to `tests/`.

### 3. Code Review
- **SKILL.md**: Updated agreement test path check to `tests/contracts/`.
- **REVIEW_REPORT_TEMPLATE.md**: Generalized example paths (`tests/integration/` instead of `it/consistency/`).

### 4. System Diagnosis
- **SKILL.md**:
    - Replaced `uv run pytest` with generic `pytest` or `[Test Command]`.
    - Removed `docker logs` specific example.
    - Generalized `it/consistency/` to `tests/integration/`.

## Verification Results

### Manual Check
- All files were successfully updated.
- No "Pusher" or `uv run` references remain in the target files.
- Path conventions are now consistent (`tests/contracts`, `tests/integration`).

## Repository Restructuring
- **Action**: Moved all skill directories (`architectural-design`, `code-implementation`, `code-review`, `system-diagnosis`, `cortex`) into a new `skills/` subdirectory.
- **Documentation**: Updated `README.md` to reflect the new hierarchical structure.
- **Cleanup**: Removed `EXTENDING_CORTEX.md` as requested.

## Project Quality Improvements
- **Documentation**: Created `CONTRIBUTING.md` and `LICENSE` (MIT).
- **Configuration**: Added `.gitignore` to exclude temporary files and personal configs.
- **Index**: Updated `README.md` to reference the new directory structure and contribution guide.

## Cortex "Meta-Maintenance"
Acting as the Cortex (System Diagnosis/Self-Correction), I identified and fixed two defects in the skill definitions:
1.  **Duplicate Header**: Removed a redundant "Task Template" header in `architectural-design/SKILL.md`.
2.  **Template Extraction**: Extracted the hardcoded `current_ticket` template from `code-implementation/SKILL.md` into a reusable reference file `references/CURRENT_TICKET_TEMPLATE.md`.
3.  **Cross-Reference Integrity**: Fixed a numbering gap in `code-review/SKILL.md` and simultaneously sanitized a lingering project-specific path (`it/specs/` -> `tests/contracts/`) that had evaded previous checks.
4.  **Documentation Accuracy**: Updated `README.md` to accurately reflect the new nested directory structure (`.agent/skills/skills/...`).

## Architectural Design Session
Facilitated a Legislative Session to define the "Constitution" of the Workflow.
- **Outcome**: Created 3 fundamental specs in `specs/`.
    - `00-GLOSSARY.md`: Defined "One Agent, Many Skills" model.
    - `01-ARCHITECTURE.md`: Defined the "Persona Switching" logic.
    - `10-WORKFLOW_LOOP.md`: Defined the **Self-Healing Automative State Machine** (A-B-JSON model).

## Architectural Design Skill Refinement
- **Reverse Engineering**: Added "Phase 0: Discovery" to `skills/architectural-design/SKILL.md`. This instructs the Architect to reverse-engineer `specs/` (01, 10, then 00) from existing code if the directory is missing.
- **Rule of Law**: Established the "Glossary Supremacy" rule. Once `00-GLOSSARY.md` is generated (even if last), it becomes the absolute Source of Truth, making conflicting code "Legacy Debt".

## Latest Bug Fixes
1.  **Ticket Path Correction**: Moved `tickets/` to `.agent/tickets/` to reduce root clutter and updated all references in `SKILL.md` and `README.md`.
2.  **Workstream Initialization**: Migrated the "Workstream Selection/Creation" logic from `code-implementation` to `cortex`.
    - **Cortex**: Now handles "Step 0: Context Hydration" (Resume vs. New) at entry (State S0).
    - **Code Implementation**: Now assumes context is already hydrated and proceeds directly to execution.
3.  **UI Standardization**: Enforced a mandatory "Identity Banner" for all skills (Cortex, Architect, Executor, Judge, Detective) to clearly display current State (S0-S4), Workstream, and Active Ticket at the start of every response.

4.  **Context Isolation**: Removed global `.agent/current_ticket.md`. Each Workstream now maintains its own independent context file at `.agent/workstreams/wk-{id}/context.md` (Flat Structure) to support multi-agent concurrency.
5.  **Dynamic Workstream Summaries**: Introduced `meta.json` with a 15-char limit `summary` field.
    - **Cortex**: Displays "ID + Summary" during workstream selection.
    - **Code Review**: Updates description after every review (e.g., "API Ready", "Refactor Done").
6.  **Variable Standard**: Defined `$wk-current` as the standard variable for the active workstream directory (e.g., `.agent/workstreams/wk-123/`).
    - **Cortex**: Resolves `$wk-current` at startup.
    - **All Other Skills**: Use `$wk-current/context.md` and `$wk-current/meta.json` abstractly, decoupling them from the specific directory structure.
7.  **Specification Backfill**: Updated `specs/` to formalize these recent architectural changes.
    - `00-GLOSSARY.md`: Added definitions for **Workstream**, **Context Hydration**, and **$wk-current**.
    - `01-ARCHITECTURE.md`: Added **Context Isolation** section (CPU vs RAM analogy).
    - `10-WORKFLOW_LOOP.md`: Added **Identity Banner** protocol requirements.
8.  **Session Control**: Implemented "Hi/Bye" protocol.
    - **Hi Cortex**: Wakes system (S-1 Dormant -> S0 Idle).
    - **Bye Cortex**: Shuts down system, saves context, and exits Agent mode.
9.  **Self-Correction Plan**: Created `TICKET_002_SKILL_ALIGNMENT` to systematically update all `SKILL.md` files to align with these new Specs (fixing any drift or missing banners).
10. **Git-Based Workstreams**: Redesigned workstream identity to leverage Git Branches.
    - **ID**: Workstream ID = Git Branch Name.
    - **Path**: Fixed at `.agent/workstream/` (per-branch unique context).
    - **Cleanup**: Ephemeral context is deleted before merging to `master` to prevent conflicts.
11. **Startup Self-Reflection**: Enhanced "Hi Cortex" to include a Spec Drift Check.
    - **Logic**: Scans `git log --merges` on startup.
    - **Prompt**: If recent merges found, asks User if Specs need updating, creating a virtuous cycle of "Code -> Merge -> Reflect -> Spec Update".
