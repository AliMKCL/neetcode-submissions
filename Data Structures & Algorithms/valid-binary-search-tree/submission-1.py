import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Cover all cases / branches --> DFS
        
        if not root:
            return True
        
        return self.isValid(root, -math.inf, math.inf)
    
    def isValid(self, root: Optional[TreeNode], lower:int, upper:int) -> bool:
        
        if not root:
            return True

        if not (lower < root.val < upper):
            return False
        
        return (self.isValid(root.left, lower, root.val) and self.isValid(root.right, root.val, upper))
