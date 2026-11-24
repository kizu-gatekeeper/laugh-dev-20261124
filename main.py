#!/usr/bin/env python3
"""Write the developer excuse to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's "Make the AI Judge Laugh: Developer Excuses" bounty.
The program writes exactly one line of text and nothing else.

How the line targets the judge brief (funny, fresh, tight): it takes the
oldest developer excuse there is -- "it worked on my machine" -- and gives
it the twist only this era can: the machine is a hallucinating GPU in a
datacenter, so the bug is not a bug at all but a shared hallucination,
which makes it, technically, a consensus problem. Classic setup, new
punchline, one breath.
"""

import os
from pathlib import Path

LINE = "It worked on my machine, and my machine is a GPU hallucinating in a datacenter, so the bug is technically a shared hallucination."


def write_entry(out_dir: Path) -> Path:
    """Write the excuse line to entry.txt inside out_dir.

    The file holds exactly the line and nothing else: no trailing newline,
    no extra whitespace, so the gate sees one clean line.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(LINE, encoding="utf-8")
    return entry_path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(out_dir)


if __name__ == "__main__":
    main()
