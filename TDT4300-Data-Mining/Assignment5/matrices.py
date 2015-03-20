import coordinates
import math

dataSet = coordinates.getAllClasses()


def euclidean(x,y):
	return round(math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2),2)

def manhatten(x,y):
	return abs(x[0]-y[0])+abs(x[1]-y[1])



def similarity():
	hString = "\t"
	l = len(dataSet)

	matrix = []
	for x in range(l):
		vString = ""
		vString += dataSet[x].name
		for y in range(l):
			if x == 0:
				hString += dataSet[y].name + "  \t"
				
			
			if dataSet[x].cluster == dataSet[y].cluster:
				vString += "\t" + "1"
			else:
				vString += "\t" + "0"


		
		matrix.append(vString)

	matrix.insert(0,hString)

	return matrix



def main():
	m = similarity()
	for l in m:
		print "\n", l
main()