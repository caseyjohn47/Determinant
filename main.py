# Casey Lewis
# Linear Algebra Functions
# Finding the determinant of a n x n matrix using a recursive function
# Determine if a set of vectors is orthogonal
# Find norm of vector and orthonormalize sets

import math


# get the determinant
# matrix is matrix to find determinant of
# n is length of the matrix
def det(matrix, n):

    # determinant value
    value = 0
    # current row
    row = 0

    # if n = 2 then use det = ad - bc
    if (n == 2):
        # value = a*d - b*c
        value = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    
    # if n > 2, use recursion
    else:
        # for every column in in matrix
        for col in range(n):
            # create new matrix that eliminates current row and current column
            curr_matrix = new_matrix(matrix, row, col, n)
            # if even column, add new part
            if (col % 2 == 0):
                # value = value + (current position value * determinant of new matrix)
                value = value + (matrix[0][col] * det(curr_matrix, n-1))
            # if odd column, subtract new part
            else:
                value = value - (matrix[0][col] * det(curr_matrix, n-1))
            # delete curr_matrix after use to save space
            del curr_matrix
    
    # return value
    return value


# get new matrix from original matrix
# matrix is orginal matrix
# row is row to be eliminated
# column is column to be eliminated
# length is length of original matrix
def new_matrix(matrix, row, column, length):

    # Initialize matrix of all 0's of size length-1 x length-1
    smaller_matrix = [[0 for j in range(length-1)] for k in range(length-1)]

    # current position of smaller matrix that needs to be filled
    curr_x = 0
    curr_y = 0

    # for every row in original matrix
    for x in range(length):
        if (x != row):
            # for every column in original matrix
            for y in range(length):
                # if the current position is not in row or column that must be eliminated
                if (y != column):
                    # insert position of original matrix into current position of new matrix
                    smaller_matrix[curr_x][curr_y] = matrix[x][y]
                    # increase column position by 1
                    curr_y = curr_y + 1
            # increase row position by 1
            curr_x = curr_x + 1
        # reset column position to 0
        curr_y = 0

    # return new matrix
    return smaller_matrix


# check if a matrix is orthogonal
# every ROW is a vector
# checks if their dot products are 0
def is_orthogonal_set(matrix):
    # variables for row and column lengths
    rows = len(matrix)
    cols = len(matrix[0])
    # loop through matrix and for each one, check if orthogonal to all other
    for curr_row_num in range(rows-1):
        curr_row = matrix[curr_row_num]
        for x in range(curr_row_num+1, rows):
            next_row = matrix[x]
            if not is_orthogonal(curr_row, next_row):
                return False
    return True


# checks if two vectors are orthogonal
# their dot product must equal 0
def is_orthogonal(vector1, vector2):
    total = 0
    # loop through each value in vectors and multiply and add to total
    for x in range(len(vector1)):
        total = total + (vector1[x] * vector2[x])
    if total == 0:
        return True
    else:
        return False


# find the norm of a vector
# square root of every value in the vector squared then added together
def find_norm(vector):
    total = 0
    for x in vector:
        total = total + (x * x)
    total = math.sqrt(total)
    return total


# normalize a vector
# divide vector by the norm
def normalize_vector(vector):
    norm = find_norm(vector)
    vec = []
    for x in vector:
        vec.append(x * (1/norm))
    return vec


# every row is a vector
def orthonormalize_set(matrix):
    new_matrix = []
    if is_orthogonal_set(matrix):
        for vector in matrix:
            vec = normalize_vector(vector)
            new_matrix.append(vec)
        return new_matrix
    return matrix