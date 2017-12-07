#!/usr/bin/env python

from operator import itemgetter #No lo esta usando
import sys

current_city = None
current_max = -9999.0
current_min = 9999.0
city = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    city, tmax, tmin  = line.split('\t', 2)

    # convert count (currently a string) to int
    try:
        tmax = float(tmax)
        tmin = float(tmin)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    
    #discard nulls
    if tmin == -9999.0:
        tmin = 9999.0

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_city == city:
        if current_max < tmax:
            current_max = tmax
        if current_min > tmin:
            current_min = tmin
    else:
        if current_city:
            # write result to STDOUT
            print '%s\t%s\t%s' % (current_city, current_max, current_min)
        current_min = tmin
        current_max = tmax
        current_city = city

# do not forget to output the last word if needed!
if current_city == city:
    print '%s\t%s\t%s' % (current_city, current_max, current_min)
