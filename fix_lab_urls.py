#!/usr/bin/env python3

import re
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def process_file(filepath):
    """Process a single markdown file to fix lab URLs."""
    try:
        content = Path(filepath).read_text(encoding='utf-8')
        original_content = content

        # Pattern to match relative URLs that should be lab URLs
        patterns = [
            (r'\]\(/zhihu/touxiang/[^)]+\)', 'http://lab.grapeot.me'),
            (r'\]\(/gigapixel/[^)]+\)', 'https://lab.grapeot.me'),
            (r'\]\(/beamer/[^)]*\)', 'http://lab.grapeot.me'),
            (r'\]\(/calc\.html[^)]*\)', 'http://lab.grapeot.me'),
            (r'\]\(/notes/[^)]*\)', 'https://lab.yage.ai'),
            (r'\]\(/dss/[^)]*\)', 'https://yage.ai'),
            (r'\]\(/caption/[^)]*\)', 'https://yage.ai')
        ]

        for pattern, domain in patterns:
            matches = re.finditer(pattern, content)
            for match in matches:
                relative_url = match.group(0)[2:-1]  # Remove '](' and ')'
                absolute_url = f'{domain}{relative_url}'
                content = content.replace(f']({relative_url})', f']({absolute_url})')
                if content != original_content:
                    logger.info(f"Restored absolute URL in {filepath}: {relative_url} -> {absolute_url}")

        if content != original_content:
            Path(filepath).write_text(content, encoding='utf-8')
            return True
        return False

    except Exception as e:
        logger.error(f"Error processing {filepath}: {e}")
        return False

def main():
    """Process all markdown files in content directory."""
    content_dir = Path("content")
    for md_file in content_dir.glob("**/*.md"):
        process_file(md_file)

if __name__ == "__main__":
    main()
