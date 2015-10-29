from move_helper import move as MOVE
from move_helper import valid_move
from tile import Tile
import heuristics
import random
import copy
from sample_boards import get_sample

EMPTY = 0
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
#MOVES = [UP,DOWN,LEFT,RIGHT]
MOVES = [LEFT,UP,RIGHT,DOWN]
class Minimax:
	def __init__(self):
		self.state = None
		self.move = None


	def minimax(self,node,depth,my_turn):
		if depth == 0:
			return heuristics.corner(node.board) #+ heuristics.top_row(node.board)
		if my_turn:
			alpha = float('-inf')
			children = self.generate_children(node)
			for child in children:
				alpha = max(alpha, self.minimax(child, depth-1, False))
		else:
			alpha = 0
			children = self.generate_random(node)
			for child in children:
				alpha = alpha + (child.prob * self.minimax(child,depth-1 , True))  
		
		return alpha

	def generate_children(self,node):
		children = []
		for move in MOVES:
			temp = copy.deepcopy(node)
			temp.board = MOVE(node.board,move)
			if valid_move():
				children.append(temp)
				temp.ai_move = move
		return children

	def generate_random(self,node):
		available = node.get_ready_places()
		length = len(available)
		children = []
		while available:
			temp = copy.deepcopy(node)
			pos = available.pop()
			x = pos[0]
			y = pos[1]
			tile = Tile(2)
			temp.prob = 1.0/length
			temp.board[x][y] = tile
			children.append(temp)
		return children

	def predict(self):
		empty_spots = len(self.state.get_ready_places())
		depth = empty_spots > 7 and 1 or (empty_spots > 4 and 2 or 3)
		
		children = self.generate_children(self.state)
		if not children: return
		max_board = children[0]
		max_score = self.minimax(max_board,depth,False)
		for child in children:
			score = self.minimax(child,depth,False)
			if max_score < score:
				max_score = score
				max_board = child
		return max_board.ai_move

	def get_move(self):
		move = self.predict()
		return move