#!/usr/bin/env python3
import os
import sys
from pathlib import Path

def ready_check():
    """
    Evidence Provider for code-implementation.
    """
    project_root = Path(os.getcwd())
    active_dir = project_root / "tickets" / "active"
    backlog_dir = project_root / "tickets" / "backlog"
    
    has_active = active_dir.exists() and any(active_dir.glob("*.md"))
    has_backlog = backlog_dir.exists() and any(backlog_dir.glob("*.md"))
    
    specs_dir = project_root / "specs"
    has_specs = specs_dir.exists() and any(specs_dir.glob("*.md"))

    print(f"REPORT: [ACTIVE:{has_active}] [BACKLOG:{has_backlog}] [SPECS:{has_specs}]")
    
    sys.exit(0)

if __name__ == "__main__":
    ready_check()
