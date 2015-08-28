import math 

def distance(x,y):
	return round(math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2),2)


#A = (1,2)
#B = (3,7)
#C = (7,8)
#D = (14,6)
#E = (11,1)
A = (2,3)
B = (4,5)
C = (6,4)
D = (6,5)
E = (7,5)
F = (7,12)
G = (8,2)
H = (8,10)
I = (8,14)
J = (9,12)
K = (9,13)
L = (10,12)
M = (11,16)
N = (13,16)
O = (13,18)
P = (16,16)
Q = (16,19)
#R = (17,11)




points = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q]
def modify(txt):
	string = ""
	temp = len(txt)
	for x in range(5-temp):
		string += " "
	string += txt
	return string

def main():
	length = len(points)
	string = "\tP"
	for x in range(length):
		if(x < length -1):
			string += str(x) + "\tP" 
		else:
			string += str(x)
	print string
	print "\n"
	temp = 0
	for x in range(length):
		if x >= 10:
			temp = ""
		dis = ""
		for y in range(length):

			dis += modify(str(distance(points[x],points[y]))) + "\t"
			

		print "P"+ str(temp)+ str(x)+"\t" +dis+"\n"

		
		
		
			


main()