def findWords(board, words):
    """
    Given an m x n board of characters and a list of strings words, return all words on the board.

    Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

    The results should not have repeating words
    """
        
    root = build_trie(words)
    # print(root)
    
    rows = len(board)
    cols = len(board[0])
    all_words = []
    
    for r in range(rows):
        for c in range(cols):
            if board[r][c] in root:
                dfs(board, r, c, root[board[r][c]], {(r,c)}, board[r][c], all_words)

    print(list(set(all_words)))           
    return list(set(all_words))
                    
                    
def dfs(board, r, c, node, visited, word, all_words):
    
    if '*' in node:
        all_words.append(word)

    neighbors = [(r-1, c), (r+1, c), (r, c-1), (r,c+1)]
    for r, c in neighbors:
        if (r,c) not in visited and r>=0 and c>=0 and r< len(board) and c<len(board[0]) and board[r][c] in node:
            visited.add((r,c))
            dfs(board, r, c, node[board[r][c]], visited, word+board[r][c], all_words)
            visited.remove((r,c))
        
        
def build_trie(words):
    
    root = {}
    
    for word in words:
        curr = root
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['*'] = {}
        

    return root

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","e","a","t"]]
words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
findWords(board, words)