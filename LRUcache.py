from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        """ Using Ordered dict """
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            self.promote_to_top_of_cache(key)
            print("from get:", self.cache[key])
            return self.cache[key]
        print("from get: -1")
        return -1

    def put(self, key: int, value):
        if key in self.cache:
            self.promote_to_top_of_cache(key)  
        else:
            self.adjust_capacity_if_needed()
        self.cache[key] = value
        # print("cache: ",self.cache)
        
    def promote_to_top_of_cache(self, key):
        self.cache.move_to_end(key, last=True)

    
    def adjust_capacity_if_needed(self):
        if len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        

obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)

param_1 = obj.get(1)

obj.put(3,3)
param_1 = obj.get(2)
obj.put(4,4)
param_1 = obj.get(1)
param_1 = obj.get(3)
param_1 = obj.get(4)

############### Without Ordered Dict, with doubly linked list + hash map ###############

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


obj = LRUCache2(2)
obj.put(1,1)
obj.put(2,2)

param_1 = obj.get(1)
print(param_1)

obj.put(3,3)
param_1 = obj.get(2)
print(param_1)
obj.put(4,4)
param_1 = obj.get(1)
print(param_1)
param_1 = obj.get(3)
print(param_1)
param_1 = obj.get(4)
print(param_1)
