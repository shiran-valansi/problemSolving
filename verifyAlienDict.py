def isAlienSorted( words, order):
    """
    In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

    Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

    >>> isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
    True

    >>> isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz")
    False

    >>> isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")
    False

    """
        
    # for each word check if the word before is smaller

    char_dict = get_char_dict(order)
    prev = words[0]
    for word in words[1:]:
        if not inOrder(prev, word, char_dict):
            return False
        prev = word
    return True
    
def get_char_dict(order):
    char_dict = {}
    for i in range(len(order)):
        char_dict[order[i]] = i
    return char_dict
    
    
def inOrder(smaller, bigger, char_dict):

    i = 0
    while i < len(smaller) and i< len(bigger):
        if char_dict[smaller[i]]  < char_dict[bigger[i]]:
            return True
        if char_dict[ smaller[i]]  > char_dict[bigger[i]]:
            return False
        i += 1
            
    if len(smaller) > len(bigger):
        return False
    return True
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()