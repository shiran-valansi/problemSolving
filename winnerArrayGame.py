# A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). 
# In each round of the game, we compare arr[0] with arr[1], 
# the larger integer wins and remains at position 0 and the smaller integer moves to the end of the array. 
# The game ends when an integer wins k consecutive rounds.
# Return the integer which will win the game.
# It is guaranteed that there will be a winner of the game.


def getWinner(arr, k):
        
    def countWinner(winner, loser, loser_index, win_count, k, arr):
        win_count[winner] = win_count.get(winner, 0) + 1
        if win_count[winner] == k:
            return True
        arr.append(loser)
        arr.pop(loser_index)
        return False
    
    ####### MAIN #######
    win_count = {}
    max_num = max(arr)
    
    while True:
        if arr[0] == max_num:
            return arr[0]
        
        if arr[1] > arr[0]:
            if countWinner(arr[1], arr[0], 0, win_count, k, arr):
                return arr[1]

        else:
            if countWinner(arr[0], arr[1], 1, win_count, k, arr):
                return arr[0]



def getWinnerImprovement(arr, k):

    curr = arr[0]
    curr_wins = 0
    for i in range(1, len(arr)):
        if arr[i] > curr:
            curr = arr[i]
            curr_wins = 0
        curr_wins += 1
        if curr_wins == k:
            return curr
    return curr

arr = [1,25,35,42,68,70]
print(getWinner(arr, 1))
print(getWinnerImprovement(arr, 1))

arr2 = [1,11,22,33,44,55,66,77,88,99]
k2 = 1000000000
print(getWinner(arr2, k2))
print(getWinnerImprovement(arr2, k2))