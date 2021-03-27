#!/usr/bin/env python3

"""Read csv input and output a crosstab csv.

Input is read on stdin and the result is written to stdout.

There is no options to change the csv-dialect currently but that should be easy
to change.

First column in the input will be the label for the rows.
Second column in the input will be the label for the columns.
"""

import csv
import sys
from collections import defaultdict
from itertools import chain


def main():
    reader = csv.reader(sys.stdin)
    data = defaultdict(dict)

    for y, x, value in reader:
        data[y][x] = value

    columns = [""]  # First column doesn't have a title
    columns.extend(sorted(set(chain(*(d.keys() for d in data.values())))))

    writer = csv.DictWriter(sys.stdout, fieldnames=columns)
    writer.writeheader()

    for row_key in sorted(data.keys()):
        row = {"": row_key}  # First column
        row.update(data[row_key])

        writer.writerow(row)


if __name__ == "__main__":
    main()
