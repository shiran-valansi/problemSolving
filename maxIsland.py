def maxAreaOfIsland(grid):
    """
    Given a grid of 0's and 1's return the max area of an island (1's)

    >>> maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])
    6


    >>> maxAreaOfIsland([[0,0,0,0,0,0,0,0]])
    0

    """
        
    max_area = 0
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    
    def get_island_size(row, col):
        
        q = [(row,col)]
        count = 1
        while q:
            r, c = q.pop(0)
            neighbors = [(r+1, c), (r-1, c), (r,c+1), (r,c-1)]
            for r1, c1 in neighbors:
                if r1>=0 and r1<rows and c1>=0 and c1<cols and grid[r1][c1] == 1 and (r1,c1) not in visited:
                    visited.add((r1,c1))
                    q.append((r1,c1))
                    count += 1
                    
        return count

    for r in range(rows):
        for c in range(cols):
            if (r,c) in visited:
                continue
            visited.add((r,c))
            if grid[r][c] == 1:
                max_area = max(max_area, get_island_size(r, c))
                    
    return max_area
                    
if __name__ == "__main__":
    import doctest
    doctest.testmod()       