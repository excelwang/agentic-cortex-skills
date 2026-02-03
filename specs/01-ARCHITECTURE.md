# 01 - Macro Architecture (The Cortex System)

> **Status**: Draft Requirements
> **Version**: 1.1 (Refined)

## 1. System Overview

The Agentic Cortex is a **Single-Agent, Multi-Persona Orchestrator**. 

Instead of spawning multiple distinct agents, it allows one capability-rich agent to **sequentially adopt different Skills**. This approach minimizes context-switching overhead while maintaining the rigorous discipline of a multi-role team.

## 1.5 Context Isolation (Multi-Agent Concurrency)
While the system uses a Single Agent *conceptually* at any given moment, it supports **concurrent workstreams** for multiple instantiated Agents (e.g., in a team or parallel sessions).

- **Processor (CPU)**: The Agent instance.
- **Memory (RAM)**: The specific Workstream Directory (`.agent/workstreams/wk-{id}/`).
- **Variable**: All Skills (except Cortex) use the relative variable `$wk-current` to reference their memory.
- **Global Awareness (Cortex)**: Only Cortex is aware of the absolute paths to efficiently route the Agent to the correct memory block.

## 2. Component Diagram

```mermaid
graph TD
    User([User]) -->|Requirement| Cortex[Cortex Skill (Dispatcher)]
    
    subgraph "Single Agent Context"
        Cortex -->|Switch Hat| Leg[Legislative Persona]
        Cortex -->|Switch Hat| Exec[Executive Persona]
        Cortex -->|Switch Hat| Jud[Judiciary Persona]
    end

    Leg -->|Use Skill| Skill1[architectural-design]
    Exec -->|Use Skill| Skill2[code-implementation]
    Jud -->|Use Skill| Skill3[code-review]

    Skill1 -->|Write| Specs[(specs/)]
    Skill2 -->|Read| Specs
    Skill3 -->|Enforce| Specs
```

## 3. Data Flow Guarantees

1.  **Persona Discipline**: 
    - When holding the `code-implementation` Skill, the Agent **must not** modify `specs/`.
    - To change Specs, the Agent must explicitly **switch** to the `architectural-design` Skill.
2.  **Gatekeeping**:
    - The Agent cannot self-merge without enabling the `code-review` Skill and generating a PASS verdict.
