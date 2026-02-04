#!/usr/bin/env python3
import os
import sys
from pathlib import Path

def ready_check():
    """
    Checks pre-conditions for system-diagnosis.
    Guides the Detective on where to start investigation.
    """
    print(f"--- 🕵️ Detective Readiness Check ---")
    
    project_root = Path(os.getcwd())
    logs_dir = project_root / "logs"
    
    # Check for evidence sources
    evidence_found = False
    if logs_dir.exists() and any(logs_dir.iterdir()):
        print("[✓] Evidence: Found logs in logs/ directory.")
        evidence_found = True
    
    # Check for recent failures in tickets/active
    active_dir = project_root / "tickets" / "active"
    if active_dir.exists():
        fail_tickets = [t for t in active_dir.glob("*.md") if "fail" in t.name.lower() or "bug" in t.name.lower()]
        if fail_tickets:
            print(f"[✓] Evidence: Found {len(fail_tickets)} bug/failure ticket(s).")
            evidence_found = True

    if not evidence_found:
        print("[i] Note: No automated failure evidence found.")
        print("    -> Advice: Start by manual inspection of terminal output or running tests.")
        
    print("\n[✓] Detective persona is ready to hunt.")
    sys.exit(0)

if __name__ == "__main__":
    ready_check()
