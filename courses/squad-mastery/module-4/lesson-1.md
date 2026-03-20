# Module 4: Ralph & Autonomous Work

## What You'll Learn
- What Ralph is and how to set it up
- GitHub Issues Mode for auto-triaging and processing issues
- PRD Mode for spec-to-shipped-code workflows
- Idle-watch polling and state management

---

## Lesson 1: What Is Ralph?

Ralph is Squad's **work monitor** — a persistent agent session that watches for work, triages it, and dispatches it to the right agents. Think of Ralph as a project manager who never sleeps.

### Ralph's Core Loop

```
┌─────────────────────────────────────────┐
│              RALPH'S LOOP               │
│                                         │
│  1. Scan for work (GitHub issues, PRDs) │
│  2. Triage: What needs doing?           │
│  3. Route: Which agent handles this?    │
│  4. Spawn: Launch agents                │
│  5. Monitor: Watch progress             │
│  6. Collect: Gather results             │
│  7. Ship: Create branches, PRs          │
│  8. Go to 1                             │
│                                         │
└─────────────────────────────────────────┘
```

### What Makes Ralph Different

Ralph isn't a simple cron job. It's an intelligent agent with:

- **State persistence** — remembers which issues it's processed
- **Event subscriptions** — reacts to completions, errors, and blockers
- **Crash recovery** — picks up exactly where it left off
- **Context awareness** — reads team decisions and history before dispatching

---

## Lesson 2: Setting Up Ralph

### Prerequisites

```bash
# GitHub CLI authenticated
gh auth login
gh auth status  # verify: "Logged in to github.com"

# Squad initialized
squad init

# Repository has GitHub issues enabled
```

### Starting Ralph

**Basic start (10-minute polling):**
```bash
squad triage
```

**Custom polling interval:**
```bash
squad triage --interval 5  # Poll every 5 minutes
```

**Using aliases:**
```bash
squad watch      # Same as squad triage
squad loop       # Same as squad triage
```

### What Ralph Does on First Run

1. Connects to your GitHub repository
2. Scans open issues
3. Reads your team's `routing.md` to understand capabilities
4. Begins the triage loop

### Ralph's Output

When Ralph is running, you'll see:

```
🔍 Ralph scanning issues... (interval: 5 minutes)
📋 Found 3 new issues
  #42 "Add user profile endpoint" → Backend (Verbal)
  #43 "Fix mobile nav z-index" → Frontend (McManus)  
  #44 "Add unit tests for auth" → Testing (Fenster)
🚀 Spawning agents...
  ✅ Verbal: Working on #42
  ✅ McManus: Working on #43
  ✅ Fenster: Working on #44
⏳ Waiting for results...
```

---

## Lesson 3: GitHub Issues Mode

This is Ralph's primary mode — watching GitHub issues and turning them into completed work.

### How Issues Get Triaged

Ralph reads each issue and determines:

1. **Type of work** — frontend, backend, testing, documentation?
2. **Priority** — based on labels, milestone, age
3. **Complexity** — simple fix vs. multi-agent feature
4. **Dependencies** — does this need other work to finish first?

### Issue Labels That Help Ralph

Set up labels that align with your team's routing:

| Label | Ralph's Action |
|-------|---------------|
| `frontend` | Routes to McManus |
| `backend` | Routes to Verbal |
| `bug` | Routes to Fenster for reproduction, then fix agent |
| `documentation` | Routes to Kobayashi |
| `design-needed` | Routes to Keaton for design review first |
| `squad-ready` | Explicitly flagged for Squad processing |

### The Issue-to-PR Lifecycle

```
GitHub Issue (#42: "Add user profile endpoint")
    ↓
Ralph triages → Backend task → Verbal
    ↓
Verbal reads issue + team context
    ↓
Branch created: feature/user-profile-42
    ↓
Verbal implements endpoint
    ↓
Verbal routes testing to Fenster
    ↓
Fenster writes and runs tests
    ↓
PR created: "Implement user profile endpoint (#42)"
    ↓
PR description includes:
  - What was done
  - Decisions made
  - Test results
  - Link to original issue
    ↓
Waiting for human review → Merge
```

### Example: Full Issue Processing

**Issue #42:**
```markdown
## Add user profile endpoint

GET /api/users/:id should return the user's profile data including:
- name, email, avatar URL
- join date
- recipe count

Should require authentication.
```

**Ralph's processing:**
```
🔍 Processing issue #42...
📋 Analysis: Backend API task, requires auth
🎯 Routing to Verbal (Backend)
🚀 Spawning Verbal...

Verbal's work:
  ✅ Created src/routes/users.ts
  ✅ Added GET /api/users/:id handler
  ✅ Integrated with auth middleware
  ✅ Added input validation
  ✅ Decision: Return 404 for non-existent users (not 403)
  
🔗 Routing to Fenster for testing...

Fenster's work:
  ✅ Created tests/routes/users.test.ts
  ✅ Tests: auth required, valid profile, user not found, invalid ID
  ✅ All tests passing

📦 Creating PR...
  Branch: feature/user-profile-42
  PR #15: "Implement user profile endpoint (#42)"
  Status: Ready for review
```

---

## Lesson 4: PRD Mode — From Spec to Shipped Code

PRD (Product Requirements Document) Mode lets you give Ralph a full specification, and it orchestrates the entire team to deliver the feature.

### Creating a PRD

Create a markdown file with your requirements:

```markdown
# PRD: Recipe Search Feature

## Overview
Users should be able to search recipes by ingredient, cuisine type, 
and cooking time.

## Requirements

### Search API
- GET /api/recipes/search
- Query params: ingredients (comma-separated), cuisine, maxTime
- Returns paginated results (20 per page)
- Full-text search on recipe title and description

### Search UI
- Search bar with auto-complete for ingredients
- Filter sidebar for cuisine and cooking time
- Results grid with recipe cards
- Infinite scroll pagination

### Testing
- API endpoint tests with various query combinations
- UI component tests for search bar, filters, results
- Performance test: search should return in < 200ms

## Acceptance Criteria
- [ ] Search returns relevant results for ingredient queries
- [ ] Filters can be combined (ingredient + cuisine + time)
- [ ] Empty results show a helpful message
- [ ] Mobile responsive
```

### Running PRD Mode

```bash
# Point Ralph at the PRD
squad triage --prd docs/prd-recipe-search.md
```

### How Ralph Processes a PRD

```
PRD Loaded: "Recipe Search Feature"
    ↓
Keaton: Architecture review
  - Database indexing strategy
  - API design decisions
  - Component breakdown
    ↓
Fan-out:
  ├── Verbal: Search API implementation
  ├── McManus: Search UI components
  └── Kobayashi: API documentation
    ↓
Follow-up:
  ├── Fenster: Integration tests
  └── Fenster: Performance tests
    ↓
Final:
  - PR created with all changes
  - Acceptance criteria checked
  - PRD updated with completion status
```

---

## Lesson 5: State Management and Crash Recovery

### Ralph's State File

Ralph persists its state to `.squad/ralph-state.json`:

```json
{
  "lastScan": "2025-01-20T15:30:00Z",
  "processedIssues": [42, 43, 44],
  "activeWork": {
    "45": {
      "agent": "Verbal",
      "status": "in-progress",
      "startedAt": "2025-01-20T15:25:00Z",
      "branch": "feature/notifications-45"
    }
  },
  "pendingReview": [15, 16],
  "stats": {
    "issuesProcessed": 12,
    "prsCreated": 8,
    "totalWorkTime": "4h 32m"
  }
}
```

### Crash Recovery

If Ralph crashes (network timeout, model error, process killed):

1. On restart, Ralph reads `ralph-state.json`
2. Knows which issues are already processed
3. Resumes in-progress work from last checkpoint
4. Doesn't duplicate completed work

```bash
# Ralph crashed at 2 AM
# You restart it at 8 AM

squad triage --interval 5

# Ralph output:
# 🔄 Resuming from state...
# ✅ Issues 42-44: Already completed
# ⚠️ Issue 45: In progress — checking status...
# 🔧 Issue 45: Branch exists, resuming from checkpoint
```

### Event Monitoring

Ralph exposes events you can subscribe to programmatically:

```typescript
// Using the SDK
const ralph = new RalphMonitor({
  teamRoot: '.squad',
  healthCheckInterval: 30000,
  statePath: '.squad/ralph-state.json',
});

ralph.subscribe('agent:task-complete', (event) => {
  console.log(`✅ ${event.agentName} finished: ${event.task}`);
  // Send Slack notification, update dashboard, etc.
});

ralph.subscribe('agent:error', (event) => {
  console.log(`❌ ${event.agentName} failed: ${event.error}`);
  // Alert on-call engineer
});

ralph.subscribe('pr:created', (event) => {
  console.log(`📦 PR #${event.prNumber}: ${event.title}`);
  // Notify reviewers
});

await ralph.start();
```

### Idle-Watch Polling

Ralph uses a smart polling strategy:

- **Active period** (recent activity): Polls every N minutes (your configured interval)
- **Quiet period** (no new work): Gradually increases interval to conserve resources
- **On new work detected**: Immediately returns to active polling

```
Active:  ──5m──5m──5m──5m──
                            └─ No new issues for 30m
Quiet:   ────10m────15m────20m────
                                  └─ New issue detected!
Active:  ──5m──5m──5m──
```

This prevents Ralph from burning API rate limits when there's no work to do.
