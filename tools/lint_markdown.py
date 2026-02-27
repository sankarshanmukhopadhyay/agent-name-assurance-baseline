#!/usr/bin/env python3
"""
Lightweight markdown lint for this repo.

Intent: catch common quality regressions without pulling heavy tooling.
Checks:
- no tab characters
- heading lines must have a space after the leading hash run (e.g., "# Title", "## Title")
- no trailing whitespace (except the canonical two-space hard line break)
"""

from __future__ import annotations
from pathlib import Path
import sys
import re

ROOT = Path(__file__).resolve().parents[1]

def iter_md_files() -> list[Path]:
    return [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]

def has_illegal_trailing_ws(line: str) -> bool:
    # allow markdown hard line break "  " (two spaces) at EOL
    if line.endswith("  ") and not line.endswith("   "):
        return False
    return line.rstrip(" ") != line

def heading_missing_space(line: str) -> bool:
    if not line.startswith("#"):
        return False
    m = re.match(r"^(#+)", line)
    if not m:
        return False
    n = len(m.group(1))
    if n >= len(line):
        return True
    return line[n] != " "

def main() -> int:
    bad = 0
    for p in iter_md_files():
        lines = p.read_text(encoding="utf-8").splitlines()
        for i, line in enumerate(lines, start=1):
            if "\t" in line:
                print(f"{p}:{i}: TAB character found", file=sys.stderr)
                bad += 1
            if has_illegal_trailing_ws(line):
                print(f"{p}:{i}: trailing whitespace", file=sys.stderr)
                bad += 1
            if heading_missing_space(line):
                print(f"{p}:{i}: heading missing space after #", file=sys.stderr)
                bad += 1

    if bad:
        print(f"ERROR: markdown lint failed with {bad} issue(s).", file=sys.stderr)
        return 2
    print("OK: markdown lint passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
