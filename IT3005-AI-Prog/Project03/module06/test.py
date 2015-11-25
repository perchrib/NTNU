from random import randrange, sample
from itertools import product
from math import log
from tile import Tile
from board import Board
from minimax import Minimax
import numpy as np

features = set([])
labels = []

"""Generate random boards"""

def generate_random_node():
	num = randrange(1,17)
	b = [[0 for i in range(4)]for j in range(4)]
	all_combos = list(product(range(4),range(4)))
	random_sample = sample(all_combos, 4)
	for y,x in random_sample:
		b[y][x] = generate_tile()
	return b

def generate_random_node2():
	num = randrange(1,17)
	board = Board()
	b = [[0 for i in range(4)]for j in range(4)]
	board.board = b
	for i in range(num):
		board.set_new_tile(Tile(2**randrange(12)))
	return board

def generate_tile():
	return 2**randrange(12)


def to_bit(b):
	r = ""
	for y in range(4):
		for x in range(4):
			if b.board[y][x] == 0:
				r += "0"
			else:
				r += str(int(log(b.board[y][x].value,2)))
			if x < 3: r += "-"
		if y < 3: r += ":"
	return r
"""Flatten, sum_s and convert, Converts a matrix into a representation of text string"""
def flatten(b):
	r = ""
	for i in range(4):
		for j in range(4):
			r += str(b[i][j])
			if j < 3: r += "-" 
		if i < 3: r += ":"
	return r

def flatten2(b):
	r = ""
	for i in range(4):
		for j in range(4):
			if b[i][j] == 0:
				value = 0
			else:
				value = int(log(b[i][j].value,2))
			r += str(value)
			if j < 3: r += "-" 
		if i < 3: r += ":"
	return r
def sum_s(flat_b):
	m = []
	rows = flat_b.split(":")
	for i in rows:
		m.append(i.split("-"))

	m = list(map(lambda row: list(map(int, row)), m))
	matrix = np.asmatrix(m)
	rows = matrix.sum(axis=1)/48
	columns = matrix.sum(axis=0)/48
	rows = rows.ravel().tolist()[0]
	columns = columns.ravel().tolist()[0]

	f = ""
	for y in range(4):
		f += str(rows[y])
		if y < 3:
			f += '-'
	f += ':'
	for x in range(4):
		f += str(columns[x])
		if x < 3:
			f += '-'
	return f

def convert(flat_b):
	m = []
	rows = flat_b.split(":")
	for i in rows:
		m.append(i.split("-"))
	f = ""
	for y in range(4):
		for x in range(4):
			num = int(m[y][x])
			for i in range(num):
				f += "1"
				if i < 11: f += "-"
			f += "0-"*(12 - num - 1) + "0"
			if x < 3: f += "-"
		if y < 3: f += ":"
	return f

"""Loads the specific data files"""
def load_cases():
	features = []
	labels = []
	f = open("dataset/a_test_games_12_times_16_features.txt", "r")
	#f = open("a_test_games_features.txt", "r")
	l = open("dataset/a_test_games_labels.txt","r")
	moves = l.readlines()
	boards = f.readlines()
	f.close()
	l.close()
	for i,j in zip(boards, moves):
		if j.strip("\n") == "None": continue
		features.append(restore2(i))
		labels.append(int(j.strip("\n"))-1)
	return features,labels

"""Restore represents a text string into a matrix, (board state)"""
def restore2(flat_b):
	tmp = flat_b.split(":")
	b = []
	for row in tmp:
		temp = list(map(float,row.split("-")))
		for tile in temp:
			b.append(tile)
	return b

def restore(flat_b):
	tmp = flat_b.split(":")
	b = []
	for row in tmp:
		temp = list(map(int,row.split("-")))
		li_temp = []
		for tile in temp:
			if tile == 0:
				li_temp.append(0)
			else:
				li_temp.append(Tile(2**tile))
		b.append(li_temp)
	board = Board()
	board.board = b
	return board

"""Genrate continuesly games with AI"""
def new_game():
	board = Board(4)
	tile = Tile(None)
	tile.set_start_value()
	board.set_new_tile(tile)
	return board

"""Code that has been used during generate data representation files"""
# def generate_games():
# 	f = open("a_test_games_features.txt","w")
# 	l = open("a_test_games_labels.txt","w")
# 	for x in range(150):
# 		print("GAME NUMBER: ",x+1)
# 		board = new_game()
# 		ai = Minimax()
# 		i = 0
# 		while not board.has_lost():
# 			f.write(to_bit(board) + "\n")
# 			ai.state = board
# 			move = ai.get_move()
# 			l.write(str(move) + "\n")
# 			board.move(move)
# 			if board.valid_move:
# 				i += 1
# 				if i % 100 == 0:
# 					print("MOVES: ", i)
# 				new_tile = Tile(None)
# 				new_tile.set_start_value()
# 				board.set_new_tile(new_tile)
# 			else:
# 				print("TOTAL MOVES: ", i)
# 				break
# 	f.close()
# 	l.close()

#generate_games()

# f = open("test_features.txt","w")
# while len(features) < 10000:
# 	f.write(to_bit(generate_random_node2()) + "\n")
# 	features.add(to_bit(generate_random_node2()))
# 	if len(features) % 1000 == 0: print(len(features))
# f.close()

# f = open("test_features.txt","r")
# l = f.readlines()
# f.close()

# ai = Minimax()
# f = open("test_labels.txt", "w")
# for i in range(len(l)):
# 	board = restore(l[i])
# 	ai.state = board
# 	move = ai.get_move()
# 	f.write(str(move) + "\n") 
# 	labels.append(move)
# 	if len(labels) % 100 == 0: print(len(labels))
# f.close()

# print(len(labels))
