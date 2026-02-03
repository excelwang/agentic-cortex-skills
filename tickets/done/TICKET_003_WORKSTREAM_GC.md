# Ticket 003: Workstream Garbage Collection

> **Status**: Backlog
> **Type**: Feature/Maintenance
> **Workstream**: TBD

## 1. Context
The system uses `.agent/workstreams/{branch_name}/` to store local context.
Currently, these directories are only deleted if the Agent successfully follows the "Merge & Release" protocol in `code-implementation`.
If a branch is deleted manually (e.g., `git branch -D`), or if the Agent crashes before cleanup, 'zombie' workstreams remain on disk.

## 2. Requirements

### A. Logic
1.  **Trigger**: Cortex Startup (S0) OR Explicit Command.
2.  **Scan**: List all directories in `.agent/workstreams/`.
3.  **Check**: For each directory `dir_name`:
    -   If `dir_name` == `reflection.json`, SKIP.
    -   Check if `dir_name` exists as a local git branch.
4.  **Action**:
    -   If Branch Exists -> KEEP.
    -   If Branch Missing -> DELETE `.agent/workstreams/dir_name/`.

### B. Safety
-   Ideally, check if `ticket.md` inside has "Unsaved Context" (though this is hard to define).
-   **Simple Rule**: If the branch is gone, the context is logically orphaned and safe to delete.

## 3. Implementation
-   **Script**: Create `scripts/maintenance/gc_workstreams.py`.
-   **Skill Update**: Update `cortex/SKILL.md` or `system-diagnosis/SKILL.md` to include running this script as a maintenance step.
    -   *Recommendation*: `system-diagnosis` is the "Doctor", maybe it fits there? Or `cortex` "Pre-flight".
    -   Let's put the script in `system-diagnosis` toolkit first, or a global `scripts/` dir.

## 4. Acceptance Criteria
- [x] `scripts/maintenance/gc_workstreams.py` exists and works.
- [x] `cortex/SKILL.md` is updated to suggest running GC if workstreams look cluttered (Optional) OR `system-diagnosis` has a new Action "Clean Up".
