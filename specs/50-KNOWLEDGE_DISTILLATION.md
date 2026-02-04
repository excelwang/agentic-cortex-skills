# 50 - Knowledge Distillation (Lessons Learned System)

> **Status**: Implemented
> **Version**: 1.0

## 1. Purpose

The Knowledge Distillation system provides a standardized mechanism for capturing and persisting lessons learned during the development lifecycle. It ensures that insights from code reviews (Judge) and debugging sessions (Detective) are systematically recorded for future reference.

## 2. Design Goals

1. **Consistency**: All lessons follow a uniform schema.
2. **Safety**: File locking prevents race conditions during concurrent writes.
3. **Traceability**: Each lesson links to its originating context (Ticket/File).
4. **Accessibility**: Lessons are human-readable Markdown.

## 3. Schema

Each lesson entry contains:

| Field | Type | Description |
|-------|------|-------------|
| `type` | Enum | `Mistake`, `Pattern`, `Anti-Pattern` |
| `context` | String | Ticket ID or File reference |
| `content` | String | The lesson description |
| `author` | Enum | `Judge`, `Detective`, `Architect`, `Executor` |
| `date` | Timestamp | Auto-generated on creation |

## 4. Tooling

### A. The Script (`scripts/record_lesson.py`)

```bash
python3 scripts/record_lesson.py \
    --type "Pattern|Mistake|Anti-Pattern" \
    --context "[TICKET_ID or File]" \
    --content "[Lesson description]" \
    --author "Judge|Detective|Architect|Executor"
```

### B. Storage Location

- **Path**: `.agent/brain/lessons.md`
- **Format**: Append-only Markdown with structured entries

## 5. Access Control

| Persona | Permission |
|---------|------------|
| Judge | Append only |
| Detective | Append only |
| Architect | Full (revision/archive) |
| Executor | Append only |

## 6. Integration

Skills that use this system:
- `code-review/SKILL.md` - Section: Knowledge Persistence
- `system-diagnosis/SKILL.md` - Section: Cold Case Knowledge
