#!/usr/bin/env python

import sys

USER = 2
URL = 3

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    tokens = line.split()
    
    if ".jpg" in tokens[URL]:
        count = 1
    else:
        continue
    
    print '%s\t%s' % (tokens[USER], count)
