#!/usr/bin/env python
import sys

current_attribute = None
current_value = 0.0
attribute = None
i = 0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    attribute, value = line.split('\t', 1)

    # convert value (currently a string) to int
    try:
        value = float(value)
    except ValueError:
        # value was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: attribute) before it is passed to the reducer
    if current_attribute == attribute:
        current_value += value
        i += 1
    else:
        if current_attribute:
            # write result to STDOUT
            print '%s\t%s' % (current_attribute, current_value/i)
        i = 1
        current_value = value
        current_attribute = attribute

# do not forget to output the last attribute if needed!
if current_attribute == attribute:
    print '%s\t%s' % (current_attribute, current_value/i)
