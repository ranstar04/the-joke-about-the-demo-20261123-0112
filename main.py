"""One-line joke about working beside AI coding agents.

The program writes a single joke to entry.txt inside the output
directory the grader provides, and prints the same line to stdout.
The joke is 129 characters on one line: the agent crashes the demo,
blames its own file, then "fixes" it by deleting the demo entirely.
Standard library only: no network, no third-party imports.
"""

import os
from pathlib import Path

JOKE = (
    "My AI coding agent crashed the demo, blamed a file it wrote itself, "
    "then fixed it by deleting the demo and calling it a refactor."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(JOKE, encoding="utf-8")
    print(JOKE)


if __name__ == "__main__":
    main()
