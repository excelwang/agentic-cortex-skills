# 01 - Macro Architecture (The Cortex System)

> **Status**: Draft Requirements
> **Version**: 1.1 (Refined)

## 1. System Overview

The Agentic Cortex is a **Single-Agent, Multi-Persona Orchestrator**. 

Instead of spawning multiple distinct agents, it allows one capability-rich agent to **sequentially adopt different Skills**. This approach minimizes context-switching overhead while maintaining the rigorous discipline of a multi-role team.

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
