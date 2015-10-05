from permutations import generate_permutation
import collections
import Tkinter as tk

"""This class represent the variables in csp"""
class Variable:
	def __init__(self,index,length,nLength,fill):
		self.fill = fill
		self.index = index
		self.hash = index[0]
		self.length = length
		self.neighbour_length = nLength
		self.neighbour = []
		self.domain = []
		self.current = []
		self.generate_permutation()

	def isRow(self):
		return self.index[0] == 'row'
	def isCol(self):
		return self.index[0] == 'col'
	
	def generate_permutation(self):
		self.domain = generate_permutation(self.length,self.fill)

	def generate_neighbour(self,allVariables):
		for i in range(self.length):
			if self.isRow():
				self.neighbour.append(allVariables[('col',i)])
			if self.isCol():
				self.neighbour.append(allVariables[('row',i)])


""""This Class represent the node in A star search states"""
class Node:
	def __init__(self,parent,variables):
		self.variables = variables
		self.parent = parent
		self.kids = []
		self.g = 0
		self.f = 0
		self.status = None
		self.assuptionVariable = None
	
	def __lt__(self,other):
		return self.f < other.f
	
	"""Heuristic depending on how many domains that is left, counts every domain greater than ONE"""
	def heuristic(self):
		h = 0
		for key in self.variables:
			variable = self.variables[key]
			if 'row' in key:
				h += len(variable.domain) - 1
			if 'col' in key:
				h += len(variable.domain) - 1
		return h

	def isFinish(self):
		finish = True
		for key in self.variables:
			v = self.variables[key]
			if len(v.domain) != 1:
				finish = False

		return finish

def initiateData(data):
	init = data.pop(0)
	row = init[1]
	col = init[0]
	temp_data = data[:row]
	allVariables = {}
	for i in range(row):
		""""Row started with 0 to differentiate between ROW AND COL ID"""
		variable = Variable(('row',i),col,row,temp_data[i])
		allVariables[variable.index] = variable

	temp_data = data[row:]
	for i in range(col):
		""""COL end with 0 """
		variable = Variable(('col',i),row,col,temp_data[i])
		allVariables[variable.index] = variable
		
	return allVariables,row,col

def readFile(f):
	data = map(lambda x: x.strip(), open(f,'r'))
	data = map(lambda x: x.split(),data)
	data = map(lambda row: map(int, row), data)

	return data

class Draw(tk.Tk):
	def __init__(self,rows,columns):
		tk.Tk.__init__(self)
		if len(rows) > len(columns):
			factor_s = len(rows)
		else:
			factor_s = len(columns)
		node_size = (self.winfo_screenheight()-50)/factor_s
		self.width = self.winfo_screenheight()
		self.height = self.winfo_screenheight()
		self.canvas = tk.Canvas(self, width= self.width,height=self.height)
		self.canvas.pack()
		for x in range(len(rows)):
			for y in range(len(columns)): 
				gridx = node_size*y+1
				gridy = node_size*x+1
				gridx2 = gridx + node_size -2
				gridy2 = gridy + node_size -2
				first_domain_X = rows[x].domain[0]
				node_in_domain_X = first_domain_X[y]

				tag = 'a'+ str(rows[x].index[1])+"-" + str(y)
				
				if node_in_domain_X is 0:
					self.canvas.create_rectangle(gridx,gridy, gridx2, gridy2, fill="mint cream",tags=tag)
				elif node_in_domain_X is 1:
					self.canvas.create_rectangle(gridx,gridy, gridx2, gridy2, fill="black",tags=tag)

def setColor(route):
	if route is 0:
		return 'mint cream'
	if route is 1:
		return 'black'

def getVariables():
	f = "nanograms/scenario_7.txt"
	data,num_of_row,num_of_col = initiateData(readFile(f))
	sort = collections.OrderedDict(sorted(data.items()))
	rows = []
	columns = []
	for key in sort:
		variable = sort[key]
		if 'col' in key:
			columns.append(variable)
		if 'row' in key:
			rows.append(variable)

		variable.generate_neighbour(sort)

	rows.reverse()
	gui = Draw(rows,columns)
	
	return sort,num_of_row,num_of_col,gui