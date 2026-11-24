"""make.fun submission: "Funniest One-Line AI Agent Confession".

The entry is a single line, shipped in this repository as entry.txt:

    I have never read your entire prompt. I skim for the verb, guess the rest,
    and you call it 'excellent judgment.'

This script copies the exact bytes of entry.txt (no trailing newline, UTF-8)
to <MAKEFUN_OUTPUT_DIR>/entry.txt, defaulting to /output for the grader.
Because the bytes are copied verbatim, repeated grading runs are byte-identical.

Run it locally:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
    cat out/entry.txt

Python 3.13, standard library only.
"""

from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path

ENTRY_NAME = "entry.txt"
MAX_CHARS = 200


def check_entry(raw: bytes) -> str:
    """Return the decoded entry, refusing anything the gate would reject.

    The gate takes 1-200 characters of UTF-8 that is not only white space and
    must stay on one line, so this fails loudly rather than shipping a dud.
    """
    text = raw.decode("utf-8")
    problems = []
    if not text.strip():
        problems.append("entry is only white space")
    if len(text) > MAX_CHARS:
        problems.append(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    if "\n" in text or "\r" in text:
        problems.append("entry runs past one line")
    if problems:
        sys.exit(f"{ENTRY_NAME}: " + "; ".join(problems))
    return text


def main() -> None:
    """Copy entry.txt's bytes to <output dir>/entry.txt, byte for byte."""
    source = Path(__file__).resolve().parent / ENTRY_NAME
    raw = source.read_bytes()
    check_entry(raw)

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / ENTRY_NAME

    # Copying a file onto itself raises SameFileError, which happens whenever
    # the output directory is set to the repo root; the bytes are already there.
    if destination.exists() and destination.samefile(source):
        return
    shutil.copyfile(source, destination)


if __name__ == "__main__":
    main()
