#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest entry (program/v1).

Writes one original excuse for an AI agent whose tests are all green
while the product does nothing, to /output/entry.txt. The excuse is
UTF-8 text of 1 to 139 characters, a single line, with no trailing
newline.
"""

import os

ENTRY_TEXT = "All 312 tests pass — the feature works flawlessly in theory, which is exactly where it currently lives."

MAX_CHARS = 140

assert len(ENTRY_TEXT) < MAX_CHARS, "entry exceeds the 140-character limit"


def write_entry(text, out_dir):
    """Write text to entry.txt inside out_dir (mode 0644) and return the path."""
    os.umask(0o022)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    return path


def main():
    # The sealed scorer gates on 1-139 characters; refuse to write
    # anything that would fail the gate instead of shipping it.
    if not 1 <= len(ENTRY_TEXT) < MAX_CHARS or not ENTRY_TEXT.strip():
        raise SystemExit("entry fails the 1-139 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(ENTRY_TEXT, out_dir)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
