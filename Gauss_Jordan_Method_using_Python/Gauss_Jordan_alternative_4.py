# https://github.com/zeeshan2k2/Guass-Jordan-Elimination-Matrix
# python program for gauss-jordan elimination method in a matrix.
# function to print list in a matrix form
def printmatrix():
    print("---------------------------")
    for i in matrix:
        for j in i:
            if j == -0: # this condition is used to change -0 to 0.
                j = 0
            #if the number is whole number in matrix it prints it without printing any zeros
            # after decimal point
            elif j % 1 == 0:
                j = "%.0f" % j
            # if the number is not whole number in matrix it prints two number after decimal point
            # i.e for 2.346446 = 2.34 you can change it by increasing or decreasing number of n in
            #"%.nf" % j where n will be the numbers after decimal point
            elif j % 1 != 0:
                j = "%.2f" % j
            print(j, end="  ")
        print()
    print("---------------------------")


# function to solve the pivot column
def pivotelement():
    rows = int(input("Enter the number of rows:"))
    rows -= 1
    colm = int(input("Enter the number of columns:"))
    colm -= 1
    # for first row pivot element
    pivot_element = matrix[rows][colm]
    print()
    print("%.1f" % pivot_element, "is pivot element")
    print()
    # divide pivot element by pivot row
    for i in range(len(matrix[rows])):
        matrix[rows][i] = matrix[rows][i] / pivot_element
    for row in range(len(matrix)):
        if row == rows:
            continue
        else:
            make_zero = matrix[row][colm]
            for col in range(len(matrix[colm])):
                matrix[row][col] = matrix[row][col] - make_zero * matrix[rows][col]


# to solve the pivot column and remove negative sign from all zeros.
def solve_pivotelement():
    print()
    pivotelement()
    printmatrix()
    print()


# this function will be used to solve the number of time we'll have to solve pivot column
def no_of_pivot_element():
    print()
    printmatrix()
    print()

    #if row number is equal column number
    if row_number == column_number:
        for i in range(row_number-1):
            number = ["first", "second", "third", "fourth", "fifth", "sixth"]
            n = i
            print("For", number[n], "pivot element enter the values of row and column")
            solve_pivotelement()
        print("This is the final Matrix.")

    #if row number is smaller than row number
    elif row_number < column_number:
        for i in range(row_number):
            number = ["first", "second", "third", "fourth", "fifth", "sixth"]
            n = i
            print("For", number[n], "pivot element enter the values of row and column")
            solve_pivotelement()
        print("This is the final Matrix.")

    #if row number is greater than column number
    elif row_number > column_number:
        for i in range(column_number-1):
            number = ["first", "second", "third", "fourth", "fifth", "sixth"]
            n = i
            print("For", number[n], "pivot element enter the values of row and column")
            solve_pivotelement()
        print("This is the final Matrix.")



# taking input for rows and column
print("What type of matrix do you want to solve")
row_number = int(input("rows : "))
print(row_number)
column_number = int(input("columns : "))
print(column_number)

# setting some pre-conditions
if column_number < 2 or row_number < 2:
    print("This matrix is not possible")
    quit()

n = 0
# taking input for matrix
matrix = [[0 for i in range(column_number)] for x in range(row_number)]
while n != row_number:
    number = ["first", "second", "third", "fourth", "fifth", "sixth"]
    print()
    print("Enter numbers for", number[n], "row")
    for i in range(column_number):
        data = int(input())
        matrix[n][i] = data
    n = n + 1

#using function that tells how to solve a matrix in certain given conditions
no_of_pivot_element()