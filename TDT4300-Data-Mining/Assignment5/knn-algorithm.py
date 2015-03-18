import math
import coordinates 

dataset,c1,c2,c3 = coordinates.getDataSet()

def euclidean(x,y):
	return round(math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2),2)

def manhatten(x,y):
	return abs(x[0]-y[0])+abs(x[1]-y[1])



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
	




printDistance(1)