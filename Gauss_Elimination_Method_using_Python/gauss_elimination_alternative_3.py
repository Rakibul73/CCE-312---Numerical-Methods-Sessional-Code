# https://techgoggler.com/computer-engineering/linear-equations-python-gauss-elimination-method/
import numpy as np
def gaussElim(a,b):
    n = len(b)
    # Elimination phase
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                #if not null define λ
                lam = a [i,k]/a[k,k]
                #we calculate the new row of the matrix
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                #we update vector b
                b[i] = b[i] - lam*b[k]
                # backward substitution
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    
    return b

#initial coefficients
a=np.array([[1.0,1.0,1.0],[1.0,-1.0,-1.0],[1.0,-2.0,3.0]])
b=np.array([1.0,1.0,-5.0])
aOrig = a.copy() # save original matrix A
bOrig = b.copy() #save original vector b
x = gaussElim(a,b)
#print A transformed for check
print(a)
print("x =\n",x)
#det = np.prod(np.diagonal(a)) #determinant
#print("\ndet =",det)
#check result and numerical precision
print("\nCheck result: [a]{x} - b =\n",np.dot(aOrig,x) - bOrig)