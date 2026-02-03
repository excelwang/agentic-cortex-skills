# TODO: System Improvements

## High Priority
- [ ] **Workstream Garbage Collection**:
    - **Logic**: During Cortex Startup, scan `.agent/workstreams/` against `git branch`. Delete folders where the branch no longer exists.
    - **Safety**: Check for uncommitted changes in the workstream before deletion.

## Medium Priority
- [ ] **Tracking Branch Concurrency**:
    - **Protocol**: implement a "pull-apply-push" loop for syncing `tickets/` on the `tracking` branch to handle simultaneous updates.
