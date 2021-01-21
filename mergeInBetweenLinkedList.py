class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # def print_by_node(self):
    #     curr = self
    #     # print("root:", self.root.val)
    #     while curr:
    #         print(curr.val, "->", end=" ")
    #         curr = curr.next

    #     print("None")

def merge_in_between(list1, a, b, list2):
    
    # get to node a in list1, save that place
    # continue to b in list 1, seperate from the list and save the next node's place
    # put nodes list2 in place
    
    left = list1.root
    i = 0
    while i < a: 
        prev_left = left
        left = left.next
        i += 1    
    # here i = a
    # connect new node and continue traversal
    prev_left.next = list2.root
    
    while prev_left:
        prev = prev_left
        prev_left = prev_left.next
    
    # got to the end of list2
    
    # continue to b in list 1
    while i < b:
        left = left.next
        i += 1
        
    # i = b
    prev.next = left.next
    left.next = None
    
    return list1

class LinkedList:

    def __init__(self):
        self.root = ListNode()

    def build_linked_list(self, lst):
        if len(lst) == 0:
            return
        self.root.val = lst[0]
        curr = self.root
        for value in lst[1:]:
            node = ListNode(value)
            curr.next = node
            curr = curr.next

    def print_linked_list(self):
        curr = self.root
        # print("root:", self.root.val)
        while curr:
            print(curr.val, "->", end=" ")
            curr = curr.next

        print("None")

linked_list1 = LinkedList()
linked_list1.build_linked_list([1,2,3,4,5,6])
linked_list1.print_linked_list()

linked_list2 = LinkedList()
linked_list2.build_linked_list([10,11,12,13,14,15,16])
linked_list2.print_linked_list()

merged_list = merge_in_between(linked_list1, 2, 4, linked_list2)
merged_list.print_linked_list()