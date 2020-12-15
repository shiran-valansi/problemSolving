# Given a string S return the length of the longest substring where each char 
# repeats itself a minimum of k times

def longestSubstring(s, k):
        
    
    def countNonValids(word, k):
        freq = {}
        non_valids = set()
        
        for char in word:
            freq[char] = freq.get(char, 0) + 1
            
        for char in freq:
            if freq[char] < k:
                non_valids.add(char)
                
        return non_valids
    
    
    def longestSubRecurse(word, k):
        
        if k <= 1:
            return len(word)
        
        if len(word) < k:
            return 0

        nonValids = countNonValids(word, k)
            
        for i in range(len(word)):
            
            if word[i] in nonValids:
                return max(longestSubRecurse(word[:i], k), longestSubRecurse(word[i+1:], k))
        
        return len(word)

            
    return longestSubRecurse(s,k)

print(longestSubstring('aaabb', 3))
print(longestSubstring('ababbc', 2))
print(longestSubstring('ababbc', 1))
print(longestSubstring('ababbc', 3))
