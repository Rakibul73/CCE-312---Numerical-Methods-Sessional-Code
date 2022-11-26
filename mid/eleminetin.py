import numpy as np

n = int(input("enter unknown: "))
a = np.zeros((n , n + 1))
x = np.zeros(n)

for i in range(n):
    for j in range(n+1):
        a[i][j] = input()

for i in range(n):
    for j in range(i+1 , n):
        ratio = a[i][i] / a[j][i]
        for k in range(n+1):
            a[j][k] = a[j][k] * ratio  -  a[i][k]


x[n-1] = a[n-1][n] / a[n-1][n-1]

for i in range(n-2 , -1 , -1):
    x[i] = a[i][n]

    for j in range(i+1, n):
        x[i] = x[i] - x[j] * a[i][j]
    x[i] = x[i] / a[i][i]

for i in range(n):
    print(x[i])
