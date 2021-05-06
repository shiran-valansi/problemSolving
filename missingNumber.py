def missingNumber(nums):
    """
    Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
    Implement a solution using only O(1) extra space complexity and O(n) runtime complexity

    >>> missingNumber([3,0,1])
    2

    >>> missingNumber([0,1])
    2

    >>> missingNumber([9,6,4,2,3,5,7,0,1])
    8

    >>> missingNumber([0])
    1


    """
    n = len(nums)
    target = (n * (n+1) )//2
    sum_nums = sum(nums)
    
    return target - sum_nums

if __name__ == "__main__":
    import doctest
    doctest.testmod()    