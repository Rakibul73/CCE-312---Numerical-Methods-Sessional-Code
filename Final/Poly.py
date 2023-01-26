import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# data = pd.read_csv('E:/Study/5th Semester/Latest/CCE 312 (Numerical Methods Sessional)/CCE-312---Numerical-Methods-Sessional-Code/Final/zzzz.csv')
# x = np.array(data.Level).reshape((-1,1))
# y = np.array(data.Salary)

x = np.array([[ 80],
            [ 40],
            [ -40],
            [ -120],
            [ -200],
            [ -280],
            [ -340]])
y = np.array([[ 6.47*10**-6],
            [ 6.24*10**-6],
            [ 5.72*10**-6],
            [ 5.09*10**-6],
            [ 4.30*10**-6],
            [ 3.33*10**-6],
            [ 2.45*10**-6]])
# x = np.array([[ 1],
#             [ 2],
#             [ 3],
#             [ 4],
#             [ 5],
#             [ 6]])
# y = np.array([[ 1],
#             [ 2],
#             [ 3],
#             [ 4],
#             [ 5],
#             [ 6]])

poly_x = PolynomialFeatures(degree=2).fit_transform(x)

model = LinearRegression().fit(poly_x,y)


print(model.intercept_)
print(model.coef_)
print("y = " + str(round(*model.intercept_, 3))+ " + " + str(round(model.coef_[0][1], 3)) + "*x + " + str(round(model.coef_[0][2], 3)) + "*x^2" )

# showing GUI
# plt.scatter(x,y)
# plt.plot(x,model.predict(poly_x))
# plt.show()

# future value predict
# print(model.predict(PolynomialFeatures(degree=2).fit_transform(np.array([    [4] ,[5]   ]))))

