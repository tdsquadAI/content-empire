# Module 3: Quiz — Advanced Orchestration

## Question 1
What is a "ceremony" in Squad?

- A) A deployment ritual that must happen before each release
- B) A structured team interaction like design reviews or retrospectives
- C) The process of casting agent names
- D) The initialization sequence when starting Squad

**Answer:** B) A structured team interaction like design reviews or retrospectives
**Explanation:** Ceremonies are defined in `ceremonies.md` and provide frameworks for recurring team activities like design reviews (evaluating proposals before implementation) and retrospectives (reflecting on what worked and what to change).

---

## Question 2
What is the "sync-then-parallel" pattern?

- A) Running all agents sequentially, then in parallel
- B) Having a lead agent make decisions first, then fanning out implementation to specialists
- C) Syncing git branches before parallel development
- D) A debugging technique for async issues

**Answer:** B) Having a lead agent make decisions first, then fanning out implementation to specialists
**Explanation:** In this pattern, a design/architecture step runs first (sync) to establish decisions, then multiple agents implement their parts in parallel based on those decisions.

---

## Question 3
What is the "drop-box pattern"?

- A) A technique for deleting old agent files
- B) A shared directory where agents can produce and consume files for inter-agent communication
- C) A way to archive completed tasks
- D) An integration with Dropbox cloud storage

**Answer:** B) A shared directory where agents can produce and consume files for inter-agent communication
**Explanation:** Since agents run in separate contexts and can't communicate directly, the drop-box pattern uses a shared directory (e.g., `.squad/dropbox/`) where one agent writes files and another reads them.

---

## Question 4
What is the recommended maximum number of parallel agents for optimal performance?

- A) 2
- B) 3-4
- C) 10
- D) Unlimited

**Answer:** B) 3-4
**Explanation:** While Squad can run more agents in parallel, there are diminishing returns above 5. Starting with 3-4 parallel agents gives you the best balance of throughput and quality.

---

## Question 5
How do git worktrees benefit Squad workflows?

- A) They make Squad run faster
- B) They allow multiple agents to work on different branches simultaneously without switching
- C) They enable cloud deployment
- D) They reduce git repository size

**Answer:** B) They allow multiple agents to work on different branches simultaneously without switching
**Explanation:** Worktrees let you check out multiple branches in different directories. Different agents can work on different features in separate worktrees, all sharing the same `.squad/` configuration and decisions.

---

## Question 6
In a design review ceremony, what is the expected output?

- A) A completed implementation of the feature
- B) Decision entries in decisions.md and an implementation plan
- C) A pull request ready for merge
- D) Updated agent charter files

**Answer:** B) Decision entries in decisions.md and an implementation plan
**Explanation:** A design review produces decisions (recorded in `decisions.md`) and an implementation plan. The actual coding happens after the review, informed by these decisions.

---

## Question 7
When should you use the drop-box pattern instead of decisions.md?

- A) Always — the drop-box is better in every case
- B) When sharing structured data like specs, schemas, or test fixtures between agents
- C) When recording simple yes/no decisions
- D) When agents need to communicate in real-time

**Answer:** B) When sharing structured data like specs, schemas, or test fixtures between agents
**Explanation:** The drop-box is for structured documents — API specs, test plans, data fixtures. For simple decisions and choices, `decisions.md` is more appropriate. The drop-box shines when agents need to share larger, more detailed artifacts.

---

## Question 8
In the "Competitive Fan-Out" pattern, what is the goal?

- A) To have agents compete for the fastest implementation
- B) To generate multiple proposals for the same problem, allowing selection of the best approach
- C) To benchmark different agent performances
- D) To create redundant implementations for reliability

**Answer:** B) To generate multiple proposals for the same problem, allowing selection of the best approach
**Explanation:** Competitive fan-out has multiple agents propose different solutions. You (or the lead agent) then choose the best approach, getting the benefit of multiple perspectives before committing to a direction.

---

## Question 9
Why should parallel tasks avoid writing to the same files?

- A) It causes performance issues in the AI model
- B) It can cause merge conflicts and data loss when results are collected
- C) Squad doesn't support parallel file writes
- D) It violates the agent charter rules

**Answer:** B) It can cause merge conflicts and data loss when results are collected
**Explanation:** When multiple agents write to the same file simultaneously, their changes can conflict. Give each parallel agent clear, non-overlapping file responsibilities to avoid this.

---

## Question 10
What is a retro's most valuable output in Squad?

- A) Performance metrics for each agent
- B) Updated skills, conventions, and routing refinements that improve future sessions
- C) A report card for each agent
- D) A list of bugs found

**Answer:** B) Updated skills, conventions, and routing refinements that improve future sessions
**Explanation:** Retrospectives generate actionable improvements: new skills in `.squad/skills/`, updated conventions in agent histories, and refined routing rules — all of which make the team more effective in future sessions.
