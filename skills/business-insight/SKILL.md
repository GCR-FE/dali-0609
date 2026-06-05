---
name: "business-insight"
description: >
  BMC → Porter → PESTLE → SWOT/TOWS → Top Strategic Initiatives.
  Use whenever sales asks for strategic analysis, SWOT, business model breakdown,
  "帮我分析一下这个客户", "商业模式", "战略分析",
  or any need to understand a customer's business — even if they just say "分析一下".
user_locked: true
---

# Business Insight Agent


## Procedure — Control / Record / View

Every run of this skill executes three stages, in this fixed order:

Procedure 1. **Control** — gather inputs, run the analysis steps, apply guardrails. Everything in the existing sections below (Hard Rules, Execution Protocol, Quality Standards) up through the analysis is part of Control.
Procedure 2. **Record** — write the complete unsummarized work product to a local markdown file. Mandatory. See "Procedure 2: Record Full Working Document" below.
Procedure 3. **View** — render the HTML/PDF deliverable from the saved record, with "see more detail" affordances back to the record. See "Procedure 3: View — HTML → PDF" below.

If Record fails, stop. Do not render View from in-memory state.




---

## Execution Discipline

STOP. Read this entire skill file before executing.
Step 1 requires loading reference/bi.md — this is the core analytical process, not optional background.
Do NOT start research until bi.md is fully loaded and understood.

---

## Procedure 1: Control

### Step 1: Conduct research and gather information

**REQUIRED: Load `reference/bi.md` before any research begins.** This file IS the core analytical process — every prompt block must be executed in sequence. 
- Use bocha_web_search
- Use bocha_ai_search
- use agent-browser on baidu.com as search engine. 
- Invoke deep research and thinking using ultrathink

### Step 2: conduct full swot and tows analysis, and then rank the top 1-3 initiatives that company is likely to pursue as a conclusion. The swot/tows should be done based on the findings of bmc, pestle, and porter's five forces.


## Procedure 2: Record Full Working Document (mandatory)

Save the complete unsummarized work product as markdown to disk. The record is the audit trail and the authoritative source the View renders from.

### What to save

Everything produced during Procedure 1 Control

### Where to save

Default path: `~/Sales/{Customer}/`

Follows the workspace convention defined by the Orchestrator (Section 6). Skill creates the directory if missing at runtime.

### Filename convention

This skill produces **two record files per run**, both sharing the same prefix and customer date:

Filename `BI_{Customer}_{YYYY-MM-DD}.md` 

Customer name uses Pinyin for Chinese companies (e.g., `AA_Haier_2026-05-12.md`).


## Procedure 3: View — HTML → PDF

**REQUIRED: Load `assets/OUTPUT_REFERENCE.html` before generating any HTML output.**

Every Output produced by this skill ships as **an HTML file that auto-exports to PDF**. The HTML is the canonical rendering surface — no other renderer is used.

### Step 0: HTML 生成方式（强制）

**不允许从零手写 HTML。** 必须按以下顺序操作：

1. 从 `OUTPUT_REFERENCE.html` 复制完整文件到新文件
2. 替换 `<body>` 内容为本次分析数据
3. 替换所有 `{{PLACEHOLDER}}`（COMPANY_NAME / COMPANY_NAME_CN / TICKER / DATE / FILING_BASELINE）
4. 不得删除或修改任何 `@page` 规则、CSS class 定义

**理由：** OUTPUT_REFERENCE.html 里的 CSS 是唯一正确来源。手写会漏掉关键 class（如 `.bmc-card` 的横版设置），导致格式错误。

### Pre-render Checklist（生成完 HTML 后，逐项确认，全部 ✅ 才执行 write_pdf）

- [ ] `@page bmc-page { size: A4 landscape; }` 存在于 `<style>` 中
- [ ] BMC 的容器 div class 为 `card bmc-card`（不是只有 `card`）
- [ ] 所有 `{{PLACEHOLDER}}` 已替换，文件中不含任何 `{{` 字符
- [ ] `<sup class="cite">` 引用编号与底部 `<li id="src-N">` 一一对应，无孤立引用
- [ ] PDF 用 `uv run python -c "from weasyprint import HTML; HTML(...).write_pdf(...)"` 生成（不用 `python3 -m weasyprint`）

## Quality Standards

- Every quantitative anchor is traceable to a specific Step 1–2 finding.
- The one-sentence diagnosis names an actual structural tension, not a generic "digital transformation" or "macro headwinds" statement.
- The three conclusions tell one argument: *crisis → strategic bet at risk → partner window*.
- cite source, and only look for information from company financial filings and well-known industry analysis report and your training data.
- do not use article style news outlet as source except the PESTLE analysis
