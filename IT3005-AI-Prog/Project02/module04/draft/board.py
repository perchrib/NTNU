import random
from move_helper import move as MOVE
from move_helper import valid_move
from tile import Tile

directions = {1:'UP',
			  2:'DOWN',
			  3:'LEFT',
			  4:'RIGHT'}
EMPTY = 0
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
class Board:
	def __init__(self,dimension):
		self.dimension = dimension
		self.board = [[EMPTY for x in range(dimension)] for y in range(dimension)]
		self.valid_move = None
	"""INTERNAL FUNC called by set_new_tile"""
	def get_ready_places(self):
		indexes = []
		for row_index in range(self.dimension):
			for col_index in range(self.dimension):
				if self.board[row_index][col_index] == EMPTY:
					indexes.append((row_index,col_index))
		return indexes

	def set_new_tile(self,tile):
		options = self.get_ready_places()
		random_item = random.choice(options)
		x = random_item[0]
		y = random_item[1]
		self.board[x][y] = tile
		tile.pos = str(x) + '-' + str(y)

	"""Move all tiles which defines by the game rules"""
	def move(self,move):
		self.board = MOVE(self.board,move)
		self.valid_move = valid_move()

	def print_board(self):
		print "--------------------------"
		for r in range(self.dimension):
			for i in range(self.dimension):
				if self.board[r][i] != EMPTY:
					print " | " , self.board[r][i].value,
				elif self.board[r][i] == EMPTY:
					print " | " , EMPTY,

				if i == self.dimension-1:
					print " | "

			print "--------------------------"

	def has_lost(self):
		full_board = True
		for row in self.board:
			for tile in row:
				if tile == EMPTY:
					full_board = False
					break
			break
		if full_board and self.valid_move == False:
			return True
		return False
		
	def update_tile_pos(self):
		for x in range(self.dimension):
			for y in range(self.dimension):
				tile = self.board[x][y]
				if tile is EMPTY:
					continue
				else:
					self.board[x][y].pos = str(x)+"-"+ str(y) 