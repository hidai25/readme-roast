---
name: readme-benchmark
description: Category benchmarking for README star conversion. Compares a README against pre-analyzed patterns from 15-20 top-starred repos in the same category (CLI tools, AI/ML, web frameworks, testing, DevOps). Identifies specific gaps vs. category leaders and provides data-driven recommendations.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# README Category Benchmarking Skill

## Core Insight

"Your README is good" means nothing without context. "Your README is missing a GIF demo, which 73% of top CLI tools with 5K+ stars have" — that's actionable. This skill provides that context by comparing any README against curated benchmark data from the top-performing repos in each category.

The benchmark data answers the question: **"What do repos that get lots of stars actually do differently in their READMEs?"**

---

## How Benchmarking Works

### Step 1: Detect or Accept Category

If category is provided by the audit orchestrator, use it. Otherwise, detect using:
- GitHub topics
- Primary language
- Repo description keywords
- README content patterns

Categories: `cli-tools`, `ai-ml`, `web-frameworks`, `testing`, `devops`, `library` (default — used for generic packages/SDKs)

### Step 2: Load Benchmark Data

Read the matching file from the `benchmarks/` directory:
- `benchmarks/cli-tools.json`
- `benchmarks/ai-ml.json`
- `benchmarks/web-frameworks.json`
- `benchmarks/testing.json`
- `benchmarks/devops.json`
- `benchmarks/library.json` (default fallback)

Each file contains:
- Individual repo scores and pattern data
- Category averages across all 6 scoring dimensions
- Pattern frequency data (% of top repos with each pattern)

### Step 3: Score the Target README

Using the same criteria as the benchmark data, extract patterns from the target README:

| Pattern | How to Detect |
|---------|---------------|
| `has_gif` | Image URL ending in .gif, or `<video>` tag, or asciinema embed |
| `has_screenshot` | Image URL ending in .png, .jpg, .webp (non-badge) |
| `has_demo_link` | Links to stackblitz, codesandbox, replit, or live demo URL |
| `has_comparison_table` | Markdown table comparing features with alternatives |
| `has_comparison_section` | H2/H3 containing "vs", "alternatives", "comparison", "why" |
| `install_steps` | Count of commands in install/quickstart sections |
| `has_used_by` | Section containing "used by", "trusted by", or logo grid |
| `has_toc` | Linked list near top referencing README headings |
| `hero_words` | Word count of first paragraph after H1 |
| `total_lines` | Total README line count |
| `badges_count` | Count of badge images (shields.io, etc.) |
| `has_quickstart_output` | Expected output shown after quickstart commands |
| `code_blocks` | Total fenced code blocks |
| `has_contributing` | Section with "contributing" heading or CONTRIBUTING.md link |
| `has_license_badge` | License badge in README |
| `has_community_link` | Discord, Slack, Discussions, or Matrix link |

### Step 4: Compare Against Benchmarks

For each pattern, compare the target against:
1. **Category average** — what the average top repo has
2. **Pattern frequency** — what percentage of top repos have this pattern
3. **Top 3 repos** — specific examples of repos doing it well

### Step 5: Identify Gaps

Rank gaps by impact. A missing pattern that 80% of top repos have is more impactful than one that 30% have. Weight by the scoring category it affects.

Gap priority formula:
```
Gap_Priority = pattern_frequency * category_weight * (benchmark_avg - target_score)
```

### Step 6: Generate Recommendations

For each gap, provide:
1. What's missing
2. What percentage of top repos have it
3. A specific example from a top repo
4. How to implement it

---

## Output Format

Generate `README-BENCHMARK.md`:

```markdown
# README Benchmark Report: [Repo Name]

**Category:** [Category]
**Benchmarked Against:** [N] top-starred [category] repos
**Benchmark Data Date:** [Date]

---

## How You Compare

### Overall Score Position
```
Your README:   [▓▓▓▓▓░░░░░░░░░░░░░░░]  [X]/100
Category Avg:  [▓▓▓▓▓▓▓▓▓░░░░░░░░░░░]  [X]/100
Top Performer: [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░]  [X]/100
```

### Score Comparison by Category

| Category | Your Score | Category Avg | Gap | Top Performer |
|----------|-----------|-------------|-----|---------------|
| Hero & Value Prop | [X] | [X] | [+/-X] | [Repo]: [Score] |
| Visual Proof | [X] | [X] | [+/-X] | [Repo]: [Score] |
| Install & Quickstart | [X] | [X] | [+/-X] | [Repo]: [Score] |
| Trust Signals | [X] | [X] | [+/-X] | [Repo]: [Score] |
| Structure | [X] | [X] | [+/-X] | [Repo]: [Score] |
| Differentiation | [X] | [X] | [+/-X] | [Repo]: [Score] |

---

## Pattern Comparison

| Pattern | You | % of Top Repos | Gap? |
|---------|-----|---------------|------|
| GIF/video demo | [Yes/No] | [X]% | [Yes/No] |
| Screenshot | [Yes/No] | [X]% | [Yes/No] |
| Live demo link | [Yes/No] | [X]% | [Yes/No] |
| Comparison section | [Yes/No] | [X]% | [Yes/No] |
| "Used by" logos | [Yes/No] | [X]% | [Yes/No] |
| Table of contents | [Yes/No] | [X]% | [Yes/No] |
| Quickstart output shown | [Yes/No] | [X]% | [Yes/No] |
| Community link | [Yes/No] | [X]% | [Yes/No] |
| Contributing guide | [Yes/No] | [X]% | [Yes/No] |
| License badge | [Yes/No] | [X]% | [Yes/No] |

### Numeric Comparisons
| Metric | You | Category Avg | Best | Worst |
|--------|-----|-------------|------|-------|
| Install steps | [N] | [N] | [N] | [N] |
| README lines | [N] | [N] | [N] | [N] |
| Badge count | [N] | [N] | [N] | [N] |
| Code blocks | [N] | [N] | [N] | [N] |
| Hero word count | [N] | [N] | [N] | [N] |

---

## Top Gaps (Ranked by Impact)

### 1. [Pattern] — [X]% of top repos have this, you don't
**Impact:** This affects your [category] score by approximately [X] points.
**Example:** [Repo Name] does this: [specific description of how they implement it]
**How to fix:** [Specific, actionable steps]

### 2. [Pattern] — [X]% of top repos have this, you don't
[Same format]

### 3. [Pattern] — [X]% of top repos have this, you don't
[Same format]

---

## Top 5 Repos in Your Category

| Rank | Repo | Stars | Overall Score | Best Dimension |
|------|------|-------|---------------|----------------|
| 1 | [Repo] | [Stars] | [Score]/100 | [Category]: [Score] |
| 2 | [Repo] | [Stars] | [Score]/100 | [Category]: [Score] |
| 3 | [Repo] | [Stars] | [Score]/100 | [Category]: [Score] |
| 4 | [Repo] | [Stars] | [Score]/100 | [Category]: [Score] |
| 5 | [Repo] | [Stars] | [Score]/100 | [Category]: [Score] |

---

## What Would It Take to Reach Category Average?

| Action | Estimated Score Lift | Effort |
|--------|---------------------|--------|
| [Action 1] | +[X] points | [Low/Med/High] |
| [Action 2] | +[X] points | [Low/Med/High] |
| [Action 3] | +[X] points | [Low/Med/High] |
| **Total** | **+[X] points → [New Score]/100** | |
```
