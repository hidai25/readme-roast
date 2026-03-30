---
name: readme-report-pdf
description: Generate a professional PDF report from README audit data using ReportLab. Creates a polished, shareable PDF with score gauges, bar charts, benchmark comparison visuals, and prioritized action plans.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# README Roast PDF Report Generator

## Purpose

Generate a professional, visually polished PDF report from README audit data. The PDF includes score gauges, bar charts, benchmark comparison visuals, and a prioritized action plan — ready to share as a before/after or deliver to a client.

## Prerequisites

- **ReportLab** must be installed: `pip install reportlab`
- Run a full README audit first (using `/readme-audit`) to have data
- The PDF generation script is at: `scripts/generate_pdf_report.py`

## How to Generate

### Step 1: Collect Audit Data

After running `/readme-audit`, collect all scores into a JSON structure:

```json
{
    "repo_name": "eval-view",
    "repo_url": "https://github.com/hidai25/eval-view",
    "stars": 77,
    "category": "testing",
    "date": "2026-03-30",
    "readme_score": 52,
    "scores": {
        "hero": 55,
        "visuals": 30,
        "install": 72,
        "trust": 45,
        "structure": 60,
        "differentiation": 40
    },
    "category_averages": {
        "hero": 78,
        "visuals": 72,
        "install": 82,
        "trust": 70,
        "structure": 75,
        "differentiation": 65
    },
    "star_killers": [
        {"category": "Visual Proof", "gap": 42, "fix": "Add a GIF demo showing test output"},
        {"category": "Trust Signals", "gap": 25, "fix": "Add CI badge and used-by section"},
        {"category": "Differentiation", "gap": 25, "fix": "Add comparison table vs alternatives"}
    ],
    "quick_wins": [
        "Add CI/build status badge",
        "Add GIF showing test run output",
        "Add 'Used by' section with any known users",
        "Add comparison section vs LangSmith, Braintrust",
        "Move install command above the fold"
    ],
    "medium_term": [
        "Record 15-second GIF demo of core workflow",
        "Create comparison table with 5 alternatives",
        "Add quickstart that shows real test output"
    ],
    "strategic": [
        "Build 'Used by' section with real logos",
        "Add live demo or playground link"
    ],
    "patterns": {
        "has_gif": false,
        "has_screenshot": true,
        "has_demo_link": false,
        "has_comparison_table": false,
        "has_used_by": false,
        "has_toc": false,
        "has_quickstart_output": true,
        "has_community_link": false,
        "has_contributing": true,
        "has_license_badge": true,
        "install_steps": 3,
        "badges_count": 2,
        "code_blocks": 8,
        "total_lines": 180
    },
    "pattern_benchmarks": {
        "has_gif": 40,
        "has_screenshot": 67,
        "has_demo_link": 10,
        "has_comparison_table": 7,
        "has_used_by": 60,
        "has_toc": 47,
        "has_quickstart_output": 53,
        "has_community_link": 53,
        "has_contributing": 87,
        "has_license_badge": 80
    },
    "score_projection": [
        {"milestone": "Current", "score": 52, "change": "—"},
        {"milestone": "After quick wins", "score": 65, "change": "Add badges, GIF, used-by"},
        {"milestone": "Full optimization", "score": 80, "change": "Comparison table, community"}
    ]
}
```

### Step 2: Write JSON and Generate PDF

```bash
cat > /tmp/readme-audit-data.json << 'EOF'
{ ... audit JSON data ... }
EOF

python3 scripts/generate_pdf_report.py /tmp/readme-audit-data.json README-ROAST-REPORT.pdf
```

### PDF Contents

The generated PDF includes:
- **Cover Page** — Repo name, URL, stars, date, overall score gauge
- **Score Dashboard** — Table + bar chart of all 6 categories (you vs. category average)
- **Star Killers** — Top 3-5 issues with gap size and fix recommendations
- **Pattern Gaps** — Table showing what you have vs. what top repos have (requires `patterns` and `pattern_benchmarks` in JSON)
- **Score Projection** — Current → After quick wins → After full optimization (requires `score_projection` in JSON)
- **Action Plan** — Prioritized quick wins, medium-term, and strategic actions

### Color Palette

- Navy primary: `#1a1a2e`
- Blue accent: `#0f3460`
- Green (good): `#00b894`
- Yellow (fair): `#fdcb6e`
- Red (poor): `#e17055`
- Coral highlight: `#e94560`

### Score Gauge Colors

- 80+: Green (`#00b894`)
- 60-79: Blue (`#0f3460`)
- 40-59: Yellow (`#fdcb6e`)
- Below 40: Red (`#e17055`)

## Workflow When User Runs This Skill

1. Check for existing `README-AUDIT-REPORT.md` in current directory
2. If not found, tell user to run `/readme-audit` first
3. If found, parse markdown to extract scores, findings, recommendations
4. Build JSON data structure
5. Write to `/tmp/readme-audit-data.json`
6. Run `python3 scripts/generate_pdf_report.py /tmp/readme-audit-data.json README-ROAST-REPORT.pdf`
7. Report success with file path and size

## Output

`README-ROAST-REPORT.pdf` in the current working directory.
