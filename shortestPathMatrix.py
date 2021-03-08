def shortestPathBinaryMatrix(grid):
    """
    Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

    A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

    All the visited cells of the path are 0.
    All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
    The length of a clear path is the number of visited cells of this path.

    >>> shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])
    4

    >>> shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]])
    -1

    >>> shortestPathBinaryMatrix([[0,1,1,0,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],[0,0,0,1,1,0],[1,1,1,1,1,0],[1,1,1,1,1,0]])
    14


    """
        
    if grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1
    
    min_len = get_min_path(grid)
    
    return min_len
                
                
def get_min_path(grid):
    
    q = [(0,0, 1)]
    visited = set()
    
    while q:
        r, c, level = q.pop(0)
        
        if r == len(grid)-1 and c == len(grid[0])-1:
            return level
        
        q.extend(get_neighbors(r,c,grid, level, visited))
        
    return -1
        
        
        
def get_neighbors(r1, c1, grid, level, visited):
    
    neighbors = []
    
    for r in range(r1-1, r1+2):
        for c in range(c1-1, c1+2):
            if r >= 0 and r< len(grid) and c >= 0 and c < len(grid[0]) and (r,c) != (r1, c1) and grid[r][c] == 0 and (r,c) not in visited:
                visited.add((r,c))
                neighbors.append((r,c, level+1))
                
    return neighbors

if __name__ == "__main__":
    import doctest
    doctest.testmod()
        
        