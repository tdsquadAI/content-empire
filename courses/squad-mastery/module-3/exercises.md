# Module 3: Exercises

## Exercise 1: Run a Design Review

**Objective:** Practice the design review ceremony with your Squad team.

### Steps

1. Set up a scenario — you're adding a comments feature to a blog:
   ```
   Team, let's do a design review. We need to add a commenting system to 
   our blog. Requirements:
   - Users can leave comments on blog posts
   - Comments support nesting (replies)
   - Real-time updates when new comments appear
   - Spam filtering
   
   Keaton, present a proposal. Everyone provide feedback.
   ```

2. Observe the review:
   - Did Keaton propose an architecture?
   - Did McManus raise UI/UX concerns?
   - Did Verbal suggest backend approaches?
   - Did Fenster identify testing challenges?

3. Check `decisions.md` — are the review outcomes recorded?

4. Now implement based on the review:
   ```
   Team, implement the commenting system based on our design review decisions.
   ```

---

## Exercise 2: Parallel Fan-Out Experiment

**Objective:** Test different fan-out strategies and compare results.

### Steps

1. **Sequential approach** (baseline):
   ```
   McManus, create a header component with navigation.
   ```
   Wait for completion. Then:
   ```
   McManus, create a footer component with links.
   ```
   Wait for completion. Then:
   ```
   McManus, create a sidebar component with filters.
   ```
   Note the total time.

2. **Parallel approach:**
   ```
   Team, create three components in parallel:
   1. McManus: Header component with navigation
   2. McManus: Footer component with links  
   3. McManus: Sidebar component with filters
   ```
   Note the total time.

3. Compare: Was parallel execution faster? Were there any quality differences?

---

## Exercise 3: Set Up a Drop-Box

**Objective:** Use the drop-box pattern for agent-to-agent information sharing.

### Steps

1. Create the drop-box structure:
   ```bash
   mkdir -p .squad/dropbox/specs
   mkdir -p .squad/dropbox/handoffs
   ```

2. Have Keaton create a specification:
   ```
   Keaton, write a detailed API specification for a user management system 
   (CRUD operations) and save it to .squad/dropbox/specs/user-api.md
   ```

3. Have Verbal implement from the spec:
   ```
   Verbal, implement the API endpoints defined in .squad/dropbox/specs/user-api.md
   ```

4. Have Verbal create a handoff for Fenster:
   ```
   Verbal, write a test plan for the user API and save it to 
   .squad/dropbox/handoffs/user-api-test-plan.md
   ```

5. Have Fenster execute the test plan:
   ```
   Fenster, implement the tests described in 
   .squad/dropbox/handoffs/user-api-test-plan.md
   ```

6. Review the flow: Did each agent correctly produce and consume shared files?

---

## Exercise 4: Worktree Setup

**Objective:** Set up git worktrees for parallel feature development.

### Steps

1. Create two feature branches:
   ```bash
   git checkout -b feature/auth
   git checkout main
   git checkout -b feature/dashboard  
   git checkout main
   ```

2. Create worktrees:
   ```bash
   git worktree add ../my-project-auth feature/auth
   git worktree add ../my-project-dashboard feature/dashboard
   ```

3. Verify the setup:
   ```bash
   git worktree list
   ```

4. In the auth worktree, start Squad:
   ```bash
   cd ../my-project-auth
   copilot --yolo
   # McManus, create a login form component
   ```

5. In the dashboard worktree (new terminal), start Squad:
   ```bash
   cd ../my-project-dashboard
   copilot --yolo
   # McManus, create a dashboard layout with sidebar navigation
   ```

6. Check that both worktrees share the same `.squad/decisions.md`.

---

## Exercise 5: Orchestration Pattern Practice

**Objective:** Implement the "Feature Development" orchestration pattern end-to-end.

### Steps

1. Define a feature: "Add user profile pages with avatar upload"

2. Follow the pattern:

   **Step 1: Design Review**
   ```
   Keaton, design the user profile feature. Consider:
   - Profile page layout
   - Avatar upload and storage strategy
   - API endpoints needed
   - Data model changes
   Record your decisions.
   ```

   **Step 2: Fan-Out Implementation**
   ```
   Team, implement based on Keaton's design:
   - McManus: Profile page UI with avatar upload component
   - Verbal: Profile API endpoints + avatar storage
   - Kobayashi: Document the profile API
   ```

   **Step 3: Testing**
   ```
   Fenster, write integration tests for the profile feature — 
   both frontend component tests and API tests.
   ```

   **Step 4: Documentation**
   ```
   Kobayashi, update the project README with the new profile feature.
   ```

3. Review the full output:
   - Are all pieces consistent with each other?
   - Did decisions from the design review cascade to implementation?
   - Are tests aligned with the actual implementation?
