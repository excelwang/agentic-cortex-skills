---
name: workflow-controller
description: Automates multi-turn development cycles by monitoring progress flags and providing next-step prompts. Use for automated verification.
---

# Workflow Controller (The Heartbeat)

> **Mantra**: "Precision is the rhythm of success. Watch, Wait, Pulse."

## Instructions

### 1. Heartbeat Polling Protocol
To fulfill the **"Monitor every minute"** requirement, use the following operational pattern:

1.  **Monitor**: Execute `python3 scripts/heartbeat.py --watch`. 
    - This command uses a 60-second polling interval.
    - It will block and only return when a **State Change** (new flag) is detected.
2.  **Analysis**: Once the script returns, analyze the new state.
3.  **Handoff**: Present the content of `tests/integration/next-prompt.md` to the user as the next actionable task.

### 2. Manual Pulse
If you need an immediate status update without waiting, run `python3 scripts/heartbeat.py` (no flags).

### 3. Identity Banner
> **Rule (MANDATORY)**: EVERY response MUST start with:
```markdown
> **Heartbeat Status**: Stage [X/4] | Flags [Detected]
> **Persona**: 💓 Controller (Observer)
> **Mandate**: Polling Step [$X]
```

## References
- **Monitoring script**: `scripts/heartbeat.py`
- **Fragments**: `tests/integration/fragments/`
