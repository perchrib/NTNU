from Tkinter import *



def startInput():
	dimension = input("Dimension ")
	start = input("Youre Start Point: ")
	end = input("Youre End Point: ")
	board = Board(dimension,start,end)
	#board = Board((10,10),(1,1),(9,9))
	allBoards.append(board)
	inValue = 1
	while (inValue != 0):
		inValue =  input("Type grid for obstacles and 0 for finish ")
		if inValue != 0:
			tempObstacle = Obstacle(inValue)
			allObstacles.append(tempObstacle)
			

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

	#for i in range(board.getXdim()):
	#    canvas.create_line(50 * i, 0, 50 * i, 500)
	#for i in range(board.getYdim()):    
	#	canvas.create_line(0, 50 * i, 500, 50 * i)
	

	for x in range(board.getYdim()):
		for y in range(board.getXdim()):
			gridx = width/board.getXdim()*y 
			gridy = height/board.getYdim()*x 
			if board.getBoard()[x][y] == '-':
				canvas.create_rectangle(gridx+2,gridy + 2, gridx+48, gridy+48, fill="mint cream")
			elif board.getBoard()[x][y] == 'S':
				canvas.create_rectangle(gridx+2,gridy + 2, gridx+48, gridy+48, fill="lime green")
			elif board.getBoard()[x][y] == 'F':
				canvas.create_rectangle(gridx+2,gridy + 2, gridx+48, gridy+48, fill="red")
			elif board.getBoard()[x][y] == '*':
				canvas.create_rectangle(gridx+2,gridy + 2, gridx+48, gridy+48, fill="grey")
			elif board.getBoard()[x][y] == '>':
				canvas.create_rectangle(gridx+2,gridy + 2, gridx+48, gridy+48, fill="light blue")
			


	root.mainloop()
	
def getBoard():
	return allBoards[0]
	
























