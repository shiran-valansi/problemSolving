def climb_stairs_brute_force(n):
    """
    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    """
        
    #Brute force
    def climb_stairs_recurse(i,n):
        
        if i > n:
            return 0
        if i == n:
            return 1
        
        return climb_stairs_recurse(i+1,n) + climb_stairs_recurse(i+2,n)

    return climb_stairs_recurse(0, n)
        

def climb_stairs_memoization(n):

    def climb_stairs_recurse(i,n, memo):

        if i > n:
            return 0
        if i == n:
            return 1

        if memo[i] > 0:
            return memo[i]

        memo[i] = climb_stairs_recurse(i+1,n, memo) + climb_stairs_recurse(i+2,n, memo)

        return memo[i]

    memo = [0]*(n+1)
    
    return climb_stairs_recurse(0, n, memo)
        
        
def climb_stairs_dynamic_programing(n):

    dp = [1,2]
    
    for i in range(2,n):
        new = dp[i-1] + dp[i-2]
        dp.append(new)
    return dp[n-1]
    
       
def climb_stairs_fibonacci_const_space(n):

    if n == 1:
        return 1
    if n == 2:
        return 2
    
    first = 1
    second = 2
    
    for i in range(3,n+1):
        fib = first + second
        first = second
        second = fib
        
    return fib
        
    
n = 5
print(climb_stairs_brute_force(n))
print(climb_stairs_memoization(n))
print(climb_stairs_dynamic_programing(n))  
print(climb_stairs_fibonacci_const_space(n))
    
    