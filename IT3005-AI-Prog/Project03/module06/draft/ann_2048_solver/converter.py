from math import log
import numpy as np
from test import *

def sum_s(flat_b):
	m = []
	rows = flat_b.split(":")
	for i in rows:
		m.append(i.split("-"))

	m = list(map(lambda row: list(map(int, row)), m))
	matrix = np.asmatrix(m)
	rows = matrix.sum(axis=1)
	columns = matrix.sum(axis=0)
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

def run():
	r = open("a_test_games_features.txt","r")
	f = open("a_test_games_sum.txt","w")
	g = r.readlines()
	for line in g:
		f.write(sum_s(line) + "\n")

	f.close()
	r.close()
run()


	