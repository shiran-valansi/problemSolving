#3. sortByBeauty- divide matrix into small matrices, 
# for each sub matrix find its beauty (=the smallest number bigger than 0 that's not in the sub matrix), 
# place sub matrices back sorted by beauty. (left right up down). 
# if 2 subs have the same beauty, place them back in their original order
#example:
# 1,2
# 4,6
# beauty is 3

#example:
# 1,2,2,3
# 3,4,10,4
# 2,10,1,2
# 5,4,4,5
# size=2
# 2,3,2,10
# 10,4,5,4
# 1,2,1,2
# 4,5,3,4
from collections import defaultdict
def sortByBeauty(matrix, size):

    # sub matrices into a list
    # sort list
    # find missing number
    # beauty to sub matrix dictionary
    # sort dictionary by keys
    # place back in matrix

    n = len(matrix)
   
    beauty_to_sub = get_beauty_to_sub(n, size, matrix)

    #sort dictionary by keys
    sorted_beauties = sorted(beauty_to_sub)
    print("sorted keys:", sorted_beauties)
    
    beauty_index = 0
      
    for r1 in range(0,n, size):
        for c1 in range(0,n,size):
            i = 0
            sub = beauty_to_sub[sorted_beauties[beauty_index]][0]

            for r in range(r1,r1+size):
                for c in range(c1,c1+size):
                    matrix[r][c] = sub[i]
                    i += 1
            beauty_to_sub[sorted_beauties[beauty_index]].pop(0)
            if len(beauty_to_sub[sorted_beauties[beauty_index]]) < 1:
                beauty_index += 1

    print_board(matrix, n,n )
    return matrix


def get_beauty_to_sub(n, size, matrix):

    beauty_to_sub = defaultdict(list)
    for r1 in range(0,n, size):
        for c1 in range(0,n,size):
            sub = []
            for r in range(r1,r1+size):
                for c in range(c1,c1+size):
                    sub.append(matrix[r][c])

            beauty = get_beauty(sub)
            beauty_to_sub[beauty].append(sub)
    return beauty_to_sub


def get_beauty(sub):

    b = 1
    sorted_sub = sorted(sub)
    for i in range(len(sorted_sub)):
        if sorted_sub[i] > b:
            return b
        if sorted_sub[i] == b:
            b += 1

    return b

def print_board(board, rows, cols):
    for r in range(rows):
        for c in range(cols):
            print(board[r][c], end="    ")
        print("")

matrix = [[1,2,2,3],
[3,4,10,4],
[2,10,1,2],
[5,4,4,5]]

sortByBeauty(matrix, 2)

















