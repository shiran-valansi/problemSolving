
def letterCombinations(digits):
    """
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

    >>> letterCombinations("23")
    ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

    >>> letterCombinations("")
    []
    
    """
        
    phone = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    
    
    def backtrack(combo, next_digits, all_combos):
        
        if len(next_digits) == 0:
            all_combos.append(combo)
        
        else:
            curr_digit = next_digits[0]
            for char in phone[curr_digit]:
                backtrack(combo+char, next_digits[1:], all_combos)

        return all_combos
            
    all_combos = []
    if len(digits)<1:
        return all_combos
    return backtrack("", digits, all_combos)

if __name__ == "__main__":
    import doctest
    doctest.testmod()