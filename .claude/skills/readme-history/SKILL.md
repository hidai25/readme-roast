---
name: readme-history
description: >
  Audit history and progression tracking for README Roast. Stores audit snapshots
  in `.readme-roast/` inside the repo being audited — git-friendly, self-tracking,
  designed for measuring your own README improvement over time. Correlates score
  changes with star velocity. Use when user says "history", "timeline", "progression",
  "past audits", "show progress", or "star correlation".
allowed-tools:
  - Read
  - Write
  - Bash
  - Glob
  - Grep
---

# README History — Audit Progression Tracking

## Philosophy

Your README improvement is a story. Every audit is a chapter. This skill stores
that story inside your repo so you can:
- See your score climb over time
- Know exactly which changes moved the needle
- Correlate README improvements with star growth
- Share a compelling before/after narrative (Reddit post, anyone?)

The history lives in `.readme-roast/` at the root of the audited repo. It's
designed to be committed to git — your README journey is part of your project's
story.

---

## Directory Structure

```
.readme-roast/
├── history.json              # Timeline index — lightweight, human-readable
└── snapshots/
    ├── 2026-03-30T04-46.json # Full audit data from first run
    ├── 2026-04-05T12-30.json # Full audit data from second run
    └── ...
```

### history.json Schema

The history index is intentionally lightweight — full audit data lives in
snapshot files. Each audit entry has just enough to render the timeline.

```json
{
  "repo": "eval-view",
  "url": "https://github.com/hidai25/eval-view",
  "category": "testing",
  "audits": [
    {
      "id": "2026-03-30T04-46",
      "date": "2026-03-30",
      "readme_hash": "a3f2b1c",
      "stars": 77,
      "score": 77,
      "rating": "Good"
    },
    {
      "id": "2026-04-05T12-30",
      "date": "2026-04-05",
      "readme_hash": "d4e5f6a",
      "stars": 92,
      "score": 85,
      "rating": "Excellent"
    }
  ]
}
```

### Snapshot File Schema (snapshots/*.json)

Each snapshot stores the complete audit data for that run — everything needed
to reconstruct the full report or generate comparisons:

```json
{
  "id": "2026-03-30T04-46",
  "date": "2026-03-30",
  "readme_hash": "a3f2b1c",
  "stars": 77,
  "category": "testing",
  "scores": {
    "hero": 82,
    "visuals": 78,
    "install": 88,
    "trust": 64,
    "structure": 68,
    "differentiation": 76,
    "overall": 77
  },
  "rating": "Good",
  "patterns": {
    "has_gif": true,
    "has_screenshot": true,
    "has_comparison_table": true,
    "has_used_by": false,
    "has_toc": false,
    "install_steps": 3,
    "badges_count": 6,
    "total_lines": 450,
    "code_blocks": 15,
    "has_quickstart_output": true,
    "has_contributing": true,
    "has_license_badge": true,
    "has_community_link": false
  },
  "star_killers": [
    {"category": "Trust Signals", "gap": 20, "score": 64, "benchmark_avg": 84, "fix": "Add used-by section"},
    {"category": "Structure", "gap": 12, "score": 68, "benchmark_avg": 80, "fix": "Add TOC, reduce length"}
  ],
  "action_items": [
    "Add TOC",
    "Add used-by section",
    "Record 15-second GIF demo",
    "Build community channel"
  ],
  "previous_audit": null,
  "delta": null
}
```

For subsequent audits, the `previous_audit` field links to the prior snapshot ID,
and `delta` contains per-category score changes:

```json
{
  "previous_audit": "2026-03-30T04-46",
  "delta": {
    "overall": 8,
    "hero": 6,
    "visuals": 7,
    "install": 2,
    "trust": 14,
    "structure": 12,
    "differentiation": 4
  }
}
```

---

## Commands

### `/readme-history`

Show the full audit timeline with progression.

**Output format:**

```
README Roast History — eval-view
Category: testing | Audits: 4 | Tracking since: 2026-03-30

Score Progression:
  #1  2026-03-30  ████████░░░░░░░░░░░░  52/100  Needs Work   ⭐ 77
  #2  2026-04-05  ████████████░░░░░░░░  65/100  Fair         ⭐ 84   ▲+13
  #3  2026-04-12  ███████████████░░░░░  77/100  Good         ⭐ 92   ▲+12
  #4  2026-04-26  █████████████████░░░  85/100  Excellent    ⭐ 118  ▲+8

Overall: +33 points in 27 days | Stars: 77 → 118 (+53%)

Category Trends:
  Hero:            52 → 65 → 82 → 88  (▲+36)
  Visuals:         30 → 55 → 78 → 85  (▲+55)
  Install:         72 → 75 → 88 → 90  (▲+18)
  Trust:           45 → 55 → 64 → 78  (▲+33)
  Structure:       60 → 68 → 68 → 80  (▲+20)
  Differentiation: 40 → 65 → 76 → 80  (▲+40)

Key Changes That Moved the Needle:
  #1→#2: Added GIF demo (+25 visuals), added comparison table (+25 diff)
  #2→#3: Added used-by section (+9 trust), added TOC (+10 structure)
  #3→#4: Rewrote hero with pain-first hook (+6 hero), added community link (+14 trust)
```

### `/readme-history init`

Initialize `.readme-roast/` in the current repo. Creates the directory structure
and an empty `history.json`. Safe to run multiple times — won't overwrite existing data.

### `/readme-history note "your note here"`

Add a note to the most recent audit entry. Useful for recording what you changed
between audits:

```
/readme-history note "Rewrote hero section, added GIF demo, shortened to 380 lines"
```

### `/readme-history stars`

Show score-to-star correlation analysis:

```
Star Velocity Correlation — eval-view

| Period | Score Change | Stars Gained | Stars/Day |
|--------|-------------|-------------|-----------|
| Audit #1→#2 | +13 pts | +7 stars | 1.0/day |
| Audit #2→#3 | +12 pts | +8 stars | 1.1/day |
| Audit #3→#4 | +8 pts | +26 stars | 1.9/day |

Observations:
- Star velocity increased 90% after README score crossed 77
- Biggest star acceleration came after the visual proof improvements
- Total: +33 README points correlated with +53% star growth
```

---

## Integration with Other Skills

### Auto-Save After `/readme-audit`

When `/readme-audit` completes, it should automatically:

1. Check if `.readme-roast/` exists in the audited repo
2. If yes: save a snapshot and append to `history.json`
3. If no: ask the user if they want to initialize tracking
4. Generate the snapshot ID from the current timestamp: `YYYY-MM-DDTHH-mm`
5. Fetch current star count via GitHub API
6. Compute `readme_hash` as first 7 chars of md5 of the README content
7. Detect `changes_since_last` by diffing the current README against the previous snapshot's `readme_hash` — if the hash changed, prompt the user to describe what they changed (or auto-detect from git log)

### Auto-Read by `/readme-compare`

When `/readme-compare` runs without arguments:

1. Read `.readme-roast/history.json`
2. Use the last two entries as "before" and "after"
3. Generate the delta report from the snapshot data
4. No need for manual file arguments

When `/readme-compare #1 #3` is used:

1. Read history, find audits #1 and #3
2. Load their snapshots from `snapshots/`
3. Generate delta between those specific audits

---

## Procedures

### Initializing History

```
1. Create .readme-roast/ directory
2. Create .readme-roast/snapshots/ directory
3. Create .readme-roast/history.json with:
   {
     "repo": "<detected from git or cwd>",
     "url": "<detected from git remote>",
     "category": null,
     "created": "<today>",
     "audits": []
   }
4. Suggest adding to .gitignore if user doesn't want to track publicly
   (but recommend committing — the journey is the content)
```

### Saving a Snapshot

```
1. Generate ID: datetime.now().strftime("%Y-%m-%dT%H-%M")
2. Build snapshot JSON from audit results
3. Write to .readme-roast/snapshots/{id}.json
4. Compute README hash: hashlib.md5(readme_content.encode()).hexdigest()[:7]
5. If previous audit exists and readme_hash differs:
   a. Try to detect changes from git log:
      git log --oneline --since="{last_audit_date}" -- README.md
   b. Store commit messages as changes_since_last
6. Append entry to history.json audits array
7. Print confirmation:
   ✓ Audit #N saved to .readme-roast/snapshots/{id}.json
   Score: {score}/100 ({rating}) | Stars: {stars}
   {delta from last audit if exists}
```

### Reading History

```
1. Read .readme-roast/history.json
2. For each audit entry, calculate:
   - Delta from previous audit (score, stars, per-category)
   - Stars per day between audits
   - Which categories improved most
3. Render the timeline with progress bars
4. Identify the changes that had the biggest score impact
```

---

## .gitignore Recommendation

Recommend users add this to their `.gitignore` if they want to keep history private:

```
# README Roast audit history (remove this line to commit your README journey)
# .readme-roast/
```

But the default recommendation is to commit it — the progression data is valuable
content for blog posts, Reddit, and demonstrating OSS growth practices.

---

## Output Files

| Command | Output |
|---------|--------|
| `/readme-history init` | Creates `.readme-roast/` directory structure |
| `/readme-history` | Inline timeline display (no file) |
| `/readme-history note` | Updates `history.json` in place |
| `/readme-history stars` | Inline correlation analysis (no file) |
| `/readme-audit` (auto) | Saves snapshot to `.readme-roast/snapshots/` |
| `/readme-compare` (auto) | Reads from `.readme-roast/history.json` |
