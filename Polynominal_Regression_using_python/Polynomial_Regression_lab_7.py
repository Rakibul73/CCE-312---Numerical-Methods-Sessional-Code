import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

weather_data_p = pd.read_csv("E:/Study/5th Semester/Latest/CCE 312 (Numerical Methods Sessional)/CCE 312 - Numerical Methods Sessional Code/Polynominal_Regression_using_python/sample_lab_7.csv")

X = weather_data_p[["xi"]]
y = weather_data_p.yi

plt.scatter(X, y, c = "black")
plt.xlabel("xi")
plt.ylabel("yi")
plt.show()

pre_process = PolynomialFeatures(degree=2)

X_poly = pre_process.fit_transform(X)

df_X_poly = pd.DataFrame(X_poly)
df_X_poly.columns = ['1','x','x_squared']

df_X_poly.head()


pr_model = LinearRegression()

pr_model.fit(X_poly, y)

y_pred = pr_model.predict(X_poly)


plt.scatter(X, y, c = "black")
plt.xlabel("xi")
plt.ylabel("yi")
plt.plot(X, y_pred)
plt.show()


theta0 = pr_model.intercept_
_, theta1, theta2 = pr_model.coef_

print("Y = " + str(theta0) +" + "+ str(theta1)+"*X + "+ str(theta2) + "*XX")
