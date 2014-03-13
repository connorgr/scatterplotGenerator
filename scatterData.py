import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys

from pylab import *

def rotatePts(xs, ys, slope):
  theta = -90#-45
  if slope == 'positive':
    theta = -45
  rotation = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
  rotatedPoints = np.dot(rotation, np.array([xs, ys]))
  xs = rotatedPoints[0]
  ys = rotatedPoints[1]

  return xs, ys

def makeCluster(center, setSize, slope):
  x = center[0]
  y = center[1]
  xStd = 10
  yStd = 3.5

  pts_x = []
  pts_y = []
  pts = []

  overlapDistance = 10

  # Add random, non-overlapping points

  pts_x = np.random.normal(x, xStd, setSize)
  pts_y = np.random.normal(y, yStd, setSize)
  return pts_x, pts_y

# Expects an length 8 means (4 xy pairs) and an 8x8 covariance matrix
def makeFourClusters(means, covar, overlap, seedSize, setSize, slope):
  def formatCluster(x,y,num):
    return zip(list(x), list(y), [num for i in range(len(list(x)))])

  def removeOverlaps(pts):
    originalData = map(lambda x: list(x), zip(*pts))
    xs = originalData[0]
    ys = originalData[1]
    clusterIds = originalData[2]

    overlapPts = []
    for x, y, cluster in pts:
      index = xs.index(x)
      # escape the loop if we're on the last element
      if index == len(xs) - 1:
        break
      # check all later xs for overlap
      for i in range(index+1,len(pts)):
        if abs(x-xs[i]) <= overlap and abs(y-ys[i]) <= overlap:
          overlapPts.append((xs[i], ys[i], clusterIds[i]))

    # Remove duplicates from the overlap list
    overlapPtsSet = set(overlapPts)
    ptsSet = set(pts)

    distinctPts = list(ptsSet - overlapPtsSet)
    numRemoved = len(overlapPtsSet)
    return distinctPts, numRemoved


  x1, y1, x2, y2, x3, y3, x4, y4 = np.random.multivariate_normal(means, covar, seedSize/4).T
  x1, y1 = rotatePts(x1, y1, slope)
  x2, y2 = rotatePts(x2, y2, slope)
  x3, y3 = rotatePts(x3, y3, slope)
  x4, y4 = rotatePts(x4, y4, slope)

  c1 = formatCluster(x1,y1,1)
  c2 = formatCluster(x2,y2,2)
  c3 = formatCluster(x3,y3,3)
  c4 = formatCluster(x4,y4,4)

  clusters = c1 + c2 + c3 + c4

  pts, numRemoved = removeOverlaps(clusters)

  # The number of elements allowed in each cluster
  capacity = setSize/4

  # fudge factor used to reduce iterations if needed
  fudgeFactor = (seedSize-setSize)/2

  # array for seeing if generation of a plot is stuck
  history = []
  historyLen = 30
  while True:
    x1, y1, x2, y2, x3, y3, x4, y4 = np.random.multivariate_normal(means, covar, numRemoved/4).T

    x1, y1 = rotatePts(x1, y1, slope)
    x2, y2 = rotatePts(x2, y2, slope)
    x3, y3 = rotatePts(x3, y3, slope)
    x4, y4 = rotatePts(x4, y4, slope)
    c1 = formatCluster(x1,y1,1)
    c2 = formatCluster(x2,y2,2)
    c3 = formatCluster(x3,y3,3)
    c4 = formatCluster(x4,y4,4)

    clusters = c1 + c2 + c3 + c4

    allPts = pts + clusters
    pts, numRemoved = removeOverlaps(allPts)

    clusters = map(lambda x: x[2], pts)
    lenC1 = len(filter(lambda x: True if x == 1 else False, clusters))
    lenC2 = len(filter(lambda x: True if x == 2 else False, clusters))
    lenC3 = len(filter(lambda x: True if x == 3 else False, clusters))
    lenC4 = len(filter(lambda x: True if x == 4 else False, clusters))
    lenAll = lenC1 + lenC2 + lenC3 + lenC4

    clustersFull = lenC1 >= capacity and lenC2 >= capacity and lenC3 >= capacity and lenC4 >= capacity
    if clustersFull:
      break

    # The following code block is failure recovery if a given sample isn't converging
    history.append(lenAll)
    if len(history) > historyLen:
      history = history[len(history)-historyLen:historyLen-1]
      uniqueHistory = set(history)
      if len(uniqueHistory) == 1:
        print 'Clusters not converging to cluster size. Remaking cluster....'
        return makeFourClusters(means, covar, overlap, seedSize, setSize, slope)

  # Unzip the points
  #pts = map(lambda x: list(x), zip(*pts))

  c1 = filter(lambda x: True if x[2] == 1 else False, pts)[:capacity]
  c2 = filter(lambda x: True if x[2] == 2 else False, pts)[:capacity]
  c3 = filter(lambda x: True if x[2] == 3 else False, pts)[:capacity]
  c4 = filter(lambda x: True if x[2] == 4 else False, pts)[:capacity]

  clusters = [c1,c2,c3,c4]
  return [map(lambda x: list(x), zip(*pts)) for pts in clusters]


################################################################################
################################################################################
# RUN THE CODE!
# Assumes that setSize is < 700; if you want a larger value feel free to change
#  the 700 seedSize to be larger. seedSize is about 2x th set size as it is
#  faster to overgenerate points and then cull extras
def makeScatterData(setSize, slope, targetQuad):
  bigMean = [ 40,40,
              40,60,
              60,40,
              60,60]
  bigCovar = [[50,0,0,0,0,0,0,0],[0,200,0,0,0,0,0,0],
              [0,0,50,0,0,0,0,0],[0,0,0,200,0,0,0,0],
              [0,0,0,0,50,0,0,0],[0,0,0,0,0,200,0,0],
              [0,0,0,0,0,0,50,0],[0,0,0,0,0,0,0,200]]

  clusters = makeFourClusters(bigMean, bigCovar, 2, 700, setSize, slope)
  minX = min(min(c[0]) for c in clusters)
  minY = min(min(c[1]) for c in clusters)

  for c in clusters:
    if minX < 0:
      c[0] = [x + abs(minX) for x in c[0]]
    if minY < 0:
      c[1] = [y + abs(minY) for y in c[1]]

  maxX = max(max(c[0]) for c in clusters)
  maxY = max(max(c[1]) for c in clusters)

  outputRows = []
  for c in clusters:
    xs = [(x/maxX)*100 for x in c[0]]
    ys = [(y/maxY)*100 for y in c[1]]
    cluster = c[2]

    # TODO create color assignments to zip in the below for loop
    clusterLen = len(xs)
    numClusters = len(clusters)
    numColors = 4.0
    marksPerColor = clusterLen/numColors

    colorsRemaining = []
    for i in range(4):
      colorsRemaining.append(marksPerColor)

    # Assign random color assignments for each point
    # This means that each grid can be used either for group or single colors
    randColor = []
    for i in range(clusterLen):
      index = np.random.random_integers(1,numColors)
      while colorsRemaining[index-1] == 0:
        index = np.random.random_integers(1,numColors)
      color = index
      colorsRemaining[index-1] = colorsRemaining[index-1] - 1
      # add the color to the list of colors
      randColor.append(color)

    for x,y,c,r in zip(xs,ys,cluster,randColor):
      outputRows.append({'x':x,'y':y,'cluster':c, 'randColor':r})

  while True:
    index = np.random.random_integers(0,len(outputRows)-1)
    pt = outputRows[index]
    #print targetQuad, pt
    if targetQuad == 'tl':
      if pt['x'] < 50 and pt['y'] > 50:
        outputRows[index]['cluster'] = 5
        outputRows[index]['randColor'] = 5
        break
    elif targetQuad == 'tr':
      if pt['x'] > 50 and pt['y'] > 50:
        outputRows[index]['cluster'] = 5
        outputRows[index]['randColor'] = 5
        break
    elif targetQuad == 'bl':
      if pt['x'] < 50 and pt['y'] < 50:
        outputRows[index]['cluster'] = 5
        outputRows[index]['randColor'] = 5
        break
    elif targetQuad == 'br':
      if pt['x'] > 50 and pt['y'] < 50:
        outputRows[index]['cluster'] = 5
        outputRows[index]['randColor'] = 5
        break
    else:
      print 'ERROR!!! QUAD NON-EXISTANT!'
      sys.exit(1)
  output = {'pts': outputRows}
  return output
