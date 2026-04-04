# 🧠 Prompt Engineering Cheat Sheet for Developers
## By TDSquad DevTools

> Master the art of talking to AI — get better code, faster reviews, and smarter agents.

---

## The CIDER Framework

Every great developer prompt follows five elements:

| Element | What It Means | Example |
|---------|--------------|---------|
| **C** — Context | Background info the AI needs | "I'm working on a Node.js REST API with Express and PostgreSQL" |
| **I** — Intent | What you want to achieve | "I need to add rate limiting to prevent abuse" |
| **D** — Details | Specifics, constraints, edge cases | "Use a sliding window algorithm, 100 req/min per IP, return 429 status" |
| **E** — Examples | Show the format you expect | "Return JSON like `{ error: 'Rate limited', retryAfter: 45 }`" |
| **R** — Review | Ask AI to verify its own work | "Check for race conditions and test with concurrent requests" |

### Quick Template
```
Context: [tech stack, project type, current state]
Intent: [what you're building/fixing]
Details: [constraints, performance needs, edge cases]
Examples: [expected input/output format]
Review: [what to double-check]
```

---

## 🔧 Code Generation Prompts

### New Feature
```
Build a [feature] for [tech stack].
Requirements:
- [requirement 1]
- [requirement 2]
Constraints: [performance, security, compatibility]
Return: [complete file / function / class]
Include: [error handling, types, tests]
```

### Refactoring
```
Refactor this [function/class] to:
- [improvement 1: e.g., reduce complexity]
- [improvement 2: e.g., improve testability]
Keep: [existing behavior, API contract, test compatibility]
Don't change: [public interface, database schema]
```

### Bug Fix
```
This code has a bug: [describe symptom]
Expected: [what should happen]
Actual: [what happens instead]
Reproduce: [steps or input that triggers it]
Fix the bug and explain what caused it.
```

---

## 🔍 Code Review Prompts

### Security Review
```
Review this code for security vulnerabilities:
- SQL injection
- XSS
- Path traversal
- Hardcoded secrets
- Insecure deserialization
Rate each finding: Critical / High / Medium / Low
```

### Performance Review
```
Analyze this code for performance issues:
- N+1 queries
- Missing indexes implied by query patterns
- Unnecessary allocations in hot paths
- Blocking I/O in async contexts
Suggest fixes with estimated impact.
```

### Architecture Review
```
Review this [module/service] for:
- Single Responsibility violations
- Tight coupling between layers
- Missing abstractions
- Error handling gaps
Suggest a refactored structure.
```

---

## 🤖 AI Agent Prompts

### Task Decomposition
```
Break this task into subtasks that can be executed independently:
Task: [description]
Constraints:
- Each subtask must be completable in one step
- Identify dependencies between subtasks
- Mark which can run in parallel
Output as a DAG (directed acyclic graph).
```

### Agent Instruction
```
You are [role]. Your job is to [objective].

Rules:
- [constraint 1]
- [constraint 2]

Tools available: [list tools]

Process:
1. [step 1]
2. [step 2]
3. [verification step]

Output format: [expected format]
```

### Multi-Agent Coordination
```
Orchestrate these agents:
- Agent A: [role and capability]
- Agent B: [role and capability]
- Agent C: [role and capability]

Task: [what needs to be accomplished]
Coordination: [sequential / parallel / fan-out-fan-in]
Handoff format: [how agents share results]
```

---

## 📝 Documentation Prompts

### API Documentation
```
Generate API documentation for this [endpoint/module]:
Include: description, parameters, return types, error codes, examples
Format: [OpenAPI / JSDoc / Markdown table]
Audience: [junior devs / external consumers / internal team]
```

### README Generator
```
Generate a README.md for this project:
Sections: Overview, Quick Start, Installation, Usage, API, Contributing, License
Tone: [professional / casual / technical]
Include badges for: [build status, coverage, npm version]
```

---

## 🧪 Testing Prompts

### Unit Test Generation
```
Generate unit tests for [function/class]:
Framework: [Jest / pytest / xUnit / NUnit]
Cover:
- Happy path with typical inputs
- Edge cases: [empty, null, boundary values]
- Error cases: [invalid input, network failure, timeout]
Use: [mocks / stubs / fakes] for [dependencies]
Aim for: [80%+ / line / branch] coverage
```

### Integration Test
```
Write an integration test for [workflow]:
Setup: [database state, API mocks, environment]
Steps: [sequence of operations]
Assertions: [expected state after each step]
Cleanup: [teardown procedure]
```

---

## ⚡ Power Patterns

### Chain of Thought
Force the AI to reason step by step:
```
Think through this step by step:
1. First, analyze [input]
2. Then, identify [pattern/issue]
3. Finally, propose [solution]
Show your reasoning at each step.
```

### Few-Shot Learning
Teach by example:
```
Convert these SQL queries to TypeORM:

Example 1:
SQL: SELECT * FROM users WHERE age > 18
TypeORM: userRepo.find({ where: { age: MoreThan(18) } })

Example 2:
SQL: SELECT u.*, p.* FROM users u JOIN posts p ON u.id = p.userId
TypeORM: userRepo.find({ relations: ['posts'] })

Now convert:
SQL: [your query]
```

### Constraint Injection
Prevent common AI mistakes:
```
[Your prompt here]

Important constraints:
- Do NOT use deprecated APIs
- Do NOT include placeholder comments like "// TODO" or "// add logic here"
- Do NOT import packages that aren't in package.json
- Every function must have error handling
- Use TypeScript strict mode
```

### Iterative Refinement
```
Here's your previous output: [paste output]

Issues:
1. [problem 1]
2. [problem 2]

Keep: [what worked well]
Fix: [specific changes needed]
Add: [missing elements]
```

---

## 🎯 Quick Reference — Prompt Modifiers

| Modifier | Effect | Example |
|----------|--------|---------|
| "Be concise" | Shorter output | "Explain in 3 sentences" |
| "Be thorough" | Detailed output | "Include edge cases and error handling" |
| "As a senior engineer" | Higher quality patterns | "Review as a principal engineer would" |
| "For production" | Production-ready code | "Include logging, monitoring, error recovery" |
| "Step by step" | Chain-of-thought reasoning | "Walk through the logic step by step" |
| "Compare approaches" | Multiple solutions | "Show 3 approaches with tradeoffs" |
| "Teach me" | Educational explanations | "Explain why this pattern is preferred" |

---

## 🚫 Anti-Patterns to Avoid

| ❌ Don't | ✅ Do Instead |
|----------|--------------|
| "Write some code" | "Write a rate limiter middleware for Express using sliding window" |
| "Fix the bug" | "The login endpoint returns 500 when email contains '+'. Fix the email parsing" |
| "Make it better" | "Reduce time complexity from O(n²) to O(n log n) for the sort function" |
| "Add tests" | "Add unit tests for the UserService.create() method covering: valid input, duplicate email, missing required fields" |
| Dump entire codebase | Provide relevant files + context only |
| Accept first output | Iterate: review, critique, refine |

---

## 📊 Prompt Quality Scoring

Rate your prompts before sending:

| Criteria | Score |
|----------|-------|
| Has clear context? | ☐ +1 |
| States specific intent? | ☐ +1 |
| Includes constraints/details? | ☐ +1 |
| Provides examples? | ☐ +1 |
| Asks for self-review? | ☐ +1 |
| **Total** | **/5** |

**Score 4-5:** Send it — you'll get great results.
**Score 2-3:** Add more context or examples.
**Score 0-1:** Rewrite — you're gambling on AI reading your mind.

---

*Built by TDSquad DevTools — developer tools for the AI era.*
*Get more at [squadai.gumroad.com](https://squadai.gumroad.com)*
