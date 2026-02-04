#!/usr/bin/env python3
import os
import sys
from pathlib import Path

def ready_check():
    """
    Evidence Provider for architectural-design.
    """
    project_root = Path(os.getcwd())
    specs_dir = project_root / "specs"
    
    # 1. Specs Check
    has_specs_dir = specs_dir.exists()
    has_arch = (specs_dir / "01-ARCHITECTURE.md").exists() if has_specs_dir else False
    has_goals = (specs_dir / "02-DESIGN_GOALS.md").exists() if has_specs_dir else False
    
    print(f"REPORT: [SPECS_DIR:{has_specs_dir}] [ARCH:{has_arch}] [GOALS:{has_goals}]")

    # 2. Reflections Check
    script_dir = Path(__file__).parent
    check_reflections = script_dir / "check_reflections.py"
    has_reflections = False
    if check_reflections.exists():
        import subprocess
        result = subprocess.run([sys.executable, str(check_reflections)], capture_output=True, text=True)
        if result.returncode == 0:
            has_reflections = True
            
    print(f"REPORT: [REFLECTIONS:{has_reflections}]")
    
    sys.exit(0)

if __name__ == "__main__":
    ready_check()
