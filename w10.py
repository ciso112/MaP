from collections import Counter
import random
from sklearn.datasets import make_regression, make_blobs
from sklearn.cluster import KMeans
from matplotlib import pyplot
from scipy.stats import linregress
import numpy as np
from numpy import arange,array,ones,linalg

x = []
y = []
normx = []
normy = []

# load each of 2 rows into a list( x and y)
def load_file(file):

    lines = [line.rstrip('\n') for line in open(file)]
    for line in lines:
        v1, v2 = line.split(' ')
        x.append(float(v1))
        y.append(float(v2))
    return x, y

def normalize(x):
    norm = [float(i) / max(x) for i in x]
    return norm


# ### A Linear regression ###

load_file('linreg.txt')
normx = normalize(x)
normy = normalize(y)
pyplot.scatter(normx, normy)

# function used: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html

slope, intercept, r_value, p_value, std_err = linregress(normx, normy)
print slope, intercept, r_value, p_value, std_err
line_x = np.arange(min(normx), max(normx))
line_y = slope*line_x + intercept
pyplot.plot(line_x, line_y)

pyplot.show()


#  ### B Clusters - not finished ###

# load_file('faithful.txt')
# normx = normalize(x)
# normy = normalize(y)
# data =
# # pyplot.scatter(normx, normy)
# k = 3
# # X coordinates of random centroids
# C_x = np.random.randint(0, np.max(X)-20, size=k)
# # Y coordinates of random centroids
# C_y = np.random.randint(0, np.max(X)-20, size=k)
# C = np.array(list(zip(C_x, C_y)), dtype=np.float32)
# print(C)



# data = np.vstack((normx, normy)).T
# kmeans = KMeans(n_clusters=2, max_iter=300).fit(data)
# print kmeans

# pyplot.show()



def generate_data(min, max):
    number = random.random
    return min + (number * (max - min))

def linear_reg():
    x, y = make_regression(n_samples=100, n_features=1, noise=45)
    pyplot.scatter(x, y)
    pyplot.show()
    # print x, y

def clusters():
    x, y = make_blobs(n_samples=50, n_features=2, centers = 3)
    pyplot.scatter(x, y)
    pyplot.show()
