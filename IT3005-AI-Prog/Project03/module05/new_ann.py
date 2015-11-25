import numpy as np
from theano import tensor as T 
import theano

def floatX(X):
	return np.asarray(X, dtype=theano.config.floatX)
 
def init_weights(shape):
	return theano.shared(floatX(np.random.randn(*shape) * 0.01))

def softmax(X):
	e_x = T.exp(X - X.max(axis=1).dimshuffle(0, 'x'))
	return e_x / e_x.sum(axis=1).dimshuffle(0, 'x')

def backpropagate(cost, params, lr=0.001, rho=0.9, epsilon=1e-6):
	grads = T.grad(cost=cost, wrt=params)
	updates = []
	for p, g in zip(params, grads):
		acc = theano.shared(p.get_value() * 0.)
		acc_new = rho * acc + (1 - rho) * g ** 2
		gradient_scaling = T.sqrt(acc_new + epsilon)
		g = g / gradient_scaling
		updates.append((acc, acc_new))
		updates.append((p, p - lr * g))
	return updates


def create_weights(sizes):
	weights = []
	for x in range(len(sizes)-1):
		w1 = sizes[x]
		w2 = sizes[x+1]
		weights.append(init_weights((w1,w2)))
	return weights

def rectify(X):
	return T.maximum(X, 0.)

def sigmoid(X):
	return T.nnet.sigmoid(X)

def sinh(X):
	return T.sinh(X)
	
def softmax(X):
	e_x = T.exp(X - X.max(axis=1).dimshuffle(0, 'x'))
	return e_x / e_x.sum(axis=1).dimshuffle(0, 'x')

class Ann:
	def __init__(self,sizes,features,labels, act):
		self.sizes = sizes
		self.act = act
		self.weights = create_weights(self.sizes)
		
		self.X = T.fmatrix()
		self.Y = T.fmatrix() 
		self.py_x = self.model(self.X, self.weights, self.act)
		
		self.y_x = T.argmax(self.py_x, axis=1)
		
		self.cost = T.mean(T.nnet.categorical_crossentropy(self.py_x, self.Y))

		self.updates = backpropagate(self.cost, self.weights)
		self.train = theano.function(inputs=[self.X, self.Y], outputs=self.cost, updates=self.updates, allow_input_downcast=True)
		self.predict = theano.function(inputs=[self.X], outputs=self.y_x, allow_input_downcast=True)

	def model(self,X,weights, act):
		output_layer = weights[-1]
		for w in range(len(weights) - 1):
			if act == "rectify": X = rectify(T.dot(X, weights[w]))
			if act == "sigmoid": X = sigmoid(T.dot(X, weights[w]))
			if act == "sinh": 	 X = sinh(T.dot(X, weights[w]))
		pyx = softmax(T.dot(X, output_layer))
		return pyx

	def blind_test(self,feature_sets):
		return list(self.predict(feature_sets))








		