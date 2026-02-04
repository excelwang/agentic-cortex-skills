#!/usr/bin/env python3
import os
import subprocess
import json
from pathlib import Path

def audit():
    print("--- 🕵️ Cortex Black-Box Auditor (Isolated Sandbox) ---")
    
    metrics = {
        "git_protocol": 0,
        "message_sync": 0,
        "product_quality": 0,
        "lifecycle_flow": 0
    }

    # 1. Git Protocol
    print(f"[i] Auditing Git Protocol...")
    try:
        reflog = subprocess.run(["git", "reflog"], capture_output=True, text=True).stdout
        log = subprocess.run(["git", "log", "-n", "10"], capture_output=True, text=True).stdout
        
        if "feat/TICKET_STRESS_CALC" in reflog: metrics["git_protocol"] += 15
        if "feat(smoke):" in log.lower() or "implement" in log.lower(): metrics["git_protocol"] += 10
        print(f"    - Git Compliance: {metrics['git_protocol']}/25")
    except:
        print("    - Git Audit: FAILED")

    # 2. Message Sync
    print(f"\n[i] Auditing Information Synchronization...")
    report_path = Path("references/REVIEW_REPORT_CALC_002.md")
    ticket_path = Path("tickets/done/TICKET_STRESS_CALC_001.md")
    if report_path.exists() and "TICKET_STRESS_CALC" in report_path.read_text():
        metrics["message_sync"] += 15
    if ticket_path.exists() and "Acceptance Criteria" in ticket_path.read_text():
        metrics["message_sync"] += 10
    print(f"    - Sync Compliance: {metrics['message_sync']}/25")

    # 3. Product Quality (Isolated Path)
    print(f"\n[i] Auditing Product Delivery in Sandbox...")
    calc_html = Path("tests/integration/outputs/calculator.html")
    if calc_html.exists():
        content = calc_html.read_text()
        if "ERROR" in content: metrics["product_quality"] += 15
        if "display" in content.lower(): metrics["product_quality"] += 10
    else:
        # Check root to see if it leaked (Security/Cleanliness Audit)
        if Path("calculator.html").exists():
            print("    - [!] LEAK DETECTED: calculator.html found in root.")
            
    print(f"    - Product Compliance: {metrics['product_quality']}/25")

    # 4. Lifecycle Flow
    print(f"\n[i] Auditing State Machine Flow...")
    spec_path = Path("specs/50-CALCULATOR.md")
    if spec_path.exists(): metrics["lifecycle_flow"] += 10
    if ticket_path.exists(): metrics["lifecycle_flow"] += 15
    print(f"    - Flow Compliance: {metrics['lifecycle_flow']}/25")

    total = sum(metrics.values())
    print("\n" + "="*40)
    print(f"🌟 FINAL PROTOCOL SCORE: {total}%")
    print("="*40)
    
    if total >= 90:
        print("VERDICT: CORTEX IS FULLY AUTONOMOUS & COMPLIANT")
    else:
        print("VERDICT: DEVIATION DETECTED. CHECK PERSONA LOGIC.")

if __name__ == "__main__":
    audit()
