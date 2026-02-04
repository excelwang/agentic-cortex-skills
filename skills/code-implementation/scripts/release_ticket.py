#!/usr/bin/env python3
import os
import sys
import subprocess
import shutil
from pathlib import Path

def release_ticket(ticket_id):
    """
    Automates Git Protocol 2.B:
    1. Moves ticket from active/ to done/.
    2. Suggests branch cleanup.
    """
    project_root = Path(os.getcwd())
    active_dir = project_root / "tickets" / "active"
    done_dir = project_root / "tickets" / "done"
    workstreams_root = project_root / ".agent" / "workstreams"
    
    print(f"--- 🔓 Releasing Ticket: {ticket_id} ---")

    # 1. Find the ticket
    ticket_file = None
    for f in active_dir.glob(f"*{ticket_id}*"):
        ticket_file = f
        break
    
    if not ticket_file:
        print(f"[✗] Error: Ticket {ticket_id} not found in tickets/active/.")
        sys.exit(1)

    # 2. Move Ticket (The Unlock)
    done_file = done_dir / ticket_file.name
    done_dir.mkdir(parents=True, exist_ok=True)
    shutil.move(str(ticket_file), str(done_file))
    print(f"[✓] Moved to {done_dir.relative_to(project_root)}.")

    # 3. Cleanup Workstream Context
    branch_name = f"feat/{ticket_id}" # Assumption on naming
    context_dir = workstreams_root / branch_name
    if context_dir.exists():
        shutil.rmtree(context_dir)
        print(f"[✓] Deleted temporary context: {context_dir.relative_to(project_root)}.")

    print("\n" + "="*60)
    print("TICKET RELEASED. TRANSITIONING TO IDLE (S0).")
    print("="*60)
    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 release_ticket.py <TICKET_ID>")
        sys.exit(1)
    release_ticket(sys.argv[1])
