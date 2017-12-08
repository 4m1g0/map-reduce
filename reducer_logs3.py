#!/usr/bin/env python

from operator import itemgetter #No lo esta usando
import sys

maxVisits = 0
currentUrl = ''

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    id, url, visits1 = line.split('\t', 2)

    # convert count (currently a string) to int
    try:
        visits = int(visits1)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    if visits > maxVisits:
        maxVisits = visits
        currentUrl = url

print '%s\t%s' % (currentUrl, maxVisits)
