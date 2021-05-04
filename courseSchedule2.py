def findOrder(numCourses, prerequisites):
    """
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
    You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
    Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

    >>> findOrder(1, [])
    [0]

    >>> findOrder(2, [[1,0]])
    [0, 1]

    >>> findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
    [0, 1, 2, 3]


    """    
    pre_to_course = {i: [] for i in range(numCourses)}
    preq_count = {i: 0 for i in range(numCourses)}
    
    for child, parent in prerequisites:
        pre_to_course[parent].append(child)
        preq_count[child] += 1
        
    q = []
    course_order = []
    for course in preq_count:
        if preq_count[course] == 0:
            q.append(course)
            course_order.append(course)

    while q:
        curr = q.pop(0)
        for child in pre_to_course[curr]:
            preq_count[child] -= 1
            if preq_count[child] == 0:
                q.append(child)
                course_order.append(child)
                
    if len(course_order) == numCourses:
        return course_order
    return []

if __name__ == "__main__":
    import doctest
    doctest.testmod()  