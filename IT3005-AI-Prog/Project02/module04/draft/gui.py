import Tkinter as tk
from tile import Tile
from board import Board
from minimax import Minimax
EMPTY = 0
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

class Draw(tk.Tk):
	def __init__(self,dimension):
		tk.Tk.__init__(self)
		self.dimension = dimension
		node_size = (self.winfo_screenheight()-150)/self.dimension #100 Standard
		self.width = self.winfo_screenheight()-150
		self.height = self.winfo_screenheight()-100
		self.board = None
		"""CREATE """
		self.wm_title("---2048---")
		self.topframe = tk.Frame(self)
		self.canvas = tk.Canvas(self, width= self.width,height=self.height)
		self.play_button = tk.Button(self.topframe, text="PLAY",width=10,height=5)
		self.undo_button = tk.Button(self.topframe, text="UNDO",width=10,height=5)
		self.ai_button = tk.Button(self.topframe, text="AI-SOLVER",width=10,height=5)
		"""PACK"""
		self.topframe.pack(side='top') 
		self.ai_button.pack(padx=2,side='right')
		self.undo_button.pack(padx=2,side='right')
		self.play_button.pack(padx=2,side='right')
		self.canvas.pack()
		"""LISTENERS"""
		self.play_button.bind('<Button-1>',self.play)
		self.ai_button.bind('<Button-1>',self.ai)
		self.undo_button.bind('<Button-1>',self.undo)
		
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
		
		if self.board.valid_move:
			self.update_board()
			self.board.all_moves.append(self.board.board)
			new_tile = Tile(None)
			new_tile.set_start_value()
			self.board.set_new_tile(new_tile)
			self.update_tile(new_tile,250)
			#self.board.print_board()
		elif self.board.has_lost():
			print "You have lost "
			self.game_ended()		
		elif self.board.valid_move == False:
			print "Try another direction!"

	


	def play(self,event):
		self.new_game()
		print "PLAY"
		self.bind("<Key>", self.key_pressed)
	def ai(self,event):
		print "AI"
		self.new_game()
		ai = Minimax()
		while not self.board.has_lost():
			ai.state = self.board
			move = ai.get_move()
			self.board.move(move)
			if self.board.valid_move:
				new_tile = Tile(None)
				new_tile.set_start_value()
				self.board.set_new_tile(new_tile)
				self.update_board()
			else:
				self.update_board()
				break
		self.game_ended()
		#self.update_board()
	def undo(self,event):
		if len(self.board.all_moves) > 0:
			if len(self.board.all_moves) == 1:
				self.board.board = self.board.all_moves[0]
			else:
				self.board.board = self.board.all_moves.pop()
			self.update_board()
			#self.board.print_board()
			print "UNDO"

	def update_tile(self,tile,delay):
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

	def game_ended(self):
		size = 15
		toplevel = tk.Toplevel()
		label1 = tk.Label(toplevel, text="YOU LOOSE!",font=("Helvetica",size), height=0, width=50)
		label1.pack()
		label2 = tk.Label(toplevel, text="LOOSER!",font=("Helvetica",size), height=0, width=50)
		label2.pack()
		label3 = tk.Label(toplevel, text="PLAY AGAIN",font=("Helvetica",size), height=0, width=50)
		label3.pack()
		b1 = tk.Button(toplevel, text="NEW GAME",font=("Helvetica",size),width=20, command=self.new_game)
		b1.pack(padx=10,side='left')
		b2 = tk.Button(toplevel, text="Quit", font=("Helvetica",size),width=20, command=toplevel.destroy)
		b2.pack(padx=10,side='left')
	
	def new_game(self):
		self.board = Board(self.dimension)
		tile = Tile(None)
		tile.set_start_value()
		self.board.set_new_tile(tile)
		self.board.all_moves.append(self.board.board)
		self.update_board()

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