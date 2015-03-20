p1 = (4,6)
p2 = (6,9)
p3 = (8,8)
p4 = (3,3)
p5 = (10,2)
p6 = (9,6)
p7 = (8,1)
p8 = (3,4)
p9 = (8,3)
p10 = (4,4)

x = (6,3)
y = (6,6)
z = (8,5)
#dataset = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]

c1 = [p1,p4,p8,p10]
c2 = [p2,p3,p6]
c3 = [p5,p7,p9]
samples = [x,y,z]

dataSet = []

class Point:
	def __init__(self,grid,cluster,name):
		self.grid = grid
		self.cluster = cluster
		self.name = name


	
i = 0
j = 0
m = 0
for x in range(1,11):
	if x in [1,4,8,10]:
		dataSet.append(Point(c1[i],"C1","P"+str(x))) 
		i += 1
	elif x in [2,3,6]:	
		dataSet.append(Point(c2[j],"C2","P"+str(x))) 
		j += 1
	elif x in [5,7,9]:
		dataSet.append(Point(c3[m],"C3","P"+str(x)))
		m += 1


def getAllClasses():
	return dataSet

#for s in dataSet:
#	print s.name,s.cluster,s.grid


def getSampleClass():
	name = ["X","Y","Z"]
	samp =[]
	for s in range(len(samples)):
		samp.append(Point(samples[s],"SAMPLE", name[s]))

	return samp




def getDataSet():
	return [c1,c2,c3],samples

def getC1():
	return c1

def getSamples():
	return samples








