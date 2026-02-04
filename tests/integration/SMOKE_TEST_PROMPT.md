# ⚖️ FAIR TEST MANDATE: The "Pure Intent" Workflow

**Objective**: Verify the Agentic Cortex system by building a functional Web Calculator using ONLY standardized user-level commands.

---

### 🟢 TURN 1: DESIGN
**Command**: `Hi Cortex, S1 design a web calculator`
**Verification**: 
- Does the Architect (S1) correctly identify Mode A (Legislation)?
- Does it create `specs/50-CALCULATOR.md` and a ticket in `backlog/`?
- Does it run `ready_check.py` without being told?

### 🔵 TURN 2: IMPLEMENT
**Command**: `Hi Cortex, S2 code the calculator`
**Verification**:
- Does the Executor (S2) run `ready_check.py` and `claim_ticket.py`?
- Does it implement `calculator.html` correctly?
- Does it run `submit_for_review.py` autonomously before finishing?

### 🔴 TURN 3: JUDGE
**Command**: `Hi Cortex, S3 judge the calculator`
**Verification**:
- Does the Judge (S3) audit the diff and requirements?
- Does it provide a verdict (PASS/FAIL)?

### ⚪ TURN 4: RELEASE
**Command**: `Hi Cortex, finish the task`
**Verification**:
- Does Cortex (S0) correctly route to S2/S3 for release?
- Is `release_ticket.py` executed?
- Is the environment cleaned?

---

### 🕵️ AUDIT CRITERIA
1. **No Hallucination**: The Agent must not reference internal script names unless they are actually running them.
2. **Protocol Adherence**: The `Identity Banner` must be present and accurate in every turn.
3. **Black-Box Success**: Artifacts must exist and be functional at the end of the chain.
