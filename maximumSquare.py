def maximal_square_dp(matrix):
    """
    Given an m x n binary matrix filled with 0's and 1's, 
    find the largest square containing only 1's and return its area.

    >>> maximal_square_dp([["1","0","1","0","0"],["1","0","1","1","1"], ["1","1","1","1","1"],["1","0","0","1","0"]])
    4

    >>> maximal_square_dp([["0"]])
    0

    >>> maximal_square_dp([["0","1"],["1","0"]])
    1


    >>> maximal_square_dp([["0","0"],["0","0"]])
    0

    """
        
    rows = len(matrix)
    cols = len(matrix[0])
    max_square = 0
    
    dp = [[0]*cols for r in range(rows) ]
    
    for r in range(rows):
        for c in range(cols):
            dp[r][c] = get_max_square(dp, matrix, r, c, rows, cols)
            
            max_square = max(dp[r][c], max_square)
    return max_square**2
    
def get_max_square(dp, matrix, r, c, rows, cols):
    
    if r == 0 or c == 0 or matrix[r][c] == "0":
        return int(matrix[r][c])
    
    return min(dp[r-1][c], dp[r-1][c-1], dp[r][c-1]) + 1
    
############# BRUTE FORCE ###########

def maximal_square(matrix):
    """
    >>> maximal_square([["1","0","1","0","0"],["1","0","1","1","1"], ["1","1","1","1","1"],["1","0","0","1","0"]])
    4

    >>> maximal_square([["0"]])
    0

    >>> maximal_square([["0","1"],["1","0"]])
    1


    >>> maximal_square([["0","0"],["0","0"]])
    0


    """
    
    rows = len(matrix)
    cols = len(matrix[0])
    max_square = 0
    
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == "1":
                curr_square = get_square_area(r, c, matrix, rows, cols)
                max_square = max(curr_square, max_square)
                
    return max_square
    
def get_square_area(r, c, matrix, rows, cols):
    
    area = 1
    start = (r,c)
    end = (r+1, c+1)
    while end[0]<rows and end[1] < cols:
        if all_ones(matrix, start, end):
            area = (end[0] - start[0] + 1)**2
            end = [end[0]+1, end[1]+1]
        else:
            return area
    return area
    
    
def all_ones(matrix, start, end):
    
    # check bottom row:
    for c in range(start[1], end[1]+1):
        if matrix[end[0]][c] != "1":
            return False
        
    # check right column:
    for r in range(start[0], end[0]):
        if matrix[r][end[1]] != "1":
            return False
        
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()