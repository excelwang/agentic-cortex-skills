# Knowledge Distillation: Lessons Learned

This registry captures critical insights, common pitfalls, and design patterns discovered across all workstreams.

| Date | Ticket | Category | Problem/Context | Lesson Learned | Actionable Suggestion |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-02-03 | N/A | Infra | Multi-branch workstream collision | Flat directories lead to context leakage. | Use `.agent/workstreams/{branch}/`. |
| 2026-02-03 | N/A | Process | Spec drift on Startup | 24h window for reflection is unreliable. | Use commit-based reflection (`reflection.json`). |
