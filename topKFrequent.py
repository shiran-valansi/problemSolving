def topKFrequent(nums, k):
    """
    Given a non-empty array of integers, return the k most frequent elements.

    >>> topKFrequent([1,1,1,2,2,3], 2)
    [1, 2]

    >>> topKFrequent([1], 1)
    [1]

    """
    
    freq_dict = get_freq_dict(nums)
    
    nums_sorted_by_freq = sorted(freq_dict, key=freq_dict.get, reverse=True)
    return nums_sorted_by_freq[:k]

def get_freq_dict(nums):
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
            
        return freq_dict

if __name__ == "__main__":
    import doctest
    doctest.testmod()