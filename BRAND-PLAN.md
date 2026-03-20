# Content Empire — Brand Plan

## Mission

Aggregate, curate, and distribute high-quality tech content across multiple platforms to build audience and revenue through syndication, SEO, and monetization.

## Revenue Streams

| Stream           | Platform         | Status           | Notes                                |
|-----------------|------------------|------------------|--------------------------------------|
| Ad Revenue       | Google AdSense   | ⏳ Pending signup | Site monetization                    |
| Affiliates       | Multiple         | ⏳ Pending signup | Tech product affiliate links         |
| Digital Products | Gumroad          | ✅ Active         | Via TechAI Explained store           |
| Sponsored Posts  | Direct           | 📋 Planned        | Sponsored content on blog            |

## Distribution Channels

| Channel       | Purpose                      | Frequency      | Status         |
|---------------|------------------------------|----------------|----------------|
| Medium        | Long-form articles           | 2-3x/week      | 📋 Planned     |
| Dev.to        | Developer-focused articles   | 2-3x/week      | 📋 Planned     |
| Hashnode      | Cross-posted articles        | 2-3x/week      | 📋 Planned     |
| Substack      | Newsletter                   | Weekly          | 📋 Planned     |
| Site (static) | SEO landing pages            | Ongoing         | ✅ Active       |
| Reddit        | Community posts              | 2-3x/week      | 📋 Planned     |

## Automation

### Current
- Content calendar managed via GitHub Issues
- Static site generation

### Planned
- Medium cross-posting via API
- Substack newsletter auto-generation
- Dev.to API cross-posting
- Social media scheduled posting
- RSS-to-newsletter pipeline

## Cross-Brand Promotion

| From              | To                | Method                           |
|-------------------|-------------------|----------------------------------|
| Content Empire    | TechAI Explained  | Feature daily briefs in articles  |
| Content Empire    | JellyBolt Games   | GameDev content syndication       |
| TechAI Explained  | Content Empire    | Syndicate articles to platforms   |

## Content Calendar

### Weekly
- Monday: Plan content for the week
- Tue–Thu: Publish 1 article per day (cross-posted)
- Friday: Newsletter draft
- Weekend: Social media engagement

### Monthly
- Review top-performing articles
- Update SEO keywords
- Refresh affiliate links
- Analyze traffic sources

## Key Metrics
- Article views across platforms
- Newsletter subscriber count
- Affiliate click-through rates
- SEO ranking for target keywords
- Revenue per article

## Session History

### March 19–20, 2026 — Major Build Session
- **Agents used:** 87 AI agents (squad pattern across all 3 brands)
- **Files created/modified:** 250+ (across all repos)

**What was built:**
- 10 unique articles (cross-posted to Medium-ready, Dev.to-ready, and site)
- 5 Medium-ready articles with SEO tags and canonical URLs
- 3 Dev.to-ready articles formatted for Dev.to API
- Hugo static site with 11 posts, ~106 built pages in docs/
- Complete publishing checklist (PUBLISHING_CHECKLIST.md) with staggered schedule
- 7-module AI-Powered Development course product listing
- Brand guide and cross-posting workflow docs
- Content calendar for 2025
- Gumroad product listing templates
- Affiliate configs (config/affiliates.json)
- Revenue strategy document
- Social media profile configs
- GitHub Actions deploy workflow

**Key decisions:**
- Hugo as static site generator (fast, Go-based)
- Cross-posting strategy: stagger Medium (days 1,3,5,8,10) and Dev.to (days 2,4,9)
- Course pricing: Early Bird $9.99, Full $19.99, Team $14.99/seat
- Content Empire as aggregation/syndication hub for all brands
- GitHub Pages for initial hosting (plan to migrate to independent domain)
