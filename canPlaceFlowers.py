def canPlaceFlowers(flowerbed, n):
    """
    Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, 
    return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

    >>> canPlaceFlowers([1,0,0,0,1], 1)
    True

    >>> canPlaceFlowers([1,0,0,0,1], 2)
    False

    """
    
    if n == 0:
        return True
    i = 0
    while i < len(flowerbed) and n>0:
        if flowerbed[i] == 0:
            n = check_adjacents(i, flowerbed, n)
        # print(i, n, flowerbed)
        i += 1
                
    return n == 0    

def check_adjacents(i, flowerbed, n):
    
    # check for 3 zeros or 2 zeros if we are on the edges
    if (i == 0 and i+1 < len(flowerbed) and flowerbed[i+1] == 0) or (i == len(flowerbed)-1 and flowerbed[i-1] == 0) or (flowerbed[i-1] == 0 and i+1<len(flowerbed) and flowerbed[i+1] == 0):
        flowerbed[i] = 1
        n -= 1
    return n


if __name__ == "__main__":
    import doctest
    doctest.testmod()