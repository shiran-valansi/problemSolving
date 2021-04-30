from collections import defaultdict, deque

def minReorder(n, connections):
    """
    There are n cities numbered from 0 to n-1 and n-1 roads such that there is only one way to travel between two different cities (this network form a tree). 
    The roads are one way.
    Roads are represented by connections where connections[i] = [a, b] represents a road from city a to b.

    This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

    Your task consists of reorienting some roads such that each city can visit the city 0. 
    Return the minimum number of edges changed.

    It's guaranteed that each city can reach the city 0 after reorder.

    >>> minReorder(5, [[1,0],[1,2],[3,2],[3,4]])
    2

    >>> minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]])
    3


    """
    
    # make a directed graph (original) and undirected
    # traverse the undirected starting with 0
    # each time check to see if the node points to the parent in the directed graph
    # if not- add 1 to counter
    
    directed = defaultdict(set)
    undirected = defaultdict(set)
    
    for a,b in connections:
        directed[a].add(b)
        undirected[a].add(b)
        undirected[b].add(a)
    
    def bfs():
        
        count = 0
        q = deque()
        q.append((0, -1))
        visited = set()
        visited.add(0)
        
        while q:
            curr, parent = q.popleft()
            if parent!=-1 and parent not in directed[curr]:
                count += 1
            for child in undirected[curr]:
                if child in visited:
                    continue
                visited.add(child)
                q.append((child, curr))
            
        return count
    
    return bfs()
                
if __name__ == "__main__":
    import doctest
    doctest.testmod()