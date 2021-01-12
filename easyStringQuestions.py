def isPalindrome(s):
    """
    Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
    >>> isPalindrome("A man, a plan, a canal: Panama")
    True

    >>> isPalindrome("race a car")
    False

    >>> isPalindrome("123f")
    False
    """
    
    string_without_spaces = ''
    for char in s:
        if char.isalnum():
            string_without_spaces = string_without_spaces + char
    string_without_spaces = string_without_spaces.lower()
    return string_without_spaces == string_without_spaces[::-1]


def isAnagram(s, t):
    """
    >>> isAnagram( "anagram", "nagaram")
    True

    >>> isAnagram("rat", "car")
    False

    """
    def get_freq_dict(s):
        freq_dict = {}
        for char in s:
            freq_dict[char] = freq_dict.get(char, 0) + 1
        return freq_dict
    
    if len(s) != len(t):
        return False
    freq_dict_s = get_freq_dict(s)
    freq_dict_t = get_freq_dict(t)
    
    for char in freq_dict_s:
        if char in freq_dict_t and freq_dict_t[char] == freq_dict_s[char]:
            continue
        return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()