import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

weather_data_p = pd.read_csv("E:/Study/5th Semester/Latest/CCE 312 (Numerical Methods Sessional)/CCE 312 - Numerical Methods Sessional Code/Polynominal_Regression_using_python/sample.csv")

# Set our input x to Pressure, use [[]] to convert to 2D array suitable for model input
X = weather_data_p[["xi"]]
y = weather_data_p.yi

# Produce a scatter graph of Humidity against Pressure
plt.scatter(X, y, c = "black")
plt.xlabel("xi")
plt.ylabel("yi")
plt.show()

# Import the function "PolynomialFeatures" from sklearn, to preprocess our data
# Import LinearRegression model from sklearn
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Set PolynomialFeatures to degree 2 and store in the variable pre_process
# Degree 2 preprocesses x to 1, x and x^2
# Degree 3 preprocesses x to 1, x, x^2 and x^3
# and so on..
 
pre_process = PolynomialFeatures(degree=2)

# Transform our x input to 1, x and x^2
X_poly = pre_process.fit_transform(X)
# Show the transformation on the notebook


df_X_poly = pd.DataFrame(X_poly)
df_X_poly.columns = ['1','x','x_squared']

df_X_poly.head()


pr_model = LinearRegression()

# Fit our preprocessed data to the polynomial regression model
pr_model.fit(X_poly, y)

# Store our predicted Humidity values in the variable y_new
y_pred = pr_model.predict(X_poly)


# Plot our model on our data
plt.scatter(X, y, c = "black")
plt.xlabel("xi")
plt.ylabel("yi")
plt.plot(X, y_pred)
plt.show()


theta0 = pr_model.intercept_
_, theta1, theta2 = pr_model.coef_

print("Y = " + str(theta0) +" + "+ str(theta1)+"*X + "+ str(theta2) + "*XX")
