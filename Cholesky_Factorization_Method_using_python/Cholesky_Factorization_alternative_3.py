import numpy as np

def myLU(A):
    n = A.shape[0] # get the dimension of the matrix A
    L = np.matrix( np.identity(n) ) # Build the identity part L
    U = np.copy(A) # start the U matrix as a copy of A
    for j in range(0,n-1):
        for i in range(j+1,n):
            mult = A[i,j] / A[j,j]
            U[i, j+1:n] = U[i, j+1:n] - mult * U[j,j+1:n]
            L[i,j] = mult
            U[i,j] = 0 # why are we doing this?
    return L,U



A = np.array([
        [6, 3, 4, 8], 
        [3, 6, 5, 1], 
        [4, 5, 10, 7], 
        [8, 1, 7, 25]
        ])

x,y = myLU(A)

print(x,"\n\n",y)