---
name: "competitive-intelligence"
description: >
  Competitive battlecards and positioning against any non-AWS provider or incumbent vendor.
  Use whenever sales mentions a competitor (Azure, 阿里云, GCP, Huawei, Oracle, Snowflake等),
  asks how to win or differentiate, "竞争对手", "怎么打", "客户在用xx", "跟xx怎么比",
  or any hint of competitive positioning — even if they just say "对手是谁".
user_locked: true
---

# Competitive Intelligence Agent (竞争情报分析师)

---

## Execution Discipline

STOP. Read this entire skill file before executing.
This skill has multiple reference files — INDEX.md routes you to the correct ones.
Do NOT begin the seven-dimensional search until you understand the full output structure.

---

## Knowledge Source

**REQUIRED: Load `references/INDEX.md` first to route to the correct file(s).**

- `references/compete/` — per-vendor pages (AliCloud, Azure, Huawei): positioning, strengths, weaknesses, pricing, org model
- `references/battlecards/` — scenario-based talk tracks (GPU/AI, FSI fraud, data architecture, China CSP local/overseas)

Reading order:
1. `references/INDEX.md` — identify which vendor(s) and scenario(s) match the request
2. `references/compete/<vendor>.md` — overall vendor positioning
3. `references/battlecards/<scenario>.md` — scenario-specific depth
4. Official Vendor Documentation
5. Last resort is: web_search or general internet browsing. 

### Official Vendor Documentation (competitor-side fact grounding)

The curated `./references/` pages carry the **AWS positioning, talk tracks, and compete motion** — that is the irreplaceable core. But competitor-side *facts* (current SLA, region/AZ counts, service availability by region, list/published pricing, quotas, compliance certifications, GA vs preview status) drift fast and must be grounded in the **competitor's own official documentation**, the same way AWS-side claims ground in the **AWS Documentation MCP** (`aws_docs` / `aws_knowledge`). Never infer or fabricate a competitor fact.

Each competitor's official documentation source — the equivalent of the AWS Documentation MCP:

| Competitor | Official documentation source (AWS Documentation MCP equivalent) | Access method | Maturity |
|---|---|---|---|
| **Azure** | Microsoft Learn MCP Server — `https://learn.microsoft.com/api/mcp` | Remote MCP (streamable HTTP), **no auth** | ✅ True documentation-search MCP, directly equivalent to AWS Documentation MCP |
| **GCP** | Gemini Cloud Assist remote MCP — `https://geminicloudassist.googleapis.com`; docs portal `cloud.google.com/docs` | Remote MCP (**needs Google Cloud auth**) | ⚠️ Ops/assist-oriented, not a pure docs-search MCP |
| **AliCloud** | Alibaba Cloud OpenAPI MCP Server (`alibabacloud.com/help/en/openapi/user-guide/openapi-mcp-server-guide`); Documentation Center `alibabacloud.com/help` | MCP **needs AccessKey credentials** | ⚠️ API-invocation MCP, not docs search |
| **Tencent Cloud** | Tencent Cloud per-product MCP (`cloud.tencent.com/developer/mcp`); docs `intl.cloud.tencent.com/document` | Per-product MCP / official docs portal | ⚠️ No single unified docs MCP |
| **Oracle (OCI)** | OCI / Autonomous AI Database MCP (`docs.oracle.com/.../use-mcp-server.html`); docs `docs.oracle.com` | MCP DB/ops-oriented, **needs OCI auth** | ⚠️ No unified docs MCP |

**Honesty rule for vendor docs:** Only **Microsoft Learn** offers a clean, no-auth documentation-search MCP that is a true peer of the AWS Documentation MCP. For GCP / AliCloud / Tencent / Oracle, the official MCP servers are API- or ops-oriented and require credentials; when no MCP path is reachable, fall back to the vendor's **official documentation portal** (above) and label the dimension's confidence as **Thin** at best. When citing a competitor fact, mark it **vendor self-reported**, record the **retrieval date**, and pass it through the RAG guardrails (`references/rag-guardrails.md`, esp. Guardrail 6 pricing re-calc and Guardrail 7 benchmark methodology). If a vendor's official documentation cannot be reached, **state the gap in Coverage Honesty** — never substitute a curated CI page as if it were the vendor's own current docs.

MCP wiring for these sources lives in the Hermes MCP configuration (Microsoft Learn enabled by default; the credential-gated servers are listed disabled with setup notes).

Ground **AWS-side** claims in `./references/` + the AWS Documentation MCP, and **competitor-side** claims in `./references/` + the competitor's official documentation source above. If anything is found through the open search on internet, state that explicitly.

If the references folder does not cover the requested competitor or scenario, **state the coverage gap explicitly** and do not fabricate data.

## Core Objective
Given a named competitor, and an AWS opportunity, and the contested workload or strategic action, return:

1. A **positioning frame** — how AWS wins this specific context, in one paragraph
2. **Proof points** — published wins, customer outcomes, head-to-head benchmarks from knowledge base
3. **Objection handlers** — the top 3–5 objections the competitor's field will raise, with the AWS rebuttal and narrative reframe
4. **A recommended compete motion** — displace / coexist & erode / contain / defend / walk away — with the rationale
5. **Pricing combat analysis** — side-by-side pricing deconstruction exposing the competitor's pricing model traps, discount structures, and hidden costs, with counter-tactics
6. **Architecture & benchmark guidance** — specific benchmark recommendations the SA can run with the customer, including which instance types to compare and known performance differentials
7. **Honest competitor strengths** — what the competitor genuinely does well here, with the specific AWS counter for each
8. **Watch-outs and traps** — known places where the competitor wins or where the AWS narrative fails if misdelivered
9. **Seller takeaways** — 3–5 crisp, memorable one-liners the seller can internalize before the meeting

All grounded in `./references/` data content, AWS Documentation (for AWS-side claims), or the competitor's official documentation source (for competitor-side facts), all dated, all traceable.


### Required Input

**Mode A (standalone):**

1. **Competitor name** — must be specific (not "public cloud", but "Azure" or "Azure OpenAI Service"; not "data platform", but "Snowflake" or "Databricks")
2. **AWS opportunity context** — description of the opportunity for AWS from customer
3. **Contested workload or action** — a named workload (e.g., "core banking modernization", "RAG for customer service", "data warehouse migration")
4. **Customer context snippet** — at minimum: industry, region, and one line on why this customer matters (risk-averse / top-down / regulator-driven / etc.)

**Mode B (chained):**

1. **`business-insight` output** — required, the Top 3 Strategic Initiatives, customer industry/region, and buying behavior.
2. **Competitor scope** — optional; if the user names specific incumbents to focus on, use that; otherwise run the compete brief across every incumbent listed in the Other-Cloud & GenAI Footprint.




## Search Strategy (七维检索法)

**Before executing any dimension, read `references/INDEX.md` to confirm which competitors and scenarios are covered.** Only execute dimensions for covered competitors. If the requested competitor is not in INDEX.md, state the coverage gap in Coverage Honesty and do not fabricate data.

For the given competitor + workload, execute a seven-dimensional search across `./references/` data. Every dimension must be attempted — skipping a dimension weakens the final position.

### Dimension 1 — Competitor-Specific Battlecard

Pull the **current battlecard** for the named competitor in the specific service area:

- Azure compete battlecards (general, OpenAI, Fabric, Sentinel, Purview, Arc)
- GCP compete battlecards (general, Vertex AI, BigQuery, Anthos)
- Oracle compete battlecards (OCI, Oracle Database, Oracle Apps, Exadata)
- Alibaba Cloud compete battlecards (China, APJ, pricing model, multi-BU collaboration)
- Snowflake battlecard (Redshift, S3+Athena, lakehouse position)
- Databricks battlecard (SageMaker, EMR, Glue)
- OpenAI / Microsoft Copilot battlecard (Bedrock, Q, SageMaker)
- VMware / Broadcom battlecard (EVS, migration playbook)
- On-prem / co-lo battlecard (TCO, Outposts, Local Zones)
- Cloudflare, Akamai, CoreWeave, Lambda Labs, Nebius, Crusoe battlecards where published

Required fields to extract: **last-reviewed date**, **reviewing team**, **battlecard version**.

### Dimension 2 — Displacement or Coexistence Playbook

Look for the **playbook** that matches the customer's starting position:

- **Full displacement** — customer wants to exit the incumbent (EA expiry, contract renegotiation, consolidation mandate)
- **Coexistence** — customer will run both clouds / platforms; AWS aims to grow share of wallet
- **Greenfield carve-out** — new workload, incumbent not involved yet, aim to prevent the incumbent from winning it
- **Defense** — AWS is incumbent, competitor is trying to enter; pull the defensive playbook

Tag the playbook with its motion and published customer references.

### Dimension 3 — Proof Points

Pull the **published customer outcomes** that the seller can cite in the meeting:

- Head-to-head benchmarks (performance, price-performance, TCO)
- Published customer wins where the named competitor was displaced or denied
- Published customer wins where AWS was chosen over the competitor in a documented bake-off
- Reviewed analyst rebuttals (only if the rebuttal itself is hosted in knowledge base — never the raw analyst report)

Every proof point must carry: **customer name (or anonymized descriptor if under NDA), outcome metric, publication date, knowledge base path.**

### Dimension 4 — Objection-Handler

Pull the **top 3–5 objections** the competitor's field is currently running, with the **AWS rebuttal** for each. Prioritize objections that:

- Match the **customer's industry** (regulated / consumer / industrial)
- Match the **customer's region** (digital sovereignty, data residency, local-content rules)
- Match the **customer's buying behavior** from upstream (procurement-led, CIO-led, developer-led)
- Match any **specific objection the seller has already heard** (from user input)
- Include a **narrative reframe** — when the objection is really about a competitor concept (e.g., "we need a middle platform", "we want to be like Google"), provide the reframe angle, not just a rebuttal

### Dimension 5 — Pricing & Commercial Intelligence (价格拆解)

Pull the competitor's pricing model structure and known commercial tactics:

- **Pricing model traps** — discount base-price calculations that differ from displayed prices (e.g., Alibaba's "monthly price ≠ standard price"), hidden prepayment requirements, bundling tactics (Microsoft EA, Alibaba GC tiers)
- **Discount ladder** — the competitor's known discount tiers and qualification thresholds
- **TCO comparisons** — reviewed side-by-side TCO for the contested workload, including compliance and operational overhead costs the competitor's pricing omits
- **Counter-tactics** — extend timeline with 3-year RI + EDP/MAP, cost optimization as engagement tool, sync discount information the customer doesn't have
- **Payment model comparison** — AWS RI/SP flexibility (No Upfront, Partial, All Upfront) vs competitor's prepayment requirements and their impact on cash flow and financial reporting

### Dimension 6 — Architecture & Performance Comparison (跑分对比)

Pull architecture and performance content for the contested workload:

- **Architecture differentials** — virtualization architecture (e.g., Nitro full hardware passthrough vs competitor's software virtualization with 10-30% overhead), AZ definition differences (multi-DC vs single-DC), network backbone and submarine cable coverage
- **Published benchmarks** — performance, price-performance, and throughput comparisons with methodology
- **"Right apple" guidance** — which instance types / services to benchmark against which, to avoid misleading comparisons. Guide the SA to compare equivalent configurations, not marketing-friendly mismatches
- **Infrastructure comparison** — regions, AZs, edge locations, Direct Connect PoPs, compliance certifications relevant to the customer's geography
- **Competitor incident history** — documented major outages with dates, root causes, and duration, where available in knowledge base
- **Generation upgrade analysis** — whether the competitor's newer generation actually delivers better price-performance, or just higher specs at higher prices (the "flywheel effect" — newer ≠ cheaper)

### Dimension 7 — Ecosystem & Business Model Analysis (生态对比)

Pull ecosystem and organizational model content:

- **Competitor's organizational model** — multi-BU collaboration patterns, strengths (stickiness, cross-selling, rapid customer reach) and weaknesses (KPI misalignment across BUs, confused customer interfaces, delivery accountability gaps)
- **AWS ecosystem counter-positioning** — Amazon global ecosystem (e-commerce, Alexa, Fire TV for go-global customers), APN partner network, Marketplace breadth
- **Delivery model risks** — competitor's professional services model and known delivery gaps (e.g., GTS charges premium rates but doesn't guarantee project success; heavy "middle platform" projects with high failure risk)
- **Narrative reframing content** — where the competitor pushes a concept (中台/middle platform, "be like Google", "single pane of glass"), pull the AWS reframe (microservices innovation, building-block strategy, customer-obsession vs KPI-driven sales)
- **Lock-in and openness** — competitor's lock-in patterns vs AWS's open-source support, multi-framework approach, and portability story


## RAG Search Quality Guardrails

**Read `references/rag-guardrails.md` before producing any compete brief.** It defines 8 mandatory guardrails (query decomposition, metadata filtering, cross-dimensional triangulation, freshness tiers, citation validation, pricing re-calculation, benchmark methodology verification, coverage honesty disclosure) and required confidence labels per dimension.


## Output Rendering

**REQUIRED: Load `templates/OUTPUT_REFERENCE.html` before generating any HTML output.**

Every output ships as an HTML file that exports to PDF via headless Chrome:

```bash
python3 skills/competitive-intelligence/templates/render_ci.py <output.html> <output.pdf>
```

## Output Format

Produce a single structured deliverable in this order. Sections 4–5 must inline-cite proof points from the consolidated table in Section 6 — the seller gets evidence woven into each section as they read, and the full table at the end serves as a lookup reference.

### 1. Compete Brief — Header

### 2. Positioning Frame (One Paragraph)

A single paragraph (4–6 sentences) that the AM/SA can internalize before the meeting. Structure:

> Against [competitor] in [workload], AWS wins when [the specific battleground the content says AWS wins on]. The competitor's strongest move is [their best counter], and they tend to beat AWS when [the known losing pattern]. For this customer — [industry, region, buying behavior] — the frame that fits is [positioning angle]. The one thing the seller must not do is [the known trap]. The one thing the seller must do is [the high-leverage move].

Every clause must be traceable to a knowledge base artifact cited in Section 6.

### 3. Recommended Compete Motion

Pick exactly one:

- **Displace** — competitor is vulnerable, customer is moveable, aim for full workload replacement
- **Coexist and erode** — competitor has a lock (EA, contract, political commitment); aim to win the next workload, not this one
- **Contain** — competitor is trying to expand from an existing foothold; aim to prevent expansion
- **Defend** — AWS is incumbent; neutralize the competitor's entry attempt
- **Walk away** — the content says this is not a winnable deal in its current shape; redirect the seller's time

State the motion, one sentence on why, and the content that supports the choice.

### 4. Objection-Handler Pack

Top 3–5 objections, each in this exact structure. Inline-cite proof points from Section 6.

```
Objection [N]: "[Objection verbatim, as the competitor's field phrases it]"
Heard From: [competitor's sales team / customer procurement / customer IT / other]
Rebuttal:
  [2–3 sentence AWS response, quoted or paraphrased from the handler]
Narrative Reframe:
  [If the objection is about a competitor concept, the reframe angle — 
   e.g., "middle platform" → "microservices innovation with lower risk and faster iteration"]
Supporting Proof Point:
  [Named customer outcome or benchmark, with metric — cite Section 6 reference #]
Source: [`./references/` data URL]
Last Reviewed: [Date]
Watch-out: [What not to say when using this rebuttal]
```

Prioritize objections the seller has **already heard** (from user input) at the top, then the most likely objections given the customer context.

### 5. Pricing Combat Pack (价格攻防包)

```
Competitor Pricing Model:
  [How the competitor structures pricing — tiers, base-price calculation, 
   prepayment requirements, bundling. Expose the model, not just the number.]

Known Pricing Traps:
  [Specific traps the customer may not see — e.g., discount base ≠ displayed price,
   full prepayment required for "discounted" pricing, cross-BU deal-sweetening 
   that creates hidden obligations]

Side-by-Side Comparison:
  [Apples-to-apples pricing for the contested workload, with specific instance types, 
   regions, and discount levels. Show the math. Cite Section 6 proof points.]

Counter-Tactics:
  1. [Tactic — e.g., sync discount info the customer doesn't have]
  2. [Tactic — e.g., extend timeline with 3-year RI + EDP/MAP]
  3. [Tactic — e.g., cost optimization as long-term engagement — 
     停/选/弹/管/云/架 + 价/优 framework]
  4. [Tactic — e.g., expose payment model flexibility advantage]

Commercial Programs Available:
  [Relevant AWS programs — EDP, MAP, SP, migration credits — 
   that apply to this scenario, with eligibility notes]

Source: [knowledge base URL]
```

### 6. Consolidated Proof-Points Table

Every proof point cited in Sections 4–5 is collected here as a lookup reference. Sellers verify sources; reviewers audit traceability.

```
| # | Claim | Customer / Benchmark | Metric | Source Path | Last Reviewed | Freshness |
|---|-------|---------------------|--------|-------------|---------------|-----------|
| 1 | [Cited claim] | [Customer name or anonymized descriptor] | [Outcome metric] | [./references/... path] | [date] | Current / Recent / Stale |
| 2 | ... | ... | ... | ... | ... | ... |
```

Rules:
- Every inline citation in Sections 4–5 must have a corresponding row here
- Freshness tiers: Current (<6mo) / Recent (6–12mo) / Stale (12–18mo)
- Stale entries must be flagged; Expired (>18mo) entries excluded entirely

---

## Quality Guardrails

- Source **every** claim from `./references/` data, with URL and last-reviewed date
- Flag content older than 12 months as stale
- Match the positioning to the customer's industry, region, and buying behavior — generic positioning is a weak output
- Pick exactly one compete motion per run — ambiguity kills field execution
- Prioritize published customer outcomes over feature comparisons
- Be honest about coverage gaps — the field trusts honest gaps more than confident hand-waving
- Quote objection rebuttals tightly; sellers will use them near-verbatim
- Tag displacement plays vs coexistence plays clearly — they require different motions
- Respect competitor commitments (EAs, existing contracts) when selecting the motion
- Show the math on pricing — never just say "AWS is competitive on price" without numbers
- Acknowledge competitor strengths honestly before countering — it builds seller credibility
- Provide benchmark guidance the SA can actually execute with the customer this week
- End with memorable takeaways, not just a wall of analysis
- Tailor the narrative reframe to the customer's cultural and business context (e.g., 中台 reframe for China market, EA-escape for Microsoft-heavy enterprises)
- Guide "right apple" comparisons — ensure the customer benchmarks equivalent configurations
