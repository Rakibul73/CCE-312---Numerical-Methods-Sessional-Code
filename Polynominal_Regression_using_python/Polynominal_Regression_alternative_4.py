# https://www.section.io/engineering-education/polynomial-regression-in-python/
# https://www.askpython.com/python/examples/polynomial-regression-in-python
# https://www.aionlinecourse.com/tutorial/machine-learning/polynomial-regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('E:/Study/5th Semester/Latest/CCE 312 (Numerical Methods Sessional)/CCE 312 - Numerical Methods Sessional Code/Polynominal_Regression_using_python/position_salaries.csv') # read the dataset

X = dataset.iloc[:, 1:-1].values # extracts features from the dataset
y = dataset.iloc[:, -1].values # extracts the labels from the dataset

from sklearn.linear_model import LinearRegression # import the Linear Regression model
from sklearn.preprocessing import PolynomialFeatures # importing a class for Polynomial Regression
poly_regr = PolynomialFeatures(degree = 4) # our polynomial model is of order
X_poly = poly_regr.fit_transform(X) # transforms the features to the polynomial form
lin_reg_2 = LinearRegression() # creates a linear regression object
lin_reg_2.fit(X_poly, y) # fits the linear regression object to the polynomial features

LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)

plt.scatter(X, y, color = 'red') # plotting the training set
plt.plot(X, lin_reg_2.predict(poly_regr.fit_transform(X)), color = 'blue') # plotting the polynomial regression line
plt.title('Truth or Bluff (Polynomial Regression)') # adding a tittle to our plot
plt.xlabel('Position level') # adding a label to the x-axis
plt.ylabel('Salary') # adding a label to the y-axis
plt.show() # prints our plot

X_grid = np.arange(min(X), max(X), 0.1) # choice of 0.1 instead of 0.01 to make the graph smoother
X_grid = X_grid.reshape((len(X_grid), 1)) # reshapes the array to be a matrix
plt.scatter(X, y, color = 'red') # plots the training set
plt.plot(X_grid, lin_reg_2.predict(poly_regr.fit_transform(X_grid)), color = 'blue') # plots a polynomial regression line
plt.title('Truth or Bluff (Polynomial Regression for higher resolution and smoother curve)') # adds tittle to the plot
plt.xlabel('Position level') # adds label to the x-axis
plt.ylabel('Salary') # adds label to the y-axis
plt.show() # prints our plot

print(lin_reg_2.predict(poly_regr.fit_transform([[6.5]])))
