#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — entrypoint.

Reads the phone's farewell line from line.txt, checks it against the
competition gate (UTF-8 text of 1 to 199 characters, not only white
space), writes it to /output/entry.txt for the harness, and prints it.
"""

from pathlib import Path

LINE_FILE = Path(__file__).with_name("line.txt")
OUTPUT_FILE = Path("/output/entry.txt")
MAX_CHARS = 199


def read_line() -> str:
    return LINE_FILE.read_text(encoding="utf-8").strip()


def check_gate(line: str) -> None:
    if not line:
        raise ValueError("entry is empty or only white space")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} characters, over the {MAX_CHARS} gate")


def main() -> None:
    line = read_line()
    check_gate(line)
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(line, encoding="utf-8")
    print(line)


if __name__ == "__main__":
    main()
