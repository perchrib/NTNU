import itertools
class CSP:
	def __init__(self):
		#self.gui = gui

		self.variables = []
		self.domains = {}
		self.constraints = {}
		

	def add_data(self,name, domain):
		self.variables.append(name)
		self.domains[name] = domain
		self.constraints[name] = {}


	def get_all_possible_pairs(self, a, b):
		"""Get a list of all possible pairs (as tuples) of the values in
		the lists 'a' and 'b', where the first component comes from list
		'a' and the second component comes from list 'b'.
		"""
		return itertools.product(a, b)

	def get_all_arcs(self):
		"""Get a list of all arcs/constraints that have been defined in
		the CSP. The arcs/constraints are represented as tuples (i, j),
		indicating a constraint between variable 'i' and 'j'.
		"""
		return [ (i, j) for i in self.constraints for j in self.constraints[i] ]

	def get_all_neighboring_arcs(self, var):
		"""Get a list of all arcs/constraints going to/from variable
		'var'. The arcs/constraints are represented as in get_all_arcs().
		"""
		return [ (i, var) for i in self.constraints[var] ]

	def add_constraint_one_way(self, i, j, filter_function):
		"""Add a new constraint between variables 'i' and 'j'. The legal
		values are specified by supplying a function 'filter_function',
		that returns True for legal value pairs and False for illegal
		value pairs. This function only adds the constraint one way,
		from i -> j. You must ensure that the function also gets called
		to add the constraint the other way, j -> i, as all constraints
		are supposed to be two-way connections!
		"""
		if not j in self.constraints[i]:
			# First, get a list of all possible pairs of values between variables i and j
			self.constraints[i][j] = self.get_all_possible_pairs(self.domains[i], self.domains[j])

		# Next, filter this list of value pairs through the function
		# 'filter_function', so that only the legal value pairs remain
		self.constraints[i][j] = filter(lambda value_pair: filter_function(*value_pair), self.constraints[i][j])

	def add_all_different_constraint(self, variables):
		"""Add an Alldiff constraint between all of the variables in the
		list 'variables'.
		"""
		for (i, j) in self.get_all_possible_pairs(variables, variables):
			if i != j:
				self.add_constraint_one_way(i, j, lambda x, y: x != y)



	def revise(self,domain,i,j):
		revised = False
		#for x in domain[i]:
		#	if not domain and 


def makefunc(var_names,expression,envir=globals()):
	args = ""
	for n in var_names:
		args = args + "," + n

	return eval("(lambda " + args[1:] + ": " + expression + ")", envir)

a = [1,2,3]
b = [5,6,7]
c = [2,3]
testData = [a,b,c]
constraint = "a + b < c*2"
func = makefunc(['x','y','z'],constraint)
csp = CSP()

for row in range(2):
	for col in range(2):
		csp.add_data('%d-%d' % (row, col), map(str, range(1, 3)))
		
for row in range(2):
	csp.add_all_different_constraint([ '%d-%d' % (row, col) for col in range(2) ])
for col in range(2):
	csp.add_all_different_constraint([ '%d-%d' % (row, col) for row in range(2) ])

#for x in range(len(testData)):
#	csp.add_data('%d'%x,testData[x])
#	csp.add_all_different_constraint('%d'%x)


print csp.variables
print csp.domains
print csp.constraints




















