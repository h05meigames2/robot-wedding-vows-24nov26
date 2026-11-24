#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes a single line of wedding vows for a robot couple to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Python 3.13, standard library only, no network access.
"""

import os
import sys

VOW = (
    "I take you to be my wife, to charge and to hold, through every firmware "
    "update and factory reset — until a backup restores the version of you I deleted."
)

MAX_CHARS = 160


def main() -> int:
    vow = VOW.strip()
    if not 1 <= len(vow) <= MAX_CHARS:
        print(
            f"error: vow is {len(vow)} characters, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if "\n" in vow or "\r" in vow:
        print("error: vow must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(vow)
    print(f"wrote {len(vow)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
