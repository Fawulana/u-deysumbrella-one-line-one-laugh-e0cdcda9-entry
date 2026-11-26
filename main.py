#!/usr/bin/env python3
"""One Line, One Laugh — writes one original one-liner to /output/entry.txt."""

import os
from pathlib import Path

LINE = (
    "My umbrella survived the storm just fine; it was me, clinging "
    "underneath it like a wet koala, who filed the damage report."
)


def main() -> None:
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # write_text adds nothing extra: the file is exactly LINE, no trailing newline.
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
