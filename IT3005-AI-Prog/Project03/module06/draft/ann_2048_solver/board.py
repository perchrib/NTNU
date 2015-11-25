import random
from move_helper import move as MOVE
from move_helper import valid_move
from tile import Tile

EMPTY = 0
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
MOVES = [UP,DOWN,LEFT,RIGHT]
class Board:
	def __init__(self,dimension=4):
		self.dimension = dimension
		self.board = [[EMPTY for x in range(dimension)] for y in range(dimension)]
		self.valid_move = None
		self.all_moves = []
		self.prob = None
		self.ai_move = None
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
		if options:
			random_item = random.choice(options)
			x = random_item[0]
			y = random_item[1]
			self.board[x][y] = tile
			tile.pos = str(x) + '-' + str(y)

	"""Move all tiles which defines by the game rules"""
	def move(self,move):
		self.board = MOVE(self.board,move)
		self.valid_move = valid_move()

	def get_highest_tile(self):
		value = 0
		for row_index in range(self.dimension):
			for col_index in range(self.dimension):
				
				tile = self.board[row_index][col_index]
				if self.board[row_index][col_index] == EMPTY:
					pass
				else:
					if value < tile.value:
						value = tile.value
		return value


	# def print_board(self):
	# 	print "--------------------------"
	# 	for r in range(self.dimension):
	# 		for i in range(self.dimension):
	# 			if self.board[r][i] != EMPTY:
	# 				print " | " , self.board[r][i].value,
	# 			elif self.board[r][i] == EMPTY:
	# 				print " | " , EMPTY,

	# 			if i == self.dimension-1:
	# 				print " | "
	# 		print "--------------------------"

	def has_lost(self):
		full_board = True
		for row in self.board:
			for tile in row:
				if tile == EMPTY:
					return False
		for move in MOVES:
			temp = MOVE(self.board,move)
			if valid_move():
				return False
		return True
		
	def update_tile_pos(self):
		for x in range(self.dimension):
			for y in range(self.dimension):
				tile = self.board[x][y]
				if tile is EMPTY:
					continue
				else:
					self.board[x][y].pos = str(x)+"-"+ str(y) 