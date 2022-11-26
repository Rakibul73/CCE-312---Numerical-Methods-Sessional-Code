
import numpy as np
from choleski import *
# a = np.array([[ 1.44, -0.36, 5.52, 0.0], 
#                 [-0.36, 10.33, -7.78, 0.0], 
#                 [ 5.52, -7.78, 28.40, 9.0], 
#                 [ 0.0, 0.0, 9.0, 61.0]])
# b = np.array([0.04, -2.15, 0.0, 0.88])


a = np.array([[ 3, -0.1, -0.2], 
                [0.1, 7, -0.3], 
                [ 0.3, -0.2, 10], 
                ])
b = np.array([7.85, -19.3, 71.4])
aOrig = a.copy()
L = choleski(a)
print(L)
x = choleskiSol(L,b)
# print("x =",x)
for i in range(3):
    print(x[i] , end="\n")
print('\nCheck: A*x =\n',np.dot(aOrig,x))

