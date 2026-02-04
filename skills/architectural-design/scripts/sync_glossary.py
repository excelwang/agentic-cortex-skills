#!/usr/bin/env python3
import os
import sys
import re
from pathlib import Path

def sync_glossary():
    """
    Scans tickets/done/ for new terms and cross-references with specs/00-GLOSSARY.md.
    This is an assistive script for the Architect.
    """
    print("--- 🏛️ Glossary Sync Assistant ---")
    
    project_root = Path(os.getcwd())
    glossary_file = project_root / "specs" / "00-GLOSSARY.md"
    done_tickets = list((project_root / "tickets" / "done").glob("*.md"))
    
    if not glossary_file.exists():
        print("[!] Error: specs/00-GLOSSARY.md not found.")
        sys.exit(1)

    glossary_content = glossary_file.read_text()
    
    # Simple heuristic: find bolded terms in tickets that aren't in glossary
    new_potential_terms = set()
    for ticket in done_tickets:
        content = ticket.read_text()
        # Look for pattern: **Term**
        matches = re.findall(r"\*\*([A-Z][a-zA-Z\s]+)\*\*", content)
        for term in matches:
            if term not in glossary_content:
                new_potential_terms.add(term)

    if new_potential_terms:
        print(f"[i] Found {len(new_potential_terms)} potential new terms in completed tickets:")
        for term in sorted(new_potential_terms):
            print(f"    - {term}")
        print("\nAction: Please review and incorporate into specs/00-GLOSSARY.md.")
    else:
        print("[✓] Glossary is currently in sync with completed tickets.")
    
    sys.exit(0)

if __name__ == "__main__":
    sync_glossary()
