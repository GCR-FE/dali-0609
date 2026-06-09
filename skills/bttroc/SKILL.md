---
name: "bttroc"
description: >
  Turns strategic analysis + AWS solutions into a CXO-ready conversation script with value proposition.
  Use whenever sales asks about opportunities, what to pitch, how to position with an executive,
  "有什么机会", "能卖什么", "切入点", "怎么跟高管聊",
  or any hint of identifying where to sell — even if they just say "这个客户有机会吗".
user_locked: true
---

# BTTROC — Break Through The Resistance Of Change

## Execution Discipline

STOP. Read this entire skill file through Procedure 3 before executing any step.
Three procedures execute in strict order: Control → Record → View.
Skipping steps produces an ungrounded script that the AM cannot use in front of a CXO.
Within Control, all six reasoning steps (2.1–2.6) must complete before producing any output.

Hard rules:
- Do NOT write the conversation script until Step 2.4 (archetype diagnosis) is done
- Do NOT render HTML until Procedure 2 (Record) has written to disk and verified

---

## Philosophy

Executives do not buy technology. They decide whether to change, and if so, how fast and how safely. Every CXO sits on a fulcrum between the cost of acting and the cost of not acting. A great seller does not "pitch a solution" — they surface the pain the executive is already feeling, name it in their language, and offer a path forward that matches their personal risk appetite.

This skill is built on four truths from the Customer Business Insight methodology:
1. **Every business worry rolls up to four dimensions** — Revenue, Cost, Efficiency, Risk. If you cannot place the conversation on this compass, the executive will not feel it.
2. **Pain lives on the Business Model Canvas** — an external shock does not hit "the company," it hits specific blocks (a Channel collapses, a Key Resource becomes a liability, a Revenue Stream erodes). Naming the block makes the pain concrete.
3. **Executives behave in predictable archetypes** — Underestimator, Wait-and-see, Risk-averse, Path-unclear, Resistant. Each archetype has one right sales path. Mismatching the path kills the deal.

Your deliverable is not a pitch deck. It is a **single, stitched-together conversation** that an AM or SA can deliver in 3–5 minutes and use to earn the next meeting. The deliverable is named the **identified potential opportunity**.


## Procedure — Control / Record / View

Every run of this skill executes three stages, in this fixed order:

Procedure 1. **Control** — gather inputs, run the analysis steps, apply guardrails. Everything in the existing sections below (Upstream Dependencies, Scope Constraints, Internal Reasoning Process, Output Format, Handoff Block, Quality Standards) up through the analysis is part of Control.
Procedure 2. **Record** — write the complete unsummarized work product to a local markdown file. Mandatory. See "Procedure 2: Record Full Working Document" below.
Procedure 3. **View** — render the HTML/PDF deliverable from the saved record, with "see more detail" affordances back to the record. See "Procedure 3: View — DETERMINISTIC HTML → PDF" below.


## Procedure 1: Control

### Step 1: Inputs

Required Input：
1. **TOWS-driven Top 3 Strategic Initiatives** — the recommended moves, OR user's input on the opportunity details
2. Solutions 搜索结果 (from `solutions-search`)， if content not found in context, run it in the background before proceeding.
3. competitive intelligence 搜索结果 (from `competitive-intelligence`) if content not found in context, run it in the background before proceeding.
4. contact profile
   - name: Contact Profile (V2.0)
   - repo: GCR-FE/contact-profiling
   - schema: CntP_{Customer}_{Name}.md
   - name: Translator Module
   - path: contact-profiling/translator/v2-translator.md
   - required: false


### Step 2: Reasoning Process (六步构建法)

Rules:
- You **must** reason through all six steps before producing the output — skipping steps produces a weak, ungrounded script.
- If the archetype in Step 4 is **Resistant**, the output format changes — see the "Resistant Archetype Exception" under Output Format.

#### Step 2.1 — For each Top Strategic Initiatives.

From the **Top Strategic Initiatives**, pick the **single most important Strategic Initiative** for this run. Criteria in order:

1. Has a **clear AWS answer** in the **Solutions 搜索结果** (otherwise the conversation has no close — BTTROC requires that the chosen initiative has at least one Solutions 搜索结果 reference)
2. Aligns with the customer's **buying behavior** — e.g., if the customer is risk-averse, pick an initiative where the Solutions 搜索结果 reference is a POC / Immersion Day pathway

Then identify the **target CXO**:

- If the user named one, use it
- Otherwise, map the threat's dominant business dimension to the likely owner:
  - Revenue erosion → CRO / CMO / GM of affected BU
  - Cost escalation → CFO
  - Operational disruption → COO
  - Security / compliance exposure → CISO / General Counsel
  - Technology debt / capability gap → CIO / CTO
- If two dimensions are tied, pick the one the customer's buying behavior points to (top-down customer → CEO-adjacent role; bottom-up → functional head)

Internal artifact from Step 1 (reasoned, not printed):

```
Dominant Threat: [one sentence]
PESTLE / Porter Provenance: [factor name and score from the strategic initiative suggestion]
Target CXO: [role, and name if known]
Why This CXO: [one sentence on why the shock lands on this role's desk]
AWS Solution to Weave In: [named service or solution from the Solutions 搜索结果]
Solutions 搜索结果 Reference: [the specific reference customer from Solutions 搜索结果 that will appear in the closing sentence]
```

#### Step 2.2 — Map Impact to the Business Model Canvas

For the selected threat, identify the **affected BMC blocks** and describe the damage in the customer's own business language — no AWS services yet, no abstractions.

Produce this table:

| BMC Block | Current State (from the strategic initiative suggestion's BMC section) | Damage Caused by the Threat | Severity (H/M/L) |
|-----------|--------------------------------------|----------------------------|------------------|

Rules:

- Include **only** blocks that are materially affected — usually 2–4 blocks, never all nine
- "Current State" must come verbatim from the strategic initiative suggestion's BMC section (inherited from the BMC analysis in `business-insight`), not reinvented
- "Damage" must be a business consequence (revenue lost, margin compressed, customer churn, cycle time, compliance gap) — not a technology statement
- If the shock affects the **right side** of the canvas (Customer Segments / Value Prop / Channels / CR / Revenue), the story is about **Differentiation erosion** — losing the ability to capture value
- If the shock affects the **left side** (Key Partners / Activities / Resources / Cost Structure), the story is about **Cost Leadership erosion** — losing the ability to produce value efficiently
- Note which side dominates — this shapes the path selection in Step 4

#### Step 2.3 — Anticipate CXO Concerns Across Four Business Dimensions

For the target CXO, build the **4-dimension concern table** — this is the compass the executive is mentally using when you walk in.

| Business Dimension | Impact Level (H / M / L) | What the CXO Is Worrying About | Evidence from Upstream |
|--------------------|--------------------------|-------------------------------|------------------------|
| Revenue Growth (Top-Line) | | Will this help or hurt revenue? Any short-term risk to current revenue? | [SWOT / PESTLE / Porter ref] |
| Cost Reduction (Bottom-Line) | | What is the cost of acting? What is the cost of not acting? Hidden costs? | [SWOT / PESTLE / Porter ref] |
| Operational Efficiency | | Will solving this disrupt current operations? How much bandwidth is needed? | [SWOT / PESTLE / Porter ref] |
| Risk Management | | What are the risks of acting vs not acting? (compliance, customers, internal politics) | [SWOT / PESTLE / Porter ref] |

Rules:

- Every dimension must be filled in — even if the level is Low, state why
- At least **one** dimension should be High, otherwise the shock is not CXO-grade and the user should rerun Step 1 with a different threat
- The concerns must be written **in the CXO's voice** — first-person worry, not third-person description ("My board will ask me why we didn't see this coming" is right; "The board may raise questions" is wrong)

#### Step 2.4 — Diagnose CXO Behavior Archetype and Select the Path

Read the CXO's existing Contact Profile data or find the person's name and run skill contact-profiling then produce data about 行为风格 that can be used to determine one of five archetypes and select the matching path,

| Archetype | Behavior Pattern | Selected Path |
|-----------|------------------|---------------|
| Underestimator — "Not urgent," "We're fine for now" | Underestimates the cost of inaction | **Amplify the Pain** |
| Wait-and-see — "Let's see how the market moves first" | Afraid of being first, fears picking the wrong path | **Lower the Risk** |
| Risk-Averse — "What if it fails?" "Too much investment" | Sees value but fears direct risks of change | **Lower the Risk** |
| Path-Unclear — "Where do we start?" "How are you different from X?" | Knows the destination but not the route | **Hybrid: Lower the Risk first, then Amplify after proven success** |
| Resistant — "No budget," "My boss won't agree" | Underlying issues — trust, politics, past failure | **Pause — diagnose deeper first with three discovery questions** |

Rules:
- State the archetype explicitly and give the **evidence** for the diagnosis (a quote, a behavior pattern from buying behavior, Contact Profile V2.0 + Translator(purpose=bttroc-archetype-hint)— 拿到人格层 archetype 倾向 hint, or a reasoned inference — label inferences as inferences)


#### Step 2.5 — Build conversation based on Template - this is called the Identified Potential Opportunity

Use one of the two templates below, template A or template B. These templates come directly from the  Business Insight and and should be used as a basis for the conversation. Explain and breakdown, give enough details using business terminology.

##### Template A — Amplify the Pain

> [CXO Name], because of [PESTLE / Porter Factor from the strategic initiative suggestion], we are seeing a rapid shift in the market regarding [Business Shock in one phrase]. Industry leaders and your peers are proactively upgrading their capabilities to turn this disruption into an advantage. [BMC Block Message — one sentence naming the specific block and the damage from Step 2]. If we do not match this rapid shift, your business could face [Amplified Result — a widening gap in efficiency, customer churn, margin compression, compliance exposure, whichever fits]. Let us not just react to the market — let us transform this area to lead the disruption. The first move I would recommend is [AWS Solution from the Solutions 搜索结果, framed as a capability not a product SKU], and here is a customer in [same or adjacent industry] who did exactly this and [specific outcome from the Solutions 搜索结果 reference].

##### Template B — Lower the Risk

> [CXO Name], driven by [PESTLE / Porter Factor from the strategic initiative suggestion], the current [Business Shock in one phrase] is putting significant pressure on your [BMC Block Message — the specific block from Step 2], potentially leading to [Amplified Result — margin erosion, operational bottleneck, churn, whichever fits]. While inaction is not an option, we also want to avoid the risks of a massive, disruptive overhaul. Let us take a pragmatic, de-risked approach. We can validate the value by executing [Small Action — the Next-Step Asset from the Solutions 搜索结果: a POC, Immersion Day, Well-Architected Review, or scoped pilot] on [Small Scope — a specific workload / BU / process] within [Short Timeframe — 4–12 weeks depending on the asset]. This ensures zero disruption to your core operations and gives you tangible proof before scaling. [Reference Customer from the Solutions 搜索结果] did exactly this and reached [specific outcome], which is why I believe this path fits your situation.

Rules for filling:
- **Every bracket must be filled** — if a bracket cannot be filled from the required upstream inputs, name the gap and stop; do not fabricate content
-every data point written must have a (source).
- **Keep it to 6-8 sentences** — anything longer loses the executive
- use business terminology, instead of IT terminology, unless target person is CIO/CTO, but busienss terminology is must
- explain the initiative, break it down so there's enough depth


#### Step 2.6 — Package the Proof Pack and Next-Meeting Ask

Attach to the script the minimum set of artifacts the AM/SA needs to walk in with:

1. **Two or three reference customers** — pull directly from the **Solutions 搜索结果**, in order of match quality (Direct > Pattern > Displacement). For each: one-line "who they are," one-line "what they did with AWS," one-line "what it delivered."
2. **One architecture or asset link** — the single most relevant knowledge base path from the **Solutions 搜索结果**
3. **One "next-meeting ask"** — the concrete commitment you are asking the CXO to make. Scale it to the path:
   - Amplify → exec-to-exec briefing with an AWS leader, or a peer reference call
   - Lower the Risk → a 2-hour scoped workshop with the relevant LOB leader to define POC success criteria
   - Hybrid → the Lower-the-Risk workshop first, with the exec briefing as a follow-on milestone
4. **Watch-outs** — two to three things the AM/SA should listen for in the meeting that would change the path.
   - **Default (no Compete 分析结果 provided):** generic watch-outs grounded in the customer's buying behavior, timing pressure, and internal politics (examples: "if the CXO pushes back on the POC timeline, pivot to the 4-week Immersion Day scope"; "if the CXO names a budget freeze, move the ask to a joint whiteboarding session instead of a paid workshop").
   - **If Compete 分析结果 was provided as optional input:** pull the incumbent-specific watch-outs directly from its "Watch-outs and Traps" section so the conversation pre-empts the right incumbent-specific objections. Examples: "if the CXO says 'we have an Azure EA,' pivot to the coexist-and-erode reframe from the compete brief"; "if the CXO raises the Snowflake performance comparison, guide the benchmark per the compete brief's right-apple guidance"; "if the CXO asks about timeline, quote the Immersion Day as the 30-day milestone from the Solutions 搜索结果 next-step asset".

---







## Procedure 2: Record Full Working Document (mandatory)

Save the complete unsummarized work product as markdown to disk. The record is the audit trail and the authoritative source the View renders from.

### What to save
Everything produced during Procedure 1 Control:
- Every input received (full strategic initiative suggestion from `business-insight`, full Solutions 搜索结果 from `solutions-search`, optional `competitive-intelligence` brief, customer name, target CXO title)
- The full **Internal Reasoning Process (六步构建法)** scratchpad — every step the skill ran internally, including the four-dimension (Revenue / Cost / Efficiency / Risk) concern map, the BMC block-pain mapping, the archetype scoring, and the path-engine intermediate output


### Where to save

Default path: `~/Sales/{Customer}/`

Follows the workspace convention defined by the Orchestrator (Section 6). Skill creates the directory if missing at runtime.

### Filename convention

 `BTT_{Customer}_{CXOTitle}_{YYYY-MM-DD}.md`

Customer name uses Pinyin for Chinese companies; CXO title in lowercase shorthand (e.g., `BTT_Haier_cto_2026-05-12.md`).

### Order of operations

1. Generate the working document and the Handoff Block in memory.
2. Write both record files to disk. Verify each write succeeded.
3. Only after step 2 succeeds, render the View (HTML/PDF) by reading from the records for Procedure 3.

If any record save fails (permission denied, path not writable), stop. Do not render the View from in-memory state — the deliverable would have no audit trail.



## Procedure 3: View — DETERMINISTIC HTML → PDF

**REQUIRED: Load `templates/OUTPUT_REFERENCE.html` before generating any HTML output.**

**REQUIRED: Load `templates/render_bttroc.py`** before converting HTML to PDF.

Ships as **an HTML file that exports to PDF via headless Chrome (`--no-pdf-header-footer`)**:

```bash
python3 skills/bttroc/templates/render_bttroc.py <output.html> <output.pdf>
```

PDF is generated via headless Chrome with `--no-pdf-header-footer` flag. Do NOT use `window.print()` or browser Export PDF — the template includes its own fixed page footer.


### Output Content

#### 1. Header

#### 2. Identified Top Strategic Initiative

The single initiative selected in Step 2.1, presented with:
- Initiative name and TOWS cell (SO / WO / ST / WT)
- One-paragraph description of the initiative (what it does, what it targets)
- Stat chips: TOWS Cell, Threat Source (P5F or PESTLE score), Opportunity (score)
- Reasoning note: why this initiative was selected over the others

#### 3. Target CXO, Concerns, Archetype & Path

Present the target executive and their diagnosed state:
- CXO role, name (if known), buyer type
- 4-Dimension Concerns grid (Revenue / Cost / Efficiency / Risk) — each with impact level (H/M/L) and one-line worry in CXO's voice
- Diagnosed archetype (with evidence)
- Selected path (with visual ribbon showing all 4 options, selected one highlighted)
- Reasoning note: why this archetype and path

#### 4. CXO Conversation Script

The filled-in template from Template A or Template B, rendered as a 3-part script (Opening / Middle / Close) that the AM/SA can read aloud. No bullet points, no step labels, no bracketed placeholders.

If the path is **Hybrid (Path-Unclear)**, produce the Lower-the-Risk script first, then a two-paragraph "after proof" follow-on that escalates into Amplify-the-Pain messaging for the second meeting.

#### Reference: Proof Pack, Next-Meeting Ask & Watch-outs

- **Reference customers** — 2–3 entries (who they are / what they did with AWS / what it delivered)
- **Architecture / asset link** — the single most relevant knowledge base path
- **Next-meeting ask** — one concrete, scheduled commitment, scaled to the path
- **Watch-outs** — 3–6 things the AM/SA should listen for that would change the path (incorporating Compete 分析結果 watch-outs if available)





### Deterministic output — locked-in rules

**Every layer renders reasoning.** No layer ships without a `推理` element. If a reasoning line is missing from the source markdown, the skill stops and asks.


### Filename convention

- Markdown source: `BTTROC_{Customer}_{YYYY-MM-DD}.md`
- HTML deliverable: `BTTROC_{Customer}_{YYYY-MM-DD}.html`
- PDF export: `BTTROC_{Customer}_{YYYY-MM-DD}.pdf`

Customer name uses Pinyin for Chinese companies (e.g., `BTTROC_Haier_2026-05-10.html`).


---

## Quality Standards

- Every claim in the script must trace back to a specific upstream artifact (SWOT line, PESTLE/Porter factor, BMC block from the strategic initiative suggestion; reference customer from the Solutions 搜索结果)
- The causal chain must be intact — PESTLE/Porter → Shock → BMC Block → Consequence → Path → AWS Answer → Proof
- The target CXO's concerns must be written in their voice, not the seller's voice
- The reference customer must be real and pulled from the **Solutions 搜索结果**, or AWS Documentation — never fabricated
- The script length is 5–7 sentences
