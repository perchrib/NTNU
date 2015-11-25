import test as db
from new_ann import Ann
import numpy as np
ann = None

"""Convert the labels into a list equal the size of output layer where 
the element at the index equivalent to the predicted move is equal to one """

def format_labels(x,n):
	if type(x) == list:
		x = np.array(x)
	x = x.flatten()
	o_h = np.zeros((len(x),n))
	o_h[np.arange(len(x)),x] = 1
	return o_h

"""Training the network"""
def train(sizes,training_iteration):
	global ann
	features,labels = db.load_cases()
	features = np.asarray(features)
	features = features
	labels = format_labels(labels,4)
	ann = Ann(sizes,features,labels)

	for i in range(training_iteration):
		for start, end in zip(range(0, len(features), 128), range(128, len(features), 128)):
			ann.cost = ann.train(features[start:end], labels[start:end])

		print("Training Step: " , i+1, "/",training_iteration )	



	# features_test,labels_test = db.load_all_flat_cases('testing')
	# features_test = np.asarray(features_test)
	# features_test = features_test/11.
	# labels_test = format_labels(labels_test,4)
	# test_case = features_test
	# answer = labels_test
	# num = 0
	# predictions = ann.predict(test_case)
	# for p in range(len(pred	ictions)):
	# 	#print("Prediction:",predictions[p],"Answer:",answer[p], predictions[p] == np.argmax(answer[p]))
	# 	if predictions[p] == np.argmax(answer[p]): num += 1
"""Gets the predicted move from ann"""	
def get_move(board):
	b = db.restore2(db.convert(db.flatten2(board)))
	b = np.asarray(b)
	#b = b/12.
	p = ann.predict([b])[0]
	return list(p)
