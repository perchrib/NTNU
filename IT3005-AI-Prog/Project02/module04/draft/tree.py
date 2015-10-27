class Tree:
	def __init__(self,data):
		self.parent = None
		self.child = []
		self.data = data

	def addChild(self,child):
		self.child.append(child)

	def addParent(self,parent):
		self.parent = parent
		