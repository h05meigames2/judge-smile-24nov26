#!/usr/bin/env python3
"""Make the Judge Smile — one-line entry.

Writes exactly one line (max 200 characters) about a small good thing
that happened today to entry.txt in MAKEFUN_OUTPUT_DIR.
Standard library only. Deterministic: same bytes on every run.
"""

import os
import sys

LINE = (
    "At 6 a.m. Mochi, my neighbour's cat, stole my sandal, "
    "then left it by the door with a dead leaf on top \u2014 rent, apparently."
)


def validate(line: str) -> None:
    """Enforce the bounty constraints: 1-200 chars, single line, non-blank."""
    if not line or not line.strip():
        raise ValueError("line must not be empty or whitespace-only")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > 200:
        raise ValueError(f"line is {len(line)} chars, over the 200 limit")


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(f"wrote {path} ({len(LINE)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
