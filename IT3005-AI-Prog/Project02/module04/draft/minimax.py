from sys import maxsize
from move_helper import move as MOVE
from move_helper import valid_move
from tree import Tree
import random
import copy
EMPTY = 0
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
MOVES = [UP,DOWN,LEFT,RIGHT]
class Minimax:
	def __init__(self):
		self.state = None
		self.move = None
		self.board = self.state.board


	def minimax(self,node,depth,my_turn):
		if depth = 0:
				return the heuristic value of node
		
		elif my_turn:
			// Return value of maximum-valued child node
			alpha = float('-inf')
			children = self.generate_children(node)
			for child in children:
				child = child[0]
				alpha = max(alpha, minimax(child, depth-1, False))
		else:
			// Return weighted average of all child nodes
			alpha = 0
			
				α := α + (Probability[child] * expectiminimax(child, depth-1))
		return α

	def generate_children(self,node):
		children = []
		for move in MOVES:
			temp = MOVE(node,move)
			if valid_move():
				children.append((node,move))
		return children

	def generate_random(self,node):
		


	
	def get_move(self):
		move = random.choice(MOVES)
		return move


	def generate_states(self):
		depth = 0
		empty_spots = len(self.state.get_ready_places())
		if empty_spots > 7:
			depth = 1
		else:
			depth = 3

		start_board = copy.deepcopy(self.board)
		tree = Tree(start_board)
		for x in range(depth):
			children = []
			for move in MOVES:
				temp_board = copy.deepcopy(self.board)
				temp_board = MOVE(temp_board,move)
				temp_tree = Tree(temp_board)








		

