#!/usr/bin/env python3
import os
import sys
import datetime
from pathlib import Path

def integrate_reflections():
    """
    Scans for LESSON_*.md in references/.
    Checks specs/specs-inbox.md.
    Consolidates ALL content into a single report.
    Deletes ALL files (lessons + inbox) to ensure 'Read-Once' atomicity.
    Prints the consolidated content for the Agent to process immediately.
    """
    script_dir = Path(__file__).parent
    skill_root = script_dir.parent
    ref_dir = skill_root / "references"
    
    # Locate specs directory
    specs_dir = skill_root.parents[1] / "specs" 
    inbox_file = specs_dir / "specs-inbox.md"

    if not ref_dir.exists() or not specs_dir.exists():
        print(f"Error: Missing directories. Ref: {ref_dir}, Specs: {specs_dir}")
        sys.exit(1)

    # 1. Gather Content
    final_report = []
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # A. From Inbox
    if inbox_file.exists():
        inbox_content = inbox_file.read_text().strip()
        if inbox_content:
            final_report.append(f"## Previous Inbox Content\n{inbox_content}\n")
    
    # B. From New Lessons
    lesson_files = []
    for f in ref_dir.glob("*.md"):
        if f.name.startswith("LESSON_") or f.name.startswith("REFLECTION_"):
            lesson_files.append(f)
            content = f.read_text().strip()
            final_report.append(f"### Source: {f.name} ({timestamp})\n{content}\n")

    # 2. Check if there is anything to report
    if not final_report:
        print("No pending reflections or inbox content.")
        sys.exit(1) # No action needed

    # 3. Output to Agent ( The Handover )
    print("CRITICAL: Consolidated Reflections found. You must ACTION these immediately.")
    print("=" * 60)
    print("\n".join(final_report))
    print("=" * 60)

    # 4. Cleanup ( The Destruction )
    # Delete lessons
    for f in lesson_files:
        f.unlink()
    
    # Delete inbox
    if inbox_file.exists():
        inbox_file.unlink()

    print("Cleanup: All source files (lessons + inbox) have been deleted.")
    sys.exit(0)

if __name__ == "__main__":
    integrate_reflections()
