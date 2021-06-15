class Node:
    
    def __init__(self, val=None):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """

        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        for i in range(index):
            curr = curr.next
 
        return curr.val
        
    
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)
            

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """

        if index < 0 or index > self.size:
            return -1
        
        new = Node(val)
        
        curr = self.head
        
        if index == 0:
            new.next = curr
            self.head = new
            
        else:
        
            for i in range(index-1):  
                curr = curr.next
            new.next = curr.next
            curr.next = new
            
        self.size += 1
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return 
    
        if index == 0:
            self.head = self.head.next
        
        else:
            curr = self.head    
            for i in range(index-1):
                curr = curr.next

            curr.next = curr.next.next         
        
        self.size -= 1
        
        
    def print_nodes(self):
        
        curr = self.head
        while curr:
            print(curr.val, "->", end=' ')
            curr = curr.next
        print('\n')


# actions = ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
# [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]

obj = MyLinkedList()

obj.addAtHead(7)
obj.addAtHead(2)
obj.addAtHead(1)

obj.print_nodes()

obj.addAtIndex(3,0)
obj.deleteAtIndex(2)

obj.print_nodes()

obj.addAtHead(6)
obj.addAtTail(4)

obj.print_nodes()

param_1 = obj.get(4)

obj.addAtHead(4)

obj.print_nodes()

obj.addAtIndex(5,0)
obj.addAtHead(6)

obj.print_nodes()