import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ttest_ind
random = [256, 256, 256, 256, 256, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 32, 32, 32]
ai1 = [512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 256, 256, 256, 256, 256, 256, 256, 256, 256, 256, 256, 256, 256, 256, 256, 256, 256, 256, 256, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 64, 32]
ai2 = [2048, 2048, 1024, 1024, 1024, 1024, 1024, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 256, 256, 256, 256, 256, 256, 256, 256, 256, 256, 256, 256, 256, 256, 128, 128, 128, 128, 128]
labels = ['RANDOM','16 INPUTS','12x16 INPUTS']
plt.axis([0, 50, 0, 2200])
plt.ylabel('Value Of Tiles')
#plt.xlabel()
def boxplot():
	plt.title("Boxplot Of 50 Runs")
	plt.boxplot([random,ai1,ai2], labels=labels)
	plt.show()


def plot():
	plt.title("Values Of 50 Runs")
	x = list(range(1,51))
	plt.plot(x,random,'r--',label='RANDOM')
	plt.plot(x,ai1,'g--',label='16 NODES')
	plt.plot(x,ai2,'b--',label='12x16 NODES')
	plt.legend()
	plt.show()

plot()