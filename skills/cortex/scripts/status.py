#!/usr/bin/env python3
import os
import sys
from pathlib import Path

def get_status():
    """
    Scans the project structure and provides a health/progress dashboard.
    Used by Cortex and the User to see the 'big picture'.
    """
    project_root = Path(os.getcwd())
    
    print("="*60)
    print(f"       AG-CORTEX SYSTEM STATUS: {project_root.name}")
    print("="*60)

    # 1. Specs
    specs_dir = project_root / "specs"
    if specs_dir.exists():
        specs = list(specs_dir.glob("*.md"))
        print(f"[Specs]: {len(specs)} laws defined.")
    else:
        print("[Specs]: No specs directory found.")

    # 2. Tickets
    ticket_states = ["active", "backlog", "done"]
    print("\n[Tickets]:")
    for state in ticket_states:
        tdir = project_root / "tickets" / state
        count = len(list(tdir.glob("*.md"))) if tdir.exists() else 0
        print(f"  - {state.capitalize()}: {count}")

    # 3. Reflections
    ref_dir = Path("skills/architectural-design/references")
    if ref_dir.exists():
        lessons = len(list(ref_dir.glob("LESSON_*.md")))
        reflections = len(list(ref_dir.glob("REFLECTION_*.md")))
        if lessons + reflections > 0:
            print(f"\n[Knowledge]: {lessons + reflections} pending reflections found.")
        else:
            print("\n[Knowledge]: No pending reflections.")
    
    # 4. Git Info
    try:
        import subprocess
        branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], text=True).strip()
        print(f"\n[Git]: Active Branch: {branch}")
    except:
        pass

    print("="*60)
    sys.exit(0)

if __name__ == "__main__":
    get_status()
