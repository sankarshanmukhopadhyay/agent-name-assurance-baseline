#!/usr/bin/env python3
"""
Simple markdown link checker:
- Verifies that relative links to files/anchors resolve.
- Does not fetch remote URLs.

Rules:
- Links like `docs/foo.md` or `../bar.md` must exist.
- Anchors are checked for presence of a matching heading id (GitHub-style slug approximation).
"""

from __future__ import annotations
from pathlib import Path
import re
import sys
import urllib.parse

ROOT = Path(__file__).resolve().parents[1]

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

def gh_slugify(heading: str) -> str:
    h = heading.strip().lower()
    # remove punctuation except hyphens/spaces
    h = re.sub(r"[^\w\s-]", "", h)
    h = re.sub(r"\s+", "-", h).strip("-")
    return h

def extract_anchors(md_text: str) -> set[str]:
    anchors = set()
    for line in md_text.splitlines():
        m = re.match(r"^(#+)\s+(.*)$", line)
        if m:
            anchors.add(gh_slugify(m.group(2)))
    return anchors

def main() -> int:
    bad = 0
    md_files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
    anchor_cache = {}
    for p in md_files:
        text = p.read_text(encoding="utf-8")
        for raw in LINK_RE.findall(text):
            link = raw.strip()
            if link.startswith("#"):
                # same-file anchor
                anchors = anchor_cache.setdefault(p, extract_anchors(text))
                anchor = link[1:]
                if anchor and anchor not in anchors:
                    print(f"{p}: broken anchor link #{anchor}", file=sys.stderr)
                    bad += 1
                continue

            parsed = urllib.parse.urlparse(link)
            if parsed.scheme in ("http", "https", "mailto"):
                continue  # don't check remote
            # strip query/fragment
            path = parsed.path
            frag = parsed.fragment
            # ignore empty
            if not path:
                continue
            target = (p.parent / path).resolve()
            if not str(target).startswith(str(ROOT.resolve())):
                # outside repo; ignore
                continue
            if not target.exists():
                print(f"{p}: broken relative link -> {path}", file=sys.stderr)
                bad += 1
                continue
            if frag:
                # check anchor in target markdown
                if target.suffix.lower() == ".md":
                    ttext = target.read_text(encoding="utf-8")
                    anchors = anchor_cache.setdefault(target, extract_anchors(ttext))
                    if frag not in anchors:
                        print(f"{p}: broken anchor {path}#{frag}", file=sys.stderr)
                        bad += 1

    if bad:
        print(f"ERROR: link check failed with {bad} issue(s).", file=sys.stderr)
        return 2
    print("OK: link check passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
