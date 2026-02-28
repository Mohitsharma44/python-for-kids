# Python for Kids - Project Context

## Project Overview

This is an open-ended, week-by-week Python course for kids aged 9-12. The student has some prior text-based coding experience. The course teaches Python through game development using **Pygame Zero (pgzero)**. The student is a big Roblox fan, so game-themed content keeps them engaged — but the goal is **Python only** (no bridge to Lua/Roblox Studio).

**Author:** Mohit Sharma (Mohitsharma44@gmail.com)

## Student Profile

- **Age:** 9-12
- **Experience:** Some text-based coding (not a complete beginner)
- **Interests:** Roblox, gaming
- **Motivation:** Game-themed content; building things they can see and interact with
- **Goal:** Learn Python fundamentals through game development

## Repository Structure

```
python-for-kids/
├── weekNN/                    # Each week is a folder (week01, week02, ...)
│   ├── assignment.txt         # Step-by-step assignment with challenges
│   ├── <game_or_project>.py   # The main Python file for the week
│   └── images/                # Image assets used by the game (PNG files)
├── Dockerfile                 # Kasm/Thonny remote desktop environment
├── Makefile                   # venv, install, dev, run, fmt, lint, clean
├── requirements.txt           # Runtime deps: pgzero, pygame-ce, arcade
├── requirements-dev.txt       # Dev deps: black, isort, flake8, pre-commit
└── .flake8                    # Linter config (max-line-length=100, pgzero builtins)
```

## Tech Stack

- **Language:** Python 3.10+
- **Game Framework:** Pygame Zero (`pgzero`) — simplified game development, no boilerplate
- **IDE:** Thonny (beginner-friendly, runs in Docker/Kasm desktop)
- **Formatter:** `black`
- **Import Sorter:** `isort`
- **Linter:** `flake8` (max line length 100, pgzero builtins registered)
- **Pre-commit hooks:** black + isort + flake8

## Content Conventions

### Folder Naming

- Weeks are numbered with zero-padding: `week01`, `week02`, `week03`, etc.

### Assignment Files (`assignment.txt`)

Every week includes an `assignment.txt` with this structure:

1. **Header** with the week's project name
2. **How to Get Started** — 4 simple steps (open, run, follow challenges, fill in report)
3. **Learning Objectives** — bullet list of concepts covered
4. **Step-by-Step Challenges** — progressive difficulty, each with a **Checkpoint** at the end:
   - **Step 1: Beginner** — run the game, observe, make small changes
   - **Step 2: Intermediate** — unlock/toggle features, understand new concepts
   - **Step 3: Advanced** — more complex modifications, reading function internals (keep to ~5 sub-steps max)
   - **Step 4: Creative/Experimentation** — open-ended customization
5. **Thinking Questions** — metacognitive questions; prefer experimental ("try this and see") over purely theoretical
6. **Bonus Challenges** — extension tasks for fast learners; must be achievable independently with hints provided
7. **How to Submit** — instructions to fill in and email `mission_report.txt`
8. **Tips for Success** — encouragement and safety nets
9. **Troubleshooting** — common issues and fixes

### Mission Report Files (`mission_report.txt`)

Every week includes a `mission_report.txt` template for structured submission:

- **Themed header** matching the week's game (e.g., "STAR DODGER — MISSION REPORT")
- **Sections per step** with specific prompts matching the assignment challenges
- **Thinking question section** with space to write answers
- **Bonus challenges section** for optional work
- **Favorite settings section** — what values they liked best
- **Final thoughts** — most interesting thing learned, most confusing part, star rating
- **Submission instructions** at the bottom (email subject line format: "Week NN Mission Report - [Name]")

### Python Game Files

Code files follow these patterns:

- **Module docstring** at the top explaining what the game is, what they'll learn, and how to play
- **Section headers** with `# ========` dividers and descriptive titles
- **Heavy commenting** — every block, every non-obvious line gets a comment explaining *what* it does and *why*
- **Feature toggles** — boolean switches (`USE_SPRITES = False`) that let the student unlock features by changing `True`/`False`
- **Graceful fallbacks** — if sprites/assets are missing, the game falls back to simple shapes so nothing breaks
- **Console feedback** — `print()` statements with emoji to confirm what's happening behind the scenes
- **In-file instructions** — a commented step-by-step guide at the bottom of the file for quick reference
- **`pgzrun.go()`** at the very end to start the game

### Code Style

- Follow `black` formatting (auto-applied)
- Max line length: 100 characters
- Use descriptive variable names (no single letters except loop vars)
- Register pgzero builtins in `.flake8`: `Actor, animate, clock, keys, keyboard, music, Rect, screen, sounds, images, tone, WIDTH, HEIGHT`
- f-strings for string formatting
- `global` keyword explicitly called out and explained when used

## Teaching Style & Tone

### Voice

- **Encouraging and warm** — "Don't be afraid to experiment - that's how you learn!"
- **Direct and clear** — short sentences, simple vocabulary appropriate for 9-12 year olds
- **Use emoji in instructional content** (assignments, code comments, print statements) to make it visually engaging: use game-related emoji like the ones used in week01 assignment.txt and gold_collector_game.py
- **Concrete before abstract** — always show what the code *does* before explaining the theory
- **No jargon without explanation** — if introducing a term like "collision detection", immediately explain it in plain language

### Pedagogical Approach

1. **Play first, read code second** — student runs the game before looking at code
2. **Feature toggles for progressive complexity** — boolean switches unlock features without rewriting code
3. **One concept at a time** — each step focuses on a single idea
4. **Immediate visual feedback** — every code change produces a visible result in the game
5. **Safe experimentation** — always remind to save, provide fallbacks, make it hard to break things
6. **Thinking questions** — not just "do this" but "why does this work?"
7. **Bonus challenges** — stretch goals for when the student finishes early or wants more

### When Answering Student Questions

- Use simple analogies the student can relate to (game mechanics, real-world objects)
- Reference Roblox concepts when helpful (e.g., "like how in Roblox, scripts run your game logic — here `update()` does the same thing")
- Show code examples inline — don't just describe, demonstrate
- Keep explanations to 2-3 sentences, then offer to explain more if needed
- If the student asks something beyond current scope, give a simplified answer and note they'll learn more later

## Guidelines for Creating New Weeks

### Planning a New Week

1. **Pick one new concept** to teach (e.g., lists, loops, classes, sound effects)
2. **Design a game or project** that naturally requires that concept
3. **Build on prior weeks** — reference things the student already knows
4. **Keep the game playable and fun** — learning is the goal, but engagement is the vehicle

### File Checklist for Each New Week

- [ ] `weekNN/` folder
- [ ] Main Python file with full comments and feature toggles
- [ ] `assignment.txt` with all sections (see structure above)
- [ ] `mission_report.txt` template matching the assignment steps
- [ ] `images/` folder with any needed PNG assets
- [ ] Update `Makefile` `run` target if needed for the new week's game
- [ ] Ensure all code passes `black . && isort . && flake8`

### Concept Progression (What's Been Covered)

**Week 01:** Variables, data types (int, tuple, bool, str), functions (`draw`, `update`), if statements, keyboard input, collision detection, global keyword, f-strings, random numbers, RGB colors, coordinate system, max/min for boundaries, modulo operator

**Week 02:** Lists (`[]`, `append()`, `clear()`, `remove()`), for loops (`for x in list:`), `range()`, the "to_remove" pattern (why you can't remove while iterating), `clock.schedule_interval()`, `clock.schedule_unique()`, functions that return values, `len()`, `hasattr()`, tuple unpacking, `on_key_down()` event hook, game state reset, `continue` keyword

### Concepts Available for Future Weeks

Build on what's covered. Reasonable next topics (not prescriptive — pick based on what fits a fun game idea):

- **Loops** (`for`, `while`) — e.g., drawing multiple objects, animation frames
- **Lists** — e.g., multiple enemies, inventory system, high score tracking
- **Dictionaries** — e.g., item properties, character stats
- **Classes/Objects** — e.g., creating a Player class, Enemy class
- **Sound/Music** — pgzero has built-in `sounds` and `music` support
- **Animation** — `animate()` function, sprite sheets
- **Timers** — `clock.schedule()` for timed events
- **File I/O** — saving/loading high scores
- **More complex game mechanics** — gravity, platforming, health bars, levels

## Development Workflow

```bash
# Setup
make dev              # Creates venv, installs runtime + dev deps

# Run a game
make run              # Runs week01 game (update Makefile for other weeks)

# Before committing
make fmt              # Runs black + isort
make lint             # Runs flake8

# Or use pre-commit hooks
pre-commit install
pre-commit run --all-files
```

## CI/CD

- **Lint check** on every push/PR to main
- **Docker image** built and pushed to `mohitsharma44/python-for-kids` on Docker Hub with semantic version tags
- GitHub Actions workflow at `.github/workflows/ci.yml`
