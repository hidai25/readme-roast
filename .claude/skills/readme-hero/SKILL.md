---
name: readme-hero
description: Hero section and value proposition scoring for README star conversion. Analyzes the first 20 lines of a README to determine if visitors can understand what the project does and why they should care within 5 seconds. Provides a score (0-100) with specific rewrite suggestions.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# README Hero & Value Prop Scoring Skill

## Core Insight

The first 5 seconds determine whether a visitor stars your repo or leaves. Research across 500+ top-starred repos shows that high-converting READMEs share three hero patterns: (1) a specific one-liner that names the problem, (2) a "why should I care" hook in the first paragraph, and (3) differentiation from alternatives within the first screen.

Most READMEs fail here by being either too vague ("A powerful framework for building applications") or too technical ("A Rust-based concurrent AST walker with pluggable backends"). The sweet spot is specific and benefit-oriented: "Find files 5x faster than find. Made for humans, not shell scripts."

---

## Scoring Rubric (0-100)

### Dimension 1: One-Liner Clarity (30% of hero score)

The very first line of description — either the repo tagline or the first sentence.

| Score | Criteria |
|-------|----------|
| 90-100 | Specific, names the problem AND the benefit. Uses concrete language. A non-technical person could grasp it. Example: "Regression testing for AI agents — catch behavior changes before your users do." |
| 70-89 | Clear what it does, benefit implied but not explicit. Example: "Fast, lightweight test runner for JavaScript." |
| 50-69 | Understandable but generic. Could describe many tools. Example: "A modern testing framework." |
| 30-49 | Overly technical or jargon-heavy. Requires domain knowledge to understand. Example: "Concurrent polyglot AST mutation testing engine." |
| 0-29 | No clear description, or first line is installation command, or repo has no description at all. |

**High-scoring patterns:**
- "[What it does] — [why it matters]" format
- "[Verb] [thing] [benefit]" format: "Search code 5x faster with ripgrep"
- Problem-first: "Tired of flaky AI tests? EvalView catches regressions before production."

**Low-scoring patterns:**
- Starting with "This is a..." or "A tool for..."
- Listing technologies instead of benefits
- Using acronyms without expansion in the first line

### Dimension 2: "Why Should I Care?" Hook (30% of hero score)

The first paragraph or section after the one-liner. Does it create urgency, curiosity, or desire?

| Score | Criteria |
|-------|----------|
| 90-100 | Explicitly states the pain point this solves. Uses concrete outcomes ("saves 2 hours/week", "catches 40% more bugs"). Creates emotional resonance. Reader thinks "I need this." |
| 70-89 | Pain point referenced but not viscerally. Benefits mentioned but not quantified. Reader thinks "This could be useful." |
| 50-69 | Features listed without connecting to pain. Reader thinks "OK, what does this actually do for me?" |
| 30-49 | Jumps straight to how-it-works without why-it-matters. Reader has to infer the benefit. |
| 0-29 | No motivation provided. README starts with installation or usage without context. Reader thinks "Why would I use this?" |

**Signals of a strong hook:**
- Pain language: "Ever deployed an AI agent that silently started hallucinating?"
- Outcome language: "Ship AI agents with confidence"
- Social proof in hook: "Used by 500+ teams to catch LLM regressions"
- Contrast: "Unlike X, which only does Y, this does Z"

**Signals of a weak hook:**
- Feature dump: "Supports JSON, YAML, TOML, and XML configuration"
- Implementation focus: "Built with React, TypeScript, and Tailwind"
- Meta-description: "This repository contains the source code for..."

### Dimension 3: Specificity vs. Genericness (20% of hero score)

How specific and concrete is the opening content?

| Score | Criteria |
|-------|----------|
| 90-100 | Names specific use cases, specific numbers, specific comparisons. "5x faster than grep for code search" is specific. |
| 70-89 | Mostly specific with occasional generic phrasing. Mentions concrete features. |
| 50-69 | Mix of specific and generic. Some concrete claims, some hand-waving. |
| 30-49 | Mostly generic. "Fast", "lightweight", "modern", "powerful" without evidence. |
| 0-29 | Entirely generic. Could be describing any tool in the category. |

**Specificity test:** Replace the project name with a competitor's name. If the description still works, it's too generic.

### Dimension 4: Above-the-Fold Completeness (20% of hero score)

What can the reader learn without scrolling? (First ~20 lines on GitHub)

| Score | Criteria |
|-------|----------|
| 90-100 | First screen contains: what it does, why it matters, a visual (GIF/screenshot), and how to install. Complete story above the fold. |
| 70-89 | First screen has 3 of 4 elements (what, why, visual, install). |
| 50-69 | First screen has 2 of 4 elements. |
| 30-49 | First screen has only 1 element (usually just a description). |
| 0-29 | First screen is badges-only, empty, or immediately starts with a TOC. |

---

## Analysis Procedure

### Step 1: Extract Hero Content

1. Get the README content (first 50 lines minimum)
2. Identify the hero section:
   - The H1 heading (usually the project name)
   - The first paragraph after H1 (the one-liner/description)
   - Everything before the first H2 heading = the "hero section"
3. Count total lines in the hero section

### Step 2: Analyze One-Liner

1. Extract the first sentence/tagline
2. Check for problem-naming: does it mention a pain point or user need?
3. Check for benefit-stating: does it say what the user gains?
4. Check for specificity: are there concrete claims vs. generic adjectives?
5. Check word count: ideal one-liner is 8-20 words

### Step 3: Analyze Hook

1. Extract the first 2-3 paragraphs after the one-liner
2. Check for pain language (problems, frustrations, costs)
3. Check for outcome language (results, benefits, improvements)
4. Check for quantified claims (numbers, percentages, time savings)
5. Check for social proof (users, companies, downloads)

### Step 4: Analyze Specificity

1. Count generic adjectives ("powerful", "fast", "modern", "lightweight", "simple", "easy")
2. Count specific claims (numbers, comparisons, named use cases)
3. Calculate ratio: specific_claims / (specific_claims + generic_adjectives)
4. Run the substitution test: could this describe a competitor?

### Step 5: Analyze Above-the-Fold

1. Check what appears in the first 20 lines:
   - [ ] Clear description (what it does)
   - [ ] Motivation (why it matters)
   - [ ] Visual proof (image/GIF reference)
   - [ ] Install/quickstart command
2. Count how many of the 4 elements are present

### Step 6: Calculate Score & Generate Suggestions

1. Calculate weighted hero score:
   ```
   Hero_Score = (OneLiner * 0.30) + (Hook * 0.30) + (Specificity * 0.20) + (AboveFold * 0.20)
   ```
2. For each dimension scoring below 60, generate a specific rewrite suggestion
3. Include examples from benchmark data of what top repos in the same category do

---

## Output Format

```markdown
## Hero & Value Prop Analysis

**Hero Score: [X]/100**

### Score Breakdown
| Dimension | Score | Issue |
|-----------|-------|-------|
| One-Liner Clarity | [X]/100 | [One-line issue or "Strong"] |
| "Why Should I Care?" Hook | [X]/100 | [One-line issue or "Strong"] |
| Specificity | [X]/100 | [One-line issue or "Strong"] |
| Above-the-Fold Completeness | [X]/100 | [One-line issue or "Strong"] |

### Current Hero Section
> [Quote the first 5-10 lines of the README]

### What's Working
- [Specific strength with evidence]

### What's Hurting Star Conversion
- [Specific weakness with evidence]

### Suggested Rewrite
> [Rewritten hero section — same content, better structure and language]

### What Top [Category] Repos Do
- [Pattern from benchmark data with specific repo example]
- [Pattern from benchmark data with specific repo example]
```

---

## Reference: Hero Patterns from Top Repos

### Pattern 1: Problem → Solution → Proof
```
# ProjectName
> One-liner: what it does + why it matters

[Problem statement — 1-2 sentences about the pain]
[Solution statement — how this tool solves it]
[Proof — GIF, screenshot, or key metric]
```

### Pattern 2: Tagline → Visual → Install
```
# ProjectName — [Punchy tagline]

[GIF or screenshot]

[One paragraph explaining the value prop]

## Quick Start
```bash
pip install projectname
```

### Pattern 3: Badge Row → Description → Features → Visual
```
[badges]

# ProjectName

[2-3 sentence description with specific benefits]

**Key features:**
- [Benefit-oriented feature 1]
- [Benefit-oriented feature 2]
- [Benefit-oriented feature 3]

[Screenshot or GIF]
```
