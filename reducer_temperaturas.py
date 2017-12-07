#!/usr/bin/env python

from operator import itemgetter #No lo esta usando
import sys

current_measure = None
current_city = None
current_temp = None
city = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    measure, city, temp  = line.split('\t', 2)

    # convert count (currently a string) to int
    try:
        temp = float(temp)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_measure == measure:
        if measure == 'min':
            if temp < current_temp:
                current_temp = temp
                current_city = city
        elif temp > current_temp:
            current_temp = temp
            current_city = city
    else:
        if current_measure:
            print '%s:\t%s\t%s' % (current_measure, current_city, current_temp)
        
        current_measure = measure
        current_temp = temp
        current_city = city

print '%s:\t%s\t%s' % (current_measure, current_city, current_temp)
