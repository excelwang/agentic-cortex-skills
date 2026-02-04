#!/usr/bin/env python3
import os
import sys
import subprocess
import shutil
from pathlib import Path

def claim_ticket(ticket_id):
    """
    Automates Git Protocol 2.A:
    1. Moves ticket from backlog/ to active/.
    2. Creates a git branch 'feat/[ticket_id]'.
    3. Initializes the workstream context directory.
    """
    project_root = Path(os.getcwd())
    backlog_dir = project_root / "tickets" / "backlog"
    active_dir = project_root / "tickets" / "active"
    workstreams_root = project_root / ".agent" / "workstreams"
    
    print(f"--- 🔒 Claiming Ticket: {ticket_id} ---")

    # 1. Find the ticket
    ticket_file = None
    for f in backlog_dir.glob(f"*{ticket_id}*"):
        ticket_file = f
        break
    
    if not ticket_file:
        print(f"[✗] Error: Ticket {ticket_id} not found in tickets/backlog/.")
        sys.exit(1)

    # 2. Git Branching
    branch_name = f"feat/{ticket_id}"
    print(f"[i] Creating branch: {branch_name}")
    try:
        subprocess.run(["git", "checkout", "-b", branch_name], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Warning: Branch might already exist or git error: {e.stderr.decode()}")
        # Proceeding as it might just be a retry

    # 3. Move Ticket (The Lock)
    active_file = active_dir / ticket_file.name
    active_dir.mkdir(parents=True, exist_ok=True)
    shutil.move(str(ticket_file), str(active_file))
    print(f"[✓] Moved to {active_dir.relative_to(project_root)}.")

    # 4. Initialize Workstream Context
    context_dir = workstreams_root / branch_name
    context_dir.mkdir(parents=True, exist_ok=True)
    
    # Create initial ticket context
    with open(context_dir / "ticket.md", "w") as f:
        f.write(f"# Workstream Context: {ticket_id}\n\nLinked Ticket: {active_file.relative_to(project_root)}\n")
    
    print(f"[✓] Initialized workstream context in {context_dir.relative_to(project_root)}.")
    
    print("\n" + "="*60)
    print("TICKET CLAIMED. ESCALATING TO EXECUTOR (S2).")
    print("="*60)
    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 claim_ticket.py <TICKET_ID>")
        sys.exit(1)
    claim_ticket(sys.argv[1])
