from gui import Draw
from main import train
from ai2048demo import welch
from math import log,ceil
import numpy as np
from scipy.stats import ttest_ind
DIM = 4
def main():
	#train([192,625,300,100,4],20)
	#train([192,150,80,25,4],1)
	#train([192,100,4],10)
	train([192,100,4],2)
	
	#train([192,625,300,100,4],50) #BEST
	gui = Draw(DIM)

	response = input("Press Enter To continue: ")
	while not response:
		random , ai = gui.samples()
		random.sort()
		ai.sort()
		random.reverse()
		ai.reverse()
		print('\n','\t\t---RANDOM---')
		print_list(random)
		print('\n','\t\t---AI---',)
		print_list(ai)
		##############
		w = welch(random,ai)
		print('\n',w)
		#visualize = input("type y to show: ")
		#if visualize == 'y':
			#gui.DEMO = True
		response = input("Print Enter To continue: ")
	gui.mainloop()

def print_list(li):
	for x in range(5):
		start = x*10
		end = 10*(x+1)
		print(li[start:end])

def welch_test(l1,l2):
	t, p = ttest_ind(l1, l2, equal_var=False)
	return t,p
def avg(li):
	return sum(li)/len(li)


main()


