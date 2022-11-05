import numpy as np
from scipy.sparse import diags
import pandas as pd

# We consider that matrix A can be written as A=L*L^T.
# Here we define the function responsible for finding the L matrix.

def Cholesky(A):
    A=np.array(A, float)
    L=np.zeros_like(A)
    n,_=np.shape(A)

    for i in range(n):
        
        L[i,i]=np.sqrt(A[i,i]-L[i,i] ** 2)


        sum = L[i,i-1] * L[i-1,i-1] + L[i,i] * L[i-1,i]
        L[i,i-1] = (A[i,i-1]-sum) / L[i-1,i-1]

        
    return L
    
# Now we define a function that solves our system using firstly forward substition and then backward
# It uses the matrix given from the first function, its transpose and B from Ax=B and provides the solution x

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
    
# Finally, we constract matrix A (500x500)

a = [1+i for i in range(2, 501)]
b = [1000+i for i in range(1, 501)]
c = [1+i for i in range(2, 501)]
offset = [-1,0,1]
matrix = np.array([a, b, c])
A = diags(matrix, offset).toarray()

# And then B (500x1)

B = [1+i for i in range(1,501)]

l = Cholesky(A)
U = np.transpose(l)
x = solver(l, U, B)

# Now, we use the built-in function for Cholesky Decomposition to compare our results

from numpy.linalg import cholesky

L = cholesky(A)
U = np.transpose(L)
x = solver(L, U, B)