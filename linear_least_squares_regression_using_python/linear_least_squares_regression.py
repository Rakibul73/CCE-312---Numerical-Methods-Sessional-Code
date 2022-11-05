# https://github.com/chasinginfinity/ml-from-scratch/tree/master/01%20Linear%20Regression%20using%20Least%20Squares

# Making imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12.0, 9.0)
# Preprocessing Input data
data = pd.read_csv('E:/Study/5th Semester/Latest/CCE 312 (Numerical Methods Sessional)/CCE 312 - Numerical Methods Sessional Code/linear_least_squares_regression_using_python/sample.csv')
X = data.iloc[:, 0]
Y = data.iloc[:, 1]
plt.scatter(X, Y)
plt.show()
# Building the model
X_mean = np.mean(X)
Y_mean = np.mean(Y)

num = 0
den = 0
for i in range(len(X)):
    num += (X[i] - X_mean)*(Y[i] - Y_mean)
    den += (X[i] - X_mean)**2
m = num / den
c = Y_mean - m*X_mean

print (m, c)

print("y =" , m,"x +", c)



