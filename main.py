#!/usr/bin/env python3
"""Write a single everyday-wonder sentence to the entry file.

The program prepares the output folder, then stores one fixed
sentence about a mirror and a face that is a day older each
morning. It uses only the standard library, takes no arguments,
and always produces exactly the same bytes on every run.
"""

from pathlib import Path

# The approved entry: one sentence, 91 characters, no trailing newline.
ENTRY_TEXT = (
    "Every morning the mirror shows a face one day older, "
    "and it has never once repeated itself."
)
OUTPUT_PATH = Path("/output/entry.txt")


def write_entry() -> None:
    """Create the output directory if needed and write the entry."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
