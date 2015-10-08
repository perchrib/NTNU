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

	"""This is the main Loop of ASTAR"""
	def mainLoop(self):
		while self.openStore:
			if not self.openStore:
				print "Fail"
				break
				
			currentNode = self.openStore.pop()
			currentNode.status = 'CLOSED'
			self.closedStore.add(currentNode)
			neighbours = self.generateNeighbours(currentNode)
			for node in neighbours:				
				"""Calling on gac rerun to filter domains"""
				revise = self.csp.initialice(node.variables)

				self.csp.variables = node.variables
				if not revise:
					self.closedStore.add(node)
					continue

				if self.csp.isFinish():

					print "OPEN ", len(self.openStore)
					print "CLOSED ", len(self.closedStore)
				
					return
 
				node.f = node.heuristic()
				self.openStore.add(node) 
			

	
	"""Genereate other neighbour state, try to set the variable with more than one in its domain,
	trying out every domain once. return all combination with one domain. setting also the variable as an 
	assuption-Variable that will run in gac rerun"""
	def generateNeighbours(self,original):
		neighbours = []
		temp_node = self.find_first_expandable(original)
		#print "Returned: " , temp_node.index
		if temp_node is not None:
			for permutation in temp_node.domain:
				successor = copy.deepcopy(original)
				successor.variables[temp_node.index].domain = [permutation]
				successor.assuptionVariable = successor.variables[temp_node.index]
				
				neighbours.append(successor)
		return neighbours

	"""Finds the first domain with more than one and return that variable othervise None """
	def find_first_expandable(self,node):
		for key in node.variables:
			variable = node.variables[key]
			if variable.domain:
				if len(variable.domain) > 1:
					return variable
		
		return None


				
		











					
					




