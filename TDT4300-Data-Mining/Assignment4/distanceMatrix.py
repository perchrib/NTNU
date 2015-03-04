import math 

def distance(x,y):
	return round(math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2),2)


A = (1,2)
B = (3,7)
C = (7,8)
D = (14,6)
E = (11,1)

points = [A,B,C,D,E]
def modify(txt):
	string = ""
	temp = len(txt)
	for x in range(5-temp):
		string += " "
	return txt + string

def main():
	length = len(points)
	string = "      P"
	for x in range(length):
		if(x < length -1):
			string += str(x) + "      P" 
		else:
			string += str(x)
	print string
	print "\n"
	for x in range(length):
		dis = ""
		for y in range(length):

			dis += modify(str(distance(points[x],points[y]))) + "   "
			

		print "P" + str(x) +"   " +dis+"\n"

		
		
		
			


main()