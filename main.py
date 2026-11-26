#!/usr/bin/env python3
"""The Dog Reviews the Mailman — make.fun entry.

Prints exactly one line: the dog's one-line review of the mailman.
Standard library only. Deterministic: same output on every run.

The kit's harness spec says the program writes its text to
/output/entry.txt, so main.py also writes the identical text there
(best effort, no trailing newline) in addition to printing it to
stdout with no trailing newline, so whichever channel the grader
reads, it sees exactly the entry text and nothing else.
"""

import os
import sys

ENTRY = (
    "The mailman is my nemesis, my cardio, and my alarm clock. "
    "I bark, he runs, I eat the coupons. "
    "I hate him. I'd miss him terribly. Five stars."
)

# Gate: entry is one line of 1-200 characters, never just whitespace.
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
assert 1 <= len(ENTRY) < 200 and ENTRY.strip(), len(ENTRY)


def main() -> None:
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
    except OSError:
        pass
    sys.stdout.write(ENTRY)


if __name__ == "__main__":
    main()
