import numpy as np

def cramers(mat , contstant):
    detarminat = np.linalg.det(mat)

    mat1 = np.array([ contstant , mat[:,1] , mat[:,2]])
    mat2 = np.array([ mat[:,0] , contstant , mat[:,2]])
    mat3 = np.array([  mat[:,0] , mat[:,1] , contstant])

    d1 = np.linalg.det(mat1)
    d2 = np.linalg.det(mat2)
    d3 = np.linalg.det(mat3)

    x1 = d1/detarminat
    x2 = d2/detarminat
    x3 = d3/detarminat

    print(x1)
    print(x2)
    print(x3)





a = np.array([[6546,841,6546], [36586,356,648412], [542,564,231]])
b= np.array([654,32879894,1654])

cramers(a,b)