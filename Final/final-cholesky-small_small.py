import numpy as np
from scipy.linalg import lu_factor, lu_solve  


A = np.array([ [3,-.1,-.2],
                [.1,7,-.3], 
                [.3,-.2,10] ])

b = np.array([ 7.85, -19.3, 71.4 ])


lu, piv = lu_factor(A)
x = lu_solve((lu, piv), b)
print(x)



import numpy as np
import scipy.linalg



lu, piv = scipy.linalg.lu_factor(A)
x = lu_solve((lu, piv) , b)

print(x)
