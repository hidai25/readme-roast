---
name: readme-report
description: Generate a professional, shareable README audit report combining all scoring dimensions into a single deliverable with scores, findings, benchmark comparison, and prioritized action plan. Client-ready format suitable for sharing with team members or posting as before/after content.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# README Roast Report Generator

## Purpose

This skill aggregates outputs from all README audit skills into a single, professional report. The report is designed to be **shareable** — posted on X/Twitter as a before/after, shared with co-maintainers, or used as proof of README improvement. Written for developers and OSS maintainers, not executives.

## How to Use

1. Run `/readme-audit <url>` first (or have existing audit data)
2. Run `/readme-report` to generate the composite report
3. Output: `README-ROAST-REPORT.md`

---

## Report Template

```markdown
# README Roast Report: [Repo Name]

**Repository:** [URL]
**Stars:** [Count] | **Language:** [Language] | **Category:** [Category]
**Audit Date:** [Date]
**README Lines:** [Count]

---

## README Score: [X]/100 — [Rating]

> [2-3 sentence executive summary: what's working, what's the biggest problem, and the single most impactful change to make.]

### Score Dashboard

| Category | Score | Weight | Weighted | vs. Top [Category] Repos |
|----------|-------|--------|----------|--------------------------|
| Hero & Value Prop | [X]/100 | 25% | [X] | [▲/▼ X] vs avg [X] |
| Visual Proof | [X]/100 | 20% | [X] | [▲/▼ X] vs avg [X] |
| Install & Quickstart | [X]/100 | 15% | [X] | [▲/▼ X] vs avg [X] |
| Trust Signals | [X]/100 | 15% | [X] | [▲/▼ X] vs avg [X] |
| Structure & Scannability | [X]/100 | 15% | [X] | [▲/▼ X] vs avg [X] |
| Differentiation & CTA | [X]/100 | 10% | [X] | [▲/▼ X] vs avg [X] |
| **TOTAL** | | | **[X]/100** | **vs avg [X]** |

---

## Star Killers — What's Hurting Your Stars Most

### 1. [Issue Title]
**Score gap:** [X] points below category average
**The problem:** [Plain language explanation]
**What [Top Repo Name] does instead:** [Specific example]
**Fix:** [Concrete action with expected point gain]

### 2. [Issue Title]
[Same format]

### 3. [Issue Title]
[Same format]

---

## What's Working Well

- **[Strength 1]:** [Why this is effective, with specific evidence from the README]
- **[Strength 2]:** [Why this is effective]
- **[Strength 3]:** [Why this is effective]

---

## Deep Dive: Each Category

### Hero & Value Prop — [X]/100

**Current first lines:**
> [Quote the first 5 lines]

**Analysis:** [What works and what doesn't]
**Key issue:** [Main problem]
**Suggested improvement:** [Specific rewrite or action]

### Visual Proof — [X]/100

**Visuals found:** [List: type, position, alignment]
**Analysis:** [Assessment]
**Key issue:** [Main problem or "None — strong visual presence"]
**Suggested improvement:** [Specific action]

### Install & Quickstart — [X]/100

**Current steps:** [Count]
**Step breakdown:** [1. command 2. command ...]
**Analysis:** [Friction assessment]
**Key issue:** [Main friction point]
**Suggested improvement:** [Streamlined version]

### Trust Signals — [X]/100

**Signals found:** [List: badges, social proof, maintenance, license, community]
**Signals missing:** [List]
**Key issue:** [Main trust gap]
**Suggested improvement:** [Specific action]

### Structure & Scannability — [X]/100

**Sections found:** [Ordered list]
**Stats:** [Lines, bullets, tables, code blocks]
**Key issue:** [Main structural problem]
**Suggested improvement:** [Specific action]

### Differentiation & CTA — [X]/100

**Comparison content:** [Found/Not found]
**CTA:** [What exists]
**Key issue:** [Main differentiation gap]
**Suggested improvement:** [Specific action]

---

## Benchmark Snapshot

**Category:** [Category] | **Repos Analyzed:** [N]

| Metric | Your README | Category Average | Gap |
|--------|-------------|-----------------|-----|
| Overall Score | [X]/100 | [X]/100 | [+/-X] |
| Has GIF Demo | [Yes/No] | [X]% do | [Gap?] |
| Install Steps | [N] | Avg [N] | [+/-N] |
| Has Comparison | [Yes/No] | [X]% do | [Gap?] |
| Has "Used By" | [Yes/No] | [X]% do | [Gap?] |
| Badge Count | [N] | Avg [N] | [+/-N] |
| README Lines | [N] | Avg [N] | [+/-N] |

---

## Action Plan

### Quick Wins (< 1 hour each)
| # | Action | Expected Impact | Category |
|---|--------|----------------|----------|
| 1 | [Action] | +[X] points | [Category] |
| 2 | [Action] | +[X] points | [Category] |
| 3 | [Action] | +[X] points | [Category] |
| 4 | [Action] | +[X] points | [Category] |
| 5 | [Action] | +[X] points | [Category] |

### This Weekend
| # | Action | Expected Impact | Category |
|---|--------|----------------|----------|
| 1 | [Action] | +[X] points | [Category] |
| 2 | [Action] | +[X] points | [Category] |
| 3 | [Action] | +[X] points | [Category] |

### When You're Ready
| # | Action | Expected Impact | Category |
|---|--------|----------------|----------|
| 1 | [Action] | +[X] points | [Category] |
| 2 | [Action] | +[X] points | [Category] |

### Score Projection
| Milestone | Score | Key Change |
|-----------|-------|------------|
| Current | [X]/100 | — |
| After quick wins | ~[X]/100 | +[X] points |
| After weekend work | ~[X]/100 | +[X] points |
| Full optimization | ~[X]/100 | Competitive with category leaders |

---

*Generated by [README Roast](https://github.com/hidai25/readme-roast) — the open-source README audit tool for star conversion.*
```

---

## Tone & Formatting Guidelines

- **Direct, not diplomatic.** "Your hero buries the value prop" not "Consider potentially improving the clarity of your opening section."
- **Specific, not vague.** Always reference line numbers, exact text, or concrete patterns.
- **Actionable, not theoretical.** Every finding connects to a "do this" action.
- **Data-backed.** Reference benchmark data ("73% of top CLI tools have this").
- **Shareable.** The report should look good when screenshotted and posted on X/Twitter.
- **No hedging.** "Add a GIF demo" not "You might want to consider adding a GIF demo."

## Output

Generate `README-ROAST-REPORT.md` in the current working directory.
