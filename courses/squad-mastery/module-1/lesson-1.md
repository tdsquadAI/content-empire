# Module 1: Getting Started with Squad

## What You'll Learn
- What Squad is and how it works
- Installing and initializing Squad in a project
- Understanding the core configuration files
- Running your first agent interaction

---

## Lesson 1: What Is Squad?

Squad is an open-source framework that gives you an AI development team through GitHub Copilot. Instead of a single chatbot, you get a team of specialized agents — each with their own identity, expertise, memory, and execution context.

### Key Concepts

| Concept | Description |
|---------|-------------|
| **Agent** | A specialized AI team member (e.g., Lead, Frontend, Backend, Tester) |
| **Coordinator** | The routing layer that dispatches work to the right agents |
| **Charter** | An agent's identity document — role, expertise, personality, voice |
| **History** | An agent's accumulated knowledge about YOUR project |
| **Casting** | The system that assigns persistent character names from movie universes |
| **Decisions** | A shared log where agents record architectural choices for the whole team |

### How It's Different

Most AI coding tools are **one agent, one context**. You paste code, get a response, lose context. Squad is fundamentally different:

1. **Multiple agents** run in separate execution contexts simultaneously
2. **Persistent memory** — agents remember what they learned across sessions
3. **Shared decisions** — one agent's choice informs all other agents
4. **Everything in git** — clone the repo, get the team with all accumulated knowledge
5. **Code-level guardrails** — file-write guards, PII scrubbing, rate limiting

---

## Lesson 2: Installation

### Prerequisites

Before installing Squad, you need:

- **Node.js** (v18 or later)
- **Git** (initialized repository)
- **GitHub CLI** (`gh`) — for issues, PRs, and Ralph features
- **GitHub Copilot** — CLI or VS Code extension

### Step 1: Create or Navigate to Your Project

```bash
# New project
mkdir my-project && cd my-project
git init

# Or use an existing project
cd /path/to/existing-project
```

**✓ Validate:** Run `git status` — you should see a valid git repository.

### Step 2: Install Squad

**Global install (recommended for frequent use):**
```bash
npm install -g @bradygaster/squad-cli
```

**Local project install:**
```bash
npm install --save-dev @bradygaster/squad-cli
```

**One-time use with npx:**
```bash
npx @bradygaster/squad-cli
```

**✓ Validate:** Run `squad --version` to confirm installation.

### Step 3: Initialize Squad

```bash
squad init
```

This creates the `.squad/` directory with your team configuration. The command is idempotent — safe to run multiple times without losing existing state.

**✓ Validate:** Check that `.squad/team.md` exists in your project.

### Step 4: Authenticate with GitHub

```bash
gh auth login
```

This enables Squad to work with GitHub issues, branches, and pull requests.

**✓ Validate:** Run `gh auth status` — you should see "Logged in to github.com".

### Step 5: Run Squad with Copilot

```bash
# Recommended: auto-approve tool calls
copilot --yolo
```

In the Copilot CLI, select the Squad agent and start talking:

```
I'm starting a new project. Set up the team.
Here's what I'm building: a task management app with React and Express.
```

Squad will propose a team. Type **yes** to confirm.

> **Why `--yolo`?** Squad makes many tool calls per session. Without `--yolo`, Copilot prompts you to approve each one, which breaks the flow of autonomous work.

---

## Lesson 3: Understanding the Configuration Files

After `squad init`, your project gets a `.squad/` directory. Here's what each file does:

### `team.md` — The Roster

This file lists every agent on your team with their role, name, and a brief description.

```markdown
## Team Roster

| Role | Agent | Expertise |
|------|-------|-----------|
| Lead | Keaton | Architecture, requirements, coordination |
| Frontend | McManus | UI/UX, React, CSS, accessibility |
| Backend | Verbal | APIs, databases, auth, infrastructure |
| Tester | Fenster | QA, test suites, edge cases, CI |
| Scribe | Kobayashi | Documentation, decisions, knowledge management |
```

**When to edit:** Add new roles, change agent assignments, update expertise descriptions.

### `routing.md` — Who Handles What

Routing rules tell the coordinator how to dispatch incoming requests.

```markdown
## Routing Rules

- Frontend tasks (UI, components, styling) → McManus
- Backend tasks (API, database, auth) → Verbal
- Architecture decisions → Keaton
- Testing and QA → Fenster
- Documentation → Kobayashi
- Ambiguous requests → Keaton (for triage)
```

**When to edit:** Customize routing for your project's specific needs.

### `decisions.md` — The Shared Brain

Every significant decision made by any agent is recorded here. This is how knowledge propagates across the team.

```markdown
## Decision Log

### 2025-01-15: Use PostgreSQL for primary database
**Author:** Keaton
**Reason:** Team expertise, ACID compliance, JSON support via JSONB
**Impact:** All database-related work should target PostgreSQL

### 2025-01-15: Use bcrypt for password hashing
**Author:** Verbal
**Reason:** Battle-tested, configurable work factor, resistant to rainbow tables
```

**When to edit:** Generally don't edit manually — let agents write decisions. But you can add decisions that represent pre-existing team choices.

### `ceremonies.md` — Sprint Ceremonies

Configuration for team ceremonies like design reviews and retrospectives.

### `agents/{name}/charter.md` — Agent Identity

Each agent has a charter that defines who they are:

```markdown
# McManus — Frontend Engineer

## Expertise
- React, TypeScript, Tailwind CSS
- Accessibility (WCAG 2.1 AA)
- Component architecture and design systems

## Voice
Direct, opinionated about UI/UX, favors simplicity

## Permissions
- Can write to: src/components/**, src/styles/**, src/pages/**
- Cannot modify: server/**, database/**
```

### `agents/{name}/history.md` — Agent Memory

Accumulated learnings about YOUR project:

```markdown
# McManus History

## Learnings
- Project uses Tailwind v4 with dark mode via class strategy
- Design system is built on shadcn/ui components
- All forms use react-hook-form with zod validation
- Color palette defined in tailwind.config.ts
```

---

## Lesson 4: Your First Team Interaction

Let's do a complete first interaction with your Squad team.

### Step 1: Start Copilot

```bash
copilot --yolo
```

### Step 2: Tell Squad About Your Project

```
Team, I'm building a recipe sharing app. Here's what I need:
- Users can sign up and log in
- Users can create, edit, and delete recipes
- Recipes have a title, ingredients list, and instructions
- Users can search recipes by ingredient
- Tech stack: React frontend, Express backend, PostgreSQL database
```

### Step 3: Watch the Team Work

The coordinator will:
1. Route the high-level architecture to Keaton (Lead)
2. Fan out frontend component planning to McManus
3. Send API design to Verbal (Backend)
4. Have Fenster start a test plan
5. Kobayashi logs all decisions

### Step 4: Review the Output

After the team finishes:
- Check `decisions.md` for architectural choices made
- Browse `agents/*/history.md` for what each agent learned
- Look at the actual code files created
- Review any test files generated

### Step 5: Iterate

```
McManus, the recipe card component needs a photo upload feature.
Verbal, add pagination to the recipe search endpoint — 20 per page.
```

You can address agents directly by name, or describe the work and let the coordinator route it.

---

## Key Takeaways

1. **Squad turns one AI into a team** — specialized agents working in parallel
2. **Installation is one command** — `npm install -g @bradygaster/squad-cli && squad init`
3. **Configuration is markdown** — human-readable, git-friendly, easy to customize
4. **Knowledge persists** — agents remember across sessions via history files
5. **Everything is in git** — clone the repo, get the entire team with accumulated knowledge
