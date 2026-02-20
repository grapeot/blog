"""Test that all blog articles have Summary metadata for SEO."""
import pytest
from pathlib import Path


CONTENT_DIR = Path(__file__).parent.parent / "content"


def get_all_articles():
    """Get all markdown articles in content directory."""
    return list(CONTENT_DIR.glob("*.md"))


def has_summary(filepath: Path) -> bool:
    """Check if article has Summary field in front matter."""
    content = filepath.read_text(encoding="utf-8")
    return "Summary:" in content


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


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
