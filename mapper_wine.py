#!/usr/bin/env python

import sys

fixed_acidity=0
volatile_acidity=1
citric_acid=2
residual_sugar=3
chlorides=4
free_sulfur_dioxide=5
total_sulfur_dioxide=6
density=7
pH=8
sulphates=9
alcohol=10
quality=11

URL = 0
VISITS = 1

maxVisits = 0
url = ''

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    tokens = line.split(';')
    
    #print 'fixed_acidity\t%s' % (tokens[fixed_acidity])
    print 'volatile_acidity\t%s' % (tokens[volatile_acidity])
    #print 'citric_acid\t%s' % (tokens[citric_acid])
    #print 'residual_sugar\t%s' % (tokens[residual_sugar])
    #print 'chlorides\t%s' % (tokens[chlorides])
    #print 'free_sulfur_dioxide\t%s' % (tokens[free_sulfur_dioxide])
    #print 'total_sulfur_dioxide\t%s' % (tokens[total_sulfur_dioxide])
    #print 'density\t%s' % (tokens[density])
    #print 'pH\t%s' % (tokens[pH])
    #print 'sulphates\t%s' % (tokens[sulphates])
    #print 'alcohol\t%s' % (tokens[alcohol])
    #print 'quality\t%s' % (tokens[quality])
    

