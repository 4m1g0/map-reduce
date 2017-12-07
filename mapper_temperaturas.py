#!/usr/bin/env python

import sys

ID = 0
T_DAILY_MAX = 5
T_DAILY_MIN = 6

minTemp = 999.0
maxTemp = -999.0

maxStation = {
    'id': '0',
    'temp': -999.0 
}

minStation = {
    'id': '0',
    'temp': 999.0 
}
    

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    tokens = line.split()
    
    if (float(tokens[T_DAILY_MAX]) > maxStation['temp']):
        maxStation['id'] = tokens[ID]
        maxStation['temp'] = float(tokens[T_DAILY_MAX])
    
    if (tokens[T_DAILY_MIN] != '-9999.0' and float(tokens[T_DAILY_MIN]) < minStation['temp']):
        minStation['id'] = tokens[ID]
        minStation['temp'] = float(tokens[T_DAILY_MIN])
    
print 'max\t%s\t%s' % (maxStation['id'], maxStation['temp'])
print 'min\t%s\t%s' % (minStation['id'], minStation['temp'])

