from search_queue import SearchQueue
import itertools


class A_star():
	def __init__(self, board, gui, searchMethod,speed):
		self.speed = speed
		self.gui = gui
			
		self.board = board
		self.openStore = SearchQueue(searchMethod)
		self.closedStore = SearchQueue(searchMethod)

		self.board.startNode.f = self.board.startNode.g + self.board.startNode.h
		#print "finishNode", board.finishNode.state , "is Finish: ", board.finishNode.isFinish
		self.openStore.add(board.startNode)
		self.path = []
		
	def mainLoop(self):
		while self.openStore:
			if not self.openStore:
				print "Fail"
				break
			#print "\n################################\n"
			#self.openStore.string()
			currentNode = self.openStore.pop()
			currentNode.status = 'CLOSED'
			self.closedStore.add(currentNode)			
			
			#print "Current Node State: ",currentNode.state,"   Current Node Heuristic: ", currentNode.h

			if self.gui:
				self.drawPath(currentNode)
				self.rase()
				if not currentNode.isStart and not currentNode.isFinish:
					self.gui.canvas.itemconfig(currentNode.ID, fill="chocolate3")
				self.gui.after(self.speed,self.gui.update())
			
			if currentNode.isFinish:
				print "Solution found"
				if self.gui:
					self.drawPath(currentNode)

				#print "closedStore: ", len(self.closedStore)
				#print "openStore: " ,len(self.openStore)				
				break

			currentNode.generateNeighbours()
			for node in currentNode.neighbours:
				#if not node in self.openStore:
					#if not node in self.openStore or not node in self.closedStore :
					#	node.status = 'OPEN'
					#	self.openStore.add(node)
				currentNode.kids.append(node)
				if not node.status == 'OPEN' and not node.status == 'CLOSED':					
					if not node.isFinish:
						if self.gui:
							self.gui.canvas.itemconfig(node.ID, fill="sandy brown")
							self.gui.after(self.speed,self.gui.update())
					self.attachAndEval(node,currentNode)
					node.status = 'OPEN'
					self.openStore.add(node)

				elif currentNode.g + 1 < node.g:
					attachAndEval(node,currentNode)
					print"DENNE"
					if node == 'CLOSED':
						improve_path(node)



	def attachAndEval(self,node,currentNode):
		node.parent = currentNode
		node.g = currentNode.g + 1
		node.f = node.g + node.h

	def improve_path(node):
		for kid in node.kids:
			kid.parent = node
			kid.g = node.g + 1
			kid.f = kid.c + kid.h

	def findPath(self, node):
		route = []
		temp_node = node
		while not temp_node is None:
			route.append(temp_node)
			temp_node = temp_node.parent

		route.reverse()
		return route[1:-1]

	def drawPath(self,node):

		path = self.findPath(node)
		self.path = path 
		for n in path:
			if not n.isStart or not n.isFinish:
				self.gui.canvas.itemconfig(n.ID, fill="light blue")
				self.gui.after(0,self.gui.update())

	def rase(self):
		if self.path:
			for n in self.path:
				if not n.isStart or not n.isFinish:
					self.gui.canvas.itemconfig(n.ID, fill="mint cream")
					#self.gui.after(0,self.gui.update())







					
					




