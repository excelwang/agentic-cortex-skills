#!/usr/bin/env python3
import os
import time
import sys
from pathlib import Path

# Config
FLAG_DIR = Path(".agent/workstreams/flags")
FRAGMENTS_DIR = Path("tests/integration/fragments/web-calculator")
NEXT_PROMPT_FILE = Path("tests/integration/next-prompt.md")

STAGES = [
    {"name": "Step 1: Design", "flag": "S1_DONE", "fragment": "01_start_design.md"},
    {"name": "Step 2: Implementation", "flag": "S2_DONE", "fragment": "02_begin_implementation.md"},
    {"name": "Step 3: Review", "flag": "S3_DONE", "fragment": "03_request_review.md"},
    {"name": "Step 4: Release", "flag": "S4_DONE", "fragment": "04_release_production.md"},
]

def check_status(quiet=False):
    FLAG_DIR.mkdir(parents=True, exist_ok=True)
    
    current_stage_idx = 0
    for i, stage in enumerate(STAGES):
        if (FLAG_DIR / stage["flag"]).exists():
            current_stage_idx = i + 1
    
    if current_stage_idx >= len(STAGES):
        if not quiet: print("✅ ALL STAGES COMPLETED.")
        return True, current_stage_idx

    next_stage = STAGES[current_stage_idx]
    fragment_path = FRAGMENTS_DIR / next_stage["fragment"]
    
    if not quiet:
        print(f"--- 💓 Workflow Heartbeat ---")
        print(f"Current Status: Stage {current_stage_idx} complete.")
        print(f"Pending: {next_stage['name']}")
    
    if fragment_path.exists():
        prompt_content = fragment_path.read_text()
        with open(NEXT_PROMPT_FILE, 'w') as f:
            f.write(f"# ⏭️ NEXT PROMPT: {next_stage['name']}\n\n")
            f.write("---")
            f.write(prompt_content)
            f.write("---\n")
    
    return False, current_stage_idx

def watch(interval=60):
    print(f"--- 🕵️ Watching for state changes (Interval: {interval}s) ---")
    _, initial_stage = check_status(quiet=True)
    
    while True:
        done, current_stage = check_status(quiet=True)
        if current_stage > initial_stage or done:
            print(f"\n[!] State Change Detected: Stage {current_stage}")
            check_status() # Final print
            break
        
        # Simple progress spinner
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(interval)

if __name__ == "__main__":
    if "--watch" in sys.argv:
        watch()
    else:
        check_status()
