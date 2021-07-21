def insertionSortList(head):
    """Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head."""

    # we will need to keep 3 nodes each time
    # first and next nodes of our original list, prev = dummy node which will be the beginning of the new list
    # Our curr node will be placed between prev and prev.next
    
    dummy_head = ListNode()
    prev = dummy_head 
    
    curr = head
    next = None

    while curr is not None:
        next = curr.next
        
        while prev.next is not None and prev.next.val < curr.val:
            prev = prev.next
        
        curr.next = prev.next
        prev.next = curr
        curr = next
        prev = dummy_head  
    
    
    return dummy_head.next

def print_list(head):

    curr = head
    while curr is not None:
        print(curr.val, '->', end=' ')
        curr = curr.next
    print('None')


# [4,2,1,3]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = ListNode()

    def buildList(self, a):

        # dummy = self.head
        curr = self.head

        for num in a:

            new = ListNode(num)
            curr.next = new
            curr = curr.next

        self.head = self.head.next

    def print_list(self):

        curr = self.head
        while curr is not None:
            print(curr.val, '->', end=' ')
            curr = curr.next

a = [4,0,2,1,-1,3]
my_list = LinkedList()
my_list.buildList(a)
print_list(my_list.head)

new_head = insertionSortList(my_list.head)
print_list(new_head)