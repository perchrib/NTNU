import math 
import numpy as np
import matplotlib.pyplot as plt
import coordinates
import copy

def distance(p1,p2):
	return round(math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2),2)


eps = 3.0
minPts = 3.0

points = []
queue = []

x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []


class Point:
	ID = 1
	def __init__(self,coordinate):
		self.x = coordinate[0]
		self.y = coordinate[1]
		self.color = ""
		self.neighbours = []
		self.ID = Point.ID
		Point.ID += 1

	def addNeighbours(self,point):
		self.neighbours.append(point)

	def numOfNeighbours(self):
		return len(self.neighbours)





def generateCells():
	coor = coordinates.allCoordinates()
	for x in coor:
		points.append(Point(x))

def findNeighbours():
	
	for i in range(len(points)):
		pn = points[i]
		for j in range(i+1,len(points)):
			pm = points[j]
			d = distance(pn,pm)
			if d <= eps:
				pn.addNeighbours(pm)
				pm.addNeighbours(pn)
				#print "NABO" ,pn.ID,pm.ID, pn.x,pn.y,pm.x,pm.y



	



def setTypeToPoint():
	for point in points:
		if point.numOfNeighbours() >= minPts:
			print point.numOfNeighbours(), point.x,point.y

			x1.append(point.x)
			y1.append(point.y)


			point.color = 'r'
		elif point.numOfNeighbours() == 0:
			x2.append(point.x)
			y2.append(point.y)
			point.color = 'g'
		elif point.numOfNeighbours() < minPts:
			x3.append(point.x)
			y3.append(point.y)
			point.color = 'y'

def n():
	for p in points:
		print p.ID, "Har nabo"
		for n in p.neighbours:
			print n.ID



def main():
	generateCells()
	findNeighbours()
	setTypeToPoint()
	plt.plot(x1,y1,'ro',x2,y2,'*',x3,y3,'_')
	plt.axis([0,20,0,20])
	plt.ylabel('some numbers')
	n()

	plt.show()

main()




		


