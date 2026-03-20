# Module 1: Quiz — Getting Started with Squad

## Question 1
What is the primary command to initialize Squad in a project?

- A) `squad start`
- B) `squad init`
- C) `squad setup`
- D) `squad new`

**Answer:** B) `squad init`
**Explanation:** `squad init` scaffolds the `.squad/` directory with team configuration files. It's idempotent, meaning it's safe to run multiple times.

---

## Question 2
Where does Squad store its team configuration?

- A) `~/.squad/` (home directory)
- B) `.ai-team/` (project root)
- C) `.squad/` (project root)
- D) `node_modules/@squad/config/`

**Answer:** C) `.squad/` (project root)
**Explanation:** Squad creates a `.squad/` directory in your project root. This directory is meant to be committed to git so anyone who clones the repo gets the team.

---

## Question 3
What is the purpose of `decisions.md`?

- A) A list of tasks for the team to complete
- B) A shared log of architectural decisions made by any agent
- C) The routing table for dispatching work
- D) A configuration file for the casting system

**Answer:** B) A shared log of architectural decisions made by any agent
**Explanation:** When any agent makes a significant decision, it's recorded in `decisions.md`. All agents read this file before working, ensuring decisions propagate across the team.

---

## Question 4
Why is the `--yolo` flag recommended when running Copilot with Squad?

- A) It enables experimental features
- B) It increases the model's creativity
- C) It auto-approves tool calls so agents can work without interruption
- D) It enables parallel agent execution

**Answer:** C) It auto-approves tool calls so agents can work without interruption
**Explanation:** Squad makes many tool calls in a typical session. Without `--yolo`, Copilot would prompt you to approve each one, breaking the flow of autonomous work.

---

## Question 5
What is "casting" in Squad?

- A) A process that compiles TypeScript to JavaScript
- B) A system that assigns persistent character names from movie universes to agents
- C) A way to deploy agents to production
- D) A testing framework for agent responses

**Answer:** B) A system that assigns persistent character names from movie universes to agents
**Explanation:** The casting system gives agents memorable, persistent names from movie universes (e.g., The Usual Suspects). The same agent keeps the same name across sessions, helping developers build familiarity.

---

## Question 6
What file defines an individual agent's identity, expertise, and permissions?

- A) `team.md`
- B) `routing.md`
- C) `agents/{name}/charter.md`
- D) `agents/{name}/history.md`

**Answer:** C) `agents/{name}/charter.md`
**Explanation:** The charter is an agent's identity document — it defines their role, expertise areas, personality, voice, and file permissions.

---

## Question 7
What happens to an agent's knowledge between sessions?

- A) It's lost — each session starts fresh
- B) It's stored in the cloud and synchronized
- C) It persists in `history.md` files committed to git
- D) It's cached in `node_modules/`

**Answer:** C) It persists in `history.md` files committed to git
**Explanation:** Agents write their learnings to `agents/{name}/history.md`. This file persists across sessions and is committed to git, so anyone who clones the repo gets agents with accumulated project knowledge.

---

## Question 8
Which tool is required for Squad to work with GitHub issues and pull requests?

- A) Docker
- B) GitHub CLI (`gh`)
- C) GitHub Desktop
- D) Postman

**Answer:** B) GitHub CLI (`gh`)
**Explanation:** Squad uses the GitHub CLI (`gh`) for features like issue triage, branch creation, and pull request management. You need to authenticate with `gh auth login`.

---

## Question 9
True or False: You should NOT commit the `.squad/` directory to git.

**Answer:** False
**Explanation:** The `.squad/` directory should absolutely be committed to git. It contains the team configuration, agent knowledge, and decision history. Committing it means anyone who clones the repo gets the full team with all accumulated context.

---

## Question 10
What is the default movie universe used for agent names in Squad?

- A) Star Wars
- B) The Matrix
- C) The Usual Suspects
- D) Alien

**Answer:** C) The Usual Suspects
**Explanation:** The default casting universe is The Usual Suspects (1995). Agents get names like Keaton (lead), McManus (frontend), Verbal (backend), Fenster (tester), and Kobayashi (scribe).
