# TICKET-002: Service Infrastructure Repair

## Goal
Fix broken file references and backfill missing templates identified in the Architectural Gap Analysis.

## Context
Audit findings reveal that `system-diagnosis` points to a non-existent path for cleanup scripts, and multiple SKILLs reference missing templates.

## Tasks
- [ ] Fix `system-diagnosis/SKILL.md`: Update `scripts/gc_workstreams.py` to `scripts/maintenance/gc_workstreams.py`.
- [ ] Create `references/AUDIT_TEMPLATE.md`.
- [ ] Create `references/DEBUG_REPORT_TEMPLATE.md`.
- [ ] Create `references/MAINTENANCE.md`.
- [ ] Create `references/environment_spec.md`.
- [ ] Create `references/qa_protocol.md`.
- [ ] Create `references/TICKET_TEMPLATE.md`.
