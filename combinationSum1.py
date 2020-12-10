
# Given a collection of candidate numbers and a target number, 
# find all unique combinations in candidates where the candidate numbers sum to target.
# The same number may be chosen from candidates an unlimited number of times


def combinationSum(candidates, target):
        
    all_combos = []
    candidates.sort() #nlogn
    
    def getCombos(path, index, target):
        
        if index >= len(candidates):
            return
        
        if target == 0:
            all_combos.append(path)
            
            
        for i in range(index, len(candidates)): 
            
            if candidates[i] > target:
                return
            
            getCombos(path + [candidates[i]], i, target-candidates[i])
                            
            
    getCombos([], 0, target)
    return all_combos



nums = [2,7,6,3,5,1]
target = 9
print(combinationSum(nums, target))