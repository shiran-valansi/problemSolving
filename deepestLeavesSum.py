from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        """
        Given a binary tree, return the sum of values of its deepest leaves.
        """
        # need to know the level of the deapest leaves
        nodes_by_level = defaultdict(list)
        max_level = 0
        
        q = [[root,1]]
        
        while len(q) > 0:
            curr, level = q.pop(0)
            max_level = max(level, max_level)
            nodes_by_level[level].append(curr.val)
            if curr.left:
                q.append([curr.left, level+1])
            if curr.right:
                q.append([curr.right, level+1])
             
        return sum(nodes_by_level[max_level])
        