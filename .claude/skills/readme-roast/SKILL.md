---
name: readme-roast
description: >
  README audit tool for GitHub star conversion. Scores READMEs against patterns
  from top-starred repos in each category. Performs full audits, hero analysis,
  install friction checks, trust signal scoring, visual proof evaluation,
  scannability assessment, category benchmarking, and professional report generation.
  Use when user says "readme", "audit", "star conversion", "readme score",
  "star killers", "benchmark", "rewrite", or any GitHub URL for README analysis.
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# README Roast — Claude Code Skill

> **Philosophy:** Your README is your landing page. If it doesn't convert visitors
> to stars in 30 seconds, everything else you built doesn't matter.

---

## Quick Reference

| Command | What It Does |
|---------|-------------|
| `/readme-audit <url>` | Full README audit with parallel subagents |
| `/readme-audit` | Audit current repo's README.md |
| `/readme-hero <url>` | Score hero section & value prop (25% of total) |
| `/readme-install <url>` | Analyze install friction (15% of total) |
| `/readme-trust <url>` | Check trust signals — badges, social proof (15% of total) |
| `/readme-visuals <url>` | Evaluate visual proof — GIF, screenshot, demo (20% of total) |
| `/readme-structure <url>` | Check scannability & section flow (15% of total) |
| `/readme-benchmark <url>` | Compare against top repos in your category |
| `/readme-report` | Generate client-ready markdown report |
| `/readme-report-pdf` | Generate professional PDF report with charts |
| `/readme-compare` | Before/after delta tracking |
| `/readme-rewrite` | Generate improved README sections |
| `/readme-star-killers` | Show the top issues killing star conversion |
| `/readme-history` | Show audit timeline with score progression and star correlation |
| `/readme-history init` | Initialize `.readme-roast/` tracking in current repo |
| `/readme-history note "..."` | Add a note about what you changed since last audit |
| `/readme-history stars` | Show score-to-star velocity correlation |

---

## Why README Auditing Matters

| Insight | Source |
|---------|--------|
| Daytona got 4,000 stars in one week after a README rewrite | Daytona blog, 2025 |
| People star projects they understand and trust | Scrapegraphai founder |
| The awesome-readme list has 20K+ stars — devs care about this | GitHub |
| README is the #1 factor in first-impression decisions | Multiple OSS surveys |
| Repos with GIF demos get 3x more stars in first week | Category benchmark data |
| Single-command install repos convert 2x better | Category benchmark data |

---

## Orchestration Logic

### Full Audit (`/readme-audit <url>`)

**Phase 1: Fetch & Classify (Sequential)**
1. Fetch the README.md from the provided GitHub URL, local path, or current repo
   - GitHub URL: Use `gh api repos/{owner}/{repo}/readme --jq .content | base64 -d` or WebFetch `https://raw.githubusercontent.com/{owner}/{repo}/main/README.md`
   - Local: Read `./README.md` from the current directory
2. Fetch repo metadata via GitHub API: stars, language, topics, last commit, description
3. Classify the repo category using topics, language, and description:

| Category | Detection Signals |
|----------|-----------------|
| **CLI Tool** | Topics include "cli", "terminal", "command-line"; primary language is Rust, Go, or has "cli" in name |
| **AI/ML** | Topics include "ai", "ml", "llm", "machine-learning", "deep-learning"; uses Python with AI dependencies |
| **Web Framework** | Topics include "framework", "web", "frontend", "backend"; has routing/middleware patterns |
| **Testing** | Topics include "testing", "test", "e2e", "unit-test"; name contains "test" or description mentions testing |
| **DevOps** | Topics include "devops", "infrastructure", "deployment", "ci-cd", "container" |
| **Library** | Default for packages/modules that don't fit above categories |

**Phase 2: Parallel Analysis (Delegate to 3 Subagents)**

| Subagent | Agent File | Skills Used |
|----------|-----------|-------------|
| First Impression | `agents/readme-first-impression.md` | readme-hero, readme-visuals, readme-structure |
| Conversion | `agents/readme-conversion.md` | readme-trust, readme-install (+ differentiation scoring) |
| Competitive | `agents/readme-competitive.md` | readme-benchmark |

**Phase 3: Score Aggregation (Sequential)**
1. Collect all subagent scores
2. Calculate composite README Score using weighted formula
3. Load benchmark data for detected category from `benchmarks/*.json`
4. Compare scores against category averages
5. Identify top 3 "star killers" (biggest gaps vs. category leaders)
6. Generate prioritized action plan

### Scoring Formula

```
README_Score = (Hero * 0.25) + (Visuals * 0.20) + (Install * 0.15) + (Trust * 0.15) + (Structure * 0.15) + (Differentiation * 0.10)
```

| Category | Weight | What It Measures |
|----------|--------|-----------------|
| Hero & Value Prop | 25% | Can someone understand what this does and why in 5 seconds? |
| Visual Proof | 20% | Is there a GIF/screenshot/demo showing it works? |
| Install & Quickstart | 15% | How many steps from zero to "wow this works"? |
| Trust Signals | 15% | Badges, social proof, maintenance signals? |
| Structure & Scannability | 15% | Can you get it by scanning for 30 seconds? |
| Differentiation & CTA | 10% | Why this over alternatives? What should I do next? |

### Score Interpretation

| Score | Rating | Meaning |
|-------|--------|---------|
| 85-100 | Excellent | Top-tier README. High star-conversion potential. |
| 70-84 | Good | Solid README with specific improvement opportunities. |
| 55-69 | Fair | Average README. Missing key elements that top repos have. |
| 40-54 | Needs Work | Below average. Multiple gaps reducing star conversion. |
| 0-39 | Critical | README is actively hurting adoption. Major rewrite needed. |

---

## Sub-Skills (14 Specialized Components)

| # | Skill | Purpose |
|---|-------|---------|
| 1 | readme-roast | Master orchestrator (this file) |
| 2 | readme-audit | Full audit orchestration and scoring |
| 3 | readme-hero | Hero section & value prop analysis |
| 4 | readme-install | Install friction and quickstart analysis |
| 5 | readme-trust | Trust signals — badges, social proof, maintenance |
| 6 | readme-visuals | Visual proof — GIF, screenshots, demos |
| 7 | readme-structure | Scannability, section order, formatting |
| 8 | readme-benchmark | Category benchmarking against top repos |
| 9 | readme-report | Client-ready markdown report generation |
| 10 | readme-report-pdf | Professional PDF report with charts |
| 11 | readme-compare | Before/after delta tracking |
| 12 | readme-rewrite | Generate improved README sections |
| 13 | readme-star-killers | Quick diagnostic of top issues killing star conversion |
| 14 | readme-history | Audit progression tracking, star correlation, timeline |

---

## Subagents (3 Parallel Workers)

| Agent | File | Skills Used |
|-------|------|-------------|
| First Impression | `agents/readme-first-impression.md` | readme-hero, readme-visuals, readme-structure |
| Conversion | `agents/readme-conversion.md` | readme-trust, readme-install |
| Competitive | `agents/readme-competitive.md` | readme-benchmark |

---

## Output Files

| Command | Output File |
|---------|------------|
| `/readme-audit` | `README-AUDIT-REPORT.md` |
| `/readme-hero` | Inline score + suggestions |
| `/readme-install` | Inline score + suggestions |
| `/readme-trust` | Inline score + suggestions |
| `/readme-visuals` | Inline score + suggestions |
| `/readme-structure` | Inline score + suggestions |
| `/readme-benchmark` | `README-BENCHMARK.md` |
| `/readme-report` | `README-ROAST-REPORT.md` |
| `/readme-report-pdf` | `README-ROAST-REPORT.pdf` |
| `/readme-compare` | `README-COMPARE.md` |
| `/readme-rewrite` | `README-REWRITE.md` |

---

## Benchmark Data

Pre-analyzed patterns from top-starred repos in 6 categories, stored in `benchmarks/*.json`:

| Category | File | Repos |
|----------|------|-------|
| CLI Tools | `benchmarks/cli-tools.json` | ripgrep, fd, bat, fzf, jq, httpie, starship, etc. |
| AI/ML | `benchmarks/ai-ml.json` | langchain, ollama, llamaindex, dspy, instructor, etc. |
| Web Frameworks | `benchmarks/web-frameworks.json` | next.js, astro, fastapi, hono, drizzle, etc. |
| Testing | `benchmarks/testing.json` | playwright, vitest, pytest, cypress, k6, etc. |
| DevOps | `benchmarks/devops.json` | terraform, pulumi, caddy, traefik, dagger, etc. |
| Library | `benchmarks/library.json` | axios, zod, pydantic, rich, tanstack-query, etc. (default fallback) |

Each benchmark includes:
- Per-repo scores across all 6 categories
- Pattern detection (has GIF, has comparison table, install steps, etc.)
- Category averages for comparison
- Pattern frequency data ("73% of top CLI tools have a GIF demo")

---

## Quick Start Examples

```
# Full audit of a GitHub repo
/readme-audit https://github.com/user/repo

# Audit your current repo's README
/readme-audit

# Just check the hero section
/readme-hero https://github.com/user/repo

# Compare against top repos in your category
/readme-benchmark https://github.com/user/repo

# Generate a shareable report
/readme-report

# See what's killing your star conversion
/readme-star-killers

# Get rewrite suggestions
/readme-rewrite
```
