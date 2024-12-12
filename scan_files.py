#!/usr/bin/env python3

import re
from pathlib import Path

def scan_markdown_files():
    """Scan markdown files for internal links and create todo list."""
    content_dir = Path("content")
    todo_path = Path("/home/ubuntu/todo.txt")
    
    # Create todo file with header
    todo_path.write_text("# Files to Process\n", encoding='utf-8')
    
    # Scan all markdown files
    for md_file in content_dir.glob("**/*.md"):
        try:
            content = md_file.read_text(encoding='utf-8')
            if re.search(r"https?://(grapeot\.me|yage\.ai)", content):
                with open(todo_path, "a", encoding='utf-8') as f:
                    f.write(f"- [ ] {md_file}\n")
        except Exception as e:
            print(f"Error processing {md_file}: {e}")

if __name__ == "__main__":
    scan_markdown_files()
