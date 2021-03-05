def threeSum(nums, target):
    """
    given an array of numbers, return all unique triplets that sum up to target

    >>> threeSum([-1,0,1,2,-1,-4], 0)
    [[-1,-1,2],[-1,0,1]]


    """

    sum_list = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        sum_list += getNumsTwoPointer(nums[i+1:], nums[i], target)

    return sum_list

def getNumsTwoPointer(nums, first, target):

    l = 0
    r = len(nums)-1
    combinations = []
    while l < r:
        if first + nums[l] + nums[r] > target:
            r -= 1
        elif first + nums[l] + nums[r] < target:
            l += 1
        else:
            combinations.append([first, nums[l], nums[r]])
            l += 1
            while l < r and nums[l] == nums[l-1]:
                l += 1
    return combinations 

print(threeSum([-1,0,1,2,-1,-4], 0))
print(threeSum([-1,0,1,2,-1,-4], -2))
print(threeSum([-1,0,2,2,-2,-2, 0], 0))