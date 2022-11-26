import numpy as np
import scipy
from numpy.linalg import cholesky

# We consider that matrix A can be written as A=L*L^T.
# Here we define the function responsible for finding the L matrix.


def solver(L,U,b):
  L=np.array(L, float)
  U=np.array(U, float)
  b=np.array(b, float)

  n,_=np.shape(L)
  y=np.zeros(n)
  x=np.zeros(n)

# Forward substitution
  for i in range(n):
    sumj=0
    for j in range(i):
      sumj += L[i,j]*y[j]
    y[i]=(b[i]-sumj)/L[i,i]

# Backward substitution  
  for i in range(n-1, -1, -1):
    sumj=0
    for j in range(i+1,n):
      sumj += U[i,j] * x[j]
    x[i]=(y[i]-sumj)/U[i,i]
  return x
    

# Now, we use the built-in function for Cholesky Decomposition to compare our results

A = scipy.array([ [3,-.1,-.2],
                [.1,7,-.3], 
                [.3,-.2,10] ])
L = cholesky(A)
U = np.transpose(L)
x = solver(L, U, B)