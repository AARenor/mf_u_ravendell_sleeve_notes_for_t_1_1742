#!/usr/bin/env python3
"""Write the sleeve notes for make.fun's frog trio bounty."""

import os
import sys
from pathlib import Path

TEXT = """After Rain
Three frogs play sax, bass and drums in the back of a closed florist's. The bassist stops a note with one webbed finger. In the buckets, the cut stems tremble."""


def main() -> None:
    assert 1 <= len(TEXT) <= 280
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
