#!/usr/bin/env python3

import fileinput
from itertools import zip_longest
from textwrap import wrap
from typing import Sequence


def main() -> None:
    # List comprehension to actually have a copy in memory
    # But tuples to save memory if we have a lot of lines
    data = [tuple(line.strip().split("\t")) for line in fileinput.input()]

    # Fine to use generator/iterator here since this is only used
    # to determine the longest value in each column
    lengths = ((len(s) for s in v) for v in data)

    # Transpose recipe taken from
    # https://stackoverflow.com/questions/6473679/transpose-list-of-lists
    column_widths = map(max, zip_longest(*lengths))

    format_string = "  ".join(f"%-{ w }s" for w in column_widths)

    for row in data:
        print(format_string % row)


if __name__ == "__main__":
    main()
