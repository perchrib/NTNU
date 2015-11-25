import gui
import random
from a_star import A_star

class CSP:
	def __init__(self,variables):
		self.variables = variables.variables
		self.constraint = self.makefunc(['A','B'],'A == B')

	"""Gac initialaze, start filtering if possible"""
	def initialice(self,vertexes):
		combinations = []
		for key in vertexes:
			v = vertexes[key]
			for n in v.neighbour:
				combinations.append((v,n))
		return self.ac_3(combinations)
	"""Gac rerun, called when a star is used"""
	def rerun(self,v):
		print "ASUMTION: ", v.index
		combinations = []
		for n in v.neighbour:
			combinations.append((n,v))
		return self.ac_3(combinations)


	def isFinish(self):
		for key in self.variables:
			variable = self.variables[key]
			if len(variable.domain) != 1:
				return False
		return True
	
	"""The domain filtering loop, filter all domains that does not satisfy the constraints """
	def ac_3(self,queue):
		queue = queue
		while queue:

			xi,xj = queue.pop(0)
			if self.revise(xi,xj):
				if len(xi.domain) == 0:
					return False
				for xn in xi.neighbour:
					#print "ADDED"
					queue.append((xn,xi))
		return True

	"""Revise function actually delete domains that not satisfy the constraints, return true if 
	it removes a domain, othervise False"""
	def revise(self,xi,xj):
		
		revised = False
		delete = []
		for x in xi.domain:
			all_inValid = True
			for y in xj.domain:
				if 'row' in xi.index[0]:
					x_i = x[xj.index[1]]
					k = xj.length - xi.index[1] 
					y_i = y[k - 1] # -1
				if 'col' in xi.index[0]:
					k = xi.length - xj.index[1]
					x_i = x[k-1]
					y_i = y[xi.index[1]]  

				if self.constraint(x_i,y_i):
					
					all_inValid = False

			if all_inValid:
				xi.domain.remove(x)
				revised = True


		return revised
	"""Make func, creates chunks of code depending on input"""
	def makefunc(self,var_names,expression,envir=globals()):
		args = ""
		for n in var_names:
			args = args + "," + n

		return eval("(lambda " + args[1:] + ": " + expression + ")", envir)


"""MAIN, Start everything from here"""
def main():
	variables,rows,cols,gui_draw = gui.getVariables()
	node = gui.Node(None,variables)

	csp = CSP(node)
	csp.initialice(node.variables)

	while not csp.isFinish():
		#csp.initialice(node.variables)
		a_star = A_star('astar',node,csp) 
		print "Astar Started: "
		a_star.mainLoop()



	finishedRows = []
	for key in csp.variables:
		variable = variables[key]
		if 'row' in key:
			finishedRows.append(variable)
			if variable.index[1] > 9:
				print "key: ", variable.index, "domain: " ,variable.domain ," len: ", len(variable.domain), "fill: ", variable.fill
			else:
				print "key: ", variable.index, " domain: ",variable.domain , " len: ", len(variable.domain), "fill: ", variable.fill
				
		else:
			if variable.index[1] > 9:
				print "key: ", variable.index, "domain: " ,variable.domain ," len: ", len(variable.domain), "fill: ", variable.fill
			else:
				print "key: ", variable.index, " domain: ",variable.domain , " len: ", len(variable.domain), "fill: ", variable.fill
				
	
	finishedRows.reverse()
	for variable in finishedRows:
		for i in range(cols):

			gui_draw.canvas.itemconfig('a'+str(variable.index[1])+'-'+str(i), fill=gui.setColor(variable.domain[0][i]))

	gui_draw.after(5,gui_draw.update())
	gui_draw.mainloop()

main()



