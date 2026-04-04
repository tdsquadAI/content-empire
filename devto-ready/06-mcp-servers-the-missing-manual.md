---
title: "MCP Servers: The Missing Manual for Developers"
published: false
description: "A practical guide to building your first Model Context Protocol server and why it matters for AI integrations"
tags: ai, mcp, typescript, tutorial
cover_image: https://placeholder-for-cover-image.jpg
---

The Model Context Protocol (MCP) is one of those specs that sounds boring in theory but is ridiculously useful in practice.

If you've ever built an AI chatbot or agent and thought "I wish this thing could just access my database" or "Why can't this read my internal docs?"—MCP is the answer.

But here's the problem: The official docs assume you already know what you're building. They skip the "why" and jump straight to the "how."

This is the tutorial I wish existed when I built my first MCP server last month.

## What is MCP? (And Why Should You Care?)

**TL;DR:** MCP is a standardized protocol for connecting AI models to your tools, data sources, and services.

Think of it like this:

- **Without MCP:** Your AI assistant is a brain in a jar—it can think, but it can't interact with the world.
- **With MCP:** Your AI assistant becomes a developer with access to your APIs, databases, file systems, and internal tools.

**The architecture:**

```
┌─────────────────┐         ┌──────────────────┐         ┌─────────────────┐
│                 │         │                  │         │                 │
│   AI Client     │ ◄─MCP──► │   MCP Server    │ ◄─────► │  Your Tools     │
│  (Claude, etc)  │         │  (Your Code)     │         │  (DB, APIs)     │
│                 │         │                  │         │                 │
└─────────────────┘         └──────────────────┘         └─────────────────┘
```

**The protocol defines three primitives:**

1. **Resources** — Things the AI can read (files, database records, API responses)
2. **Tools** — Actions the AI can take (run queries, call APIs, create files)
3. **Prompts** — Reusable templates the AI can invoke

The beauty? Once you build an MCP server, it works with *any* MCP-compatible AI client—Claude Desktop, VS Code with GitHub Copilot, custom chatbots, etc.

## Why MCP Matters (Real Use Cases)

Here are five things I've built with MCP servers in the last month:

1. **Internal docs search** — Claude can now search our entire Notion workspace
2. **Database query assistant** — Ask "How many users signed up last week?" in plain English
3. **Deployment dashboard** — Check service health, view logs, rollback deployments via chat
4. **Code review bot** — Reads GitHub PRs, runs linters, posts review comments
5. **Customer support agent** — Looks up user accounts, checks order status, creates tickets

Each of these took ~2 hours to build. Without MCP? Probably 2 days of glue code.

## Your First MCP Server: GitHub Issue Tracker

Let's build something practical: an MCP server that lets an AI assistant interact with GitHub issues.

**What it'll do:**
- List issues in a repo
- Read issue details
- Create new issues
- Add comments to issues

### Step 1: Project Setup

```bash
mkdir mcp-github-server
cd mcp-github-server
npm init -y
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

**Why these deps?**
- `@modelcontextprotocol/sdk` — Official MCP SDK
- `zod` — Runtime type validation (MCP tool inputs must be validated)
- TypeScript — Type safety (trust me, you want this)

**tsconfig.json:**
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "Node16",
    "moduleResolution": "Node16",
    "outDir": "./build",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true
  }
}
```

### Step 2: Core Server Structure

**src/index.ts:**

```typescript
#!/usr/bin/env node
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  ListToolsRequestSchema,
  CallToolRequestSchema,
  Tool,
} from '@modelcontextprotocol/sdk/types.js';
import { z } from 'zod';

// GitHub API client (simplified - use Octokit in production)
const GITHUB_TOKEN = process.env.GITHUB_TOKEN;
const GITHUB_API = 'https://api.github.com';

async function fetchGitHub(path: string, options: RequestInit = {}) {
  const response = await fetch(`${GITHUB_API}${path}`, {
    ...options,
    headers: {
      'Authorization': `Bearer ${GITHUB_TOKEN}`,
      'Accept': 'application/vnd.github.v3+json',
      ...options.headers,
    },
  });

  if (!response.ok) {
    throw new Error(`GitHub API error: ${response.statusText}`);
  }

  return response.json();
}

// Define tool schemas
const ListIssuesSchema = z.object({
  owner: z.string().describe('Repository owner'),
  repo: z.string().describe('Repository name'),
  state: z.enum(['open', 'closed', 'all']).default('open'),
});

const CreateIssueSchema = z.object({
  owner: z.string().describe('Repository owner'),
  repo: z.string().describe('Repository name'),
  title: z.string().describe('Issue title'),
  body: z.string().optional().describe('Issue description'),
  labels: z.array(z.string()).optional(),
});

const AddCommentSchema = z.object({
  owner: z.string(),
  repo: z.string(),
  issue_number: z.number(),
  body: z.string().describe('Comment text'),
});

// Tool definitions
const tools: Tool[] = [
  {
    name: 'list_issues',
    description: 'List issues in a GitHub repository',
    inputSchema: {
      type: 'object',
      properties: {
        owner: { type: 'string', description: 'Repository owner' },
        repo: { type: 'string', description: 'Repository name' },
        state: { 
          type: 'string', 
          enum: ['open', 'closed', 'all'],
          description: 'Filter by issue state',
        },
      },
      required: ['owner', 'repo'],
    },
  },
  {
    name: 'create_issue',
    description: 'Create a new issue in a GitHub repository',
    inputSchema: {
      type: 'object',
      properties: {
        owner: { type: 'string' },
        repo: { type: 'string' },
        title: { type: 'string', description: 'Issue title' },
        body: { type: 'string', description: 'Issue description' },
        labels: { 
          type: 'array',
          items: { type: 'string' },
          description: 'Labels to apply',
        },
      },
      required: ['owner', 'repo', 'title'],
    },
  },
  {
    name: 'add_comment',
    description: 'Add a comment to an existing issue',
    inputSchema: {
      type: 'object',
      properties: {
        owner: { type: 'string' },
        repo: { type: 'string' },
        issue_number: { type: 'number' },
        body: { type: 'string', description: 'Comment text' },
      },
      required: ['owner', 'repo', 'issue_number', 'body'],
    },
  },
];

// Tool implementations
async function listIssues(args: z.infer<typeof ListIssuesSchema>) {
  const { owner, repo, state } = args;
  const issues = await fetchGitHub(
    `/repos/${owner}/${repo}/issues?state=${state}`
  );

  return {
    content: [
      {
        type: 'text',
        text: JSON.stringify(
          issues.map((issue: any) => ({
            number: issue.number,
            title: issue.title,
            state: issue.state,
            url: issue.html_url,
            created_at: issue.created_at,
          })),
          null,
          2
        ),
      },
    ],
  };
}

async function createIssue(args: z.infer<typeof CreateIssueSchema>) {
  const { owner, repo, title, body, labels } = args;
  
  const issue = await fetchGitHub(`/repos/${owner}/${repo}/issues`, {
    method: 'POST',
    body: JSON.stringify({ title, body, labels }),
    headers: { 'Content-Type': 'application/json' },
  });

  return {
    content: [
      {
        type: 'text',
        text: `Created issue #${issue.number}: ${issue.html_url}`,
      },
    ],
  };
}

async function addComment(args: z.infer<typeof AddCommentSchema>) {
  const { owner, repo, issue_number, body } = args;

  await fetchGitHub(
    `/repos/${owner}/${repo}/issues/${issue_number}/comments`,
    {
      method: 'POST',
      body: JSON.stringify({ body }),
      headers: { 'Content-Type': 'application/json' },
    }
  );

  return {
    content: [
      {
        type: 'text',
        text: `Added comment to issue #${issue_number}`,
      },
    ],
  };
}

// Create and configure server
const server = new Server(
  {
    name: 'github-issues-mcp',
    version: '1.0.0',
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Handle tool listing
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return { tools };
});

// Handle tool execution
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  try {
    switch (name) {
      case 'list_issues': {
        const validated = ListIssuesSchema.parse(args);
        return await listIssues(validated);
      }
      case 'create_issue': {
        const validated = CreateIssueSchema.parse(args);
        return await createIssue(validated);
      }
      case 'add_comment': {
        const validated = AddCommentSchema.parse(args);
        return await addComment(validated);
      }
      default:
        throw new Error(`Unknown tool: ${name}`);
    }
  } catch (error) {
    return {
      content: [
        {
          type: 'text',
          text: `Error: ${error instanceof Error ? error.message : String(error)}`,
        },
      ],
      isError: true,
    };
  }
});

// Start the server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error('GitHub Issues MCP server running on stdio');
}

main().catch((error) => {
  console.error('Fatal error:', error);
  process.exit(1);
});
```

### Step 3: Build and Configure

**package.json:**
```json
{
  "name": "mcp-github-server",
  "version": "1.0.0",
  "type": "module",
  "bin": {
    "mcp-github-server": "./build/index.js"
  },
  "scripts": {
    "build": "tsc",
    "dev": "tsc --watch"
  }
}
```

**Build it:**
```bash
npm run build
```

**Configure MCP client (e.g., Claude Desktop):**

Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "github-issues": {
      "command": "node",
      "args": ["/path/to/mcp-github-server/build/index.js"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

Restart Claude Desktop.

### Step 4: Test It

Open Claude and try:

> "List open issues in my-org/my-repo"

Claude will:
1. Detect you want to use the GitHub MCP server
2. Call the `list_issues` tool with appropriate args
3. Display the results

You can now:
- Create issues via chat
- Add comments without leaving the conversation
- Search and triage issues in natural language

## Key MCP Patterns to Know

### 1. Error Handling

Always wrap tool execution in try/catch and return structured errors:

```typescript
try {
  return await myTool(args);
} catch (error) {
  return {
    content: [{ type: 'text', text: `Error: ${error.message}` }],
    isError: true,
  };
}
```

### 2. Input Validation

Use Zod to validate all inputs—the AI will sometimes send garbage:

```typescript
const MyToolSchema = z.object({
  id: z.number().positive(), // Enforce positive numbers
  email: z.string().email(), // Validate email format
  status: z.enum(['active', 'inactive']), // Only allow specific values
});
```

### 3. Pagination

For large result sets, return paginated data:

```typescript
{
  content: [{
    type: 'text',
    text: JSON.stringify({
      items: results.slice(0, 10),
      total: results.length,
      hasMore: results.length > 10,
    }),
  }],
}
```

### 4. Rich Responses

MCP supports multiple content types:

```typescript
{
  content: [
    { type: 'text', text: 'Found 3 issues:' },
    { type: 'text', text: JSON.stringify(issues) },
    { 
      type: 'resource',
      resource: { uri: 'github://my-org/my-repo/issues/42' }
    },
  ],
}
```

## Production Considerations

### Security

- **Never hardcode tokens** — Use environment variables
- **Validate all inputs** — AI models can be tricked into sending malicious payloads
- **Rate limiting** — Wrap expensive operations with rate limits
- **Audit logs** — Log all tool calls for debugging and security

### Performance

- **Cache aggressively** — MCP servers are called frequently
- **Lazy load** — Don't fetch data until the tool is actually invoked
- **Streaming** — For long-running operations, consider streaming responses

### Observability

```typescript
import { trace } from '@opentelemetry/api';

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const span = trace.getTracer('mcp-server').startSpan('tool_call');
  span.setAttribute('tool.name', request.params.name);
  
  try {
    return await executeTool(request);
  } finally {
    span.end();
  }
});
```

## Beyond GitHub: More MCP Server Ideas

Once you understand the pattern, you can build MCP servers for:

- **Databases** — Natural language SQL queries
- **Internal APIs** — Expose company tools to AI assistants
- **File systems** — Let AI read/write project files
- **Analytics** — Query dashboards and metrics
- **Customer data** — Lookup accounts, orders, tickets
- **Deployment pipelines** — Trigger builds, check status

The limiting factor isn't the protocol—it's your imagination.

## Going Deeper with AI-Powered Development

This tutorial scratches the surface of what's possible when you give AI assistants access to real tools and data.

We've written an in-depth guide on building production AI integrations that covers MCP servers, agent orchestration, tool design patterns, and security best practices.

**[AI-Powered Development Guide →](https://squadai.gumroad.com/l/ai-powered-dev)** ($9.99)

It includes:
- 10+ production-ready MCP server templates
- Authentication and authorization patterns
- Testing strategies for AI integrations
- Debugging tools and observability setup
- Real-world case studies from teams in production

Perfect for developers building AI features into existing products.

## The Big Picture

MCP is still early (the spec is <1 year old), but it's already becoming the standard for AI-tool integration.

**Why it matters:**
- Anthropic (Claude) built it and uses it in production
- GitHub is integrating it into Copilot
- Microsoft is exploring it for Azure AI

If you're building AI features, learning MCP now gives you a 12-month head start.

**Start with one tool:**
- Pick a frequently-used internal API
- Build a simple MCP server with 2-3 tools
- Wire it up to Claude Desktop or your AI assistant
- Measure how often you use it

You'll know within a week if it's valuable.

And if it is? Scale it. Build more servers. Connect more tools. Watch your AI assistant go from "helpful chatbot" to "indispensable teammate."

---

*Published by the TechAI Explained team. Find us on [Gumroad](https://squadai.gumroad.com) | [GitHub](https://github.com/tdsquadAI)*
