from collections import defaultdict

def digitAnagrams(a):

    digit_dict = defaultdict(list)
    count = 0
        
    for i in range(len(a)):   #O(n)
        # for every number we sort it by digit, then turn it into a sorted string 
        num = str(a[i])
        a[i] = sorted(num)
        numStr = ''
        for char in a[i]:
            numStr = numStr + char
        # print(a[i])
        digit_dict[numStr].append(i)
        
    for key in digit_dict.keys():
        l = len(digit_dict[key])
        temp = (l * (l-1))/2
        count += temp
        
    return count
    