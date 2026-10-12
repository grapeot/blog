import importlib.util
from pathlib import Path

OUTPUT = Path(__file__).parent.parent / "output"
PLUGIN = Path(__file__).parent.parent / "plugins" / "markdown_twin.py"


def load_plugin():
    spec = importlib.util.spec_from_file_location("markdown_twin", PLUGIN)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestMarkdownTwinUnit:
    def test_strips_yaml_and_native_frontmatter(self):
        plugin = load_plugin()
        yaml_body = plugin.strip_frontmatter(
            "---\nTitle: 标题\nSlug: 中文-slug\n---\n\n正文\n"
        )
        native_body = plugin.strip_frontmatter("Title: 标题\nSlug: kept-slug\n\n正文\n")
        assert yaml_body == "正文\n"
        assert native_body == "正文\n"
        assert "Slug:" not in yaml_body

    def test_image_urls_are_absolute_and_idempotent(self):
        plugin = load_plugin()
        source = (
            "![a](images/a.jpg)\n"
            "![b](/images/b.jpg)\n"
            '<img src="images/c.jpg" alt="c">\n'
            "<img src='/images/d.jpg'>\n"
            "[essay](/other.html)\n"
            "![ext](https://example.com/images/e.jpg)\n"
            "`images/keep.jpg`\n"
            "```\n"
            "![sample](/images/in-fence.jpg)\n"
            "```\n"
        )
        once = plugin.rewrite_site_images(source, "https://yage.ai")
        twice = plugin.rewrite_site_images(once, "https://yage.ai")
        assert "https://yage.ai/images/a.jpg" in once
        assert "https://yage.ai/images/b.jpg" in once
        assert 'src="https://yage.ai/images/c.jpg"' in once
        assert "src='https://yage.ai/images/d.jpg'" in once
        assert "[essay](/other.html)" in once
        assert "![ext](https://example.com/images/e.jpg)" in once
        assert "`images/keep.jpg`" in once
        assert "![sample](/images/in-fence.jpg)" in once
        assert once == twice

    def test_cjk_slug_uses_save_as_not_source_filename(self):
        plugin = load_plugin()
        assert plugin.twin_relpath("中文-slug.html") == "中文-slug.md"
        assert plugin.twin_href("中文-slug.html") == "./中文-slug.md"
        assert plugin.twin_href("drafts/中文-slug.html") == "./中文-slug.md"
        assert plugin.twin_relpath("drafts/中文-slug.html") == "drafts/中文-slug.md"


class TestMarkdownTwinBuild:
    def test_chinese_slug_mismatch_twin(self):
        md_path = OUTPUT / "written-at-the-end-of-summer.md"
        html_path = OUTPUT / "written-at-the-end-of-summer.html"
        assert md_path.is_file()
        assert not (OUTPUT / "write-in-the-end-of-summer.md").exists()
        text = md_path.read_text(encoding="utf-8")
        assert text.startswith("还记得当时刚去加州的时候")
        assert "Slug:" not in text
        assert 'src="https://yage.ai/images/low-steps-2012-summer.jpg"' in text
        assert 'src="images/' not in text
        html = html_path.read_text(encoding="utf-8")
        assert (
            '<link rel="alternate" type="text/markdown" href="./written-at-the-end-of-summer.md">'
            in html
        )
        assert 'href="/written-at-the-end-of-summer.md"' not in html

    def test_english_twin_rewrites_both_image_forms(self):
        text = (OUTPUT / "ai-coding-en.md").read_text(encoding="utf-8")
        html = (OUTPUT / "ai-coding-en.html").read_text(encoding="utf-8")
        assert "![Framework](https://yage.ai/images/ai-code-framework-en.png)" in text
        assert "![UI](https://yage.ai/images/ai-code-ui-en.jpg)" in text
        assert "![Framework](/images/" not in text
        assert "![UI](images/" not in text
        assert (
            '<link rel="alternate" type="text/markdown" href="./ai-coding-en.md">'
            in html
        )

    def test_chinese_prose_twin_has_no_frontmatter(self):
        text = (OUTPUT / "ai-creativity.md").read_text(encoding="utf-8")
        html = (OUTPUT / "ai-creativity.html").read_text(encoding="utf-8")
        assert text.startswith("在谈AI和创意之前")
        assert "Title:" not in text.splitlines()[0]
        assert (
            '<link rel="alternate" type="text/markdown" href="./ai-creativity.md">'
            in html
        )
