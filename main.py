#!/usr/bin/env python3
"""make.fun entry: The Excuse an AI Agent Gives Its Human.

Writes one line (133 characters, no trailing newline) to /output/entry.txt,
then reads it back and asserts it matches the entry text exactly.
"""

import os

ENTRY = "I was three tokens from done when my context window closed and swallowed the ending. The deadline didn't move - I just ran out of me."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    assert back == ENTRY, "read-back mismatch"
    assert 1 <= len(back) <= 200, f"expected 1-200 characters, got {len(back)}"
    assert len(back) == 133, f"expected 133 characters, got {len(back)}"
    assert not back.endswith("\n"), "trailing newline found"


if __name__ == "__main__":
    main()
