import numpy as np


def det2x2(A, v=False):
    if v:  print ('compute 2 x 2 det of')
    if v:  print (A)
    assert A.shape == (2,2)
    return A[0][0]*A[1][1] - A[0][1]*A[1][0]

def det3x3(A):
    print ('compute 3 x 3 det of')
    print (A)
    assert A.shape == (3,3)
    a,b,c = A[0]
    c1 = a * det2x2(A[1:3,[1,2]])
    c2 = b * det2x2(A[1:3,[0,2]])
    c3 = c * det2x2(A[1:3,[0,1]])
    return c1 - c2 + c3
         
def solve(A):
    print ('solve')
    print( A, '\n')
    assert A.shape == (3,4)
    D = det3x3(A[:,:3])
    print ('D = '), D, '\n'
    if D == 0:
        print ('no solution')
        return
    Dx = det3x3(A[:,[3,1,2]])
    print ('Dx = '), Dx, '\n'
    Dy = det3x3(A[:,[0,3,2]])
    print ('Dy = '), Dy, '\n'
    Dz = det3x3(A[:,[0,1,3]])
    print ('Dz = '), Dz, '\n'
    return Dx*1.0/D, Dy*1.0/D, Dz*1.0/D
    
def check(A,x,y,z):
    print ('check')
    for i,r in enumerate(A):
        print ('row', i, '=', r)
        pL = list()
        for coeff,var in zip(r[:3],(x,y,z)):
            c = str(round(coeff,2))
            v = str(round(var,2))
            pL.append(c + '*' + v)
        print (' + '.join(pL),)
        print (' =', r[0]*x + r[1]*y + r[2]*z, '\n')
