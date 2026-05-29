# Competitive Intelligence — Reference Data Index

> **Read this first.** This file routes the CI agent to the correct reference material.
> Source: copied from `knowledge/wiki/Compete/` + `knowledge/wiki/Battlecards/`.
> Last synced: 2026-05-18

---

## What's Here

```
references/
├── INDEX.md          ← YOU ARE HERE
├── compete/          ← per-vendor positioning pages
│   ├── AliCloud.md   — 阿里云全面竞争分析 (中国+海外)
│   ├── Azure.md      — Azure/21VCA-E 竞争分析 (含商务模型+1-pager)
│   └── Huawei.md     — 华为云竞争分析
└── battlecards/      ← scenario-based talk tracks
    ├── AWS-vs-Local-CSP-China.md   — 中国 CSP 本土对比 (韧性/隐私/网络/创新)
    ├── China-CSP-Overseas.md       — 中国 CSP 海外覆盖 (GCR外/ESG/关停史)
    ├── E2E-Data-Architecture.md    — 端到端数据架构对比 (Lake Formation vs MaxCompute)
    ├── FSI-Fraud-AI.md             — FSI 反欺诈 AI 对比 (MS/Google/中国CSP)
    └── GPU-Competitive.md          — GPU/AI 算力对比 (H200/H100/B200+定价)
```

---

## Official Vendor Documentation (competitor-side fact grounding)

Curated `compete/` and `battlecards/` pages carry the **AWS positioning and talk tracks**. Competitor-side *facts* that drift fast — current SLA, region/AZ counts, per-region service availability, published pricing, quotas, compliance certs, GA vs preview — must be grounded in the **competitor's own official documentation**, the peer of the AWS Documentation MCP (`aws_docs` / `aws_knowledge`).

| Competitor | Official documentation source | Access | Notes |
|------------|------------------------------|--------|-------|
| Azure | Microsoft Learn MCP — `https://learn.microsoft.com/api/mcp` | Remote MCP, no auth | True docs-search MCP; enabled in `mcp.json` |
| GCP | Gemini Cloud Assist MCP `https://geminicloudassist.googleapis.com` / docs `cloud.google.com/docs` | MCP needs GCP auth | Assist/ops-oriented; portal fallback |
| AliCloud | OpenAPI MCP Server / Documentation Center `alibabacloud.com/help` | MCP needs AccessKey | API-invocation MCP; portal fallback |
| Tencent Cloud | Per-product MCP `cloud.tencent.com/developer/mcp` / docs `intl.cloud.tencent.com/document` | Per-product / portal | No unified docs MCP |
| Oracle (OCI) | OCI/ADB MCP / docs `docs.oracle.com` | MCP needs OCI auth | DB/ops-oriented; portal fallback |

**Only Microsoft Learn** is a no-auth docs-search MCP equivalent to the AWS Documentation MCP. For the others, fall back to the official docs portal and cap confidence at **Thin**. Mark every competitor fact **vendor self-reported** with a **retrieval date**, and run pricing/benchmark claims through `rag-guardrails.md`. MCP wiring lives in `.kiro/settings/mcp.json`.

---

## Routing: "I need X — where do I look?"

| Need | Read |
|------|------|
| AliCloud positioning, pricing model, weaknesses | `compete/AliCloud.md` (+ AliCloud official docs for current facts) |
| Azure / 21Vianet positioning, EA dynamics | `compete/Azure.md` (+ Microsoft Learn MCP for current facts) |
| Huawei Cloud positioning, org model weaknesses | `compete/Huawei.md` |
| China local CSP vs AWS (sovereignty, resilience) | `battlecards/AWS-vs-Local-CSP-China.md` |
| Chinese CSP going overseas — why AWS wins | `battlecards/China-CSP-Overseas.md` |
| Data platform compete (Redshift/Glue vs MaxCompute) | `battlecards/E2E-Data-Architecture.md` |
| FSI fraud/financial-crime AI compete | `battlecards/FSI-Fraud-AI.md` |
| GPU/AI compute compete (NVIDIA instances, pricing) | `battlecards/GPU-Competitive.md` |
| Current competitor SLA / region / pricing / GA status | competitor official documentation source (table above) |

---

## Reading Order

1. **Read this INDEX.md** — identify which vendor(s) and scenario(s) match the user's request
2. **Read the relevant `compete/` page** — overall vendor positioning, strengths, weaknesses, pricing
3. **Read matching `battlecards/`** — scenario-specific depth, talk tracks, counter-tactics
4. **Synthesize** into the output format defined in `SKILL.md`

---

## Coverage Gaps (be honest about these)

The following competitors/scenarios have **no curated `compete/` page** yet. For the cloud vendors below, competitor-side *facts* can still be grounded in their **official documentation source** (see the table above), but there is no AWS positioning / talk track / compete-motion content here — so positioning still counts as a gap:

- **GCP / Google Cloud** — no curated page; facts via Gemini Cloud Assist MCP / `cloud.google.com/docs`
- **Oracle / OCI** — no curated page; facts via OCI docs `docs.oracle.com`
- **Tencent Cloud** — no curated page; facts via `intl.cloud.tencent.com/document`
- **Snowflake** — no curated page, no vendor-docs source wired
- **Databricks** — no curated page, no vendor-docs source wired
- **VMware / Broadcom** — no curated page, no vendor-docs source wired
- **OpenAI / Microsoft Copilot (standalone)** — partially covered in Azure.md; facts via Microsoft Learn MCP
- **CoreWeave / Lambda Labs / Nebius / Crusoe** — no curated page, no vendor-docs source wired

If the user requests compete analysis for a vendor not covered here, **state the gap explicitly** in Coverage Honesty. Grounding a competitor *fact* in that vendor's official docs is allowed and encouraged (labeled vendor self-reported + dated); fabricating AWS positioning or proof points is not.

---

## Sync & Maintenance

These files are copies from `knowledge/wiki/Compete/` and `knowledge/wiki/Battlecards/`.
When the knowledge base is updated, re-copy the affected files here.

To sync all:
```bash
cp knowledge/wiki/Compete/*.md Dali/skills/competitive-intelligence/references/compete/
cp knowledge/wiki/Battlecards/*.md Dali/skills/competitive-intelligence/references/battlecards/
```

---

*INDEX.md — last synced 2026-05-18*
