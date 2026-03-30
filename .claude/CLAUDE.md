# README Roast

README audit tool for GitHub star conversion. Built as Claude Code skills.

## Architecture

- **Skills** in `.claude/skills/` — each has a SKILL.md with scoring rubrics
- **Agents** in `.claude/agents/` — parallel workers combining skills
- **Benchmarks** in `benchmarks/` — curated data from top-starred repos per category
- **Scripts** in `scripts/` — PDF report generation

## Commands

| Command | What It Does |
|---------|-------------|
| `/readme-audit <url>` | Full README audit with parallel subagents |
| `/readme-audit` | Audit current repo's README |
| `/readme-hero <url>` | Score hero section & value prop |
| `/readme-install <url>` | Analyze install friction |
| `/readme-trust <url>` | Check trust signals |
| `/readme-visuals <url>` | Evaluate visual proof |
| `/readme-structure <url>` | Check scannability |
| `/readme-benchmark <url>` | Compare against top repos in category |
| `/readme-report` | Generate markdown report |
| `/readme-report-pdf` | Generate PDF report |
| `/readme-compare` | Before/after delta tracking |
| `/readme-rewrite` | Generate improved README sections |
| `/readme-star-killers` | Show top issues killing star conversion |

## Scoring Formula

```
README_Score = (Hero * 0.25) + (Visuals * 0.20) + (Install * 0.15) + (Trust * 0.15) + (Structure * 0.15) + (Differentiation * 0.10)
```

## Score Interpretation

| Score | Rating |
|-------|--------|
| 85-100 | Excellent |
| 70-84 | Good |
| 55-69 | Fair |
| 40-54 | Needs Work |
| 0-39 | Critical |

## Conventions

- All audit output goes to markdown files in the working directory
- Benchmark data lives in `benchmarks/*.json`
- PDF generation requires ReportLab: `pip install reportlab`
- GitHub API access via `gh` CLI for repo metadata
