"""Test that all blog articles have valid Summary metadata for SEO."""
from html.parser import HTMLParser
import re
import pytest
from pathlib import Path


CONTENT_DIR = Path(__file__).parent.parent / "content"
OUTPUT_DIR = Path(__file__).parent.parent / "output"


class MetaParser(HTMLParser):
    """Collect meta tag attributes from generated article HTML."""

    def __init__(self):
        super().__init__()
        self.meta = []

    def handle_starttag(self, tag, attrs):
        if tag == "meta":
            self.meta.append(dict(attrs))


def get_all_articles():
    """Get all markdown articles in content directory."""
    return list(CONTENT_DIR.glob("*.md"))


def has_summary(filepath: Path) -> bool:
    """Check if article has Summary field in front matter."""
    content = filepath.read_text(encoding="utf-8")
    return "Summary:" in content


def get_frontmatter_field(filepath: Path, field: str) -> str | None:
    """Read a single-line field from Markdown front matter."""
    prefix = f"{field}:"
    for line in filepath.read_text(encoding="utf-8").splitlines():
        if line.startswith(prefix):
            return line.split(":", 1)[1].strip()
    return None


def get_meta_content(html_path: Path, *, name: str | None = None, property_: str | None = None) -> str | None:
    parser = MetaParser()
    parser.feed(html_path.read_text(encoding="utf-8"))
    for meta in parser.meta:
        if name and meta.get("name") == name:
            return meta.get("content")
        if property_ and meta.get("property") == property_:
            return meta.get("content")
    return None


def normalize_summary_for_meta(summary: str) -> str:
    """Approximate Pelican's metadata rendering before template striptags."""
    summary = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", summary)
    return summary.replace(r"\[", "[").replace(r"\]", "]")


class TestSummaryCoverage:
    """Tests for Summary field coverage."""
    
    def test_all_articles_have_summary(self):
        """All articles must have a Summary field for SEO."""
        articles = get_all_articles()
        missing_summary = []
        
        for article in articles:
            if not has_summary(article):
                missing_summary.append(article.name)
        
        assert len(missing_summary) == 0, (
            f"The following {len(missing_summary)} articles are missing Summary:\n"
            + "\n".join(missing_summary)
        )
    
    def test_summary_not_empty(self):
        """Summary fields should not be empty."""
        articles = get_all_articles()
        empty_summaries = []
        
        for article in articles:
            content = article.read_text(encoding="utf-8")
            for line in content.split("\n"):
                if line.startswith("Summary:"):
                    summary_content = line.split(":", 1)[1].strip()
                    if not summary_content:
                        empty_summaries.append(article.name)
                    break
        
        assert len(empty_summaries) == 0, (
            f"The following articles have empty Summary:\n"
            + "\n".join(empty_summaries)
        )

    def test_summary_meta_tags_preserve_full_text(self):
        """Generated SEO meta tags must preserve Summary without quote truncation."""
        failures = []

        for article in get_all_articles():
            slug = get_frontmatter_field(article, "Slug")
            summary = get_frontmatter_field(article, "Summary")
            if not slug or not summary:
                continue

            html_path = OUTPUT_DIR / f"{slug}.html"
            if not html_path.exists():
                failures.append(f"{article.name}: missing generated HTML for slug {slug}")
                continue

            checks = {
                "description": get_meta_content(html_path, name="description"),
                "og:description": get_meta_content(html_path, property_="og:description"),
                "twitter:description": get_meta_content(html_path, name="twitter:description"),
            }

            expected = normalize_summary_for_meta(summary)
            for meta_name, actual in checks.items():
                if actual != expected:
                    failures.append(
                        f"{article.name} {meta_name}: expected {expected!r}, got {actual!r}"
                    )

        assert not failures, "SEO meta description mismatch:\n" + "\n".join(failures)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
