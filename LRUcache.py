from collections import OrderedDict

################# Using Ordered dict #################

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()


    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        
        if self.get(key) == -1:
            
            if self.cap == len(self.cache):
                self.cache.popitem(last=False)
            
        self.cache[key] = value


############### Implementing Ordered Dict, with doubly linked list + hash map ###############

class Node:
    def __init__(self, key=None, val=None, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache2:

    def __init__(self, capacity: int):
        """ Based on a dictionary where each key is the key, each value is a node with val, next, prev """
        
        self.cap = capacity
        
        self.cache = {}
        
        self.head = Node()
        self.tail = Node()
        
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
       
        if key in self.cache:
            self.move_to_head(self.cache[key])
            return self.cache[key].val
        
        return -1
    
    
    def move_to_head(self, node):
        
        self.remove(node) 
        self.add(node)
        
        
    def add(self, node):
        
        temp = self.head.next
        
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node
        
        self.cache[node.key] = node
        

    def remove(self, node):
        
        prev = node.prev
        new = node.next
        
        prev.next = new
        new.prev = prev
        
        del self.cache[node.key]
    
    
    def remove_least(self):
        self.remove(self.tail.prev)
    
    
    def put(self, key: int, value: int) -> None:
        
        if key not in self.cache:
            if len(self.cache) == self.cap:
                self.remove_least()          
        else:
            node = self.cache[key]  
            self.remove(node)
            
        node = Node(key, value)    
        self.add(node)


if __name__ == "__main__":

    tasks = ["put","put","get","put","get","put","get","get","get"]
    items = [[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]] 
    expected = [None,None,1, None, -1,None, -1, 3,4]
    cache1 = LRUCache(2)
    cache2 = LRUCache2(2)

    results1 = []
    results2 = []

    for task, item in zip(tasks, items):
        if task == 'put':
            results1.append(cache1.put(item[0], item[1]))
            results2.append(cache2.put(item[0], item[1]))
        if task == 'get':
            results1.append(cache1.get(item[0]))
            results2.append(cache2.get(item[0]))

    for expect, result1, result2 in zip(expected, results1, results2):
        assert(expect == result1 == result2)
        
    print(results1)
    print(results2)
    
