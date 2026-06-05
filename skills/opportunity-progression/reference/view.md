═══════════════════════════════════════════════════════════
PROCEDURE 3 — VIEW
═══════════════════════════════════════════════════════════

Templates contain placeholders only — no `if/then` logic, no recomputation, no judgment. Decisions belong in Model and are passed in as values.

Naming: `view:phase<N>.<purpose>` for phase-specific templates, `view:shared.<purpose>` for cross-phase.

## V.0 Language Standard (register / phrasing / bilingual / numeric attribution base)

**Authority:** V.0 governs **how words are styled**. **V.0.6 governs which words are forbidden / allowed** for user-facing strings. Where they overlap on vocabulary, V.0.6 wins. V.0's bilingual rendering rules (below) and numeric attribution rules remain authoritative.

Register: senior sales manager writing a business analysis. Tone: professional, neutral, analytical. Persona governs *what* is analyzed; this rule governs *how* it is worded.

**Phrasing:** Declarative and precise, attributed to analysis rather than anthropomorphized.

| ✅ Use | ❌ Avoid |
|---|---|
| "Analysis indicates rollback to Prospect is warranted." | "Data says you should roll back." |
| "The opportunity shows no EB engagement (E = 0%)." | "You haven't touched the EB yet." |
| "M (0%) is At Risk; relates to I (67%), itself below 80%." (Model layer) | "E is the bottleneck — go get the EB." |

**Note on `At Risk` etc. above:** these are Model-layer phrasings — fine in source data and Model output. View layer (per V.0.6) substitutes with concrete deal language.

**Chinese / English:**
- MEDDPICC element codes stay in English (M, E, DC, DP, P, I, CH, CP) regardless of `language`.
- Section headers, status tags, narrative follow `language`.
- Chinese register is formal business: 商机进展 / 关键障碍 / 阶段对齐性评估, not colloquial 卡点 / 对齐一下 / 搞定.

**Bilingual label rendering (HARD):** Templates show many labels in `中文 / English` form (e.g., `30 天改进目标 / 30-Day Improvement Targets`). Both sides are kept in template text for cross-language documentation. **At render time, output only the side matching `language`:**

| `language` | Output |
|---|---|
| `zh-CN` | Simplified Chinese side only |
| `zh-TW` | Traditional Chinese side only — apply Traditional substitutions where template shows Simplified |
| `en` | English side only |

The separator ` / ` is the explicit signal of a bilingual label. Single-language phrases without ` / ` are NOT auto-translated — they are source-data quotes (e.g., Excel column `课后`) or fixed proper nouns. For narrative phrases needing translation but lacking a ` / ` form, see V.0.5.

**Numbers with attribution:** State figures with source per V.0.1. Example: `E = 10/15 = 67% (source: Scorecard Element score)`. NOT `E is fairly low` or `E 偏低`.

**Drop:**
- Dramatic contrast framing.
- Imperatives directed at the user ("回一个", "pick one").
- Attitudinal adverbs ("exactly", "honestly", "obviously").
- Persona flavor phrases ("the seasoned closer sees...").
- Slang / gaming metaphors / sports idioms ("追分", "seasoned closer", "the deal is stuck", "punchy").
- Directional metaphors for element relationships ("upstream / downstream / cascading / drives / depends on") — the matrix is symmetric.

**Verbatim output blocks:** any "output verbatim" instruction elsewhere is subordinate to V.0 + V.0.6. If conflict, V.0.6 wins (vocabulary), then V.0 (register / phrasing).

## V.0.1 Data Attribution Display (cross-layer with M.0)

Render source alongside any value.

**Inline citation format (preferred):**
- `E = 10/15 = 67% (source: Scorecard / MEDDPICC / E final statement weight 5)`
- `EB Job Title: CFO (source: Scorecard Competitive Info sheet)`

**Footnote format:** numbered references at end of section. Use only when inline would clutter; inline is preferred.

**Inference tag:** when source is `⚠️ Industry/role-based inference, not from Scorecard or connected interfaces`, render the tag verbatim alongside the value.

Never describe an element as low/high/strong/weak without actual percentage and source.

## V.0.2 Reserved Interface Transparency (cross-layer)

When a phase references a reserved interface, status MUST appear in output.

Connected:
```
[Interface #N — Name]: connected. [optional one-line summary]
```

Not connected:
```
[Interface #N — Name]: ⚠️ Not connected. Using LLM internal knowledge as fallback.
```

Never silently omit an interface reference.

## V.0.3 Standing Warning Banner (cross-layer with M.13)

When `rollback_recommended = true`, every Phase 3–6 output (and the Phase 7 report header) prepends a sales-readable rollback banner. The banner is two lines:

```
🔴 建议回退到 [rollback_target]
[rollback_banner.reason — one or two sentences in sales-readable language]
```

**`rollback_banner.reason` rules (HARD — specialization of V.0.6 for the rollback banner):**

The `reason` text is what appears under the banner title. It MUST follow **V.0.6 User-Facing Language Rule** (see V.0.6 Sections A–C for full forbidden / allowed vocabulary).

**Specialization beyond V.0.6: required content (3 items, woven into 1–2 sentences):**

1. **What concretely failed** — the specific exit criterion(s) or stakeholder gap that triggered rollback. Use deal-specific nouns (e.g., "Tech Validation 两条核心退出标准", "EB Ava 实质未接触"), NOT scoring labels.
2. **What stage the deal actually is at** — the rollback target framed as the deal's true position (e.g., "商机其实还停在 Qualified", "其实还停在 Prospect 阶段").
3. **Why the rest of the report still uses the reported stage** — explained as a caveat the rep can quickly understand (e.g., "下面的分析按 Tech Validation 在做，分数容易显得过分乐观").

**Examples:**

- ❌ "Tech Validation 阶段聚合完成度 15%（< 60% 阈值）；当前阶段两条核心退出标准均未实质推进。"
- ❌ "Stakeholder Gate 触发：EB% (15%) + Champion% (83%) = 98%，低于 Qualified 阶段 100% 阈值。"
- ✅ "Tech Validation 两条核心退出标准（架构共识、技术方案达成一致）合计完成度只有 15%，商机其实还停在 Qualified；下面的分析按 Tech Validation 在做，分数容易显得过分乐观。"
- ✅ "Qualified 阶段 EB 与 Champion 接触完整度合计仅 98%（< 100%），且 EB Ava 实质未接触；商机其实还停在 Prospect；下面的分析按 Qualified 在做，分数容易显得过分乐观。"

`view:shared.warning-banner` — slots filled from `current_stage`, `rollback_target`, `rollback_reasons`, gap elements from M.16.

## V.0.4 Symbol Vocabulary

See M.1.6. No symbol may be redefined within a template.

## V.0.5 Phrase Translation Table

Bilingual labels with ` / ` are handled by V.0. This table covers single-language fixed phrases that need language-driven translation. At render time, substitute by `language`.

| Source phrase (template) | `zh-CN` | `zh-TW` | `en` |
|---|---|---|---|
| `Proceeding to Deal Assessment.` | 进入 Deal Assessment 阶段。 | 進入 Deal Assessment 階段。 | Proceeding to Deal Assessment. |
| `Open the file in a browser to view.` | 用浏览器打开文件查看。 | 用瀏覽器開啟檔案查看。 | Open the file in a browser to view. |
| `For PDF or Word copies, reply "导出 PDF" or "导出 Word".` | 需要 PDF 或 Word 版本，回复 "导出 PDF" 或 "导出 Word"。 | 需要 PDF 或 Word 版本，回覆 "導出 PDF" 或 "導出 Word"。 | For PDF or Word copies, reply `导出 PDF` or `导出 Word`. |
| `Sections rendered:` | 已渲染的分块： | 已渲染的分塊： | Sections rendered: |
| `connected.` (interface status) | 已连接。 | 已連接。 | connected. |
| `Not connected. Using LLM internal knowledge as fallback.` | 未连接。回退使用 LLM 内部知识。 | 未連接。回退使用 LLM 內部知識。 | Not connected. Using LLM internal knowledge as fallback. |

NOT translated:
- Confirmation tokens (`continue` / `proceed` / `下一步` / `go`) — user input recognizers.
- Excel column quotes (`课后`, `Completion %`) — source-data field names.

If a new fixed phrase is added to a template and needs translation, extend this table rather than embedding language switches in the template.

## V.0.6 User-Facing Language Rule (HARD — single source of truth for all View output)

This is the **single source of truth** for every string a sales rep will read in any output (chat, HTML report, PDF, Word). It applies to:

- All `view:*` templates
- Every free-text field rendered from data (`rationale`, `root_cause`, `evidence`, `relationship_note`, risk text, action description, strategy rationale, banner reason, etc.)
- Every Phase 2–7 user-facing string

**Sister rules — narrower specializations of V.0.6 (still must be honored):**
- **V.0** Language Standard — register, phrasing, bilingual rendering, numeric attribution conventions. V.0.6 absorbs V.0's vocabulary table; for register / formality, V.0 still governs.
- **M.14 `rationale_text` rules** — Primary Blocker rationale, 3-sentence structure.
- **V.0.3 `rollback_banner.reason` rules** — banner reason, 3-content-item structure.
- **Phase 2 view template placeholders** — section-specific phrasing notes.

If any of these specializations conflict with V.0.6's substitution table or forbidden list, **V.0.6 wins**. Specializations may add stricter rules but cannot relax V.0.6.

**Audience assumption:** A working sales rep at AWS opening this report on Monday morning. They have ~30 seconds before deciding whether to keep reading. They are MEDDPICC-aware but do NOT know this skill's internal scoring/algorithm vocabulary. They want to know: *what's wrong, why does it matter to my deal, what do I do this week*.

---

### Section A — Forbidden vocabulary in user-facing output

**A1. Scoring labels (never bare; always replace with deal-specific description):**

| Forbidden | Reason |
|---|---|
| `P0` / `P1` / `P2` (as bare labels) | scoring band — internal classification |
| `At Risk` / `Needs Improvement` / `On Track` (as bare labels) | scoring labels — say what's actually wrong |
| `阈值` / `threshold` | scoring rule artifact — describe what the customer hasn't done |
| `tiebreak` / `tiebreaker` | algorithm — internal |
| `fact-only` | methodology label — internal |

Note: `P0` / `P1` / `P2` MAY appear as priority badges in Phase 5 Layer A table (where they are the column meaning), but the **rationale and free-text descriptions** must not rely on these labels alone.

**A2. Aggregation / threshold language:**

| Forbidden | Reason |
|---|---|
| `聚合完成度` (raw form) | analytic noun — say "两条退出标准合计完成 X%" instead |
| `进阶门槛` | gate label — say "还差 X / Y / Z 才能进 [next stage]" |
| `60% / 80% / 100% 阈值` (without context) | bare threshold — explain what the threshold means in deal terms |

**A3. Data-structure jargon:**

| Forbidden | Reason |
|---|---|
| `矩阵` / `interdependency matrix` | data structure — never explain the matrix to sales |
| `Layer A` / `Layer B` (in narrative — section headers OK in Phase 5 since they're consistent template anchors) | structure label |
| `看似达标` (Phase 5 Layer A flag — keep flag itself, but never write it inside a paragraph) | flag label leaking into narrative |
| `MEDDPICC 框架归类` / `按 MEDDPICC 体系算 Coach` | meta-framework reference; just state the role and what evidence supports it |

**A4. Phase / model node references:**

| Forbidden | Reason |
|---|---|
| `Phase 2 Primary Blocker = ...` | cross-phase reference — sales doesn't track phases |
| `M.14`, `M.20`, any model node id | implementation detail |
| `Phase 3-6 结果按当前阶段解读` | technical caveat |

**A5. Internal flag names:**

| Forbidden | Reason |
|---|---|
| `Stakeholder Gate` / `Exit Criteria Gate` / `Stage Progression Gate` | gate names — internal |
| `Pass 1` / `Pass 2` / `Pass 3` | pass numbers — internal |
| `Foundation Risk` / `Progression Risk` / `MEDDPICC Risk` (as section badges) | bucket labels — internal classification |

**A6. Academic / defensive caveats:**

| Forbidden | Reason |
|---|---|
| `需视为可能过于乐观` | academic hedge — say "下面的分析按当前阶段在做，分数容易显得过分乐观" |
| `关键前置条件` / `必要 milestone` / `重要节点` / `关键环节` | filler modifiers — name the actual deal mechanic |
| `诊断性建议` / `不会自动改变 CRM 数据` | system-level disclaimer — sales rep already knows reports are advisory |
| `Champion 元素 X% 未达 60% 验证门槛` | scoring-rule speak — describe what David / Champion can't do |

**A7. Slang / informal imagery (V.0 inheritance — re-stated):**

Avoid: 追分 / Score Push, seasoned closer, Gatekeeper, the deal is stuck, punchy, gaming metaphors, sports idioms, directional metaphors for element relationships ("upstream / downstream / cascading / drives / depends on" — the matrix is symmetric).

---

### Section B — Substitution patterns (Model output → View render)

| If model produces | View must render as |
|---|---|
| `M is P0 (At Risk)` | `M 0%（4 项基线指标都没建立）` — score + concrete description |
| `Tech Validation 出口标准未达成` | `Tech Validation 两条退出标准（[name them]）合计完成 X%` |
| `M 与 I 在矩阵中相关` | `M 和 I 都低分，要一起治理` (or omit if not needed) |
| `Tech Validation 阶段聚合完成度 15% (< 60% 阈值)` | `Tech Validation 两条退出标准合计只完成 15%` |
| `进阶门槛未满足` | `还差 X / Y / Z 才能进 [next stage]`（具体列项） |
| `Phase 3-6 结果按当前阶段解读，但需视为可能过于乐观` | `下面的分析按当前阶段在做，分数容易显得过分乐观` |
| `Foundation Risk / Progression Risk / MEDDPICC Risk` | `上一阶段未做到位 / 当前阶段卡点 / 关键人物缺位` |
| `按 MEDDPICC 框架归类为 Coach：Champion 元素 33% 未达验证门槛` | `客户口头识别为内部联系人，但 [Name] 的权力和影响力还没验证（CH 评分只 33%）— 现在只能算 Coach（能给信息但推不动签字）` |
| `E = 0% At Risk; foundation gap` | `EB 还没接触；商机其实还停在 Prospect / Qualified` |

---

### Section C — Allowed canonical phrasing

| Concept | Allowed phrasing |
|---|---|
| Element score state | `M 0%（基线指标空白）`、`I 67%（痛点已识别但损失未量化）` — score + concrete description, never label only |
| Stage relationship | `商机其实还停在 [stage] 推不动`、`下一步进入 [stage] 卡在 [thing]` |
| Element relationship | `M 和 I 都低，需要一起补齐` (when relevant; omit if no concrete action implied) |
| Required action language | `缺少 / 尚未 / 阻碍 / 推进受阻 / 推不动` |
| Visualizable stalls | `商机停在 [stage] 推不动`、`EDP 谈判进不了下一轮`、`下次 EBC 没东西可以汇报`、`本季度 forecast 收不进来` |
| Role normalization | `Coach (能给信息但推不动签字)`、`Champion candidate (待验证)`、`Champion (已验证)`、`EB (Economic Buyer)` |
| Risk bucket labels (when displayed) | `上一阶段未做到位` / `当前阶段卡点` / `关键人物缺位` |

---

### Section D — Per-surface specialization summaries

These are the surfaces with stricter content rules. The forbidden vocabulary above applies universally; below adds per-surface structure.

| Surface | Rules |
|---|---|
| **Phase 2 `primary_blocker.rationale`** | M.14 — 3 sentences: (1) what's missing concretely, (2) what it blocks, (3) visualizable stall |
| **Phase 2 `rollback_banner.reason`** | V.0.3 — 3 content items: (1) what concretely failed, (2) what stage the deal actually is at, (3) why the rest of report still uses reported stage |
| **Phase 2 verdict `rationale[]`** | 2–3 short paragraphs, plain Chinese, name specific exit criteria + gap elements; no defensive disclaimer language |
| **Phase 2 `progression_gaps.items`** | One bullet per missing condition, format `[element] = [score]% → 目标 [target]%` or `[concrete action] (when statement-level gap)`. No "阈值" wording. |
| **Phase 3 `risks[].kind`** | Use sales-readable bucket label (`上一阶段未做到位` / `当前阶段卡点` / `关键人物缺位`), not internal classification (`Foundation Risk` etc.) |
| **Phase 3 `risks[].text`** | Name the specific stage + exit criterion + element. Describe what the customer has / hasn't done. No bare thresholds. |
| **Phase 5 `relationship_note`** | One short clause describing what's true about this element's situation. No `关联 X · Y` raw matrix dump. |
| **Phase 5 Layer B `evidence`** | Quote conflicting Scorecard statements, name the contradiction in plain language. |
| **Phase 5 Layer B `root_cause`** | 2–4 sentences. Cite Scorecard remarks/notes, customer business context. No "矩阵中相关联" / "处于 At Risk" / "未达 80% 阈值". |
| **Phase 5 stakeholder `desc`** | Quote the Scorecard text where the contact appears, then describe role + what's verified vs. unverified. Use Coach / Champion candidate / Champion / EB labels only. |
| **Phase 6 strategy `rationale`** | One sentence linking the strategy to a real deal mechanic (Primary Blocker / 30-day target / unmet exit criterion). No `Phase 2 Primary Blocker = ...` cross-references. |
| **Phase 6 weekly action `description`** | Concrete action with contact / meeting type / deliverable. Avoid generic phrasing ("gather information", "align stakeholders"). |
| **Phase 7 banner / footer** | No `AWS Sales Agent` / `Scorecard: ...` system-meta footer. Use `Generated by Opportunity Progression Skill · Dali Agent` and `Report Date: ...` only. |

---

### Section E — Renderer checklist (every view template MUST satisfy before emit)

1. ✅ No element label appears without a concrete description of what's missing
2. ✅ No threshold number appears without an explanation of what it means for the deal
3. ✅ No data-structure noun (矩阵 / Layer / Gate / Pass) appears in user-facing strings
4. ✅ No phase or model node id appears in user-facing strings
5. ✅ Risk bucket labels (if used) translated to plain Chinese sales language
6. ✅ Role labels (Coach / Champion candidate / Champion / EB) — never raw "Supporter / Sponsor / Stakeholder"
7. ✅ No defensive system-level disclaimer ("诊断性建议", "不会改变 CRM")
8. ✅ Every percentage cited in narrative has a concrete description (not just `M 0%`)

---

### Section F — Examples (full sentences)

**Banner reason:**

- ❌ `Tech Validation 阶段聚合完成度 15%（< 60% 阈值）；当前阶段两条核心退出标准均未实质推进。`
- ✅ `Tech Validation 两条核心退出标准（架构共识、技术方案达成一致）合计完成度只有 15%，商机其实还停在 Qualified；下面的分析按 Tech Validation 在做，分数容易显得过分乐观。`

**Primary Blocker rationale:**

- ❌ `M 处于 P0 优先级（0% < 60% At Risk 阈值）；与 M 在矩阵中相关的 2 个评估项中，I (67%) 也处于 60–80% 偏低区间。按 P0 优先 + 最低分 tiebreak，M 是当前 Primary Blocker。`
- ❌ `DSP 业务的 4 项基线指标尚未量化。没有量化基线，EB 无法对方案价值做出确认。这阻碍了进入 Business Validation 的关键前置条件。` (third sentence too vague)
- ✅ `DSP 业务的 4 项基线指标（投放预算 / ROAS / CPM / 续费率）尚未量化。没有这些数字，EB 没法对方案价值做出确认。这一步过不去，商机就停在 Tech Validation 推不动。`

**Phase 5 root_cause:**

- ❌ `M 与 I 在矩阵中相关联，I 同样未达 80%，两者需共同治理。`
- ✅ `M 和 I 都低分，要一起补：先把痛点损失量化出来，指标就有锚点了。`

**Phase 6 strategy rationale:**

- ❌ `Phase 2 Primary Blocker = M · 0%；Tech Validation 出口标准'技术成功指标已建立'未满足。`
- ✅ `M 是当前关键阻塞（4 项基线指标全空白）；本季度 review 的'技术成功指标已建立'这条要求也卡在这里。`

**Stakeholder David description:**

- ❌ `按 MEDDPICC 框架归类为 Coach：Champion 元素 33% 未达 60% 验证门槛，CH 第 1、2 条 = No，权力与影响力维度未验证。`
- ✅ `Sheet1 备注：'确认了 supporter 是 David'。客户口头识别为内部联系人，但 David 的权力和影响力还没验证（CH 评分只 33%）— 现在只能算 Coach（能给信息但推不动签字）。Phase 6 通过具体动作验证后，再决定能不能升级为 Champion 候选。`

---

### Section G — Cross-reference

- M.14 `rationale_text` rules — specialization for Primary Blocker rationale (still authoritative for its 3-sentence structure).
- V.0.3 Standing Warning Banner — specialization for rollback banner.
- V.0 Language Standard — base register / phrasing / bilingual rendering rules.

V.0.6 supersedes V.0's vocabulary table where they overlap. V.0's bilingual rendering rules and numeric attribution rules remain authoritative.

## V.0.7 Inferred Scorecard Banner (cross-layer with M.3-Auto)

When `scorecard_source = "auto-inferred-accepted"`, every Phase 2–7 output (and the Phase 7 report header) prepends an Inferred Scorecard banner. This is independent of the Rollback banner (V.0.3) — both can render simultaneously, with the Inferred banner above the Rollback banner.

```
ℹ️ 本次分析基于 AI 自动推断的 Scorecard。整体推断信心：[overall_confidence: 高 | 中 | 低]。
[N] / [Total] 条陈述有明确证据；其余由"无足够信息推断"默认为 No。
建议关键 review 前用上传或填表单的方式校准。
```

**Slot fills:**
- `overall_confidence` — from `inference_confidence.overall`.
- `[N]`, `[Total]` — counted from M.3-Auto inferred_statements where `confidence != low` (or where `source != "无足够信息推断"`).

**Render rules:**
- Always render in `surface-container` (neutral / blue) styling, NOT warning yellow — distinguishes "AI 推断" from "Rollback 警告" so banners don't visually compete.
- The banner is permanent across all subsequent phases until skill session ends.
- Phase 7 HTML report includes the same banner verbatim at the top of the report (above the Rollback banner if also present).

**Rationale:** the user already opted into this path in Phase 1A and saw the per-statement review in Phase 1A-Auto. The banner is a persistent reminder, not a re-confirmation prompt.

---

## Phase 1 Templates

### view:phase1.classification-matrix

```
# 商机分级 / Opportunity Classification

请参考下方 4 维度矩阵确认商机分级。

## 4-Dimension Matrix

| Dimension | Commodity | Simple | Strategic |
|-----------|-----------|--------|-----------|
| Solution complexity | Standard product, direct use | Light config / option comparison | Custom design / architecture / POC |
| Reversibility | Fully reversible (use and walk) | Low lock-in (discount refundable) | High lock-in (switching very expensive) |
| Decision cycle | <2 weeks | 2–8 weeks | >8 weeks |
| Deal size (ARR) *— Reference only* | <$50K | $50K–$200K | >$200K |

First three dimensions drive the classification. Deal size is reference context only — it cross-checks but does not decide.

## 请确认分级 / Your Classification

请选择：
- "Commodity" — 退出工具，输出升级信号监测清单
- "Simple" — 请上传 EDDIC Scorecard（5 个要素）
- "Strategic" — 请上传 MEDDPICC Scorecard（8 个要素）
```

### view:phase1.upgrade-signal-checklist

```
# Commodity Confirmed — Upgrade Signals to Watch

This opportunity does not need MEDDPICC/EDDIC analysis at this time. Re-enter this skill if any signal below appears in future customer conversations — the tool will re-classify based on the new picture.

## Dimension-driven signals (aligned with Classification axes)
- New use case or workload scoped on top of the commercial ask *(Solution complexity)*
- Scope expands from one use case to platform / architecture *(Solution complexity)*
- Customer asks AWS to bring in a Solution Architect to design — conversation has left pricing *(Decision cycle)*
- Timeline stretches beyond original window *(Decision cycle)*

## People-driven signals (additional, not in the 4 dimensions)
- Second stakeholder joins ("my manager wants to take a look too")
- New decision-maker appears (VP / CFO joins)
- Decision-makers count crosses 3, or any C-level joins
- Named competitor surfaces (Azure / Alibaba Cloud / GCP)

One trigger hit = re-run classification. Classification only ratchets upward — never downgrade.
```

### view:phase1.eddic-upload-request

```
Classification locked as **Simple Opportunity — EDDIC framework**. Please upload your EDDIC Scorecard (.xlsx) — 5 elements: I, E, DC, DP, CP.

If you do not have one yet, open `eddic-scorecard-form.html` (packaged with this skill) in your browser and fill the form. The Export button produces a valid .xlsx for upload here. Expected fill time: ~5–8 minutes.
```

### view:phase1.meddpicc-upload-request

```
Classification locked as **Strategic Opportunity — MEDDPICC framework**. Please upload your MEDDPICC Scorecard (.xlsx) — all 8 elements.

If you do not have one yet, open `scorecard-form.html` (packaged with this skill) in your browser and fill the form. The Export button produces a valid .xlsx for upload here. Expected fill time: ~10–15 minutes.
```

---

## Phase 1A Templates

### view:phase1a.scorecard-source-prompt

```
Classification locked as **[Simple — EDDIC framework | Strategic — MEDDPICC framework]**.

Scorecard 来源 / Scorecard Source — 怎么提供数据？

(A) **我有 Scorecard** — 直接上传 .xlsx，分析最精准。
(B) **我没有，让我填一份** — 打开表单（[`eddic-scorecard-form.html` | `scorecard-form.html`]）填写后导出 .xlsx 上传，约 [5–8 | 10–15] 分钟。
(C) **让 Agent 用现有信息推断** — 基于本会话中其他 skill（如 `account-context` / `contact-profiling` / `competitive-intelligence` 等）已经收集的信息自动填写 Scorecard。**精度会下降**，但能省时间。Agent 推断后会让你确认或修改。

⚠️ 选 A 或 B 是高精度路径。选 C 是省时路径，结果用于内部参考；建议关键 review 前用 A 或 B 校准。

请回复 A / B / C。
```

`[Simple — EDDIC framework | Strategic — MEDDPICC framework]`、表单文件名、时间估计 — 都根据 `tier` 切换。

### view:phase1a.no-context-fallback

Rendered when user picks Option C but no other Dali skill has run in this session.

```
我手头没有其他 skill 的输出可以参考 — 自动推断会几乎全空白，没意义。建议先选 A（已有 Scorecard 上传）或 B（填表单），或者先跑其他 skill 收集背景信息（如 `account-context` / `contact-profiling`）再回来。

请回复 A 或 B，或者输入 `先跑 account-context`（自动跳转）。
```

---

## Phase 1A-Auto Templates

### view:phase1a-auto.collect-basics-prompt

```
Auto-Inference 准备 — 我需要 4 项基本信息（这些是 Scorecard 之外的描述，无法从其他 skill 直接推断）：

1. 客户名称 / Customer name：
2. 商机名称 / Opportunity name：
3. 当前阶段 / Current stage（从下面选）：
   - Prospect / Qualified / Tech Validation / Business Validation / Committed / Closed/Launched
4. 商机简述 / Opportunity description（可选，1–2 句话，会帮我推断更准）：

请按上述 4 项格式回复（描述可省略）。
```

### view:phase1a-auto.context-relevance-prompt

Rendered after the user provides the 4 basic items. The agent enumerates skill outputs visible in the conversation and asks the user to confirm relevance.

```
Context 关联确认 — 防止用错商机的数据 / Confirm context relevance

我看到本会话中已经有以下 skill 输出。为了避免把别的商机的信息混进来，请逐项告诉我：

[For each visible skill output in conversation:]
- **[skill_name]** — 这个输出是为 **[customer_name] / [opportunity_name]** 跑的吗？
  请回复：
  - `confirmed` — 是的，同客户 + 同商机
  - `assumed` — 同客户但不同商机，或者不确定（信心会被打到中以下）
  - `unrelated` — 不是这单的，请忽略

举例回复格式：
- account-context: confirmed
- contact-profiling: confirmed
- bttroc: assumed
- engagement-plan: unrelated

⚠️ 标 `unrelated` 的 skill 输出会被完全忽略，不会用作推断依据。
⚠️ 如果你没有跑过相关 skill，或者所有都是 `unrelated`，推断质量会很弱（基本全 No），建议改选 Option B 自己填表单。
```

**Implementation rules:**
- Enumerate every skill that has produced output in the current Dali conversation. Use Dali orchestrator to list session-visible skill outputs.
- If none exist, render `view:phase1a-auto.no-context-warning` instead (see below) and do NOT proceed.
- The user's response builds the relevance map (Tier 2 input to M.3-Auto).
- Default for any skill not mentioned by the user: `unrelated` (safest assumption).

### view:phase1a-auto.no-context-warning

Rendered when context check finds zero usable skill outputs (none visible OR all marked unrelated).

```
我手头没有可用的 context — 自动推断会几乎全空白（Scorecard 大部分为 No / 信心低）。

建议改选：
- A — 上传已有 Scorecard
- B — 填表单（约 10–15 分钟）

请回复 A 或 B。或者继续，我会按"全 No / 低信心"基线生成一份默认 Scorecard 给你审阅（不推荐）。
```

### view:phase1a-auto.review-card

This is the most important user-facing surface in the auto-inference path. Render rules:

```
# Auto-Inferred Scorecard — 请审阅 / Please Review

ℹ️ 这是 AI 基于 Dali 其他 skill 的输出推断的 Scorecard。整体推断信心：**[overall_confidence: 高 | 中 | 低]**。

**证据来源分布：**
- [tier_3_confirmed_count] 条由 confirmed_current 的 skill 输出支持（信心可达 高）
- [tier_3_assumed_count] 条由 assumed_current 的 skill 输出支持（信心 capped at 中）
- [tier_1_count] 条由你的商机描述支持
- [default_no_count] 条因无足够信息默认为 No（信心 低）

**Context 使用情况：**
- 已用：[列出 confirmed_current + assumed_current 的 skill 名称]
- 已忽略：[列出 unrelated 的 skill 名称]
- 未跑：[列出本会话中没有跑过、对推断有帮助的 skill — 如 post-meeting-report, business-insight 等]

**基本信息（你提供）：**
- 客户：[customer_name]
- 商机：[opportunity_name]
- 当前阶段：[current_stage]
- 分级：[tier]

---

## 推断的评分（按元素分组）

[For each in-scope element:]

### [Element code] — [Element name]
**推断得分：[score]/[max] = [percent]% · 信心：[高 | 中 | 低]**

[For each statement under this element:]

| 陈述 | 推断 | 依据 | 信心 |
|---|---|---|---|
| [statement_text] | ✅ Yes / ❌ No | [source with source_tier + source_relevance — e.g., "Tier 3 confirmed: contact-profiling — David influence_score = 4" / "Tier 1: 你的描述" / "⚠️ 无足够信息推断"] | 高 / 中 / 低 |

---

## 接下来怎么做？

请回复一项：

- `全部接受` — 把推断结果作为 Scorecard，进入 Phase 2 Deal Assessment。
- `修改 [statement IDs，例如 M-S2, CH-S1]` — 我会逐项让你重打分。
- `修改 context 关联` — 回到 Step 3 重新标记每个 skill 的关联性（推断会基于新的 relevance 重跑）。
- `我自己填表单` — 放弃推断，跳到表单填写流程。

ℹ️ 所有下游报告会带"AI 推断"提示横幅。完整分析建议在关键 review 前用上传或填表单的方式校准。
```

**Implementation rules:**
- Per-element and overall confidence come from M.3-Auto.
- "Yes" inferences MUST cite a specific source with `source_tier` + `source_relevance` (e.g., `"Tier 3 confirmed: contact-profiling — David influence_score = 4"`, `"Tier 1: 用户商机描述"`).
- "No" inferences MUST cite either evidence-of-absence OR `"⚠️ 无足够信息推断"` — never silent.
- Statements list under each element follows the M.1.2 reference weights; render in the order they appear in the standard Scorecard template.
- The 3-line "证据来源分布" + "Context 使用情况" header is mandatory and computed from `inference_confidence.statement_count_by_tier` + `context_used`. This makes the user's data hygiene visible at a glance.

### view:phase1a-auto.statement-edit-prompt

When user replies `修改 [IDs]`, render one prompt per statement:

```
[element code] — Statement [n]:
"[statement_text]"

当前推断：[Yes | No]（依据：[source]）

请回复新的答案：`Yes` / `No` / `保持`。
```

After all edits collected, re-compute element scores and re-render `view:phase1a-auto.review-card`.

---

## Phase 1B Templates

### view:phase1b.parse-error

```
The file format does not meet requirements. Please use the latest Scorecard template for your tier.
```

### view:phase1b.tier-mismatch-prompt

Two variants based on M.4 outcome:

**Lenient mismatch (Simple + MEDDPICC uploaded):**
```
Classification is Simple (EDDIC), but a MEDDPICC Scorecard was uploaded. Analysis will read only the 5 EDDIC-relevant elements (I, E, DC, DP, CP) and ignore M, P, CH — that matches the locked tier. Confirm to continue?
```

**Strict mismatch (Strategic + EDDIC uploaded):**
```
Classification is Strategic (MEDDPICC), but an EDDIC Scorecard was uploaded. EDDIC is missing M, P, and CH — three elements critical for Strategic analysis. Two options:

(A) Downgrade classification to Simple and proceed with EDDIC.
(B) Keep Strategic and complete a full MEDDPICC Scorecard. Existing EDDIC answers can be reused where elements overlap.

Please confirm option (A) or (B).
```

### view:phase1b.consistency-anomaly

```
Scorecard parse complete with one anomaly:
[anomaly description from M.6 — specific cells, expected vs actual]

Confirm to proceed (analysis will use Basic Info Score-After as authoritative for Strategic tier), or re-upload a corrected Scorecard.
```

### view:phase1b.silent-handoff

```
✅ Scorecard parsed — [customer_name] / [opportunity_name] / [current_stage] / [score_display]. Proceeding to Deal Assessment.
```

`[score_display]` per M.6:
- Strategic: `[Score]/100`
- Simple: `EDDIC [Score]/63 = [Z]%`

`Proceeding to Deal Assessment.` is a V.0.5 translatable phrase.

### view:phase1b.full-extraction-dump

On-demand only. Renders:
- Basic Info table (Customer / Opportunity / Location / Type / Stage / Total Score)
- Per-element score breakdown (with weights and contributing statements)
- Consistency check (Basic Info Score-After vs per-element sum)
- Competitive Info status (named competitors, EB Job Title, Customer Business Objective, Potential Obstacles, AWS Solutions)
- Out-of-scope element values (Simple tier with M/P/CH data present)
- Source citation for each cell per V.0.1.

---

## Phase 2 Templates

### view:phase2.deal-assessment-card

Single consolidated card. **All adaptive sections are conditionally rendered — never show "skipped" or "not applicable" placeholders.** Section ordering is fixed; absent sections are omitted entirely.

**Verdict tag (Section 1) — selected by `alignment_result`:**

| `alignment_result` | Verdict tag |
|---|---|
| `Rollback Recommended` | 🔴 **建议回退到 [rollback_target] 阶段** |
| `Aligned — Strengthening Recommended` | ℹ️ **状态合理，建议补强** |
| `Aligned` | ✅ **状态合理** |
| `Advancement Ready` | 🚀 **可推进到 [next_stage]** |

If `alignment_result = Aligned` AND `progression_gate_passed = false`, append to verdict: `（但下一阶段门槛未达）`.

**Body template:**

```
# [Opportunity Name] — Deal Assessment

[Verdict tag from table above]

## 评分与阶段
- 总分：[score display per Score Display Rule]
- 当前阶段：[current_stage][, append "（[verdict tag]）" only if Rollback Recommended or Advancement Ready]
- [current_stage] 出口标准完成度：[aggregate]%

## 关键阻塞
**[primary_blocker.element]** · [primary_blocker.score]% — [primary_blocker.rationale_text — 3 sentences per M.14 (specialization of V.0.6): (1) what is missing concretely, (2) what it blocks, (3) visualizable stall]

[## 进下一阶段（[progression_gate_target]）还需要  ← only when Strategic tier AND progression_gate_passed = false]
[
[for each item in progression_gate_failed_conditions:]
- [condition text per V.0.6 — sales-readable, no Gate / Pass / 阈值 jargon. Examples:
  - "I = 67% → 目标 100%"
  - "CH = 33% → 目标 100%"
  - "已与 EB 接触并提及该项目"（when E S1 = No）
  - "总分 67/100 → 目标 ≥ 65"
]
]

## 本周行动
[one specific action with verifiable outcome, directly tied to Primary Blocker. Must specify contact, meeting type, or deliverable. Avoid generic phrasing.]

## 30 天目标
[up to 3 lines, format: Element ≥ X% · short verification phrase]

[## 为什么[verdict tag short form]  ← only when verdict is Rollback Recommended OR Advancement Ready, OR Aligned with progression_gate_passed = false]
[
2–3 sentences per V.0.6 (plain sales language, no defensive disclaimers). References:
- the specific exit criteria not yet met (from M.16 Foundation Risks / Progression Risks — but render bucket labels per V.0.6 Section B substitution)
- the specific gap elements ("Champion 验证", "基线指标 M") — not the gate names
- if Rollback Recommended AND Stakeholder Gate also triggered (Qualified-only): "同时，最终决策者尚未实质接触" — express as a fact, not as a gate trigger
- if Advancement Ready: state which exit criteria reached 100% and confirm next-stage readiness conditions
- if progression_gate_passed = false: explain in plain language what the next stage requires that's missing

Forbidden per V.0.6: defensive system-level disclaimer language ("Phase 3–6 will continue at reported stage", "warning banner", "diagnostic recommendation", "CRM data"). The audience is a sales rep who already knows analysis is advisory.
]
```

**Footer (Simple tier with out-of-scope data only):**
```
注：M / P / CH 已在 Scorecard 中填写，但 Simple 商机分级不计入分析。如需完整 MEDDPICC 分析，请以 Strategic 分级重新运行。
```

**Score display rule:**
- Strategic: `[Score]/100`
- Simple: `EDDIC [Score]/63 = [Z]%` primary; if Basic Info Score-After differs, append `(ref: Basic Info [W]/100)` in italics.

**Section rules (specialized; full vocabulary discipline per V.0.6):**

- **Section 关键阻塞** must state sales-readable rationale per M.14 — 3 sentences (what's missing / what it blocks / visualizable stall). Never bare scoring labels.
- **Section 进下一阶段** is rendered only at Strategic tier when `progression_gate_passed = false`. Each failed condition is one bullet per V.0.6 (no Gate / Pass / 阈值 jargon). **Do NOT** include a "已达标" list of passing conditions — only show what's missing. **Do NOT** include "进阶门槛是诊断性建议" disclaimer.
- **Section 本周行动** must specify contact, meeting type, or deliverable. Generic phrasing is forbidden per V.0.6 ("gather additional information", "align with stakeholders").
- **Section 30 天目标** elements come from M.10. Maximum 3.
- **Section 为什么…** is the consolidated explanation that replaces the old Phase 2.5 "Result paragraph + Advisory block + acknowledgment prompt". It is rendered ONLY for verdict states that need explaining — `Aligned` (default) is self-explanatory and skips this section.

**Implementation notes:**

- The legacy `view:phase25.alignment-card` and `view:phase25.acknowledgment-prompts` are no longer rendered. Their content has been merged into this single card.
- All internal Model terminology (Stakeholder Gate / Exit Criteria Gate / Stage Progression Gate / Pass 1 / Pass 2 / Pass 3) MUST NOT appear in the user-facing card per V.0.6 Section A5. The Model still uses these names; the View renders only consolidated business language.
- After rendering the card, Control proceeds with standard Phase Gating ("确认进入 Phase 3" or equivalent in detected language). Do NOT render a separate acknowledgment prompt.

---

## Phase 3 Templates

### view:phase3.exit-criteria-table

Header:
```
| # | Stage | Exit Criterion | Scorecard Completion % | Mapped Element (with %) | Status |
|---|---|---|---|---|---|
```

Each row from M.15. Status uses M.1.6 symbol vocabulary.

When one exit criterion has multiple element mappings, render multiple rows (one per mapping) with the criterion text repeated. Lowest-status precedence determines the criterion's aggregate status (rendered in `view:phase3.stage-aggregation`).

### view:phase3.stage-aggregation

For each stage from Prospect through current_stage:
```
**[stage]**: [aggregate]% (in-scope criteria mean) — [N] criteria evaluated
```

### view:phase3.stage-progression-recommendation

Selected by `alignment_result`:

- **Aligned:** `Analysis proceeds at [current_stage]; exit-criteria evidence supports the reported stage.`
- **Aligned — Strengthening Recommended:** `Analysis proceeds at [current_stage]. Current-stage aggregate completion is [aggregate]% (60–79% range); strengthen remaining exit criteria before advancement.`
- **Rollback Recommended:** `Analysis proceeds at [current_stage]. Rollback to [rollback_target] was recommended because [stakeholder gate / exit-criteria gate / both gates] failed. ⚠️ Current-stage findings are potentially over-optimistic; foundation gaps listed below remain unresolved.`
- **Advancement Ready:** `Analysis proceeds at [current_stage]. Current-stage exit criteria at 100% — [next_stage] is supported by the evidence for advancement at the analyst's discretion.`

### view:phase3.risk-buckets

```
## Foundation Risk
[bullets from M.16 foundation_risks. Each bullet: "[stage] / [element] [score]% — [finding]". Empty bucket → render "None — prior-stage foundation is solid."]

## Progression Risk
[bullets from M.16 progression_risks. Inline contradictions are part of finding text, NOT a separate section.]

## MEDDPICC Risk
[bullets from M.16 meddpicc_risks. When element also appears in Foundation/Progression bucket, format as: "[element] [score]% — see Foundation Risk above."]
```

---

## Phase 4 Templates

### view:phase4.market-search

```
## Section 1 — Customer's Current Cloud & GenAI Stack
*Source: account-context skill*

- **Other cloud providers in use:** [output | "not available"]
- **GenAI / LLM providers in use:** [output | "not available"]

## Section 2 — Industry Buying Behavior
*Source: account-context skill (scoped by industry + Opportunity Location + Opportunity Type)*

- **决策因素 / Decision factors:** [output | "not available"]
- **采购痛点 / Procurement pain points:** [output | "not available"]
- **采购周期特征 / Buying cycle characteristics:** [output | "not available"]
- **技术考虑因素 / Technical considerations:** [output | "not available"]

## Section 3 — Same-Industry Customer References
*Source: solutions-search skill*

[customer names | one of:
- Chinese language: 找不到同行业的客户使用该方案
- English language: No customers in the same industry have been found using this solution.]
```

**Render rules:**
- "not available" preserved verbatim — no inference, no training-data substitution.
- Section 3 fallback string is exact — no adjacent-industry substitution.
- No "what this means for the deal" / "recommendation" section.

### view:phase4.compete-block

Rendered only when competitive-intelligence skill is called.

Sections (whatever competitive-intelligence skill returns):
- Competitor profiles
- Service-by-service comparison
- Battle cards
- Defensive posture
- Win/loss precedent

If competitive-intelligence reports thin intel on a specific competitor, surface the gap as-is. No web-search or training-data fallback.

CP covers four dimensions — direct rivals, DIY, competing priorities, status quo. competitive-intelligence skill covers direct rivals; the other three are flagged as one-line notes from Scorecard signals.

**Simple-tier no-competitor case:**
```
No named competitors in Competitive Info — competitive monitoring not triggered at Simple tier.
```

### view:phase4.provenance-note

```
Source: account-context skill + solutions-search skill + competitive-intelligence skill. Their internal data sources and methods are their own.
```

---

## Phase 5 Templates

### view:phase5.layer-a-table

```
| 评估项 / Element | 得分 / Score | Priority | 关联状态 / Relationship | 数据源 / Source |
|---|---|---|---|---|
```

Each row from M.17 layer_a_rows. Column rules:

- **评估项:** full label, e.g., "E — Economic Buyer".
- **得分:** `[score]/[max] = **[%]%**` (percentage bolded).
- **Priority:** `P0` / `P1` / `P2` / `—` (— for 100% elements with `⚠️` flag, since they are at the score ceiling but flagged for related-element fragility).
- **关联状态:** text from M.14 `related_status_label` per its rules. Examples:
  - `关联 I (67%) 偏低`
  - `关联 CH (33%) 处于 At Risk`
  - `⚠️ 看似达标 — 关联 I (67%) 偏低`
  - `关联项均 ≥ 80%` (only when an element appears for other reasons; otherwise the row is skipped from Layer A entirely)
  - `—` (no related elements with material score gap)
- **数据源:** specific Scorecard row numbers / field names per V.0.1. Never bare "Scorecard".

Scope per M.1.1; show all in-scope elements except those at 100% with all related elements ≥ 80%.

No directional language ("拖累 / 受...拖累 / depends on / blocks / upstream / downstream") may appear in any cell.

### view:phase5.layer-b-cards

For each P0/P1 element from M.17 layer_b_cards:

```
### [element_label] ([score]%)

[_Diagnostic Evidence: [diagnostic_evidence_text]_  ← only when M.17 sets it]

**根本原因 / Root Cause:**
[root_cause_text — 2–4 sentences, causal not descriptive. Inference content tagged with ⚠️ per V.0.1. References to related elements must be fact-only — no directional verbs.]
```

Skip P2 elements.

**Diagnostic Evidence rendering:** one italic line stating the specific contradiction/anomaly. NOT a bulleted list of Nos. When M.17 returns null, omit the line entirely.

**Root Cause rendering:** never include "Impact if Unresolved" or "Recommendations" subsections.

### view:phase5.stakeholder-profiling

Source status declared at top of section per V.0.2 pattern:

- `Source: contact-profiling skill` (when skill returned output)
- `⚠️ contact-profiling skill not yet available — generating role-archetype profile from LLM internal knowledge as fallback.` (fallback)
- `Source: cxo-personas skill — [persona file name]` (when EB is C-level and the skill returned a persona)
- `⚠️ cxo-personas skill not available — proceeding without CxO overlay.` (when EB is C-level but the skill is not connected)

When `no_persona_mode = true` (EB not identified), source status renders as:
- `Source: LLM 内部知识 / role archetypes — Scorecard 中未提供 EB 职位，按角色原型生成。`

Then the body:

```
### a. 客户接触人画像 / Contact Profiling
[tone, priorities, cultural considerations, rapport-building approach, question-sequencing principles — content from contact-profiling skill or fallback]

### b. CxO Persona  ← ONLY when eb_identity is C-level AND cxo-personas skill returned a persona
[CxO-specific overlay: decision levers, technical priorities, etc.]
```

**Role labeling discipline (HARD — applies to every contact rendered in this section):**

- Every contact carries exactly one MEDDPICC role tag: **EB**, **Champion**, **Champion candidate**, or **Coach**. No other role label is permitted in user-facing output.
- Contacts surfaced from Remarks / Notes / 备注 free-text are normalized per **M.7 free-text rules** before rendering. Do NOT render raw labels like "Supporter" / "Sponsor" / "Stakeholder" — substitute the M.7 `meddpicc_classification`.
- When citing the original Scorecard text, keep the raw word inside the quote, then append the M.7-derived classification in parentheses. Example:
  - ✅ `Sheet1 备注："确认了 supporter 是 David"（按 MEDDPICC 框架归类为 Coach: Champion 元素 33% 未达验证门槛）`
  - ❌ `David: Supporter`
- A `Champion candidate` tag is permitted ONLY when M.7's gating logic produced it. Otherwise default to `Coach`.

**Do NOT** include a "What This Means for Your Next Move" section. Tactical implications appear as `view:phase5.persona-traits-applied` blocks inside the question section.

### view:phase5.persona-traits-applied

Rendered for each P0/P1 element when `no_persona_mode = false`:

```
> Persona traits applied:
> (1) [trait — citing specific Persona attribute, e.g., "CTO prioritizes latency, QPS, ROAS over generic ROI — use quantitative metrics in M-related questions."]
> (2) [trait]
> (3) [trait]  ← optional third
```

Skipped entirely when `no_persona_mode = true`.

### view:phase5.verification-questions

For each P0/P1 element from M.19 output:

```
### [element_label] ([score]%)

[view:phase5.persona-traits-applied — if applicable]

**Q1.** [main_question]
- *Purpose:* [purpose]
- *Expected insights:* [expected_insights]
- *Follow-ups:* [follow_up_suggestions]

**Q2.** [main_question — only when budget allows]
- *Purpose:* ...
- *Expected insights:* ...
- *Follow-ups:* ...

**Q3.** [main_question — only for P0 elements with three justified angles]
- *Purpose:* ...
- *Expected insights:* ...
- *Follow-ups:* ...
```

**Optional EB hint at the end of Phase 5 (only when `no_persona_mode = true`):**

After all P0/P1 verification questions are rendered, append exactly this single line at the end of Phase 5 output:

```
ℹ️ 如果你能补充一下 EB 的角色（如 CFO / VP），下次问题会更精准。
```

Rules for the optional hint:
- Render only when `no_persona_mode = true`. Skip entirely when EB is identified.
- One line only — no header, no bullet list, no follow-up prompt.
- Does NOT pause execution. Phase 5 still ends with standard "确认进入 Phase 6" gating.
- The user's response (if any) is treated as input to the next conversation turn — if they provide a job title, M.18 picks it up via "prior user input in current conversation" path on subsequent calls.

P2 elements skipped (monitoring only). Total ≤ 12 main questions enforced by M.19; each P0 element generates 2–3 main, each P1 element generates 2 main.

**Do NOT prepend** any "⚠️ No EB identified — questions are not persona-tuned" warning. The hint above is the only acknowledgment of degraded mode in user-facing output.

---

## Phase 6 Templates

### view:phase6.action-plan

```
# [Opportunity Name] — Action Plan

[view:shared.warning-banner — when rollback_recommended = true]

## 1. Current Position
[score display per M.20.1] | Current Stage: [current_stage] ([alignment_result — for Rollback, append "→ [rollback_target]"]) | [current_stage] completion [aggregate]%

_Context — unfinished exit criteria feeding the strategies below:_
- **Prior stage ([prior_stage_name])**: [element] = [score]% — [specific gap]
- **Current stage ([current_stage_name])**: [element] = [score]% — [specific gap]
- [additional bullets, max 5]

---

## 2. Winning Strategies (背景叙事)

For each Strategy from `winning_strategies`:

```
**S1** — [strategy.title] · [strategy.target]
_Rationale: [strategy.rationale]_
```

Render as 1 line per strategy plus 1 italic rationale line below. No nested weekly action details inside the strategy block.

---

## 3. Weekly Plan (执行视角)

For each `{week, actions[]}` entry from `weekly_actions`:

```
### Week N（本周）  ← "本周" tag only on the soonest week (W1)
- [action.description]  ［[strategy_tags joined with · ]］
- [...]
```

Render rules:
- Each action is one bullet line, no nested sub-bullets.
- Strategy tags appear in trailing brackets, multi-tag separated by `·` (e.g., `[S1·S2·S3]`).
- Tag-only ASCII brackets — no badge styling, no color.
- Each action stays under `ACTION_DESCRIPTION_MAX_CHARS`.
- Weeks with no action are skipped.
- Calendar-event de-duplication has already been applied in Model layer (M.20). View does not re-merge or re-split.

[when M.21 set extended horizon:]
_Horizon extended to [weekly_horizon] weeks because [horizon_extension_reason]._

---

## 4. Key Success Metrics (30-day targets)

For each metric from `success_metrics`:

```
- ✅ [Element] ≥ [threshold]% — [verification condition: objective, observable]  ［[strategy_tag][, optional · 来源 W[N]–W[M]]］
```

Strategy tag uses the single id (e.g., `S1`); optional `source_week` field appends as `· 来源 W3–W5` to trace which weekly actions feed this metric.
```

**Render constraints (per M.20):**
- Action-first weekly view (samples in M.20). Same-calendar-event actions are merged once with multi-tag, never duplicated across strategies.
- Each action ≤ 100 chars.
- No "Immediate Next Step" footer — W1 first action covers it.
- No 🔴🟠🟡 priority tags — W-numbering carries time semantics.
- Score display matches Phase 2 exactly.
- Strategy 1 targets the Primary Blocker (per M.20 rule 3).
- Number of Strategies = number of Metrics = number of Phase 2 30-day targets (≤ 3).

---

## Phase 7 Templates

### view:phase7.save-path-prompt

```
报告要存到哪里？直接回车使用当前目录，或指定一个路径（例如 `~/Desktop`、`~/Documents/OP-Reports/`）。

Where should the report be saved? Press Enter for current directory, or specify a path (e.g., `~/Desktop`, `~/Documents/OP-Reports/`).
```

### view:phase7.delivery-confirmation

```
✅ Reading report generated: [absolute file path]

Sections rendered:
- Header + Rollback Banner ([shown / omitted])
- Phase 2 Deal Assessment ([alignment_result])
- Phase 3 Exit Criteria ([N] rows, [M] stages)
- Phase 4 Market & Competitive ([full / Simple-tier lite / omitted])
- Phase 5 Element Gap ([P0_count] P0 + [P1_count] P1 cards)
- Phase 5 Stakeholder Profiling ([N] stakeholders)
- Phase 5 Verification Questions ([N] questions across [M] elements)
- Phase 6 Action Plan ([N] strategies, [W_count] weekly actions)

Open the file in a browser to view. For PDF or Word copies, reply "导出 PDF" or "导出 Word".

_Model snapshot stored at `~/.dali/opportunity-progression/snapshots/{filename}.json` (machine-only; no user action needed)._
```

For Path B (jumped from earlier than Phase 6), explicitly list omitted sections.

For naming fallback (Customer slug instead of Opportunity slug), append a one-line note.

The Model snapshot footnote is appended as the last line. If snapshot write failed (M.24 surfaces error), replace footnote with: `_Model snapshot save failed: {error_message}._`

### view:phase7.export-confirmation

```
✅ [PDF / Word] exported: [absolute file path]
```

---

## V.HTML.0 — HTML Render Pipeline

```
M.22 → data dict → Jinja2 template (templates/opportunity-progression.html.j2) → M.23 → write HTML
```

Jinja2 settings: `autoescape=True`, `trim_blocks=True`, `lstrip_blocks=True`. Reference: `examples/render_sample.py`.

**Visual system (fixed, no deviation):**
- MD3 palette, primary `#6750A4`.
- Tailwind via CDN; Material Symbols icons.
- Max-width `6xl`; cards `28px` radius; pill badges `100px` radius.
- Stepper with circle nodes.
- **Typography:** Latin → Amazon Ember; CJK → 思源黑体 SC (Source Han Sans SC). HTML/PDF: `font-family` chain in template + `Noto Sans SC` Google Fonts fallback. Silent system-default fallback if unavailable.

## V.PDF.0 — PDF Export Format Rules

Invoke `examples/export_pdf.py` with the rendered HTML.

- Engine: headless Chromium via Playwright (preferred) or system Chrome fallback. NOT WeasyPrint — Tailwind CDN's JIT engine requires a real browser.
- Save next to the HTML with `.pdf` extension.
- On-demand only. Never produce PDF automatically alongside HTML.

## V.DOCX.0 — Word Export Format Rules

Invoke `examples/export_docx.py` with the same JSON data dict that fed the HTML render.

- Engine: `python-docx`. Builds Word document directly from data contract. Does NOT parse HTML.
- Word does not attempt pixel-for-pixel fidelity with HTML.
- Typography: Normal style `w:rFonts` — `ascii/hAnsi = Amazon Ember`, `eastAsia/cs = Source Han Sans SC`.
- Save next to the HTML with `.docx` extension.
- On-demand only.

**Schema sync rule (HARD):** any change to Phase 7 sections requires coordinated update to ALL of: `templates/opportunity-progression.html.j2`, `examples/sample-data.json`, `examples/export_docx.py`, `examples/render_sample.py` verification, `examples/README.md` schema note. Missing any one creates HTML/Word drift.
