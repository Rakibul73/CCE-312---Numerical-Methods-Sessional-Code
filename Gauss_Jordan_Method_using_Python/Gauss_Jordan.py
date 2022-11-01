#  https://www.geeksforgeeks.org/program-for-gauss-jordan-elimination-method/
# Python3 Implementation for Gauss-Jordan
# Elimination Method
M = 10

# Function to print the matrix
def PrintMatrix(a, n):
	for i in range(n):
		print(*a[i])

# function to reduce matrix to reduced
# row echelon form.
def PerformOperation(a, n):
	i = 0
	j = 0
	k = 0
	c = 0
	flag = 0
	m = 0
	pro = 0

	# Performing elementary operations
	for i in range(n):
		if (a[i][i] == 0):

			c = 1
			while ((i + c) < n and a[i + c][i] == 0):
				c += 1
			if ((i + c) == n):

				flag = 1
				break

			j = i
			for k in range(1 + n):

				temp = a[j][k]
				a[j][k] = a[j+c][k]
				a[j+c][k] = temp

		for j in range(n):

			# Excluding all i == j
			if (i != j):
				# Converting Matrix to reduced row
				# echelon form(diagonal matrix)
				p = a[j][i] / a[i][i]

				k = 0
				for k in range(n + 1):
					a[j][k] = a[j][k] - (a[i][k]) * p

	return flag

# Function to print the desired result
# if unique solutions exists, otherwise
# prints no solution or infinite solutions
# depending upon the input given.
def PrintResult(a, n, flag):

	print("Result is : ")

	if (flag == 2):
		print("Infinite Solutions Exists<br>")
	elif (flag == 3):
		print("No Solution Exists<br>")

	# Printing the solution by dividing constants by
	# their respective diagonal elements
	else:
		for i in range(n):
			print(a[i][n] / a[i][i], end=" ")

# To check whether infinite solutions
# exists or no solution exists
def CheckConsistency(a, n, flag):

	# flag == 2 for infinite solution
	# flag == 3 for No solution
	flag = 3
	for i in range(n):
		sum = 0
		for j in range(n):
			sum = sum + a[i][j]
		if (sum == a[i][j]):
			flag = 2

	return flag

# Driver code
a = [[0, 2, 1, 4], [1, 1, 2, 6], [2, 1, 1, 7]]

# Order of Matrix(n)
n = 3
flag = 0

# Performing Matrix transformation
flag = PerformOperation(a, n)

if (flag == 1):
	flag = CheckConsistency(a, n, flag)

# Printing Final Matrix
print("Final Augmented Matrix is : ")
PrintMatrix(a, n)
print()

# Printing Solutions(if exist)
PrintResult(a, n, flag)

# This code is contributed by phasing17
