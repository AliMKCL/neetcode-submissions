from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        queue = deque([root])
        result = []

        """
        How this works:
            - After a layer is complete (for example node), the resulting queue produces 1 layer.
            - Once that queue is depleted (counted by the for loop, len(queue)), the nodes detected
            in that loop belong to the same layer.
            - After that, the new larger queue holds the next depth layer of nodes.

        """
        while len(queue) > 0:
            level = []
            for i in range(len(queue)): # At the start this is 1 for root
                node = queue.popleft()  # Left is the start
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result