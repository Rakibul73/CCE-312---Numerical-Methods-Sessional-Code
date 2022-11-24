# https://stackoverflow.com/questions/70323836/solving-system-of-linear-equation-using-cramers-method-in-python

import numpy as np

def cramer(mat, constant): # takes the matrix and the costants
    
    D = np.linalg.det(mat) # calculating the determinant of the original matrix

    # substitution of the column with costant and creating new matrix

    mat1 = np.array([constant, mat[:,1], mat[:,2]])
    mat2 = np.array([mat[:,0], constant, mat[:,2]])
    mat3 = np.array([mat[:,0], mat[:,1], constant])  
    
    #calculatin determinant of the matrix
    D1 = np.linalg.det(mat1)
    D2 = np.linalg.det(mat2)
    D3 = np.linalg.det(mat3)
    
    #finding the X1, X2, X3
    X1 = D1/D
    X2 = D2/D
    X3 = D3/D
    
    print(X1, X2, X3)


# main function
a = np.array([[10, 40, 70],
             [20, 50, 80],
             [30, 60, 80]])

b = np.array([300, 360, 390])

cramer(a,b)