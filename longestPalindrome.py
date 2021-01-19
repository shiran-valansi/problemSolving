def longestPalindrome(s):
    """
    Given a string s, return the longest palindromic substring in s.

    >>> longestPalindrome("babad")
    'bab'

    >>> longestPalindrome("cbbd")
    'bb'

    >>> longestPalindrome("a")
    'a'

    >>> longestPalindrome("abbcccbbbcaaccbababcbcabca")
    'bbcccbb'
    """
        
    n = len(s)
    dp = [[False]*n for i in range(n)]
    
    if len(s) < 1:
        return s
    
    max_len = 1
    max_word = s[0]
    
    
    # base case- strings of length 1 and 2
    for i in range(n):
        dp[i][i] = True
        
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            max_len = 2
            max_word = s[i:i+2]
            
    length = 3
    while length <= n:
        start = 0
        end = start + length -1
        while end < n:
            if dp[start+1][end-1] and s[start] == s[end]:
                dp[start][end] = True
                if length > max_len:
                    max_len = length
                    max_word = s[start:end+1]
            start += 1
            end += 1
            
        length += 1
        
        
    # print(dp)
                
    return max_word

if __name__ == "__main__":
    import doctest
    doctest.testmod()