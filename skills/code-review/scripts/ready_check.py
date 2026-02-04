#!/usr/bin/env python3
import os
import sys
from pathlib import Path
import subprocess

def ready_check():
    """
    Checks pre-conditions for code-review.
    Ensures the Judge has evidence (diff) to audit.
    """
    print(f"--- ⚖️ Judge Readiness Check ---")
    
    try:
        # Check for uncommitted changes or diff with master
        result = subprocess.run(["git", "diff", "origin/master...HEAD", "--name-only"], capture_output=True, text=True)
        if result.returncode != 0:
            print("[✗] Blocker: Git diff failed.")
            print("    -> Action: Ensure you are in a git repository and 'origin/master' exists.")
            sys.exit(1)
            
        diff_files = result.stdout.strip().splitlines()
        if not diff_files or (len(diff_files) == 1 and diff_files[0] == ''):
            print("[✗] Blocker: No changes found to review.")
            print("    -> Action: Return to Executor (S2) to implement feature logic first.")
            sys.exit(1)
            
        print(f"[✓] Evidence: Found {len(diff_files)} changed file(s) for audit.")
        
    except FileNotFoundError:
        print("[✗] Blocker: 'git' command not found in environment.")
        sys.exit(1)
        
    print("\n[✓] Judiciary persona is ready to proceed.")
    sys.exit(0)

if __name__ == "__main__":
    ready_check()
