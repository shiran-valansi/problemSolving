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