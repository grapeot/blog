#!/usr/bin/env python3
"""
Split articles without Summary into batches for parallel processing.
"""
from pathlib import Path

CONTENT_DIR = Path(__file__).parent.parent / "content"
BATCH_SIZE = 45  # ~354 articles / 8 agents

def get_articles_without_summary():
    """Get list of articles without Summary field."""
    articles = []
    for f in CONTENT_DIR.glob("*.md"):
        content = f.read_text(encoding="utf-8")
        if "Summary:" not in content:
            articles.append(str(f))
    return sorted(articles)

def main():
    articles = get_articles_without_summary()
    print(f"Found {len(articles)} articles without Summary")
    
    # Split into 8 batches
    for i in range(8):
        start = i * BATCH_SIZE
        end = min((i + 1) * BATCH_SIZE, len(articles))
        batch = articles[start:end]
        
        batch_file = Path(__file__).parent / f"batch_{i+1}.txt"
        batch_file.write_text("\n".join(batch), encoding="utf-8")
        print(f"Batch {i+1}: {len(batch)} articles -> {batch_file}")

if __name__ == "__main__":
    main()
