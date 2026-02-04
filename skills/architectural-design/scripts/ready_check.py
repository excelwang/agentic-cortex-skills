#!/usr/bin/env python3
import os
import sys
from pathlib import Path

def ready_check():
    """
    Checks pre-conditions for architectural-design.
    Provides helpful guidance for next steps.
    """
    project_root = Path(os.getcwd())
    specs_dir = project_root / "specs"
    
    print(f"--- 🏛️ Architect Readiness Check ---")
    
    # Check specs directory
    if not specs_dir.exists():
        print("[i] Status: Greenfield Project detected. No specs/ directory found.")
        print("    -> Action: I will initiate Mode D (Discovery) to gather requirements.")
    else:
        print("[✓] Law: specs/ directory found.")

    # Check for reflections (synergy with check_reflections.py)
    script_dir = Path(__file__).parent
    check_reflections = script_dir / "check_reflections.py"
    if check_reflections.exists():
        import subprocess
        result = subprocess.run([sys.executable, str(check_reflections)], capture_output=True, text=True)
        if result.returncode == 0:
            print("[!] Evolution: Pending lessons/reflections found in references/.")
            print("    -> Action: Please process these in Mode E before starting new designs.")
            print(result.stdout)
    
    print("\n[✓] Legislator persona is ready to proceed.")
    sys.exit(0)

if __name__ == "__main__":
    ready_check()
