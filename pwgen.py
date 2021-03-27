#!/usr/bin/env python3

import io
import locale
import os
from random import random, seed
import sys
from math import log

seed()

# locale.setlocale(locale.LC_ALL, '')

SEPARATORS = "-_#%&/|<([{}])>=?+*.:,;"
sep_count = len(SEPARATORS)
separator = SEPARATORS[int(random() * sep_count)]

encoding = locale.getpreferredencoding()

word_path = "~/Documents/wordlists/english-word-list-sowpods"
# word_path = "~/Documents/wordlists/swedish-word-list"
WORD_LIST = os.path.expanduser(word_path)

pass_length = 5

if 2 <= len(sys.argv):
    arg_length = int(sys.argv[1])
    if arg_length:
        pass_length = arg_length

with io.open(WORD_LIST, "r", encoding='iso8859-1') as list_file:
    words = list_file.readlines()
    N = len(words)
    ns = (int(random() * N) for _ in range(pass_length))
    pw_list = (words[n].strip() for n in ns)

    password = separator.join(pw_list)  # .encode(encoding)
    print("Entropy: %d bits\tCombinations: %g"
          % (int(log((N ** pass_length) * sep_count, 2)),
             (N ** pass_length) * sep_count,),
          file=sys.stderr)
    print("Length: %d chars\tWord list length: %d words"
          % (len(password), len(words)),
          file=sys.stderr)
    print(password)
