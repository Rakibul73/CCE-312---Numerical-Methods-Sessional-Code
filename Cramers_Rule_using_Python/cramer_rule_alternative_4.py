# Cramer Rule Matrix Systems Calculator and Laplace Theorem
# Cramer's Rule | Xi = det(Ai) / det(A)
# Laplace       | Sum cof(A)i*j * A(i*j)
# Cofactor      | (-1)^i+j * det(A)i*j
# https://github.com/guiriosoficial/CramersRule

# Laplace algorithm
def laplace(matrix, val=1):
    # Set the matrix length
    n = len(matrix)

    # Return Det if Matrix length is 1
    if n == 1:
        return val * matrix[0][0]
    else:
        sign = -1
        det = 0
        for i in range(n):
            mtx = []
            for j in range(1, n):
                buff = []
                for k in range(n):
                    if k != i:
                        buff.append(matrix[j][k])
                mtx.append(buff)
            sign *= -1
            det += val * laplace(mtx, sign * matrix[0][i])
        return det

# Cramer algorithm
def cramer(matrix, results, order):
    # Calc and Show Main Matrix Determinant
    main_det = laplace(matrix)
    print(f'\nMain matrix determinant: {main_det}')

    # Build New Matrix with Substitutions
    if main_det != 0:
        resolution = []
        for r in range(order):
            matrix_sub = []
            for i in range(order):
                matrix_sub.append([])
                for j in range(order):
                    if j == r:
                        matrix_sub[i].append(results[i])
                    else:
                        matrix_sub[i].append(matrix[i][j])

            # Show Actual Matrix with Substitution
            print(f'\nMatrix with replacement at COLUMN {r + 1}:')
            for line in matrix_sub:
                for val in line:
                    print(f'{val:^8}', end=' ')
                print()

            # Calc Determinant with Substitution
            sub_det = laplace(matrix_sub)
            print(f'Determinant of this matrix: {sub_det}')

            # Calc and Save Final Resolution
            resolution.append(sub_det / main_det)

    # Return Resolution to Display in Main
        return resolution

    # Display Resolution if Main Det is 0
    else:
        return 0

# Main function
def main():
    # Read Matrix Range
    order = int(input('Enter the Matrix Order: '))

    # Read Matrix Numbers
    print(f'Enter the Matrix {order}x{order} formatted with SPACES (for columns) and ENTERS (for lines):')
    matrix = [list(map(float, input().split())) for i in range(order)]

    # Read Matrix Results
    results = list(map(float, input('Enter the respective results for LINES separated by SPACES: ').split()))

    # Show Mounted Matrix
    print('\nCheck if your system is mounted correctly:\n')
    for l, line in enumerate(matrix):
        for val in line:
            print(f'{val:^8}', end=' ')
        print(f'= {results[l]:^8}', end='\n')

    # Define if Has Correct Data
    reset = input('\nEnter (Y) for YES or (N) for NO. (YES is default): ').lower()
    if reset == 'n':
        print(), main()
    else:
        # Show Final Results
        resolution = cramer(matrix, results, order)
        if resolution != 0:
            print('\nSolution set:')
            for r in range(order):
                print(f'A{r + 1} = {resolution[r]}')
        else:
            print('\nImpossible to finish algorithm.\nThe determinant of the main matrix is EQUAL to 0.')


main()
