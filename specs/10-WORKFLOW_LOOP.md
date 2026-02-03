# 10 - Workflow Loop (The Automative State Machine)

> **Status**: Draft Requirements
> **Version**: 1.1 (Refined)

## 1. The Finite State Machine (FSM)

The workflow consists of a single Agent transitioning between different **Persona States** by equipping different Skills.

### States (Persona Modes)

| State | Active Skill | Description |
| :--- | :--- | :--- |
| **S0: IDLE** | `cortex` | The "Brain" waiting for intent. |
| **S1: DESIGNING** | `architectural-design` | Agent becomes the **Legislator**. Writing Specs. |
| **S2: CODING** | `code-implementation` | Agent becomes the **Executor**. Writing Code. |
| **S3: REVIEWING** | `code-review` | Agent becomes the **Judge**. Auditing Diffs. |
| **S4: DIAGNOSING** | `system-diagnosis` | Agent becomes the **Detective**. Troubleshooting. |

## 2. Transition Logic (Persona Switching)

### T1: IDLE -> DESIGNING (Context: Clarification)
- **Trigger**: User Intent = "New Feature" or "Ambiguity".
- **Action**: Cortex loads `architectural-design/SKILL.md`.

### T2: DESIGNING -> CODING (Context: Handoff)
- **Trigger**: Design Artifacts (`specs/*`, `tickets/*`) are finalized.
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
2.  **State Persistence**: 
    - `.agent/current_ticket.md` and `.agent/workstreams/` (JSON) act as the file-based database.
    - No SQLite required.
