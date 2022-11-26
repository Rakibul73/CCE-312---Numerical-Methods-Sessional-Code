import pprint
import scipy
import scipy.linalg
import numpy as np


def cramer(mat, constant): 
    
    D = np.linalg.det(mat)

    mat1 = np.array([constant, mat[:,1], mat[:,2]])
    mat2 = np.array([mat[:,0], constant, mat[:,2]])
    mat3 = np.array([mat[:,0], mat[:,1], constant])  
    
    D1 = np.linalg.det(mat1)
    D2 = np.linalg.det(mat2)
    D3 = np.linalg.det(mat3)
    
    X1 = D1/D
    X2 = D2/D
    X3 = D3/D
    
    
    return X1 , X2 , X3

A = np.array([ [3,-.1,-.2],
                [.1,7,-.3], 
                [.3,-.2,10] ])


P, L, U = scipy.linalg.lu(A)

print ("L:")
pprint.pprint(L)

print ("U:")
pprint.pprint(U)



b = np.array([7.85, -19.3, 71.4])

Y1 , Y2, Y3 = cramer(L,b)
y = np.array([ Y1 , Y2 , Y3])

X1 , X2 , X3 = cramer(U,y)

print(X1 , X2 , X3)


