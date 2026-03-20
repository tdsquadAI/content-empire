# Module 2: Exercises

## Exercise 1: Trace the Agent Lifecycle

**Objective:** Understand exactly what happens when Squad processes a request.

### Steps

1. Start a Squad session:
   ```bash
   copilot --yolo
   ```

2. Give a simple task:
   ```
   Team, create a utility function that validates email addresses.
   ```

3. Watch the output carefully and answer:
   - Which agent(s) were spawned?
   - What information was loaded for each agent?
   - Did agents work in parallel or sequentially?
   - Were any decisions recorded?

4. Check the orchestration evidence:
   ```bash
   cat .squad/decisions.md
   cat .squad/agents/*/history.md
   ```

---

## Exercise 2: Parallel vs Sequential Work

**Objective:** See the difference between parallel and sequential agent execution.

### Steps

1. Give a task that triggers parallel work:
   ```
   Team, build a contact form with a frontend component, a backend API endpoint, and tests for both.
   ```

2. Observe: multiple agents should work simultaneously.

3. Now give a task that requires sequential work:
   ```
   Keaton, first review our current project structure and decide on a folder convention. 
   Then have McManus create a new component following that convention.
   ```

4. Compare the two flows. How did timing differ?

---

## Exercise 3: Decision Cascading

**Objective:** See how one agent's decision affects another agent's work.

### Steps

1. Manually add a decision to `decisions.md`:
   ```markdown
   ### 2025-01-20: All API responses must follow JSON:API specification
   **Author:** Human
   **Reason:** Standardization across all endpoints
   **Impact:** Every API endpoint must return data in JSON:API format
   ```

2. Now ask Verbal to create an endpoint:
   ```
   Verbal, create a GET /api/users endpoint that returns a list of users.
   ```

3. Check: Did Verbal follow the JSON:API specification from the decision log?

4. Then ask McManus:
   ```
   McManus, create a component that displays the user list from /api/users.
   ```

5. Check: Did McManus handle the JSON:API response format correctly?

---

## Exercise 4: Agent History Inspection

**Objective:** Understand how agent knowledge accumulates.

### Steps

1. Check current agent histories:
   ```bash
   for f in .squad/agents/*/history.md; do echo "=== $f ==="; cat "$f"; echo; done
   ```

2. Run three different tasks in the same session:
   ```
   McManus, create a button component with primary, secondary, and danger variants.
   McManus, create a card component that uses the button component.
   McManus, create a modal component with a close button.
   ```

3. After each task, check McManus's history:
   ```bash
   cat .squad/agents/*/history.md
   ```

4. Does McManus's history grow? Does it reference patterns from previous tasks?

---

## Exercise 5: Manual Skill Creation

**Objective:** Create a reusable skill that agents can reference.

### Steps

1. Create a skills directory if it doesn't exist:
   ```bash
   mkdir -p .squad/skills/api-patterns
   ```

2. Create a skill file:
   ```bash
   cat > .squad/skills/api-patterns/SKILL.md << 'EOF'
   # API Patterns
   
   ## Standard Response Format
   All API responses should follow this structure:
   ```json
   {
     "success": true,
     "data": { ... },
     "meta": { "timestamp": "ISO-8601", "version": "1.0" }
   }
   ```
   
   ## Error Response Format
   ```json
   {
     "success": false,
     "error": { "code": "NOT_FOUND", "message": "Resource not found" },
     "meta": { "timestamp": "ISO-8601" }
   }
   ```
   
   ## Confidence: High
   EOF
   ```

3. Ask Verbal to create an endpoint and see if the skill influences the response format:
   ```
   Verbal, create a GET /api/products endpoint.
   ```

4. Compare the output against your skill definition.
