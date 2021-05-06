from collections import deque
def sortedSquares(nums):
    """
    Given an integer array nums sorted in non-decreasing order, 
    return an array of the squares of each number sorted in non-decreasing order.
    Do this in O(n) time

    >>> sortedSquares([-4,-1,0,3,10])
    [0, 1, 9, 16, 100]


    >>> sortedSquares([-7,-3,2,3,11])
    [4, 9, 9, 49, 121]


    """
    # with 2 pointers - non trivial
    # always push the largest abs number into the new array, from the left 
    # this will be the largest abs number in nums
    
    new_nums = deque()
    right = len(nums)-1
    left = 0
    
    while left <= right:
        
        if abs(nums[right]) > abs(nums[left]):
            new_nums.appendleft(nums[right]**2)
            right -= 1
        else:
            new_nums.appendleft(nums[left]**2)
            left += 1

    return list(new_nums)

if __name__ == "__main__":
    import doctest
    doctest.testmod()    