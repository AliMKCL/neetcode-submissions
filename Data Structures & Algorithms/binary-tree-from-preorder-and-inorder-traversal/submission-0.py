# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        hash = {}
        for index, num in enumerate(inorder):
            hash[num] = index
        
    
        self.counter = 0
        def build(left, right) -> TreeNode:
            if left > right:
                return None

            root = TreeNode(preorder[self.counter])
            self.counter += 1

            split_point = hash[root.val]

            root.left = build(left, split_point-1)

            # At this point left's have finished, go 1 right (next in preorder)
            root.right = build(split_point+1, right)
            return root

        return build(0, len(preorder)-1)
            

            



        

