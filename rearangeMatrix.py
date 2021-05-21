import time

def rearrangeOnDiagonals(a, corner):
    """
    Given a 2d array, and a number corner, rearrange the elements of the array in the following way:
    if the original array look like this:
    1,2,3
    4,5,6
    7,8,9

    if corner = 1:    if corner = 2:   if corner = 3:   if corner = 4:
    1,3,6             4,2,1            9,7,4            6,8,9 
    2,5,8             7,5,3            8,5,2            3,5,7
    4,7,9             9,8,6            6,3,1            1,2,4


    >>> rearrangeOnDiagonals([[1,2,3],[4,5,6],[7,8,9]], 1)
    [[1, 3, 6], [2, 5, 8], [4, 7, 9]]

    >>> rearrangeOnDiagonals([[1,2,3],[4,5,6],[7,8,9]], 2)
    [[4, 2, 1], [7, 5, 3], [9, 8, 6]]

    >>> rearrangeOnDiagonals([[1,2,3],[4,5,6],[7,8,9]], 3)
    [[9, 7, 4], [8, 5, 2], [6, 3, 1]]

    >>> rearrangeOnDiagonals([[1,2,3],[4,5,6],[7,8,9]], 4)
    [[6, 8, 9], [3, 5, 7], [1, 2, 4]]


    >>> rearrangeOnDiagonals([[1,2,3],[4,5,6],[7,8,9], [1,2,3], [4,5,6]], 1)
    [[1, 3, 6], [2, 5, 9], [4, 8, 3], [7, 2, 5], [1, 4, 6]]

    >>> rearrangeOnDiagonals([[1,2,3,4,5], [6,7,8,9,1], [2,3,4,5,6]], 1)
    [[1, 3, 6, 9, 3], [2, 5, 8, 2, 5], [4, 7, 1, 4, 6]]

    """
    # start = time.time()
    # print("-----Start-----")
    # printMatrix(a)

    order = get_original_order(a)

    rows = len(a)
    cols = len(a[0])
    
    if corner == 1:
        arrange_one(a, order, rows, cols)
    elif corner == 2:
        arrange_two(a, order, rows, cols)
    elif corner == 3:
        arrange_three(a, order, rows, cols)
    elif corner == 4:
        arrange_four(a, order, rows, cols)
        
    # printMatrix(a)

    # print("time: ", time.time()-start)
    return a


def printMatrix(matrix):
    n = len(matrix)
    for r in range(n):
        print(matrix[r])
    print("---------")


def get_original_order(a):
    order = []
    for r in range(len(a)):
        order.extend(a[r])
        
    return order


def arrange_four(a, order, rows, cols):
    
    j = 0

    for i in range(0, cols):
        r = rows - 1
        c = i
        while r >= 0 and c >= 0:

            a[r][c] = order[j]
            j += 1
            r -= 1
            c -= 1
            
    for i in range(rows-2, -1, -1):
        r = i
        c = cols - 1
        while r >= 0 and c >= 0:
            a[r][c] = order[j]
            j += 1
            r -= 1
            c -= 1


def arrange_three(a, order, rows, cols):

    j = 0

    for i in range(rows-1, -1, -1):
        r = i
        c = cols - 1
        while r < rows and c >= 0:

            a[r][c] = order[j]
            j += 1
            r += 1
            c -= 1
            
    for i in range(cols-2, -1, -1):
        r = 0
        c = i
        while r < rows and c >= 0:
            a[r][c] = order[j]
            j += 1
            r += 1
            c -= 1
    
    
def arrange_two(a, order, rows, cols):

    j = 0

    for i in range(cols-1, -1, -1):
        r = 0
        c = i
        while r < rows and c < cols:

            a[r][c] = order[j]
            j += 1
            r += 1
            c += 1
            
    for i in range(1, rows):
        r = i
        c = 0
        while r < rows and c < cols:
            a[r][c] = order[j]
            j += 1
            r += 1
            c += 1
    
    
def arrange_one(a, order, rows, cols):

    j = 0

    # upper part
    for i in range(0, rows):
        r = i
        c = 0 
        while r >= 0 and c < cols:
            
            a[r][c] = order[j]
            j += 1
            r -= 1
            c += 1

    # bottom part   
    for i in range(1, cols):
        r = rows - 1
        c = i
        
        while r >= 0 and c < cols:
            a[r][c] = order[j]
            j += 1
            r -= 1
            c += 1
    
a = [[1,2,3],[4,5,6],[7,8,9]]   
rearrangeOnDiagonals(a, 4)

a = [[1,2,3],[4,5,6],[7,8,9], [1,2,3], [4,5,6]]   
rearrangeOnDiagonals(a, 4)

a = [[1,2,3,4,5], [6,7,8,9,1], [2,3,4,5,6]]            
rearrangeOnDiagonals(a, 4)

if __name__ == "__main__":
    import doctest
    doctest.testmod()  
