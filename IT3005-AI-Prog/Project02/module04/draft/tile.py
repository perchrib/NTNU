import random
class Tile():
	def __init__(self,value):
		self.value = value
		self.pos = None
		self.color = None
		
	def set_start_value(self):
		prob = random.randint(0,9)
		if prob > 0:
			self.value = 2
		else:
			self.value = 4

		return prob