import numpy as np
from theano import tensor as T 
import theano


def floatX(X):
	return np.asarray(X, dtype=theano.config.floatX)

"""Generate random weights between -0.01 and 0.01"""
def init_weights(shape):
	return theano.shared(floatX(np.random.randn(*shape) * 0.01))

def softmax(X):
	e_x = T.exp(X - X.max(axis=1).dimshuffle(0, 'x'))
	return e_x / e_x.sum(axis=1).dimshuffle(0, 'x')
"""The backpropogation function"""
def RMSprop(cost, params, lr=0.001, rho=0.9, epsilon=1e-6):
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

"""Activation Functions"""
def rectify(X):
	return T.maximum(X, 0.)

def sigmoid(X):
	return T.nnet.sigmoid(X)

def sinh(X):
	return T.sinh(X)
	


"""Class representation of the neural network"""
class Ann:
	def __init__(self,sizes,features,labels):
		self.sizes = sizes
		self.weights = create_weights(self.sizes)
		
		self.X = T.fmatrix()
		self.Y = T.fmatrix() 
		self.py_x = self.model(self.X, self.weights)
		
		self.y_x = T.argmax(self.py_x, axis=1)
		
		self.cost = T.mean(T.nnet.categorical_crossentropy(self.py_x, self.Y))

		self.updates = RMSprop(self.cost, self.weights)
		self.train = theano.function(inputs=[self.X, self.Y], outputs=self.cost, updates=self.updates, allow_input_downcast=True)
		self.predict = theano.function(inputs=[self.X], outputs=self.py_x, allow_input_downcast=True)

	"""Model and where the activation function, layers and their sizes are set"""
	def model(self,X,weights):
		output_layer = weights[-1]
		for w in range(len(weights) - 1):	
			X = rectify(T.dot(X,weights[w]))
			#X = sigmoid(T.dot(X,weights[w]))
			#X = sinh(T.dot(X, weights[w]))
		pyx = softmax(T.dot(X, output_layer))
		return pyx




