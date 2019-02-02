import numpy as np

class MU():
    def __init__(self, data):
        self.data = data

    def mean_estimator(self):
        return np.mean(self.data)

"""
Write your class here, no need to change the name of class and function
"""

class MLE(MU):
    def __init__(self, data):
        MU.__init__(self, data)

    def variance_estimator(self):
	      variance = 0
        //Will need to convert variance equation to python code here
	      return variance
	

"""
Write code to read data from given .txt file,  use numpy.loadtxt 
"""

filename = "data1.txt"
data = np.loadtxt(filename)
