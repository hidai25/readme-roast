---
name: readme-visuals
description: Visual proof analysis for README star conversion. Detects and evaluates GIFs, screenshots, videos, architecture diagrams, and demo links. Scores based on position (above/below fold), quality, relevance to value prop, and type effectiveness. Provides score (0-100) with visual improvement suggestions.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# README Visual Proof Scoring Skill

## Core Insight

A GIF demo above the fold is the single strongest predictor of high star velocity in the first week after launch. Analysis of top-starred devtools repos shows that 73% of repos with 5K+ stars have an animated demo in their README, compared to only 28% of repos with under 1K stars.

The reason is simple: a GIF proves the tool works. It eliminates skepticism, demonstrates the UX, and creates a "wow" moment that text alone cannot achieve. Screenshots are the second-best option. Text-only READMEs convert at the lowest rate.

---

## Visual Type Hierarchy (by star-conversion impact)

| Rank | Type | Impact | Why |
|------|------|--------|-----|
| 1 | **Animated GIF/video** of tool in action | Highest | Proves it works, shows real UX, creates "wow" |
| 2 | **Interactive demo link** (Stackblitz, CodeSandbox, live URL) | Very High | Lets visitor try before installing |
| 3 | **Terminal recording** (asciinema, svg-term) | High | Proves CLI tools work, shows real output |
| 4 | **Screenshot** of real output | Medium | Static proof, less compelling than animation |
| 5 | **Architecture diagram** | Medium-Low | Shows how it works, not that it works |
| 6 | **Logo or banner** only | Low | Branding, not proof |
| 7 | **No visuals** | Negative | Reader has to imagine what the tool does |

---

## Scoring Rubric (0-100)

### Dimension 1: Visual Presence & Type (40% of visual score)

| Score | Criteria |
|-------|----------|
| 90-100 | Animated GIF/video showing the core value prop in action. High resolution, current, well-edited (not 30 seconds of setup before the demo). |
| 75-89 | Terminal recording or high-quality screenshot showing real output. Clear and professional. |
| 60-74 | Static screenshot or architecture diagram. Shows the tool but not "in action." |
| 40-59 | Logo, banner, or decorative image only. No product demonstration. |
| 20-39 | Images exist but are low quality, broken, or irrelevant. |
| 0-19 | No visuals at all. Pure text README. |

### Dimension 2: Position — Above vs. Below the Fold (30% of visual score)

"The fold" = the first screen visible on GitHub without scrolling (~first 25 lines of rendered README).

| Score | Criteria |
|-------|----------|
| 90-100 | Primary visual is within the first 15 lines. Immediately visible. |
| 70-89 | Visual is within the first 25 lines. Visible without much scrolling. |
| 50-69 | Visual is below the fold but within the first half of the README. |
| 30-49 | Visual is buried deep in the README (bottom half). |
| 0-29 | Visual exists only in linked docs, not in the README itself. Or no visual. |

### Dimension 3: Value Prop Alignment (30% of visual score)

Does the visual demonstrate the core value proposition stated in the hero?

| Score | Criteria |
|-------|----------|
| 90-100 | Visual directly shows the main thing the tool does. If hero says "catch AI regressions," the visual shows a regression being caught. Perfect alignment. |
| 70-89 | Visual shows the tool in use but not the specific value prop. Shows general usage, not the key differentiator. |
| 50-69 | Visual shows a secondary feature or a setup screen, not the core value. |
| 30-49 | Visual is tangentially related (architecture diagram for a tool that needs a demo). |
| 0-29 | Visual has no relation to value prop (just a logo or stock image). |

---

## Important Scoring Rules

### GIF Subsumes Screenshot
If a repo has an animated GIF or video demo, do NOT penalize for missing static screenshots. A GIF is strictly better than a screenshot — it shows everything a screenshot shows plus motion and interaction. When reporting benchmark comparisons, treat `has_gif = true` as satisfying both the GIF and screenshot patterns.

### Category-Aware Visual Expectations

Different categories have different visual needs. Adjust recommendations accordingly:

| Category | Primary Visual Need | Secondary | Low Value |
|----------|-------------------|-----------|-----------|
| **CLI Tools** | Terminal recording / GIF | asciinema embed | UI screenshot |
| **AI/ML** | GIF of output / notebook screenshot | Architecture diagram | UI screenshot |
| **Web Frameworks** | UI screenshot / live demo link | GIF of dev workflow | Terminal recording |
| **Testing** | Terminal output screenshot / GIF | CI output screenshot | Architecture diagram |
| **DevOps** | Architecture diagram / terminal GIF | Dashboard screenshot | UI screenshot |
| **Library** | Code example output (can be text) | API screenshot | GIF (often unnecessary) |

For **Library** category repos specifically: if the README has clear code examples with output shown, the visual requirement is largely satisfied even without images. Libraries communicate through code, not screenshots.

When making recommendations, suggest the **primary visual need** for the detected category, not generic "add a screenshot."

---

## Analysis Procedure

### Step 1: Detect All Visual Elements

Scan the README for:
1. **Markdown images:** `![alt](url)` or `<img src="url">`
2. **GIF indicators:** URLs ending in `.gif`, `.webp` (animated)
3. **Video links:** YouTube, Vimeo, Loom URLs. `<video>` tags.
4. **Demo links:** Stackblitz, CodeSandbox, Replit, Gitpod, live demo URLs
5. **Terminal recordings:** asciinema links, svg-term embeds
6. **Badges:** Exclude badge images from visual analysis (handled by readme-trust)

### Step 2: Classify Each Visual

For each detected visual:
1. Determine type: GIF, video, screenshot, diagram, logo, badge, other
2. Determine position: line number in README
3. Determine if it's above the fold (line ≤ 25)
4. Extract alt text for context
5. Check if URL is accessible (not 404)

### Step 3: Evaluate Value Prop Alignment

1. Read the hero section (what the tool claims to do)
2. For each visual, assess: does it demonstrate that claim?
3. Score alignment based on how directly the visual proves the value prop

### Step 4: Calculate Score

```
Visual_Score = (Presence_Type * 0.40) + (Position * 0.30) + (Alignment * 0.30)
```

---

## Output Format

```markdown
## Visual Proof Analysis

**Visual Score: [X]/100**

### Score Breakdown
| Dimension | Score | Details |
|-----------|-------|---------|
| Visual Presence & Type | [X]/100 | [Best visual type found] |
| Position (Above/Below Fold) | [X]/100 | [Line number of first visual] |
| Value Prop Alignment | [X]/100 | [Alignment assessment] |

### Visuals Detected
| # | Type | Position (Line) | Above Fold? | Shows Value Prop? |
|---|------|----------------|-------------|-------------------|
| 1 | [Type] | [Line #] | [Yes/No] | [Yes/Partially/No] |

### What's Missing
- [Specific visual that should be added]

### Recommendations
1. **[Highest impact]** — Add a [GIF/screenshot] showing [specific value prop in action]
2. **[Quick win]** — Move the existing [visual] above the fold (before line 15)
3. **[Aspirational]** — [What top repos in this category do]

### What Top [Category] Repos Do
- [X]% have animated GIF/video demos
- [X]% place their primary visual above the fold
- Average position of first visual: line [N]
- [X]% have live demo links
```

---

## Reference: Visual Patterns from Top Repos

### Pattern 1: GIF Demo (Most Effective)
```markdown
# Tool Name — Tagline

![Demo](./assets/demo.gif)

Tool Name does X for Y...
```

### Pattern 2: Terminal Recording
```markdown
# CLI Tool

[![asciicast](https://asciinema.org/a/xxxxx.svg)](https://asciinema.org/a/xxxxx)
```

### Pattern 3: Screenshot Gallery
```markdown
# Tool Name

<p align="center">
  <img src="./screenshots/main.png" alt="Main view" width="600">
</p>
```

### Pattern 4: Live Demo Badge
```markdown
# Tool Name

[![Try it on StackBlitz](https://developer.stackblitz.com/img/open_in_stackblitz.svg)](https://stackblitz.com/github/user/repo)
```

### Visual Creation Tips (for recommendations)
- **GIF recording tools:** Kap (Mac), ScreenToGif (Windows), Peek (Linux), asciinema (terminal)
- **Optimal GIF specs:** 800px wide, < 5MB, < 15 seconds, starts with the "wow" moment
- **Screenshot tools:** Any, but crop to just the relevant output. Add a subtle shadow/border.
- **Architecture diagrams:** Excalidraw, Mermaid (renders in GitHub), draw.io
