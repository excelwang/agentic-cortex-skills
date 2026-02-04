#!/usr/bin/env python3
"""
Knowledge Distillation Tool - record_lesson.py

Safely appends structured lessons to .agent/brain/lessons.md with locking
to prevent race conditions and ensure consistent formatting.

Usage:
    python3 scripts/record_lesson.py --type "Pattern" --context "TICKET_005" \
        --content "Always use file locking for append operations" --author "Judge"
"""

import argparse
import fcntl
import os
import sys
from datetime import datetime
from pathlib import Path

# Valid values for type and author
VALID_TYPES = ["Mistake", "Pattern", "Anti-Pattern"]
VALID_AUTHORS = ["Judge", "Detective", "Architect", "Executor"]

# Target file path (relative to project root)
LESSONS_FILE = ".agent/brain/lessons.md"


def get_project_root() -> Path:
    """Find project root by looking for .agent or .git directory."""
    current = Path.cwd()
    for parent in [current] + list(current.parents):
        if (parent / ".agent").exists() or (parent / ".git").exists():
            return parent
    return current


def ensure_lessons_file(filepath: Path) -> None:
    """Create lessons.md with header if it doesn't exist."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    if not filepath.exists():
        header = """# Lessons Learned

> **Purpose**: Knowledge base for patterns, mistakes, and anti-patterns discovered during development.
> **Access**: Append-only for Judge/Detective; Revision by Architect only.

---

"""
        filepath.write_text(header)


def format_lesson(lesson_type: str, context: str, content: str, author: str) -> str:
    """Format a lesson entry with consistent schema."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    emoji_map = {
        "Mistake": "❌",
        "Pattern": "✅",
        "Anti-Pattern": "⚠️"
    }
    emoji = emoji_map.get(lesson_type, "📝")
    
    return f"""
## {emoji} {lesson_type}: {context}

| Field | Value |
|-------|-------|
| **Date** | {timestamp} |
| **Author** | {author} |
| **Context** | {context} |

**Lesson**:
> {content}

---
"""


def append_lesson_safe(filepath: Path, lesson_content: str) -> bool:
    """Append lesson using file locking for safety."""
    try:
        with open(filepath, "a") as f:
            # Acquire exclusive lock
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            try:
                f.write(lesson_content)
                f.flush()
                return True
            finally:
                # Release lock
                fcntl.flock(f.fileno(), fcntl.LOCK_UN)
    except IOError as e:
        print(f"Error writing to lessons file: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Record a lesson to the knowledge base.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Record a pattern:
    python3 scripts/record_lesson.py --type "Pattern" --context "TICKET_005" \\
        --content "Use file locking for safe concurrent writes" --author "Judge"
  
  Record a mistake:
    python3 scripts/record_lesson.py --type "Mistake" --context "auth_module.py" \\
        --content "Forgot to validate token expiry" --author "Detective"
"""
    )
    
    parser.add_argument(
        "--type", "-t",
        required=True,
        choices=VALID_TYPES,
        help=f"Type of lesson: {', '.join(VALID_TYPES)}"
    )
    parser.add_argument(
        "--context", "-c",
        required=True,
        help="The Ticket ID or File ID this lesson relates to"
    )
    parser.add_argument(
        "--content", "-m",
        required=True,
        help="The lesson text/description"
    )
    parser.add_argument(
        "--author", "-a",
        required=True,
        choices=VALID_AUTHORS,
        help=f"The Persona recording this: {', '.join(VALID_AUTHORS)}"
    )
    
    args = parser.parse_args()
    
    # Resolve file path
    project_root = get_project_root()
    lessons_path = project_root / LESSONS_FILE
    
    # Ensure file exists with header
    ensure_lessons_file(lessons_path)
    
    # Format and write lesson
    lesson_entry = format_lesson(args.type, args.context, args.content, args.author)
    
    if append_lesson_safe(lessons_path, lesson_entry):
        print(f"✅ Lesson recorded to {lessons_path}")
        print(f"   Type: {args.type} | Context: {args.context} | Author: {args.author}")
        return 0
    else:
        print("❌ Failed to record lesson", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
