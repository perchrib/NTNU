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


	def initialice(self,vertexes):
		combinations = []
		for v in vertexes:
			for n in v.neighbour:
				combinations.append((v,n))

		return self.ac_3(combinations)
	
	def rerun(self,vertex):
		combinations = []
		for n in vertex.neighbour:
			combinations.append((n,vertex))
		return self.ac_3(combinations)



	def ac_3(self,queue):
		#self.generate_permutations(self.graph)
		queue = queue
		while queue:
			xi,xj = queue.pop(0)
			#print "XI: " , xi.index, " XJ: ",xj.index, " Length: ", len(queue) 
			if self.revise(xi,xj):
				if len(xi.domain) == 0:
					return False
				for xn in xi.neighbour:
					#print "ADDED"
					queue.append((xn,xi))
				#for i,j in queue:
				#	print i.index,j.index

		return True

	
	def revise(self,xi,xj):
		
		revised = False
		
		
		#print "DOMAIN xi: ", xi.domain, " DOMAIN xj: " , xj.domain
		for x in xi.domain:
			no_valid = True
			for y in xj.domain:
				b = self.constraint(x,y)
				#print "X:", x, "Y:",y,"Func:",b
				if self.constraint(x,y):
					no_valid = False
			if no_valid:
				#print "DELETED: ", x
				xi.domain.remove(x)
				revised = True

		return revised

	def makefunc(self,var_names,expression,envir=globals()):
		args = ""
		for n in var_names:
			args = args + "," + n

		return eval("(lambda " + args[1:] + ": " + expression + ")", envir)

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

	def run_GAC(self):
		print "run"
	

def main():
	#domain = ['Green','Red']
	allVertexes,t_gui = gui.getVertexes() 
	sys.setrecursionlimit(5000)
	graph = gui.Graph(None,allVertexes)
	for vertex in graph.graph:
		vertex.domain = ['Green','Red','Blue','Yellow']
	csp = CSP(graph,t_gui)
	csp.initialice(graph.graph)
	#csp.graph[0].domain = [csp.graph[0].domain[0]]
	print "################################## yo"
	

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

















