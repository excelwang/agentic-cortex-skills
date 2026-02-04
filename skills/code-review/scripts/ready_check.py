#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

def ready_check():
    """
    Evidence Provider for code-review.
    """
    has_diff = False
    try:
        # Check for diff against origin/master
        result = subprocess.run(["git", "diff", "origin/master...HEAD", "--name-only"], capture_output=True, text=True)
        if result.returncode == 0:
            diff_files = result.stdout.strip().splitlines()
            if diff_files and diff_files[0] != '':
                has_diff = True
    except:
        pass

    print(f"REPORT: [GIT_DIFF:{has_diff}]")
    sys.exit(0)

if __name__ == "__main__":
    ready_check()
