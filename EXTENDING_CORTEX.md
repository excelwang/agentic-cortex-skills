# The Zen of Cortex: Extension through Legislation

The `Agentic Cortex` framework adheres to the principle of **Self-Contained Skills**. Customization is not achieved by modifying the "Brain's" reasoning code, but by defining the "World" it operates in.

## 1. The Separation
- **Skill (Static Reasoning)**: "Follow instructions and verify outcomes." (Immutable)
- **Spec/Ticket (Dynamic Context)**: "Here are the project-specific rules and steps." (Mutable)

## 2. Customization via Legislation (Example Case)

To make a generic skill behave like a specialized expert, the customization occurs at the **Planning Phase**:

### Feature A: Specialized Review Criteria
Instead of adding a "Project-Specific Mode" to `code-review`, the **Solution Architect** simply writes a high-quality Technical Specification.
- **Generic Spec**: "The system must be consistent."
- **Project Spec**: "The system must adhere to [Specific Protocol X]. All updates must [Action Y]."
*The `code-review` skill, being self-contained and logical, will correctly catch violations simply by following the Spec.*

### Feature B: Specialized Diagnostic Procedures
Instead of hardcoding diagnostic steps into `system-diagnosis`, the **Ticket** defines the procedure.
- **Generic Ticket**: "Debug the failure."
- **Project Ticket**: "1. Run [Tool Z]. 2. Analyze the sequence of [Event A]. 3. Report the result."

## 3. Creating New Capabilities (Satellite Skills)
If the required logic is so unique that it cannot be described in a Spec (e.g., calling a specific proprietary tool with complex parameters), create a **Satellite Skill**.

- **Structure**: Place the new folder (e.g., `project-special-diag/`) in `.agent/skills/`.
- **Discovery**: The `cortex` dispatcher will automatically find it.
- **Usage**: The Architect can now write Tickets that say "Trigger the `project-special-diag` skill to analyze this crash."

## 4. Key Takeaway
**Do not change the Skills. Change the Specs and the Tickets.** This keeps the core logic pure, testable, and upstream-compatible while allowing infinite project-level flexibility.

