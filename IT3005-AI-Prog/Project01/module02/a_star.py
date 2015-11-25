from search_queue import SearchQueue
from math import sqrt
import copy
#import itertools


class A_star():
	def __init__(self,searchMethod,startNode,csp):
		self.cost = 1
		self.openStore = SearchQueue(searchMethod)
		self.closedStore = SearchQueue(searchMethod)
		self.startNode = startNode
		self.startNode.f = self.startNode.g + self.startNode.heuristic()
		self.openStore.add(self.startNode)
		self.path = []
		self.csp = csp
		self.generator = []
		self.gui = csp.gui
	
	"""This is the main Loop of ASTAR"""
	def mainLoop(self):
		while self.openStore:
			if not self.openStore:
				print "Fail"
				break
	
			currentNode = self.openStore.pop()
			currentNode.status = 'CLOSED'
			self.closedStore.add(currentNode)

			self.draw_graph(currentNode)

			neighbours = self.generateNeighbours(currentNode)
			currentNode.printGraph()
			for node in neighbours:	
				"""Calling on gac rerun to filter domains"""			
				revise = self.csp.rerun(node.assuptionVertex)
				self.csp.graph = node.graph 

				if not revise:
					self.closedStore.add(node)
					continue
		
				if self.csp.isFinish():
					print "OPEN ", len(self.openStore)
					print "CLOSED ", len(self.closedStore)
				
					return 
				node.f = node.heuristic()
				self.openStore.add(node) 			
			self.csp.gui.after(5,self.gui.update())
			
	def arc_cost(self,currentNode,neighbour):
		return self.cost * 1 #sqrt(((currentNode.state[0]-neighbour.state[0])**2) + ((currentNode.state[1]-neighbour.state[1])**2)) * self.cost


	def attachAndEval(self,node,currentNode):
		node.parent = currentNode
		node.g = currentNode.g + self.arc_cost(currentNode,node)
		node.f = node.g + node.heuristic()

	def improve_path(currentNode):
		for kid in currentNode.kids:
			kid.parent = currentNode
			kid.g = currentNode.g + self.arc_cost(currentNode,kid)
			kid.f = kid.c + kid.heuristic()
	"""Genereate other neighbour state, try to set the variable with more than one in its domain,
	trying out every domain once. return all combination with one domain. setting also the variable as an 
	assuption-Variable that will run in gac rerun"""
	def generateNeighbours(self,original):
		neighbours = []
		temp_node = self.find_first_expandable(original)
		if temp_node is not None:
			for color in temp_node.domain:
				successor = copy.deepcopy(original)
				successor.graph[temp_node.index].domain = [color]
				successor.assuptionVertex = successor.graph[temp_node.index]
				neighbours.append(successor)
		return neighbours

	"""Finds the first domain with more than one and return that variable othervise None """
	def find_first_expandable(self,node):
		for v in node.graph:
			if v.domain:
				if len(v.domain) > 1:
					return v
		return None

	def draw_graph(self,currentNode):
		for v in self.csp.graph:
			if len(v.domain) == 1:
				color = v.domain
				self.csp.gui.canvas.itemconfig('a'+str(v.index), fill=color)

				
		











					
					




