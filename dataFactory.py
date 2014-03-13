import json
import os
import scatterData
import time

start = time.clock()

colorLayouts = ['grouped','random']
markSizes = [4,6,8,10]
quads = ['tl', 'tr', 'bl', 'br']
slopes = ['positive', 'negative'] # degrees rotating from vertical orientation
setSizes = [196, 324, 484]
repetitions = 10

output = []
for c in colorLayouts:
  for m in markSizes:
    for s in setSizes:
      for slope in slopes:
        for q in quads:
          for r in range(repetitions):
            d = scatterData.makeScatterData(s, slope, q)
            d['colorLayout'] = c
            d['markSize'] = m
            d['quad'] = q
            d['setSize'] = s
            d['slope'] = slope
            c['repetition'] = r
            output.append(d)

filePath = os.getcwd() + '/clusterdata.json'
with open(filePath, 'w') as fPath:
  json.dump(output, fPath)

elapsed = (time.clock() - start)

print 'Total elapsed time: ' + str(elapsed)