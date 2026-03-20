# Mastering AI Agent Teams with Squad

**A comprehensive course on building, orchestrating, and scaling AI agent teams using the Squad framework.**

## Course Overview

Squad gives you an AI development team through GitHub Copilot. This course takes you from installation to running autonomous content pipelines — with hands-on exercises at every step.

**Prerequisites:**
- Node.js v18+
- Git
- GitHub CLI (`gh`)
- GitHub Copilot (CLI or VS Code)

**Time to complete:** ~8–10 hours

---

## Modules

### Module 1: Getting Started with Squad
- What Squad is and how it works
- Installing and initializing Squad
- Understanding `team.md`, `routing.md`, and `decisions.md`
- Your first team interaction

### Module 2: The Agent Lifecycle
- How agents are spawned with charters and history
- Background vs sync execution modes
- Agent communication patterns (decisions, routing, memory)
- Decision tracking and knowledge compounding

### Module 3: Advanced Orchestration
- Ceremonies: design reviews and retrospectives
- Parallel fan-out strategies for maximum throughput
- The drop-box pattern for inter-agent file sharing
- Git worktree awareness for multi-branch workflows

### Module 4: Ralph & Autonomous Work
- Setting up Ralph — the tireless work monitor
- GitHub Issues Mode: auto-triage to shipped PRs
- PRD Mode: from specification to working code
- State management and crash recovery

### Module 5: Building Your Own Content Empire
- Multi-brand setup and team customization
- Platform publishing automation pipelines
- Game development with AI agent teams
- Scaling from 1 to 21+ products

---

## Each Module Contains

- **lesson-1.md** — Written content with real code examples and configurations
- **exercises.md** — Hands-on tasks to practice what you learned
- **quiz.md** — Knowledge check questions with detailed explanations

---

## Quick Start

```bash
# Install Squad
npm install -g @bradygaster/squad-cli

# Create a project
mkdir my-project && cd my-project && git init

# Initialize Squad
squad init

# Start working
copilot --yolo
```

---

## Resources

- [Squad on GitHub](https://github.com/bradygaster/squad)
- [Squad npm package](https://www.npmjs.com/package/@bradygaster/squad-cli)
- TechAI Explained YouTube channel — video companion series
