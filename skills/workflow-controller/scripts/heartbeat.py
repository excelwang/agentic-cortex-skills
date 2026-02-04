#!/usr/bin/env python3
import os
import time
import sys
import argparse
from pathlib import Path

def check_status(scenario_dir, flag_dir, quiet=False):
    scenario_dir = Path(scenario_dir)
    flag_dir = Path(flag_dir)
    fragments_dir = scenario_dir / "fragments"
    next_prompt_file = scenario_dir / "next-prompt.md"
    
    # We assume a standard fragment naming convention in the scenario
    fragments = sorted(list(fragments_dir.glob("*.md")))
    if not fragments:
        if not quiet: print(f"[✗] Error: No fragments found in {fragments_dir}")
        return True, 0

    # Define stages based on available fragments
    stages = []
    for i, frag in enumerate(fragments):
        # We expect flags like S1_DONE, S2_DONE based on fragment index
        stages.append({
            "name": f"Stage {i+1}",
            "flag": f"S{i+1}_DONE",
            "fragment": frag.name
        })

    flag_dir.mkdir(parents=True, exist_ok=True)
    
    current_stage_idx = 0
    for i, stage in enumerate(stages):
        if (flag_dir / stage["flag"]).exists():
            current_stage_idx = i + 1
    
    if current_stage_idx >= len(stages):
        if not quiet: print("✅ ALL STAGES COMPLETED.")
        return True, current_stage_idx

    next_stage = stages[current_stage_idx]
    fragment_path = fragments_dir / next_stage["fragment"]
    
    if not quiet:
        print(f"--- 💓 Workflow Heartbeat ---")
        print(f"Scenario: {scenario_dir.name}")
        print(f"Current Status: Stage {current_stage_idx} complete.")
        print(f"Pending: {next_stage['name']} ({next_stage['fragment']})")
    
    if fragment_path.exists():
        prompt_content = fragment_path.read_text()
        with open(next_prompt_file, 'w') as f:
            f.write(f"# ⏭️ NEXT PROMPT: {next_stage['name']}\n\n")
            f.write("---\n")
            f.write(prompt_content)
            f.write("\n---\n")
    
    return False, current_stage_idx

def watch(scenario_dir, flag_dir, interval=60):
    print(f"--- 🕵️ Watching Scenario: {scenario_dir} ---")
    print(f"Interval: {interval}s | Flags: {flag_dir}")
    
    _, initial_stage = check_status(scenario_dir, flag_dir, quiet=True)
    
    while True:
        done, current_stage = check_status(scenario_dir, flag_dir, quiet=True)
        if current_stage > initial_stage or done:
            print(f"\n[!] State Change Detected: Stage {current_stage}")
            check_status(scenario_dir, flag_dir) # Final print
            break
        
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(interval)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generic Workflow Heartbeat Engine")
    parser.add_argument("--scenario", required=True, help="Path to the scenario directory containing fragments/")
    parser.add_argument("--flags", default=".agent/workstreams/flags", help="Path to the progress flags directory")
    parser.add_argument("--watch", action="store_true", help="Enable polling mode")
    parser.add_argument("--interval", type=int, default=60, help="Polling interval in seconds")
    
    args = parser.parse_args()
    
    if args.watch:
        watch(args.scenario, args.flags, args.interval)
    else:
        check_status(args.scenario, args.flags)
