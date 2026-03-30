---
name: readme-rewrite
description: >
  Generate improved README sections based on audit findings and benchmark patterns.
  Rewrites hero section, quickstart, feature bullets, comparison section, and CTA
  using patterns from top-starred repos in the same category. Outputs a complete
  rewritten README or individual section rewrites.
allowed-tools: Read, Write, Bash, Glob, Grep, WebFetch
---

# README Rewrite Skill

## Purpose

Turn audit findings into concrete rewrites. This skill takes the current README, the audit scores, and benchmark data, then generates improved versions of each section — optimized for star conversion using patterns from top repos in the same category.

## How to Use

1. Run `/readme-audit` first to get scores and findings
2. Run `/readme-rewrite` to generate improved sections
3. Review and apply the suggestions you like
4. Output: `README-REWRITE.md`

---

## Rewrite Principles

### 1. Benefit Over Feature
- Before: "Supports JSON, YAML, and TOML configuration"
- After: "Configure once, run everywhere — supports JSON, YAML, and TOML"

### 2. Specific Over Generic
- Before: "A fast testing framework"
- After: "Run 10,000 tests in 3 seconds — 40x faster than Jest for large suites"

### 3. Problem Over Solution
- Before: "EvalView provides regression testing for AI agents"
- After: "Your AI agent passed all tests yesterday. Today it's hallucinating. EvalView catches these silent regressions before your users do."

### 4. Show Over Tell
- Before: "Easy to install and use"
- After: `pip install evalview && evalview run` (that's it — results in 30 seconds)

### 5. Scannable Over Readable
- Before: Long paragraph explaining features
- After: Bullet list with bold lead + one-line explanation

---

## Rewrite Procedure

### Step 1: Read Current README & Audit Data

1. Read the current README.md
2. Read README-AUDIT-REPORT.md (if exists) for scores and findings
3. Determine the repo category and load benchmark patterns

### Step 2: Rewrite Each Section

For each section scoring below 70, generate an improved version.

#### Hero Section Rewrite

Structure:
```markdown
# [Project Name]

> [One-liner: what it does + the benefit, 10-15 words max]

[Problem statement — 1-2 sentences. Name the pain. Be specific.]

[Solution statement — How this tool solves it. One sentence.]

[GIF or screenshot placeholder — describe what it should show]

## Quick Start

```bash
[Single install command]
[Single run command]
```

[Expected output — show what success looks like]
```

Rules:
- First line after H1 must be the tagline (< 15 words)
- First paragraph must name the problem, not the solution
- Use "you" language ("your tests", "your team")
- Include a specific claim if possible (speed, reduction, coverage)
- End the hero with a quickstart, not more explanation

#### Feature Bullets Rewrite

Structure:
```markdown
## Features

- **[Benefit]** — [How it works in one sentence]
- **[Benefit]** — [How it works in one sentence]
- **[Benefit]** — [How it works in one sentence]
```

Rules:
- Lead each bullet with the BENEFIT in bold, not the feature name
- Keep to 5-7 bullets (not 15)
- Each bullet must be one line
- Avoid technical jargon in the bold part
- Order by importance to the user, not by complexity

#### Comparison Section Rewrite

Structure:
```markdown
## Why [Project Name]?

| Feature | [Project] | [Alternative 1] | [Alternative 2] |
|---------|-----------|-----------------|-----------------|
| [Feature 1] | ✅ | ❌ | ✅ |
| [Feature 2] | ✅ | ✅ | ❌ |

**Choose [Project] when:** [1-2 sentence positioning statement]
**Choose [Alternative] when:** [Honest acknowledgment of when alternatives are better]
```

Rules:
- Use a table for comparisons (scannable)
- Be honest — acknowledge where alternatives are stronger
- Focus on differentiating features, not common ones
- Include 2-3 alternatives maximum
- End with positioning: "Choose X when..."

#### CTA Section Rewrite

Structure:
```markdown
## Get Started

```bash
[Install command]
```

- [Star this repo](link) if it's useful
- [Join our Discord](link) for help and discussions
- [Read the docs](link) for full API reference
- [Contribute](CONTRIBUTING.md) — PRs welcome!
```

### Step 3: Generate Output

Create `README-REWRITE.md` with:
1. Each rewritten section clearly labeled
2. The original version quoted for comparison
3. Explanation of why the change improves star conversion
4. Score estimate for the new version

---

## Output Format

```markdown
# README Rewrite Suggestions: [Repo Name]

**Current Score:** [X]/100
**Estimated Score After Rewrites:** [X]/100

---

## Hero Section

### Current (Score: [X]/100)
> [Current first 10 lines quoted]

### Suggested Rewrite
[New hero section — complete, copy-pasteable]

### Why This Is Better
- [Specific improvement with scoring impact]
- [Specific improvement]

---

## Feature Bullets

### Current
> [Current feature section quoted]

### Suggested Rewrite
[New feature bullets — benefit-first format]

### Why This Is Better
- [Improvement explanation]

---

## Comparison Section

### Current
> [Current comparison content, or "None exists"]

### Suggested Rewrite
[New comparison table with positioning]

### Why This Is Better
- [X]% of top [category] repos have comparison sections
- [Specific impact on differentiation score]

---

## Quick Start

### Current (Score: [X]/100)
> [Current install/quickstart quoted]

### Suggested Rewrite
[Streamlined quickstart with expected output]

### Why This Is Better
- Reduced from [N] steps to [N] steps
- Added expected output
- [Other improvements]

---

## CTA Section

### Current
> [Current CTA or "None"]

### Suggested Rewrite
[New CTA section]

---

## Full Rewritten README

[Complete README with all rewrites applied — ready to copy-paste as a starting point]

---

*Generated by [README Roast](https://github.com/hidai25/readme-roast)*
```

## Important Notes

- Rewrites are suggestions, not replacements. The maintainer knows their project best.
- Preserve technical accuracy — don't make claims the tool can't support.
- Keep the maintainer's voice where it's strong. Don't homogenize.
- Focus rewrites on the lowest-scoring sections first.
- Always provide the full rewritten README at the end for easy adoption.
