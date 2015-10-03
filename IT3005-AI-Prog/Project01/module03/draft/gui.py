from permutations import generate_permutation
import collections

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




def initiateData(data):
	

	init = data.pop(0)
	row = init[1]
	col = init[0]

	temp_data = data[:row]
	#temp_data.reverse()
	#data.reverse()
	allVariables = {}
	for i in range(row):
		""""Row started with 0 to differentiate between ROW AND COL ID"""
		variable = Variable(('row',i),col,row,temp_data[i])
		allVariables[variable.index] = variable
		#print "ROW: " , temp_data[i]

	temp_data = data[row:]
	for i in range(col):
		""""COL end with 0 """
		variable = Variable(('col',i),row,col,temp_data[i])
		allVariables[variable.index] = variable
		#print "COL: ", temp_data[i]

	
	return allVariables,row,col

def readFile(f):
	data = map(lambda x: x.strip(), open(f,'r'))
	data = map(lambda x: x.split(),data)
	data = map(lambda row: map(int, row), data)

	return data

def getVariables():
	f = "nanograms/scenario_9.txt"
	data,num_of_row,num_of_col = initiateData(readFile(f))
	sort = collections.OrderedDict(sorted(data.items()))
	for d in sort:
		variable = sort[d]
		# print variable.index, " ", variable.length , " ", variable.fill
		# for n in variable.neighbour:
		# 	print "N: ", n , variable.isCol()

		# print "\n"

		# for x in variable.domain:
		# 	print x
		# print "\n"
		# print variable.index, " neighbour length:" , variable.neighbour_length
		variable.generate_neighbour(sort)

	return sort,num_of_col,num_of_row
	

		


















