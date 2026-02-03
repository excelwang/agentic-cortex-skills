# Agent Cortex: A Philosophical Workflow for Agentic Coding

`Agent Cortex` is a mature, production-ready framework for managing complex software development tasks using autonomous AI agents. It implements a rigorous **Separation of Powers** philosophy within the **D-C-R (Design-Code-Review) Loop**, ensuring code integrity, architectural consistency, and high reliability.

## 🏛 The Philosophy: Separation of Powers

To prevent "Agency Drift" and quality decay, this system divides the agent's capabilities into three distinct "Philosophical Personas":

1.  **Legislative (立法者) - `architectural-design`**:
    *   **Goal**: Define "What" to do.
    *   **Power**: Owns the Specs (laws) and Tickets (work orders). Only this persona can change the technical specification.
2.  **Executive (执行者) - `code-implementation`**:
    *   **Goal**: Define "How" to do it.
    *   **Power**: Implements the code based on the legislation. It must strictly abide by the Specs and cannot change them.
3.  **Judiciary (司法官) - `code-review`**:
    *   **Goal**: Verify "Is it right".
    *   **Power**: Scrutinizes the implementation against the Specs. It is the final gate before merging.

*Extended Capability:*
*   **Diagnostician (诊断医) - `system-diagnosis`**:
    *   **Goal**: Investigate "Why it failed".
    *   **Power**: Performs Root Cause Analysis (RCA) and Chaos Testing for complex integration failures.

---

## 🧠 Core Component: Cortex

The **`cortex`** skill is the central nervous system. It acts as the unified entry point for the user, dispatching requests to the appropriate persona based on intent analysis.

---

## 🛠 Skill Map

All skills follow the [Agent Skills Specification](https://agentskills.io).

| Skill | Semantic Name | Role (Persona) | Primary Output |
| :--- | :--- | :--- | :--- |
| `cortex` | Central Dispatcher | The Brain | Decision & Routing |
| `architectural-design` | Architecture Design | The Legislator | `specs/`, `tickets/` |
| `code-implementation` | Implementation | The Executor | Source Code, Unit Tests |
| `code-review` | Code Review | The Judge | Review Reports |
| `system-diagnosis` | Reliability Eng. | The Detective | RCA Reports, Repro Scripts |

---

## 📁 Library Structure

This repository is a flat collection of skills. It should be mounted at `.agent/skills/` in your project.

```text
.
├── README.md                 # Framework overview
├── architectural-design/     # Legislative Skill
├── code-implementation/      # Executive Skill
├── code-review/              # Judiciary Skill
├── system-diagnosis/         # Diagnostician Skill
└── cortex/                   # Unified Entrypoint
```

---

## 🚀 How to Integrate

Add this repository as a submodule to your project's `.agent/skills/` directory:

```bash
git submodule add git@github.com:excelwang/agentic-cortex-skills.git .agent/skills
```

Your project structure should then look like:
```text
.agent/
├── skills/ (Submodule: agent-cortex)
│   ├── architectural-design/
│   ├── code-implementation/
│   └── ...
├── rules/   (Project specific)
└── tickets/ (Project specific)
```

---

## ⚖️ License
MIT
