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
		
	def mainLoop(self):
		while self.openStore:
			if not self.openStore:
				#print "Fail"
				break
			
			#print "QUEUE: ", self.openStore.string()	
			currentNode = self.openStore.pop()
			currentNode.status = 'CLOSED'
			self.closedStore.add(currentNode)
			#print "Current Node State: ",currentNode.state,"   Current Node Heuristic: ", currentNode.h

			self.draw_graph(currentNode)

			neighbours = self.generateNeighbours(currentNode)
			currentNode.printGraph()
			for node in neighbours:				
				#print "INDEX: ", node.assuptionVertex.index		
				revise = self.csp.rerun(node.assuptionVertex)
				self.csp.graph = node.graph 
				#print "Revise: ", revise

				#if not node in self.openStore:
					#if not node in self.openStore or not node in self.closedStore :
					#	node.status = 'OPEN'
					#	self.openStore.add(node)
				if not revise:
					self.closedStore.add(node)
					continue
		
				if self.csp.isFinish():
					# halla
					#print "Solution found"

					#print "closedStore: ", len(self.closedStore)
					#print "openStore: " ,len(self.openStore)				
					return 
				node.f = node.heuristic()

				#print "LENGTH: " ,len(self.openStore)
				self.openStore.add(node) 

				# currentNode.kids.append(node)
				# if not node.status == 'OPEN' and not node.status == 'CLOSED':					
	
				# 	self.attachAndEval(node,currentNode)
				# 	node.status = 'OPEN'
				# 	self.openStore.add(node)

				# elif currentNode.g + self.arc_cost(currentNode,node) < node.g:
				# 	self.attachAndEval(node,currentNode)
				# 	print"DENNE"
				# 	if node == 'CLOSED':
				# 		improve_path(node)
			
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

	def find_first_expandable(self,node):
		for v in node.graph:
			if v.domain:
				if len(v.domain) > 1:
					return v
		return None

		# t = 100
		# minVertex = None
		# for v in node.graph:
		# 	minT = len(v.neighbour)
		# 	if minT < t and len(v.domain) > 1:
		# 		t = len(v.neighbour)
		# 		minVertex = v 
		#print "MINIMUM: ", minVertex.index
		#return minVertex
	def draw_graph(self,currentNode):
		for v in self.csp.graph:
		#print v.domain
			if len(v.domain) == 1:
				color = v.domain
				self.csp.gui.canvas.itemconfig('a'+str(v.index), fill=color)

				
		











					
					




