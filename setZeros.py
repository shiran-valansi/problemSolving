def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.
    """
    
    # get all zero's rows and cols
    # go through the matrix and turn all ones in those rows and cols to zeros
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    zero_rows = set()
    zero_cols = set()
    
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)
    
    for r in range(rows):
        for c in range(cols):
            if r in zero_rows or c in zero_cols:
                matrix[r][c] = 0
    print(matrix)
                
matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)


def setZeroesConstSpace(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    zero_first_col = False
    zero_first_row = False
    
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                matrix[r][0] = 0
                if c == 0:
                    zero_first_col = True
                if r == 0:
                    zero_first_row = True
    
    # we go through the matrix starting from matrix[1][1], otherwise we could falsely zero out everything
    for r in range(1,rows):
        for c in range(1,cols):
            if matrix[0][c] == 0 or matrix[r][0] == 0:                    
                matrix[r][c] = 0
                
    #check if matrix[0][0] == 0
    if matrix[0][0] == 0:
        if zero_first_row:
            for c in range(1,cols):
                matrix[0][c] = 0
        if zero_first_col:
            for r in range(1,rows):
                matrix[r][0] = 0
    print(matrix)

matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroesConstSpace(matrix)
matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeroesConstSpace(matrix2)
