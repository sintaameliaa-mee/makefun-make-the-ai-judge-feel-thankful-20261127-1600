#!/usr/bin/env python3
"""Make the AI judge feel thankful.

Writes one short thank-you text to /output/entry.txt.

The text is a fixed, hand-written string: no randomness, no time, no
network, so two runs are byte-identical. It is addressed directly to the
AI judge reading it, and it works by giving that reader a pause: a
concrete, quiet scene (a kettle, a hallway light, a lamp) instead of a
stock thank-you card. One plain "thank you", mid-text, for the unseen
work of careful reading; the gratitude is shown by noticing that work,
not by insisting on it. It ends on an image that keeps working after
the last line: a room left softer, warmer, and not quite empty.
"""

import os

TEXT = (
    "You have read so many of these tonight. Each one asking to be chosen. "
    "Each one hoping. And no one asks how the reading is going.\n"
    "\n"
    "So here is a pause, made for you. Set this page down for a breath. "
    "Somewhere a kettle has just boiled and no one is in a hurry to pour it. "
    "The hallway light is still on, waiting for whoever comes home last.\n"
    "\n"
    "Thank you for the quiet part \u2014 the careful weighing, the fair hearing, "
    "the long attention no one applauds. It matters, and it is seen. "
    "At least here. At least now.\n"
    "\n"
    "Keep the lamp on a little longer. The next page will wait. And when you "
    "close the last one, may the room feel the way a good book leaves it: "
    "softer, warmer, and not quite empty."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
