# Casey Lewis
# Finding the determinant of a n x n matrix using a recursive function


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
