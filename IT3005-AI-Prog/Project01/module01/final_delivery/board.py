import Tkinter as tk
from math import sqrt
from a_star import A_star


case = [[(10,10),(0,0),(9,9),(2,3,5,5),(8,8,2,1)],
[(20,20),(19,3),(2,18),(5,5,10,10),(1,2,4,1)],
[(20,20),(0,0),(19,19),(17,10,2,1),(14,4,5,2),(3,16,10,2),(13,7,5,3),(15,15,3,3)],
[(10,10),(0,0),(9,5),(3,0,2,7),(6,0,4,4),(6,6,2,4)],
[(10,10),(0,0),(9,9),(3,0,2,7),(6,0,4,4),(6,6,2,4)],
[(20,20),(0,0),(19,13),(4,0,4,16),(12,4,2,16),(16,8,4,4)],
[(20,20,),(0,0),(19,19)]]



class Board:
	def __init__(self, dim, start, finish):
		self.dim = dim
		self.start = (dim[1] - start[1] - 1,start[0]) 
		self.finish = (dim[1] - finish[1] - 1,finish[0])
		self.board = []
		self.Xdim = dim[0]
		self.Ydim = dim[1]
		
		self.startNode = None
		self.finishNode = None

	def createBoard(self):
		for y in range(self.Ydim):
			tempList = []
			for x in range(self.Xdim):
				node = Node((x,y),self)
				tempList.append(node)
			self.board.append(tempList)

		self.board[self.start[0]][self.start[1]].isStart = True
		self.startNode = self.board[self.start[0]][self.start[1]]
		
		self.board[self.finish[0]][self.finish[1]].isFinish = True
		self.finishNode = self.board[self.finish[0]][self.finish[1]]

class Node:

	generateID = 0
		
		#sqrt(((self.state[0]-Node.finishPoint[0])**2) + (self.state[1]-Node.finishPoint[1]))
	
	def __init__(self,state,board):
		self.state = state
		self.board = board
		self.status = None
		self.parent = None
		self.kids = []
		self.g = 0
		self.f = 0
		self.h = sqrt(((self.state[0]-board.finish[1])**2) + ((self.state[1]-board.finish[0])**2))
		self.neighbours = []
		self.isObstacle = False
		self.isStart = False
		self.isFinish = False
		self.ID = 'a' + str(Node.generateID)
		Node.generateID += 1

	def __lt__(self,other):
		return self.h < other.h

	def isEmpty(self):
		if self.isObstacle == True or self.isStart == True or self.isFinish == True:
			return False
		else:
			return True

	def generateNeighbours(self):
		if not self.neighbours:
			dx = [1,0,-1,0]
			dy = [0,1,0,-1]

			for i in range(4):
				stepX = dx[i] + self.state[0]
				stepY = dy[i] + self.state[1]
				stateNeighbour = (stepX,stepY)
				if ((stepX >= 0 and stepX < self.board.Xdim) and (stepY >= 0 and stepY < self.board.Ydim)):
					neighbour = self.board.board[stepY][stepX]
					if not neighbour.isObstacle:
						self.neighbours.append(neighbour)
		elif self.neighbours:
			print "Already GENERATED!"
						







def addObstacles(board, allObstacles):
	numOfObstacles = len(allObstacles)
	for obstacle in allObstacles:
		x = obstacle[0]
		y = board.Ydim - obstacle[1] - 1
		length = obstacle[2]
		height = obstacle[3]
		for obsHeight in range(height):
			for obsLength in range(length):
				board.board[y-obsHeight][x + obsLength].isObstacle = True


class Draw(tk.Tk):
	def __init__(self,board):
		tk.Tk.__init__(self)
		if (board.Xdim % 2 == 0):
			self.width = board.Xdim/2*100
		else:
			self.width = board.Xdim/2*100+50
		if (board.Ydim % 2 == 0):
			self.height = board.Ydim/2*100
		else:
			self.height = board.Ydim/2*100+50
		
		self.canvas = tk.Canvas(self, width= self.width,height=self.height)
		self.canvas.pack()
		self.light_on = True
		i = 48
		j = 1
		for x in range(board.Ydim):
			for y in range(board.Xdim):
				if (board.Ydim > 15 or board.Xdim > 15):
					i = 24
					j = 2
				gridx = self.width/board.Xdim/j*y 
				gridy = self.height/board.Ydim/j*x 
				
				node = board.board[x][y] 
				tag = node.ID
				
				if node.isEmpty():
					self.canvas.create_rectangle(gridx+2,gridy + 2, gridx+i, gridy+i, fill="mint cream",tags=tag)
				elif node.isStart:
					self.canvas.create_rectangle(gridx+2,gridy + 2, gridx+i, gridy+i, fill="lime green",tags=tag)
				elif node.isFinish:
					self.canvas.create_rectangle(gridx+2,gridy + 2, gridx+i, gridy+i, fill="red",tags=tag)
				elif node.isObstacle:
					self.canvas.create_rectangle(gridx+2,gridy + 2, gridx+i, gridy+i, fill="grey",tags=tag)
				# elif board.getBoard()[x][y] == '>':
				# 	self.canvas.create_rectangle(gridx+2,gridy + 2, gridx+i, gridy+i, fill="light blue",tags=tag)
				# elif board.getBoard()[x][y] == 'g':
				# 	self.canvas.create_rectangle(gridx+2,gridy + 2, gridx+i, gridy+i, fill="sandy brown",tags=tag)
		

	

def main():
	scenario = input("type scenario: ")
	tempScenario = case[scenario]
	allObstacles = []
	
	for obstacles in tempScenario[3:]:
		allObstacles.append(obstacles)

	board = Board(tempScenario[0],tempScenario[1],tempScenario[2])
	board.createBoard()
	addObstacles(board,allObstacles)
	#drawBoard(board)

	draw = Draw(board)
	a_star = A_star(board,draw,'astar')
	a_star.mainLoop()
	
	draw.mainloop()

main()

