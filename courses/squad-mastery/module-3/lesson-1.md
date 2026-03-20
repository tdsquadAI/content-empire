# Module 3: Advanced Orchestration

## What You'll Learn
- How to run team ceremonies (design reviews, retrospectives)
- Parallel fan-out strategies for maximum throughput
- The drop-box pattern for shared file access
- Working with git worktrees for isolation

---

## Lesson 1: Ceremonies — Design Reviews and Retrospectives

Squad supports structured team interactions called **ceremonies**. These are defined in `.squad/ceremonies.md` and provide a framework for recurring team activities.

### Design Reviews

A design review brings multiple agents together to evaluate a proposed approach before implementation begins.

**How to trigger a design review:**
```
Team, let's do a design review. We need to add real-time notifications 
to the app. Keaton, present a proposal. Everyone else, give feedback.
```

**What happens:**
1. Keaton (Lead) presents the architectural proposal
2. McManus (Frontend) evaluates UI/UX implications
3. Verbal (Backend) evaluates infrastructure requirements
4. Fenster (Tester) identifies testability concerns
5. All feedback is recorded in `decisions.md`

**Configuring ceremonies in `ceremonies.md`:**
```markdown
## Design Reviews
- Trigger: Before any feature that touches 3+ files
- Required participants: Lead, relevant specialists
- Output: Decision entry + implementation plan
- Duration: 1 round of feedback per agent

## Retrospectives
- Trigger: After every 5 completed tasks
- Participants: All agents
- Output: Updated team conventions, new skills
- Focus: What worked, what didn't, what to change
```

### Retrospectives

Retrospectives let the team reflect on recent work:

```
Team, let's do a retro on the last sprint. What worked well? 
What should we change? What patterns should we document?
```

**Valuable retro outputs:**
- New skills written to `.squad/skills/`
- Updated conventions in agent histories
- Routing rule refinements
- Decision log entries for process changes

---

## Lesson 2: Parallel Fan-Out Strategies

The key to Squad's productivity is parallel execution. Here are strategies to maximize it.

### Strategy 1: Independent Task Batching

When tasks have no dependencies, batch them for simultaneous execution:

```
Team, here are three independent tasks:
1. McManus: Create a user profile page component
2. Verbal: Add a PATCH /api/users/:id endpoint for profile updates
3. Fenster: Write unit tests for the existing auth middleware
```

All three agents work simultaneously. The coordinator collects results as each finishes.

### Strategy 2: Design-First Fan-Out

Have the lead agent design the approach, then fan out implementation:

```
Step 1: Keaton, design the notification system architecture.
Step 2: Based on Keaton's design, everyone implement your part.
```

This is a **sync-then-parallel** pattern — Keaton works first (sync), then all specialists work in parallel.

### Strategy 3: Pipeline Fan-Out

For features that have a natural workflow, use pipeline stages:

```
Stage 1 (parallel): 
  - Keaton: Define API contracts
  - McManus: Create UI wireframes/component structure

Stage 2 (parallel, after Stage 1):
  - Verbal: Implement APIs from Keaton's contracts
  - McManus: Implement components from wireframes

Stage 3 (parallel, after Stage 2):
  - Fenster: Test APIs
  - Fenster: Test UI components
  - Kobayashi: Write documentation
```

### Strategy 4: Competitive Fan-Out

For design decisions, have multiple agents propose approaches:

```
Team, I need a caching strategy. Keaton and Verbal, each propose an 
approach. Then we'll decide which one to go with.
```

This generates multiple options, letting you pick the best one.

### Fan-Out Performance Tips

| Tip | Why |
|-----|-----|
| Give each agent clear, bounded tasks | Reduces overlap and conflicts |
| Avoid tasks that write to the same files | Prevents merge conflicts |
| Use decisions.md for shared context | Better than duplicating info in each task |
| Start with 3-4 parallel agents max | Diminishing returns above 5 |

---

## Lesson 3: The Drop-Box Pattern

When agents need to share files — drafts, specs, data — use the **drop-box pattern**.

### The Problem

Agents run in separate contexts. Agent A can't directly pass data to Agent B. If both agents need the same reference document, how do they share it?

### The Solution: A Shared Directory

Create a drop-box directory in your project:

```bash
mkdir -p .squad/dropbox
```

**Producer agent** writes files to the drop-box:
```
Keaton, write the API specification to .squad/dropbox/api-spec.md
```

**Consumer agent** reads from the drop-box:
```
Verbal, implement the endpoints defined in .squad/dropbox/api-spec.md
```

### Drop-Box Conventions

```
.squad/dropbox/
├── specs/              # Design specifications
│   ├── api-v2.md
│   └── auth-flow.md
├── reviews/            # Code review notes
│   └── pr-42-feedback.md
├── data/               # Shared data files
│   └── test-fixtures.json
└── handoffs/           # Agent-to-agent handoffs
    └── verbal-to-fenster-auth-tests.md
```

### Best Practices

1. **Name files descriptively** — include the source agent and purpose
2. **Clean up after use** — remove files once they've been consumed
3. **Use for structured data** — specs, schemas, test fixtures
4. **Don't overuse** — decisions.md is better for simple decisions

---

## Lesson 4: Worktree Awareness

Squad is aware of git worktrees, enabling advanced multi-branch workflows.

### What Are Git Worktrees?

Git worktrees let you check out multiple branches simultaneously in different directories:

```bash
# Main branch in the original directory
git worktree add ../feature-auth feature/auth
git worktree add ../feature-dashboard feature/dashboard
```

### Squad + Worktrees

Squad can work across worktrees, meaning different agents can work on different branches simultaneously:

```
# In the main worktree
Verbal: Working on API improvements on main

# In the feature-auth worktree  
McManus: Building auth UI on feature/auth branch

# In the feature-dashboard worktree
Keaton: Designing dashboard on feature/dashboard branch
```

### Setting Up Worktree-Aware Squad

1. **Initialize Squad in the main worktree** — the `.squad/` directory lives at the root
2. **Worktrees share the same `.squad/` configuration** — all agents have the same team context
3. **Each worktree has its own working copy** — agents in different worktrees modify different files

### Benefits

| Benefit | Description |
|---------|-------------|
| Branch isolation | Each feature gets its own directory — no switching branches |
| Parallel development | Multiple features progress simultaneously |
| Shared decisions | All worktrees read the same `decisions.md` |
| Clean PRs | Each worktree produces a clean, focused PR |

### Practical Workflow

```bash
# Set up worktrees
git worktree add ../project-auth feature/auth
git worktree add ../project-dashboard feature/dashboard

# In main worktree: Verbal handles API work
cd /path/to/main
copilot --yolo
# "Verbal, refactor the API response middleware"

# In auth worktree: McManus handles auth UI
cd ../project-auth
copilot --yolo
# "McManus, build the login and registration pages"

# Both agents work independently, sharing decisions
```

---

## Lesson 5: Orchestration Patterns Cookbook

Here are proven patterns for common scenarios:

### Pattern: Feature Development

```
1. Keaton: Design review → decisions.md
2. Fan-out:
   ├── McManus: Build UI components
   ├── Verbal: Build API endpoints
   └── Kobayashi: Write API documentation
3. Fenster: Integration testing
4. Kobayashi: Update changelog
```

### Pattern: Bug Fix

```
1. Fenster: Reproduce and isolate the bug → .squad/dropbox/bug-report.md
2. Keaton: Root cause analysis → decisions.md (fix approach)
3. Verbal or McManus: Implement fix (based on bug location)
4. Fenster: Verify fix + regression test
```

### Pattern: Code Review

```
1. Keaton: Review PR diff → feedback in dropbox/
2. Fan-out feedback to relevant agents:
   ├── McManus: Address UI feedback
   └── Verbal: Address API feedback
3. Fenster: Re-run test suite
4. Keaton: Final approval
```

### Pattern: Documentation Sprint

```
Fan-out (all parallel):
├── Kobayashi: API reference docs
├── McManus: Component storybook entries
├── Verbal: Database schema docs
└── Keaton: Architecture decision records
```
