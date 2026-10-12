import logging
import os
import re
from itertools import chain

from markdown import Markdown
from pelican import signals
from pelican.utils import pelican_open, sanitised_join

logger = logging.getLogger(__name__)

_FENCE_RE = re.compile(r"^(```|~~~)")
_INLINE_CODE_RE = re.compile(r"(`[^`\n]*`)")
_MD_IMAGE_DEST_RE = re.compile(r"(?P<prefix>\]\()(?P<url>/?images/[^)\s]+)")
_HTML_IMAGE_SRC_RE = re.compile(
    r"""(?P<prefix>\b(?:src|href)=(?P<q>["']))(?P<url>/?images/[^"']+)"""
)


def strip_frontmatter(text):
    parser = Markdown(extensions=["markdown.extensions.meta"])
    body_lines = parser.preprocessors["meta"].run(text.splitlines())
    if body_lines and body_lines[0] == "":
        body_lines = body_lines[1:]
    body = "\n".join(body_lines)
    if not body.endswith("\n"):
        body += "\n"
    return body


def _image_origin(siteurl):
    origin = (siteurl or "https://yage.ai").strip()
    if not origin or origin in {".", ".."} or origin.startswith("."):
        origin = "https://yage.ai"
    return origin.rstrip("/")


def _absolutize_image(url, origin):
    path = url[1:] if url.startswith("/") else url
    if not path.startswith("images/"):
        return url
    return origin + "/" + path


def _rewrite_plain(text, origin):
    def replace(match):
        return match.group("prefix") + _absolutize_image(match.group("url"), origin)

    text = _MD_IMAGE_DEST_RE.sub(replace, text)
    return _HTML_IMAGE_SRC_RE.sub(replace, text)


def rewrite_site_images(text, siteurl):
    origin = _image_origin(siteurl)
    lines = text.split("\n")
    rewritten = []
    in_fence = False
    fence_mark = None
    for line in lines:
        stripped = line.lstrip()
        if not in_fence and _FENCE_RE.match(stripped):
            in_fence = True
            fence_mark = stripped[:3]
            rewritten.append(line)
            continue
        if in_fence:
            if stripped.startswith(fence_mark):
                in_fence = False
            rewritten.append(line)
            continue
        parts = _INLINE_CODE_RE.split(line)
        rewritten.append(
            "".join(
                part if part.startswith("`") else _rewrite_plain(part, origin)
                for part in parts
            )
        )
    return "\n".join(rewritten)


def markdown_for_source(source_text, siteurl):
    return rewrite_site_images(strip_frontmatter(source_text), siteurl)


def twin_relpath(save_as):
    if not isinstance(save_as, str) or not save_as.endswith(".html"):
        return None
    return save_as[: -len(".html")] + ".md"


def twin_href(save_as):
    relpath = twin_relpath(save_as)
    if relpath is None:
        return None
    return "./" + relpath.replace("\\", "/").rsplit("/", 1)[-1]


def iter_articles(generator):
    return chain(
        generator.articles,
        generator.translations,
        generator.hidden_articles,
        generator.hidden_translations,
        generator.drafts,
        generator.drafts_translations,
    )


def attach_markdown_hrefs(generator):
    for article in iter_articles(generator):
        href = twin_href(getattr(article, "save_as", None))
        if href:
            article.markdown_twin_href = href


def write_markdown_twins(generator, writer):
    output_path = writer.output_path
    siteurl = generator.settings.get("SITEURL")
    written = 0
    for article in iter_articles(generator):
        relpath = twin_relpath(getattr(article, "save_as", None))
        source_path = getattr(article, "source_path", None)
        if not relpath or not source_path:
            continue
        with pelican_open(source_path) as source_text:
            body = markdown_for_source(source_text, siteurl)
        dest = sanitised_join(output_path, relpath)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(body)
        written += 1
    logger.info("Wrote %s markdown twins", written)


def register():
    signals.article_generator_finalized.connect(attach_markdown_hrefs)
    signals.article_writer_finalized.connect(write_markdown_twins)
