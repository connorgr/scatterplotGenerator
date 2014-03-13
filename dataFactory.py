import json
import os
import scatterData

colorLayouts = ['grouped','random']
markSizes = [4,6,8,10]
quads = ['tl', 'tr', 'bl', 'br']
slopes = ['positive', 'negative'] # degrees rotating from vertical orientation
setSizes = [196, 256, 324, 400]

output = []
for c in colorLayouts:
  for m in markSizes:
    for s in setSizes:
      for slope in slopes:
        for q in quads:
          print c,m,s,slope,q
          d = scatterData.makeScatterData(s, slope, q);
          d['colorLayout'] = c
          d['markSize'] = m
          d['quad'] = q
          d['setSize'] = s
          d['slope'] = slope
          output.append(d)

filePath = os.getcwd() + '/clusterdata.json'
with open(filePath, 'w') as fPath:
  json.dump(output, fPath)