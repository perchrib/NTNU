import copy
from tile import Tile
EMPTY = 0
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

"""Main func for moving tiles to one side, arg[0] matrix, arg[1], UP,DOWN,LEFT,RIGHT
Only call this function when import from another .py file"""
def move(matrix,move):
	global TILE_MOVED
	TILE_MOVED = False
	transposed = False
	if move == UP or move == DOWN:
		transposed = True
		matrix = transpose(matrix)
	
	merged = merge_matrix(matrix,move)
	one_sided = move_to_one_side(merged,move)
	if transposed:
		one_sided = transpose(one_sided)
	return one_sided

"""Make row to columns and uposite"""
def transpose(matrix):
	columns = []
	for i in range(len(matrix)):
		columns.append(one_columns(matrix,i))
	return columns
"""return one col from a matrix"""
def one_columns(matrix,i):
	return [row[i] for row in matrix]

"""Move all elements to one side if it is possible"""
def move_to_one_side(matrix,move):
	copy_matrix = copy.deepcopy(matrix)
	new_matrix = []
	for i in range(len(matrix)):
		temp = []
		for j in range(len(matrix)):
			tile = matrix[i][j]
			if tile == EMPTY:
				copy_matrix[i].remove(tile)
				temp.append(EMPTY)
		if move == RIGHT or move == DOWN:
			new_matrix.append(temp + copy_matrix[i])
		elif move == LEFT or move == UP:
			new_matrix.append(copy_matrix[i] + temp)
		check_if_tile_was_moved(new_matrix[i],matrix[i])
	return new_matrix
"""Merge the matrix if possible (Valid Moves)"""	
def merge_matrix(matrix, move):
	merged = []
	matrix = move_to_one_side(matrix,move)
	for serie in matrix:
		merged.append(merge_serie(serie,move))
	return merged
"""Merge one row or column if possible"""
def merge_serie(array,move):
	is_reversed = False
	if move == RIGHT or move == DOWN: #End of List
		is_reversed = True
		array.reverse()
	i = 0
	j = 1
	for index in range(len(array)):
		if i < len(array)-1:
			if array[i] != EMPTY and array[i+j] != EMPTY:
				t1 = array[i].value 
				t2 = array[i+j].value
				if t1 == t2:
					temp_tile = Tile(t1*2)
					array[i] = temp_tile
					array[i+j] = EMPTY
					global TILE_MOVED
					TILE_MOVED = True
					i += 2
				else:
					i += 1
			elif array[i] == EMPTY:
				i += 1
	if is_reversed:
		array.reverse()
		return array
	return array
"""Help func for valid move"""
def check_if_tile_was_moved(l1,l2):
	global TILE_MOVED
	for i in range(len(l1)):
		if l1[i] == EMPTY and l2[i] != EMPTY:
			TILE_MOVED = True
		elif l1[i] != EMPTY and l2[i] == EMPTY:
			TILE_MOVED = True
"""Return boolean if it possible to move that given direction"""
def valid_move():
	global TILE_MOVED
	return TILE_MOVED