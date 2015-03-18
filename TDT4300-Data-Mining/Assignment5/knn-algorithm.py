import math
import coordinates 

clusters,samples = coordinates.getDataSet()

allSamples = []
allPoints = []
def euclidean(x,y):
	return round(math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2),2)

def manhatten(x,y):
	return abs(x[0]-y[0])+abs(x[1]-y[1])


class Samples:
	def __init__(self,grid):
		self.grid = grid
		self.x = grid[0]
		self.y = grid[1]
		self.neighbours = {}
	


	def getNeighbours(self,k):
		return self.neighbours



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

		for p in allPoints:
			d = euclidean(s.grid,p.grid)
			s.neighbours[p] = d




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
	

generatePoints()
generateSamples()
generateNeighboursEucledian()
for s in allSamples:
	print s.neighbours

