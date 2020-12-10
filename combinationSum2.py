
# Given a collection of candidate numbers and a target number, 
# find all unique combinations in candidates where the candidate numbers sum to target.
# The same number cannot appear twice

def combinationSum2(candidates, target):
    
    candidates.sort()
    print("***** ", candidates)
    all_combos = []
    
    def getAllCombos(path, index, target):
                    
        if index > len(candidates):
            return
        
        if target == 0:
            all_combos.append(path)
    
        for i in range(index, len(candidates)):

            if i >index and candidates[i] == candidates[i-1]: 
                continue

            if candidates[i] > target:
                return
            
            # curr item is smaller than target, we will append it to path
            getAllCombos(path+[candidates[i]], i+1, target-candidates[i])
            
    def getAllCombos2(index, target):
        
        if index>=len(candidates) or candidates[index]> target :
            return []
        curr = candidates[index]
        if curr == target:
            return [[curr]]
        
        combos = getAllCombos2(index+1, target-curr)
        
        result = [[curr]+combo for combo in combos]
            
        combos = getAllCombos2(index+1, target)
        
        result.extend(combos)
        
        return result 
    
    # all_combos = getAllCombos2(0, target)
    # print(all_combos)
    # all_combos_set = list_to_set(all_combos)
    # print(all_combos_set)
    # all_combos = set_to_list(all_combos_set)
    
    getAllCombos([],0, target)
    
    return all_combos

#########################################################
def list_to_set(all_combos):
    all_sets = set()
    for combo in all_combos:
        combo_set = tuple(combo)
        all_sets.add(combo_set)
        
    return all_sets
    
def set_to_list(all_combos_set):
    combos_list = []
    for combo in all_combos_set:
        combo_list = list(combo)
        combos_list.append(combo_list)
    return combos_list
    


nums = [2,5,1,1,3]    
print(combinationSum2(nums, 8))