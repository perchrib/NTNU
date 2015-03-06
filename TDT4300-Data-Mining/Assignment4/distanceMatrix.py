import math 

def distance(x,y):
	return round(math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2),2)


A = (1,2)
B = (3,7)
C = (7,8)
D = (14,6)
E = (11,1)
# A = (2,4)
# B = (4,17)
# C = (5,14)
# D = (5,7)
# E = (5,4)
# F = (6,19)
# G = (7,17)
# H = (7,4)
# I = (8,18)
# J = (9,15)
# K = (9,4)
# L = (12,12)
# M = (12,9)
# N = (14,13)
# O = (14,11)
# P = (15,8)
# Q = (16,13)
# R = (17,11)




points = [A,B,C,D,E]
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