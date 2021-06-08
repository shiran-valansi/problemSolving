def findSubsequences(nums):
    """
    Given an integer array nums, return all the different possible increasing subsequences of the given array with at least two elements. 

    The given array may contain duplicates, and two equal integers should also be considered a special case of increasing sequence.
    """
    
    all_subs = []
    # get_all_subs(nums, [],all_subs, set())
    get_all_subs_2(nums, [],all_subs)
    return all_subs

    
def get_all_subs(nums, curr_sub, all_subs, visited):
    # only adding subsequences that havent been added yet, using visited
    
    if len(curr_sub) >1 :
        curr_tuple = tuple(curr_sub)
        if curr_tuple not in visited:
            visited.add(curr_tuple)
            all_subs.append(curr_sub)
    
    for i in range(len(nums)):
        
        if len(curr_sub)==0 or curr_sub[-1] <= nums[i]:
            get_all_subs(nums[i+1:], curr_sub+[nums[i]], all_subs, visited)
            


def get_all_subs_2(nums, curr_sub, all_subs):
    # using a 'used' set which is unique to every recursion call
    
    if len(curr_sub) >1 :
        all_subs.append(curr_sub)
    
    used = set()
    for i in range(len(nums)):
        
        if len(curr_sub)==0 or curr_sub[-1] <= nums[i]:
            if nums[i] not in used:
                used.add(nums[i])
                get_all_subs_2(nums[i+1:], curr_sub+[nums[i]], all_subs)

nums = [4,6,7,7]  
print(findSubsequences(nums))
nums = [4,4,3,2,1]  
print(findSubsequences(nums))