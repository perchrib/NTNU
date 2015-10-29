EMPTY = 0
"""Heuristics"""

"""Give Points respect to number of open places"""
def free_cells(board):
	total_score = 0
	for row in board:
		for tile in row:
			if tile == EMPTY:
				total_score += 1
	return total_score

# zero_filter = [
# 	[512,256,128,64],
# 	[0,0,0,0],
# 	[0,0,0,0],
# 	[0,0,0,0],
# ]
"""Filter for having a snake tactics"""
zero_filter = [[10,8,7,6.5],
 				[.5,.7,1,3],
 				[-.5,-1.5,-1.8,-2],
 				[-3.8,-3.7,-3.5,-3]]
"""GOOD"""
# zero_filter = [[16,15,14,13],
# 				[9,10,11,12],
# 				[8,7,6,5],
# 				[1,2,3,4]]

"""Use the filter to accomplish the snake format"""
def snake(board):
	return dot(board, zero_filter) #+ free_cells(board)**2

def dot(node1, node2):
	r = 0
	for y in xrange(4):
		for x in xrange(4):
			tile = node1[y][x]
			if tile == EMPTY:
				continue
			else:
				r += tile.value * node2[y][x]
	return r

"""Give points for have the top row filled"""
def top_row(board):
	score = 0
	for x in xrange(4):
		tile = board[0][x]
		if tile == EMPTY:
			score = -10
			return score
		else:
			score += 5
	return score

def sum_tiles(board):
	total_score = 0
	for row in board:
		for tile in row:
			if tile == EMPTY:
				continue 
			else:
				total_score += tile.value
	return total_score

