# Module 2: Quiz — The Agent Lifecycle

## Question 1
When the coordinator receives a request, what is the first thing it does?

- A) Randomly assigns it to an available agent
- B) Reads `routing.md` to match the request to the right agent(s)
- C) Asks the user which agent should handle it
- D) Sends it to all agents simultaneously

**Answer:** B) Reads `routing.md` to match the request to the right agent(s)
**Explanation:** The coordinator uses routing rules defined in `routing.md` to determine which agent(s) should handle a request based on the type of work described.

---

## Question 2
What information does an agent receive when it's spawned?

- A) Only the user's original message
- B) Charter, task, history, relevant decisions, and skills
- C) The entire `.squad/` directory contents
- D) Just its charter and the task description

**Answer:** B) Charter, task, history, relevant decisions, and skills
**Explanation:** Each agent receives its identity (charter), the specific task, its accumulated knowledge (history), relevant team decisions, and any applicable skills — giving it full context without unnecessary information.

---

## Question 3
How do agents communicate with each other?

- A) Direct messaging between agent contexts
- B) Through shared files: decisions.md, routing via squad_route, and history files
- C) WebSocket connections between agent processes
- D) They share the same execution context

**Answer:** B) Through shared files: decisions.md, routing via squad_route, and history files
**Explanation:** Agents never talk directly. They communicate through: (1) decisions.md — shared decision log, (2) squad_route — handing off tasks, (3) history files — accumulated knowledge. This is an indirect, file-based communication model.

---

## Question 4
When should you use sync mode instead of background (parallel) mode?

- A) Always — sync mode is always more reliable
- B) When later tasks depend on the results of earlier tasks
- C) When you want the fastest possible execution
- D) Only for testing purposes

**Answer:** B) When later tasks depend on the results of earlier tasks
**Explanation:** Sync mode ensures that dependent work happens in the right order. For example, architecture review should complete before implementation starts, because the review's decisions inform how agents implement.

---

## Question 5
What is the `squad_route` tool used for?

- A) Configuring URL routing for a web application
- B) Handing off a task from one agent to another
- C) Setting up network routing between servers
- D) Defining the coordinator's routing rules

**Answer:** B) Handing off a task from one agent to another
**Explanation:** `squad_route` allows one agent to route work to another. For example, Verbal (backend) can route testing work to Fenster (tester) after finishing API endpoints, creating chained workflows.

---

## Question 6
What is the difference between agent history and agent skills?

- A) There is no difference — they're the same thing
- B) History is project-specific knowledge; skills are reusable patterns across projects
- C) History is written by the user; skills are written by agents
- D) History is public; skills are private

**Answer:** B) History is project-specific knowledge; skills are reusable patterns across projects
**Explanation:** History (`history.md`) contains learnings specific to your project ("this project uses Tailwind v4"). Skills (`skills/`) contain reusable patterns that could apply to any project ("here's how to set up JWT auth in Express").

---

## Question 7
What happens when an agent makes a decision using `squad_decide`?

- A) The decision is emailed to the project lead
- B) An entry is written to `decisions.md` that all agents read before future work
- C) The decision is stored only in that agent's memory
- D) A GitHub issue is created for human review

**Answer:** B) An entry is written to `decisions.md` that all agents read before future work
**Explanation:** The `squad_decide` tool writes decisions to the shared decision log. Since all agents read `decisions.md` before starting work, one agent's decision cascades to the entire team.

---

## Question 8
True or False: Each agent runs in the same execution context and shares memory with other agents.

**Answer:** False
**Explanation:** Each agent runs in its own separate execution context. They do NOT share memory. Communication happens through files (decisions.md, history.md, skills). This isolation prevents agents from interfering with each other.

---

## Question 9
How does knowledge compound across sessions?

- A) It doesn't — each session starts completely fresh
- B) Agents write learnings to history.md, which is read at the start of each new session
- C) Knowledge is stored in the cloud and downloaded each session
- D) The coordinator memorizes everything internally

**Answer:** B) Agents write learnings to history.md, which is read at the start of each new session
**Explanation:** During each session, agents write what they learned to `history.md`. In the next session, they read this file before starting, giving them accumulated project knowledge. Over time, agents know your conventions, preferences, and patterns without being told.

---

## Question 10
You can manually inject decisions into `decisions.md` for agents to follow. When is this most useful?

- A) Never — only agents should write decisions
- B) When you have pre-existing architectural choices that agents must respect
- C) When agents are making wrong decisions
- D) When starting a new project without any history

**Answer:** B) When you have pre-existing architectural choices that agents must respect
**Explanation:** Adding manual decisions is the best way to communicate existing constraints to your team. For example, "We use PostgreSQL" or "All API responses follow JSON:API format." Agents will read and follow these decisions.
