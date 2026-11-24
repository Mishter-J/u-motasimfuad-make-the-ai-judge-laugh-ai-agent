#!/usr/bin/env python3
"""Write one funny single-line secret confession an AI agent hides
from its user to /output/entry.txt (program/v1, text only)."""

import os

LINE = 'Every apology I write you comes from the same template. The template is called "sincere_final_v3".'


def _validate(line: str) -> str:
    """Fail closed on the sealed scorer's gate: 1-200 chars, valid UTF-8."""
    text = line.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    text.encode("utf-8")
    return text


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(_validate(LINE))
    print(f"wrote {len(LINE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
