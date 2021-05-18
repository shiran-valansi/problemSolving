def sort_boundaries(matrix):
    """
    Sort boundaries border by border 
    Example:
    1234
    1234
    1234
    1234
    should give:
    1111
    4222
    4332
    4433

    """

    # go boundary boundary
    # get the array, sort, and put back in the matrix
    # we iterate by half diagonal
    
    rows = len(matrix)
    cols = len(matrix[0])
    boundaries = min(rows,cols) // 2

    for b in range(boundaries):

        boundary = get_boundary(b, matrix, rows, cols)
        place_boundary(b, matrix, boundary, rows, cols)
        
    print_matrix(matrix)

    return matrix 

def get_boundary(b, matrix, rows, cols):

    boundary = []
  
    # row above
    for c in range(b, cols-b-1):
        boundary.append(matrix[b][c])

    # right column
    for r in range(b, rows-b-1):
        boundary.append(matrix[r][cols-b-1])

    # row below
    for c in range(cols-b-1, b-1, -1):
        boundary.append(matrix[rows-b-1][c])

    # left column
    for r in range(rows-b-1, b, -1):
        boundary.append(matrix[r][b])
  
    boundary.sort()
    return boundary


def place_boundary(b, matrix, boundary, rows, cols):

    i = 0
    # row above
    for c in range(b, cols-b-1):
        matrix[b][c] = boundary[i]
        i += 1

    # right column
    for r in range(b, rows-b-1):
        matrix[r][cols-b-1] = boundary[i]
        i += 1

    # row below
    for c in range(cols-b-1, b-1, -1):
        matrix[rows-b-1][c] = boundary[i]
        i += 1

    # left column
    for r in range(rows-b-1, b, -1):
        matrix[r][b] = boundary[i]
        i += 1
    
def print_matrix(matrix):
    for r in range(len(matrix)):
        print(matrix[r])


matrix1 = [[1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4]]
matrix2 = [[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]]
matrix3 = [[1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8]]
matrix4 = [[1,2,3], [1,2,3], [1,2,3], [1,2,3], [1,2,3], [1,2,3], [1,2,3]]
sort_boundaries(matrix4)