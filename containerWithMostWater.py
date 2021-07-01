def maxArea(height):
    """
    Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
    Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

    >>> maxArea([1,8,6,2,5,4,8,3,7])
    49

    >>> maxArea([1,1])
    1

    >>> maxArea([4,3,2,1,4])
    16

    >>> maxArea([1,2,1])
    2

    """
    
    # 2 pointers- start with the two edges
    # move the edges inwards according to which one is shorter
    # if the left edge is shorter, increment it and calculate the new area
    
    left = 0
    right = len(height)-1
        
    max_area = 0
    
    while left < right:
        area = (right - left) * min(height[right], height[left])
        max_area = max(max_area, area)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

if __name__ == "__main__":
    import doctest
    doctest.testmod()