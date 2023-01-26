import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("E:/Study/5th Semester/Latest/CCE 312 (Numerical Methods Sessional)/CCE-312---Numerical-Methods-Sessional-Code/Final/zzzz.csv")
x = np.array(data.Level).reshape((-1,1))
y = np.array(data.Salary)

x = np.array([ [1], [2] , [3] , [4] ])
y = np.array([ [1], [2] , [3] , [4] ])

model = LinearRegression().fit(x , y)

print(model.predict(x))
print(model.predict(np.array([ [7] , [8] , [9] ])))

print(model.intercept_)
print(model.coef_)

# plt.scatter(x, y)
# plt.plot(x , model.predict(x))
# plt.show()

x_new = np.array([[6]])
y_pred = model.predict(x_new)






