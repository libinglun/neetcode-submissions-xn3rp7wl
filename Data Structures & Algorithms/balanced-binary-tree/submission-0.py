# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        def height(node):
            if not node:
                return 0
            lefth = height(node.left)
            righth = height(node.right)
            if abs(lefth - righth) > 1:
                self.ans = False
            return max(lefth, righth) + 1
        
        height(root)
        return self.ans
        