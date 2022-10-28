# https://stackoverflow.com/questions/70323836/solving-system-of-linear-equation-using-cramers-method-in-python

import numpy as np

def cramer(mat, constant):
    D = np.linalg.det(mat)
    mat1 = np.array([constant, mat[:, 1], mat[:, 2]])
    mat2 = np.array([mat[:, 0], constant, mat[:, 2]])
    mat3 = np.array([mat[:, 0], mat[:, 1], constant])
    Dx = np.linalg.det([mat1, mat2, mat3])
    X = Dx/D
    print(X)


a = np.array([[10, 40, 70],
             [20, 50, 80],
             [30, 60, 80]])

b = np.array([300, 360, 390])
cramer(a,b)