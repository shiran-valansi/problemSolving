# Count number of pairs such that their sum is divisable by 60

from collections import defaultdict

def numPairsDivisibleBy60(time):
    
    count = 0
    remainders = defaultdict(list)
    for t in time:
        curr_remainder = t % 60
        remainders[curr_remainder].append(t)
        print(remainders)
    visited = set()
    
    for remainder in remainders:
        if remainder not in visited:
            match = 60 - remainder
            n = len(remainders[remainder])
            if remainder == 30 or remainder == 0:
                count += (n-1) * n //2
            else:
                if match in remainders:
                    count += n * len(remainders[match])
            visited.add(remainder)
            visited.add(match)
        
    return count

print(numPairsDivisibleBy60([30,20,150,100,40]) )
print(numPairsDivisibleBy60([30,20,150,100,40, 60, 60, 60]) )