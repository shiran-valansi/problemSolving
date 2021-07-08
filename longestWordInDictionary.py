from collections import defaultdict
def longestWord(words):
    """
    Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

    If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

    Example:
    Input: words = ["w","wo","wor","worl","world"]
    Output: "world"
    Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

    >>> longestWord(["w","wo","wor","worl","world"])
    'world'

    >>> longestWord(["a","banana","app","appl","ap","apply","apple"])
    'apple'

    >>> longestWord(["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"])
    'yodn'

    """
    #BRUTE FORCE - shorter code + less space + no sorting
    
    # for each word, find all prefixes and check if they all are in words
                
    words_set = set(words)
    max_word = ''
    
    for word in words:
        if len(word) > len(max_word) or (len(word) == len(max_word) and word < max_word):
            if has_all_prefixes(word, words_set):
                max_word = word       
            
    return max_word

    
def has_all_prefixes(word, words_set):
    
    for end in range(len(word)):
        if word[:end+1] not in words_set:
            return False
            
    return True
        
if __name__ == "__main__":
    import doctest
    doctest.testmod() 