from numpy import array, zeros, sqrt

def decomposition(A):
    N = len(A)
    L = zeros((N,N))
    U = zeros((N,N))

    for j in range(N):                                  # j = 0 to N-1

        # Upper Triangular
        for i in range(j+1):                            # i = 0 to j

            U[i,j] = A[i,j] - sum(U[:i,j] * L[i,:i])    # k = 0 to i-1

        # Lower Triangular
        L[j,j] = 1                                          # i = j, Diagonal 1

        for i in range(j+1, N):                             # i = j+1 to N-1

            L[i,j] = (A[i,j] - sum(U[:j,j]*L[i,:j]))/U[j,j] # k = 0 to j-1

    print('LU Decomposition:')
    print('[L] =\n', L, sep='')
    print('[U] =\n', U, sep='', end='\n\n')
    return L, U


def solveLU(A, B):
    L, U = decomposition(A)
    N = len(L)
    
    X = zeros(N)
    Y = zeros(N)

    # Forward Substitution
    for i in range(N):                                      # i = 0 to N-1
        Y[i] = (B[i] - sum(L[i,:i] * Y[:i]))                # j = 0 to i-1

        # sumj = 0
        # for j in range(i):
        #     sumj += L[i,j] * Y[j]
        # Y[i] = (B[i] - sumj)

    # Backward Substitution
    for i in range(N-1, -1, -1):                            # i = N-1 to 0
        X[i] = (Y[i] - sum(U[i,i+1:] * X[i+1:])) / U[i,i]   # j = i+1 to N-1

        # sumj = 0
        # for j in range(i+1, N):
        #     sumj += U[i,j] * X[j]
        # X[i] = (Y[i] - sumj) / U[i,i]

    return X


# System of Equations

A = array([[1,1,-1],
           [2,3,5],
           [3,2,-3]], float)
B = array([2,-3,6], float)



N = len(A)


X = solveLU(A, B)

print("The Solution of the System:")
for i in range(N):
    print('X[', i+1, '] = ', round(X[i], 6), sep='')


'''

10 40 70 300
20 50 80 360
30 60 80 390

Decomposition: [A] = [L][U]   # [L][U] ≠ [U][L]    Not commutative

│a11 a12 a13 ... a1n│   │L11  0   0  ...  0 ││U11 U12 U13 ... U1n│
│a21 a22 a23 ... a2n│   │L21 L22  0  ...  0 ││ 0  U22 U23 ... U2n│
│a31 a32 a33 ... a3n│ = │L31 L32 L33 ...  0 ││ 0   0  U33 ... U3n│
│... ... ... ... ...│   │... ... ... ... ...││... ... ... ... ...│
│an1 an2 an3 ... ann│   │Ln1 Ln2 Ln3 ... Lnn││ 0   0   0  ... Unn│

For Doolittle: Lii = 1  All elements on main diagonal of [L] are 1

│a11 a12 a13 ... a1n│   │ 1   0   0  ...  0 ││U11 U12 U13 ... U1n│
│a21 a22 a23 ... a2n│   │L21  1   0  ...  0 ││ 0  U22 U23 ... U2n│
│a31 a32 a33 ... a3n│ = │L31 L32  1  ...  0 ││ 0   0  U33 ... U3n│
│... ... ... ... ...│   │... ... ...  1  ...││... ... ... ... ...│
│an1 an2 an3 ... ann│   │Ln1 Ln2 Ln3 ...  1 ││ 0   0   0  ... Unn│

│a11 a12 a13 ... a1n│
│a21 a22 a23 ... a2n│
│a31 a32 a33 ... a3n│ =
│... ... ... ... ...│
│an1 an2 an3 ... ann│

│U11    U12           U13                  ... U1n                         │
│U11L21 U12L21+U22    U13L21+U23           ... U1nL21+U2n                  │
│U11L31 U12L31+U22L32 U13L31+U23L32+U33    ... U1nL31+U2nL32+U3n           │
│ ...        ...             ...           ...             ...             │
│U11Ln1 U12Ln1+U22Ln2 U13Ln1+U23Ln2+U33Ln3 ... U1nLn1+U2nLn2+U3nLn3+...+Unn│

 U1jLi1 U1jLi1+U2jLi2 U1jLi1+U2jLi2+U3jLi3 ... U1jLi1+U2jLi2+U3jLi3+...+Unj

 where i = 1 to n, j = 1 to n, k = 1 to j


U11 = a11       U12 =  a12              U13 =  a13                     ...
L21 = a21/U11   U22 =  a22-U12L21       U23 =  a23-U13L21              ...
L31 = a31/U11   L32 = (a32-U12L31)/U22  U33 =  a33-U13L31-U23L32       ...
Ln1 = an1/U11   Ln2 = (an3-U12Ln1)/U22  Ln3 = (an3-U13L31-U23L32)/U33  ...

Uij = aij       Uij =  aij-U1jLi1       Uij =  aij-U1jLi1-U2jLi2
Lij = aij/Ujj   Lij = (aij-U1jLi1)/Ujj  Lij = (aij-U1jLi1-U2jLi2)/Ujj  

Ljj = 1                       j = 1   to n
Uij =  aij - ∑ Ukj*Lik        i = 1   to j, k = 1 to i-1
Lij = (aij - ∑ Ukj*Lik)/Ujj   i = j+1 to n, k = 1 to j-1

For U1j there is no ∑ and is implimented by k = 1 to 1-1, not entering k loop
For Li1 there is no ∑ and is implimented by k = 1 to 1-1, not entering k loop


Substitution: [A]{X}={B}    => [L][U]{X}={B}    => [U]{X}={y} and [L]{y}={B}

Forward Substitution: [L]{y}={B}

│ 1   0   0  ...  0 ││y1│   │b1│
│L21  1   0  ...  0 ││y2│   │b2│
│L31 L32  1  ...  0 ││y3│ = │b3│
│... ... ... ... ...││……│   │……│
│Ln1 Ln2 Ln3 ...  1 ││yn│   │bn│

y1 =  b1
y2 = (b2 - L21y1)
y3 = (b3 - L31y1 - L32y2)
yn = (bn - Ln1y1 - Ln2y2 - ... - L[n,n-1]y[n-1])

yi = (bi - ∑ Lij*yj)       , i = 1 to n, j = 1 to i-1

For y1 there is no ∑ and is implimented by j = 1 to 1-1, not entering j loop

Backward Substitution: [U]{X}={y}

│U11 U12 U13 ... U1n││x1│   │y1│
│ 0  U22 U23 ... U2n││x2│   │y2│
│ 0   0  U33 ... U3n││x3│ = │y3│
│... ... ... ... ...││……│   │……│
│ 0   0   0  ... Unn││xn│   │yn│

xn =  yn / Unn
x3 = (y3                   - U34*x4) / U33
x2 = (y2          - U23*x3 - U24*x4) / U22
x1 = (y1 - U12*x2 - U13*x3 - U14*x4) / U11
xi = (yi - Uij*xj - Uij*xj - Uij*xj) / Uii

xi = (yi - ∑ Uij*xj) / Uii , i = n to 1, j = i+1 to n

For xn there is no ∑ and is implimented by j = n+1 to n, not entering j loop

'''