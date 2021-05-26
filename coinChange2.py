# This function uses only O(n) space rather than O(n*m)
def change(amount, coins):
    """
    You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
    Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
    You may assume that you have an infinite number of each kind of coin.

    >>> change(10, [1,2,5])
    10

    >>> change(5, [1,2,5])
    4


    """
        
    # Less Space
    # we only look one row back each time, so we can just use a single array
    dp = [0]* (amount+1)
    dp[0] = 1
    
    for coin in coins:
        for j in range(coin, amount+1):
            dp[j] += dp[j- coin]
            
    return dp[-1]
        

def change1(amount, coins):
    """
    This was the first draft- using 2d array

    >>> change1(10, [1,2,5])
    10

    >>> change1(5, [1,2,5])
    4
    """
        
    # dp[i][j] = how many combinations can we make amount j out of the first i coins
        
    dp = [[0]* (amount+1) for i in range(len(coins)+1)]
    for r in range(len(coins)+1):
        dp[r][0] = 1
    
    for r in range(1, len(coins)+1):
        
        for c in range(amount+1):
            if c - coins[r-1] >= 0:
                new = dp[r][c - coins[r-1]]
            else:
                new = 0
            dp[r][c] = dp[r-1][c] + new
            
    return dp[-1][-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()  