
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
    
    print(X1, X2, X3)


# main function
#   10x + 40y + 70z  = 300
#   20x + 50y + 80z  = 360
#   30x + 60y + 80z  = 390

a = np.array([[10, 40, 70],
             [20, 50, 80],
             [30, 60, 80]])

b = np.array([300, 360, 390])

cramer(a,b)