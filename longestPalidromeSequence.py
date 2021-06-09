def longestPalindromeSubseq(s): 
    
    dp = [[1]*len(s) for i in range(len(s))]
    # iterate the matrix by diagonal
    for diagonal in range(len(s)):
        left = 0
        for right in range(diagonal, len(s):)
            
            if s[left] == s[right]:

                if left+1 <= right-1:
                    dp[left][right] = dp[left+1][right-1] + 2 
                elif left+1 == right:
                    dp[left][right] = 2
                
            else:
                dp[left][right] = max(dp[left+1][right], dp[left][right-1])
            
            left += 1 
    
    print(dp)
    return dp[0][-1] 

print(longestPalindromeSubseq("aaaaa"))