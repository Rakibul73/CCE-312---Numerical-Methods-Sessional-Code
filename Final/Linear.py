import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# data = pd.read_csv('E:/Study/5th Semester/Latest/CCE 312 (Numerical Methods Sessional)/CCE-312---Numerical-Methods-Sessional-Code/Final/zzzz.csv')
# x = np.array(data.Level).reshape((-1,1))
# y = np.array(data.Salary)


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
x = np.array([[ 0.698132] , [0.959931], [1.134464], [1.570796],  [1.919862] ])
y = np.array([ [0.188224], [ 0.209138], [0.230052 ], [0.250965] ,   [0.313707] ])



model = LinearRegression().fit(x,y)


# plt.scatter(x,y)
# plt.plot(x,model.predict(x))
# plt.show()

# print(model.predict(x))
print("intercept")
print(model.intercept_)
print("coefficient")
print(model.coef_)
print("y = " + str(round(*model.intercept_, 3))+ " + " + str(round(model.coef_[0][0], 3)) + "*x")


# print(model.predict(np.array([       [10]          ])))



