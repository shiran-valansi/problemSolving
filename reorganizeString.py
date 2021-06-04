from collections import Counter
from heapq import heapify, heappush, heappop
import math
def reorganizeString(s):
    """
    Given a string s, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
    If possible, output any possible result.  If not possible, return the empty string.

    >>> reorganizeString("aab")
    'aba'

    >>> reorganizeString("aaab")
    ''

    >>> reorganizeString("bbaaaacc")
    'abacabac'

    """
    
    # using a priority q / max heap we keep track of the letters by frequency
    # the heap implementaation in Python is a min heap, so we will just add the frequencies as negative values in order to work with this
    # each time we will pop the top 2 most (least) frequent letters
    # place them in the results string, and put them back deducting their frequency
    
    char_to_freq = Counter(s)
    max_heap = []
    for char in char_to_freq: 
        if char_to_freq[char] > math.ceil(len(s)/2):
            return ''
        heappush(max_heap, [-char_to_freq[char],char])
        
    word = ''
    while len(word) < len(s):
        freq1, char1 = heappop(max_heap)
        freq2, char2 = heappop(max_heap)
        if freq1 < 0:
            word = word + char1
        if freq2 < 0:
            word = word + char2
        
        heappush(max_heap, [freq1+1,char1])
        heappush(max_heap, [freq2+1, char2])
        
    return word
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()