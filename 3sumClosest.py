def threeSumClosest(nums, target):
    """

    >>> threeSumClosest([-1,2,1,-4], 1)
    2

    >>> threeSumClosest([-1,2,1,-4,0,-2], 1)
    1

    """
        
    nums.sort()
    closest = float('inf')
    
    for i in range(len(nums)):
        temp_closest = nums[i] + get_two_sum_closest(nums[i+1:], target-nums[i])    
        if target == temp_closest:
            return temp_closest
        if abs(target - temp_closest) < abs(target - closest):
            closest = temp_closest
    
    return closest
            
            
def get_two_sum_closest(a, target):

    closest = float('inf')
    
    left = 0
    right = len(a) - 1
    
    while left < right:
        
        if a[left] + a[right] == target:
            return a[left] + a[right]
    
        else:
            if abs(target - (a[left] + a[right] )) < abs(target - closest):
                closest = a[left] + a[right] 
            if a[left] + a[right] > target:
                right -= 1
            else:
                left += 1
      
    return closest


if __name__ == "__main__":
    import doctest
    doctest.testmod() 