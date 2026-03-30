# README Roast

> Audit your GitHub README for star conversion. Score it against patterns from top-starred repos in your category.

Your README is your landing page. If visitors can't understand what your project does and why they should care in 5 seconds, they leave. README Roast tells you exactly what's killing your star conversion and how to fix it — backed by data from 90 top-performing repos across 6 categories.

## Quick Start

```bash
# Clone the repo
git clone https://github.com/hidai25/readme-roast
cd readme-roast

# Audit any GitHub repo
/readme-audit https://github.com/your/repo

# Or audit the current repo
/readme-audit
```

Here's what a real audit looks like (run on [EvalView](https://github.com/hidai25/eval-view), 77 stars):

```
README Score: 77/100 — Good

┌──────────────────────────┬───────┬──────────────────┐
│         Category         │ Score │ vs. Category Avg │
├──────────────────────────┼───────┼──────────────────┤
│ Hero & Value Prop        │ 82    │ -1               │
│ Visual Proof             │ 78    │ +10              │
│ Install & Quickstart     │ 88    │ +4               │
│ Trust Signals            │ 64    │ -20              │
│ Structure & Scannability │ 68    │ -12              │
│ Differentiation & CTA    │ 76    │  0               │
└──────────────────────────┴───────┴──────────────────┘

Top Star Killers:
1. Trust Signals (-20 vs avg) — No "used by" logos, 60% of testing repos have them
2. Structure (-12 vs avg) — 450+ lines, no TOC, kitchen-sink syndrome
3. Hero (-1 vs avg) — 3 bold paragraphs push the GIF demo to the fold boundary
```

## Features

- **Score against real benchmarks** — not vibes, not generic advice. Your README scored against 15-20 top repos in your exact category
- **6 scoring dimensions** — hero clarity, visual proof, install friction, trust signals, scannability, and differentiation
- **Star killers identified** — the specific gaps costing you the most stars, ranked by impact
- **Actionable rewrites** — not "make your README better" but "rewrite your hero like this: [concrete suggestion]"
- **Category benchmarks** — "73% of top CLI tools have a GIF demo. You don't." That's the kind of feedback that moves people to action
- **Before/after tracking** — measure the impact of your README changes on your score
- **Audit history in your repo** — every audit auto-saved to `.readme-roast/`, git-friendly, tracks score progression alongside star growth
- **Star correlation** — see if your README improvements actually moved the star graph
- **PDF reports** — shareable, screenshot-able audit reports for posting on X or sharing with your team

## Commands

| Command | What It Does |
|---------|-------------|
| `/readme-audit <url>` | Full audit with scores, benchmarks, and action plan |
| `/readme-hero <url>` | Deep dive on hero section & value prop |
| `/readme-install <url>` | Install friction analysis |
| `/readme-trust <url>` | Trust signal scoring |
| `/readme-visuals <url>` | Visual proof evaluation |
| `/readme-structure <url>` | Scannability assessment |
| `/readme-benchmark <url>` | Compare against category leaders |
| `/readme-report` | Generate shareable markdown report |
| `/readme-report-pdf` | Generate PDF report with charts |
| `/readme-compare` | Before/after delta tracking |
| `/readme-rewrite` | Generate improved sections |
| `/readme-star-killers` | Show what's killing your stars |
| `/readme-history` | Audit timeline with score progression |
| `/readme-history stars` | Score-to-star velocity correlation |

## Scoring

```
README Score = (Hero × 25%) + (Visuals × 20%) + (Install × 15%) + (Trust × 15%) + (Structure × 15%) + (Differentiation × 10%)
```

| Score | Rating | What It Means |
|-------|--------|--------------|
| 85-100 | Excellent | Top-tier README. High star-conversion potential. |
| 70-84 | Good | Solid foundation with clear improvement opportunities. |
| 55-69 | Fair | Average. Missing key elements top repos have. |
| 40-54 | Needs Work | Below average. Multiple gaps reducing conversion. |
| 0-39 | Critical | README is actively hurting adoption. |

## Benchmark Categories

README Roast ships with pre-analyzed benchmark data for 6 categories (90 repos total):

| Category | Repos Analyzed | Examples |
|----------|---------------|----------|
| CLI Tools | 15 | ripgrep, fzf, bat, starship, lazygit |
| AI/ML | 15 | ollama, langchain, open-interpreter, dspy |
| Web Frameworks | 15 | next.js, astro, fastapi, supabase, hono |
| Testing | 15 | playwright, vitest, cypress, jest, k6 |
| DevOps | 15 | terraform, caddy, traefik, dagger, act |
| Library | 15 | axios, zod, pydantic, rich, tanstack-query (default fallback) |

Your repo is auto-detected into a category based on GitHub topics, language, and description.

## Architecture

Built as [Claude Code](https://claude.ai/code) skills — same architecture as [geo-seo-claude](https://github.com/ztrabzada1/geo-seo-claude):

- **14 specialized skills** — scoring, benchmarking, reporting, rewriting, and history tracking
- **3 parallel subagents** — first impression, conversion, and competitive analysis run simultaneously
- **Benchmark data** — curated JSON files with patterns from 90 top repos across 6 categories
- **Report generation** — markdown and PDF output with charts and score gauges

## How It Works

```
/readme-audit https://github.com/user/repo
        │
        ├── Fetch README + repo metadata
        ├── Detect category (CLI, AI/ML, Web, Testing, DevOps, Library)
        │
        ├── [Parallel] First Impression Agent
        │   ├── Hero & Value Prop scoring
        │   ├── Visual Proof detection
        │   └── Structure & Scannability analysis
        │
        ├── [Parallel] Conversion Agent
        │   ├── Trust Signal scanning
        │   ├── Install Friction counting
        │   └── Differentiation & CTA evaluation
        │
        ├── [Parallel] Competitive Agent
        │   └── Benchmark comparison against top repos
        │
        ├── Score aggregation + star killer identification
        ├── README-AUDIT-REPORT.md
        └── Auto-save → .readme-roast/snapshots/{timestamp}.json
```

## Contributing

PRs welcome. Especially for:
- Adding repos to benchmark categories
- New benchmark categories
- Scoring rubric refinements
- PDF report improvements

## License

MIT

---

Built by [Hidai Bar-Mor](https://github.com/hidai25) — also building [EvalView](https://github.com/hidai25/eval-view), regression testing for AI agents.
