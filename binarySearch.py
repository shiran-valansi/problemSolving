
def binary_search(arr, target):
    """
    Returns the index of the target in arr or None if the target is not in arr

    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) //2
        print("left, right, mid: ", left, right, mid)
        if arr[mid] == target:
            return mid
        if target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return None

def test_binary_search():

    arr = [0,1, 2, 3, 4]
    print(binary_search(arr, 3))
    arr = [0,1, 2, 3, 4, 5]
    print(binary_search(arr, 3))
    print(binary_search(arr, 3.5))


def binary_search_2(arr, target):
    """
    Returns the index where target should be placed in arr.
    For output i, we will place target between i-1 and i

    """
    left = 0
    right = len(arr) - 1
    print("*****")
    print(arr)    
    while left <= right and left >=0:
        mid = (left + right) //2
        # print("left, right, mid: ", left, right, mid)

        if arr[mid] == target:
            return mid
        if target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    # print("left, right, mid: ", left, right, mid)
    return  left 

def test_binary_search_2():

    arr1 = [0,1, 2, 3, 4]
    print(binary_search_2(arr1, 3))
    arr2 = [0,1, 2, 3, 4, 5]
    print(binary_search_2(arr2, 3))

    print(binary_search_2(arr1, 3.5))
    print(binary_search_2(arr2, 3.5))

    print(binary_search_2(arr1, 10))
    print(binary_search_2(arr2, 10))

    print(binary_search_2(arr1, -5))
    print(binary_search_2(arr2, -5))


def place_target(arr, target):

    index = binary_search_2(arr, target)

    arr.insert(index, target) 
    print("new array:", arr)

def test_place_target():

    arr1 = [0,1, 2, 3, 4]
    arr2 = [0,1, 2, 3, 4, 5]
    place_target(arr1, 3.5)
    place_target(arr2, 3.5)

    arr1 = [0,1, 2, 3, 4]
    arr2 = [0,1, 2, 3, 4, 5]
    place_target(arr1, 10)
    place_target(arr2, 10)

    arr1 = [0,1, 2, 3, 4]
    arr2 = [0,1, 2, 3, 4, 5]
    place_target(arr1, -5)
    place_target(arr2, -5)

test_place_target()