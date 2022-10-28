
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

def gauss_elem(mat):  
    num = len(mat)  

    for i in range(0, num):  
        max_el = abs(mat[i][i])  
        max_row = i  
        for k in range(i + 1, num):  
            if abs(mat[k][i]) > max_el:  
                max_el = abs(mat[k][i])  
                max_row = k  

        for k in range(i, n + 1):  
            temp = mat[max_row][k]  
            mat[max_row][k] = mat[i][k]  
            mat[i][k] = temp  

        for k in range(i + 1, n):  
            curr = -mat[k][i] / mat[i][i]  
            for j in range(i, n + 1):  
                if i == j:  
                    mat[k][j] = 0  
                else:  
                    mat[k][j] += curr * mat[i][j]  

    l = [0 for i in range(n)]  
    for j in range(n - 1, -1, -1):  
        l[j] = mat[j][n] / mat[j][j]  
        for k in range(j - 1, -1, -1):  
            mat[k][n] -= mat[k][j] * l[j]  
    return l  


if __name__ == "__main__":  
    from fractions import Fraction  

    n = int(input('Enter the unknown value: '))  

    print(f'Enter the Matrix {n}x{n} formatted with SPACES (for columns) and ENTERS (for lines): ')
    A_mat = [[0 for j in range(n + 1)] for i in range(n)]  

    for j in range(0, n):  
        l = map(Fraction, input().split(" "))  
        for i, elem in enumerate(l):  
            A_mat[j][i] = elem  


    l = input('Enter the respective results for LINES separated by SPACES: ').split(" ")  
    print(l)  
    last = list(map(Fraction, l))  
    for j in range(0, n):  
        A_mat[j][n] = last[j]  

    print_aug(A_mat)  

    x = gauss_elem(A_mat)  

    l = "Result:\t"  
    for j in range(0, n):  
        l += str(x[j]) + "\t"  
    print(l)   