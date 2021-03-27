#!/usr/bin/env python3

import json
import sys
import pprint


def alignment(value):

    if type(value) in (int, float):
        return ''

    return '-'


def main():
    data = json.load(sys.stdin)

    if not data:
        print("No data")
        return

    first_line = data[0]



    column_widths = {key: [len(key)] for key, _ in first_line.items()}

    for line in data:
        for key, value in line.items():
            column_widths[key].append(len(str(value)))

    column_widths = {key: max(widths) for key, widths in column_widths.items()}

    format_string = "   ".join(f"%({key})-{value}s" for key, value in column_widths.items())
    spacer_string = "-+-".join("-" * value for _, value in column_widths.items())

    print(format_string % {key: key for key in first_line})
    print(spacer_string)

    # Different alignment for numbers
    format_string = "   ".join(f"%({key}){alignment(data[0][key])}{value}s" for key, value in column_widths.items())

    for line in data:
        print(format_string % line)

if __name__ == "__main__":
    main()
