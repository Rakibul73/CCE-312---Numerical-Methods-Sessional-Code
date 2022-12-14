import numpy as np

n = int(input("enter unknown: "))
a = np.zeros((n, n+1))
ans_x = np.zeros(n)
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input("=== "))

for i in range(n):
    for j in range(n):
        if i != j:
            ratio = a[i][i] / a[j][i]
            for k in range(n+1):
                a[j][k] = a[j][k] * ratio - a[i][k]

for i in range(n):
    ans_x[i] = a[i][n] / a[i][i]

for i in range(n):
    print(ans_x[i])
