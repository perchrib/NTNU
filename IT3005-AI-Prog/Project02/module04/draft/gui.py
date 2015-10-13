import Tkinter as tk
from tile import Tile
EMPTY = 0
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

class Draw(tk.Tk):
	def __init__(self,dimension,board):
		tk.Tk.__init__(self)
		self.dimension = dimension
		node_size = (self.winfo_screenheight()-100)/self.dimension
		self.width = self.winfo_screenheight()-100
		self.height = self.winfo_screenheight()-100
		self.canvas = tk.Canvas(self, width= self.width,height=self.height)
		self.board = board
		self.bind("<Key>", self.key_pressed)
		self.canvas.pack()

		
		for x in range(self.dimension):
			for y in range(self.dimension):
				gridx = node_size*y+3
				gridy = node_size*x+3
				gridx2 = gridx + node_size -2
				gridy2 = gridy + node_size -2
				gx2 = gridx + (node_size -2)/2
				gy2 = gridy + (node_size -2)/2
				"""c for color, i for integer"""
				coltag = 'c'+ str(x)+"-"+ str(y)
				inttag = 'i'+ str(x)+"-"+ str(y)
				self.canvas.create_rectangle(gridx,gridy, gridx2, gridy2, fill="mint cream",tags=coltag)
				self.canvas.create_text(gx2,gy2,text="",font=("Helvetica",70),tags=inttag)

	def key_pressed(self,event):
		if event.keysym == 'Up':
			self.board.move(UP)
		elif event.keysym == 'Down':
			self.board.move(DOWN)
		elif event.keysym == 'Left':
			self.board.move(LEFT)
		elif event.keysym == 'Right':
			self.board.move(RIGHT)
		self.update_board()
		#self.board.print_board()
		new_tile = Tile(None)
		new_tile.set_start_value()
		self.board.set_new_tile(new_tile)
		self.update_tile(new_tile,250)
		self.board.print_board()
		

	def update_tile(self,tile,delay):
		print "TILE : ", tile.pos
		tile.color = self.getColor(tile.value)
		self.after(delay)
		self.canvas.itemconfig('c'+tile.pos,fill=tile.color)
		self.canvas.itemconfig('i'+tile.pos,text=str(tile.value))
		self.after(5,self.update())

	def update_board(self):
		self.board.update_tile_pos()
		for x in range(self.dimension):
			for y in range(self.dimension):
				if self.board.board[x][y] == EMPTY:
					self.canvas.itemconfig('c'+ str(x)+"-"+ str(y),fill='mint cream')
					self.canvas.itemconfig('i'+ str(x)+"-"+ str(y),text='')
				else:
					"""i INTEGER, c COLOR"""
					tile = self.board.board[x][y]
					tile.color = self.getColor(tile.value)
					self.canvas.itemconfig('c'+tile.pos,fill=tile.color)
					self.canvas.itemconfig('i'+tile.pos,text=str(tile.value))
		self.after(5,self.update())

	def log_2(self,number):
		if number == 1:
			return 0
		else:
			return self.log_2(number/2) + 1

	def getColor(self,tile_num):
		key = self.log_2(tile_num)
		colors = {1:'#eee4da',
				  2:'#ede0c8',
				  3:'#f2b179',
				  4:'#f59563',
				  5:'#f67c5f',
				  6:'#f65e3b',
				  7:'#edcf72',
				  8:'#edcc61',
				  9:'#edc850',
				  10:'#edc53f',
				  11:'#edc22e',
				  12:'#3c3a32'}
		return colors[key]