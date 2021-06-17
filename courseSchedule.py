from collections import defaultdict
def canFinish(numCourses, prerequisites):
    """
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
    You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
    Return true if you can finish all courses. Otherwise, return false.

    >>> canFinish(2, [[1,0]])
    True

    >>> canFinish(2, [[1,0], [0,1]])
    False

    >>> canFinish(8, [[1,0], [1,7], [2,6], [6,4], [7,0], [0,5]])
    True

    """
    
    pre_to_course = defaultdict(list)
    
    for course, pre in prerequisites:
        pre_to_course[pre].append(course)
    
    # In order to not repeat a path or sub-path that we've already visited
    visited = [False for i in range(numCourses)]

    for pre in pre_to_course:

        if visited[pre]:
            continue
        if has_loop_dfs(pre_to_course, pre_to_course[pre], {pre}, visited):
            return False
    
    return True
    
def has_loop_dfs(pre_to_course, courses, path, visited):
    # has to be dfs in order to check for a cycle in the DAG
    
    for c in courses:
        
        if visited[c]:
            continue
            
        if c in path:
            return True
        path.add(c)
        
        if c in pre_to_course and has_loop_dfs(pre_to_course, pre_to_course[c] ,path, visited):
            return True
        
        visited[c] = True
        path.remove(c)
    
    return False
    

if __name__ == "__main__":
    import doctest
    doctest.testmod() 