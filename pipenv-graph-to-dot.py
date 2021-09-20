#!/usr/bin/env python3
"""Convert pipenv graph output to dot.

Reads from stdin, outputs on stdout.

`pipenv graph --json | pipenv-graph-to-dot | dot`
"""

import json
import sys
from typing import Dict


def as_attrs(data: Dict[str, str]) -> str:
    return ", ".join(f'{key}="{value}"' for key, value in data.items())


def main() -> None:
    package_list = json.load(sys.stdin)

    print('digraph { rankdir = "LR";')

    for package in package_list:
        key = package["package"]["key"]
        name = package["package"]["package_name"]
        version = package["package"]["installed_version"]
        print(fr'"{key}" [label="{name}\n{version}"];')

        for dependency in package.get("dependencies", []):
            dependency_name = dependency["key"]
            dependency_version = dependency["required_version"] or ""

            edge_attributes = {
                "headURL": "#",
            }
            if dependency_version:
                edge_attributes['headtooltip'] = fr'{name}\n({dependency_version})'
                edge_attributes['headlabel'] = dependency_version
            else:
                edge_attributes['headtooltip'] = name

            print(f'"{key}" -> "{dependency_name}" [{as_attrs(edge_attributes)}];')

    print("}")


if __name__ == "__main__":
    main()