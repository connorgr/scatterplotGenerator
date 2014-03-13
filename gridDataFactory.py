#!/usr/bin/python

import json
import os
import scatterData
import sys
import time

c = sys.argv[1] # color layout = ['grouped','random']
m = sys.argv[2] # mark size = [4,6,8,10]
s = sys.argv[3] # set size = [196, 324, 484]
slope = sys.argv[4] # slope = ['positive', 'negative']
q = sys.argv[5] # quadrant = ['tl', 'tr', 'bl', 'br']
r = sys.argv[6] # repetition = 10

start = time.clock()

d = scatterData.makeScatterData(s, slope, q)
d['colorLayout'] = c
d['markSize'] = m
d['quad'] = q
d['setSize'] = s
d['slope'] = slope
d['repetition'] = r

elapsed = (time.clock() - start)
d['timeToMake'] = elapsed

print 'Total elapsed time: ' + str(elapsed)

fileName = c + '_' + s + '_' + m + '_' + slope + '_' + q + '_' + r + '.json'
filePath = os.getcwd() + '/' + fileName
with open(filePath, 'w') as fPath:
  json.dump(d, fPath)