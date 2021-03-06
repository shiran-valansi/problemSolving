def kClosest(points, k):
    """
    Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
    return the k closest points to the origin (0, 0).

    >>> kClosest([[1,3],[-2,2]],1)
    [[-2, 2]]

    >>> kClosest([[3,3],[5,-1],[-2,4]],  2)
    [[3, 3], [-2, 4]]

    """
        
    point_to_distance = get_point_to_distance(points)
    
    points_sorted = sorted(point_to_distance, key=point_to_distance.get)

    points_sorted = [list(points_sorted[i]) for i in range(k)]
    
    return points_sorted
        
        
        
def get_point_to_distance(points):
    
    point_to_distance = {}
    
    for x,y in points:
        d = (x**2 + y**2)**(0.5)
        point_to_distance[(x,y)] = d
        
    return point_to_distance

if __name__ == "__main__":
    import doctest
    doctest.testmod()