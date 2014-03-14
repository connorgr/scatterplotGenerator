import json
import os
import time

if not os.path.exists('completeGridData'):
  os.makedirs('completeGridData')


outData = []
gridData = 'out'
files = os.listdir(gridData + '/')
for f in files:
  if '.json' not in f: continue
  json_data=open(f)
  data = json.load(json_data)
  outData.append(data)
  json_data.close()

fileName = time.strftime('%c')
fPath = '/home/connor/scatterplotGenerator/completeGridData/'+fileName
json.dump(outData, fPath)