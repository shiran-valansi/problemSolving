def singleNonDuplicate(nums):
    """
    You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

    Follow up: Your solution should run in O(log n) time and O(1) space.

    >>> singleNonDuplicate([1,1,2,3,3])
    2

    >>> singleNonDuplicate([1,1,2,3,3,4,4,8,8])
    2

    >>> singleNonDuplicate([3,3,7,7,10,11,11])
    10

    """
    # binary search where each time we search on the odd length part of the array
    # untill we find a number that isnt adjacent to its copy
    
    left = 0
    right = len(nums)-1
    
    while left <= right:
        
        mid = (left + right) // 2
        # mid has a duplicate on the left
        if mid > left and nums[mid-1] == nums[mid]:
            if ((right-mid) % 2)!= 0:
                left = mid+1
            else:
                right = mid - 2
        # mid has a duplicate on the right
        elif mid < right and nums[mid+1] == nums[mid]:
            if ((mid-left) % 2) != 0:
                right = mid-1
                
            else:
                left = mid + 2
        # mid has no duplicates
        else:
            return nums[mid]

if __name__ == "__main__":
    import doctest
    doctest.testmod()