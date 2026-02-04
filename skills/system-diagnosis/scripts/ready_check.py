#!/usr/bin/env python3
import os
import sys
from pathlib import Path

def ready_check():
    """
    Evidence Provider for system-diagnosis.
    """
    project_root = Path(os.getcwd())
    
    has_logs = (project_root / "logs").exists() and any((project_root / "logs").iterdir())
    
    # Check for failure tickets
    active_dir = project_root / "tickets" / "active"
    has_bug_ticket = False
    if active_dir.exists():
        has_bug_ticket = any(t for t in active_dir.glob("*.md") if "fail" in t.name.lower() or "bug" in t.name.lower())

    print(f"REPORT: [LOGS:{has_logs}] [BUG_TICKET:{has_bug_ticket}]")
    sys.exit(0)

if __name__ == "__main__":
    ready_check()
