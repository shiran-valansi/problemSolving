from random import randint

class Solution:

    def __init__(self, w):
        # list of accumulative weights, which represent the upper boundary
        # so for every index i, the probablility of getting i will be 
        # (probs[i]-probs[i-1])// probs[-1]
        
        self.probs = [w[0]]
       
        for i in range(1, len(w)): 
            self.probs.append(self.probs[i-1] + w[i])
            
        self.total = self.probs[-1]
            
       
    def pickIndex(self):
        
        target = randint(1, self.total)
        left = 0
        right = len(self.probs)-1
        
        while left <= right:
            mid = (left + right) //2
            if target == self.probs[mid]:
                return mid
            if target > self.probs[mid]:
                left = mid + 1
            else:
                right = mid - 1
                
        return left
                

# Your Solution object will be instantiated and called as such:
obj = Solution([3,14,1,7])
for i in range(100):
    print(obj.pickIndex(), end=' ')