═══════════════════════════════════════════════════════════
PROCEDURE 2 — MODEL
═══════════════════════════════════════════════════════════

Nodes tagged `[shared: phase X, phase Y]` compute once per session and are reused. Control's pre-run notes trigger early so downstream phases reuse the cached value.

## M.0 Data Attribution Rule

Every value Model produces carries a `source` field. View renders source alongside value (V.0.1).

`source` types:
- **Scorecard cell** — sheet / row / column / field. Example: `{score: 13, source: "Scorecard / MEDDPICC / row 12 / E final statement / weight 5"}`.
- **Computed from Model node** — name producing node. Example: `{value: 67, source: "M.5 (E score 13) / M.5 (E max 13)"}`.
- **Reserved interface** — interface name + connection status.
- **Tagged inference** — `⚠️ Industry/role-based inference, not from Scorecard or connected interfaces`.

Aggregating nodes propagate input sources into output. Never describe an element as "low/high/strong/weak" without its actual percentage and source.

## M.1 Constants

### M.1.1 Tier Scope Table

| Tier | In-Scope Elements | Notes |
|---|---|---|
| Commodity | — | Skill exits at Phase 1 |
| Simple (EDDIC) | I, E, DC, DP, CP | M, P, CH not assessed |
| Strategic (MEDDPICC) | M, E, DC, DP, P, I, CH, CP | All 8 elements |

### M.1.2 MEDDPICC V3 Element Weights

Reference weights, used only when cell formulas are unreadable. If formulas are present, trust the formulas.

| Element | Per-statement weights | Element max |
|---|---|---|
| I | 4 / 4 / 4 | 12 |
| M | 3 / 1 / 4 / 5 | 13 |
| E | 4 / 4 / 5 | 13 |
| CH | 4 / 4 / 4 | 12 |
| CP | 4 / 4 / 4 | 12 |
| DC | 3 / 3 / 3 / 4 | 13 |
| DP | 4 / 4 / 5 | 13 |
| P | 4 / 4 / 4 | 12 |
| **MEDDPICC total** | | **100** |
| **EDDIC total** (I + E + DC + DP + CP) | | **63** |

### M.1.3 Stage → Element Mapping

Source: `aws-sales-stages.md`. Use **MEDDPICC Stage Mapping** when `tier = Strategic`, **EDDIC Stage Mapping** when `tier = Simple`. Granularity: one element per row; multi-element exit criteria → multi-row.

### M.1.4 Element Relationship Matrix

Source: `meddpicc-framework.md`. Use **MEDDPICC Element Relationship Matrix** when `tier = Strategic`, **EDDIC Element Relationship Matrix** when `tier = Simple`. The matrix is **symmetric and undirected** — it lists which elements share content scope, not which element causes or precedes another. Used by M.14 to populate the Layer A "关联状态 / Relationship" column.

### M.1.5 Classification Hard Constraints

- Never downgrade Strategic → Simple.
- Upgrades always allowed (Commodity → Simple → Strategic), one-way.
- When unsure between two adjacent tiers, pick the higher one.

### M.1.6 Symbol Vocabulary

| Symbol | Meaning | Where used |
|---|---|---|
| ✅ | On Track / Aligned / OK | Status, alignment, metric verification |
| ⚠️ | Caution / not-corroborated / not-connected / inferred | Risk flag, interface status, inference tag, 100%-with-fragile-related-element flag |
| 🔴 | Blocking / At Risk | Exit-criterion status, At Risk priority |
| 🚀 | Ready for advancement | Phase 2 Advancement Ready |
| ℹ️ | Informational / strengthening recommended | Phase 2 Aligned — Strengthening Recommended |
| — | No related elements with material score gap | Layer A Relationship column when N/A |

In Layer A, `⚠️` against a 100% element means the element is at its score ceiling but at least one related element is below 80% — i.e., the score is not corroborated by related-element strength. Single source of truth for symbols.

## M.2 Tunable Parameters

| Parameter | Default | Used in |
|---|---|---|
| `STATUS_ON_TRACK` | element % ≥ 80% | M.15 row status |
| `STATUS_NEEDS_IMPROVEMENT` | 60% ≤ element % < 80% | M.15 row status |
| `STATUS_AT_RISK` | element % < 60% | M.15 row status |
| `HEALTH_FOUNDATION_INCOMPLETE_PRIOR` | prior stage < 80% | M.9 |
| `HEALTH_FOUNDATION_INCOMPLETE_CURRENT` | current stage exit criteria < 60% | M.9 |
| `HEALTH_STALLED_EB` | EB < 50% | M.9 |
| `HEALTH_STALLED_CHAMPION` | Champion < 40% (Strategic only) | M.9 |
| `HEALTH_OFF_TRACK_TOTAL` | Total % < 70% | M.9 |
| `HEALTH_ON_PLAN_TOTAL` | Total % ≥ 70% | M.9 |
| `HEALTH_ON_PLAN_EB` | EB ≥ 70% | M.9 |
| `HEALTH_ON_PLAN_CHAMPION` | Champion ≥ 60% (Strategic only) | M.9 |
| `MEDDPICC_RISK_EB_THRESHOLD` | EB < 70% | M.16 |
| `MEDDPICC_RISK_CHAMPION_THRESHOLD` | Champion < 60% (Strategic only) | M.16 |
| `ALIGNMENT_PASS2_ROLLBACK` | current-stage aggregate completion < 60% | M.12 |
| `ALIGNMENT_PASS2_STRENGTHEN` | 60% ≤ current-stage aggregate completion < 80% | M.12 |
| `ALIGNMENT_PASS2_ALIGNED` | 80% ≤ current-stage aggregate completion < 100% | M.12 |
| `ALIGNMENT_PASS2_ADVANCEMENT_READY` | current-stage aggregate completion = 100% | M.12 |
| `ALIGNMENT_PASS1_QUAL_STAKEHOLDER_STRATEGIC` | EB% + Champion% < 100% (Qualified, Strategic) | M.12 |
| `ALIGNMENT_PASS1_QUAL_STAKEHOLDER_SIMPLE` | EB% < 100% (Qualified, Simple) | M.12 |
| `PROGRESSION_GATE_TV_BV_TOTAL` | 65 | M.12 (rows 1 & 2 of Stage Progression Gates — Total Score min) |
| `PROGRESSION_GATE_TV_BV_I_PCT` | 100% | M.12 (I element minimum) |
| `PROGRESSION_GATE_TV_BV_CH_PCT` | 100% | M.12 (CH element minimum) |
| `PROGRESSION_GATE_TV_BV_E_S1_REQUIRED` | true (E statement 1 = Yes required) | M.12 |
| `PROGRESSION_GATE_COMMIT_TOTAL` | 80 | M.12 (row 3 — Total Score min) |
| `PROGRESSION_GATE_COMMIT_E_PCT` | 100% | M.12 (row 3 — E element minimum) |
| `TARGETS_BELOW_THRESHOLD` | element < 80% (eligible for 30-day target) | M.10 |
| `TARGETS_MAX_RATE_PER_WEEK` | 15–20% improvement per element per week | M.10 |
| `TARGETS_MAX_COUNT` | ≤ 3 headline targets | M.10 |
| `QUESTION_BUDGET_TOTAL` | ≤ 12 main questions across all P0/P1 | M.19 |
| `QUESTION_BUDGET_P0` | P0 (score < 60%): 2–3 main + up to 2 follow-ups each | M.19 |
| `QUESTION_BUDGET_P1` | P1 (60% ≤ score < 80%): 2 main + 1 follow-up each | M.19 |
| `QUESTION_BUDGET_P2` | P2 (≥ 80%): skipped (monitoring only) | M.19 |
| `WEEKLY_HORIZON_DEFAULT` | 4 weeks | M.21 |
| `WEEKLY_HORIZON_EXTENDED` | 6–8 weeks (when rollback + current-stage aggregate < 30%) | M.21 |
| `WEEKLY_HORIZON_EXTEND_TRIGGER` | rollback_recommended AND current-stage aggregate < 30% | M.21 |
| `ACTION_DESCRIPTION_MAX_CHARS` | 100 chars per W-action | M.20 / V phase 6 |

## M.3 Scorecard Parser

**Inputs:** uploaded `.xlsx` file, `tier` from Phase 1.

**Outputs:** raw extracted data, `language` (auto-detected), `scorecard_type` ∈ {`EDDIC`, `MEDDPICC`}, parse status.

**Rules:**
- Required sheets: opportunity basic info sheet + at least one scoring sheet. Missing → parse error.
- Auto-detect which scoring sheet has real (non-default) scores.
- For paired pre/post columns (课前/课后, Pre-Class/After-Class): use the **课后 / After-Class / Post** column as the single source of truth for all scoring. Pre-class data is NOT retained for downstream analysis (including Phase 5 Diagnostic Evidence). If only one column exists, use it.
- Auto-detect `language`:
  - TC sheet → `zh-TW`
  - SC sheet → `zh-CN`
  - English sheet → `en`
- Auto-detect `scorecard_type` from the Basic Info sheet's Total Score cell:
  - Cell label contains "EDDIC" or denominator is `/63` → `EDDIC`
  - Denominator is `/100` (with no EDDIC marker) → `MEDDPICC`
  - Ambiguous → fall back to inspecting which scoring sheets carry data; an EDDIC Scorecard's scoring sheets cover only I / E / DC / DP / CP statements; a MEDDPICC sheet covers all 8.
- Format invalid → return parse error with message `"The file format does not meet requirements. Please use the latest Scorecard template for your tier."` (rendered by V).

## M.3-Auto Scorecard Inference

**Purpose:** When the user picks Phase 1A Option C, generate inferred Scorecard answers from already-available context in the current Dali session. Replaces M.3 / M.5 / M.6 for the inferred path.

**Critical scope distinction (HARD):** opportunity-progression does NOT actively invoke other Dali skills here. M.3-Auto reads only what is already present in the Dali agent's conversation context — i.e., outputs from skills the user happened to run earlier in the same session. If a relevant skill never ran, its data is simply absent — M.3-Auto defaults the corresponding statements to `No` with confidence `low` rather than triggering a skill call.

**Inputs (4 strict tiers, in priority order):**

1. **Tier 1 — User-provided opportunity basics** (from Phase 1A-Auto Step 1, mandatory):
   - `customer_name`
   - `opportunity_name`
   - `current_stage`
   - `opportunity_description` (optional, free-form, helps inference)

2. **Tier 2 — User-confirmed context relevance** (from Phase 1A-Auto Step 2, mandatory):
   - List of Dali skills the user explicitly confirms ran earlier in this session AND were for this same customer / opportunity.
   - Each entry: `{skill_name, customer_in_skill, opportunity_in_skill, relevance ∈ {confirmed_current | assumed_current | unrelated}}`.

3. **Tier 3 — Conversation context** (Dali agent's session memory):
   - Whatever skill outputs are visible to the LLM from earlier in this conversation. Examples: `account-context`, `contact-profiling`, `bttroc`, `engagement-plan`, `post-meeting-report`, `business-insight`, `competitive-intelligence`, `solutions-search`.
   - These are NOT actively invoked. M.3-Auto reads what's already in context.
   - Each output is filtered through the Tier 2 relevance map: only `confirmed_current` outputs are used as positive evidence; `assumed_current` are used with `confidence` capped at `med`; `unrelated` outputs are ignored.

4. **Tier 4 — `tier` from Phase 1** (governs in-scope element list).

**Phase 4 delegated skills are NOT inputs here.** Phase 4 happens after Phase 2; M.3-Auto runs at Phase 1A. Any data those skills would provide is excluded.

**Outputs:**
- `inferred_statements` — for each in-scope element, for each statement: `{statement_text, inferred_answer ∈ {Yes, No, Unknown}, source, source_tier ∈ {1, 2, 3, 4}, source_relevance ∈ {confirmed_current, assumed_current, user_input, default_no}, confidence ∈ {high, med, low}}`
- `element_scores` — derived from inferred statements using same per-statement weights as M.5 (M.1.2 reference table)
- `total_score`, `total_max`, `total_percent` — derived same as M.6
- `inference_confidence` — `{overall: low|med|high, per_element: map, statement_count_by_tier: {tier_1, tier_2, tier_3_confirmed, tier_3_assumed, default_no}}`
- `context_used` — list of skill names actually contributing positive evidence (for snapshot audit)
- `language` — defaulted to `zh-CN` unless user input clearly indicates otherwise
- `scorecard_type` — derived from `tier`: Strategic → MEDDPICC, Simple → EDDIC

**Inference rules (HARD — no fabrication):**

1. **Evidence-first, not training-data-first.** For each MEDDPICC / EDDIC statement, the inference engine asks: "is there explicit evidence in the available inputs (Tier 1-3) that supports a Yes answer?"
   - **Strong evidence** (e.g., post-meeting-report quote, named contact in contact-profiling) → `inferred_answer = Yes`, `confidence = high`.
   - **Indirect support** (e.g., role inferred from org chart but no contact record) → `inferred_answer = No`, `confidence = med`, source explicitly notes the gap.
   - **No evidence** → `inferred_answer = No` (default), `confidence = low`, source = `"无足够信息推断"`.
   - **Training-data inference is FORBIDDEN.** Do NOT use general MEDDPICC knowledge or industry conventions to fill gaps. The output must be defensible against a "where did you get this from" challenge.

2. **Tier-aware confidence cap:**
   - `Tier 3 with relevance = confirmed_current` → can produce `confidence = high`.
   - `Tier 3 with relevance = assumed_current` → confidence capped at `med` (because customer/opportunity match is assumed but not confirmed).
   - `Tier 3 with relevance = unrelated` → ignored entirely (does not contribute to any inference).
   - `Tier 1 user input` → can produce `confidence = high` for descriptive statements, `med` for evaluative ones.
   - `Tier 4 (tier alone)` → never enough for a Yes inference.

3. **Never assert specific named facts the inputs don't contain.** No invented Champion names, no invented commitments, no fabricated metric values. If a statement requires asserting "Champion is named X" without a source, default to `No` + `confidence = low` + source `"无相关 contact 记录"`.

4. **Source attribution per V.0.1.** Every statement carries:
   - `source` — naming the originating input (e.g., `"contact-profiling output (confirmed current): contact 'David' has influence_score = 4"`, `"user opportunity description"`, `"无足够信息推断"`)
   - `source_tier` — which Tier the evidence came from
   - `source_relevance` — confirmed/assumed/user_input/default_no

5. **Per-element confidence rollup:**
   - All statements `high` → element `high`.
   - Any statement `low` → element `low`.
   - Otherwise → element `med`.

6. **Overall confidence:**
   - All elements `high` → overall `high`.
   - All elements ≥ `med` → overall `med`.
   - Any element `low` → overall `low`.

**Standing flag:** writes `inference_confidence` and `context_used` to Session State; subsequent phases render the V.0.7 banner.

**Audit / re-run:** the full `inferred_statements` array (with per-statement source / source_tier / source_relevance / confidence) is persisted in M.24 Model snapshot (sub-key `M.3-Auto.inferred_statements`).

## M.4 Tier Match Validation

**Inputs:** `tier` (from Phase 1), `scorecard_type` (from M.3).

**Outputs:** match status, optional user-resolution outcome.

**Rules:**

| Phase 1 `tier` | `scorecard_type` | Outcome |
|---|---|---|
| Simple | EDDIC | Matched → proceed |
| Strategic | MEDDPICC | Matched → proceed |
| Simple | MEDDPICC | Mismatch (lenient) → render prompt; on user confirm, proceed with EDDIC scope only (M/P/CH ignored). No re-upload required. M.6 falls back to manual computation per its rule table. |
| Strategic | EDDIC | Mismatch (strict) → render prompt with two options: (A) downgrade `tier` to Simple, proceed with EDDIC; (B) request fresh MEDDPICC upload, re-run M.3. WAIT for user choice. |

## M.5 Element Score Computation

**Inputs:** parsed Scorecard sheet, `tier`.

**Outputs:** for each in-scope element: `{score, max, percent, source}`.

**Rules:**
- Each row in the scoring sheet = one evaluation statement with: Category, Element, Statement, Applies (Yes/No), Score (numeric).
- Per-statement maximum is **NOT fixed at 5**. Read weight from the cell formula (e.g., `IF(E7="Yes",4,0)` → weight = 4). Weights vary 1–5 across statements.
- For each in-scope element (per M.1.1):
  1. For each statement: read weight from formula; if cell has a plain numeric score, weight equals that number when answer = Yes; infer from M.1.2 weights if ambiguous.
  2. `Element Score = Σ (weight | answer = Yes)`
  3. `Element Max = Σ (all statement weights)`
  4. `Element % = Element Score / Element Max × 100`
- If formulas unreadable AND M.1.2 reference weights cannot be applied → flag to user (parse error).

**Non-scope data retention (Simple tier only):** if Scorecard contains M / P / CH despite Simple classification:
- Retain raw values in Session State as `out_of_scope_elements{}` for Phase 5 / Phase 6 narrative use.
- Do NOT include in Total Score (M.6) or per-element analysis (M.17).
- Phase 2 footer line is rendered (see V phase 2 footer rule).

## M.6 Total Score Computation

**Inputs:** element scores from M.5, `tier`, `scorecard_type` from M.3, Basic Info Score-After cell.

**Outputs:** `{total_score, total_max, total_percent, source}`.

**Rules — source of truth selected by (Scorecard type, Tier):**

| Scorecard type | Tier | Total Score source | Display |
|---|---|---|---|
| MEDDPICC | Strategic | Basic Info `Score-After (/100)` cell | `[Score]/100` |
| EDDIC | Simple | Basic Info `EDDIC Score-After (/63)` cell | `EDDIC [Score]/63 = [Z]%` |
| MEDDPICC | Simple (after lenient downgrade in M.4) | Computed: `score_I + score_E + score_DC + score_DP + score_CP`; max = sum of those 5 element max | `EDDIC [Score]/63 = [Z]%`. Append `(ref: MEDDPICC Basic Info = [W]/100 — EDDIC analysis does not use this)` in italics. |
| EDDIC | Strategic | n/a — blocked by M.4 strict mismatch path | n/a |

**Consistency anomaly:** set `consistency_anomaly = true` and surface to V if any of:
- Required fields (Stage, Total Score, element scores) are missing or unreadable.
- For MEDDPICC + Strategic: Basic Info Score-After does not reconcile with per-element sum (rounding tolerance).
- For EDDIC + Simple: `EDDIC Score-After (/63)` cell value ≠ `score_I + score_E + score_DC + score_DP + score_CP`.

## M.7 Role Terminology Normalization

**Rules — column-level role labels (Scorecard headers, structured fields):**
- Map "Sponsor" / "Stakeholder" / "Supporter" → MEDDPICC role framework. Only **Economic Buyer (EB)** and **Champion** are key MEDDPICC roles; everyone else is a **Coach**.
- "CO" (legacy abbreviation for Competition) → treat as synonym of **CP**. Emit CP in all downstream output regardless of input label.

**Rules — free-text role mentions (Remarks, Notes, 备注 columns, Sheet1 free-form fields):**

When parsing free-text fields anywhere in the Scorecard, scan for non-MEDDPICC role nouns ("supporter" / "sponsor" / "stakeholder" / "支持者" / "赞助者" / "联络人" used as role labels) and produce a **normalization record** for downstream phases:

```
{
  raw_label: "supporter",
  raw_text: "确认了 supporter 是 David",
  contact_name: "David",                          # extracted name if present
  meddpicc_classification: "Coach" | "Champion candidate" | null,
  classification_basis: text explaining the reasoning
}
```

**Classification logic (HARD):**

1. Default classification → `Coach` (the safe assumption — anyone identified by the customer as "supportive" is at minimum a Coach).
2. Upgrade to `Champion candidate` only if **all** of the following hold:
   - Champion element ≥ 60% (Strategic tier) AND
   - The Champion-element first statement ("Champion has power and influence") = Yes AND
   - The Champion-element second statement ("Champion provides valuable intel") = Yes
3. **Never** classify a Remarks-mentioned contact as `Champion` outright — Champion-the-role requires verification beyond a single Remarks reference. Even when both gating statements are Yes, the label is `Champion candidate` until Phase 5 root-cause analysis confirms.

**Downstream rendering rules (apply uniformly across Phase 5 / Phase 6 / Phase 7):**

- Never emit "Supporter" / "Sponsor" / "Stakeholder" as a role label in user-facing output. Substitute with the `meddpicc_classification` value (`Coach` or `Champion candidate`).
- When citing the source quote (e.g., in Layer B Diagnostic Evidence), retain the original word in the quote — but immediately follow with `({contact_name} 按 MEDDPICC 框架归类为 {meddpicc_classification}: {classification_basis})`.
- Stakeholder Profiling tables list contacts under their MEDDPICC classification column, not the raw label.
- Remarks-mentioned contacts whose Champion element scores indicate `Coach` are listed in Stakeholder Profiling with a `Coach` tag and a one-line note: "客户口头识别为内部联系人; Champion 元素分 [X]% 未达验证门槛, 当前归类为 Coach".

**Source:** This rule reflects MEDDPICC core role discipline — only EB and Champion are key roles; "Supporter" is not a MEDDPICC concept and must be normalized at parse time.

## M.8 Competitive Info Extraction

**Inputs:** Competitive Info sheet (if present).

**Outputs:**
- Named competitors list
- EB Job Title (used by M.18 EB Identity Resolution)
- Customer Business Objective
- Potential Obstacles
- AWS Solutions

If sheet absent → all fields null; downstream phases handle absence (M.18 silently enters degraded mode for EB; Phase 4 conditional Compete-skill call).

## M.9 Deal Health Logic

**Inputs:** total %, EB %, Champion % (Strategic only), current stage exit-criteria aggregate, prior stage aggregate, `tier`.

**Output:** `health_state ∈ {Foundation Incomplete, Stalled, Off Track, On Plan}` plus gap-fragment strings citing specific elements/aggregates that triggered the state.

**Rules — evaluate in priority order; first match wins:**

1. **Foundation Incomplete:**
   - Generic: current-stage exit criteria < `HEALTH_FOUNDATION_INCOMPLETE_CURRENT` AND prior stage < `HEALTH_FOUNDATION_INCOMPLETE_PRIOR`.
   - Simple-tier-only Prospect threshold: `current_stage = Prospect` AND E = 0%.
2. **Stalled:**
   - Strategic: EB < `HEALTH_STALLED_EB` OR Champion < `HEALTH_STALLED_CHAMPION`.
   - Simple: EB < `HEALTH_STALLED_EB`.
3. **Off Track:** Total % < `HEALTH_OFF_TRACK_TOTAL` (no critical blocker from rules 1–2).
4. **On Plan:**
   - Strategic: Total % ≥ `HEALTH_ON_PLAN_TOTAL` AND EB ≥ `HEALTH_ON_PLAN_EB` AND Champion ≥ `HEALTH_ON_PLAN_CHAMPION`.
   - Simple: Total % ≥ `HEALTH_ON_PLAN_TOTAL` AND EB ≥ `HEALTH_ON_PLAN_EB`.

## M.10 30-Day Targets Generation

**Inputs:** in-scope element scores, current scores below `TARGETS_BELOW_THRESHOLD` (80%).

**Output:** ordered list (≤ `TARGETS_MAX_COUNT`) of `{element, target_percent, source}`.

**Rules:**
- Eligible element: in-scope AND current score < 80%.
- Target value: current + realistic 4-week improvement at `TARGETS_MAX_RATE_PER_WEEK`. Round to threshold breakpoints (60 / 70 / 80) when within reach.
- Order by Priority from M.14 (P0 → P1 → P2) descending; tiebreak by largest gap.
- Cap at 3.

Phase 6 (M.20) consumes this list verbatim — same elements, same thresholds.

## M.11 Stage Aggregation [shared: Phase 2, Phase 3, Phase 6]

**Inputs:** Scorecard "Completion %" column from "Opportunity Basic Information" sheet, in-scope criteria per `tier`.

**Output:** for each stage from Prospect through current stage: `{stage, completion_percent, source}`.

**Rules:**
- For each stage: `stage_completion = mean of in-scope exit-criterion Completion % values within that stage`, rounded to nearest integer.
- The Completion % column is authoritative — do NOT recompute from element scores.

Cached after first computation; Phase 3 and Phase 6 reuse.

## M.12 Stage Alignment

**Inputs:** `current_stage`, EB %, Champion %, current-stage aggregate from M.11, `tier`.

**Output:** `{result, rollback_target, rollback_reasons[]}`.

**Rules — three-gate evaluation (Pass 1 ≡ Stakeholder Gate; Pass 2 ≡ Exit Criteria Gate; Pass 3 ≡ Stage Progression Gate. Model-internal terminology — view layer renders gate names only, never "Pass 1 / Pass 2 / Pass 3"):**

**Pass 1 — Stakeholder Gate (only when `current_stage = Qualified`):**
- Strategic: `EB% + Champion% < ALIGNMENT_PASS1_QUAL_STAKEHOLDER_STRATEGIC` (sum < 100) → Pass 1 triggered.
- Simple: `EB% < ALIGNMENT_PASS1_QUAL_STAKEHOLDER_SIMPLE` (< 100) → Pass 1 triggered.
- Pass 1 triggered → `result = Rollback Recommended`, `rollback_target = Prospect`. Continue to Pass 2 to optionally add a second reason.
- Not applicable (stage ≠ Qualified) → skip Pass 1.

**Pass 2 — Exit Criteria Gate (current-stage exit-criteria completeness):**

| Aggregate | Result |
|---|---|
| < `ALIGNMENT_PASS2_ROLLBACK` | Rollback Recommended (target via recursive lookup — see below) |
| `ALIGNMENT_PASS2_STRENGTHEN` ≤ aggregate < `ALIGNMENT_PASS2_ALIGNED` | Aligned — Strengthening Recommended |
| `ALIGNMENT_PASS2_ALIGNED` ≤ aggregate < `ALIGNMENT_PASS2_ADVANCEMENT_READY` | Aligned |
| = `ALIGNMENT_PASS2_ADVANCEMENT_READY` | Advancement Ready |

**Pass 2 rollback target — recursive lookup:** when Pass 2 triggers Rollback Recommended, do NOT default to the immediately prior stage. Instead, walk **backward through the stage chain** (Tech Validation → Qualified → Prospect; Business Validation → Tech Validation → Qualified → Prospect; etc.) and pick the first stage whose own aggregate ≥ `ALIGNMENT_PASS2_ALIGNED` (80%).

```
def find_rollback_target(current_stage):
    for stage in stages_before(current_stage)[::-1]:   # nearest-first
        if M.11_aggregate(stage) >= ALIGNMENT_PASS2_ALIGNED:
            return stage
    return "Prospect"   # 漏斗起点; if even Prospect < 80%, rollback target is Prospect itself
```

Rationale: the immediately prior stage may itself be incomplete, in which case rolling back there is misleading — the opportunity has not actually completed any prior stage. Walk back until finding a stage with substantive completion, or return Prospect as the funnel entry point. The same `ALIGNMENT_PASS2_ALIGNED` threshold (80%) is reused so users see one consistent "completed" bar across the skill.

**Result consolidation:**
- Pass 1 triggered AND Pass 2 triggered → single `Rollback Recommended` citing both reasons. `rollback_target = Prospect` (Pass 1 takes precedence as earlier-stage rollback).
- Pass 1 triggered, Pass 2 not → `Rollback Recommended`, `rollback_target = Prospect`.
- Pass 1 not triggered → use Pass 2 outcome directly (with rollback target from recursive lookup).

**Simple-tier exception:** if `current_stage = Prospect` AND E = 0%, do NOT trigger rollback (Prospect is the starting stage). Handled by M.9 Foundation Incomplete; M.12 returns Pass 2 outcome.

**Pass 3 — Stage Progression Gate (Strategic tier only; reference: `aws-sales-stages.md` "Stage Progression Gates" section):**

Evaluates whether the opportunity, as it stands at `current_stage`, is qualified to advance to the next stage. Always evaluated in addition to Pass 1 and Pass 2; produces a separate boolean `progression_gate_passed` and a `progression_gate_target` (next stage name). At Simple tier, Pass 3 is skipped — set `progression_gate_passed = null`, `progression_gate_target = null`.

| `current_stage` | Target stage | Required conditions (all must be satisfied) |
|---|---|---|
| `Qualified` | `Tech Validation` | Total ≥ `PROGRESSION_GATE_TV_BV_TOTAL` AND E statement 1 = Yes AND I% ≥ `PROGRESSION_GATE_TV_BV_I_PCT` AND CH% ≥ `PROGRESSION_GATE_TV_BV_CH_PCT` |
| `Tech Validation` | `Business Validation` | Same as above (rows share the same gate per policy) |
| `Business Validation` | `Committed` | Total ≥ `PROGRESSION_GATE_COMMIT_TOTAL` AND E% ≥ `PROGRESSION_GATE_COMMIT_E_PCT` |
| `Prospect` | `Qualified` | Pass 3 not defined for this transition — set `progression_gate_passed = null`, `progression_gate_target = "Qualified"` (rendered as "未设进阶门槛" in view) |
| `Committed` / `Closed/Launched` | (terminal) | Pass 3 not applicable — set both fields to `null` |

**E statement 1 source:** Read from MEDDPICC Scorecard's Economic Buyer element row 1 ("已与 Economic Buyer 接触并提及了该项目" / "I have engaged with the Economic Buyer and discussed the initiative"). Value = Yes/No. Available from M.5's per-statement raw data.

**Pass 3 behavior — diagnostic only:**
- A failed Pass 3 does NOT set `rollback_recommended = true`. It does NOT trigger rollback by itself.
- A failed Pass 3 produces an advisory message in the alignment card: "推进到 [target_stage] 的进阶门槛未满足: [specific failed condition(s)]".
- If `current_stage = Tech Validation` (Pacvue's case) and Pass 2 also triggers rollback, the alignment card surfaces both: rollback advice from Pass 2, plus progression-gate diagnosis pointing forward.

**Output additions to M.12:**
- `progression_gate_passed` ∈ {`true`, `false`, `null`}
- `progression_gate_target` ∈ stage name or `null`
- `progression_gate_failed_conditions` = list of strings naming each unmet condition (e.g., `["Total 67 < 65 阈值 — 实际已达标，无此项"]` not included; only failures); empty list when `progression_gate_passed = true`

## M.13 Alignment Flags

**Output written to Session State:**
- `alignment_result` ∈ {`Aligned`, `Aligned — Strengthening Recommended`, `Rollback Recommended`, `Advancement Ready`}
- `rollback_recommended` = `true` if Pass 1 or Pass 2 triggered rollback; else `false`
- `rollback_target` = target stage when `rollback_recommended = true`; else `null`
- `rollback_reasons` = list of triggered conditions, written in sales-readable business language per **V.0.6** (e.g., `["Tech Validation 两条核心退出标准合计完成度只有 15%"]`, `["Qualified 阶段 EB 与 Champion 接触合计 98%，EB 实质未接触"]`)
- `progression_gate_passed` ∈ {`true`, `false`, `null`} — from Pass 3
- `progression_gate_target` ∈ stage name or `null` — from Pass 3
- `progression_gate_failed_conditions` = list of unmet conditions (empty when passed) — from Pass 3

Used by: Phase 3 stage-progression line, Phase 6 banner trigger, Phase 7 report banner, V.0.3 Standing Warning Banner.

## M.14 Element Relationship Status [shared: Phase 2, Phase 5]

**Inputs:** in-scope element scores, Element Relationship Matrix per `tier` (M.1.4).

**Output:**
- `primary_blocker` = `{element, score, rationale_text, source}`.
- `relationship_rows` = for each in-scope element: `{element, score_percent, priority, related_elements[], related_status_label, source}`.

**Rules — Priority assignment (fact-only, by score threshold):**
- `P0` — element % < 60% (At Risk).
- `P1` — 60% ≤ element % < 80% (Needs Improvement).
- `P2` — 80% ≤ element % < 100% (monitoring only — no Layer B card).
- `100%` — at score ceiling. Receives a `⚠️ 看似达标` flag in `related_status_label` if any related element scores < 80%; receives `—` and is **skipped from Layer A** if all related elements score ≥ 80%.

**Rules — `related_status_label` text per element:**
- For each in-scope element, list its related elements per M.1.4 with their scores.
- Append a fact-only summary of the lowest related-element score:
  - If any related element < 60% → `关联 [Element] ([%]) 处于 At Risk`
  - Else if any related element 60–80% → `关联 [Element] ([%]) 偏低`
  - Else (all related ≥ 80%) → `关联项均 ≥ 80%`
- For 100%-score elements with at least one related element < 80%, prefix with `⚠️ 看似达标 — `.
- No directional language ("拖累 / 受...拖累 / blocks / depends on / upstream / downstream") may appear anywhere in this output.

**Rules — Primary Blocker selection (fact-only):**
- Candidate set: all in-scope elements with priority `P0` first; if none, `P1`; if none, `P2`.
- Tiebreaker: lowest absolute score percentage.
- Secondary tiebreaker (when scores tied): element with the largest number of related elements scoring < 80%.

**Rules — `rationale_text` (HARD — specialization of V.0.6 for Primary Blocker):**

The `rationale_text` is what appears in the Phase 2 user-facing card next to the blocker element name. It MUST follow **V.0.6 User-Facing Language Rule** (no internal scoring jargon, no model node references, no academic caveats — see V.0.6 Section A for full forbidden list).

**Specialization beyond V.0.6: required structure (3 sentences, in this order):**

1. **What is missing concretely** — what business capability / artifact / commitment the customer has not yet given. Use specific nouns from the deal (e.g., "DSP 业务的 4 项基线指标", "EB 的口头价值确认", "法务/财务流程对齐"), not the element name.
2. **What it blocks** — what next step in the sales motion this gap prevents. Tie to the customer's deal mechanic, not to the scoring framework (e.g., "EB 无法对方案价值做出确认", "进入 Business Validation 缺少必要前置").
3. **Concrete consequence the sales rep can visualize** — describe the visible deal stall, NOT abstract sales-process labels. Use phrasing the rep would say in a Monday standup ("商机停在 Tech Validation 推不动", "EDP 谈判进不了下一轮", "下次 EBC 没东西可以汇报", "本季度 forecast 收不进来").

For full forbidden / allowed vocabulary, see V.0.6 Sections A–C. The full canonical example (positive form) is in V.0.6 Section F.

**Element field display rule:**

The `primary_blocker.element` field MUST contain only the element label — `[Code] — [Name]` (e.g., `M — Metrics`). Do NOT bake the score into this field. The view template renders `{element} · {score}` from the separate `score_pct` field. Avoid duplicating the percentage by including it in both `element` and `score`.

Cached after first computation; Phase 5 reuses.

## M.15 Exit Criteria Evaluation

**Inputs:** Scorecard exit criteria rows (Stage / Exit Criterion / Mapped Element), Scorecard Completion % column, element % from M.5, Remarks column, `tier`, in-scope elements per M.1.1.

**Output:** for each row: `{stage, exit_criterion, scorecard_completion_percent, mapped_element, element_percent, status, remarks_override_flag, source}`.

**Rules:**
- Use row-per-mapping granularity from M.1.3 (one element per row).
- Simple tier: skip rows mapped exclusively to out-of-scope elements (M, P, CH).
- Strategic tier: evaluate all rows.
- Row status driven by **mapped element %** (NOT Scorecard Completion %):
  - element % ≥ `STATUS_ON_TRACK` → `On Track` (✅)
  - `STATUS_NEEDS_IMPROVEMENT` ≤ element % < `STATUS_ON_TRACK` → `Needs Improvement` (⚠️)
  - element % < `STATUS_AT_RISK` → `At Risk` (🔴)
  - Remarks column has manual "At risk" flag → override status to `At Risk` regardless of element %, set `remarks_override_flag = true`.
- Scorecard Completion % column is retained for reporting (AE's self-assessment of progress) but does NOT drive status.

**Exit-criterion aggregate status (when one criterion has multiple rows):** lowest-status precedence.
- Any mapped element < 60% → exit-criterion is At Risk.
- Else any < 80% → Needs Improvement.
- Else On Track.

## M.16 Risk Bucketing

**Inputs:** M.15 row statuses, M.5 element scores, M.11 stage aggregates, current_stage, prior_stage, `tier`.

**Output:** three buckets, each a list of `{stage, element, finding, source}`:
- `foundation_risks` — prior stage exit criteria not met (lowest-status precedence At Risk).
- `progression_risks` — current stage exit criteria not met. When element score is high but Scorecard Completion % for the mapped exit criterion is far lower (or vice versa), include that contradiction inline as part of the finding text — do NOT spin a separate "contradictions" section.
- `meddpicc_risks`:
  - Strategic: EB < `MEDDPICC_RISK_EB_THRESHOLD` OR Champion < `MEDDPICC_RISK_CHAMPION_THRESHOLD`.
  - Simple: EB < `MEDDPICC_RISK_EB_THRESHOLD`.
  - When the same element also appears as root cause in Foundation or Progression bucket, reference once in MEDDPICC bucket and point back; do not re-list.

Element-level deep root-cause analysis is owned by M.17.

## M.17 Element Diagnostic

**Inputs:** in-scope element scores, M.14 priority + relationship labels, Scorecard Remarks, Potential Obstacles, Competitive Info, Phase 4 outputs (when Strategic).

**Output:**
- `layer_a_rows` — for each in-scope element where M.14 has assigned a priority of `P0` / `P1` / `P2` (i.e., scoring < 100%), AND for elements at 100% where M.14 has set `⚠️ 看似达标` (at least one related element < 80%): `{element_label, score_display, priority, related_status_label, source}`. Elements at 100% with all related elements ≥ 80% are skipped from Layer A.
- `layer_b_cards` — for each P0/P1 element: `{element, root_cause_text, diagnostic_evidence_text or null}`.

**Rules — Layer A priority:** assigned by M.14 from absolute score thresholds (P0 < 60%, P1 60–80%, P2 80–100%). M.17 consumes these directly — no re-derivation, no directional logic.

**Rules — Layer B Diagnostic Evidence inclusion (STRICT — include ONLY if at least one trigger):**
- **Cross-statement contradiction:** Yes statement logically conflicts with No statement in same or other element. Example: DC "EB confirmed AWS preference" = Yes while E "engaged with EB" = No.
- **Remarks-statement mismatch:** Remarks column says something contradicting statement scores. Example: Remarks says "found Champion" but CH statements scored 0.
- **Counter-intuitive No:** No on a statement that industry-standard practice would expect Yes at this stage.

**Do NOT include Diagnostic Evidence if:**
- It would just list which statements scored No (Scorecard restatement, no analytical value).
- All Nos point to same obvious fact (Root Cause paragraph already covers).
- User can read the same signal directly off the Scorecard without analytical assistance.

**Format:** when included, output as one italic line stating the specific contradiction/anomaly — NOT a bulleted list of Nos. Quote conflicting statements or reference Remarks cells. Use post-class ("课后") scored data only.

**Root Cause rules:**
- Causal ("why"), not descriptive ("what").
- 2–4 sentences.
- Draw from Scorecard Remarks, Potential Obstacles, Competitive Info, or tagged inference.
- If cause requires inference beyond Scorecard data, tag explicitly with ⚠️ inference tag per M.0.
- Cross-element contradictions surface here AND in Diagnostic Evidence (qualifies under cross-statement rule).
- Strategic tier: when Phase 4 competitive intel is relevant to root cause, weave in. If Phase 4 already flagged an element's score as fragile, reference rather than re-argue.
- Reference related elements by **fact, not direction** — e.g., "M and I are related elements per the matrix; both score below 80%, indicating shared treatment is needed". Never use "M is downstream of I", "I drives M", "M depends on I", or similar directional phrasing.
- Do NOT include "Impact if Unresolved" or "Recommendations" — those belong to Phase 6 (Action Plan).
- Specific source citations for "where" already in Layer A — do not duplicate in Root Cause.

## M.18 EB Identity Resolution

**Inputs:** Scorecard Competitive Info "EB Job Title" field (M.8 output), prior user input in current conversation.

**Output:** `eb_identity` (string or null), `no_persona_mode` (bool).

**EB identity sources (HARD — only these two):**
1. EB Job Title field in Scorecard Competitive Info sheet.
2. Explicit user input in current conversation (provided spontaneously, NOT prompted by the skill).

No other Scorecard fields infer EB. No training-data inference, no industry-convention guess.

**Resolution flow (silent — no user prompt):**
- Either source provides title → `eb_identity = title`, `no_persona_mode = false`.
- Neither source → `eb_identity = null`, `no_persona_mode = true`.

**No prompting:** M.18 NEVER renders a prompt and NEVER pauses for user input. If `eb_identity` cannot be resolved from the two hard sources, the skill silently enters degraded mode and continues. The user is not interrupted to "fill in" missing information.

**Optional EB hint at end of Phase 5:** when `no_persona_mode = true`, the verification-questions view appends a single optional hint line at the very end of Phase 5 output (see `view:phase5.verification-questions`). The hint is purely informational — it does NOT block, does NOT pause, and does NOT require a response.

**Downstream impact:** when `no_persona_mode = true`:
- Step 4 (`contact-profiling` + `cxo-personas` skill calls) is skipped.
- `view:phase5.stakeholder-profiling` falls back to LLM-internal-knowledge role archetypes (no EB-specific overlay).
- `view:phase5.persona-traits-applied` is omitted entirely.
- `view:phase5.verification-questions` uses generic phrasing without EB-role calibration.

## M.19 Question Generation

**Inputs:** P0/P1 elements from M.17 Layer A, `eb_identity`, `no_persona_mode`, Phase 4 industry terminology (when available), Opportunity Location.

**Output:** for each P0/P1 element: `{element, persona_traits_applied[], main_questions[], follow_up_questions[]}`.

**Rules:**

**Hard caps (per M.2):**
- Total budget across all P0/P1 elements ≤ `QUESTION_BUDGET_TOTAL` (12 main questions).
- Per element by priority (NOT by raw score — use M.14 priority):
  - **P0** (score < 60%, At Risk) → `QUESTION_BUDGET_P0`: **2–3 main** + up to 2 follow-ups each. The 2–3 main questions must target genuinely different angles (e.g., 不同 stakeholder 视角、不同维度的验证). If three angles cannot be justified, ship 2.
  - **P1** (60% ≤ score < 80%, Needs Improvement) → `QUESTION_BUDGET_P1`: **2 main** + up to 1 follow-up each.
  - **P2** (≥ 80%, monitoring only) → `QUESTION_BUDGET_P2`: **skipped**. Do NOT generate questions for P2 elements.
- If sum across all P0/P1 elements would exceed 12 main, drop the lowest-priority elements first. Within the same priority band, drop the element with the highest score (least urgent). Never split a 2-question allocation — drop or keep whole.

**Skip P2 elements** — monitoring-only; their score health does not require active verification at this cycle.

**De-duplication (MANDATORY):** before output, scan for overlap. Two questions targeting same information goal through different phrasing → collapse into one main + follow-ups. A question earns its slot only if it unlocks information others cannot.

**Persona-to-Question Mapping (when `no_persona_mode = false`):**
- For each element, populate `persona_traits_applied[]` with 2–3 specific traits from Stakeholder Profiling that shaped question design.
- Each main question's phrasing, vocabulary, and tone must reflect those traits.

**Degraded mode (when `no_persona_mode = true`):**
- `persona_traits_applied[]` empty.
- Generate questions from element gaps alone — no persona-shaped phrasing, no vocabulary references to specific EB role, no industry-specific tone calibration based on EB seniority.

**Each main question carries:**
- `purpose` (why ask)
- `expected_insights` (what surface)
- `follow_up_suggestions` (carry second-angle gathering without inflating main count)

**Tone:** conversational, non-threatening, naturally extracts MEDDPICC information. Strengthens AWS value positioning; do NOT expose competitive intelligence. Adapts to Opportunity Location culture.

## M.20 Phase 2-6 Consistency Rules

**Inputs:** Phase 2 outputs (`primary_blocker`, `30_day_targets`, score display), Phase 5 outputs, current Phase 3 unmet exit criteria.

**Output:** `winning_strategies` (list, ≤3, high-level), `weekly_actions` (list, grouped by week, action-first), `success_metrics` (list, ≤3, with strategy tags), all with binding constraints enforced.

**Rules (HARD — violation invalidates Phase 6):**

1. **Score display matches Phase 2 Section 2 exactly:**
   - Strategic: `[Score]/100`.
   - Simple: `EDDIC [Score]/63 = [Z]%`.
2. **Analytical stage matches Phase 2's reported stage.** Phase 2 advisories (rollback / advancement) do NOT reframe.
3. **Strategy 1 MUST target the Primary Blocker** named in Phase 2 Section 3. Order is locked.
4. **Key Success Metrics = expanded Phase 2 30-day targets:** same elements, same thresholds, same count (≤ 3). Add verification condition + Strategy tag. Do NOT introduce new elements or change thresholds.
5. **Metric count ≤ 3, aligned with Phase 2.** If Phase 2 listed 2 targets, Phase 6 produces 2 Strategies and 2 Metrics.

**Strategy generation (high-level overview only — no W-action details inside Strategy):**
- Number of Strategies = number of Key Success Metrics = number of Phase 2 30-day targets.
- Each Strategy maps 1:1 to one Phase 2 headline target (same underlying element).
- Each Strategy entry contains:
  - `id`: short tag like `S1`, `S2`, `S3` (used in weekly action `strategy_tags` field)
  - `title`: directional and action-oriented (e.g., "建立 EB 接触通道"), NOT descriptive (e.g., "Improve E score")
  - `target`: the Phase 2 30-day threshold (e.g., "M ≥ 60%")
  - `rationale`: one sentence citing BOTH (a) Deal Assessment reference (Primary Blocker / 30-day target) AND (b) specific unmet Phase 3 exit criterion.
- **Strategy block does NOT contain weekly actions.** Weekly actions live in the separate `weekly_actions` structure (action-first).

**Weekly action generation (action-first, calendar-event de-dup):**

Output structure: `weekly_actions = [{week: "W1", actions: [{description, owner, verification, strategy_tags: [S1, S3]}]}, ...]`.

- Each action ≤ `ACTION_DESCRIPTION_MAX_CHARS`.
- Each action carries `strategy_tags` — list of Strategy ids the action contributes to (one or many).
- Actions are listed in chronological order grouped by week. Weeks with no action are skipped.
- W1 actions verifiable within the week — no vague "gather information" or "align stakeholders".
- W1 includes an action whose description is an expanded version of Phase 2's "Immediate Action (This Week)" — same core action with added specificity.
- Later-week actions may carry dependencies — state explicitly in description ("depends on W1 outcome"), not implicit.

**Calendar-event de-duplication (SOFT rule):**

When generating weekly actions, before emitting two action entries that look like the same calendar event, check the following heuristic:

```
def is_same_calendar_event(action_a, action_b):
    return (
        action_a.week == action_b.week AND
        action_a.owner == action_b.owner AND
        actions describe the same physical event / deliverable
        (e.g., same meeting subject, same document, same call participants)
    )
```

If `is_same_calendar_event` evaluates true, **merge into a single action entry** with `strategy_tags` containing all involved Strategy ids. Examples:

- ✅ Merge: `W3 [S1] David 牵头三方会议升级 v2` + `W3 [S2] David 牵头三方会议验证推动力` + `W3 [S3] David 牵头三方会议确认 I 量化` → `W3 [S1·S2·S3] David 牵头三方会议，发布"业务成功指标 v2"` (same physical meeting, three strategies served simultaneously)
- ❌ Do NOT merge: `W3 [S1] 与 David 复盘基线表 v2` + `W3 [S2] 与 David 复盘三方会议反馈` (same week + same owner, but different agendas / deliverables — these are two separate 1-on-1s or one meeting with explicitly partitioned segments). When unsure, keep separate.

The rule is SOFT because LLM judgment is required to decide whether two descriptions are truly the same calendar event. The View renders whatever Model emits — Model is the authority on de-duplication, not the View.

**Metrics rules:**
- Threshold from Phase 2, not reinvented.
- Verification condition must be objective ("EB meeting held with v2 doc" / "量化指标 EB 口头确认"), not subjective ("alignment improved").
- Each metric carries `strategy_tag` (single Strategy id, since metric maps 1:1 to a Strategy).
- Optionally also carry `source_week` (e.g., "W4–W5") to trace which weeks' actions yield this metric's verification — helpful for retrospective review.

## M.21 Weekly Horizon Logic

**Inputs:** `rollback_recommended`, current-stage aggregate from M.11.

**Output:** `weekly_horizon` (integer 4–8), `horizon_extension_reason` (string or null).

**Rules:**
- Default: `WEEKLY_HORIZON_DEFAULT` (4 weeks).
- Extended to 6–8 weeks when `WEEKLY_HORIZON_EXTEND_TRIGGER` matches: `rollback_recommended = true` AND current-stage aggregate < 30%. State extension reason explicitly (V renders as italic note: "_Horizon extended to 6 weeks because Qualified foundation is at 22%._").

## M.22 Report Data Dict Assembly

**Inputs:** Session State, all phase outputs in context, `phases_completed`.

**Output:** structured data dict matching `examples/sample-data.json` contract.

**Top-level keys and source mappings:**

| Key | Source | When populated |
|---|---|---|
| `meta` | Phase 1B basic info | Always |
| `rollback_banner` | `rollback_recommended` + `rollback_reasons` | Only when `rollback_recommended = true`; otherwise omit key entirely |
| `phase2` | Phase 2 outputs (consolidated: deal health + stage alignment + progression gate) | If Phase 2 in `phases_completed` |
| `phase25` | DEPRECATED — kept for backward compatibility with legacy report templates. New reports populate everything under `phase2`. | Omit unless legacy template requires |
| `phase3` | M.15 rows + M.11 aggregation + M.16 risk buckets | If Phase 3 in `phases_completed` |
| `phase4` | Phase 4 three sections + Compete block. `show: false` only when Phase 4 was never reached (Commodity exit / Path-B jump to Phase 7). In a full-sequence run Phase 4 always runs — see Phase 4 HARD block; Compete block alone may be absent at Simple tier with no competitor | If Phase 4 in `phases_completed` |
| `phase5` | M.17 Layer A + Layer B + Stakeholder Profiling + M.19 questions | If Phase 5 in `phases_completed` |
| `phase6` | M.20 strategies + M.21 horizon + Metrics | If Phase 6 in `phases_completed` |

**Color tokens** (M3 semantic names — template maps to `--md-sys-color-*` variables; never hard-coded hex):
- Status / priority: `success`, `warning`, `error`, `primary`.
- Stakeholder tag pairs (`tag_bg` / `tag_fg`):
  - Champion / Supporter → `success-container` / `on-success-container`
  - Neutral → `warning-container` / `on-warning-container`
  - Skeptic / At Risk → `error-container` / `on-error-container`
  - Economic Buyer → `secondary-container` / `on-primary-container`
  - Coach → `surface-container-highest` / `on-surface-variant`

If a new category is needed, extend `:root` in template and reference by variable name — do not introduce hex inline.

## M.23 File Naming & Collision

**Inputs:** Opportunity Name (preferred) or Customer Name (fallback), save path, current date.

**Output:** absolute file path for the report.

**Rules:**
- Naming: `progression-report-[opportunity-name-slug]-[YYYYMMDD].html`.
- `opportunity-name-slug` from Opportunity Name field. Transform: lowercase, spaces → hyphens, Chinese characters preserved, strip path-unsafe characters (`/ \ : * ? " < > |`), truncate to 60 chars.
- Missing Opportunity Name → fall back to `progression-report-[customer-slug]-[YYYYMMDD].html` and note fallback in V delivery confirmation.
- Collision: append `-v2`, `-v3`, etc. if file exists.
- Save path: empty/Enter → current working directory; otherwise expand `~` and use provided path. Create directory if not exists.

## M.24 Model Snapshot Persistence (machine-readable)

**Purpose:** Persist a complete Model-layer snapshot of the skill session for downstream machine consumption — re-runs / diff comparison / external system handoff. NOT user-facing; never rendered by any view.

**Inputs:** complete Session State + all `M.x` outputs accumulated during the session, `phases_completed`.

**Output:** JSON file written to a fixed root directory, independent of the user-facing report path.

**Storage location (fixed, not user-configurable):**

```
~/.dali/opportunity-progression/snapshots/
```

The directory is created if it doesn't exist. This is a stable agent-level location separate from `~/Sales/{Customer}/` (where Phase 7 reports go). It is shared across all customers and opportunities.

**File naming (HARD):**

```
{customer-slug}__{opportunity-slug}__{YYYY-MM-DD-HHmm}.json
```

- `customer-slug` and `opportunity-slug` use the same slug transform as M.23 (lowercase, spaces → hyphens, Chinese preserved, path-unsafe characters stripped, truncated to 60 chars).
- `{YYYY-MM-DD-HHmm}` is the timestamp at write time, in local time.
- The double-underscore (`__`) separator distinguishes parts since slugs may contain hyphens.
- Example: `pacvue__beijing-dsp-ad-investment__2026-05-19-1430.json`
- Collision: if the same path exists (sub-minute re-run), append `-v2`, `-v3`, etc.

**Schema (HARD):**

```json
{
  "schema_version": "1.0",
  "metadata": {
    "session_id": "{ISO-8601 timestamp}-{customer-slug}-{opportunity-slug}",
    "skill_name": "opportunity-progression",
    "skill_version": "{value from skill frontmatter or 'unversioned'}",
    "report_date": "{YYYY-MM-DD}",
    "snapshot_time": "{ISO-8601 timestamp}",
    "customer_name": "{customer_name}",
    "opportunity_name": "{opportunity_name}",
    "tier": "Commodity | Simple | Strategic",
    "scorecard_type": "EDDIC | MEDDPICC | null",
    "scorecard_file_hash": "{sha256 of uploaded Scorecard if available, else null}",
    "language": "{zh-CN | zh-TW | en}",
    "scorecard_source": "upload | form | auto-inferred-accepted",
    "inference_confidence": {
      "overall": "high | med | low | null (if not auto-inferred)",
      "per_element": { "I": "high", "M": "low", "...": "..." }
    },
    "phases_completed": ["Phase 1", "Phase 1A", "Phase 1A-Auto (if applicable)", "Phase 1B (if applicable)", ...]
  },
  "session_state": {
    "alignment_result": "...",
    "rollback_recommended": true,
    "rollback_target": "...",
    "rollback_reasons": [...],
    "progression_gate_passed": false,
    "progression_gate_target": "...",
    "progression_gate_failed_conditions": [...],
    "eb_identity": null,
    "no_persona_mode": true,
    "phase7_path": "A | B"
  },
  "model_outputs": {
    "M.3_scorecard_parser": { ... },
    "M.3-Auto_scorecard_inference": { "inferred_statements": [...], "element_scores": {...}, "total_score": {...}, "inference_confidence": {...} },
    "M.4_tier_match_validation": { ... },
    "M.5_element_scores": {
      "I": { "score": ..., "max": ..., "percent": ..., "source": "..." },
      "M": { ... },
      "E": { ... },
      "DC": { ... },
      "DP": { ... },
      "P": { ... },
      "CH": { ... },
      "CP": { ... }
    },
    "M.6_total_score": { ... },
    "M.7_role_normalization": { "free_text_records": [...] },
    "M.8_competitive_info": { ... },
    "M.9_deal_health": { ... },
    "M.10_30_day_targets": [ ... ],
    "M.11_stage_aggregates": [ ... ],
    "M.12_stage_alignment": { ... },
    "M.13_alignment_flags": { ... },
    "M.14_relationship_status": {
      "primary_blocker": { ... },
      "relationship_rows": [ ... ]
    },
    "M.15_exit_criteria_evaluation": [ ... ],
    "M.16_risk_buckets": { "foundation_risks": [...], "progression_risks": [...], "meddpicc_risks": [...] },
    "M.17_element_diagnostic": { "layer_a_rows": [...], "layer_b_cards": [...] },
    "M.18_eb_identity_resolution": { ... },
    "M.19_question_generation": [ ... ],
    "M.20_consistency_rules": { "winning_strategies": [...], "weekly_actions": [...], "success_metrics": [...] },
    "M.21_weekly_horizon": { ... }
  }
}
```

**Field rules:**

- Every node entry MUST be the actual structured output of that node. If a node was not invoked in this session (e.g., Phase 4 skipped at Simple tier with no competitors), set the value to `null`.
- Source attribution (per M.0) MUST be preserved in every nested entry — `source` field carried verbatim.
- Internal scoring vocabulary (At Risk / P0 / 阈值 / etc.) IS allowed in this file — V.0.6 forbidden vocab does NOT apply, since this is machine-only data.
- `scorecard_file_hash` enables detecting whether the underlying Scorecard changed between runs (for diff). Computed if the original file path is available; `null` otherwise.

**Write behavior:**

- Phase 7 writes the snapshot once, at the same step as the report HTML write (Phase 7 Step 5 → expanded to also persist Model snapshot).
- File is written atomically (write to `*.tmp`, rename) to avoid partial writes on interrupt.
- No retry on failure — if write fails (disk full, permission), surface the error in the delivery confirmation but do NOT block report generation.
- The snapshot file is silent in user output. The delivery confirmation (Phase 7 view) MAY mention "Model snapshot stored" with the path as a one-liner footnote, but should NOT be the primary content.

**Read behavior (for future re-runs / diff):**

- M.24 produces the file. Reading it back is the responsibility of any future skill invocation that wants to consume historical snapshots.
- Naming convention guarantees: alphabetical sort within `{customer}/{opportunity}` groups gives chronological order.
- Future M.x extension (e.g., "M.25 Snapshot Diff") may use this file as input.

**Privacy / safety:**

- The snapshot may contain customer-identifying data (names, contacts, deal sizes). It is treated with same sensitivity as the rendered report.
- The directory `~/.dali/` is on the user's local machine; not synced anywhere by this skill.


