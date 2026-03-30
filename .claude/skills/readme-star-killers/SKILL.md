---
name: readme-star-killers
description: >
  Quick diagnostic showing the top issues killing your README's star conversion.
  Runs a lightweight audit and surfaces only the highest-impact gaps ranked by
  the distance between your score and the category benchmark average. Use when
  user says "star killers", "what's hurting my stars", "why no stars", or
  "what's wrong with my readme".
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# README Star Killers Skill

## Purpose

Skip the full audit. Just show the 3-5 issues most likely reducing star conversion, ranked by impact. This is the "what do I fix first?" command.

## How It Works

### If an audit report already exists

1. Look for `README-AUDIT-REPORT.md` in the current directory
2. Parse the scores and star killers section
3. Display a focused summary

### If no audit report exists

1. Fetch the README (from URL argument, or `./README.md`)
2. Run a quick scoring pass across all 6 dimensions (no subagents — single-pass)
3. Load benchmark data for the detected category
4. Calculate gaps: `category_avg - your_score` for each dimension
5. Rank by gap size (largest first)
6. Display the top 3-5 gaps with specific fixes

## Quick Scoring Pass

When no full audit exists, score each dimension with a fast heuristic:

### Hero (0-100)
- Has a one-liner tagline after H1? (+25)
- First paragraph mentions a problem/pain? (+25)
- Specific claims vs. generic adjectives? (+25)
- Visual + install in first 25 lines? (+25)

### Visuals (0-100)
- Has any non-badge image? (+30)
- Image is a GIF or video? (+30)
- Image is in the first 25 lines? (+20)
- Image shows the product in action? (+20)

### Install (0-100)
- Has install section? (+20)
- Single install command? (+30)
- Commands in code blocks? (+20)
- Expected output shown? (+15)
- Prerequisites listed? (+15)

### Trust (0-100)
- Has 3+ badges? (+20)
- Has "used by" or social proof? (+25)
- Last commit within 3 months? (+25)
- Has license badge/mention? (+10)
- Has community link? (+20)

### Structure (0-100)
- Has TOC (if > 200 lines)? (+25)
- Headings follow ideal order? (+25)
- More bullets than dense paragraphs? (+25)
- Length in ideal range for category? (+25)

### Differentiation (0-100)
- Has comparison table or "vs" section? (+40)
- Has explicit CTA? (+30)
- Features describe benefits, not just features? (+30)

## Output Format

Display inline (no file output):

```
Star Killers — [Repo Name]

README Score: [X]/100 ([Rating])
Category: [Category] (avg: [X]/100)

🔴 #1: [Category] — [X] points below average
   Problem: [Plain language]
   Fix: [Specific action]
   Impact: +[X] points

🟡 #2: [Category] — [X] points below average
   Problem: [Plain language]
   Fix: [Specific action]
   Impact: +[X] points

🟡 #3: [Category] — [X] points below average
   Problem: [Plain language]
   Fix: [Specific action]
   Impact: +[X] points

Fix all three → estimated score: [X]/100 ([New Rating])

Run /readme-audit for the full report.
```
