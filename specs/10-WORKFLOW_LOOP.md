# 10 - Workflow Loop (The Automative State Machine)

> **Status**: Draft Requirements
> **Version**: 1.1 (Refined)

## 1. The Finite State Machine (FSM)

The workflow consists of a single Agent transitioning between different **Persona States** by equipping different Skills.

### States (Persona Modes)

| State | Active Skill | Description |
| :--- | :--- | :--- |
| **S-1: DORMANT** | None | System is offline/sleeping. Waits for "Hi Cortex". |
| **S0: IDLE** | `cortex` | The "Brain" waiting for intent. |
| **S1: DESIGNING** | `architectural-design` | Agent becomes the **Legislator**. Writing Specs. |
| **S2: CODING** | `code-implementation` | Agent becomes the **Executor**. Writing Code. |
| **S3: REVIEWING** | `code-review` | Agent becomes the **Judge**. Auditing Diffs. |
| **S4: DIAGNOSING** | `system-diagnosis` | Agent becomes the **Detective**. Troubleshooting. |

## 2. Transition Logic (Persona Switching)

### T0: DORMANT -> IDLE (Wake Up)
- **Trigger**: "Hi Cortex"
- **Action**: Load `cortex/SKILL.md` (Self-Boot).

### T-Exit: ANY -> DORMANT (Shutdown)
- **Trigger**: "Bye Cortex"
- **Action**: Persist state, clear context, and stop.

### T-Reflect: IDLE -> DESIGNING (Self-Correction)
- **Trigger**: Cortex Startup (Self-Reflection) detects Spec Drift.
- **Action**: Cortex recommends switching to `architectural-design` to update `specs/` before starting new work.

### T1: IDLE -> DESIGNING (Context: Clarification)
- **Trigger**: User Intent = "New Feature" or "Ambiguity".
- **Action**: Cortex loads `architectural-design/SKILL.md`.

### T2: DESIGNING -> CODING (Context: Handoff)
- **Trigger**: Design Artifacts (`specs/*`, `.agent/tickets/*`) are finalized.
- **Action**: Cortex switches context, loads `code-implementation/SKILL.md`.

### T3: CODING -> REVIEWING (Context: Checkpoint)
- **Trigger**: "Feature Complete" or "Sub-task Complete" (logical unit).
- **Action**: Agent pauses coding, clears context, loads `code-review/SKILL.md`.

### T4: REVIEWING -> CODING (Context: Feedback)
- **Trigger**: Verdict = **FAIL**.
- **Action**: Agent re-loads `code-implementation` to apply fixes found during review.

### T5: ANY -> DIAGNOSING (Context: Self-Heal)
- **Trigger**: Tool Failure (e.g., `git merge` conflict, `pytest` crash) OR Non-deterministic Test Failure.
- **Action**:
    1. Agent suspends current Persona.
    2. Agent loads `system-diagnosis/SKILL.md`.
    3. Agent performs RCA and attempts **one** fix (e.g., `git merge --abort`).
    4. Agents returns to previous Persona.

## 3. Automation Requirements

1.  **Runtime Model (Prompt-Driven)**: 
    - This workflow does **not** require an external CLI binary.
    - The "Engine" is the Agent's own context window and prompt adherence.
    - The User's role is passive: Copy/Paste prompts if the Agent cannot auto-loop, but the Agent should treat itself as an autonomous loop where possible.
2.  **State Persistence (Git-Native)**:
    - **Workstream ID**: Current Git Branch name.
    - **Context Storage**: Local `.agent/workstream/tickets/`.
    - **Lifecycle**: Temporary context is deleted before merging to `master`.
    - **Shared Registry (Tickets)**: The `tickets/` directory on the `master` branch acts as the **Atomic Lock** for parallel development.

3.  **Atomic Ticket Locking Protocol**:
    - **Claiming (Lock)**:
        1. Switch to `master` branch.
        2. `git pull origin master`.
        3. Move ticket from `tickets/backlog/` to `tickets/active/`.
        4. `git commit -m "feat(ticket): claim TICKET_ID"` and `git push origin master`.
        5. Switch back to feature branch to start work.
    - **Completion (Release)**:
        1. Switch to `master` branch.
        2. `git pull origin master`.
        3. Move ticket from `tickets/active/` to `tickets/done/`.
        4. `git commit -m "feat(ticket): complete TICKET_ID"` and `git push origin master`.
83: 
84: 4.  **Commit Protocol (Semantic)**:
    - **Format**: `type(scope): subject` + `Body`.
    - **Requirement**: Body MUST reference the Spec File/Section being implemented.
    - **Goal**: Enable Cortex Self-Reflection to trace code changes back to Specs.
4.  **Communication Protocol (Identity Banner)**:
    - **Requirement**: Every Agent response MUST start with a standardized header block.
    - **Goal**: Immediate visual confirmation of State (S0-S4), Persona, and Active Workstream/Ticket.
    - **Format**:
      ```markdown
      > **Cortex Status**: S{n} ({State Name})
      > **Workstream**: {ID} (or None)
      > **Persona**: {Emoji} {Name} ({Role})
      > **Ticket**: {Ticket ID}
      ```
