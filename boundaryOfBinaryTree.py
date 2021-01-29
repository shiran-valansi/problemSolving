# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        
        if root is None:
            return root
        if self.is_leaf(root):
            return [root.val]
        
        left_bound = []
        right_bound = []
        leaves = []
        
        self.get_left(root.left, left_bound)
   
        self.get_right(root.right, right_bound)
    
        self.get_leaves(root, leaves)
        
        boundary = [root.val] + left_bound + leaves + right_bound[::-1]
        return boundary
        
        
    def get_right(self, root, right_bound):
        
        if root is None or self.is_leaf(root):
            return
        right_bound.append(root.val)
        
        if root.right:
            self.get_right(root.right, right_bound)
        else:
            self.get_right(root.left, right_bound)
        
        
    def get_left(self, root, left_bound):
        
        if root is None or self.is_leaf(root):
            return
        left_bound.append(root.val)
        
        if root.left:
            self.get_left(root.left, left_bound)
        else:
            self.get_left(root.right, left_bound)
            
               
    def is_leaf(self, node):
        return node.left is None and node.right is None

        
    def get_leaves(self, root, leaves): 
        
        if root is None:
            return
        if self.is_leaf(root):
            leaves.append(root.val)

        self.get_leaves(root.left, leaves)
        self.get_leaves(root.right, leaves)
                
    