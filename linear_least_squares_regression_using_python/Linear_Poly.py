import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv('E:/Study/5th Semester/Latest/CCE 312 (Numerical Methods Sessional)/CCE-312---Numerical-Methods-Sessional-Code/linear_least_squares_regression_using_python/data.csv')
x = np.array(data.Level).reshape((-1,1))
y = np.array(data.Salary)

model = LinearRegression().fit(x,y)

plt.scatter(x,y)
plt.show()

plt.scatter(x,y)
plt.plot(x,model.predict(x))
plt.show()

print(model.predict(x))
print(model.intercept_)
print(model.coef_)
print(model.predict(np.array([[10]])))

# poly_x = PolynomialFeatures(degree=3).fit_transform(x)

# model = LinearRegression().fit(poly_x,y)

# print(model.predict(poly_x))
# print(model.intercept_)
# print(model.coef_)

# plt.scatter(x,y)
# plt.plot(x,model.predict(poly_x))
# plt.show()

# print(model.predict(PolynomialFeatures(degree=3).fit_transform(np.array([[10]]))))