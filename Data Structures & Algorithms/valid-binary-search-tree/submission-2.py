import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        first = root

        return self.isValid(-math.inf, math.inf, root)

    def isValid(self, lower, upper, root:Optional[TreeNode]) -> bool:
        # Covers the case where a leaf has no left or right --> Auto true 
        # (since its val already satisfies the constraints)
        if not root:    
            return True
        
        if not lower < root.val < upper:
            return False
        
        # And allows returned False and True's to bubble up to effect the final answer.
        return (self.isValid(lower, root.val, root.left) and self.isValid(root.val, upper, root.right))