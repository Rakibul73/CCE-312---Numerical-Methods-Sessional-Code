# https://stackoverflow.com/questions/70323836/solving-system-of-linear-equation-using-cramers-method-in-python

import numpy as np

def cramer(a, b):
    mask = np.broadcast_to(np.diag([1,1,1]), [3, 3, 3]).swapaxes(0, 1)
    Ms = np.where(mask, np.repeat(b, 3).reshape(3, 3), a)
    return np.linalg.det(Ms) / np.linalg.det(a)



# main function
a = np.array([[10, 40, 70],
             [20, 50, 80],
             [30, 60, 80]])

b = np.array([300, 360, 390])

print(cramer(a,b))