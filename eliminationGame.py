# There is a list of sorted integers from 1 to n. Starting from left to right, 
# remove the first number and every other number afterward until you reach the end of the list.

# Repeat the previous step again, but this time from right to left, 
# remove the right most number and every other number from the remaining numbers.

# We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

# Find the last number that remains starting with a list of length n.

# Example:

# Input:
# n = 9,
# 1 2 3 4 5 6 7 8 9
# 2 4 6 8
# 2 6
# 6

# Output:
# 6


def lastRemaining(n):
        
        left_to_right = True
        distance = 1
        first = 1
        
        # each iteration we calculate the first number, which will eventually be the number we are left with
        # either it stays the same, or grows by "distance" amount
        
        while n > 1:
            # the only time the first number doesnt change is if we are right to left with an even amount of numbers
            if left_to_right or n % 2 != 0:
                first += distance
            
            left_to_right = not left_to_right 
            distance *= 2
            n //=2
        return first

print(lastRemaining(9))
print(lastRemaining(10))
print(lastRemaining(11))