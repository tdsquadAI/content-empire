# 📋 Publishing Checklist — Content Empire Articles

## Medium Publishing (5 articles)

### Setup (One-Time)
- [ ] Create Medium account at https://medium.com (or log in)
- [ ] Set up profile: Add bio, photo, links to your sites
- [ ] Connect a custom domain (optional but recommended)
- [ ] Join relevant Medium publications to submit articles to:
  - **Better Programming** — largest programming pub
  - **Towards Data Science** — for AI/ML articles
  - **The Startup** — for business/solopreneur content
  - **JavaScript in Plain English** — for JS/TS articles
  - **Level Up Coding** — general programming

### For Each Article

#### Article 1: Building AI Agent Teams That Ship Code
- [ ] Open `medium-ready/01-building-ai-agent-teams.md`
- [ ] Go to Medium → New Story
- [ ] Paste the markdown content
- [ ] Review formatting (code blocks, tables, images)
- [ ] Add cover image (suggestion: robot team / AI collaboration visual)
- [ ] Set canonical URL to: `https://content-empire-pub.github.io/content-empire/posts/building-ai-agent-teams/`
- [ ] Add tags: `AI`, `Agents`, `Software Development`, `Automation`, `Programming`
- [ ] Submit to **Better Programming** or **Towards Data Science** publication
- [ ] Publish or schedule

#### Article 2: MCP Servers — The Plugin System AI Agents Were Missing
- [ ] Open `medium-ready/02-mcp-servers-plugin-system.md`
- [ ] Same process as above
- [ ] Canonical URL: `https://content-empire-pub.github.io/content-empire/posts/mcp-servers-plugin-system/`
- [ ] Tags: `AI`, `MCP`, `Architecture`, `Tools`, `Programming`
- [ ] Submit to **Better Programming**

#### Article 3: Browser Automation with Playwright — Beyond Testing
- [ ] Open `medium-ready/03-playwright-beyond-testing.md`
- [ ] Canonical URL: `https://content-empire-pub.github.io/content-empire/posts/playwright-beyond-testing/`
- [ ] Tags: `Playwright`, `Automation`, `JavaScript`, `Web Scraping`, `Productivity`
- [ ] Submit to **JavaScript in Plain English** or **Better Programming**

#### Article 4: Building a Content Empire with Zero Employees
- [ ] Open `medium-ready/04-content-empire-zero-employees.md`
- [ ] Canonical URL: `https://content-empire-pub.github.io/content-empire/posts/content-empire-zero-employees/`
- [ ] Tags: `AI`, `Content Creation`, `Solopreneur`, `Business`, `Automation`
- [ ] Submit to **The Startup**

#### Article 5: The Hidden Cost of Not Automating
- [ ] Open `medium-ready/05-hidden-cost-of-not-automating.md`
- [ ] Canonical URL: `https://content-empire-pub.github.io/content-empire/posts/hidden-cost-of-not-automating/`
- [ ] Tags: `DevOps`, `Automation`, `Productivity`, `CI/CD`, `Programming`
- [ ] Submit to **Better Programming** or **Level Up Coding**

### Publishing Schedule (Recommended)
- **Day 1 (Monday):** Article 1 — AI Agent Teams (highest engagement topic)
- **Day 3 (Wednesday):** Article 2 — MCP Servers
- **Day 5 (Friday):** Article 5 — Hidden Cost of Not Automating
- **Day 8 (Monday):** Article 3 — Playwright Beyond Testing
- **Day 10 (Wednesday):** Article 4 — Content Empire Zero Employees

### Medium Tips
- ⚡ Always set canonical URL to preserve SEO on your own site
- 📊 Publish between 7-9 AM EST for maximum engagement
- 🏷️ Use exactly 5 tags (Medium's limit)
- 📝 Submitting to publications dramatically increases reach
- 🔄 Respond to comments within 24 hours for algorithm boost
- 💡 Add a "Follow me" CTA in your bio, not just at article end

---

## Dev.to Publishing (3 articles)

### Setup (One-Time)
- [ ] Create Dev.to account at https://dev.to (or log in with GitHub)
- [ ] Set up profile with links and bio
- [ ] Get API key: Settings → Extensions → Generate API Key
- [ ] Save API key securely

### Manual Publishing
For each article in `devto-ready/`:
- [ ] Go to https://dev.to/new
- [ ] Paste markdown content
- [ ] Add front matter (title, tags) — Dev.to auto-detects tags in `{% tag %}` format
- [ ] Set canonical URL to your site
- [ ] Add cover image
- [ ] Preview and publish

### API Publishing (Automated)
```bash
# Publish via API
curl -X POST https://dev.to/api/articles \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_DEV_TO_API_KEY" \
  -d '{
    "article": {
      "title": "Building AI Agent Teams That Actually Ship Code",
      "body_markdown": "PASTE_MARKDOWN_HERE",
      "published": true,
      "tags": ["ai", "agents", "programming", "automation"],
      "canonical_url": "https://content-empire-pub.github.io/content-empire/posts/building-ai-agent-teams/"
    }
  }'
```

### Dev.to Articles
1. `devto-ready/01-ai-agent-teams.md` — AI Agent Teams
2. `devto-ready/02-mcp-servers.md` — MCP Servers
3. `devto-ready/03-hidden-cost-not-automating.md` — Hidden Cost of Not Automating

### Dev.to Publishing Schedule
- **Day 2 (Tuesday):** Article 1 — AI Agent Teams
- **Day 4 (Thursday):** Article 2 — MCP Servers
- **Day 9 (Tuesday):** Article 3 — Hidden Cost

This staggers with Medium so you're not posting the same content on the same day.

---

## Gumroad Product Setup

- [ ] Open `monetization/gumroad-product-listing.md`
- [ ] Follow the step-by-step instructions to create the product
- [ ] Set price to $19.99 with EARLYBIRD code for $9.99
- [ ] After product URL is live, update CTAs in articles if the slug differs

---

## Post-Publishing Tasks
- [ ] Share each article on Twitter/X with a thread summarizing key points
- [ ] Share on LinkedIn with a professional intro
- [ ] Cross-link articles to each other in comments/edits
- [ ] Monitor analytics after 48 hours and double down on what performs
- [ ] Reply to all comments within 24 hours
