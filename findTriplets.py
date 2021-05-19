import time
from collections import defaultdict

def findTheTriples(arr, queries):
    """
    given an array of triplets queries
    find how many occurrences of each query as a subsequence in the given array
    example:
    arr = [1,2,3,4,5]
    queries = [[1,2,4], [2,4,3], [1,1,1]]
    ==> [1,0,0]

    >>> findTheTriples([1,2,3,4,5], [[1,2,4], [2,4,3], [1,1,1], [2,4,5]])
    [1, 0, 0, 1]

    >>> findTheTriples([1,2,2,1,2,1,2], [[1,1,2], [1,2,1]])
    [4, 6]

    >>> findTheTriples([1,1,1,1], [[1,1,1]])
    [4]

    """
    # start = time.time()
    final_count = []
    
    num_to_index = defaultdict(list)
    for i, num in enumerate(arr):
        num_to_index[num].append(i)

    for q in queries:
        count = 0
        if q[0] in num_to_index and q[1] in num_to_index and q[2] in num_to_index:
            for a in num_to_index[q[0]]:
                for b in num_to_index[q[1]]:
                    for c in num_to_index[q[2]]:
                        if a < b < c:
                            count += 1
        final_count.append(count) 

    # print(final_count)
    # print("time: ", time.time()-start)
    return final_count

arr = [1,2,3,4,5]
queries1 = [[1,2,4], [2,4,3], [1,1,1], [2,4,5]]

arr2 = [1,2,2,1,2,1,2]
queries = [[1,1,2], [1,2,1]]

arr3 = [1,1,1,1]
queries = [[1,1,1]]

arr4 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
queries = [[1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1]]
findTheTriples(arr, queries1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()  