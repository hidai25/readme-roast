---
name: readme-audit
description: Full README audit with parallel subagent delegation. Orchestrates a comprehensive star-conversion audit across hero/value prop, visual proof, install friction, trust signals, scannability, and category benchmarking. Produces a composite README Score (0-100) with prioritized action plan.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# README Audit Orchestration Skill

## Purpose

This skill performs a comprehensive README audit measuring how effectively a GitHub repo's README converts visitors into stars. It delegates analysis to parallel subagents, aggregates scores, compares against category benchmarks, and produces an actionable report.

---

## Audit Workflow

### Phase 1: Fetch & Classify

**Step 1: Get the README**

If a GitHub URL is provided (e.g., `https://github.com/owner/repo`):
1. Extract owner and repo from URL
2. Fetch README via: `curl -s https://raw.githubusercontent.com/{owner}/{repo}/main/README.md`
3. If main branch fails, try `master`
4. Also fetch repo metadata: `gh api repos/{owner}/{repo} --jq '{stars: .stargazers_count, language: .language, topics: .topics, description: .description, pushed_at: .pushed_at, license: .license.spdx_id, forks: .forks_count, open_issues: .open_issues_count}'`

If no URL provided:
1. Read `./README.md` from the current directory
2. Try to get repo info from `.git/config` or `gh repo view --json`

**Step 2: Classify the Repo Category**

Use repo topics, language, and description to detect category:

| Category | Detection Signals |
|----------|-----------------|
| **CLI Tool** | Topics: "cli", "terminal", "command-line". Language: Rust, Go. Has "cli" in name/description. |
| **AI/ML** | Topics: "ai", "ml", "llm", "machine-learning". Language: Python with AI libs. |
| **Web Framework** | Topics: "framework", "web", "react", "vue". Has routing/middleware patterns. |
| **Testing** | Topics: "testing", "test", "e2e". Name/description mentions testing. |
| **DevOps** | Topics: "devops", "infrastructure", "deployment", "docker", "kubernetes". |
| **Library** | Default category for packages that don't fit above. |

**Step 3: Load Benchmark Data**

Read the matching `benchmarks/{category}.json` file. If category not found, use `benchmarks/library.json` as default (the "library" category covers general-purpose packages and SDKs). Extract:
- Category averages for each scoring dimension
- Pattern frequency data
- Top 3 repos in category for comparison

---

### Phase 2: Parallel Subagent Delegation

Launch 3 subagents simultaneously. Pass each the full README content and repo metadata.

**Subagent 1: First Impression Analysis** (`agents/readme-first-impression.md`)
- Analyzes hero section & value prop (readme-hero)
- Evaluates visual proof (readme-visuals)
- Checks structure & scannability (readme-structure)
- Returns: hero_score, visuals_score, structure_score + findings

**Subagent 2: Conversion Analysis** (`agents/readme-conversion.md`)
- Checks trust signals (readme-trust)
- Analyzes install friction (readme-install)
- Evaluates differentiation & CTA
- Returns: trust_score, install_score, differentiation_score + findings

**Subagent 3: Competitive Analysis** (`agents/readme-competitive.md`)
- Compares README against category benchmarks (readme-benchmark)
- Identifies pattern gaps vs. top repos
- Returns: benchmark_comparison, pattern_gaps, category_rank_estimate

---

### Phase 3: Score Aggregation & Report

#### Composite Score Calculation

```
README_Score = (Hero * 0.25) + (Visuals * 0.20) + (Install * 0.15) + (Trust * 0.15) + (Structure * 0.15) + (Differentiation * 0.10)
```

| Category | Weight | What It Measures |
|----------|--------|-----------------|
| Hero & Value Prop | 25% | Is the "why should I care" clear in 5 seconds? |
| Visual Proof | 20% | GIF/screenshot/demo above the fold? |
| Install & Quickstart | 15% | Steps from zero to first output? |
| Trust Signals | 15% | Badges, social proof, maintenance signals? |
| Structure & Scannability | 15% | Scannable in 30 seconds? |
| Differentiation & CTA | 10% | Why this over alternatives? Clear next step? |

#### Score Interpretation

| Score | Rating | Meaning |
|-------|--------|---------|
| 85-100 | Excellent | Top-tier README. High star-conversion potential. |
| 70-84 | Good | Solid README with specific improvement opportunities. |
| 55-69 | Fair | Average README. Missing key elements that top repos have. |
| 40-54 | Needs Work | Below average. Multiple gaps reducing star conversion. |
| 0-39 | Critical | README is actively hurting adoption. Major rewrite needed. |

#### Star Killers Identification

Compare each category score against the category benchmark average. The categories where the repo scores furthest below the benchmark average are the "star killers" — the issues most likely reducing star conversion.

Rank star killers by: `benchmark_average - repo_score` (highest gap first).

---

## Output Format

Generate a file called `README-AUDIT-REPORT.md`:

```markdown
# README Audit Report: [Repo Name]

**Audit Date:** [Date]
**Repository:** [URL]
**Stars:** [Count]
**Category:** [Detected Category]
**README Lines:** [Count]

---

## README Score: [X]/100 ([Rating])

[2-3 sentence summary: What's working, what's hurting star conversion, and the single most impactful change.]

### Score Breakdown

| Category | Score | Weight | Weighted | vs. Category Avg |
|----------|-------|--------|----------|-----------------|
| Hero & Value Prop | [X]/100 | 25% | [X] | [+/- vs avg] |
| Visual Proof | [X]/100 | 20% | [X] | [+/- vs avg] |
| Install & Quickstart | [X]/100 | 15% | [X] | [+/- vs avg] |
| Trust Signals | [X]/100 | 15% | [X] | [+/- vs avg] |
| Structure & Scannability | [X]/100 | 15% | [X] | [+/- vs avg] |
| Differentiation & CTA | [X]/100 | 10% | [X] | [+/- vs avg] |
| **Overall** | | | **[X]/100** | |

---

## Top Star Killers

### 1. [Category] — [X] points below category average
**The problem:** [What's wrong in plain language]
**What top repos do:** [Pattern from benchmark data]
**Fix:** [Specific, actionable recommendation]
**Expected impact:** +[X] points

### 2. [Category] — [X] points below category average
[Same format]

### 3. [Category] — [X] points below category average
[Same format]

---

## Category Deep Dives

### Hero & Value Prop ([X]/100)
[Detailed analysis of the first 20 lines, value prop clarity, emotional hook]

### Visual Proof ([X]/100)
[What visuals exist, their position, quality, and effectiveness]

### Install & Quickstart ([X]/100)
[Step count, friction points, copy-pasteability, time-to-first-result]

### Trust Signals ([X]/100)
[Badges found, social proof, maintenance signals, what's missing]

### Structure & Scannability ([X]/100)
[Section order, TOC, heading hierarchy, bullet vs text ratio, length]

### Differentiation & CTA ([X]/100)
[Comparison content, alternative mentions, CTA presence and clarity]

---

## Benchmark Comparison

**Category:** [Category] ([N] top repos analyzed)

| Pattern | Your README | Category Average | Top Performers |
|---------|-------------|-----------------|----------------|
| Has GIF/video demo | [Yes/No] | [X]% have it | [X]% have it |
| Install steps | [N] | [Avg] | [Best] |
| Has comparison section | [Yes/No] | [X]% have it | [X]% have it |
| Has "Used by" logos | [Yes/No] | [X]% have it | [X]% have it |
| Has TOC | [Yes/No] | [X]% have it | [X]% have it |
| Total lines | [N] | [Avg] | [Range] |
| Badge count | [N] | [Avg] | [Range] |

---

## Quick Wins (Do This Week)

1. **[Action]** — Expected impact: +[X] points
2. **[Action]** — Expected impact: +[X] points
3. **[Action]** — Expected impact: +[X] points
4. **[Action]** — Expected impact: +[X] points
5. **[Action]** — Expected impact: +[X] points

## Medium-Term Improvements (This Month)

1. **[Action]** — Expected impact: +[X] points
2. **[Action]** — Expected impact: +[X] points
3. **[Action]** — Expected impact: +[X] points

## Aspirational (When Ready)

1. **[Action]** — What top repos in your category do
2. **[Action]** — What top repos in your category do

---

## Path Forward

| Milestone | Score | Key Change |
|-----------|-------|------------|
| Current | [X]/100 | — |
| After quick wins | ~[X]/100 | [Key improvement] |
| After medium-term | ~[X]/100 | [Key improvement] |
| Target | 80+/100 | Competitive with category leaders |
```

---

## Phase 4: Auto-Save to History

After generating the report, automatically persist the audit:

1. Check if `.readme-roast/` exists in the repo being audited
2. If it doesn't exist, create it:
   - `mkdir -p .readme-roast/snapshots`
   - Initialize `history.json` with repo name, URL, category, and empty audits array
3. Generate snapshot ID: current timestamp as `YYYY-MM-DDTHH-mm`
4. Compute README hash: first 7 characters of the md5 hash of the README content
5. Build snapshot JSON with all scores, patterns, star killers, and action items
6. Write snapshot to `.readme-roast/snapshots/{id}.json`
7. Append audit entry to `.readme-roast/history.json`
8. If a previous audit exists and the README hash changed:
   - Try to detect changes from git: `git log --oneline --since="{last_date}" -- README.md`
   - Store commit messages as `changes_since_last`
9. Print confirmation:
   ```
   ✓ Audit #N saved → .readme-roast/snapshots/{id}.json
     Score: {score}/100 ({rating}) | Stars: {stars}
     {delta from previous if exists: "▲+X points since audit #N-1"}

   Run /readme-history to see your full progression.
   Run /readme-compare to see what changed since last audit.
   ```

This means `/readme-compare` can work without arguments — it reads the last
two entries from `history.json` automatically.

---

## Quality Gates

- **README size limit:** If README exceeds 50KB, analyze only the first 50KB and note truncation.
- **GitHub API:** Respect rate limits. Use `gh` CLI which handles auth automatically.
- **Benchmark data:** If no matching category benchmark exists, use general patterns and note the limitation.
- **Scoring consistency:** All scores must be integers 0-100. Weighted scores calculated to 1 decimal place.
- **Actionability:** Every finding must connect to a specific, implementable action. No vague recommendations.
- **History auto-save:** Always save to `.readme-roast/` after a successful audit. Never silently skip.
