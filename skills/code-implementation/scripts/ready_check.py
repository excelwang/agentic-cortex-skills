#!/usr/bin/env python3
import os
import sys
from pathlib import Path

def ready_check():
    """
    Checks pre-conditions for code-implementation.
    Guides the agent back to Architect if no mandate (ticket) exists.
    """
    project_root = Path(os.getcwd())
    active_dir = project_root / "tickets" / "active"
    backlog_dir = project_root / "tickets" / "backlog"
    
    print(f"--- 👷 Executor Readiness Check ---")
    
    if not active_dir.exists():
        print("[✗] Blocker: tickets/active/ directory not found.")
        print("    -> Action: Return to Architect (S1) to initialize project structure.")
        sys.exit(1)
        
    tickets = list(active_dir.glob("*.md"))
    if not tickets:
        print("[✗] Blocker: No active tickets found.")
        
        # Look for backlog to give better advice
        if backlog_dir.exists():
            backlog = list(backlog_dir.glob("*.md"))
            if backlog:
                print(f"    -> Action: Found {len(backlog)} tickets in backlog. Return to Architect (S1) to promote one.")
            else:
                print("    -> Action: Backlog is also empty. Return to Architect (S1) to run Mode B (Gap Analysis).")
        else:
            print("    -> Action: Return to Architect (S1) to generate new work mandates.")
        sys.exit(1)
    
    print(f"[✓] Mandate: Found {len(tickets)} active ticket(s) for execution.")
    print(f"    Active: {tickets[0].name}")
        
    print("\n[✓] Executor persona is ready to proceed.")
    sys.exit(0)

if __name__ == "__main__":
    ready_check()
