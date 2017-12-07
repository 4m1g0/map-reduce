#!/usr/bin/env python

import sys
import os

USER = 2
URL = 3

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    tokens = line.split()
    
    if tokens[URL].endswith('.jpg"'):
        count = 1
    else:
        continue
        
    user = os.environ['map_input_file']
    user = user[user.rfind('/')+1:].split('.')[0]
    print '%s\t%s' % (user, count)
