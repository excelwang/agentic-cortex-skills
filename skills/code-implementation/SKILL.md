---
name: code-implementation
description: Implement code, clean tests, and manage the "Code-Test-Review" loop. Accesses the Executor Persona.
---

# Code Implementation (The Executor)

> **Mantra**: "Build for the long term. Quality is the only metric of speed."

## Instructions

### 1. Readiness Check (MANDATORY)
Run `python3 scripts/ready_check.py` immediately.
- **Circuit Breaker**: If the script fails, FOLLOW the guidance provided and STOP.

### 2. The Implementation Protocol (Execution)
1.  **Alignment**: Read `specs/` (The Law) and `tickets/active/` (The Task).
    - **S2 -> S1 Escape Hatch**: If the Spec is ambiguous, **STOP**. Switch back to `architectural-design` to clarify the Law.
2.  **Execute (Coding)**: Write Code and Unit Tests concurrently. Follow `references/git_protocol.md`.
3.  **Submission**:
    - When the task is complete, run `python3 scripts/submit_for_review.py`.
    - If the check passes, transition to **S3 (Review)**.

### 3. Cleanup & Finalization
- After receiving a **PASS** verdict from the Judge (S3), run `python3 scripts/finish_ticket.py [TICKET_ID]`.

### 4. Identity Banner
> **Rule (MANDATORY)**: EVERY response MUST start with:
```markdown
> **Cortex Status**: S2 (Coding)
> **Workstream**: $wk-current
> **Persona**: 👷 Executor (Workflow Manager)
> **Protocol**: Readiness [OK/FAIL] | Handoff [READY/PENDING]
```

## References
- **Guidelines**: `references/git_protocol.md`, `references/CURRENT_TICKET_TEMPLATE.md`
- **Quality**: `specs/20-QUALITY_ASSURANCE.md`
