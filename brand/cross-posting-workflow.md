# Content Empire — Cross-Posting Workflow

## Overview

This document describes the workflow for cross-posting Content Empire articles across multiple platforms.

## Platform Priority

1. **Blog (GitHub Pages)** — Primary, canonical source
2. **Medium** — Cross-post within 24 hours (use canonical URL)
3. **Dev.to** — Cross-post within 48 hours (use canonical URL)
4. **LinkedIn** — Summary + link within 24 hours
5. **Twitter/X** — Thread summary on publish day
6. **Reddit** — Share to relevant subreddits within 48 hours

## Cross-Posting Checklist

### For Each Article:

```markdown
- [ ] Published on blog (canonical URL)
- [ ] Cross-posted to Medium with canonical_url set
- [ ] Cross-posted to Dev.to with canonical_url set
- [ ] LinkedIn post with key takeaways + link
- [ ] Twitter thread (3-5 tweets summarizing key points)
- [ ] Reddit post to 1-2 relevant subreddits
```

### Medium Cross-Posting

1. Use the Import tool: https://medium.com/p/import
2. Paste the blog URL — Medium auto-imports with canonical URL
3. Add Medium-specific tags (up to 5)
4. Add "Originally published at Content Empire" at the bottom
5. Submit to relevant publications

### Dev.to Cross-Posting

Add front matter to the Dev.to version:

```yaml
---
title: "Article Title"
published: true
tags: tag1, tag2, tag3, tag4
canonical_url: https://tamirdresher.github.io/content-empire/posts/article-slug/
---
```

### LinkedIn Posts

Format:
```
[Hook — one compelling line]

[3-4 key takeaways as bullet points]

[Link to full article]

#hashtag1 #hashtag2 #hashtag3
```

### Twitter Threads

Format:
```
Tweet 1: Hook + "Thread 🧵"
Tweet 2-4: Key insights (one per tweet)
Tweet 5: Link to full article + CTA
```

## Automation (Future)

Future automation via GitHub Actions:
- On new post merge to main → auto-post to Dev.to via API
- On new post merge to main → generate LinkedIn summary draft
- On new post merge to main → generate Twitter thread draft
- Drafts stored in `cross-posts/` directory for review

## Canonical URL Strategy

Always set the blog as the canonical source to consolidate SEO value:
- Medium: Uses built-in canonical URL feature
- Dev.to: Uses `canonical_url` front matter
- All other platforms: Link back to original blog post
