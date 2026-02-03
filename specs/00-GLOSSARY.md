# 00 - Glossary (Ubiquitous Language)

> **Status**: Draft Requirements
> **Version**: 1.1 (Refined)

## Core Terminology

### 1. Concepts
- **Agentic Cortex**: A comprehensive **Skill Set** that orchestrates an autonomous workflow. It is NOT a multi-agent system, but a framework for a *single* agent to switch contexts effectively.
- **Skill**: A distinct folder of instructions/tools (e.g., `architectural-design`) that the Agent "equips".
- **Persona**: The psychological mode the Agent adopts when using a Skill (e.g., "The Legislator", "The Judge").
- **Separation of Powers**: The discipline of strictly adhering to the current Persona's constraints to prevent "Agency Drift".
- **D-C-R Loop**: The "Design-Code-Review" cycle.

### 2. Artifacts
- **Spec (Specification)**: A "Law". An immutable description of *what* to do. 
- **Ticket**: A "Work Order". A mutable plan of *how* to implement the Spec.
- **Review Report**: A "Verdict".
- **Workstream**: A dedicated "runtime instance" of a Ticket. It is physically hosted in `.agent/workstreams/{branch_name}/` and contains the dynamic state (checkpoints, sub-tasks) of the work. bound to the Git Branch.
- **Context Hydration**: The process of "loading" a Workstream's local state (`ticket.md`) into the Agent's active memory.

### 3. Personas (Modes)
- **Legislator (Mode)**: Adopting `architectural-design`. Focus: Requirements & Specs.
- **Executor (Mode)**: Adopting `code-implementation`. Focus: Code & Test.
- **Judge (Mode)**: Adopting `code-review`. Focus: Verification & Diffs.
- **Detective (Mode)**: Adopting `system-diagnosis`. Focus: Root Cause Analysis.
