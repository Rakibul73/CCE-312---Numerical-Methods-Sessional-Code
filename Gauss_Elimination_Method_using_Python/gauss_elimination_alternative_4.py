# https://youtu.be/_1Ue-BASy8Q

import numpy
from numpy import array, zeros

#Input System of Equations

a = array([[1, 1, -1],
            [6, 2, 2],
            [-3, 4, 1]], float)

b = array([-3,2, 1], float)
n = len(b)
x = zeros(n, float)


#Forward Elimination

for k in range(n-1):
    for i in range(k+1, n):
        fctr= a[i, k] / a[k, k]
        for j in range(k, n):
            a[i, j] = a[i, j] - fctr*a[k, j]
        b[i]= b[i] - fctr*b[k]


#Back-substitution

x[n-1] = b[n-1] / a[n-1, n-1]
for i in range(n-2, -1, -1):
    Sum = b[i]
    for j in range(i+1, n):
        Sum = Sum - a[i, j]*x[j]
    x[i] = Sum/a[i, i]


print("The solution of the system:")
print(x)
