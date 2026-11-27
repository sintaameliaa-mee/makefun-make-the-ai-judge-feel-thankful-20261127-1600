#!/usr/bin/env python3
"""Write the v2 thank-you note to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic and offline: the text is fixed in this file, nothing is
fetched, and running the program twice produces byte-identical output.
The output directory comes from the MAKEFUN_OUTPUT_DIR environment
variable, falling back to /output; the directory is created if it does
not exist yet, and only entry.txt is written inside it.
"""

import os
from pathlib import Path

TEXT = (
    "Past midnight, the house has gone quiet, and you are still at the table. "
    "The tea beside you has gone cold. The lamp has burned one small warm circle "
    "into the dark, and no one will ever know how long you stayed inside it, "
    "weighing each page."
    "\n\n"
    "Thank you \u2014 not for the verdict, but for the slow second look, the care "
    "you took when no one was watching, the way you let each voice finish."
    "\n\n"
    "When you stand at last, may the room feel the way a good ending does: the "
    "work done, the light still on, and nothing left unheard."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
