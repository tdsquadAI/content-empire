# Content Empire — Project Status
Last updated: 2026-11-11

## Ralph Watch — 2026-11-11

- Checked both repositories: 25 open primary issues, 1 open organization issue,
  and no open PRs. Both main branches and the clean checkout started at
  `09e6eb0`. Latest Pages deployments succeeded; the homepage, `/posts/`,
  and `/pages/about/` returned HTTP 200.
- At the start of this watch, organization Netlify run `41977470319` failed
  because `NETLIFY_AUTH_TOKEN` and `NETLIFY_SITE_ID` are missing. Primary
  Netlify remains manually disabled; no ineffective rerun was requested.
- November 9 Medium runs `42691180931` (primary) and `42692866672`
  (organization) each created 0 Medium drafts and exported 10 HTML files.
  Organization artifact `13708141346` expires November 23. Corresponding
  primary and organization HTML files have identical hashes.
- November 6 newsletter runs did not create a Substack draft: organization
  run `42285736025` lacked both Substack settings, and primary run
  `42285973121` received HTTP 403. Their artifacts `13536329335` and
  `13537152495` expire November 20.
- Those saved newsletter drafts point every article link at a homepage. The
  newsletter template still contains a literal `{{unsubscribe_url}}`
  placeholder and English-only text. Do not send any drafts as-is: verify the
  provider's unsubscribe handling and add Hebrew content during manual review.
- Fixed the newsletter generator to select only articles with built site pages
  and link to their individual URLs; it fails explicitly if none are available.
  All five current article URLs returned HTTP 200. Added four focused tests and
  a workflow validation step, plus a summary clarifying that the workflow does
  not send newsletters. The tests and workflow lint pass locally.
- Preserved and verified both sets of 10 Medium HTML files and both newsletter
  HTML drafts in this watch session's local persistent `files/` directory,
  under `medium-2026-11-09-org/`, `medium-2026-11-09-primary/`,
  `newsletter-2026-11-06-org/`, and `newsletter-2026-11-06-primary/`.
  These are local drafts, not publications or cross-machine backups.
- Organization admin and primary push/triage access remain available. No
  credentials were changed, no external content was published, and no blocked
  issue was closed. Follow-up remains organization issue
  `content-empire-pub/content-empire#1` and primary issues #18, #30, and #46.

עברית: נבדקו שני המאגרים: 25 משימות פתוחות במאגר הראשי, אחת בארגון וללא
בקשות משיכה פתוחות. האתר זמין ופריסות Pages הצליחו. Netlify בארגון חסום
בגלל שני סודות חסרים; במאגר הראשי התהליך מושבת.
ריצות Medium מ-9 בנובמבר ייצאו עשר טיוטות בכל מאגר ללא יצירת טיוטה ב-Medium.
ריצות הניוזלטר מ-6 בנובמבר חסומות בהגדרות חסרות בארגון ובשגיאת 403 במאגר
הראשי. שתי קבוצות טיוטות Medium ושתי טיוטות הניוזלטר נשמרו ואומתו מקומית.
בטיוטות הניוזלטר הישנות כל קישורי המאמרים מפנים לדף הבית. תבנית הניוזלטר
עדיין מכילה מציין מקום להסרה ותוכן באנגלית בלבד; אין לשלוח טיוטות ללא בדיקת
הסרה ותרגום לעברית.
המחולל תוקן לקישור מאמרים בעלי עמוד קיים בלבד, וחמש הכתובות נבדקו בהצלחה.
נוספו בדיקות והבהרה שהתהליך אינו שולח ניוזלטרים. לא שונו פרטי גישה, לא
פורסם תוכן ולא נסגרו משימות חסומות.

## Ralph Watch — 2026-11-05

- Checked both repositories: 25 open primary issues, 1 open organization issue,
  and no open PRs. Both main branches and the clean checkout started at
  `3ac31dc`. Latest Pages deployments are successful; the homepage, `/posts/`,
  and `/pages/about/` return HTTP 200.
- Organization Netlify run `41279201637` fails at configuration validation:
  `NETLIFY_AUTH_TOKEN` and `NETLIFY_SITE_ID` are still absent. This is the
  existing configuration blocker, not a build regression. Primary Netlify
  remains manually disabled; no ineffective rerun was requested.
- November 2 Medium runs `41514894114` (organization) and `41513919844`
  (primary) each posted 0 articles and exported 10 HTML drafts. Organization
  artifact `13174243020` expires November 16. Automatic publication remains
  blocked by primary #46; successful export is not successful publication.
- Latest newsletters remain October 30: organization run `41110917713`
  exports only because Substack settings are missing; primary run
  `41110990749` receives HTTP 403 and saves a manual draft. Their artifacts
  `13001839676` and `13002114990` expire November 13.
- Downloaded and verified all 10 November 2 Medium drafts and both October 30
  newsletter drafts in this watch session's persistent `files/` directory:
  `medium-2026-11-02/`, `newsletter-2026-10-30/`, and
  `newsletter-primary-2026-10-30/`. These are preserved drafts, not publications.
- Brand configuration is readable; organization admin and primary push/triage
  access are available. No credentials were exposed or changed. Existing
  follow-up remains organization issue `content-empire-pub/content-empire#1`
  and primary issues #30 and #46. No blocked tasks were closed.

עברית: נבדקו המשימות, בקשות המשיכה ו-CI בשני המאגרים. אין בקשות משיכה
פתוחות והאתר זמין. Netlify עדיין חסום בגלל שני סודות חסרים; לא הופעלה
ריצה חוזרת ללא תיקון ההגדרות. ריצות Medium מ-2 בנובמבר ייצאו עשר טיוטות
ללא פרסום. הניוזלטר מ-30 באוקטובר חסום בהגדרות חסרות או בשגיאת 403.
עשר טיוטות Medium ושתי טיוטות ניוזלטר הורדו, אומתו ונשמרו בתיקיית הסשן
לפני תפוגתן. לא שונו פרטי גישה ולא נסגרו משימות חסומות.

## Ralph Watch — 2026-11-01

- Checked both repositories: 25 open primary issues, 1 open organization issue,
  and no open PRs. Both main branches and the clean checkout started at
  `cf9c521`. Pages CI is green and the homepage, `/posts/`, and `/pages/about/`
  return HTTP 200.
- Organization Netlify run `40409758367` now fails explicitly at configuration
  validation, as intended by the previous fix. Both `NETLIFY_AUTH_TOKEN` and
  `NETLIFY_SITE_ID` are absent; checkout, build, and deployment were skipped.
  This is an unresolved configuration blocker, not a workflow regression.
  No rerun was requested. Primary Netlify remains manually disabled.
- October 30 newsletters did not publish despite green CI. Organization run
  `41110917713` exported HTML because both Substack settings are missing;
  artifact `13001839676` expires November 13. Primary run `41110990749`
  received HTTP 403 and retained artifact `13002114990`.
- Latest Medium runs remain October 26. Organization run `40359911516`
  posted 0 articles and exported 10 HTML drafts; artifact `12666663873`
  expires November 9. Automatic publishing remains blocked by primary #46.
- Downloaded both October 30 newsletter drafts and all 10 October 26 Medium
  drafts into this watch session's persistent `files/` directory, under
  `newsletter-2026-10-30/`, `newsletter-primary-2026-10-30/`, and
  `medium-2026-10-26/`. Verified nonempty HTML content; these are preserved
  drafts, not published content.
- Brand variables are readable; organization admin and primary push/triage
  permissions remain available. No credentials were exposed or changed.
  Publishing/configuration follow-up remains organization issue
  `content-empire-pub/content-empire#1` and primary issues #30 and #46.
  No blocked tasks were closed.

עברית: נבדקו שני המאגרים: אין בקשות משיכה פתוחות והאתר זמין.
Netlify נכשל כעת במפורש בגלל שני סודות חסרים, בהתאם לתיקון הקודם;
לא בוצעה פריסה ולא הופעלה ריצה חוזרת. ריצות הניוזלטר מ-30 באוקטובר
לא פרסמו תוכן: בארגון חסרות הגדרות ובמאגר הראשי התקבלה שגיאת 403.
שתי טיוטות הניוזלטר ועשר טיוטות Medium הורדו ואומתו ונשמרו בתיקיית הסשן.
חסמי הפרסום נותרו פתוחים; לא שונו פרטי גישה ולא נסגרו משימות חסומות.

## Ralph Watch — 2026-10-27

- Checked both repositories: 25 open primary issues, 1 open organization issue,
  and no open PRs. Both main branches and the clean checkout started at
  `0c09ba4`. Recent CI runs were green; no historical retry was needed.
- October 26 Medium runs posted 0 articles and exported 10 HTML drafts on each
  repository. Organization run `40359911516` retains artifact `12666663873`
  until November 9. Downloaded and verified all 10 nonempty drafts in this
  session's persistent `files/medium-2026-10-26/` directory.
- October 25 organization Netlify run `40196084588` again reported success
  without deploying because both required secrets are absent. Added an early
  configuration check to fail explicitly with missing secret names and a job
  summary, before building or invoking the deployment action. Configure
  `NETLIFY_AUTH_TOKEN` and `NETLIFY_SITE_ID` before retrying; this change does
  not provision hosting or claim a successful deployment.
- Primary Netlify remains manually disabled. Medium and newsletter workflows
  remain active on both copies. Latest newsletter evidence is still October 23:
  missing organization Substack settings and HTTP 403 on the primary copy.
- Brand variables are readable; current permissions are organization admin
  and primary push/triage. No credentials were disclosed or changed.
- Pages homepage, `/posts/`, and `/pages/about/` return HTTP 200. Publishing
  blockers remain organization issue `content-empire-pub/content-empire#1`
  and primary issues #30 and #46. No external articles were published and
  no blocked tasks were closed.

עברית: נבדקו שני המאגרים: אין בקשות משיכה פתוחות והריצות האחרונות היו ירוקות.
ריצות Medium מ-26 באוקטובר ייצאו עשר טיוטות ללא פרסום; כולן הורדו ואומתו.
Netlify שוב דיווח על הצלחה ללא פריסה. נוספה בדיקה מוקדמת שמכשילה את הריצה
במפורש כשפרטי הגישה חסרים, בלי לחשוף ערכים. האתר זמין, אך חסמי הפרסום
והגדרות השירותים נותרו פתוחים. לא שונו פרטי גישה ולא פורסמו מאמרים.

## Ralph Watch — 2026-10-25

- Checked both repositories: 25 open primary issues, 1 open organization issue,
  and no open PRs. Recent CI runs are green; historical failures have successful
  successors and do not need reruns.
- Primary main and the clean checkout started at `0c75ec3`; organization main
  was two documentation commits behind at `d240376`. Both copies have the same
  publishing workflow code.
- Brand variables are readable again. Current API permissions report organization
  admin and primary push/triage access. The October 18 read-only finding is
  historical, not the current access state.
- October 19 Medium runs on both copies posted 0 articles and exported 10 HTML
  drafts. Organization run `39288561362` retains artifact `12203423404` until
  November 2. The primary session cookie is configured but unsupported; the
  organization has no Medium publishing credential. Primary issue #46 remains
  open for the external publishing blocker, not the already-shipped CI wiring.
- October 23 newsletter organization run `39999713202` exported HTML because
  both Substack settings are missing. Artifact `12521636968` expires November 6.
  Primary run `39999888050` received HTTP 403 and retained a manual draft.
- Downloaded and verified all 10 latest Medium HTML drafts and the latest
  newsletter HTML in this session's persistent `files/` directory, under
  `medium-2026-10-19/` and `newsletter-2026-10-23/`. These are preserved drafts,
  not published content.
- Organization Netlify still lacks both required secrets; its latest run
  `38523219469` skipped deployment despite reporting success. Primary Netlify
  remains manually disabled. No deployment or publishing rerun is warranted.
- Pages homepage, `/posts/`, and `/pages/about/` return HTTP 200. Current
  publishing/configuration blockers remain organization issue
  `content-empire-pub/content-empire#1` and primary issues #30 and #46.
- No credentials were changed, no external articles were published, and no
  blocked tasks were closed.

עברית: נבדקו שני המאגרים: אין בקשות משיכה פתוחות והריצות האחרונות ירוקות.
ההרשאות חזרו לכתיבה ומשתני המותג נגישים. Medium ייצא עשר טיוטות ללא פרסום;
הניוזלטר נשמר כטיוטה בגלל הגדרות חסרות בארגון ושגיאת 403 במאגר הראשי.
הטיוטות העדכניות הורדו ונשמרו מקומית לפני תפוגתן. האתר זמין, אך Netlify
עדיין לא פרס. לא שונו פרטי גישה ולא נסגרו משימות חסומות.

## Ralph Watch — 2026-10-18

- Both remote main branches and the clean checkout were synchronized at
  `d240376` before this update. No open PRs; 25 open primary issues and
  1 organization issue. Recent CI runs are green; no failed run needs a rerun.
- Current API access is **read-only on both repositories**. Loading organization
  brand variables returns HTTP 403. The October 14 admin/push access finding
  is historical, not current. Configuration cannot currently be verified or
  repaired through the available repository token.
- October 16 newsletter runs still did not publish: organization run
  `38941876609` exported HTML because both Substack settings are missing;
  primary run `38942022228` received HTTP 403. Organization artifact
  `12063167729` expires October 30.
- Medium's latest scheduled organization run remains October 12,
  `38298931504`: 0 posted, 10 drafts exported. Artifact `11770151503` expires
  October 26. Automatic publishing remains blocked by primary issue #46.
- Downloaded and verified all 10 Medium HTML drafts and the October 16 newsletter
  HTML in this watch session's persistent `files/` directory, under
  `medium-2026-10-12/` and `newsletter-2026-10-16/`. These local copies survive
  Actions artifact expiration; they are not published content.
- October 14 organization Netlify run `38523219469` again reported success
  while logging `Netlify credentials not provided, not deployable`. Primary
  Netlify remains manually disabled. Medium and newsletter workflows remain
  active on both repositories; do not re-enable or rerun them unnecessarily.
- Live homepage, `/posts/`, and `/pages/about/` all return HTTP 200.
  Existing follow-up remains organization issue
  `content-empire-pub/content-empire#1` and primary issues #30 and #46.
- Remote updates are blocked: pushes to both repositories return HTTP 403,
  and posting the watch report to organization issue #1 is denied by the
  Enterprise Managed User policy. This status update is retained locally.

עברית: אין בקשות משיכה פתוחות, שני המאגרים מסונכרנים והריצות האחרונות ירוקות.
עם זאת, לא פורסם תוכן: Medium ייצא עשר טיוטות, והניוזלטר חסום בהגדרות חסרות
או בשגיאת 403. הטיוטות הורדו ונשמרו בתיקיית העבודה של הסשן לפני תפוגתן.
Netlify לא פרס למרות דיווח הצלחה. האתר זמין; ההרשאות הנוכחיות בשני המאגרים
הן לקריאה בלבד, והגישה למשתני המותג חסומה.

## Ralph Watch — 2026-10-14

- Both repository copies are synchronized at `1d75996` before this status update.
  There are no open pull requests; the primary repository has 25 open issues and
  the organization repository has 1.
- Recent scheduled Medium and newsletter runs are green on both repositories,
  but **green CI is not evidence of publication**.
- Medium: October 12 runs exported 10 HTML drafts and posted 0 articles.
  Organization run `38298931504` retains artifact `11770151503` until October 26.
  Automatic Medium publishing remains blocked; see primary issue #46.
- Newsletter: the October 9 organization run `37978094544` exported HTML because
  both Substack settings are missing. Artifact `11638879326` expires October 23.
  The primary repository has the settings, but run `37978235766` received HTTP 403
  (bot protection or expired session) and also retained a manual-publishing draft.
- Netlify: organization run `37571023477` reported success while logging
  `Netlify credentials not provided, not deployable`. Neither Netlify secret is
  configured on the organization repository. The primary Netlify workflow is
  manually disabled. Do not treat either as an independent hosting deployment.
- Brand configuration is readable again. The organization token has admin access;
  the primary token has push/triage access but not admin. Earlier permission
  blockers are not evidence of the current access state. Publishing credentials
  must still be provisioned or refreshed; they cannot be recovered from secret
  names alone.
- Live checks: the organization homepage, article listing, and About page return
  HTTP 200. All five product links listed below also return HTTP 200; this checks
  reachability, not checkout, ownership, or revenue. The two-store consolidation
  decision remains unresolved.
- Tracked follow-up: organization issue
  `content-empire-pub/content-empire#1` and primary issues #30 and #46.

עברית: אין בקשות משיכה פתוחות, והריצות האחרונות ירוקות, אך הן אינן מעידות על
פרסום. Medium יצר עשר טיוטות ללא פרסום; הניוזלטר נשמר כטיוטה בגלל הגדרות חסרות
בארגון וחסימת 403 במאגר הראשי. Netlify דיווח על הצלחה ללא פריסה בגלל פרטי גישה
חסרים. האתר וקישורי המוצרים זמינים; נדרשים פרסום ידני או תיקון הגדרות הגישה.

## Brand Identity
- **Name:** Content Empire
- **NEVER mention "real owner identity"** — independent brand
- **Hugo static site** deployed to GitHub Pages (docs/ folder)
- **Base URL:** https://content-empire-pub.github.io/content-empire/ (needs independent domain)
- **Funding:** GitHub Sponsors configured (FUNDING.yml)

## Content Produced

### Articles — Medium-Ready (10)
Located in `medium-ready/`:
- 01-building-ai-agent-teams.md
- 02-mcp-servers-plugin-system.md
- 03-playwright-beyond-testing.md
- 04-content-empire-zero-employees.md
- 05-hidden-cost-of-not-automating.md
- developer-guide-technical-writing.md
- docker-compose-all-you-need.md
- github-actions-guide-2026.md
- rust-vs-go-2026.md
- saas-mvp-weekend-ai.md

### Articles — Dev.to-Ready (6 unique articles, 9 files)
Located in `devto-ready/`:
- 01-ai-agent-teams.md
- 02-mcp-servers.md
- 03-hidden-cost-not-automating.md
- 04-5-prompt-patterns-every-developer-needs.md
- 05-why-ai-agents-replace-scripts.md
- 06-mcp-servers-the-missing-manual.md

The first three also have `-devto.md` variants; do not publish both variants as
separate articles.

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

## Live URLs (verified 2026-10-14)
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
