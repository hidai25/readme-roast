---
name: readme-install
description: Installation friction and quickstart analysis for README star conversion. Counts steps to first output, checks copy-pasteability, evaluates prerequisite clarity, and scores the overall developer experience of going from zero to working. Provides score (0-100) with friction reduction suggestions.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# README Install Friction Analysis Skill

## Core Insight

Every additional step between "I found this repo" and "I see it working" loses 20-30% of potential users. Top-starred repos obsess over reducing install friction. The gold standard is: one install command + one run command = visible output in under 60 seconds.

The install section is where interest converts to action. A beautifully written hero section means nothing if the quickstart requires 8 steps, 3 config files, and a Docker setup.

---

## Scoring Rubric (0-100)

### Dimension 1: Steps to First Output (35% of install score)

Count discrete commands/actions needed from "I just found this repo" to "I see it working."

| Score | Steps | Criteria |
|-------|-------|----------|
| 90-100 | 1-2 | Single install + single run = output. E.g., `pip install x && x run` |
| 70-89 | 3 | Install + minimal config + run. E.g., `npm install`, create config, `npm start` |
| 50-69 | 4-5 | Install + config + dependencies + env setup + run |
| 30-49 | 6-8 | Multi-step setup with external service dependencies |
| 0-29 | 9+ or unclear | Complex setup, or steps are ambiguous/incomplete |

**How to count steps:**
- Each shell command = 1 step
- Creating a file = 1 step
- Setting an environment variable = 1 step
- "Sign up for an API key" = 2 steps (sign up + configure)
- "Install Docker" = 1 step (if it's a prerequisite, not shown inline)

### Dimension 2: Copy-Pasteability (25% of install score)

Can someone literally copy-paste every command and have it work?

| Score | Criteria |
|-------|----------|
| 90-100 | Every command is in a code block, ready to paste. No placeholder values OR placeholders are clearly marked and explained. Shows expected output. |
| 70-89 | Commands are in code blocks. Some placeholders without clear explanation. Output not shown. |
| 50-69 | Some commands in code blocks, some in inline text. Mix of copy-pasteable and not. |
| 30-49 | Commands described in prose ("run the install command") rather than shown. |
| 0-29 | No executable commands shown. Or commands reference files/configs not provided. |

**Friction checklist:**
- Are commands in ``` code blocks with language tag? (```bash)
- Are placeholder values clearly marked? (`YOUR_API_KEY` not just `key`)
- Is the package manager specified? (`pip install` vs. vague "install")
- Are OS-specific variations shown? (or at least the primary OS)
- Is the expected output shown after the run command?

### Dimension 3: Prerequisite Clarity (20% of install score)

Are dependencies and requirements clearly stated upfront?

| Score | Criteria |
|-------|----------|
| 90-100 | Prerequisites listed in a clear section or inline before install. Version requirements specified. Nothing assumed. |
| 70-89 | Most prerequisites mentioned. Some version requirements. Minor assumptions. |
| 50-69 | Some prerequisites mentioned. Key ones missing. Reader might hit errors. |
| 30-49 | Prerequisites scattered or incomplete. Reader will definitely hit errors. |
| 0-29 | No prerequisites listed. Reader has to guess what's needed. |

**Common prerequisite gaps:**
- Python/Node version not specified
- System dependencies not mentioned (e.g., requires FFmpeg, Redis, Docker)
- API keys needed but not mentioned until runtime error
- OS compatibility not stated

### Dimension 4: Quickstart Quality (20% of install score)

Does the README include a meaningful quickstart that demonstrates the core value?

| Score | Criteria |
|-------|----------|
| 90-100 | Quickstart shows a real use case with real output. Reader can see the value immediately. "Wow, that's cool" moment within 60 seconds. |
| 70-89 | Quickstart works and shows useful output, but uses a toy example rather than a real-world scenario. |
| 50-69 | Quickstart shows basic usage but doesn't demonstrate the key value prop. |
| 30-49 | Quickstart is just API reference or function signatures, not a runnable example. |
| 0-29 | No quickstart section. Jump from install to full API docs. |

---

## Analysis Procedure

### Step 1: Locate Install & Quickstart Sections

Search the README for these section patterns:
- `## Installation`, `## Install`, `## Getting Started`, `## Setup`
- `## Quick Start`, `## Quickstart`, `## Usage`, `## Getting Started`
- `## TL;DR`, `## 5-Minute Setup`
- If no explicit section, look for the first code block after the hero

### Step 2: Count Steps

1. Extract all code blocks from the install/quickstart sections
2. Count individual commands (separated by newlines within blocks)
3. Count non-command steps (file creation, sign-ups, downloads)
4. Total steps = command_count + non_command_steps
5. Note if steps are sequential (must be in order) or parallel (any order)

### Step 3: Check Copy-Pasteability

For each code block:
1. Is it in a fenced code block with language tag?
2. Are there placeholder values? Are they explained?
3. Would pasting this command work on a fresh machine with prerequisites?
4. Is the expected output shown after the command?
5. Are there OS-specific variations needed?

### Step 4: Check Prerequisites

1. Is there a "Requirements" or "Prerequisites" section?
2. Are language/runtime versions specified?
3. Are system dependencies listed?
4. Are external service requirements (API keys, databases) mentioned?
5. Is OS compatibility stated?

### Step 5: Evaluate Quickstart

1. Does the quickstart demonstrate the core value prop?
2. Is the output meaningful (not just "Hello World")?
3. How long would it take a new user to reach the "wow" moment?
4. Does the quickstart match what was promised in the hero?

### Step 6: Calculate Score

```
Install_Score = (Steps * 0.35) + (CopyPaste * 0.25) + (Prerequisites * 0.20) + (Quickstart * 0.20)
```

---

## Output Format

```markdown
## Install & Quickstart Analysis

**Install Score: [X]/100**

### Score Breakdown
| Dimension | Score | Details |
|-----------|-------|---------|
| Steps to First Output | [X]/100 | [N] steps counted |
| Copy-Pasteability | [X]/100 | [Issue or "Fully copy-pasteable"] |
| Prerequisite Clarity | [X]/100 | [Issue or "Clear"] |
| Quickstart Quality | [X]/100 | [Issue or "Demonstrates value"] |

### Step-by-Step Breakdown
1. [Command/action] — [friction note if any]
2. [Command/action] — [friction note if any]
...
**Total: [N] steps to first output**

### Friction Points
- [Specific friction point with line reference]
- [Specific friction point with line reference]

### Suggestions
- [Specific improvement with rewritten code block]
- [Specific improvement]

### What Top [Category] Repos Do
- Average install steps: [N]
- [X]% show expected output after install
- [X]% have single-command install
```

---

## Reference: Install Patterns from Top Repos

### Gold Standard (1-2 steps)
```bash
# Install
pip install readme-roast

# Run
readme-roast audit ./README.md
```
Output shown inline.

### Acceptable (3 steps)
```bash
# Install
npm install -g tool-name

# Initialize
tool-name init

# Run
tool-name start
```

### Common Friction Antipatterns
- "First, install Docker, then..." (hidden prerequisite)
- Config file required but template not provided
- API key needed with no link to where to get one
- "See the docs for full setup" without inline quickstart
- Platform-specific steps without clear OS detection
