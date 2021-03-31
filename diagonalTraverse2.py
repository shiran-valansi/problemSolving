from collections import defaultdict

def findDiagonalOrder(nums):
    """
    Given a list of lists of integers, nums, return all elements of nums in diagonal order 
    diagonals are from bottom left to top right.
    Notice that the matrix can have rows of different lengths
    Must work in good time complexity

    >>> findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])
    [1, 4, 2, 7, 5, 3, 8, 6, 9]

    >>> findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]])
    [1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16]

    >>> findDiagonalOrder([[1,2,3],[4],[5,6,7],[8],[9,10,11]])
    [1, 4, 2, 5, 3, 8, 6, 9, 7, 10, 11]

    >>> findDiagonalOrder([[1,2,3,4,5,6]])
    [1, 2, 3, 4, 5, 6]

    """

    diagonal_dict = defaultdict(list)
    rows = len(nums)
    
    # any cell (r,c) that has the same r+c belongs to the same diagonal    
    for r in range(rows):
        for c in range(len(nums[r])):
            diagonal_dict[r + c].append(nums[r][c])
                
    result = []
    for d in diagonal_dict:
        result.extend(diagonal_dict[d][::-1])
    
    return result
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
