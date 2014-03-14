import json
import os
import sys
import datetime

if not os.path.exists('completeGridData'):
  os.makedirs('completeGridData')


outData = []
gridData = 'out'
files = os.listdir(gridData + '/')
for f in files:
  if '.json' not in f: continue
  json_data=open('out/'+f)
  data = json.load(json_data)
  outData.append(data)
  json_data.close()
  sys.stdout.write('.')
print '\nDone appending data. Saving....'

fileName = str(datetime.datetime.now())
fPath = '/home/connor/scatterplotGenerator/completeGridData/'+fileName
json.dump(outData, fPath)

print 'Saving complete. File name: ' + fileName