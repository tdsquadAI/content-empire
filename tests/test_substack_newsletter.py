import contextlib
import importlib.util
import io
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "substack-newsletter.py"
spec = importlib.util.spec_from_file_location("substack_newsletter", SCRIPT)
if spec is None or spec.loader is None:
    raise ImportError(f"Cannot load {SCRIPT}")
newsletter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(newsletter)


class NewsletterArticleLinksTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.articles = self.root / "medium-ready"
        self.articles.mkdir()
        self.posts = self.root / "docs" / "posts"
        for name, value in (
            ("REPO_ROOT", self.root),
            ("ARTICLES_DIR", self.articles),
            ("PUBLISHED_POSTS_DIR", self.posts),
        ):
            patcher = patch.object(newsletter, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)

    def add_article(self, filename, title, modified):
        path = self.articles / filename
        path.write_text(
            f"# {title}\n\nA sufficiently long summary for the newsletter article.\n",
            encoding="utf-8",
        )
        os.utime(path, (modified, modified))
        return path

    def add_post(self, slug):
        page = self.posts / slug / "index.html"
        page.parent.mkdir(parents=True)
        page.write_text("<html>Published article</html>", encoding="utf-8")

    def test_selects_published_articles_before_applying_limit(self):
        self.add_article("99-unpublished.md", "Unpublished", 400)
        alpha = self.add_article("01-alpha.md", "Alpha", 300)
        beta = self.add_article("beta.md", "Beta", 200)
        self.add_article("03-gamma.md", "Gamma", 100)
        for slug in ("alpha", "beta", "gamma"):
            self.add_post(slug)

        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            selected = newsletter.pick_articles(self.articles, 2)

        self.assertEqual(
            selected,
            [
                (alpha, "https://content-empire-pub.github.io/content-empire/posts/alpha/"),
                (beta, "https://content-empire-pub.github.io/content-empire/posts/beta/"),
            ],
        )
        self.assertIn("99-unpublished.md: no matching built site page", output.getvalue())

    def test_export_without_credentials_links_only_to_published_posts(self):
        self.add_article("01-alpha.md", "Alpha", 100)
        self.add_article("unpublished.md", "Unpublished", 200)
        self.add_post("alpha")

        with (
            patch.object(sys, "argv", ["substack-newsletter.py"]),
            patch.dict(
                os.environ,
                {"SUBSTACK_SESSION_COOKIE": "", "SUBSTACK_PUBLICATION_URL": ""},
            ),
            patch.object(newsletter, "substack_post") as post,
            contextlib.redirect_stdout(io.StringIO()),
        ):
            newsletter.main()

        draft = (self.root / "newsletter-draft.html").read_text(encoding="utf-8")
        self.assertIn(
            'href="https://content-empire-pub.github.io/content-empire/posts/alpha/"',
            draft,
        )
        self.assertNotIn("Unpublished", draft)
        post.assert_not_called()

    def test_blocked_substack_attempt_preserves_correct_draft(self):
        self.add_article("01-alpha.md", "Alpha", 100)
        self.add_post("alpha")
        with (
            patch.object(sys, "argv", ["substack-newsletter.py"]),
            patch.dict(
                os.environ,
                {
                    "SUBSTACK_SESSION_COOKIE": "test-cookie",
                    "SUBSTACK_PUBLICATION_URL": "https://newsletter.example",
                },
            ),
            patch.object(
                newsletter,
                "substack_post",
                side_effect=newsletter.CloudflareBlockedError(403),
            ) as post,
            contextlib.redirect_stdout(io.StringIO()),
            contextlib.redirect_stderr(io.StringIO()),
            self.assertRaises(SystemExit) as exit_context,
        ):
            newsletter.main()

        self.assertEqual(exit_context.exception.code, 0)
        draft = (self.root / "newsletter-draft.html").read_text(encoding="utf-8")
        expected_link = 'href="https://content-empire-pub.github.io/content-empire/posts/alpha/"'
        self.assertIn(expected_link, draft)
        self.assertNotIn('href="https://newsletter.example"', draft)
        self.assertEqual(post.call_args.args[0], "https://newsletter.example")
        self.assertIn(expected_link, post.call_args.args[2]["draft_body"])

    def test_no_published_posts_fails_without_creating_a_draft(self):
        self.add_article("unpublished.md", "Unpublished", 100)
        output = io.StringIO()
        with (
            patch.object(sys, "argv", ["substack-newsletter.py"]),
            patch.dict(
                os.environ,
                {"SUBSTACK_SESSION_COOKIE": "", "SUBSTACK_PUBLICATION_URL": ""},
            ),
            contextlib.redirect_stdout(output),
            contextlib.redirect_stderr(io.StringIO()),
            self.assertRaises(SystemExit) as exit_context,
        ):
            newsletter.main()

        self.assertEqual(exit_context.exception.code, 1)
        self.assertFalse((self.root / "newsletter-draft.html").exists())
        self.assertIn("no matching built site page", output.getvalue())


if __name__ == "__main__":
    unittest.main()
