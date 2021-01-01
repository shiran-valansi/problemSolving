def gameOfLife(board):
    """
    Do not return anything, modify board in-place instead.
    """
    board_copy = []
    rows = len(board)
    cols = len(board[0])
    for r in range(rows):
        board_copy.append(board[r][:])
        
    for r in range(rows):
        for c in range(cols):
            board[r][c] = deadOrAlive(r, c, board, board_copy, rows, cols)
            
    print(board)
    return 

def deadOrAlive(r, c, board, board_copy, rows, cols):
    live_neighbors_count = count_live_neighbors(r, c, board_copy, rows, cols)
    if board_copy[r][c] == 1:
        if live_neighbors_count == 2 or live_neighbors_count == 3:
            return 1
        if live_neighbors_count < 2 or live_neighbors_count > 3:
            return 0
    if live_neighbors_count == 3:
        return 1
    return 0

def count_live_neighbors(row, col, board_copy, rows, cols):
    count = 0
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if r == row and c == col:
                continue
            if r>=0 and r<rows and c>=0 and c<cols:
                count += board_copy[r][c]
    return count
    



board = [[1,1],[1,0]]      
gameOfLife(board)