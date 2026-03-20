# Module 1: Exercises

## Exercise 1: Install and Initialize Squad

**Objective:** Get Squad running in a new project.

### Steps

1. Create a new directory and initialize git:
   ```bash
   mkdir squad-playground && cd squad-playground
   git init
   ```

2. Install Squad:
   ```bash
   npm install -g @bradygaster/squad-cli
   ```

3. Initialize Squad:
   ```bash
   squad init
   ```

4. Verify the installation:
   ```bash
   ls .squad/
   ```

**Expected outcome:** You should see `team.md`, `routing.md`, `decisions.md`, `ceremonies.md`, and an `agents/` directory.

---

## Exercise 2: Explore the Configuration Files

**Objective:** Understand what each configuration file contains.

### Steps

1. Open and read each file:
   ```bash
   cat .squad/team.md
   cat .squad/routing.md
   cat .squad/decisions.md
   ```

2. Open an agent's charter:
   ```bash
   # List agents
   ls .squad/agents/
   
   # Read one charter
   cat .squad/agents/*/charter.md
   ```

3. Answer these questions:
   - How many agents are on the default team?
   - What role does the scribe play?
   - What movie universe are the agent names from?

---

## Exercise 3: Your First Team Interaction

**Objective:** Have Squad's team work on a simple task.

### Steps

1. Start Copilot with auto-approve:
   ```bash
   copilot --yolo
   ```

2. Select the Squad agent.

3. Give the team a simple task:
   ```
   Team, create a simple Express.js server with:
   - A GET /health endpoint that returns { status: "ok" }
   - A GET /time endpoint that returns the current timestamp
   ```

4. Watch the agents work. Note which agent handles what.

5. After completion, check:
   ```bash
   cat .squad/decisions.md
   ```

**Expected outcome:** You should see actual code files created and decisions recorded in the log.

---

## Exercise 4: Direct Agent Communication

**Objective:** Learn to address specific agents.

### Steps

1. In your Squad session, address agents directly:
   ```
   Keaton, what's the best way to structure this project for scalability?
   ```

2. Then try:
   ```
   McManus, create a simple HTML page that displays "Hello, Squad!" with basic CSS styling.
   ```

3. Finally:
   ```
   Fenster, write tests for whatever McManus just created.
   ```

4. Compare the responses — notice how each agent has a different voice and approach.

---

## Exercise 5: Customize Your Team

**Objective:** Modify the team configuration for a specific project type.

### Steps

1. Edit `.squad/routing.md` to add a custom routing rule:
   ```markdown
   - Game-related tasks (sprites, physics, game loops) → McManus
   - Sound and music tasks → Verbal
   ```

2. Edit an agent's charter to add project-specific expertise:
   ```markdown
   # In .squad/agents/{frontend-agent}/charter.md
   ## Additional Expertise
   - HTML5 Canvas game rendering
   - Sprite animation systems
   - Pixel art workflows
   ```

3. Start a new session and test the customized routing:
   ```
   Team, build a simple Pong game in HTML5 Canvas.
   ```

4. Verify that the custom routing is being used by checking the orchestration log.

**Expected outcome:** Your customized routing rules should direct game tasks to the appropriate agents.
