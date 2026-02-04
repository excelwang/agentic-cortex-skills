#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

def submit_for_review():
    """
    Automates the handoff from Executor (S2) to Judge (S3).
    1. Checks for uncommitted changes.
    2. Runs tests.
    3. Provides clear handoff instructions.
    """
    print("--- 🚀 Submitting Ticket for Review ---")
    
    # 1. Check for uncommitted changes
    status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    if status.stdout.strip():
        print("[!] Warning: You have uncommitted changes.")
        print("    Requirement: All changes must be committed before submission.")
        # sys.exit(1) # Consider if this should be a hard fail
    else:
        print("[✓] All changes are committed.")

    # 2. Run Tests
    print("[i] Running validation tests...")
    # Check if pytest is available
    if subprocess.run(["which", "pytest"], capture_output=True).returncode == 0:
        test_cmd = ["pytest"]
    else:
        test_cmd = ["python3", "-m", "unittest", "discover", "tests"]
        
    test_result = subprocess.run(test_cmd, capture_output=True, text=True)
    if test_result.returncode != 0:
        print(f"[✗] Error: Tests failed ({test_cmd}). Fix all issues before submitting.")
        print(test_result.stdout)
        sys.exit(1)
    print(f"[✓] All tests passed ({test_cmd}).")

    # Progress Flag for S2 (Implementation ready for review)
    flag_path = Path(".agent/workstreams/flags/S2_DONE")
    flag_path.parent.mkdir(parents=True, exist_ok=True)
    flag_path.touch()

    # 3. Handoff Message
    print("\n" + "="*60)
    print("SUBMISSION SUCCESSFUL")
    print("="*60)
    print("Next Steps:")
    print("1. Switch Persona: 'Hi Cortex, Judge review this'.")
    print("2. The Judge will audit your diff and provide a verdict.")
    print("="*60)
    sys.exit(0)

if __name__ == "__main__":
    submit_for_review()
