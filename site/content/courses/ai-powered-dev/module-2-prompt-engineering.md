---
title: "Module 2: Prompt Engineering for Developers"
date: 2025-07-23
weight: 2
author: "The Content Empire Team"
tags: ["AI", "course", "prompting", "development"]
description: "Master the art of communicating with AI tools to get better code, faster — using the CIDER framework designed specifically for developers."
---

# Module 2: Prompt Engineering for Developers

## Learning Objectives

By the end of this module, you will:
- Understand why developer prompting differs from general-purpose prompting
- Master the CIDER framework for writing effective development prompts
- Have a reusable prompt library for common development tasks
- Be able to transform vague requests into precise, effective prompts

## 2.1 Why Developer Prompting Is Different

General prompt engineering advice ("be specific", "provide examples") is necessary but not sufficient for development work. Developer prompting has unique challenges:

1. **Code has strict correctness requirements** — Natural language can be vague, but code must compile and produce exact results
2. **Context is massive** — Your codebase has thousands of files with interconnected dependencies
3. **Style matters** — Generated code must match your project's patterns, not just be "correct"
4. **Iteration is expected** — Unlike writing a marketing email, code generation is almost always iterative

## 2.2 The CIDER Framework

We've developed a framework specifically for developer prompting. Each letter represents a component of an effective prompt:

### **C** — Context

Tell the AI about your project, tech stack, and the specific file or module you're working in.

❌ Bad:
```
Write a function to validate email addresses
```

✅ Good:
```
I'm working in a TypeScript Express API project using Zod for validation.
The project uses a functional style with arrow functions and 
Result<T, Error> types instead of throwing exceptions.

Write a function to validate email addresses.
```

### **I** — Intent

State clearly what you want to accomplish AND why. The "why" helps the AI make better design decisions.

❌ Bad:
```
Add caching to the getUser function
```

✅ Good:
```
Add Redis caching to the getUser function to reduce database load.
We're seeing 500+ calls/second to this endpoint, and the user data
changes infrequently (maybe once per day). Cache should invalidate
when user data is updated.
```

### **D** — Details

Specify constraints, edge cases, and requirements that the AI might not assume.

```
Details:
- Cache TTL: 1 hour
- Cache key format: `user:{userId}`
- Handle cache misses gracefully (fall back to DB)
- Handle Redis connection failures (don't crash, just skip cache)
- Log cache hits/misses for monitoring
- Use the existing RedisClient from src/lib/redis.ts
```

### **E** — Examples

Provide examples of existing code patterns in your project. This is the single most powerful technique for getting consistent output.

```
Here's how we handle caching in the getProduct function (follow this pattern):

```typescript
export const getProduct = async (id: string): Promise<Result<Product>> => {
    const cached = await cache.get<Product>(`product:${id}`);
    if (cached.ok) {
        logger.debug({ id, source: 'cache' }, 'Product cache hit');
        return Result.ok(cached.value);
    }
    
    const product = await productRepo.findById(id);
    if (!product.ok) return product;
    
    await cache.set(`product:${id}`, product.value, { ttl: 3600 });
    return product;
};
```

Now write getUser following the same pattern.
```

### **R** — Review Criteria

Tell the AI how you'll evaluate its output. This acts as a quality checklist.

```
Review criteria:
- Must pass TypeScript strict mode
- Must handle all error cases without throwing
- Must include JSDoc with @param and @returns
- Must be under 30 lines (excluding comments)
- Must have no external dependencies beyond what's already in package.json
```

## 2.3 Prompt Templates for Common Tasks

### Template: Bug Fix

```markdown
## Bug Fix Request

**Context:**
[Describe the project, relevant files, tech stack]

**Bug Description:**
[What's happening vs. what should happen]

**Reproduction Steps:**
1. [Step 1]
2. [Step 2]

**Error Output:**
```
[Paste actual error messages, stack traces]
```

**Relevant Code:**
```[language]
[Paste the suspicious code section]
```

**Constraints:**
- Don't change the public API
- Maintain backward compatibility
- Fix must include a regression test
```

### Template: Code Review

```markdown
## Code Review Request

**Context:**
This is a [type of change] in our [project description].

**What changed:**
[Brief description of the changes]

**Code to review:**
```[language]
[Paste the code]
```

**Review focus:**
- Correctness: Does this handle all edge cases?
- Performance: Any O(n²) or worse operations?
- Security: Any injection, auth, or data exposure risks?
- Maintainability: Will this be clear in 6 months?
- Testing: What test cases are missing?

**Don't comment on:**
- Code style (handled by our linter)
- Naming conventions (unless genuinely confusing)
```

### Template: Architecture Decision

```markdown
## Architecture Decision Request

**Context:**
[Describe the system, current architecture, scale]

**Problem:**
[What problem needs solving]

**Options I'm considering:**
1. [Option A] — [brief description]
2. [Option B] — [brief description]
3. [Option C] — [brief description]

**Constraints:**
- Must work with [existing tech]
- Must handle [scale requirement]
- Team has experience with [technologies]
- Budget: [hosting/infra budget]

**What I need:**
- Pros/cons analysis of each option
- Recommendation with rationale
- Migration path from current state
- Risk assessment
```

### Template: Refactoring

```markdown
## Refactoring Request

**Context:**
[Project, tech stack, the module being refactored]

**Current code:**
```[language]
[The code that needs refactoring]
```

**Problems with current code:**
- [Problem 1]
- [Problem 2]

**Desired outcome:**
- [Quality 1: e.g., "Separate business logic from HTTP handling"]
- [Quality 2: e.g., "Make the function testable without mocking HTTP"]

**Constraints:**
- All existing tests must still pass
- Public API must remain unchanged
- Follow [pattern] used elsewhere in the project
```

## 2.4 Advanced Techniques

### Chain-of-Thought for Complex Tasks

For complex tasks, ask the AI to think step by step before writing code:

```
Before writing any code, analyze this task:

1. List all the files that need to change
2. For each file, describe what changes are needed and why
3. Identify potential breaking changes
4. Propose a test strategy

Then implement the changes one file at a time.
```

### The "Critic" Pattern

After getting a response, ask the AI to critique its own work:

```
Now review the code you just wrote as if you were a senior 
developer doing a code review. Be harsh. Identify:
- Any bugs or edge cases missed
- Performance concerns
- Security issues
- Readability problems

Then provide a corrected version addressing all issues found.
```

### The "Example-Driven" Pattern

Instead of describing what you want, show the AI input/output examples:

```
I need a function that transforms data. Here are examples:

Input:  { name: "john doe", age: 30, role: "dev" }
Output: { displayName: "John Doe", metadata: { age: 30, role: "dev" } }

Input:  { name: "jane smith", age: 25, role: "pm", level: "senior" }
Output: { displayName: "Jane Smith", metadata: { age: 25, role: "pm", level: "senior" } }

Write the function. Infer the transformation rules from the examples.
```

## 2.5 Hands-On Exercise: Prompt Transformation

### Exercise: Transform These Prompts

Take each bad prompt and rewrite it using the CIDER framework:

**Prompt 1 (Bad):**
```
Write a login function
```

**Prompt 2 (Bad):**
```
Fix this code: [paste of 200 lines with no context]
```

**Prompt 3 (Bad):**
```
Make this faster
```

**Prompt 4 (Bad):**
```
Add tests
```

### Challenge

For each transformed prompt:
1. Submit both the original and improved version to your AI tool
2. Compare the outputs
3. Measure: lines of code, completeness, correctness, time to first working version

You should see dramatically better results from the CIDER-formatted prompts.

## 2.6 Building Your Prompt Library

Create a `.prompts/` directory in your project:

```
.prompts/
├── bug-fix.md
├── code-review.md
├── new-feature.md
├── refactor.md
├── test-generation.md
├── architecture-decision.md
└── README.md  (explains how to use each template)
```

Your team can share and improve these templates over time. They become institutional knowledge for how to effectively work with AI tools.

## Key Takeaways

1. Developer prompting requires more precision than general prompting because code must be correct, not just plausible
2. The CIDER framework (Context, Intent, Details, Examples, Review criteria) consistently produces better results
3. Showing examples of your project's patterns is the single most effective technique
4. Build a prompt library and share it with your team — good prompts are reusable
5. Use the "Critic" pattern to get AI to self-improve its output before you review it

## Next Module

In **Module 3: AI-Powered Code Review and Testing**, we'll build on these prompting skills to create automated code review and test generation pipelines.

---

*Continue to [Module 3: AI-Powered Code Review and Testing →](../module-3-ai-code-review/)*
