def countSubstrings(s):
    """
    Given a string s, return the number of palindromic substrings in it.

    A string is a palindrome when it reads the same backward as forward.
    A substring is a contiguous sequence of characters within the string.

    >>> countSubstrings("abc")
    3

    >>> countSubstrings("aaa")
    6

    >>> countSubstrings("")
    0


    """
    # each time we take one or 2 centers, and see if it counts as a palindrome
    
    count = 0
    for i in range(len(s)):
        count += count_palindrome_sround_center(s, i, i)
        count += count_palindrome_sround_center(s, i, i+1)

    return count
            
def count_palindrome_sround_center(s, left, right):
    
    count = 0
    
    while left >= 0 and right < len(s):
        if s[left] != s[right]:
            break
        count += 1
        left -= 1
        right += 1
    
    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod() 