import numpy as np

class MU():
    def __init__(self, data):
        self.data = data

    def mean_estimator(self):
        return np.mean(self.data)

class MLE(MU):
    def __init__(self, data):
	MU.__init__(self, data)

    def variance_estimator(self):
	n = len(data)
	mean = MLE(data).mean_estimator()
	count = 0
	sigma = 0
	while(count < n):
		sigma += (data[count] + mean) ** 2
		count += 1
	variance = (1.0/n)*(sigma)
	return variance
	

filename = "data1.txt"
data = np.loadtxt(filename)


mean = MLE(data).mean_estimator()
variance = MLE(data).variance_estimator()


print("Mean: {}\nVariance: {}".format(mean,variance))



