from Tkinter import *

case = [[(10,10),(0,0),(9,9),(2,3,5,5),(8,8,2,1)],
[(20,20),(19,3),(2,18),(5,5,10,10),(1,2,4,1)],
[(20,20),(0,0),(19,19),(17,10,2,1),(14,4,5,2),(3,16,10,2),(13,7,5,3),(15,15,3,3)],
[(10,10),(0,0),(9,5),(3,0,2,7),(6,0,4,4),(6,6,2,4)],
[(10,10),(0,0),(9,9),(3,0,2,7),(6,0,4,4),(6,6,2,4)],
[(20,20),(0,0),(19,13),(4,0,4,16),(12,4,2,16),(16,8,4,4)]]

def startInput():
	#dimension = input("Dimension ")
	#start = input("Youre Start Point: ")
	#end = input("Youre End Point: ")
	scenario = input("type scenario: ")
	tempScenario = case[scenario]
	#board = Board(dimension,start,end)
	board = Board(tempScenario[0],tempScenario[1],tempScenario[2])
	allBoards.append(board)
	
	for obstacles in tempScenario[3:]:
		tempObstacle = Obstacle(obstacles)
		allObstacles.append(tempObstacle)

	#inValue = 1
	#while (inValue != 0):
	#	inValue =  input("Type grid for obstacles and 0 for finish ")
	#	if inValue != 0:
	#		tempObstacle = Obstacle(inValue)
	#		allObstacles.append(tempObstacle)
			

	board.createBoard()
	addObstacles(board)
	board.printBoard()
	#drawBoard(board)

allObstacles = []
allBoards = []

class Board:

	def __init__(self, dim, start,finish):
		self.dim = dim
		#self.start = (start[0], dim[1] - start[1] - 1) 
		#self.finish = (finish[0], dim[1] - finish[1] - 1)
		self.start = (dim[1] - start[1] - 1,start[0]) 
		self.finish = (dim[1] - finish[1] - 1,finish[0])
		self.board = []


	def getStartPoint(self):
		return self.start
	def getXdim(self):
		return self.dim[0]

	def getYdim(self):
		return self.dim[1]

	def getFinish(self):
		return self.finish

	def isNotObstacle(self,x,y):
		if (self.board[x][y] == '*'):
			return False
		else:
			return True

	def createBoard (self):
		for y in range(self.getYdim()):
			tempList = []
			for x in range(self.getXdim()):
				tempList.append('-')

			self.board.append(tempList)

		self.board[self.start[0]][self.start[1]] = 'S'
		self.board[self.finish[0]][self.finish[1]] = 'F'
		



	def printBoard(self):
		for x in self.board:
			print x 

	def getBoard(self):
		return self.board




class Obstacle:


	def __init__(self, properties):
		self.properties = properties

	def getX(self):
		return self.properties[0]
	def getY(self):
		return self.properties[1]
	def getLength(self):
		return self.properties[2]
	def getHeight(self):
		return self.properties[3] 




def addObstacles(board):
	numOfObstacles = len(allObstacles)
	counter = 0
	while counter < numOfObstacles:
		obstacle = allObstacles[counter]
		x = obstacle.getX()
		y = board.getYdim() - obstacle.getY() - 1
		height = obstacle.getHeight()
		length = obstacle.getLength()
		for obsHeight in range(height):
			for obsLength in range(length):
				board.board[y-obsHeight][x + obsLength] = '*' 

		counter += 1




def drawBoard(board):

	root = Tk()
	if board.getXdim() % 2 == 0:
		width = board.getXdim()/2*100
	else:
		width = board.getXdim()/2*100+50
	if board.getYdim() % 2 == 0:
		height = board.getYdim()/2*100
	else:
		height = board.getYdim()/2*100+50
	canvas = Canvas(root, width= width,height=height)
	canvas.pack()
	i = 48
	j = 1
	for x in range(board.getYdim()):
		for y in range(board.getXdim()):
			if (board.getYdim()> 15 or board.getXdim() > 15):
				i = 24
				j = 2
			gridx = width/board.getXdim()/j*y 
			gridy = height/board.getYdim()/j*x 
			if board.getBoard()[x][y] == '-':
				canvas.create_rectangle(gridx+2,gridy + 2, gridx+i, gridy+i, fill="mint cream")
			elif board.getBoard()[x][y] == 'S':
				canvas.create_rectangle(gridx+2,gridy + 2, gridx+i, gridy+i, fill="lime green")
			elif board.getBoard()[x][y] == 'F':
				canvas.create_rectangle(gridx+2,gridy + 2, gridx+i, gridy+i, fill="red")
			elif board.getBoard()[x][y] == '*':
				canvas.create_rectangle(gridx+2,gridy + 2, gridx+i, gridy+i, fill="grey")
			elif board.getBoard()[x][y] == '>':
				canvas.create_rectangle(gridx+2,gridy + 2, gridx+i, gridy+i, fill="light blue")
			elif board.getBoard()[x][y] == 'g':
				canvas.create_rectangle(gridx+2,gridy + 2, gridx+i, gridy+i, fill="sandy brown")

	#for i in range(board.getXdim()):
	#    canvas.create_line(50 * i, 0, 50 * i, 500)
	#for i in range(board.getYdim()):    
	#	canvas.create_line(0, 50 * i, 500, 50 * i)
	
	
			


	#root.update()
	#root.update_idletasks()
	#root.update()			
	root.mainloop()


def updateBoard(board):
	return None


	
def getBoard():
	return allBoards[0]
	
























