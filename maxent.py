import math
import random
# psudo code
#@1 Find out how many features are needed,say k features, and what they are
#@2 Initialize k features to 0
#@3 Calculate emperical expectation:For every feature, f_i, count the number of training tuples which has f_i, as
#n_i, divide them by N, the number of total training tuples. We get Er_i
#@4 

class Maxent:

	def __init__(self):
		"model expectation and observed expectation of f_i"
		self.classes = [0,1,2,3,4,5,6]
		self.amountOfFeatrues = 35
		self.features =	['f21','f30','f40','f51','f60','f70','f81','f91','f101','f111','f120','f130','f144','f150','f160','f171','f80','f151','f20','f41','f50','f71','f110','f131','f140','f170','f161','f31','f61','f90','f142','f100','f146','f121','f148','f21','f30','f40','f51','f60','f70','f81','f91','f101','f111','f120','f130','f144','f150','f160','f171','f80','f151','f20','f41','f50','f71','f110','f131','f140','f170','f161','f31','f61','f90','f142','f100','f146','f121','f148']
		self.observed = dict()
		for i in self.classes:
			self.observed[i] = [0 for j in range(self.amountOfFeatrues)]

		self.expected = dict()
		for i in self.classes:
			self.expected[i] = [0 for j in range(self.amountOfFeatrues)]

		# Lambdas store the trained lambdas, key of the dict
		# is the number of lambda, corresponding to the number
		# of feature functions. That is to say, each feature 
		# function has its own lambda param.
		self.Lambdas = dict()
		for i in self.classes:
			#self.Lambdas[i] = [0 for j in range(self.amountOfFeatrues)] 
			self.Lambdas[i] = [1.0/random.randint(1,100) for j in range(self.amountOfFeatrues)] 

		pass

	def Reset(self):
		"This method reset the model"
		pass

	def tmpTrainingInstanceParser(self,FilePath):
		'''This method should serve as a method that output list of training
		tuples. With the form (class,[fet1,fet2,fet3...])'''
		trainFile = open(FilePath,'r')
		trainSet = []
		line = trainFile.readline()
		while line != '':
			trainSet.append(line.strip())
			line = trainFile.readline()
		return trainSet


	def TestInstanceGenerator(self,FilePath):
		"Just like the TrainingInstanceParser, but for test tuples"
		pass

	def tmpFeatureFunctions(self, oneInstance):
		"This function returns the feature value of one training instance"
		s = oneInstance.split(' ')
		result = dict()
		c = int(s[0][-1]) - 1
		flist = [0 for i in range(self.amountOfFeatrues)]
		for i in s[1:]:
			flist[self.features.index(i)] = 1
		result[c] = flist
		for i in self.classes:
			if i != c:
				result[i] = [0 for j in range(self.amountOfFeatrues)]
		return result

	def TrainModel(self):
		"This method train the model"
		trainSet = self.tmpTrainingInstanceParser("./data/train") 

		# calculate observed
		for i in trainSet:
			features = self.tmpFeatureFunctions(i)
			for y in features:
				for k in range(self.amountOfFeatrues):
					self.observed[y][k] += features[y][k]
		fplist = []
		for i in self.classes:
			fplist.append(max(self.observed[i]))
		#fpound = max(fplist)
		fpound = 16 

		for i in self.classes:
			for k in range(self.amountOfFeatrues):
				self.observed[i][k] = float(self.observed[i][k])/len(trainSet)
		#for k in range(len(self.observed)):
			#self.observed[k] = float(self.observed[k])/len(trainSet)
		#print self.observed

		logFile = open("log2.txt",'w')
		for it in range(100):
			# i is the ith training instance
			for i in range(len(trainSet)):
				features = self.tmpFeatureFunctions(trainSet[i])
				# y is class label
				for y1 in self.classes:
					s =  [[0 for m in range(len(self.classes))] \
											for n in range(len(trainSet))]
					for y2 in self.classes:
						# features is a dict, key is the label of class,
						# value is a list of feature values{0,1} under that class
						for k in range(self.amountOfFeatrues):
							s[i][y1] += self.Lambdas[y2][k] * features[y2][k]
	
				z = sum([math.exp(s[i][y]) for y in self.classes])
				#print z
				
				for y in self.classes:
					for k in range(self.amountOfFeatrues):
						self.expected[y][k] += \
								features[y][k] * math.exp(s[i][y]) / z
			#print self.expected
	
			for y in self.classes:
				for k in range(self.amountOfFeatrues):
					#print "fpound:",fpound
					#print "ob:",self.observed[k],"exp:",self.expected[k],"k",k
					#print "ob:",math.log(self.observed[k]),"exp:",math.log(self.expected[k]),"k",k
					if self.observed[y][k] == 0:
						continue
					#print "minus log:",(math.log(self.observed[y][k]) -\
							#math.log(self.expected[y][k]))
					delta =	(math.log(self.observed[y][k]) -\
							 math.log(self.expected[y][k]))/fpound
					#if self.Lambdas[y][k] + delta < 0:
						#continue
					#print delta
					self.Lambdas[y][k] += delta

			diffList = []
			for i in self.classes:
				for j in range(self.amountOfFeatrues):
					diffList.append(self.observed[i][j]-self.expected[i][j])
			print sum(diffList)/len(diffList)

		#logFile.write("========="+str(it)+"==========\n")
		for j in range(self.amountOfFeatrues):
			for i in self.classes:
				logFile.write(str(i)+","+self.features[j]+"\t"+str(self.Lambdas[i][j])+"\n")
		logFile.close()

			





							#self.Lambdas[k] * math.exp()


	def TestModel(self):
		"This method test a single model"
		pass

	def OutputModelToFile(self,path):
		"This method output the trained model to a file"
		pass

	def ReadModelFromFile(self,path):
		"This method read a model from a file"
		pass


test = Maxent()
test.TrainModel()
