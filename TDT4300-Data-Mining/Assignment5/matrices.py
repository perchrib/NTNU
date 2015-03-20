import coordinates
import math
from colors import Color

dataSet = coordinates.getAllClasses()
sample = coordinates.getSampleClass()


def euclidean(x,y):
	return round(math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2),2)

def manhatten(x,y):
	return abs(x[0]-y[0])+abs(x[1]-y[1])

def makeTextColor(txt,c):
	rTxt = ""
	if c =='r':
		rTXT += Color.red + txt + Color.end
	elif c == 'b':
		rTXT += Color.blue + txt + Color.end

	elif c == 'y':
		rTXT += Color.yellov + txt + Color.end

	return rTXT


def distanceMatrix(a):
	hString = "\t"
	l = len(dataSet)
	r = Color.red
	ye = Color.yellow
	b = Color.blue
	e = Color.end
	w = Color.white
	matrix = []

	for x in range(l):
		color2 = ""
		vString = ""
		
		if dataSet[x].cluster == "C1":
			color2 += r
		elif dataSet[x].cluster == "C2": 
			color2 += b
		elif dataSet[x].cluster == "C3": 
			color2 += ye
		vString += color2 + dataSet[x].name + e 
		for y in range(l):
			color=""
			

			if dataSet[y].cluster == "C1":
				color += r
			elif dataSet[y].cluster == "C2": 
				color += b
			elif dataSet[y].cluster == "C3": 
				color += ye
			
			if x == 0:
				hString += color + dataSet[y].name + "  \t" + e
			if a == 0:
				c =""
				#print dataSet[x].cluster
				if dataSet[x].cluster == dataSet[y].cluster:
					if dataSet[x].cluster == "C1":
						c += r
					elif dataSet[x].cluster == "C2":
						c += b
					elif dataSet[x].cluster == "C3":
						c += ye



				else:
					c += w 
				
				vString += c + "\t"+ str(manhatten(dataSet[x].grid,dataSet[y].grid))


		matrix.append(vString)
	matrix.insert(0,hString)
	print "\n"
	print "\t"+"\t"+"\t"+"\t",r + "C1: " + "RED" + e
	print "\t"+"\t"+"\t"+"\t",b + "C2: " + "BLUE" + e
	print "\t"+"\t"+"\t"+"\t",ye + "C3: " + "YELLOW" + e
	print "\t"+"\t"+"\t"+"\t",w + "NO CLUSTER: " + "WHITE"+ w + e
 	return matrix


def realIdeal():
	X = 3.75
	Y = 4.25
	Z = 5.75
	hString = "\t"
	l = len(dataSet)

	matrix = []

	for x in range(l):
		vString = ""
		vString += dataSet[x].name
		for y in range(l):
			if x == 0:
				hString += dataSet[y].name + "  \t"
				
			
			if dataSet[x].cluster == "C1" and dataSet[x].cluster != dataSet[y].cluster:
				vString += "\t" + "1"
			



			elif dataSet[x].cluster != dataSet[y].cluster:
				vString += "\t" + "0"


		
		matrix.append(vString)

	matrix.insert(0,hString)

	return matrix




def idealMatrix():
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
			elif dataSet[x].cluster != dataSet[y].cluster:
				vString += "\t" + "0"


		
		matrix.append(vString)

	matrix.insert(0,hString)

	return matrix



def main():
	#i = idealMatrix()
	i = idealMatrix()
	for l in i:
		print "\n", l
main()






