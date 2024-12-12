#!/usr/bin/env python3

import markdown
import re
import os
from pathlib import Path
import sys
from urllib.parse import urlparse, urljoin
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configure change logging
CHANGES_LOG = os.path.expanduser("~/link_changes.txt")

def setup_logging():
    """Ensure the changes log file exists and is writable."""
    try:
        Path(CHANGES_LOG).touch(exist_ok=True)
        return True
    except Exception as e:
        logger.error(f"Failed to setup logging: {e}")
        return False

def extract_links(content):
    """Extract markdown links using regex."""
    return re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content)

def is_internal_link(url):
    """Check if URL points to grapeot.me or yage.ai."""
    return any(domain in url.lower() for domain in ['grapeot.me', 'yage.ai'])

def verify_output_file(path):
    """Check if the path exists in the output directory."""
    clean_path = path.lstrip('/')
    output_path = os.path.join("output", clean_path)
    exists = os.path.exists(output_path)
    if not exists:
        # Try with .html extension if not found
        if not path.endswith('.html'):
            output_path = os.path.join("output", clean_path + '.html')
            exists = os.path.exists(output_path)
    return exists

def convert_to_relative_url(url):
    """Convert absolute URL to relative path."""
    parsed = urlparse(url)
    return parsed.path

def log_changes(filepath, changes):
    """Log changes made to the file."""
    try:
        with open(CHANGES_LOG, "a", encoding='utf-8') as f:
            f.write(f"\n=== {filepath} ===\n")
            f.write("\n".join(changes) + "\n")
    except Exception as e:
        logger.error(f"Failed to log changes: {e}")

def process_file(filepath):
    """Process a single markdown file."""
    try:
        content = Path(filepath).read_text(encoding='utf-8')
        original_content = content
        links = extract_links(content)
        changes = []

        for text, url in links:
            if is_internal_link(url):
                relative_path = convert_to_relative_url(url)
                if verify_output_file(relative_path):
                    new_url = relative_path
                    content = content.replace(f"]({url})", f"]({new_url})")
                    changes.append(f"Converted {url} to {new_url}")
                    logger.info(f"Converted link in {filepath}: {url} -> {new_url}")
                else:
                    logger.warning(f"Link not found in output/: {url} in {filepath}")
                    # Keep the link as is for now, will be verified against live site later

        if changes:
            Path(filepath).write_text(content, encoding='utf-8')
            log_changes(filepath, changes)
            return True

        return False

    except Exception as e:
        logger.error(f"Error processing {filepath}: {e}")
        return False

def update_todo(filepath):
    """Mark a file as processed in todo.txt."""
    todo_path = os.path.expanduser("~/todo.txt")
    try:
        with open(todo_path, "r", encoding='utf-8') as f:
            lines = f.readlines()

        with open(todo_path, "w", encoding='utf-8') as f:
            for line in lines:
                if filepath in line and "[ ]" in line:
                    f.write(line.replace("[ ]", "[x]"))
                else:
                    f.write(line)
    except Exception as e:
        logger.error(f"Failed to update todo.txt: {e}")

def get_unprocessed_files():
    """Get list of unprocessed files from todo.txt."""
    todo_path = os.path.expanduser("~/todo.txt")
    unprocessed = []
    try:
        with open(todo_path, "r", encoding='utf-8') as f:
            for line in f:
                if "- [ ]" in line:
                    filepath = line.strip().replace("- [ ] ", "")
                    unprocessed.append(filepath)
    except Exception as e:
        logger.error(f"Failed to read todo.txt: {e}")
    return unprocessed

def main():
    """Main function to process all unprocessed files."""
    if not setup_logging():
        sys.exit(1)

    files = get_unprocessed_files()
    if not files:
        logger.info("No files to process")
        sys.exit(0)

    processed_count = 0
    for filepath in files:
        if not os.path.exists(filepath):
            logger.error(f"File not found: {filepath}")
            continue

        logger.info(f"Processing {filepath}...")
        if process_file(filepath):
            update_todo(filepath)
            processed_count += 1

    logger.info(f"Processed {processed_count} files")
    sys.exit(0 if processed_count > 0 else 1)

if __name__ == "__main__":
    main()
