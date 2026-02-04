# TICKET-003: Implement Reflections Pipeline

## Goal
Implement the `scripts/check_reflections.py` script to enable the Cortex Startup Audit Protocol.

## Context
The `architectural-design` skill relies on this script to integrate lessons learned into specifications. Currently, the script is missing, causing the protocol to fail silently or be skipped.

## Tasks
- [ ] Create `scripts/check_reflections.py`.
- [ ] Logic:
    - Check file system for "Reflection" artifacts (logic tbd).
    - If found, read and consolidate.
    - Output to stdout.
    - Exit code 0 if reflections found, 1 if not.
