def exist(board, word):
    """
    Given a board of letters and a string word, return True if we can find word on the board, like a word jumble

    >>> exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
    True

    >>> exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
    True

    >>> exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
    False

    >>> exist([["A","B","C","E"],["S","F","C","S"],["C","B","F","E"]], "ABFSA")
    False

    """
        
    rows = len(board)
    cols = len(board[0])
    visited = set()
    
    for r in range(rows):
        for c in range(cols):
            
            if (r,c) not in visited and board[r][c] == word[0]:
                if dfs(board, r, c, word[1:], {(r,c)}):
                    return True
                visited.add((r,c))
                
    return False

    
def dfs(board, r, c, word, visited):
    
    if len(word) < 1:
        return True
    
    neighbors = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]
    
    for r,c in neighbors:
        
        if (r,c) not in visited and r>=0 and r<len(board) and c>=0 and c<len(board[0]):
            if board[r][c] == word[0]:
                visited.add((r,c))
                if dfs(board, r, c, word[1:], visited):
                    return True
                visited.remove((r,c))
                
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod() 
                
                
                
                