from collections import deque

def connect(root):
    """
    You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. 

    Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
    Initially, all next pointers are set to NULL.

    """
    
    if not root:
        return root
    
    curr_level = -1
    q = deque([(root, 0)])
    
    while q:
        node, level = q.popleft()

        if level != curr_level:
            curr_level = level
            prev = None
                
        node.next = prev
            
        if node.right:
            q.append((node.right, level+1))
        if node.left:
            q.append((node.left,level+1))
        prev = node
    
    print_tree(root)
    return root

def print_tree(node):

    q = [(node, 0)]
    l = 0
    while q:
        node, level = q.pop(0)
        if not node:
            continue
        if level != l:
            l = level
            print('\n')
        if node.next:
            print(node.val, '(', node.next.val, ')', end=' ')
        else:
            print(node.val, '(Null)', end=' ')
        q.append((node.left, level+1))
        q.append((node.right, level+1))



# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

connect(root)