def mergeIntervals(intervals):
        
    intervals.sort()        
    merged = []
    start = intervals[0][0]
    end = intervals[0][1]
    
    for interval in intervals[1:]:
        if interval[0] > end:
            merged.append([start, end])
            start = interval[0]
            end = interval[1]
            
        else: 
            # merge
            if interval[1] > end:
                end = interval[1]
    
    merged.append([start, end])
    print(merged)
    return merged

mergeIntervals([[1,3],[2,6],[8,10],[9, 10], [15,18]])
mergeIntervals([[1,4],[4,5]])