# Content Empire — Project Status
Last updated: 2026-07-28

## Brand Identity
- **Name:** Content Empire
- **NEVER mention "real owner identity"** — independent brand
- **Hugo static site** deployed to GitHub Pages (docs/ folder)
- **Base URL:** https://content-empire-pub.github.io/content-empire/ (needs independent domain)
- **Funding:** GitHub Sponsors configured (FUNDING.yml)

## Content Produced

### Articles — Medium-Ready (5)
Located in `medium-ready/`:
- 01-building-ai-agent-teams.md
- 02-mcp-servers-plugin-system.md
- 03-playwright-beyond-testing.md
- 04-content-empire-zero-employees.md
- 05-hidden-cost-of-not-automating.md

### Articles — Dev.to-Ready (3)
Located in `devto-ready/`:
- 01-ai-agent-teams.md
- 02-mcp-servers.md
- 03-hidden-cost-not-automating.md

### Articles — Site Posts (11)
Located in `site/content/posts/`:
- build-content-empire.md
- building-ai-agent-teams.md
- content-empire-zero-employees.md
- durable-task-aspire.md
- hidden-cost-of-not-automating.md
- indie-game-dev-2026.md
- kubernetes-for-side-projects.md
- mcp-servers-plugin-system.md
- non-human-accounts.md
- playwright-beyond-testing.md
- _index.md (listing page)

**Total unique articles: ~10** (some cross-posted across platforms)

### Course Product
- **"AI-Powered Development: From Copilot to Full Agent Teams"** — 7 modules
  - Defined in `course-product.md`
  - Early Bird: $9.99 | Full Price: $19.99 | Team: $14.99/seat
  - Modules: AI Landscape, Prompt Engineering, Code Review, AI Agents, Multi-Agent, Production, Future

### Hugo Static Site
- **Generator:** Hugo (`site/hugo.toml`)
- **Built output:** `docs/` directory (~106 files)
- **Menu:** Articles, Courses, About
- **Output formats:** HTML + RSS

## Supporting Materials

### Brand & Marketing
- `brand/brand-guide.md` — Brand guidelines
- `brand/cross-posting-workflow.md` — Cross-platform publishing workflow
- `social/profiles.md` — Social media profile configs
- `content-calendar/calendar-2025.md` — Content calendar

### Publishing
- `PUBLISHING_CHECKLIST.md` — Detailed guide for Medium (5 articles) + Dev.to (3 articles)
  - Includes publishing schedule, SEO tips, social sharing steps
  - Medium: Days 1, 3, 5, 8, 10
  - Dev.to: Days 2, 4, 9 (staggered)

### Monetization
- `monetization/gumroad-product-listing.md` — Gumroad product creation guide
- `config/affiliates.json` — Affiliate program configs
- `ads-setup.md` — AdSense setup instructions
- `REVENUE_STRATEGY.md` — Revenue strategy document

## GitHub Actions Workflows
- `deploy.yml` — Site deployment workflow (publishes `docs/` + root `index.html` landing page to GitHub Pages)
- `post-medium.yml`, `substack-newsletter.yml`, `upload-youtube.yml`, `deploy-netlify.yml`

## Live URLs (verified 2026-07-28)
- Site: https://content-empire-pub.github.io/content-empire/ — 200
- Gumroad store: https://squadai.gumroad.com — 200
  - `/l/squad-mastery` ($14.99), `/l/ai-powered-dev` ($9.99), `/l/prompt-cheatsheet` ($4.99) — all 200
- ⚠️ `https://content-empire.netlify.app/` is dead (404). All references replaced with the GitHub Pages URL.
- ⚠️ Two Gumroad stores exist: `squadai.gumroad.com` (used by all repo content) and
  `tdsquad.gumroad.com` (referenced by the `GUMROAD_STORE_URL` repo variable). The
  `GUMROAD_AI_COURSE_ID=jnmqpd` / K8s `nnefv` product IDs only resolve on `tdsquad`.
  These need to be consolidated onto one store.

## GitHub Issues
- Tracked in `GITHUB_ISSUES.md` (4 key issues):
  1. Launch Course on Gumroad (Early Bird $9.99/$19.99)
  2. Set Up GitHub Sponsors (3 tiers: $5, $15, $50/month)
  3. Launch Newsletter (target: 500+ subscribers in 3 months)
  4. Create First Digital Product (Prompt Engineering Cheat Sheet $4.99)

## Pending Actions
- [ ] **BLOCKED** Fix `deploy.yml` to publish `docs/` (see org issue #2). Patch is on local
      branch `fix/deploy-full-site`; cannot be pushed without a `workflow`-scoped token.
      Verified live: `/posts/` returns 404 because only `index.html` is deployed.
- [ ] **BLOCKED** Grant push access on `content-empire-pub/content-empire` (see org issue #3)
- [ ] Consolidate Gumroad stores (squadai vs tdsquad) and update `GUMROAD_STORE_URL` variable
- [ ] Publish 5 articles to Medium (follow PUBLISHING_CHECKLIST.md schedule)
- [ ] Publish 3 articles to Dev.to
- [ ] Create Gumroad listing for AI-Powered Dev course
- [ ] Deploy to independent hosting (Netlify/Vercel)
- [ ] Set up Substack newsletter
- [ ] Register real AdSense publisher ID
- [ ] Create social media accounts (Dev.to, Medium, Hashnode, X)
- [ ] Create Prompt Engineering Cheat Sheet product ($4.99)
- [ ] Set up Medium cross-posting API automation
