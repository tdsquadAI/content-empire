# Module 4: Exercises

## Exercise 1: Start Ralph for the First Time

**Objective:** Get Ralph running and watching your GitHub issues.

### Steps

1. Ensure prerequisites:
   ```bash
   gh auth status  # Should show "Logged in"
   squad status    # Should show active Squad
   ```

2. Create a test issue on your GitHub repo:
   ```bash
   gh issue create --title "Add health check endpoint" \
     --body "Create a GET /health endpoint that returns { status: 'ok', uptime: <seconds> }" \
     --label "backend"
   ```

3. Start Ralph:
   ```bash
   squad triage --interval 2
   ```

4. Watch Ralph pick up and process the issue.

5. Check results:
   ```bash
   gh pr list  # Should show a new PR
   cat .squad/ralph-state.json  # Should show processed issue
   ```

---

## Exercise 2: Multiple Issue Processing

**Objective:** See Ralph handle multiple issues in a single scan cycle.

### Steps

1. Create three issues with different types:
   ```bash
   gh issue create --title "Create About page" \
     --body "Simple about page with team info" --label "frontend"
   
   gh issue create --title "Add rate limiting to API" \
     --body "Implement rate limiting (100 req/min per IP)" --label "backend"
   
   gh issue create --title "Write API documentation" \
     --body "Document all existing endpoints with examples" --label "documentation"
   ```

2. Start Ralph:
   ```bash
   squad triage --interval 2
   ```

3. Observe which agent Ralph assigns to each issue.

4. Track progress:
   ```bash
   # Check Ralph's state
   cat .squad/ralph-state.json
   
   # Check for new branches
   git branch -a
   
   # Check for PRs
   gh pr list
   ```

---

## Exercise 3: Crash Recovery Test

**Objective:** Verify Ralph resumes correctly after interruption.

### Steps

1. Start Ralph:
   ```bash
   squad triage --interval 2
   ```

2. Wait for it to start processing an issue.

3. Kill Ralph mid-processing (Ctrl+C).

4. Check the state file:
   ```bash
   cat .squad/ralph-state.json
   ```

5. Restart Ralph:
   ```bash
   squad triage --interval 2
   ```

6. Verify:
   - Does Ralph recognize already-processed issues?
   - Does it resume in-progress work?
   - Does it avoid duplicating completed work?

---

## Exercise 4: PRD-Driven Development

**Objective:** Use a PRD to drive a full feature implementation.

### Steps

1. Create a PRD file:
   ```bash
   mkdir -p docs
   cat > docs/prd-todo-api.md << 'EOF'
   # PRD: Todo List API
   
   ## Overview
   A RESTful API for managing todo items.
   
   ## Requirements
   
   ### Endpoints
   - POST /api/todos - Create a todo
   - GET /api/todos - List all todos (with pagination)
   - GET /api/todos/:id - Get a specific todo
   - PATCH /api/todos/:id - Update a todo
   - DELETE /api/todos/:id - Delete a todo
   
   ### Data Model
   - id: UUID
   - title: string (required, max 200 chars)
   - description: string (optional)
   - completed: boolean (default: false)
   - createdAt: timestamp
   - updatedAt: timestamp
   
   ### Validation
   - Title is required and must be 1-200 characters
   - Description is optional, max 1000 characters
   
   ### Testing
   - Unit tests for each endpoint
   - Validation tests for invalid inputs
   - Pagination tests
   
   ## Acceptance Criteria
   - [ ] All CRUD operations work correctly
   - [ ] Input validation returns helpful error messages
   - [ ] Pagination works with page and limit params
   - [ ] Tests cover happy path and error cases
   EOF
   ```

2. Have the team process the PRD:
   ```
   Team, implement the feature described in docs/prd-todo-api.md
   ```

3. Review the output against the acceptance criteria.

---

## Exercise 5: Monitor Ralph's Event Stream

**Objective:** Observe Ralph's events and understand its decision-making.

### Steps

1. Start Ralph with verbose output:
   ```bash
   squad triage --interval 2
   ```

2. Create an issue that requires multiple agents:
   ```bash
   gh issue create --title "Add search functionality" \
     --body "Add a search bar to the UI and a search API endpoint. 
   Frontend should have autocomplete. Backend should support 
   full-text search." --label "feature"
   ```

3. Watch Ralph's event stream. Log the events you see:
   - Issue detection
   - Triage decision
   - Agent spawning
   - Task completion
   - PR creation

4. Check the decision log:
   ```bash
   cat .squad/decisions.md
   ```

5. Document: How did Ralph decide to split this between frontend and backend agents?
