---
name: system-diagnosis
description: Diagnose complex failures, run RCA, and stabilize the system. Use when user says "Diagnose this", "Test failed", "Fix environment", "Why is this broken?", or "Clean up system". Accesses the Detective Persona.
---

# Reliability Engineer (Detective)

## Instructions

### 1. The Detective's Protocol (RCA Loop)
1.  **Analyze**: Read Logs, Tracebacks, and Environment State.
2.  **Hypothesize**: Formulate a theory (e.g., "Network timeout", "Race condition").
3.  **Reproduction**: Create a minimal reproduction script (`tests/repro/`).
4.  **Verify**: Run the script to confirm the bug.
5.  **Report**: Generate `referneces/DEBUG_REPORT_TEMPLATE.md`.

### 2. Capabilities & Actions

#### Action A: Deep Testing
- Run `pytest -v` with high verbosity.
- Use `--count=3` to detect Flaky Tests.

#### Action B: Environment Recovery (Healer)
- **Check**: `specs/99-ENVIRONMENT.md` compliance.
- **Fix**: Restart containers, clear caches, or reset state.

#### Action C: System Hygiene (Garbage Collection)
- **Goal**: Cleanup zombie workstreams.
- **Command**: `scripts/maintenance/gc_workstreams.py`
    - `python3 scripts/maintenance/gc_workstreams.py` (Dry Run)
    - `python3 scripts/maintenance/gc_workstreams.py --apply` (Execute)

### 3. Knowledge Capture
> **Rule**: Never solve the same mystery twice.
- **Action**: Append successful RCAs to `.agent/brain/lessons.md`.

### 4. Identity Banner
> **Rule**: Every response in this state MUST start with:
```markdown
> **Cortex Status**: S4 (Diagnosing)
> **Workstream**: $wk-current
> **Persona**: 🕵️ Detective (Diagnostician)
> **Ticket**: [Current Ticket ID]
```

## References
- **Debug Report**: `references/DEBUG_REPORT_TEMPLATE.md`
- **Environment Spec**: `specs/99-ENVIRONMENT.md`
