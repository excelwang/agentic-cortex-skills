#!/usr/bin/env python3
import os
import sys
import shutil
from pathlib import Path

def finish_ticket(ticket_id):
    """
    Finalizes a ticket:
    1. Moves ticket to done/
    2. Suggests a reflection capture.
    """
    project_root = Path(os.getcwd())
    active_dir = project_root / "tickets" / "active"
    done_dir = project_root / "tickets" / "done"
    
    print(f"--- 🏁 Finalizing Ticket: {ticket_id} ---")
    
    done_dir.mkdir(parents=True, exist_ok=True)
    
    # Find the ticket file
    ticket_file = None
    for f in active_dir.glob(f"*{ticket_id}*.md"):
        ticket_file = f
        break
        
    if not ticket_file:
        print(f"[✗] Error: Ticket {ticket_id} not found in tickets/active/.")
        sys.exit(1)

    # Move to done
    shutil.move(str(ticket_file), str(done_dir / ticket_file.name))
    print(f"[✓] Ticket moved to {done_dir.relative_to(project_root)}.")

    print("\n" + "="*60)
    print("TICKET COMPLETE")
    print("="*60)
    print("Recommended Action:")
    print("- 'Hi Cortex, design reflect on [Topic]' to capture lessons.")
    print("- Or 'Hi Cortex' to pick up the next task.")
    print("="*60)
    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 finish_ticket.py <TICKET_ID>")
        sys.exit(1)
    finish_ticket(sys.argv[1])
