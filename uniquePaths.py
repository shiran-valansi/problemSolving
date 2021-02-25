##### DP bottom up #######

def uniquePaths(rows, cols):
    """
    A robot is located at the top-left corner of a m x n grid

    The robot can only move either down or right at any point in time

    How many possible unique paths are there to the bottom right corner?


    >>> uniquePaths(3, 7)
    28

    >>> uniquePaths(3, 3)
    6

    >>> uniquePaths(1,1)
    1

    """
    # padding the dp matrix with zeros to make it simpler
    dp = [[0]*(cols+1) for i in range(rows+1)]
    dp[rows][cols-1] = 1
    
    for r in range(rows):
        for c in range(cols):
            dp[rows-r-1][cols-c-1] = dp[rows-r][cols-c-1] + dp[rows-r-1][cols-c]
    
    return dp[0][0]


##### DP top down - more complicated #######

def uniquePathsTopDown(rows, cols):
    """

    >>> uniquePathsTopDown(3, 7)
    28

    >>> uniquePathsTopDown(3, 3)
    6

    >>> uniquePathsTopDown(1,1)
    1

    """

    
    dp = [[0]*(cols) for i in range(rows)]
    get_number_of_routes(0, 0, dp, rows, cols)
    
    return dp[0][0]
        
        
def get_number_of_routes(r, c, dp, rows, cols):
    
    if r == rows-1 and c == cols-1:
        dp[r][c] = 1
        return 1
    
    if r == rows or c == cols:
        return 0
        
    dp[r][c] = get_number_of_routes(r+1, c, dp, rows, cols) + get_number_of_routes(r, c+1, dp, rows, cols)
    return dp[r][c]


if __name__ == "__main__":
    import doctest
    doctest.testmod()