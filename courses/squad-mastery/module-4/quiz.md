# Module 4: Quiz — Ralph & Autonomous Work

## Question 1
What is Ralph in the Squad framework?

- A) A code linting tool
- B) A persistent work monitor that scans for tasks and dispatches agents
- C) A version control plugin
- D) A CI/CD pipeline runner

**Answer:** B) A persistent work monitor that scans for tasks and dispatches agents
**Explanation:** Ralph is a persistent agent session that continuously monitors for work (GitHub issues, PRDs), triages it, spawns the right agents, and collects results — creating a fully autonomous work pipeline.

---

## Question 2
What command starts Ralph's triage loop?

- A) `squad start ralph`
- B) `squad monitor`
- C) `squad triage`
- D) `squad agent ralph`

**Answer:** C) `squad triage`
**Explanation:** `squad triage` starts Ralph's monitoring loop. It can also be invoked with aliases: `squad watch` or `squad loop`. The `--interval` flag controls polling frequency.

---

## Question 3
What is the default polling interval for Ralph?

- A) 1 minute
- B) 5 minutes
- C) 10 minutes
- D) 30 minutes

**Answer:** C) 10 minutes
**Explanation:** By default, Ralph polls every 10 minutes. You can customize this with `squad triage --interval N` where N is the number of minutes between scans.

---

## Question 4
How does Ralph handle crashes?

- A) All progress is lost and must be restarted from scratch
- B) It reads its persisted state file and resumes from where it left off
- C) It sends an email notification and waits for manual restart
- D) It automatically recovers in the same process

**Answer:** B) It reads its persisted state file and resumes from where it left off
**Explanation:** Ralph persists its state to `.squad/ralph-state.json`, tracking processed issues, active work, and pending reviews. On restart, it reads this file and continues without duplicating completed work.

---

## Question 5
In the Issue-to-PR lifecycle, what happens AFTER an agent finishes implementing code?

- A) The code is automatically deployed to production
- B) A pull request is created with the changes, linked to the original issue
- C) The issue is closed immediately
- D) Ralph emails the team lead for approval

**Answer:** B) A pull request is created with the changes, linked to the original issue
**Explanation:** After agents finish their work (implementation + testing), Ralph creates a branch, commits the changes, and opens a pull request that links back to the original issue. The PR then awaits human review.

---

## Question 6
What is PRD Mode?

- A) A debugging mode for Ralph
- B) A mode where Ralph processes a Product Requirements Document to deliver a full feature
- C) A performance monitoring mode
- D) A read-only mode for viewing project status

**Answer:** B) A mode where Ralph processes a Product Requirements Document to deliver a full feature
**Explanation:** PRD Mode lets you give Ralph a full specification document. Ralph orchestrates the entire team — design review, parallel implementation, testing, documentation — to deliver the feature described in the PRD.

---

## Question 7
What information does Ralph's state file track?

- A) Only the last scan timestamp
- B) Processed issues, active work, pending reviews, and statistics
- C) Agent charter files
- D) Git commit hashes

**Answer:** B) Processed issues, active work, pending reviews, and statistics
**Explanation:** The state file (`ralph-state.json`) tracks: which issues have been processed, which agents are currently working on what, PRs awaiting review, and overall statistics like total issues processed and work time.

---

## Question 8
What is "idle-watch polling"?

- A) A mode where Ralph does nothing
- B) A smart polling strategy that increases intervals during quiet periods and returns to active polling when work is detected
- C) A way to monitor if agents are idle
- D) A power-saving mode for laptops

**Answer:** B) A smart polling strategy that increases intervals during quiet periods and returns to active polling when work is detected
**Explanation:** Idle-watch polling prevents Ralph from burning API rate limits when there's no work. During quiet periods, the polling interval gradually increases. When new work is detected, it immediately returns to the configured active interval.

---

## Question 9
Which GitHub CLI tool must be installed and authenticated for Ralph to work?

- A) `hub`
- B) `git`
- C) `gh`
- D) `github-cli`

**Answer:** C) `gh`
**Explanation:** Ralph uses the GitHub CLI (`gh`) to interact with GitHub issues, branches, and pull requests. You must authenticate with `gh auth login` before starting Ralph.

---

## Question 10
How does Ralph decide which agent should handle a specific GitHub issue?

- A) It randomly assigns issues to agents
- B) It reads the team's routing.md rules and matches issue content to agent specializations
- C) It always assigns everything to the lead agent
- D) Users must manually assign issues to agents

**Answer:** B) It reads the team's routing.md rules and matches issue content to agent specializations
**Explanation:** Ralph uses the team's routing rules from `routing.md` to determine which agent handles what. It analyzes the issue content (title, body, labels) and matches it to the appropriate specialist — frontend tasks to McManus, backend to Verbal, etc.
