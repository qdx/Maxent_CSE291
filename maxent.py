# psudo code
#@1 Find out how many features are needed,say k features, and what they are
#@2 Initialize k features to 0
#@3 Calculate emperical expectation:For every feature, f_i, count the number of training tuples which has f_i, as
#n_i, divide them by N, the number of total training tuples. We get Er_i
#@4 

class Maxent:

	def __init__(self):
		"model expectation and observed expectation of f_i"
		self.observed = []
		self.expected = []
		pass

	def Reset(self):
		"This method reset the model"
		pass

	def TrainingInstanceGenerator(self,FilePath):
		'''This method should serve as a generator that output training
		tuples. With the form (class,[fet1,fet2,fet3...])'''
		pass

	def TestInstanceGenerator(self,FilePath):
		"Just like the TrainingInstanceGenerator, but for test tuples"
		pass

	def TrainModel(self):
		"This method train the model"
		pass

	def TestModel(self):
		"This method test a single model"
		pass

	def OutputModelToFile(self,path):
		"This method output the trained model to a file"
		pass

	def ReadModelFromFile(self,path):
		"This method read a model from a file"
		pass



