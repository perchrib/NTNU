import random


class Tile:
	def __init__(self):
		self.pos = None
		self.value = None
		self.color = None


	def set_start_value(self):
		prob = random.randint(0,9)
		if prob > 0:
			self.value = 2
		else:
			self.value = 4

		return prob

	def get_color(self):


	def set_color(self):
		colors = {}
class Board:
	def __init__(self,dimension):
		self.domension = dimension
		self.board = [[None for x in range(dimension)] for y in range(dimension)]

	def


b = Board(4)
for x in b.board:
	print x
t = None
while t != 0:
	tile = Tile()
	t = tile.set_start_value()
	print "Prob ", t, " value: ", tile.value

