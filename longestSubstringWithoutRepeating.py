def lengthOfLongestSubstring(s):
    """
    Given a string s, find the length of the longest substring without repeating characters.
    
    >>> lengthOfLongestSubstring("abcabca")
    3

    >>> lengthOfLongestSubstring("abcabbbcadvfer")
    8

    >>> lengthOfLongestSubstring("")
    0

    >>> lengthOfLongestSubstring("aaaaa")
    1
    
    
    """


        
    # keep an index dict of letters
    # sliding window- each time we reach a letter- we check if its already in the dict
    # if yes- promote left index to after that first letter index or keep it in the same place (if left > index)  
    # update right in dictionary
    # increase right index
    
    max_substring = 0
    char_to_index = {}
    left = 0
    right = 0
    
    while right < len(s):
        
        if s[right] in char_to_index: 
            left = max(left, char_to_index[s[right]] + 1)
            
        char_to_index[s[right]] = right    
        right += 1
            
        max_substring = max(max_substring, right - left)
        
    return max_substring
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()