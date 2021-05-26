def partition(s):
    """
    Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
    A palindrome string is a string that reads the same backward as forward.

    >>> partition("aab")
    [['a', 'a', 'b'], ['aa', 'b']]
    
    >>> partition("a")   
    [['a']]

    >>> partition("aaaa")
    [['a', 'a', 'a', 'a'], ['a', 'a', 'aa'], ['a', 'aa', 'a'], ['a', 'aaa'], ['aa', 'a', 'a'], ['aa', 'aa'], ['aaa', 'a'], ['aaaa']]

    """
        
    all_partitions = []
    get_parts(s, [], all_partitions)
    return all_partitions
        
        
def get_parts(s, curr, all_partitions):
    
    if len(s) == 0:
        all_partitions.append(curr)
        return
    
    for j in range(len(s)):
        if is_pal(s[:j+1]): 
            get_parts(s[j+1:], curr + [s[:j+1]],all_partitions)


def is_pal(word):
    return word == word[::-1]
    
if __name__ == "__main__":
    import doctest
    doctest.testmod() 