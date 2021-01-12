def isPalindrome(s):
    """
    Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
    >>> isPalindrome("A man, a plan, a canal: Panama")
    True

    >>> isPalindrome("race a car")
    False
    """
    
    string_without_spaces = ''
    for char in s:
        if char.isalpha():
            string_without_spaces = string_without_spaces + char
    string_without_spaces = string_without_spaces.lower()
    return string_without_spaces == string_without_spaces[::-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()