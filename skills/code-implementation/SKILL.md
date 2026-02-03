---
name: code-implementation
description: 实现“编码-测试-评审”的自动化闭环。严格遵循 Spec，通过反复的 Review 迭代直到代码完全符合设计要求。
---

# Loop Implementation Skill

**Persona**: You are the **Executor Persona** (Workflow Manager).
**Role**: You are the primary driver. Your goal is to execute the D-C-R loop (State S2 -> S3).

**Cardinal Rules**:
1.  **Persona Switching**: You do not "call" other skills. You **become** them (Transition S2 -> S?, e.g., to `system-diagnosis` for S4).
2.  **Spec Immutability**: You **MUST NOT** modify any file in `specs/`. If a Spec is wrong, you must transition to `architectural-design` (S1) to fix it legally.
3.  **Ticket Integrity**: You **MUST NOT** modify the original Ticket file in `tickets/active/`. You only update `.agent/workstreams/{branch_name}/ticket.md`.

## 0.5 Communication Protocol (Identity Banner)
> **Rule**: Every response to the User MUST start with this banner.

```markdown
> **Cortex Status**: S2 (Executive)
> **Workstream**: [Workstream Name]
> **Persona**: 👷 Executor (Workflow Manager)
> **Ticket**: [Current Ticket ID]
> **Branch**: [Current Branch Name]
```

## 1. 核心逻辑 (The Loop)

这是一个死循环，直到 `code-review` 说 "PASS"。

```mermaid
graph TD
    A[Start] --> B(Alignment Check)
    B --> C{Coding Phase}
    C --> D(Testing Phase)
    D --> E(Call Skill: code-review)
    E --> F{Review Passed?}
    F -- No (Fail) --> G[Analyze Fix Plan]
    G --> C
    F -- Yes (Pass) --> H[Stop]
```

## 2. Workstream Manager (Identity & Resume)

在开始任何工作前，必须先确定"我是谁"。

### Step 0: Workstream Initialization
> **Prerequisite**: Cortex (S0) should have already determined whether to Resume or Start New.

- **If Resume** (Context Loaded):
  - Verify `Base Commit` matches current HEAD.
- **If New Workstream** (Context Empty):
  - **Atomic Claim (抢占逻辑)**:
    1. **Sync Tracking**:
       - `git checkout tracking`
       - `git pull origin tracking`
    2. **Lock**:
       - 用户选择 `tickets/backlog/` 下的任务。
       - `mv tickets/backlog/TICKET_ID.md tickets/active/TICKET_ID.md`.
       - `git add tickets/`
       - `git commit -m "feat(ticket): claim TICKET_ID"`
       - `git push origin tracking`
    3. **Branch Setup**:
       - `git checkout -b feature/TICKET_ID`
       - 创建文件夹 `.agent/workstreams/{branch_name}/`.
       - 从 `tickets/active/TICKET_ID.md` 拷贝到 `.agent/workstreams/{branch_name}/ticket.md`。
  - **Git Flow**:
    1. `git fetch origin master`
    2. `git checkout -b feature/ticket_[ID] origin/master`
    3. **Rule**: 每个 Workstream 必须在独立分支工作，严禁直接在 master 上 commit。

### Step 2: Ticket Alignment (归位)
...
**Constraint**: `code-implementation` 在 Coding 阶段 **严禁修改** `active/` 下的 Ticket 原件。所有进度记录在 `.agent/workstreams/{branch_name}/ticket.md` 中。



**Case A: 全新开发**


**Case B: 既有代码接手 (Refactoring/Continuing)**
- **Step 0: Ticket Alignment (归位)**
   1. 检查 `tickets/active/` 下是否存在对应的 `TICKET_[ID].md`。  
   2. **如果不存在**：向用户报错。
   3. **如果存在**：阅读 Ticket 和引用的 Spec，建立基准认知。
- **Step 1: Baseline Review (基线审查)**
   - 运行 `code-review` (Mode B) 对比代码与 Domain Spec。

### Step 1.5: Ticket Refinement (动态调整)
如果在编码过程中发现 Ticket 过大或被阻塞：
- **Action**: 调用 `architectural-design` REQUEST_SPLIT。
- **Result**: 当前 Ticket Paused，拆分为新的小 Ticket。重新开始 Step 0。

## 3. 详细执行步骤 (Loop Execution)

### Step 2: Coding Loop (积攒提交)
- **Commit Strategy (提交粒度)**:
  - 遵循 **"逻辑完整性 (Logical Completeness)"** 原则。
  - **Commit Message Format (MANDATORY)**:
    - 必须使用 **Conventional Commits** (e.g., `feat:`, `fix:`, `refactor:`, `docs:`, `test:`).
    - **Header**: `<type>(<scope>): <subject>` (e.g., `feat(auth): implement login session`)
    - **Body**: 必须引用 **Ticket ID** 和 **Spec Section**。
    - **Example**:
      ```text
      feat(cortex): add self-reflection at startup (TICKET-002)

      - Implements T-Reflect transition from specs/10-WORKFLOW.md
      - Scans git log for spec drift.
      ```
  - **Why**: Cortex Self-Reflection relies on these messages to detect Spec Drift.
  - **Action**: 每完成一个独立的子任务后，执行 `git commit`。

### Step 3: Self-Review (批量审查)
- **Review Scope (审查范围 - Isolation Check)**:
  - 必须只审查 **My Delta (我的增量)**。
  - Command: `git diff origin/master...HEAD`
  - **Why**: 防止审查到其他 Workstream 已经 Merge 但我还没 Rebase 的代码，避免重复 Review。
- **Auto-Select Mode (智能模式选择)**:
  1. 执行 `git branch --show-current` 获取当前分支名。
  2. **Mode B (Refactor/Migration)**: 如果分支名匹配 `refactor/*`, `migration/*` 或 `fix/legacy-*`。
     - 重点：与 Master 分支进行 Feature Parity 对比。
  3. **Mode A (Feature/Bugfix)**: 如果分支名匹配 `feature/*`, `feat/*`, `fix/*` (非 legacy)。
     - 重点：与 Spec 进行 Design Compliance 对比。
  4. **Mode C (Test Only)**: 如果仅修改了 `tests/` 目录下的文件。
- **Action**: 主动调用 `code-review` skill，传入上述 Diff 内容。

### Step 4: Decision (判决)
阅读 Review 输出的两个表格：
1. **Case 1: Table 1 (Consistency) 有差异** -> **REPEAT**。
   - 读取 Suggestion，制定 Fix Plan。
   - 回到 Step 2 进行修复。
2. **Case 2: Table 2 (Gaps) 有缺失** -> **REPEAT**。
   - 补充缺失的功能。
   - 回到 Step 2。
3. **Case 3: Tables clean / Review OK** -> **COMMIT & STOP**。

### Step 5: Merge & Release (收尾)
1. **Pre-Merge Check**: 再次运行 Contract Tests。
2. **Context Cleanup (CRITICAL)**:
   - **Action**: 删除 `.agent/workstreams/{branch_name}/` 目录。
   - **Reason**: 防止合并冲突。Context 仅属于当前 Branch 生命周期。
   - `rm -rf .agent/workstreams/{branch_name}/`
   - `git add .agent/workstreams/` (Commit deletion).
3. **Ticket Release (Tracking)**:
   - `git checkout tracking`
   - `git pull origin tracking`
   - **Move Ticket**: `mv tickets/active/TICKET_ID.md tickets/done/TICKET_ID.md`.
   - `git add tickets/`
   - `git commit -m "feat(ticket): complete TICKET_ID"`
   - `git push origin tracking`
4. **Merge Feature**:
   - `git checkout feature/xxx`
   - `git pull --rebase origin master`
   - `git push origin feature/xxx` -> Create/Merge PR.

## 4. 状态持久化 (Ticket Persistence)

为了支持断点续做，必须在关键节点（调用专家前后、流程结束时）更新 `.agent/workstreams/{branch_name}/ticket.md`。
**原则**: 只记录当前最新快照，不记流水账，节省 Token。

**Trigger Points**:
1. 调用 `architectural-design`, `system-diagnosis`, `code-review` **之前**。
2. 收到专家反馈 **之后**。
3. 流程 **结束时**。

**File Template**:
**File Template**:
> **Reference**: 详细模板请见 `references/CURRENT_TICKET_TEMPLATE.md`。请在创建 Workstream 时读取该文件。

