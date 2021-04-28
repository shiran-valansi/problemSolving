def countBattleships(board):
    """
    Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

    Battleships can only be placed horizontally or vertically on board.

    >>> countBattleshipsOnePass([['.']])
    0

    >>> countBattleshipsOnePass([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]])
    2


    """

    rows = len(board)
    cols = len(board[0])
    visited = set()
    count = 0
    
    for r in range(rows):
        for c in range(cols):
            if (r,c) in visited:
                continue
            if board[r][c] == 'X':
                count += 1
                visited.add((r,c))
                dfs(r, c, board, visited, rows, cols)
                
    return count
    
def dfs(r, c, board, visited, rows, cols):

    neighbors = [(r+1, c), (r,c+1)]
    for r1,c1 in neighbors:
        if r1<rows and c1<cols and (r1,c1) not in visited:
            visited.add((r1,c1))
            if board[r1][c1] == 'X':
                dfs(r1, c1, board, visited, rows, cols)
            


def countBattleshipsOnePass(board):
    """
    Same, but with one pass on matrix, const added memory and without modifying the values board

    >>> countBattleshipsOnePass([['.']])
    0

    >>> countBattleshipsOnePass([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]])
    2


    """

    rows = len(board)
    cols = len(board[0])
    count = 0
    
    for r in range(rows):
        for c in range(cols):
            
            visited = False
                
            if board[r][c] == 'X':
                # peek backwards
                if (r-1 >=0 and board[r-1][c] == 'X') or (c-1 >= 0 and board[r][c-1] == 'X'):
                    visited = True
                    
                if not visited:
                    count += 1
                
    return count
    
            
if __name__ == "__main__":
    import doctest
    doctest.testmod()