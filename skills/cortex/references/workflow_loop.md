# 10 - Workflow Loop (The Autonomous State Machine)

> **Status**: Live
> **Version**: 2.0 (Unified Protocol)

## 1. The Finite State Machine (FSM)

The workflow consists of a single Agent transitioning between different **Persona States**.

### States (Persona Modes)

| State | Active Skill | Description |
| :--- | :--- | :--- |
| **S-1: DORMANT** | None | System is offline. Waits for "Hi Cortex". |
| **S0: IDLE** | `cortex` | The "Brain" executing the **Unified Startup Protocol**. |
| **S1: DESIGNING** | `architectural-design` | **Legislator**. Modes: Spec, Gap Analysis, Reverse Eng, Interview, Reflection. |
| **S2: CODING** | `code-implementation` | **Executor**. Writing Code. |
| **S3: REVIEWING** | `code-review` | **Judge**. Auditing Diffs. |
| **S4: DIAGNOSING** | `system-diagnosis` | **Detective**. Troubleshooting. |

## 2. Transition Logic (The Unified Startup Protocol)

On "Hi Cortex", the Agent executes a strictly linear sequence:

### Step 1: Manual Override (Intent Recognition)
- **Constraint**: CHECK FIRST.
- **Trigger**: Pattern `Hi Cortex, [nickname] [scope]`.
    - **"Design/Architect"** -> **S1**
    - **"Code/Executor"** -> **S2**
    - **"Review/Judge"** -> **S3**
    - **"Diagnose/Detective"** -> **S4**
- **Action**: Load target Persona and pass `[scope]` as the initial task context.

### Step 2: Auto-Pilot (Context-Aware Routing)
- **Constraint**: Only if NO Intent detected.
- **Logic**:
    1.  **Reflections?** (Found by script) -> **S1 (Mode E)**
    2.  **Active Tickets?** (In `tickets/active/`) -> **S2**
    3.  **Backlog?** (In `tickets/backlog/`) -> Promote to Active -> **S2**
    4.  **Specs Exist?** -> **S1 (Mode B: Gap Analysis)**
    5.  **Code Only?** -> **S1 (Mode C: Reverse Eng)**
    6.  **Empty?** -> **S1 (Mode D: Interview)**

## 3. Automation Requirements

1.  **Runtime Model (Prompt-Driven)**: 
    - The "Engine" is the Agent's own context window and prompt adherence.
    - The User's role is passive unless asked for clarification.
2.  **State Persistence (Git-Native)**:
    - **Workstream ID**: Current Git Branch name.
    - **Context Storage**: Local `.agent/workstreams/{branch_name}/`.
3.  **Data Interoperability**:
    - **Communication**: Skills do NOT chat directly. They communicate via **Shared Artifacts** (`tickets/`, `specs/`, `specs-inbox.md`).
    - **Handoff**: To request work from another Persona, write a Ticket/Issue and **STOP**.

4.  **Identity Banner (Mandatory)**:
    - Every response MUST confirm: Status, Workstream, Persona, and Ticket.
