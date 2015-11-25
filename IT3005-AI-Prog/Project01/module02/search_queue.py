from heapq import heappush, heappop


class SearchQueue():
	def __init__(self,search):
		self.search = search
		self.astar = False
		self.bfs = False
		self.dfs = False
		self.storage = []
		
		if self.search == 'astar':
			self.astar = True

		elif self.search =='bfs':
			self.bfs = True

		elif self.search == 'dfs':
			self.dfs = True

	def __len__(self):
		return len(self.storage)

	def __iter__(self):
		return iter(self.storage)




	def string(self):
		for x in self.storage:
			print "F(h): ", x.f ,  "h(): ", x.heuristic()
			 



	def add(self,element):
		if self.astar:
			heappush(self.storage,element)

		elif self.bfs:
			self.storage.append(element)
		elif self.dfs:
			self.storage.append(element)

	def pop(self):
		if self.astar:
			element = heappop(self.storage)
			#print "CurrentNode State", element.state, "CurrentNode: ", element.f
		elif self.bfs:
			element = self.storage.pop(0)

		elif self.dfs:
			element = self.storage.pop()

		return element


