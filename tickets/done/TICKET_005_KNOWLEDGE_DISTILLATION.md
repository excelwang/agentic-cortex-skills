> **Status**: Done
> **Type**: Tooling/Feature
> **Workstream**: TBD

## 1. Context
Both `code-review` (Judge) and `system-diagnosis` (Detective) have a mandate to capture "Lessons" into `.agent/brain/lessons.md`.
Currently, this is a manual editing process, which risks:
1.  Formatting inconsistencies.
2.  Overwrite errors (race conditions).
3.  Lack of structure (metadata, tags).

## 2. Requirements

### A. The Tool (`scripts/record_lesson.py`)
Create a Python script that accepts:
-   `--type`: "Mistake", "Pattern", "Anti-Pattern".
-   `--context`: The Ticket ID or File ID.
-   `--content`: The lesson text.
-   `--author`: The Persona (Judge/Detective).

**Behavior**:
-   Appends a structured entry to `.agent/brain/lessons.md`.
-   Uses a lock or safe-append strategy.

### B. Skill Integration
Update `skills/`:
-   `code-review/SKILL.md`: Replace manual "Append" instruction with `python3 scripts/record_lesson.py ...`.
-   `system-diagnosis/SKILL.md`: Same interaction.

## 3. Acceptance Criteria
- [x] `scripts/record_lesson.py` exists and works.
- [x] `lessons.md` has a consistent schema clearly defined (or enforced by the script).
- [x] Skills are updated to use the tool.
