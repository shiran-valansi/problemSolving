def canVisitAllRooms(rooms):
    """
    There are N rooms and you start in room 0.  
    Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 
    A key rooms[i][j] = v opens the room with number v.
    All the rooms start locked (except for room 0). 
    You can walk back and forth between rooms freely.

    Return true if and only if you can enter every room.

    >>> canVisitAllRooms([[1,3],[3,0,1],[2],[0]])
    False

    >>> canVisitAllRooms([[1],[2],[3],[]])
    True

    """
    ##### BFS #####    
    q = [0]
    visited = {0}

    while q:
        curr = q.pop(0)
        for child in rooms[curr]:
            if child in visited:
                continue
            visited.add(child)
            q.append(child)

    return len(visited) == len(rooms)

def canVisitAllRoomsDFS(rooms):
    """
    >>> canVisitAllRoomsDFS([[1,3],[3,0,1],[2],[0]])
    False

    >>> canVisitAllRoomsDFS([[1],[2],[3],[]])
    True

    """
    ##### DFS #####    
    visited = {0}
    
    def dfs(curr):
        
        if len(visited) == len(rooms):
            return True
        
        for child in rooms[curr]:
            if child in visited:
                continue
            visited.add(child)
            dfs(child)
    
    return dfs(0) or len(visited) == len(rooms) 
        



if __name__ == "__main__":
    import doctest
    doctest.testmod()