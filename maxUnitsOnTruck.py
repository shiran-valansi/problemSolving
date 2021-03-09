def maximumUnits(boxTypes, truckSize):
    """
    You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

    numberOfBoxesi is the number of boxes of type i.
    numberOfUnitsPerBoxi is the number of units in each box of the type i.
    You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

    Return the maximum total number of units that can be put on the truck.
    >>> maximumUnits([[1,3],[2,2],[3,1]], 4)
    8

    >>> maximumUnits([[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]], 35)
    76

    >>> maximumUnits([[5,10],[2,5],[4,7],[3,9]],10)
    98


    """
    
    boxTypes.sort(key = lambda i:i[1], reverse=True)
    boxes = 0
    units = 0
    i = 0
            
    while truckSize > 0  and i<len(boxTypes):
        
        count = min(boxTypes[i][0], truckSize)
        
        truckSize -= count
        
        units += count* boxTypes[i][1]
        
        i += 1
        
            
    return units