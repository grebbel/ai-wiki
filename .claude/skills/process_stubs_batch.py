#!/usr/bin/env python3
"""process_stubs_batch.py — Generate wiki source page templates from Zotero-acquired raw stubs.

Usage:
    python process_stubs_batch.py --collection NBRA [--mode=template|dry-run]
    python process_stubs_batch.py --new-stubs raw/papers/*.md --output-dir wiki/sources/

Features:
    - Identifies raw stubs not yet processed into wiki/sources/
    - Extracts frontmatter + content from each stub
    - Generates wiki source page templates with:
      - Populated frontmatter (title, authors, date, doi, etc.)
      - TL;DR placeholder
      - Key findings placeholder
      - Implementation implications placeholder
      - Auto-suggested related concepts (keyword matching)
    - Outputs summary of generated files
    - Supports dry-run for preview
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")


# Keyword-to-concept mappings for auto-suggestion
KEYWORD_CONCEPT_MAP = {
    "pathogen": "pathogen-inventory-systems",
    "inventory": "pathogen-inventory-systems",
    "biosecurity": "biosecurity-capacity-building",
    "capacity": "biosecurity-capacity-building",
    "training": "biosecurity-capacity-building",
    "one health": "one-health-operationalization",
    "operational": "one-health-operationalization",
    "cross-sector": "one-health-operationalization",
    "coordination": "one-health-operationalization",
}

# Entity keywords for auto-linking
KEYWORD_ENTITY_MAP = {
    "rivm": "rivm",
    "bwc": "biological-weapons-convention",
    "weapons convention": "biological-weapons-convention",
    "who": "who",
    "world health organization": "who",
}


def read_raw_stub(filepath: Path) -> dict:
    """Extract YAML frontmatter and content from raw stub."""
    content = filepath.read_text(encoding="utf-8")
    
    # Parse YAML frontmatter
    if not content.startswith("---"):
        return {}
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}
    
    try:
        frontmatter = yaml.safe_load(parts[1])
        text_body = parts[2].strip()
        return {"frontmatter": frontmatter, "body": text_body}
    except Exception as e:
        print(f"Warning: Failed to parse {filepath.name}: {e}", file=sys.stderr)
        return {}


def get_already_processed(sources_dir: Path) -> set[str]:
    """Get set of raw filenames already processed into wiki sources."""
    processed = set()
    for source_file in sources_dir.glob("*.md"):
        content = source_file.read_text(encoding="utf-8")
        # Look for raw: reference in frontmatter
        match = re.search(r'raw:\s*"?\.\.\/\.\.\/raw\/\w+\/([^"]+\.md)', content)
        if match:
            processed.add(match.group(1))
    return processed


def suggest_concepts(title: str, abstract: str) -> list[str]:
    """Suggest related concepts based on keyword matching."""
    text = (title + " " + abstract).lower()
    concepts = set()
    
    for keyword, concept in KEYWORD_CONCEPT_MAP.items():
        if keyword.lower() in text:
            concepts.add(concept)
    
    return sorted(list(concepts))


def suggest_entities(title: str, abstract: str) -> list[str]:
    """Suggest related entities based on keyword matching."""
    text = (title + " " + abstract).lower()
    entities = set()
    
    for keyword, entity in KEYWORD_ENTITY_MAP.items():
        if keyword.lower() in text:
            entities.add(entity)
    
    return sorted(list(entities))


def generate_source_page(raw_file: Path, stub_data: dict) -> Optional[str]:
    """Generate wiki source page content from stub data."""
    fm = stub_data.get("frontmatter", {})
    body = stub_data.get("body", "")
    
    if not fm:
        return None
    
    title = fm.get("title", "Untitled")
    authors = fm.get("authors", [])
    date_pub = fm.get("date_published", "")
    doi = fm.get("doi", "")
    url = fm.get("url", "")
    abstract = fm.get("abstract", "") or body
    item_type = fm.get("item_type", "article")
    
    # Determine source kind
    kind_map = {
        "journalArticle": "paper",
        "conferencePaper": "paper",
        "book": "book",
        "report": "report",
        "webpage": "article",
        "blogPost": "article",
    }
    kind = kind_map.get(item_type, "article")
    
    # Format authors
    author_yaml = ""
    if authors:
        author_yaml = "  - " + "\n  - ".join(authors)
    
    # Suggest concepts and entities
    concepts = suggest_concepts(title, abstract)
    entities = suggest_entities(title, abstract)
    
    # Format frontmatter
    frontmatter = f"""---
type: source
kind: {kind}
title: "{title}"
author:
{author_yaml}
date_published: {date_pub}
url: "{url}"
doi: "{doi}"
length: "~N pages (full-text synthesis from PDF)"
raw: "../../raw/{raw_file.parent.name}/{raw_file.name}"
zotero_item_key: {fm.get('zotero_item_key', '')}
zotero_collection: {fm.get('zotero_collection', 'NBRA')}
fulltext_source: pdf
tags:
  - TO-BE-ASSIGNED
---"""
    
    # Build related links
    concept_links = "\n- ".join(f"[[concepts/{c}|{c}]]" for c in concepts) if concepts else "(suggest concepts)"
    entity_links = "\n- ".join(f"[[entities/{e}|{e}]]" for e in entities) if entities else "(suggest entities)"
    
    body_content = f"""# {title}

## TL;DR

_[One to two sentence summary of the key contribution]_

## What was actually ingested

- Source channel: Zotero acquire from collection {fm.get('zotero_collection', 'NBRA')}.
- Raw type: {item_type} routed to raw/{raw_file.parent.name}/.
- Full-text quality: pdf (direct PDF conversion via fulltext extraction).

## Key findings

- _[Finding 1]_
- _[Finding 2]_
- _[Finding 3]_

## Implementation implications

- _[Implication 1]_
- _[Implication 2]_

## Related concepts

- {concept_links}

## Related entities

- {entity_links}
"""
    
    return frontmatter + "\n\n" + body_content


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--collection", type=str, default="NBRA", help="Zotero collection name")
    parser.add_argument("--mode", choices=["template", "dry-run"], default="template",
                        help="Mode: template (generate), dry-run (preview only)")
    parser.add_argument("--output-dir", type=Path, default=None,
                        help="Override output directory (default: wiki/sources/)")
    parser.add_argument("--new-stubs", type=str, default=None,
                        help="Explicit list of stub files (glob pattern or space-separated paths)")
    
    args = parser.parse_args()
    
    # Find repo root
    repo_root = Path.cwd()
    for parent in Path.cwd().parents:
        if (parent / "ghs-wiki").exists() and (parent / "ghs-wiki" / "wiki").exists():
            repo_root = parent / "ghs-wiki"
            break
    
    raw_dir = repo_root / "raw"
    sources_dir = args.output_dir or (repo_root / "wiki" / "sources")
    
    if not raw_dir.exists():
        print(f"Error: raw directory not found at {raw_dir}", file=sys.stderr)
        return 1
    
    # Find new stubs
    already_processed = get_already_processed(sources_dir)
    
    if args.new_stubs:
        # Explicit stub specification
        stub_files = []
        for pattern in args.new_stubs.split():
            stub_files.extend(repo_root.glob(pattern))
    else:
        # Auto-detect new stubs by checking raw/ directory
        stub_files = list(raw_dir.rglob("*.md"))
        stub_files = [f for f in stub_files if f.name not in already_processed]
    
    if not stub_files:
        print("No new stubs found.")
        return 0
    
    print(f"Found {len(stub_files)} new stub(s) to process:")
    generated = []
    
    for stub_file in sorted(stub_files):
        stub_data = read_raw_stub(stub_file)
        if not stub_data:
            print(f"  ⊘ {stub_file.name} (failed to parse)")
            continue
        
        # Determine output filename (use date + slugified title)
        fm = stub_data["frontmatter"]
        coll = str(fm.get("zotero_collection", "")).strip().lower()
        if args.collection and coll and coll != args.collection.strip().lower():
            continue

        raw_date = str(fm.get("date_published", "")).strip()
        date_str = raw_date.split()[0] if raw_date else "2026-01-01"
        title_slug = re.sub(r'[^\w\s-]', '', fm.get("title", "untitled").lower())
        title_slug = re.sub(r'[\s_-]+', '-', title_slug).strip("-")[:60]
        output_name = f"{date_str}-{title_slug}.md"
        output_path = sources_dir / output_name
        
        content = generate_source_page(stub_file, stub_data)
        if not content:
            print(f"  ⊘ {stub_file.name} (could not generate content)")
            continue
        
        if args.mode == "dry-run":
            print(f"  ✓ {output_name} (preview)")
            print(f"    Title: {fm.get('title', 'Untitled')}")
            print(f"    Authors: {', '.join(fm.get('authors', []))}")
            print()
        else:
            # Write the file
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(content, encoding="utf-8")
            print(f"  ✓ {output_name}")
            generated.append({
                "file": output_name,
                "title": fm.get("title", "Untitled"),
                "date": date_str,
            })
    
    if args.mode != "dry-run" and generated:
        print(f"\n✅ Generated {len(generated)} wiki source page(s) in {sources_dir}/")
        print("\n📝 Next steps:")
        print("  1. Review generated files in wiki/sources/")
        print("  2. Fill in TL;DR, Key findings, and Implementation implications")
        print("  3. Verify and refine related concepts/entities")
        print("  4. Run: npm run build && git status")
        print("  5. Commit changes")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
