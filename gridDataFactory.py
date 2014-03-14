#!/usr/bin/python

import json
import os
import sys
import time

import imp
scatterData = imp.load_source('module.name', '/path/to/file.py')

c = sys.argv[1] # color layout = ['grouped','random']
m = int(sys.argv[2]) # mark size = [4,6,8,10]
s = int(sys.argv[3]) # set size = [196, 324, 484]
slope = sys.argv[4] # slope = ['positive', 'negative']
q = sys.argv[5] # quadrant = ['tl', 'tr', 'bl', 'br']
r = int(sys.argv[6]) # repetition = 10

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

print c, m, q, s, slope, r
print 'Total elapsed time: ' + str(elapsed)
print '---------------'

fileName = c + '_' + str(s) + '_' + str(m) + '_' + slope + '_' + q + '_' + str(r) + '.json'
fileName = fileName.replace (' ', '_')
filePath = '/home/connor/scatterplotGenerator/out/' + fileName
with open(filePath, 'w') as fPath:
  json.dump(d, fPath)