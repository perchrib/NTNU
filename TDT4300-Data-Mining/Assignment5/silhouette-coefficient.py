import coordinates
import operator
from collections import Counter

c1 = coordinates.getC1()
samples = coordinates.getSamples()



def manhatten(x,y):
	return abs(x[0]-y[0])+abs(x[1]-y[1])

def average(li):
	value = 0
	for i in li:
		value += i
	return value*1.0/len(li)

def silhouetteCoff():
	samplesName = ["X","Y","Z"]
	coff = {}
	i = 0
	for s in samples:
		calcCoff = []
		for p in c1:
			calcCoff.append(manhatten(s,p))
		coff[samplesName[i]] = average(calcCoff)
		i += 1
		

	return coff

def main():
	print "\n"
	print "\t", "AVERAGE DISTANCE BETWEEN SAMPLES AND OBJECTS IN C1","\n" 
	print "\n\t\t\t", "MANHATTEN DISTANCE USED!" , "\n"
	print "\t\t",sorted(silhouetteCoff().items(), key=operator.itemgetter(0)),"\n"

main()