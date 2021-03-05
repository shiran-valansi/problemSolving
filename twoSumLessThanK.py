def twoSumLessThanK(nums, k):
    """
    Given an array nums of integers and integer k, 
    return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. 
    If no i, j exist satisfying this equation, return -1.
    https://leetcode.com/problems/two-sum-less-than-k/

    >>> twoSumLessThanK([34,23,1,24,75,33,54,8], 60)
    58

    >>> twoSumLessThanK([10,20,30], 15)
    -1

    """
    num_to_index = {}
    
    for i, num in enumerate(nums):
        num_to_index[num] = i
    
    nums.sort()
    
    left = 0
    right = len(nums)-1
    max_sum = -1
    
    while left < right:
        
        if nums[left] + nums[right] < k:
            max_sum = max(max_sum, nums[left] + nums[right])
            left += 1
        else:
            right -= 1
            
    return max_sum


def threeSumSmaller(nums, target):
    """
    Given an array of n integers nums and an integer target, 
    find the number of index triplets i, j, k with 0 <= i < j < k < n 
    that satisfy the condition nums[i] + nums[j] + nums[k] < target.

    >>> threeSumSmaller([-2,-1,0,1,3], 2)
    6

    >>> threeSumSmaller([-2,0,1,3], 2)
    2

    >>> threeSumSmaller([-2,0,1,3], 3)
    3

    >>> threeSumSmaller([], 0)
    0


    """
        
    nums.sort()
    count = 0
    for i in range(len(nums)):
        count += two_sum_smaller(nums[i+1:], nums[i], target-nums[i])
        
    return count
            
def two_sum_smaller(nums, num, target):
    left = 0
    right = len(nums)-1
    count = 0
    
    while left < right:
        if nums[left] + nums[right] < target:
            count += right - left
            left += 1
        else:          
            right -= 1
    
    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()