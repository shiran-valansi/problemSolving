def closedIsland(grid):
    """
    Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

    Return the number of closed islands.

    >>> closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]])
    2

    >>> closedIsland([[0,0,1,1,0,1,0,0,1,0],[1,1,0,1,1,0,1,1,1,0],[1,0,1,1,1,0,0,1,1,0],[0,1,1,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,1,1,0],[0,1,0,1,0,1,0,1,1,1],[1,0,1,0,1,1,0,0,0,1],[1,1,1,1,1,1,0,0,0,0],[1,1,1,0,0,1,0,1,0,1],[1,1,1,0,1,1,0,1,1,0]])
    5

    """
    # we can recognize a closed island if we cannot reach the borders of the matrix.
        
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    count = 0
    
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            
            if (r,c) in visited:
                continue
            if grid[r][c] == 0:
                visited.add((r, c))
                count += is_island(grid, r, c, visited)
                
    return count
    
    
def is_island(grid, r1, c1, visited):
    
    q = [(r1,c1)]
    is_island = True
    
    while q:
        r, c = q.pop(0)
        neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        
        for row, col in neighbors:
            if (row, col) in visited:
                continue        
            if grid[row][col] == 0:
                if row == 0 or col == 0 or row == len(grid)-1 or col == len(grid[0])-1:
                    is_island = False
                else:
                    q.append((row, col))
                    visited.add((row, col))
    return is_island


def closedIslandDFS(grid):
    """
    >>> closedIslandDFS([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]])
    2

    >>> closedIslandDFS([[0,0,1,1,0,1,0,0,1,0],[1,1,0,1,1,0,1,1,1,0],[1,0,1,1,1,0,0,1,1,0],[0,1,1,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,1,1,0],[0,1,0,1,0,1,0,1,1,1],[1,0,1,0,1,1,0,0,0,1],[1,1,1,1,1,1,0,0,0,0],[1,1,1,0,0,1,0,1,0,1],[1,1,1,0,1,1,0,1,1,0]])
    5
    """
    # we can recognize a closed island if we cannot reach the borders of the matrix through the island.
        
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    count = 0
    
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            
            if (r,c) in visited:
                continue
            if grid[r][c] == 0:
                count += is_island_dfs(grid, r, c, visited)
                
    return count
    
    
def is_island_dfs(grid, row, col, visited):
    
    if (row, col) in visited or grid[row][col] == 1:
        return True
    
    visited.add((row, col))
    
    if row == 0 or col == 0 or row == len(grid)-1 or col == len(grid[0])-1:
        return False

    a = is_island_dfs(grid, row-1, col, visited)
    b = is_island_dfs(grid, row+1, col, visited)
    c = is_island_dfs(grid, row, col-1, visited)
    d = is_island_dfs(grid, row, col+1, visited)
  
    return a and b and c and d
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()