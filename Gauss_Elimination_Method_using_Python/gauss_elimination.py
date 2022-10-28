# Python program to find a solution to a set of linear equations using the Gaussian Elimination method  


# 3
# 2 -6 -1
# -3 -1 7
# -8 1 -2
# -38 -34 -20
# ['-38', '-34', '-20']
# 2       | -6    | -1    | -38   |
# -3      | -1    | 7     | -34   |
# -8      | 1     | -2    | -20   |

# Result: 4       8       -2



# Creating a function to print the augmented matrix with the given set of linear equations  
def print_aug(mat):  
    no = len(mat)  
    for i in range(0, no):  
        l = ""  
        for k in range(0, n + 1):  
            l += str(mat[i][k]) + "\t"  
            if j == no - 1:  
                l += "| "  
        print(l)  
    print("")  
  
# Creating a function to perform gaussian elimination on the given matrix mat  
def gauss_elem(mat):  
    num = len(mat)  
  
    for i in range(0, num):  
        # Searching the maximum value of a particular column  
        max_el = abs(mat[i][i])  
        # Row having the element of maximum value  
        max_row = i  
        for k in range(i + 1, num):  
            if abs(mat[k][i]) > max_el:  
                max_el = abs(mat[k][i])  
                max_row = k  
  
        # Swapping the maximum row with the current row   
        for k in range(i, n + 1):  
            temp = mat[max_row][k]  
            mat[max_row][k] = mat[i][k]  
            mat[i][k] = temp  
  
        # Chaning the value of the rows below the current row to 0   
        for k in range(i + 1, n):  
            curr = -mat[k][i] / mat[i][i]  
            for j in range(i, n + 1):  
                if i == j:  
                    mat[k][j] = 0  
                else:  
                    mat[k][j] += curr * mat[i][j]  
  
    # Solving the equation Ax = b for the created upper triangular matrix mat  
    l = [0 for i in range(n)]  
    for j in range(n - 1, -1, -1):  
        l[j] = mat[j][n] / mat[j][j]  
        for k in range(j - 1, -1, -1):  
            mat[k][n] -= mat[k][j] * l[j]  
    return l  
  
  
if __name__ == "__main__":  
    from fractions import Fraction  
  
    n = int(input())  
  
    A_mat = [[0 for j in range(n + 1)] for i in range(n)]  
  
    # Reading the input coefficients of the linear equations  
    for j in range(0, n):  
        l = map(Fraction, input().split(" "))  
        for i, elem in enumerate(l):  
            A_mat[j][i] = elem  
      
  
    l = input().split(" ")  
    print(l)  
    last = list(map(Fraction, l))  
    for j in range(0, n):  
        A_mat[j][n] = last[j]  
  
    # Printing the augmented matrix from the input data   
    print_aug(A_mat)  
  
    # Calculating the solution of the matrix  
    x = gauss_elem(A_mat)  
  
    # Printing the result   
    l = "Result:\t"  
    for j in range(0, n):  
        l += str(x[j]) + "\t"  
    print(l)   