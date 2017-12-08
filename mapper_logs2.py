#!/usr/bin/env python

import sys

URL = 3

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    tokens = line.split()
    
    print '%s\t%s' % (tokens[URL], 1)
