# Module 2: The Agent Lifecycle

## What You'll Learn
- How agents are spawned and managed
- The difference between background and sync execution modes
- How agents communicate and share context
- Decision tracking and history management

---

## Lesson 1: How Agents Are Spawned

When you give Squad a task, the coordinator doesn't do the work itself. It analyzes the request, identifies which agents are needed, and spawns them — often in parallel.

### The Spawning Flow

```
User Request
    ↓
Coordinator reads routing.md
    ↓
Matches request to agent(s)
    ↓
For each matched agent:
    1. Load charter.md (identity + permissions)
    2. Load history.md (accumulated knowledge)
    3. Load relevant decisions from decisions.md
    4. Construct agent-specific prompt
    5. Spawn in separate execution context
    ↓
Agents work independently
    ↓
Results collected by coordinator
```

### What Each Agent Receives

When an agent is spawned, it gets:

- **Charter:** Its role, expertise, voice, and permissions
- **Task:** The specific work to do (from coordinator's routing)
- **Context:** Relevant project context, including recent decisions
- **History:** Everything this agent has previously learned about the project
- **Skills:** Compressed learnings from `.squad/skills/`

### The Coordinator's Role

The coordinator is the traffic controller. It:
1. Reads `routing.md` to determine which agent handles what
2. Breaks complex requests into sub-tasks
3. Fans out parallel work when possible
4. Chains follow-up tasks as results come in
5. Collects and synthesizes final results

```
"Build the login page"

Coordinator analysis:
├── Architecture decisions needed → Keaton (Lead)
├── UI component needed → McManus (Frontend)
├── Auth endpoints needed → Verbal (Backend)
├── Test cases needed → Fenster (Tester)
└── Log everything → Kobayashi (Scribe)
```

---

## Lesson 2: Background vs Sync Modes

Squad supports two execution modes for agents, and understanding the difference is important for effective use.

### Sync Mode

In sync mode, the coordinator waits for each agent to complete before moving on. This is useful for:
- Sequential workflows where later steps depend on earlier results
- Design reviews where Keaton must approve before implementation begins
- Critical decisions that need team consensus

```
Coordinator → Keaton: "Review the architecture"
[Waits for Keaton's response]
Keaton: "Approved. Use REST with Express."
Coordinator → McManus: "Build the UI" (now with Keaton's guidance)
Coordinator → Verbal: "Build the API" (now with Keaton's guidance)
```

### Background (Parallel) Mode

In background mode, multiple agents are spawned simultaneously. This is the default for independent tasks:

```
Coordinator → All agents (parallel):
├── McManus: "Build login form"        [running]
├── Verbal: "Build auth endpoints"     [running]
├── Fenster: "Write test plan"         [running]
└── Kobayashi: "Log decisions"         [running]

[All working simultaneously]
[Results collected as agents finish]
```

### When to Use Each

| Scenario | Mode | Why |
|----------|------|-----|
| Building independent features | Background | No dependencies between agents |
| Design review before coding | Sync | Implementation depends on review |
| Bug triage + fix | Sync | Need to understand before fixing |
| Testing existing code | Background | Tests can run independently |
| Architecture planning | Sync | Decisions cascade to all agents |

---

## Lesson 3: Agent Communication Patterns

Agents don't talk to each other directly. They communicate through three mechanisms:

### 1. The Decision Log (`decisions.md`)

When an agent makes a significant decision, it uses the `squad_decide` tool:

```typescript
squad_decide({
  author: 'Verbal',
  summary: 'Use JWT tokens for authentication',
  body: 'Chose JWT over session cookies because: (1) stateless, (2) works across services, (3) easy to validate on frontend',
  references: ['auth-design-task'],
});
```

This creates an entry in `decisions.md` that ALL agents read before starting work. It's the team's shared brain.

### 2. Task Routing (`squad_route`)

Agents can hand off work to other agents:

```typescript
squad_route({
  targetAgent: 'Fenster',
  task: 'Write integration tests for the auth endpoints I just created',
  priority: 'high',
  context: 'Endpoints: POST /auth/login, POST /auth/register, POST /auth/refresh',
});
```

This is how chained workflows happen — Verbal finishes the API, then routes testing work to Fenster.

### 3. History Files (`history.md`)

Agents write learnings to their own history for future sessions:

```typescript
squad_memory({
  agent: 'McManus',
  section: 'learnings',
  content: 'This project uses React 19 with Server Components. Forms use react-hook-form + zod.',
});
```

Next time McManus works on this project, it reads this history and already knows the setup.

---

## Lesson 4: Decision Tracking Deep Dive

The decision log is one of Squad's most powerful features. Here's how to use it effectively.

### How Decisions Cascade

```
Session 1:
  Keaton decides: "Use PostgreSQL"
  → Written to decisions.md

Session 2:
  Verbal reads decisions.md → Sees PostgreSQL decision
  → Creates database models for PostgreSQL (not MongoDB)
  → Decides: "Use Prisma as ORM"
  → Written to decisions.md

Session 3:
  McManus reads decisions.md → Sees PostgreSQL + Prisma decisions
  → Creates forms that match Prisma model shapes
  → No one had to tell McManus about the database choice
```

### Decision Entry Structure

A well-formed decision entry includes:

```markdown
### [Date]: [Summary]
**Author:** [Agent name]
**Reason:** [Why this choice was made]
**Alternatives considered:** [What was rejected and why]
**Impact:** [What this means for the rest of the project]
**References:** [Related tasks or prior decisions]
```

### Viewing Decision History

Decisions accumulate over time, creating a rich project history:

```bash
# View all decisions
cat .squad/decisions.md

# Search for specific decisions
grep -i "database" .squad/decisions.md
grep -i "authentication" .squad/decisions.md
```

### Manual Decision Injection

You can add decisions manually to steer the team:

```markdown
### 2025-01-20: Use Tailwind CSS, not styled-components
**Author:** Human (project lead)
**Reason:** Team standardization, performance, smaller bundle size
**Impact:** All UI work should use Tailwind utility classes
```

This is useful for pre-existing architectural choices that agents need to respect.

---

## Lesson 5: History and Knowledge Management

### How Agent History Works

Each agent maintains its own `history.md` file. This file grows across sessions:

```markdown
# McManus History

## Project Context
- React 19 with TypeScript
- Tailwind CSS v4 for styling
- shadcn/ui component library

## Patterns Learned
- Forms use react-hook-form with zod validation
- API calls go through a centralized `apiClient.ts`
- Error boundaries wrap each page component

## Known Issues
- Dark mode toggle causes flash of wrong theme on SSR
- Mobile nav drawer has z-index conflict with modals

## Conventions
- Components in PascalCase directories
- Hooks prefixed with `use`
- Tests co-located with components (ComponentName.test.tsx)
```

### Skills: Compressed Knowledge

Skills are reusable patterns extracted from work:

```markdown
# .squad/skills/auth-patterns/SKILL.md

## React Authentication Pattern

### Setup
1. Auth context provider wraps the app
2. useAuth() hook exposes: user, login, logout, isLoading
3. Protected routes check auth state and redirect

### Code Pattern
[code examples and templates]

### Confidence: High
Source: Implemented in 3 projects successfully
```

Skills are higher-level than history — they're transferable patterns that any project can benefit from.

### The Knowledge Lifecycle

```
Session Work → Agent Learnings → history.md (project-specific)
                              → skills/ (reusable patterns)
                              → decisions.md (team-wide choices)
```

Everything feeds back into the next session. Agents start each session by reading their charter, history, and recent decisions. The more they work, the more they know.
