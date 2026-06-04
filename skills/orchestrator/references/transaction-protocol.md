# 多文件写入事务协议（Transaction Protocol）

## 触发条件

当一次 skill 执行需要**写入或修改 2 个及以上文件**时，必须走事务流程。单文件写入不需要。

典型触发场景：
- `post-meeting-report` → 更新 EP + OP + Contact + State
- 信息变更传播 → 人事变动、竞争情报、deal 变化等波及多文件
- `engagement-plan` 生成/更新 → EP 文件 + State + 可能触发 OP 刷新
- 冷启动链中任何产出多文件的节点

## 事务文件格式

写入前，在 `~/Sales/.state/transactions/` 下创建事务文件：

```yaml
# ~/Sales/.state/transactions/{Customer}_{YYYYMMDD_HHmmss}_{skill}.yaml
transaction:
  id: "20260604_143022_pmr"
  customer: "客户A"
  triggered_by: "post-meeting-report"
  created_at: "2026-06-04T14:30:22+08:00"
  status: "in_progress"  # in_progress → completed | failed

  operations:
    - seq: 1
      target_file: "~/Sales/客户A/Opp1/EP_客户A_20260604.md"
      action: "append_section"
      section: "execution_log"
      description: "追加6/4会议执行记录"
      done: false

    - seq: 2
      target_file: "~/Sales/客户A/Opp1/OP_客户A_20260604.md"
      action: "update_section"
      section: "stage_evidence"
      description: "更新阶段证据"
      done: false

    - seq: 3
      target_file: "~/Sales/客户A/_account/contacts/张三.md"
      action: "update_section"
      section: "behavioral_observations"
      description: "追加本次会议行为观察"
      done: false

    - seq: 4
      target_file: "~/.state/客户A.yaml"
      action: "set_fields"
      fields:
        skills.ep.last_updated: "2026-06-04"
        skills.op.refresh_due: true
      done: false

  error_log: []
```

## 执行规则

1. 创建事务文件，status 设为 `in_progress`
2. 按 `seq` 顺序逐个执行写入
3. 每个操作完成后，将对应 `done` 改为 `true`
4. 全部完成 → status 改为 `completed`
5. 某个失败 → `error_log` 记录（seq, error, timestamp），继续后续操作，最终 status 设为 `failed`

操作顺序原则：
- 被依赖的文件先写
- State 文件总是排最后
- 用户可见主文件（EP、OP）优先于辅助文件

## 启动恢复

Orchestrator 每次激活时扫描 `~/Sales/.state/transactions/`：

| 状态 | 处理 |
|------|------|
| `in_progress` / `failed` | 从首个 `done: false` 重放，告知用户 "上次有未完成同步，正在补完" |
| `completed` 且超 48h | 移入 `~/Sales/.state/transactions/_archive/` |
| `completed` 且 48h 内 | 保留不动 |

## 幂等保证

- `append_section`: 检查内容是否已存在（按 description 去重），已存在则跳过
- `update_section`: 直接覆盖，天然幂等
- `set_fields`: 直接覆盖，天然幂等

## 冲突控制

同一客户不允许两个事务并行。检测到已有 `in_progress` 事务时等待（最多 30 秒），超时则报告用户。

## 失败处理

| 失败类型 | 处理 |
|---------|------|
| 文件路径不存在 | 尝试自动修正，不行则跳过并记录 |
| 目标 section 不存在 | 创建该 section 后写入 |
| 文件内容冲突 | 读取最新内容 merge 后重试一次 |
| 连续 3 个操作失败 | 停止，status: failed，要求用户介入 |

## 用户通知

完成后：
```
✅ 已同步 4 处更新：
  · EP 执行日志 ← 新增会议记录
  · OP 阶段证据 ← Champion确认信号
  · 张三档案 ← 行为观察追加
  · 客户状态 ← 刷新标记
```

部分失败：
```
⚠️ 同步部分完成（3/4）：
  ✅ EP 执行日志
  ✅ OP 阶段证据
  ❌ 张三档案 — 文件未找到
  ✅ 客户状态
```
