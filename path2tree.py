#!/usr/bin/env python3
""" Convert a list of paths to a tree. """

import argparse
import os
import sys
from collections import defaultdict
from itertools import chain
from itertools import repeat
from typing import Dict


def render_directory(string, options):
    separator = options.separator if options.render_separator else ""
    if options.color:
        return "\033[0;34m" + string + "\033[0m" + separator

    return string + separator


def render_file(string, options):  # pylint: disable=unused-argument
    return string


def tree_factory():
    return defaultdict(tree_factory)


def tree_print(tree: Dict, parent_render=None, options=None):
    keys = sorted(tree.keys())

    if parent_render is None:
        indicators = repeat("", len(keys))
        parent_indicators = repeat("", len(keys))
    else:
        indicators = chain(repeat("├── ", len(keys) - 1), ["└── "])
        parent_indicators = chain(repeat("│   ", len(keys) - 1), ["    "])

    parent_render = parent_render or ""

    tree_data = zip(parent_indicators, indicators, keys)
    for parent_indicator, indicator, key in tree_data:

        # Descend the tree until there are multiple branches (or none)
        # Evaluating the len() will be done at least one time, even if options.collapse is False.
        # That way we will automatically descend the tree if there are only one child
        current_node = tree
        collapseable_keys = []
        while 1 == len(values := current_node[key]):
            if not options.collapse:
                # We don't want to descend the tree unless we should collapse the levels
                break

            collapseable_keys.append(key)
            current_node = values
            key = next(iter(current_node.keys()))  # We checked before that there was a single entry

        renderer = render_directory if values else render_file

        rendered_entry = renderer(options.separator.join(collapseable_keys + [key]), options)
        print(parent_render + indicator + rendered_entry)

        tree_print(values, parent_render + parent_indicator,
                   options)


def node(tree, *path):
    current_node = tree

    for fragment in path:
        current_node = current_node[fragment]

    return current_node


def parse_args():

    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('-s', '--separator',
                        dest="separator", action="store", type=str,
                        default=os.path.sep,
                        help="Separator used in paths")

    output = parser.add_argument_group("output")

    output.add_argument('--collapse', dest="collapse", action="store_true",
                        help="Collapse levels with single children")
    output.add_argument('--no-collapse', dest="collapse", action="store_false",
                        help="Do not collapse levels with single children")
    output.set_defaults(collapse=True)

    output.add_argument('-c', '--color', dest="color", action="store_true",
                        help="Use ansi-color in output")
    output.add_argument('-n', '--no-color', dest="color", action="store_false",
                        help="Don't use ansi-color in output")
    output.set_defaults(color=sys.stdout.isatty())

    output.add_argument('--render-separator', action="store_true",
                        default=False,
                        help="Include separator in rendered output")

    parser.add_argument(dest="files", nargs="*", type=argparse.FileType(),
                        metavar="FILE",
                        default=[sys.stdin],
                        help="File to read from")

    args = parser.parse_args()

    return args


def main() -> None:
    """ Main entry point. """

    options = parse_args()

    tree = tree_factory()

    for path in chain(*options.files):
        fragments = path.strip().split(options.separator)

        node(tree, *fragments)

    tree_print(tree, options=options)


if __name__ == "__main__":
    main()
