############## O(n) ##############
def nextGreaterElements1(nums):
    """
    Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
    So for nums[-1] the next greater element wil be found by traversing the array from 0 to -2

    The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.
    
    >>> nextGreaterElements1([1,8,-1,-100,-1,222,1111111,-111111])
    [8, 222, 222, -1, 222, 1111111, -1, 1]

    >>> nextGreaterElements1([1,2,3,4,3])
    [2, 3, 4, -1, 4]

    >>> nextGreaterElements1([3,8,4,1,2])
    [8, -1, 8, 2, 3]
    """

    
    results = [0]* len(nums)
    stack = []
    
    # look to the right
    get_next_greater1(nums, results, stack)
    
    # look to the left
    get_next_greater1(nums, results, stack)
    
    return results    
            
    
def get_next_greater1(nums, results, stack):
    
    for i in range(len(nums)-1, -1, -1):

        while stack:
            if nums[stack[-1]] > nums[i]:
                results[i] = nums[stack[-1]]
                break
            else:
                stack.pop(-1)

        if len(stack) == 0:
            results[i] = -1
        
        stack.append(i)




############## O(n^2) ##############
def nextGreaterElements2(nums):
    """
    >>> nextGreaterElements2([1,8,-1,-100,-1,222,1111111,-111111])
    [8, 222, 222, -1, 222, 1111111, -1, 1]

    >>> nextGreaterElements2([1,2,3,4,3])
    [2, 3, 4, -1, 4]

    >>> nextGreaterElements2([3,8,4,1,2])
    [8, -1, 8, 2, 3]
    
    """
        
    n = len(nums)
    results = []
    
    for i, num in enumerate(nums):
                
        # look to the right
        next_greater = get_next_greater(i+1, n, num, nums)
        
        if next_greater == None:
            # look to the left
            next_greater = get_next_greater(0, i, num, nums)
        
        if next_greater == None:
            results.append(-1)
        else:
            results.append(next_greater)
            
    return results    
            
    
def get_next_greater(start, end, num, nums):
    
    while start < end:
        if nums[start] > num:
            return nums[start]
        start += 1
    return None
    

if __name__ == "__main__":
    import doctest
    doctest.testmod() 