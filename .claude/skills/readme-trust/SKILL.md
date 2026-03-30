---
name: readme-trust
description: Trust signal analysis for README star conversion. Evaluates badges, social proof, maintenance signals, sponsor information, community size, and "used by" sections. Produces a Trust Score (0-100) with recommendations for building credibility.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# README Trust Signals Scoring Skill

## Core Insight

Trust is the hidden variable in star conversion. A developer can love your value prop, but if the README signals "abandoned side project" or "unproven experiment," they won't star it. Trust signals are the social proof, maintenance evidence, and credibility markers that tell visitors: "this is real, this is active, this is used by others."

Top-starred repos have an average of 5-7 distinct trust signals. Repos with fewer than 3 trust signals convert at roughly half the rate, regardless of the quality of their content.

---

## Trust Signal Categories

### 1. Badges (20% of trust score)

Badges are the instant visual trust layer. They communicate quality and activity at a glance.

**Badge scoring:**

| Score | Criteria |
|-------|----------|
| 90-100 | 5+ relevant badges: CI status (passing), version/release, downloads/installs, license, coverage. All badges are current and functional. |
| 70-89 | 3-4 badges including CI and version. All functional. |
| 50-69 | 1-2 badges. May be just license or version. |
| 30-49 | Badges exist but are broken (404), outdated, or irrelevant. |
| 0-29 | No badges at all. |

**Badge hierarchy (by trust impact):**
1. **CI/Build status** — "Tests pass" is the #1 trust signal
2. **Version/Release** — Shows active development and stability
3. **Downloads/Installs** — Social proof through usage numbers
4. **License** — Legal clarity (MIT/Apache/ISC most trusted for OSS)
5. **Coverage** — Code quality signal
6. **TypeScript/Type support** — Quality signal for JS ecosystem
7. **Dependencies** — Shows maintenance awareness

**What to flag:**
- Broken badge images (404s)
- "Build: failing" badge (negative trust)
- Outdated version badges
- Vanity badges that add no information

### 2. Social Proof (25% of trust score)

Evidence that other people and organizations use and trust this project.

| Score | Criteria |
|-------|----------|
| 90-100 | "Used by" section with recognizable logos (5+). Testimonials from named people. Star count prominently displayed. Community size shown. |
| 70-89 | "Used by" with 2-4 logos or names. Some social proof. Star count or download count visible. |
| 50-69 | Mentions users/companies in passing but no dedicated section. Some download metrics. |
| 30-49 | No explicit social proof. Maybe a star badge but no usage evidence. |
| 0-29 | No social proof of any kind. No indication anyone uses this. |

**What to look for:**
- "Used by" / "Trusted by" / "Who uses this" section with logos
- "Featured in" / "As seen in" (blog posts, conferences, newsletters)
- Testimonial quotes from real users
- Star count display (custom badge or shields.io)
- Download/install count
- "Join 500+ developers" type claims
- Discord/Slack member count
- Contributor count

### 3. Maintenance Signals (25% of trust score)

Evidence the project is actively maintained and won't be abandoned.

| Score | Criteria |
|-------|----------|
| 90-100 | Recent release (within 3 months). Active commit history. Changelog mentioned. Roadmap or "What's next" section. Responsive to issues (mentioned or evidenced). |
| 70-89 | Recent activity (within 6 months). Some release information. No roadmap but clearly active. |
| 50-69 | Last activity 6-12 months ago. Or active but no version/release information. |
| 30-49 | Last activity 1-2 years ago. Or README mentions features as "coming soon" from long ago. |
| 0-29 | No indication of maintenance. Last activity 2+ years. Or "archived" / "deprecated" signals. |

**How to check (via GitHub API):**
```bash
gh api repos/{owner}/{repo} --jq '{
  pushed_at: .pushed_at,
  updated_at: .updated_at,
  open_issues: .open_issues_count,
  archived: .archived
}'
gh api repos/{owner}/{repo}/releases --jq '.[0] | {tag: .tag_name, date: .published_at}'
```

**What to look for in README:**
- Release version mentioned with date
- Changelog link
- "What's new" or "Recent changes" section
- Roadmap or "Coming soon" section (is it current?)
- Contributing section (suggests active community)
- "Stable" / "Production ready" / "Beta" status

### 4. License & Legal Clarity (10% of trust score)

| Score | Criteria |
|-------|----------|
| 90-100 | License clearly stated (badge + LICENSE file). Permissive license (MIT, Apache 2.0, ISC, BSD). |
| 70-89 | License file exists, mentioned in README. |
| 50-69 | License file exists but not mentioned in README. |
| 30-49 | Unclear license. Or restrictive license without explanation. |
| 0-29 | No license at all. (Legal risk — many devs won't touch this.) |

### 5. Community & Support (20% of trust score)

| Score | Criteria |
|-------|----------|
| 90-100 | Active community links (Discord/Slack with member count). Contributing guidelines. Code of conduct. Multiple communication channels. Responsive maintainers. |
| 70-89 | Community link exists (Discord/Slack/Discussions). Contributing guide. Some support pathway. |
| 50-69 | GitHub Issues as only support channel. Basic contributing section. |
| 30-49 | No community links. No contributing guidelines. |
| 0-29 | No way to get help, report bugs, or contribute. |

---

## Composite Trust Score

```
Trust_Score = (Badges * 0.20) + (SocialProof * 0.25) + (Maintenance * 0.25) + (License * 0.10) + (Community * 0.20)
```

---

## Analysis Procedure

### Step 1: Scan for Badges
1. Look for image links in the first 10 lines (common badge position)
2. Identify badge types by URL patterns:
   - `shields.io` — standard badges
   - `github.com/.../workflows/.../badge.svg` — CI status
   - `badge.fury.io` — version
   - `codecov.io` — coverage
   - `img.shields.io/npm/dm` — downloads
3. Check if badges load (not 404)
4. Categorize and count

### Step 2: Scan for Social Proof
1. Search for "used by", "trusted by", "who uses", "featured in"
2. Look for logo images in a grid/row pattern
3. Search for testimonial quotes (blockquotes with attribution)
4. Check for star/download count badges
5. Look for community size mentions

### Step 3: Check Maintenance Signals
1. Via GitHub API: get last push date, last release, open issues count
2. In README: search for version numbers, changelog links, roadmap
3. Check for "archived", "deprecated", "unmaintained" language
4. Look for "What's new" or recent update mentions

### Step 4: Check License
1. Look for license badge
2. Check if LICENSE file is referenced
3. Identify license type from badge or file

### Step 5: Check Community
1. Search for Discord/Slack/Matrix/Gitter links
2. Look for CONTRIBUTING.md reference
3. Check for CODE_OF_CONDUCT.md reference
4. Look for "Support" or "Getting Help" section
5. Check for GitHub Discussions or Sponsors links

### Step 6: Calculate Score

---

## Output Format

```markdown
## Trust Signals Analysis

**Trust Score: [X]/100**

### Score Breakdown
| Category | Score | Key Finding |
|----------|-------|-------------|
| Badges | [X]/100 | [N] badges found: [types] |
| Social Proof | [X]/100 | [Summary] |
| Maintenance | [X]/100 | Last activity: [date] |
| License | [X]/100 | [License type or "Missing"] |
| Community | [X]/100 | [Channels found or "None"] |

### Trust Signals Found
- [x] [Signal found — details]
- [x] [Signal found — details]
- [ ] [Signal missing — impact]
- [ ] [Signal missing — impact]

### Recommendations
1. **[Quick win]** — [Specific action, expected trust impact]
2. **[Medium effort]** — [Specific action]
3. **[Aspirational]** — [What top repos do]

### What Top [Category] Repos Have
- Average badge count: [N]
- [X]% have "Used by" sections
- [X]% have community links (Discord/Slack)
- [X]% show download/install counts
```
