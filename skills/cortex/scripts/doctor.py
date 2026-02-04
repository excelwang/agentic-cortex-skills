#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

def check_env():
    """
    Verifies the system environment against specs/99-ENVIRONMENT.md.
    """
    print("--- 🩺 Cortex System Doctor ---")
    
    checks = [
        ("Git", ["git", "--version"]),
        ("Python", ["python3", "--version"]),
        ("Node", ["node", "--version"]),
    ]
    
    passed = True
    for tool, cmd in checks:
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            print(f"[✓] {tool}: {result.stdout.strip()}")
        except FileNotFoundError:
            print(f"[✗] {tool}: NOT FOUND.")
            passed = False

    # Check Directory structure
    required_dirs = ["specs", "skills", "tickets"]
    for d in required_dirs:
        if Path(d).exists():
            print(f"[✓] Directory: {d}/ exists.")
        else:
            print(f"[✗] Directory: {d}/ MISSING.")
            passed = False

    if passed:
        print("\n[✓] System health is optimal.")
    else:
        print("\n[!] System health degraded. Fix missing dependencies.")
    
    sys.exit(0 if passed else 1)

if __name__ == "__main__":
    check_env()
