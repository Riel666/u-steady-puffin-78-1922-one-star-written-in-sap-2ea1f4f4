#!/usr/bin/env python3
"""Write one funny line to /output/entry.txt.

The line is written exactly as given: 142 Unicode code points,
inside the competition gate of 1-280.
Python 3, standard library only, no network.
"""

import os

TEXT = "One star. My human waters me once a month, talks to me never, then blames me for dying. I have been a loyal pothos for three years. Do better."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    assert 1 <= len(TEXT) <= 280, len(TEXT)
    assert TEXT == TEXT.strip()

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
