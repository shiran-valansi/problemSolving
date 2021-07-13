from collections import defaultdict

class Node:
    
    def __init__(self, key=None, val=None, freq = 0, next=None, prev=None):
        self.key = key
        self.val = val
        self.freq = freq


class LFUCache:
    """ 
        Implement LFU cache. If there is a frequency tie, remove item by LRU  
        Runtime for get/ put should be O(1)
        
    """


    def __init__(self, capacity: int):
        """ 
            We will use 2 dictionaries
            1- cache- key to node, for quick look up. Node definition above
            2- freq to LRU of nodes, to maintaine LRU within the same frequency
            We will also keep track of our minimum freq in order to implement LFU
        
        """
        self.cap= capacity
        self.cache = {}
        self.freq_to_nodes = defaultdict(LRUCache)
        self.min_freq = 0
        

    def get(self, key: int) -> int:
        
        if key in self.cache:
            
            node = self.cache[key]
            self.remove_by_node(node)
            node.freq += 1
            self.add(node)
            
            return self.cache[key].val
            
        return -1
        
        

    def put(self, key: int, value: int) -> None:
        
        if self.get(key) == -1:
            
            if self.cap <= 0:
                return
            
            if len(self.cache) == self.cap:
                self.remove_by_freq(self.min_freq)
                
            node = Node(key, value, 1)
            self.min_freq = 1
            
        else:
            node = self.cache[key]
            node.val = value
        
        self.add(node)

        
    def remove_by_freq(self, freq):

        key, val = self.freq_to_nodes[freq].pop_lru()
        self.remove_node(key, freq)

            
    def remove_by_node(self, node):
        del self.freq_to_nodes[node.freq].cache[node.key]
        self.remove_node(node.key, node.freq)
        

    def remove_node(self, key, freq):
        del self.cache[key]
        self.adjust_freq_if_needed(freq)
            
            
    def adjust_freq_if_needed(self, freq):
        if len(self.freq_to_nodes[freq].cache) == 0:
            if self.min_freq == freq:
                self.min_freq += 1
     
    
    def add(self, node):
        self.freq_to_nodes[node.freq].put(node.key, node.val)
        self.cache[node.key] = node
    
        
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity=float('inf')):
        self.cache = OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key, last=True)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if self.get(key) == -1:
            
            if self.capacity == len(self.cache):
                self.cache.popitem(last=False)
            
        self.cache[key] = value
            
    
    def pop_lru(self):
        return self.cache.popitem(last=False)
        

["LFUCache","put","get"]
[[0],[0,0],[0]]
cache = LFUCache(0)
cache.put(0,0)
print(cache.get(0))


tasks = ["put","put","get","put","get","get","put","get","get","get"]
items = [[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
expected = [None,None,1,None,-1,3,None,-1,3,4]
cache = LFUCache(2)

results = []
for task, item in zip(tasks, items):
    if task == 'put':
        results.append(cache.put(item[0], item[1]))
    if task == 'get':
        results.append(cache.get(item[0]))

for expect, result in zip(expected, results):
    assert(expect == result)

print(results)