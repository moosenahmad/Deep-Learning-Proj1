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
	######## Need to do variance equation here
	
        #Will need to convert variance equation to python code here
	return np.var(data)
	

"""
Write code to read data from given .txt file,  use numpy.loadtxt 
"""

filename = "data1.txt"
data = np.loadtxt(filename)


mle = MLE(data).variance_estimator()
mu = MLE(data).mean_estimator()

print(mle) #Variance
print(mu) #Mean
