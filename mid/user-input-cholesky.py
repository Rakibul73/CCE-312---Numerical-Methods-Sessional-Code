import scipy
import scipy.linalg
import pprint
import numpy as np

def cramer(mat, constant):
    D = np.linalg.det(mat)
    mat1 = np.array([constant, mat[:, 1], mat[:, 2]])
    mat2 = np.array([mat[:, 0], constant, mat[:, 2]])
    mat3 = np.array([mat[:, 0], mat[:, 1], constant])
    Dx = np.linalg.det([mat1, mat2, mat3])
    X = Dx/D
    return X

    # D = np.linalg.det(mat)
    # D_others = []
    # for i in range(n):
    #     flag = mat.copy()
    #     flag[0:n, i] = constant
    #     d = np.linalg.det(flag)
    #     d = d / D
    #     D_others.append(d)
    # return D_others


n = 3
# a = np.array([[10, 40, 70], [20, 50, 80], [30, 60, 80]])
# b = np.array([300, 360, 390])


a = np.array([[1, 1, -1],
              [2, 3, 5],
              [3, 2, -3]])

b = np.array([2, -3, 6])
# a = np.array([ [3,-.1,-.2], [.1,7,-.3], [.3,-.2,10] ])
# b = np.array([7.85, -19.3, 71.4])

c = np.zeros(n)

P, L, U = scipy.linalg.lu(a)
print ("a")
pprint.pprint(a)
print ("L")
pprint.pprint(L)
print ("U")
pprint.pprint(U)

cramer(L,b)
c= cramer(a,b)
cramer(U,c)
d= cramer(a,b)
print(d)