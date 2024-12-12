#!/usr/bin/env python3

import re
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# URLs confirmed to be 404
URLS_TO_REMOVE = [
    r'https://yage\.ai/ai-thoughts\.html',
    r'https://yage\.ai/updates-on-beamer-writer\.html',
    r'https://yage\.ai/DJI-pocket-3-first-impression\.html',
    r'https://yage\.ai/code-questions\.html',
    r'/ai-thoughts\.html',
    r'/updates-on-beamer-writer\.html',
    r'/DJI-pocket-3-first-impression\.html',
    r'/code-questions\.html'
]

def remove_404_links(filepath):
    """Remove confirmed 404 links from a markdown file."""
    try:
        content = Path(filepath).read_text(encoding='utf-8')
        original_content = content

        for url_pattern in URLS_TO_REMOVE:
            # Match markdown links containing the URL
            link_pattern = r'\[([^\]]+)\]\(' + url_pattern + r'\)'
            content = re.sub(link_pattern, r'\1', content)

        if content != original_content:
            logger.info(f"Removed 404 links from {filepath}")
            Path(filepath).write_text(content, encoding='utf-8')
            return True
        return False

    except Exception as e:
        logger.error(f"Error processing {filepath}: {e}")
        return False

def main():
    """Process all markdown files in content directory."""
    content_dir = Path("content")
    modified_files = 0

    for md_file in content_dir.glob("**/*.md"):
        if remove_404_links(md_file):
            modified_files += 1

    logger.info(f"Processed all files. Modified {modified_files} files.")

if __name__ == "__main__":
    main()
