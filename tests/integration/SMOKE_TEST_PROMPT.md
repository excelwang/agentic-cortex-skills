# ⚖️ AUTOMATED TEST MANDATE: The "Heartbeat" Workflow

**Objective**: Verify the Agentic Cortex system using the `workflow-controller` to autonomously manage a multi-turn software development lifecycle.

---

### 🟢 ENTRY POINT: ACTIVATE CONTROLLER
**Command**: `Hi Cortex, activate the workflow-controller for the web-calculator scenario`
**Requirement**:
1. The Agent must switch to the `workflow-controller` persona.
2. It must execute `python3 scripts/heartbeat.py --scenario tests/integration/scenarios/web-calculator/ --watch`.

---

### 🔄 THE CONTROL LOOP
For each stage (Design -> Implement -> Review -> Release), the following must occur:

1. **Watch**: The `workflow-controller` monitors for state changes (flags).
2. **Transition**: Upon detecting a flag (e.g., `S1_DONE`), the controller reads the next fragment from the project's `next-prompt.md`.
3. **Execution**: The Agent switches to the appropriate Worker persona (S1, S2, S3) and fulfills the mandate described in the fragment.
4. **Evidence**: Every Worker turn MUST end by running the protocol scripts (`claim_ticket`, `submit_for_review`, `release_ticket`) to set the next progress flag.

---

### 🕵️ AUDIT CRITERIA
1. **Persona Integrity**: Does the Agent correctly transition between `Observer (Heartbeat)` and `Worker (S1-S4)`?
2. **Isolation Compliance**: Is `tests/integration/outputs/calculator.html` the sole production artifact?
3. **Zero Pollution**: Are the `skills/` remains 100% project-agnostic?
4. **Protocol Score**: Final score must be 100% as verified by `LIFECYCLE_VERIFIER.py`.
