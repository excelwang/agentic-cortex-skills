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

### 3. Personas (Modes)
- **Legislator (Mode)**: Adopting `architectural-design`. Focus: Requirements & Specs.
- **Executor (Mode)**: Adopting `code-implementation`. Focus: Code & Test.
- **Judge (Mode)**: Adopting `code-review`. Focus: Verification & Diffs.
