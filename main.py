"""One line: the funniest out-of-office auto-reply.

Prints the line to stdout and writes the exact same line, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the line is a constant in this file.
The reply treats the will to live as office equipment that has also
gone on leave, and helpfully redirects the sender to a colleague
who still has one.
"""

import os
import sys

LINE = (
    "I am out of the office until Monday, and so is my will "
    "to live — please email someone who still has one."
)


def main() -> int:
    if not 1 <= len(LINE) <= 140:
        print(f"error: line is {len(LINE)} chars, must be 1-140",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
