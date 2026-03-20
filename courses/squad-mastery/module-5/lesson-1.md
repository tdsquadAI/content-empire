# Module 5: Building Your Own Content Empire

## What You'll Learn
- Setting up a multi-brand content operation with Squad
- Automating publishing across platforms
- Game development pipelines with AI agent teams
- Scaling from one product to many

---

## Lesson 1: Multi-Brand Setup

A content empire starts with brands. Each brand serves a different audience but shares the same AI team infrastructure.

### Brand Architecture

```
content-empire/
├── brands/
│   ├── techai-explained/     # YouTube tech channel
│   │   ├── .squad/           # Channel-specific team
│   │   ├── video-scripts/
│   │   └── articles/
│   ├── jellybolt-games/      # Game studio
│   │   ├── .squad/           # Game dev team
│   │   ├── games/
│   │   └── devlogs/
│   └── codeplay-academy/     # Course platform
│       ├── .squad/           # Education team
│       ├── courses/
│       └── tutorials/
├── shared/
│   ├── skills/               # Shared across brands
│   ├── templates/            # Content templates
│   └── publishing/           # Publishing automation
└── .squad/                   # Master team
```

### Team Customization Per Brand

Each brand gets its own Squad configuration tailored to its content type:

**Tech YouTube Channel Team:**
```markdown
# .squad/team.md for TechAI Explained

## Team Roster
| Role | Agent | Expertise |
|------|-------|-----------|
| Producer | Keaton | Video strategy, scripting structure |
| Scriptwriter | McManus | Technical writing, hooks, CTAs |
| Researcher | Verbal | Deep-dive technical research |
| Editor | Fenster | Script review, fact-checking |
| SEO | Kobayashi | Titles, descriptions, tags, thumbnails |
```

**Game Studio Team:**
```markdown
# .squad/team.md for JellyBolt Games

## Team Roster
| Role | Agent | Expertise |
|------|-------|-----------|
| Designer | Keaton | Game mechanics, level design |
| Developer | McManus | HTML5 Canvas, Three.js, WebGL |
| Logic | Verbal | Game state, physics, AI |
| QA | Fenster | Gameplay testing, bug reports |
| Publisher | Kobayashi | itch.io metadata, marketing copy |
```

### Setting Up Multiple Brands

```bash
# Create brand directories
mkdir -p brands/techai-explained
mkdir -p brands/jellybolt-games
mkdir -p brands/codeplay-academy

# Initialize Squad in each
cd brands/techai-explained && squad init && cd ../..
cd brands/jellybolt-games && squad init && cd ../..
cd brands/codeplay-academy && squad init && cd ../..
```

---

## Lesson 2: Platform Publishing Automation

Once content is created, automate publishing across platforms.

### Video Publishing Pipeline

```
Script Created
    ↓
Kobayashi generates metadata:
  - YouTube title (optimized for CTR)
  - Description (with links, timestamps)
  - Tags (15-20 relevant keywords)
  - Thumbnail text suggestions
    ↓
Output: video-metadata.json
{
  "title": "I Let AI Agents Run My Entire Dev Team",
  "description": "What happens when...",
  "tags": ["ai agents", "squad", "github copilot", ...],
  "thumbnailText": "AI TEAM",
  "category": "Science & Technology",
  "playlist": "AI Agent Deep Dives"
}
```

### Article Publishing Pipeline

```
Technical Content Created
    ↓
McManus reformats for each platform:
  ├── blog/article.md (full article with code blocks)
  ├── dev-to/article.md (dev.to formatted with frontmatter)
  ├── medium/article.md (Medium-optimized formatting)
  └── linkedin/post.md (condensed for LinkedIn)
    ↓
Each format includes platform-specific:
  - Frontmatter/metadata
  - Image references
  - CTAs appropriate to the platform
  - Cross-promotion links
```

### Game Publishing Pipeline

```
Game Completed + Tested
    ↓
Kobayashi generates itch.io metadata:
  - Game title and tagline
  - Full description with features
  - Screenshots (described for capture)
  - Tags and genre classification
  - System requirements
  - Credits
    ↓
Output: itch-metadata.json
{
  "title": "Neon Runner",
  "tagline": "A procedurally generated neon platformer",
  "genre": ["platformer", "action", "procedural"],
  "tags": ["html5", "browser", "pixel-art"],
  "description": "Sprint through neon-lit levels...",
  "controls": { "arrows": "Move", "space": "Jump" }
}
```

### Automation Script Pattern

```bash
#!/bin/bash
# publish-game.sh - Automated game publishing

GAME_DIR=$1
GAME_NAME=$(basename $GAME_DIR)

echo "📦 Publishing $GAME_NAME..."

# Generate metadata
echo "Kobayashi, generate itch.io metadata for $GAME_DIR" | squad shell

# Build the game
cd $GAME_DIR
npm run build

# Create distribution zip
zip -r dist/$GAME_NAME.zip build/

# Publish to itch.io (using butler)
butler push dist/$GAME_NAME.zip "studio/$GAME_NAME:html5"

echo "✅ $GAME_NAME published!"
```

---

## Lesson 3: Game Development with AI Teams

### The Game Development Pipeline

Building games with Squad follows a structured pipeline:

**Phase 1: Design**
```
Keaton, design a puzzle game with these constraints:
- Browser-based (HTML5 Canvas)
- Single-player
- Progressive difficulty (20 levels)
- Core mechanic: color matching with chain reactions
- Session length: 5-10 minutes
```

**Phase 2: Implementation**
```
Team, implement the game Keaton designed:
- McManus: Canvas rendering, UI, animations
- Verbal: Game logic, scoring, level generation  
- Use the game state pattern from our skills
```

**Phase 3: Polish**
```
Team, polish the game:
- McManus: Add particle effects and screen shake
- Verbal: Add sound effect triggers (list sounds needed)
- McManus: Mobile touch controls
```

**Phase 4: Testing**
```
Fenster, QA the game:
- Play through all 20 levels
- Test edge cases (rapid clicking, resize, tab switch)
- Check mobile responsiveness
- Verify score tracking
```

**Phase 5: Publishing**
```
Kobayashi, prepare for publishing:
- Game description for itch.io
- Screenshot descriptions (5 key moments)
- Tags and genre classification
- README with credits and controls
```

### Scaling Game Production

The key to producing many games quickly is **standardization and parallel batching**:

```
Batch 1 (Games 1-3): Design all three simultaneously
  → Keaton designs Game 1, Game 2, Game 3

Batch 1 Implementation: Build all three in parallel
  → McManus implements each game
  → Verbal handles logic for each

Batch 2 (Games 4-6): Design while Batch 1 is being built
  → Keaton designs Game 4, Game 5, Game 6

Batch 1 Testing: Test while Batch 2 is being built
  → Fenster tests Games 1-3

This pipeline keeps every agent busy at all times.
```

### Game Types That Work Well with AI Teams

| Type | Complexity | Agents Needed | Time Estimate |
|------|-----------|---------------|---------------|
| Clicker/Idle | Low | McManus + Verbal | 30 min |
| Puzzle (2D) | Medium | McManus + Verbal + Fenster | 1-2 hours |
| Platformer (2D) | Medium | All agents | 2-3 hours |
| Arcade (2D) | Medium | McManus + Verbal | 1-2 hours |
| 3D Explorer | High | All agents | 3-5 hours |
| 3D Action | High | All agents | 4-6 hours |

---

## Lesson 4: Scaling from 1 to 21 Products

### The Scaling Mindset

The difference between 1 product and 21 isn't doing things 21 times — it's building systems that multiply.

### Level 1: Single Product (Day 1-2)

```
Focus: Build one complete game
Learning: How the pipeline works
Output: 1 game + 1 article + 1 video script
```

### Level 2: Product Line (Day 3-7)

```
Focus: Build 5 games with shared patterns
Learning: What can be standardized
Output: 5 games + 5 articles + 5 video scripts

Key insight: Standardize the game state shape, 
rendering loop, and input handling. Games 3-5 
build 2x faster because patterns are established.
```

### Level 3: Content Empire (Day 8-14)

```
Focus: Build 15+ games + full content ecosystem
Learning: Multi-brand coordination
Output: 
  - 15+ games on itch.io
  - 15+ technical articles
  - 10+ video scripts
  - 1 complete course (5 modules)
  - Cross-promotion across all channels

Key insight: Content multiplication. Each product 
generates 3-5 content pieces. Agent skills make 
each subsequent product faster.
```

### The Compound Effect

```
Session 1:  Agent knows nothing → slow, exploratory
Session 5:  Agent knows your patterns → faster, consistent
Session 10: Agent has deep knowledge → autonomous, high quality
Session 20: Agent is an expert in YOUR project → nearly autonomous
```

### Metrics to Track

| Metric | What It Tells You |
|--------|-------------------|
| Time per game | Pipeline efficiency |
| Decisions reused | Knowledge compounding |
| Manual interventions | Autonomy level |
| Content pieces per product | Multiplication factor |
| Quality score (1-10) | Whether speed hurts quality |

---

## Lesson 5: The Content Empire Playbook

Here's the complete playbook for building a content empire with Squad:

### Week 1: Foundation

```
Day 1: Set up Squad, build 1 product end-to-end
Day 2: Refine team config, build 2 more products
Day 3: Establish publishing pipelines
Day 4-5: Build 5 products with established patterns
Day 6-7: Generate companion content for all products
```

### Week 2: Expansion

```
Day 8-9: Set up multiple brands
Day 10-11: Build 10 more products across brands
Day 12: Cross-promote across channels
Day 13-14: Create course from accumulated knowledge
```

### Week 3: Automation

```
Day 15: Set up Ralph for autonomous work
Day 16-17: Create issue templates for product types
Day 18-19: Ralph processes issues → products → content
Day 20-21: Monitor, iterate, scale
```

### The Flywheel

```
Products → Content → Audience → Feedback → Better Products
    ↑                                            ↓
    └────────── Agent Knowledge ←────────────────┘
```

Each product teaches your agents more. Each piece of content reaches more people. Each bit of feedback improves the next product. And all of it is captured in git — your agents' accumulated knowledge is a growing competitive advantage.

### Final Thoughts

Building a content empire with AI agent teams isn't about replacing creativity — it's about multiplying execution speed. You bring the ideas, the taste, and the quality bar. The agents bring tireless parallel execution, perfect memory, and 24/7 availability. Together, you can build in weeks what used to take months.

The tools are open source. The playbook is in your hands. Start with one product, nail the pipeline, and scale from there.
