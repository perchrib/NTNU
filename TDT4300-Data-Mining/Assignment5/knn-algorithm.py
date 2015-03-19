import math
import coordinates 
import operator
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

clusters,samples = coordinates.getDataSet()

allSamples = []
allPoints = []
def euclidean(x,y):
	return round(math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2),2)

def manhatten(x,y):
	return abs(x[0]-y[0])+abs(x[1]-y[1])


class Samples:
	name = "XYZ"
	i = 0
	def __init__(self,grid):
		self.grid = grid
		self.x = grid[0]
		self.y = grid[1]
		self.neighbours = {}
		self.name = Samples.name[Samples.i]
		Samples.i += 1
		self.shortestN = []
		self.longestNeighbourInRangeK = 0

	



class Point:
	totalClusters = []
	def __init__(self,grid,cluster):
		self.grid = grid
		self.x = grid[0]
		self.y = grid[1]
		self.cluster = cluster
		self.addClusters(cluster)
		

	def addClusters(self,cluster):
		if cluster not in Point.totalClusters:
			self.totalClusters.append(cluster)

def generatePoints():
	i = 1
	for cluster in clusters:
		whichCluster = "C" + str(i)
		for grid in cluster:
			allPoints.append(Point(grid,whichCluster))
		i += 1
		

def generateSamples():
	for s in samples:
		allSamples.append(Samples(s))

def generateNeighboursEucledian():
	for s in allSamples:
		distances = []
		for p in allPoints:
			d = euclidean(s.grid,p.grid)
			s.neighbours[p] = d


def generateNeighboursManhatten():
	for s in allSamples:
		distances = []
		for p in allPoints:
			d = manhatten(s.grid,p.grid)
			s.neighbours[p] = d

def findNearestNeighbour(k):
	for s in allSamples:
		shortestN = sorted(s.neighbours.items(), key=operator.itemgetter(1))
		s.shortestN = shortestN[:k]
		s.longestNeighbourInRangeK = s.shortestN[-1][1]

def findWhichType(list):
	modList = sorted(Counter(list).items(), key=operator.itemgetter(1))
	return modList[-1][0]

def classifier():
	for s in allSamples:
		clusters = []
		for n in s.shortestN:
			clusters.append(n[0].cluster)
		print s.name, "has nearest neighbour Type: ", clusters , "and belongs to: ", findWhichType(clusters)


def modify(txt):
	string = ""
	temp = len(txt)
	for x in range(5-temp):
		string += " "
	string += txt
	return string





def printDistance(a):
	l = len(dataset)
	string = "\tP"
	for x in range(l):
		if(x < l -1):
			string += str(x) + "\tP" 
		else:
			string += str(x)
	print string
	
	print "\n"
	temp = 0
	for x in range(l):
		if x >= 10:
			temp = ""
		dis = ""
		for y in range(l):
			if a == 0:
				dis += modify(str(euclidean(dataset[x],dataset[y]))) + "\t"
			elif a == 1:
				dis += modify(str(manhatten(dataset[x],dataset[y]))) + "\t"
		
		print "P"+ str(temp)+ str(x)+"\t" +dis+"\n"


def inputV():
	k = input("type in a value of K-neighbours: ")
	while int(k) < 0:
		k = input("type in a value of K-neighbours: ")
	a = input("type 0 for manhatten or 1 for euclidian: ")
	while int(a) != 0 and int(a) !=1:
		a = input("type 0 for manhatten or 1 for euclidian: ")
	return a,k


def plotEverything(a):
	c1x = []
	c1y = []
	c2x = []
	c2y = []
	c3x = []
	c3y = []
	for p in allPoints:
		if p.cluster == "C1":
			c1x.append(p.x)
			c1y.append(p.y)
		elif p.cluster == "C2":
			c2x.append(p.x)
			c2y.append(p.y)
		elif p.cluster == "C3":
			c3x.append(p.x)
			c3y.append(p.y)
	plt.plot(c1x,c1y, 'ro', label = 'C1')
	plt.plot(c2x,c2y, 'bo', label = 'C2')
	plt.plot(c3x,c3y, 'yo', label = 'C3')
	plt.plot([allSamples[0].x],[allSamples[0].y], 'ko', label = allSamples[0].name )
	plt.plot([allSamples[1].x],[allSamples[1].y], 'kD', label = allSamples[1].name )
	plt.plot([allSamples[2].x],[allSamples[2].y], 'ks', label = allSamples[2].name )
	c1 = plt.Circle((allSamples[0].x,allSamples[0].y),allSamples[0].longestNeighbourInRangeK,color='k',fill=False)
	c2 = plt.Circle((allSamples[1].x,allSamples[1].y),allSamples[1].longestNeighbourInRangeK,color='k',fill=False)
	c3 = plt.Circle((allSamples[2].x,allSamples[2].y),allSamples[2].longestNeighbourInRangeK,color='k',fill=False)
	fig = plt.gcf()
	fig.gca().add_artist(c1)
	fig.gca().add_artist(c2)
	fig.gca().add_artist(c3)
	plt.legend()
	plt.axis([0,12,0,10])
	if a == 0:
		plt.title('k-NN : MANHATTEN')
	else:
		plt.title('k-NN : EUCLIDIAN')
	plt.show()

def main():
	a,k = inputV()
	generatePoints()
	generateSamples()
	if int(a) == 0:
		print "\t\t" , "############ YOU CHOSEN MANHATTEN!!! ############"
		generateNeighboursManhatten()
	elif int(a) == 1:
		print "\t\t" , "############ YOU CHOSEN EUCLIDIAN!!! ############"
		generateNeighboursEucledian()
	findNearestNeighbour(int(k))
	classifier()
	plotEverything(int(a))
main()
