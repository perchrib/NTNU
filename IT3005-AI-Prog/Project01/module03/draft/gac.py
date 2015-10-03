import gui
import random

class CSP:
	def __init__(self,variables):
		self.variables = variables
		self.constraint = self.makefunc(['A','B'],'A != B')





	def initialice(self,vertexes):
		combinations = []
		for key in vertexes:
			v = vertexes[key]
			for n in v.neighbour:
				if 'row' in key:
					combinations.append((v,n))
					

		return self.ac_3(combinations)
	

	def ac_3(self,queue):
		queue = queue
		print len(queue)
		while queue:

			xi,xj = queue.pop(0)
			print "combo: ", xi.index, xj.index 
			if self.revise(xi,xj):
				if len(xi.domain) == 0:
					return False
				for xn in xi.neighbour:
					#print "ADDED"
					queue.append((xn,xi))
		return True

	
	def revise(self,xi,xj):
		
		revised = False
		
		#index_x = random.randint(0,xi.length-1)
		#print xi.index, xj.index
		delete = []
		for x in xi.domain:
			all_inValid = True
			

			for y in xj.domain:
				
				
				print "X: ", x
				print "Y: ", y
				x_i = x[xi.index[1]]
				k = xj.length - xi.index[1]
				y_i = y[k-1]
				  
				print "XI", x_i
				print "YI", y_i
				b = self.constraint(x_i,y_i)
				print b
				#print "X:", x, "Y:",y,"Func:",b
				if not b:
					#delete.append(x)
					all_inValid = False
					# for x_t in xi.domain:
					# 	print "DOMAIN: ", x_t
					# print "Removed X: ", x
					# xi.domain.remove(x)
					# revised = True
					# break

			if all_inValid:
				# for x_t in xi.domain:
				# 	print "DOMAIN: ", x_t
				print "Removed X: ", x
				xi.domain.remove(x)
				revised = True

		# if delete:
		# 	for temp in xi.domain:
		# 		print "domain: ", temp
		# 	for d in delete:
		# 		print "deleted: ", d
		# 		xi.domain.remove(d)
		# 	revised = True


		return revised

	def makefunc(self,var_names,expression,envir=globals()):
		args = ""
		for n in var_names:
			args = args + "," + n

		return eval("(lambda " + args[1:] + ": " + expression + ")", envir)

def main():
	variables,rows,cols = gui.getVariables()
	csp = CSP(variables)
	print csp.initialice(variables)

	for key in csp.variables:
		variable = variables[key]
		#if key ==('row',0):
		#	for n in variable.domain:
		#		print n
		if 'row' in key:
			print "key: ", variable.index, "domain: ", len(variable.domain)
		#print "key: ", variable.index, "fill:", variable.fill

main()



