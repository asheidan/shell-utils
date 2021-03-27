#!/usr/bin/env python3

import sys
import urllib.parse

lines = sys.stdin

if sys.argv[1:]:
    lines = [" ".join(sys.argv[1:])]

for line in lines:
    print(urllib.parse.unquote(line.strip()))
