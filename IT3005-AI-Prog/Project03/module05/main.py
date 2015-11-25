import mnist_basics as db
from new_ann import Ann
import numpy as np
import matplotlib.pyplot as plt
from mnistdemo2 import major_demo

"""Convert the labels into a list of equal size as the output layer where the element at the index equal to the predicted number is 1""" 
def format_labels(x,n):
	if type(x) == list:
		x = np.array(x)
	x = x.flatten()
	o_h = np.zeros((len(x),n))
	o_h[np.arange(len(x)),x] = 1
	return o_h

def main(sizes,training_iteration, act, test=False):
	features,labels = db.load_all_flat_cases()
	features = np.asarray(features)
	features = features/255
	labels = format_labels(labels,10)
	ann = Ann(sizes,features,labels, act)

	# x = list(range(20))
	# y = []

	"""Training the network"""
	for i in range(training_iteration):
		for start, end in zip(range(0, len(features), 128), range(128, len(features), 128)):
			ann.cost = ann.train(features[start:end], labels[start:end])
		print("Training Step: " , i+1, "/",training_iteration)	

		"""Where the network's accuracy is tested"""
		if test:
			features_test,labels_test = db.load_all_flat_cases('testing')
			features_test = np.asarray(features_test)
			features_test = features_test/255.
			labels_test = format_labels(labels_test,10)
			test_case = features_test
			answer = labels_test
			num = 0
			predictions = ann.predict(test_case)
			for p in range(len(predictions)):
				if predictions[p] == np.argmax(answer[p]): num += 1

			print(str(num) + " / 10000")
			#y.append(num)

	# canvas = plt.figure()
	# rect = canvas.patch
	# rect.set_facecolor("white")

	# sp1 = canvas.add_subplot(1,1,1, axisbg="w")
	# sp1.plot(x, y, "red", linewidth=2)
	# canvas.suptitle("Accuracy")
	# plt.xlabel("Run nr")
	# plt.ylabel("Correct classifications")
	# plt.ylim([2000,10000])
	# plt.show()

	if not test:
		temp = input("WAIT....")	
		major_demo(ann,10,"basics/")

#main[input, h, h2, ... hi, activation function, (test)]
main([784,1024,720,10],10,"rectify")





