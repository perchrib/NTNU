from a_star import A_star
import gui
import sys
class CSP:
	def __init__(self,graph,gui):

		self.variables = []
		self.domains = {}
		self.constraint = self.makefunc(['A','B'],'A != B')
		self.gui = gui
		self.queue = []
		self.graph = graph.graph

	
	def add_variables(self,name, domain):
		self.variables.append(name.index)
		self.domains[name.index] = domain

	def isFinish(self):
		finish = True
		for v in self.graph:
			if len(v.domain) != 1:
				finish = False

		return finish

	"""Gac initialaze, start filtering if possible"""
	def initialice(self,vertexes):
		combinations = []
		for v in vertexes:
			for n in v.neighbour:
				combinations.append((v,n))

		return self.ac_3(combinations)
	"""Gac rerun, called when a star is used"""
	def rerun(self,vertex):
		combinations = []
		for n in vertex.neighbour:
			combinations.append((n,vertex))
		return self.ac_3(combinations)

	"""The domain filtering loop, filter all domains that does not satisfy the constraints """
	def ac_3(self,queue):
		queue = queue
		while queue:
			xi,xj = queue.pop(0)
			if self.revise(xi,xj):
				if len(xi.domain) == 0:
					return False
				for xn in xi.neighbour:
					queue.append((xn,xi))
		return True

	"""Revise function actually delete domains that not satisfy the constraints, return true if 
	it removes a domain, othervise False"""
	def revise(self,xi,xj):
		
		revised = False

		for x in xi.domain:
			no_valid = True
			for y in xj.domain:
				b = self.constraint(x,y)
				if self.constraint(x,y):
					no_valid = False
			if no_valid:
				xi.domain.remove(x)
				revised = True

		return revised
	"""Make func, creates chunks of code depending on input"""
	def makefunc(self,var_names,expression,envir=globals()):
		args = ""
		for n in var_names:
			args = args + "," + n

		return eval("(lambda " + args[1:] + ": " + expression + ")", envir)

	"""Checks if the solution is correct"""
	def is_correct(self):
		for node in self.graph:
			if not len(node.domain) is 1:
				return False
			for neighbour in node.neighbour:
				if not len(neighbour.domain) is 1:
					return False
				if neighbour.domain[0] == node.domain[0]:
					return False
		return True
"""MAIN, Start everything from here"""
def main():

	allVertexes,t_gui = gui.getVertexes() 
	sys.setrecursionlimit(5000)
	k = int(sys.argv[2])
	graph = gui.Graph(None,allVertexes)
	for vertex in graph.graph:
		vertex.domain = ['Green','Red','Blue','Yellow','Black','Brown','Pink', 'Cyan','Magenta','Orange'][:k]
	csp = CSP(graph,t_gui)
	csp.initialice(graph.graph)
	while not csp.isFinish():
		a_star = A_star('astar',graph,csp)
		print "ASTAR STARTED"
		a_star.mainLoop()

	for v in csp.graph:
		print v.domain
		color = v.domain
		csp.gui.canvas.itemconfig('a'+str(v.index), fill=color)

	print "IS CORRECT: ", csp.is_correct()
	t_gui.mainloop()
main()

















