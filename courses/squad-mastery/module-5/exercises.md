# Module 5: Exercises

## Exercise 1: Set Up a Multi-Brand Structure

**Objective:** Create the directory structure for a multi-brand content operation.

### Steps

1. Create the brand structure:
   ```bash
   mkdir -p content-empire/brands/techai-explained
   mkdir -p content-empire/brands/jellybolt-games
   mkdir -p content-empire/brands/codeplay-academy
   mkdir -p content-empire/shared/skills
   mkdir -p content-empire/shared/templates
   ```

2. Initialize Squad in one brand:
   ```bash
   cd content-empire/brands/jellybolt-games
   git init
   squad init
   ```

3. Customize the team for game development:
   - Edit `.squad/team.md` to have game-specific roles (Designer, Developer, QA, Publisher)
   - Edit `.squad/routing.md` with game-specific routing rules

4. Create a simple game to validate the pipeline:
   ```
   Team, build a simple "Click Counter" game in HTML5:
   - Display a button and a counter
   - Button says "Click Me!"
   - Counter tracks total clicks and clicks per second
   - Celebrate milestones (100, 500, 1000 clicks)
   ```

5. Verify the output: Is the game playable in a browser?

---

## Exercise 2: Content Multiplication

**Objective:** Generate multiple content pieces from a single product.

### Steps

1. After building a game in Exercise 1, generate companion content:

   **Article:**
   ```
   Kobayashi, write a technical article titled "Building a Browser Game 
   in 10 Minutes with AI" based on the Click Counter game we just built. 
   Include code snippets, design decisions, and lessons learned.
   Save to articles/click-counter-article.md
   ```

   **Video Script:**
   ```
   McManus, write a YouTube video script for a 5-minute tutorial on 
   building this Click Counter game. Use [VISUAL] and [NARRATION] 
   markers. Include a hook, demo walkthrough, and CTA.
   Save to video-scripts/click-counter-tutorial.md
   ```

   **Course Exercise:**
   ```
   Kobayashi, create a hands-on exercise for students where they extend 
   the Click Counter with: (1) a high score tracker, (2) a reset button, 
   (3) difficulty levels. Include starter code and expected outcomes.
   Save to course-content/click-counter-exercise.md
   ```

2. Count: How many content pieces came from one game? (Should be 4+: game, article, video script, exercise)

---

## Exercise 3: Batch Game Production

**Objective:** Build multiple games in parallel using the batching strategy.

### Steps

1. Design three games at once:
   ```
   Keaton, design three simple HTML5 games:
   1. "Color Match" — a memory card matching game
   2. "Number Rush" — a math quiz with a timer
   3. "Snake Classic" — classic snake game
   
   For each game, specify: core mechanic, controls, 
   scoring system, and win/lose conditions.
   Save designs to .squad/dropbox/game-designs/
   ```

2. Implement all three in parallel:
   ```
   Team, implement all three games from Keaton's designs:
   - McManus: Implement the Canvas rendering for each
   - Verbal: Implement game logic and state for each
   Each game should be in its own directory: games/color-match, 
   games/number-rush, games/snake-classic
   ```

3. Test all three:
   ```
   Fenster, test each game:
   - Does it load without errors?
   - Are controls responsive?
   - Does scoring work correctly?
   - Does the game properly end?
   ```

4. Measure: How long did the batch of 3 take? Estimate how long 3 sequential games would take.

---

## Exercise 4: Publishing Pipeline Setup

**Objective:** Create a publishing metadata pipeline.

### Steps

1. For each game from Exercise 3, generate publishing metadata:
   ```
   Kobayashi, for each game in the games/ directory, create a 
   metadata.json file with:
   - title
   - tagline (max 100 chars)
   - description (2-3 paragraphs)
   - genre tags (3-5)
   - controls description
   - screenshots to capture (describe 3 key moments)
   ```

2. Generate a portfolio page:
   ```
   McManus, create an index.html that showcases all our games 
   in a responsive grid layout. Each game card should show:
   - Title and tagline
   - Genre tags
   - Play button (links to the game)
   Use a clean, modern design with CSS Grid.
   ```

3. Review: Is the portfolio page functional? Does it correctly link to all games?

---

## Exercise 5: The Full Empire Pipeline

**Objective:** Run the complete content empire pipeline end-to-end.

### Steps

1. Start with a single concept: "Build a Tower Defense game"

2. Execute the full pipeline:

   **Product creation:**
   ```
   Team, build a tower defense game. Enemies walk a path, player 
   places towers to stop them. 5 wave levels, 3 tower types.
   ```

   **Testing:**
   ```
   Fenster, full QA on the tower defense game.
   ```

   **Content multiplication:**
   ```
   Kobayashi, generate for the tower defense game:
   1. itch.io metadata (metadata.json)
   2. Technical article: "How AI Built a Tower Defense Game"
   3. README.md with credits and play instructions
   ```

   **Video script:**
   ```
   McManus, write a 7-minute video script: "I Asked AI to Build 
   a Tower Defense Game — The Results Shocked Me"
   Use [VISUAL] and [NARRATION] markers.
   ```

   **Course content:**
   ```
   Kobayashi, create a course lesson: "Building Tower Defense Games 
   with HTML5 Canvas" with exercises and a quiz.
   ```

3. Final count — from one concept, you should have:
   - 1 playable game
   - 1 itch.io metadata file
   - 1 technical article
   - 1 README
   - 1 video script
   - 1 course lesson with exercises + quiz
   - **Total: 6+ content pieces from 1 concept**

4. Reflection: Write down the total time spent. Calculate the content multiplication factor (pieces / time). How does this compare to creating each piece manually?
