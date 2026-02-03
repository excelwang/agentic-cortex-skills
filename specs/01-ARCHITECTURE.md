# 01 - Macro Architecture (The Cortex System)

> **Status**: Draft Requirements
> **Version**: 1.1 (Refined)

## 1. System Overview

The Agentic Cortex is a **Single-Agent, Multi-Persona Orchestrator**. 

Instead of spawning multiple distinct agents, it allows one capability-rich agent to **sequentially adopt different Skills**. This approach minimizes context-switching overhead while maintaining the rigorous discipline of a multi-role team.

## 1.5 Context Isolation (Multi-Agent Concurrency)
While the system uses a Single Agent *conceptually* at any given moment, it supports **concurrent workstreams** for multiple instantiated Agents (e.g., in a team or parallel sessions).

- **Processor (CPU)**: The Agent instance.
- **Memory (RAM)**: The specific Workstream Directory (`.agent/workstreams/{branch_name}/`).
- **Concurrency**: Achieved by switching Git branches. Each branch carries its own isolated memory.
- **Persistence**: While the directory is git-ignored, its presence under a branch-named subfolder prevents context leakage during branch switching.

## 2. Component Diagram

```mermaid
graph TD
    User([User]) -->|Requirement| Cortex[Cortex Skill (Dispatcher)]
    
    subgraph "Single Agent Context"
        Cortex -->|Switch Hat| Leg[Legislative Persona]
        Cortex -->|Switch Hat| Exec[Executive Persona]
        Cortex -->|Switch Hat| Jud[Judiciary Persona]
        
        Cortex -.->|Sleep| Dormant[S-1: Dormant]
    end

    subgraph "Workspace (Disk)"
        Specs[(specs/)]
        Wks[(".agent/workstreams/{branch}/")]
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
