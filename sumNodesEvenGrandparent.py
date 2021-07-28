############## using parent and grandparent => less memory ############## 


def sumEvenGrandparent1(root):
    """  
    Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

    If there are no nodes with an even-valued grandparent, return 0.
    """

    total = 0    
    
    def dfs(node, parent, grandparent):

        if node is None:
            return 0

        total = dfs(node.left, node, parent)
        total += dfs(node.right, node, parent)

        if grandparent is not None and grandparent.val % 2 ==0:
            total += node.val

        return total

    
    # Dfs while saving the parent and grandparent 
    
    return dfs(root, None, None)


############## keeping track of the path of the dfs ##############
def sumEvenGrandparent2(root):
                
    def dfs(node, path, evens):

    
        if node.left is not None:
            dfs(node.left, path + [node.left.val], evens)

        if len(path) > 2:
            if (path[-3] % 2) == 0:
                evens.append(node.val)

        if node.right is not None:
            dfs(node.right, path + [node.right.val], evens)

    
    # Dfs while saving the path and checking grandparent value each time
    evens = []
    dfs(root, [root.val], evens)
    return sum(evens)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Our tree [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]

root = TreeNode(val=6)
left = TreeNode(val=7)
right = TreeNode(val=8)
root.left = left
root.right = right

left = TreeNode(val=2)
right = TreeNode(val=7)
root.left.left= left
root.left.right = right

left = TreeNode(val=9)
root.left.left.left= left

left = TreeNode(val=1)
right = TreeNode(val=4)
root.left.right.left= left
root.left.right.right = right

left = TreeNode(val=1)
right = TreeNode(val=3)
root.right.left= left
root.right.right = right

right = TreeNode(val=5)
root.right.right.right = right

print(sumEvenGrandparent1(root))
print(sumEvenGrandparent2(root))
