#  https://www.edureka.co/blog/least-square-regression/

# Import the required libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reading Data Import the data set show data
data = pd.read_csv('E:/Study/5th Semester/Latest/CCE 312 (Numerical Methods Sessional)/CCE 312 - Numerical Methods Sessional Code/linear_least_squares_regression_using_python/sample2.csv')
print(data.shape)

print(data.head())


# Assigning ‘X’ as independent variable and ‘Y’ as dependent variable
# Coomputing X and Y
X = data['aa'].values
Y = data['bb'].values

# Mean X and Y
mean_x = np.mean(X)
mean_y = np.mean(Y)

# Total number of values
n = len(X)

# Calculate the values of the slope and y-intercept

# Using the formula to calculate 'm' and 'c'
numer = 0
denom = 0
for i in range(n):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2
m = numer / denom
c = mean_y - (m * mean_x)

# Printing coefficients
print("Coefficients")
print(m, c)


# Plotting the line of best fit
# Plotting Values and Regression Line
 
max_x = np.max(X) + 100
min_x = np.min(X) - 100
 
# Calculating line values x and y
x = np.linspace(min_x, max_x, 1000)
y = c + m * x
 
# Ploting Line
plt.plot(x, y, color='#58b970', label='Regression Line')
# Ploting Scatter Points
plt.scatter(X, Y, c='#ef5423', label='Scatter Plot')
 
plt.xlabel('Head Size in cm3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()
