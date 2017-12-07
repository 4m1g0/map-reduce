#!/usr/bin/env python

import sys

ID = 0
T_DAILY_MAX = 5
T_DAILY_MIN = 6

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    tokens = line.split()
    
    print '%s\t%s\t%s' % (tokens[ID], tokens[T_DAILY_MAX], tokens[T_DAILY_MIN])
