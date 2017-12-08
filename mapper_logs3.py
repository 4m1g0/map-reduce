#!/usr/bin/env python

import sys

URL = 0
VISITS = 1

maxVisits = 0
url = ''

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    tokens = line.split()
    
    try:
        visits = int(tokens[VISITS])
    except ValueError:
        continue
    
    
    if visits > maxVisits:
        maxVisits = visits
        url = tokens[URL]
    
print 'max\t%s\t%s' % (url, maxVisits)
