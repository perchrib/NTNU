from itertools import product

"""Main function that calls the otherones returns all valid permutations"""
def generate_permutation(length,fill):
	minCost = reduce(lambda x,y: x+y,fill) + len(fill) - 1
	permutation = []
	if minCost <= length:
		k = length - minCost
		index = 0
		for i in range(len(fill)):
			startValues = []
			for k in range(k+1):
				startValues.append(index+k)
			permutation.append(startValues)
			index += fill[i] + 1
	allCombos = all_combos(permutation,fill)
	finalVariables = setVariables(allCombos,fill,length)
	return finalVariables

"""Finding all combination of possible start values """
def all_combos(startValues,fill):
	all_combos = list(product(*startValues))
	finalCombos = []
	for combo in all_combos:
		if checkSpacing(list(combo),fill):
			finalCombos.append(combo)
	return finalCombos
"""Delete all combination that will not satisfy with the constraint"""
def checkSpacing(combo,fill):
	for i in range(1,len(combo)):
		if not combo[i] > combo[i-1] + fill[i-1]:
			return False
	return True 
"""Set variables as a list of 1 or 0. 0 represent empty space and 1 represent filled space"""
def setVariables(allCombos,fill,length):
	allVariables = []
	for combo in allCombos:
		tempVariable = [0] * length 
		for i in range(len(fill)):
			for j in range(combo[i],combo[i]+fill[i]):
				tempVariable[j] = 1
		allVariables.append(tempVariable)
	return allVariables





