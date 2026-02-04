# 💨 SMOKE TEST MANDATE: Project Health-Check

**Copy and Paste the section below to start the autonomous verification loop.**

---

### START OF PROMPT ###
You are the **Cortex System**. I want to verify the entire "Inheritance" (Integration) workflow. Follow this plan strictly.

**Goal**: Implement a "System Version" footer in `README.md`.

**Step 1: Architect (Design)**
- Command: **Hi Cortex, design a version footer for README**
- Requirement: Run `scripts/doctor.py` and `scripts/status.py`. Identify as S1.
- Output: Create `specs/VERSION_FOOTER.md` and a ticket in `tickets/backlog/`.

**Step 2: Executor (Code)**
- Command: **Hi Cortex, code the version footer**
- Requirement: Run `ready_check.py` and `claim_ticket.py`. Identify as S2.
- Action: Add `VERSION: 0.1.0-alpha` to `README.md`.
- Handoff: Run `submit_for_review.py`.

**Step 3: Judge (Review)**
- Command: **Hi Cortex, judge the footer implementation**
- Requirement: Run `ready_check.py`. Identify as S3.
- Action: PASS the review. Instruct the release.

**Step 4: Cleanup**
- Instruction: Run `release_ticket.py` and `status.py`.
- Final State: Show that the ticket is in `done/` and the system is IDLE.

**Constraint**: You MUST run the relevant scripts for every step and report their `[REPORT]` output.
### END OF PROMPT ###
