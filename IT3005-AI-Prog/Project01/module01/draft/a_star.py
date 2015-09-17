import world
from heapq import heappush, heappop
from math import sqrt

world.startInput()
board = world.getBoard()
#print board.getStartPoint()

OPEN = 0
CLOSED = 1

debug = True

class Node:
	distanceWalked = 0
	finishPoint = board.getFinish()
	
	def __init__(self,state,status,parent,kids):
		self.state = state
		self.status = status
		self.parent = parent
		self.kids = kids
		self.g = 0
		self.f = 0
		self.h = sqrt(((self.state[0]-Node.finishPoint[0])**2) + ((self.state[1]-Node.finishPoint[1])**2))
	

	def heuristic(self):
		return sqrt(((self.state[0]-Node.finishPoint[0])**2) + (self.state[1]-Node.finishPoint[1]))
	
	def isStart(self):
		return board.getStartPoint() == self.state

	def isEndPoint(self):
		return board.getFinish() == self.state

def findPath(node):
	route = []
	temp_node = node
	while not temp_node is None:
		route.append(temp_node)
		temp_node = temp_node.parent


	return route[1:-1]



def deleteAlreadyClosedNodesFromGeneratedSuccessors(successors,queue):
	modifiedList = successors
	for s in successors:
		for c in queue:
			if (cmp(s.state,c.state) == 0):
				modifiedList.remove(s)

	return modifiedList




def a_star():
	openQueue = []

	
	closedQueue = []
	n0 = Node(board.getStartPoint(),OPEN,None,[])
	heappush(openQueue,(n0.f,n0))

	openstack = [n0]
	##AGENDA LOOP##
	iteration = 0
	while (openstack or openQueue):
		print "ITERATIONS: ", iteration
		if (not openQueue):
			print "Failed"

		a_star = True
		DFS = False
		BFS = False
		
		if (a_star):
			tNode = heappop(openQueue) ##check!!!
			xNode = tNode[1]
		
		elif (DFS):
			xNode = openstack.pop()

		elif (BFS):
			xNode = openstack.pop(0)

		xNode.status = CLOSED
		#board.board[xNode.state[0]][xNode.state[1]] = '>'
		#world.updateBoard(board)
		
		#if(not xNode in closedQueue):
		#	heappush(closedQueue,xNode)
		q = True
		
		for s in closedQueue:
			print "ClosedQueue: ", s.state
			if(cmp(s.state,xNode.state)== 0):

				q = False
		if(q == True):
			heappush(closedQueue,xNode)
			if not (xNode.isStart() or xNode.isEndPoint()):
				board.board[xNode.state[0]][xNode.state[1]] ='g'
		#print "Open ", openQueue, "Closed ", closedQueue
		print "\n"
		print "Current NODE : ", xNode.state
		print "\n"
		if (cmp(xNode.state, Node.finishPoint) == 0):
			print "Finish"
			path = findPath(xNode)
			for r in path:
				print "Step: ", r.state
				board.board[r.state[0]][r.state[1]] = '>'
			board.printBoard()
			world.drawBoard(board)
			print "Length Open: ", len(openQueue)
			print "Length Closed: ", len(closedQueue)
			break



		tempSuccessors = generateAllSuccsessors(xNode)
		
		
		successors = deleteAlreadyClosedNodesFromGeneratedSuccessors(tempSuccessors,closedQueue)
		print "SUCCCCCCC:::: ", len(successors)
		for success in successors:
			for e in openQueue:
				openNode = e[1]
				if (cmp(success.state,openNode.state) == 0):
					success = openNode
					print "\n Already in OPEN QUEUE", success.state ,"  Status: ", success.status
					#print "STATUS EARLIER::::::: ", 
					## Mybe delete this node from openqueue

			xNode.kids.append(success)
			if ((not success.status == CLOSED) and (not success.status == OPEN)):
				attachAndEval(success,xNode)
				success.status = OPEN
				print "Hereeeeee: >>>> " , success.f
				heappush(openQueue,(success.f,success))
				openstack.append(success) ## This is for DFS/BFS SEARCH
				print "generated next step: ", success.state, "next step STATUS: ", success.status
			elif (xNode.g + 1 < success.g):
				print "HERE TRIGGER"
				attachAndEval(success,xNode)
				if (success == CLOSED):
					propPathImprove(success)
		iteration += 1
					
def propPathImprove(parent):
	for child in parent.kids:
		if(parent.g + 1 < child.g):
			child.parent = parent
			child.g = parent.g + 1
			child.f = child.g + child.h
			propPathImprove(child)



def attachAndEval(cNode,pNode):
	cNode.parent = pNode
	cNode.g = pNode.g + 1
	cNode.f = cNode.g + cNode.h
	print "f(c): " , cNode.f, "state: " , cNode.state, "h(c): " , cNode.h

def generateAllSuccsessors(nodeX):
	directions = 4
	dx = [1,0,-1,0]
	dy = [0,1,0,-1]
	successors = []
	for i in range(4):
		stepX = dx[i] + nodeX.state[0]
		stepY = dy[i] + nodeX.state[1]
		state = (stepX,stepY)
		#print "state successors: ", state 
		if ((stepX >= 0 and stepX < board.getXdim()) and (stepY >= 0 and stepY < board.getYdim()) and board.isNotObstacle(stepX,stepY)): 
			
			successNode = Node(state,None,None,[])
			successors.append(successNode)
			print "SUCSESSOR: ", state

	return successors




a_star()



















