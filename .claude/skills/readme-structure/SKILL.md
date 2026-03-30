---
name: readme-structure
description: Scannability and structural analysis for README star conversion. Evaluates section order, table of contents, heading hierarchy, bullet vs text ratio, code block quality, length, and information density. Provides score (0-100) with structural improvement suggestions.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# README Structure & Scannability Scoring Skill

## Core Insight

Developers don't read READMEs — they scan them. Eye-tracking studies on documentation show that developers spend an average of 30 seconds on a README before deciding to star, install, or leave. If your README requires reading to understand, you've already lost most visitors.

The best READMEs are designed to be scanned, not read. They use headings as signposts, bullets as summaries, code blocks as proof, and progressive disclosure so that scanning gives you 80% of the value.

---

## Ideal Section Order

Based on analysis of top-starred repos, this is the optimal section flow:

| Position | Section | Purpose | Required? |
|----------|---------|---------|-----------|
| 1 | Badges | Instant trust signals | Optional but recommended |
| 2 | Name + Tagline | What is this? | Required |
| 3 | Visual (GIF/Screenshot) | Proof it works | Strongly recommended |
| 4 | Description | Why should I care? | Required |
| 5 | Quick Start / Install | Get me started | Required |
| 6 | Features | What can it do? | Required |
| 7 | Usage / Examples | Show me more | Recommended |
| 8 | Comparison / Why This | Why not alternatives? | Recommended |
| 9 | Configuration | How to customize | Optional |
| 10 | API Reference | Deep details | Optional (link to docs) |
| 11 | Contributing | How to help | Recommended |
| 12 | License | Legal | Required |

---

## Scoring Rubric (0-100)

### Dimension 1: Section Order & Completeness (30% of structure score)

| Score | Criteria |
|-------|----------|
| 90-100 | Follows ideal order closely. All required sections present. Progressive disclosure (overview → details → reference). |
| 70-89 | Most sections present in reasonable order. Missing 1-2 recommended sections. |
| 50-69 | Key sections present but in suboptimal order (e.g., API docs before quickstart). Missing 2-3 recommended sections. |
| 30-49 | Missing required sections. Poor ordering (install before description). |
| 0-29 | Minimal sections. No logical flow. |

**Common antipatterns:**
- Install instructions before explaining what the tool does
- API reference as the main content (README ≠ docs)
- Contributing section before usage examples
- License at the top (wastes above-the-fold real estate)

### Dimension 2: Heading Hierarchy & Navigation (25% of structure score)

| Score | Criteria |
|-------|----------|
| 90-100 | Clean H1 > H2 > H3 hierarchy. TOC present for READMEs > 200 lines. Headings are descriptive and scannable. No skipped levels. |
| 70-89 | Good hierarchy. TOC present or README short enough to not need one. Minor issues. |
| 50-69 | Some hierarchy issues. No TOC for a long README. Some vague headings. |
| 30-49 | Broken hierarchy (H1 > H3 skipping H2). No TOC. Headings are generic ("Section 1"). |
| 0-29 | No heading structure. Or single level (all H2, no nesting). |

**Checks:**
- Is there exactly one H1? (the project name)
- Do H2s represent major sections?
- Are H3s nested within relevant H2s?
- Are headings descriptive? ("Installation" not "Step 1")
- Is there a TOC for README > 200 lines?
- GitHub auto-generates TOC — does the README leverage this?

### Dimension 3: Scannability — Bullets, Lists, Tables (25% of structure score)

| Score | Criteria |
|-------|----------|
| 90-100 | Feature lists use bullets. Comparisons use tables. Steps use numbered lists. Paragraphs are 2-3 sentences max. Information is scannable at a glance. |
| 70-89 | Good use of lists and tables in most sections. Some paragraphs could be broken up. |
| 50-69 | Mix of scannable sections and dense paragraphs. Some opportunities to use lists/tables missed. |
| 30-49 | Mostly paragraphs. Few lists. Dense text blocks dominate. |
| 0-29 | Wall of text. No lists, no tables, no code blocks. Reading required for everything. |

**Scannable elements checklist:**
- [ ] Feature lists as bullets (not paragraphs)
- [ ] Comparison data as tables
- [ ] Step-by-step instructions as numbered lists
- [ ] Key terms in **bold**
- [ ] Code examples in fenced blocks with language tags
- [ ] Short paragraphs (2-3 sentences max)

### Dimension 4: Length & Density (20% of structure score)

| Score | Criteria |
|-------|----------|
| 90-100 | README is 150-500 lines. Dense with information but not overwhelming. Links to docs for deep dives. |
| 70-89 | README is 100-150 or 500-800 lines. Slightly short or slightly long but still useful. |
| 50-69 | README is 50-100 (too sparse) or 800-1500 (too long without TOC). |
| 30-49 | README is under 50 lines (stub) or over 1500 lines (overwhelming). |
| 0-29 | README is under 20 lines or over 3000 lines. |

**Length guidelines by category:**
| Category | Ideal Range | Notes |
|----------|-------------|-------|
| CLI Tools | 200-500 lines | Focused, show don't tell |
| Frameworks | 300-800 lines | More features to cover |
| Libraries | 150-400 lines | API overview + link to docs |
| AI/ML Tools | 250-600 lines | Explain concept + quickstart |
| DevOps | 200-500 lines | Install + config focus |

---

## Analysis Procedure

### Step 1: Parse Structure

1. Extract all headings (H1-H6) with line numbers
2. Build section tree: H1 → H2 children → H3 children
3. Identify section names and classify them (install, features, usage, etc.)
4. Calculate total line count

### Step 2: Check Section Order

1. Map detected sections to ideal order
2. Identify out-of-order sections
3. Identify missing required sections
4. Identify missing recommended sections

### Step 3: Analyze Heading Hierarchy

1. Count H1s (should be 1)
2. Check for skipped levels (H1 → H3 without H2)
3. Check heading descriptiveness (no "Section 1", "Step 2")
4. Check for TOC (look for linked list at top referencing headings)

### Step 4: Measure Scannability

1. Count bullet/list items vs. paragraph lines
2. Count tables
3. Count code blocks (with and without language tags)
4. Calculate ratio: scannable_elements / total_content_elements
5. Count paragraphs with > 4 sentences (flag as dense)

### Step 5: Assess Length

1. Total line count
2. Total word count (approximate: lines * avg_words_per_line)
3. Code vs. prose ratio
4. Compare to category ideal range

### Step 6: Calculate Score

```
Structure_Score = (SectionOrder * 0.30) + (Headings * 0.25) + (Scannability * 0.25) + (Length * 0.20)
```

---

## Output Format

```markdown
## Structure & Scannability Analysis

**Structure Score: [X]/100**

### Score Breakdown
| Dimension | Score | Issue |
|-----------|-------|-------|
| Section Order & Completeness | [X]/100 | [Summary] |
| Heading Hierarchy & Navigation | [X]/100 | [Summary] |
| Scannability | [X]/100 | [Summary] |
| Length & Density | [X]/100 | [N] lines / [Category] ideal: [Range] |

### Section Map (Current Order)
| # | Section | Line | Expected Position | Status |
|---|---------|------|-------------------|--------|
| 1 | [Section name] | [Line #] | [Expected #] | [OK / Out of order / Missing] |

### Missing Sections
- [ ] [Section name] — Why it matters: [reason]

### Scannability Stats
- Total lines: [N]
- Bullet/list items: [N]
- Tables: [N]
- Code blocks: [N] ([N] with language tags)
- Dense paragraphs (4+ sentences): [N]
- Scan ratio: [X]% scannable

### Recommendations
1. **[Highest impact]** — [Specific structural change]
2. **[Quick win]** — [Specific change]
3. **[Improvement]** — [Specific change]
```
